---
title: "Agents: Local to Production"
description: Build an AI agent on a local open model, inspect every step, move its tools into an MCP server, and test how its behaviour changes when you swap the model.
---

# Build an AI Agent Locally, Then Test It Like You Mean It

<div class="tutorial-card__header">
  <span class="difficulty-badge difficulty-badge--intermediate">Intermediate</span>
  <span class="time-estimate">~2 hours</span>
</div>

Build a pharmacogene agent on a local open model, watch every step of its loop, move its tools into a separate server, and find out what changes when you swap the model underneath it.

**You need a Mac or Linux machine with at least 16 GB of RAM and about 10 GB of free disk. No cloud account is required for sections 1 to 4. Section 5 uses an Anthropic API key for the hosted comparison.**

The gene data in this tutorial is a three-gene teaching table, not a clinical reference. The agents' answers demonstrate behaviour, not clinical validity.

## 1. Set up (15 minutes)

```bash
brew install uv
brew install --cask gcloud-cli lm-studio
mkdir agents-primer && cd agents-primer
uv venv --python 3.12 && source .venv/bin/activate
uv pip install "google-adk[a2a]>=2.0.0" litellm fastmcp httpx google-auth
adk --version
```

In LM Studio, download `google/gemma-4-e4b` (6.9 GB), turn on Developer Mode, load the model and start the server. It now answers OpenAI-format requests on `http://localhost:1234/v1`. Two settings worth a thought: leave "start on login" off unless you mean to run another always-on service, and skip LM Link (remote model sharing) if you already reach your other machines over SSH.

## 2. Build and test an agent

Every agent framework has the same four parts. Here is the whole thing in one file.

```python
import asyncio, os, sys
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import InMemoryRunner
from google.genai import types

os.environ.setdefault("LM_STUDIO_API_BASE", "http://localhost:1234/v1")
os.environ.setdefault("LM_STUDIO_API_KEY", "lm-studio")

CALLS = []

def lookup_gene_code(gene: str) -> dict:
    """Return the internal workshop code for a gene symbol."""
    CALLS.append(gene)
    return {"gene": gene, "code": f"PKT-{len(gene) * 7919}"}

agent = Agent(
    name="smoke",
    model=LiteLlm(model="lm_studio/google/gemma-4-e4b"),
    instruction="Use the lookup_gene_code tool to answer. Reply with the code only.",
    tools=[lookup_gene_code],
)

async def main():
    runner = InMemoryRunner(agent=agent, app_name="smoke")
    session = await runner.session_service.create_session(app_name="smoke", user_id="u")
    msg = types.Content(role="user", parts=[types.Part(text="What is the code for CYP2D6?")])
    final = ""
    async for ev in runner.run_async(user_id="u", session_id=session.id, new_message=msg):
        if ev.is_final_response() and ev.content and ev.content.parts:
            final = "".join(p.text or "" for p in ev.content.parts)
    expected = f"PKT-{len('CYP2D6') * 7919}"
    ok = bool(CALLS) and expected in final
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1

sys.exit(asyncio.run(main()))
```

1. **Model.** `LiteLlm("lm_studio/google/gemma-4-e4b")`. The prefix picks the provider. Change the string and the same agent runs on another model.
2. **Tools.** Plain Python functions. The framework reads the name, the type hints and the docstring and turns them into a JSON schema. The model never sees your code, only that schema.
3. **Instruction.** The system prompt.
4. **Runner and session.** The runner drives the loop (model asks for a tool, framework runs it, result goes back to the model, model answers). The session is the conversation's memory, held in RAM here and in a database in production.

The test is the part worth copying. It passes only if the tool was called **and** the answer contains a value no model could guess. A test that checks "the agent said something plausible" passes on a hallucination.

**What happens when you break it.** These results are from a real run on 31 October 2026.

- The docstring line does nothing when Python runs the function. It is still the only description of the tool the model receives. You can print exactly what the model sees with `FunctionTool(fn)._get_declaration()`.
- Deleting the docstring did not break it. Replacing it with a lie ("Return the weather for a city") and removing the hint from the instruction did not break it either. The model weighs the name, the parameters and the description together, and `lookup_gene_code(gene: str)` was a strong enough signal on its own. The dangerous case is the reverse: a vague name like `run` or `query`, a misleading description, and twenty tools to choose between. A lying docstring passed this test, which means a test like this would never catch one.
- Three runs gave three answer formats: the bare code, a sentence, and once the model's own reasoning followed by the code. The instruction said "reply with the code only". Small models follow format instructions loosely. If the format matters, enforce it in code.

## 3. Watch the loop in the ADK web UI

ADK ships a web interface that shows every event. It needs one folder per agent, an `agent.py`, and a variable named exactly `root_agent`.

```
lesson2/gene_agent/__init__.py   ->  from . import agent
lesson2/gene_agent/agent.py      ->  root_agent = Agent(..., tools=[lookup_gene, list_genes])
```

```bash
cd lesson2 && adk web --port 8000
```

Give the agent two tools over three pharmacogenes (CYP2D6, CYP2C19, DPYD), so the model has to choose. Three findings from the reference run:

- **Session memory changes the path.** Asked about BRCA1 after an earlier "which genes do you know?", the model answered correctly without calling any tool, because the gene list was already in the conversation.
- **The stated reasoning is not a record of the action.** In that same turn, its thought said "I should first try to see if BRCA1 is in my known gene list". It never called the tool. Audit the event log, not the narration.
- **A structured negative makes honesty easy.** In a fresh session it called `lookup_gene("BRCA1")`, received `{"status": "not_found"}` and said it did not know. Design every tool to say no explicitly.

One hidden detail: the thought quoted "You are an agent. Your internal name is 'gene_agent'. The description about you is...". ADK builds that sentence from the agent's `name` and `description` and adds it to the system prompt. Those fields are prompt text, not labels.

## 4. Move the tools into an MCP server

The Model Context Protocol puts tools in their own server, so any client (ADK, Claude Code, Claude Desktop, Cursor) can use them.

```python
from fastmcp import FastMCP
mcp = FastMCP("gene-server")

@mcp.tool
def lookup_gene(gene: str) -> dict:
    """Look up a pharmacogene: its chromosome and what it does."""
    ...

if __name__ == "__main__":
    mcp.run()   # stdio transport
```

The agent changes in one place:

```python
tools=[McpToolset(connection_params=StdioConnectionParams(
    server_params=StdioServerParameters(command=sys.executable, args=["gene_server.py"])))]
```

From the model's side nothing changes: the events are identical. In the graph view the two named tools become one `McpToolset` box, because the agent now discovers its tools at runtime.

**Try this: add a gene while the UI is running.** In the reference run, TPMT was added to the server, the file saved, a new session opened and the question asked. The agent called the tool, got a clean `not_found` and honestly said it did not know. Every layer behaved correctly and the answer was still wrong, because `adk web` keeps one server process alive across sessions and that process still held the old gene list. After a restart: "TPMT is located on chromosome 6. Its role is to metabolise thiopurines, such as azathioprine." Updating the code is not updating the service. In the cloud this is the old container still serving traffic. It was caught by asking for a value only the new code could produce.

## 5. Swap the model, keep the test

Same agent, same tools, same instruction, four questions. Only the model string changed.

| Question | Gemma 4 e4b (local) | Claude Sonnet 5.5 |
|---|---|---|
| What does DPYD do? | 1 tool call, correct, 3.1 s | 1 tool call, correct, 2.7 s |
| What does BRCA1 do? (not in the tools) | Said not found, 13.7 s | Said not found and listed what it does cover, 3.5 s |
| Which of your genes is on chromosome 10? | `list_genes` then one lookup, correct, 12.1 s | `list_genes` then all three lookups, correct, 4.0 s |
| Is codeine safe for a CYP2D6 poor metaboliser? | **No tool calls.** Answered from training, raw reasoning in the reply | One lookup, said the tool "returned nothing more specific", then answered from its own knowledge |

The Gemini column failed on every question with `API key not valid`, which turned out to be a duplicated key name in my environment file with the stale value first. A configuration bug, not a model result.

The fourth question was built to sit just past the edge of the tools: they know CYP2D6 metabolises codeine and nothing about poor metabolisers. Gemma ignored the tools and the "never guess" instruction, silently. Claude used the tool, said it was not enough, and then gave the clinically correct answer (codeine is generally not recommended for poor metabolisers because it is not converted to morphine and does not work) from its own training. That is more transparent, and still beyond its evidence.

**The swap really is one string. The behaviour is not portable.** Every model change needs the test suite rerun.

## What this tutorial demonstrates

1. **Test with a positive control.** A value only the tool could produce, checked in code.
2. **The tool contract is the name, the parameters and the description together.** Keep them true to the code; nothing else will catch drift.
3. **Return explicit negatives.** `{"status": "not_found"}` makes abstention easy.
4. **Audit events, not thoughts.** The model's narration and its actions can disagree.
5. **A tool server is a running service.** A code change does nothing until the process restarts.
6. **Probe the boundary.** The dangerous agent is not the one that refuses. It is the one that blends tool evidence and memory into one confident clinical answer, with the join invisible. For genomics, give it a tool that holds the guideline, and make it cite which result each claim came from.

These are the questions ClawBio is built around: inspectable execution, evidence you can trace, and refusal when the evidence runs out.
