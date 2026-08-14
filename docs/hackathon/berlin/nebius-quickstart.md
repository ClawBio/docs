---
title: "Nebius Quickstart"
description: Put a Nebius Token Factory model in charge of ClawBio skills in about fifteen minutes. The starting point for every Berlin challenge.
---

# Nebius Quickstart

<div class="tutorial-card__header">
  <span class="difficulty-badge difficulty-badge--beginner">Beginner</span>
  <span class="time-estimate">~15 min</span>
</div>

Do this before you pick a challenge. It is the smallest complete thing that is
genuinely agentic, and everything in the three briefs builds on it.

!!! info "This is the main route for the day"

    A local ClawBio checkout with a Nebius Token Factory model in charge of it. It reaches
    all 95 skills and your own files, and it is verified working end to end.

    Nebius have a hosted one-click agent in preparation which would package this behind a
    deploy button. It is not published to participant accounts yet, so do not wait for it;
    see [Setup](setup.md) for the current state. Nothing on this page depends on it.

## Why this page exists

ClawBio skills are plain Python. 94 of the 95 need no language model at all:
`rare-high-impact-variants` reads a VCF and does arithmetic. You can run every skill
in the library from a terminal, all afternoon, and consume no Nebius credit and build
nothing agentic.

The interesting part is the layer above. An agent reads each `SKILL.md`, decides which
skill answers the question, runs it, reads the output and reports what it found and what
it could not conclude. That agent runs on a model, the model runs on Nebius Token
Factory, and that is where your credits go.

This page wires those two halves together.

## 0. What you need first

Two things, and you very likely have both.

```bash
git --version          # any recent version
python3 --version      # must be 3.11 or newer
```

If either is missing:

=== "macOS"

    ```bash
    xcode-select --install                 # git, if you do not have it
    brew install python@3.12               # python, if yours is older than 3.11
    ```

=== "Linux"

    ```bash
    sudo apt update && sudo apt install -y git python3 python3-venv python3-pip
    ```

=== "Windows"

    Use [Git for Windows](https://git-scm.com/download/win) and
    [python.org/downloads](https://www.python.org/downloads/). Tick **Add python.exe to
    PATH** in the installer. Then run the commands below in Git Bash or PowerShell,
    replacing `python3` with `python`.

**You do not need `uv`, Conda, Docker, or a GPU.** Steps 1 and 2 use nothing but the
Python standard library.

## 1. Get ClawBio

```bash
git clone --depth 1 https://github.com/ClawBio/ClawBio.git
cd ClawBio
```

That is the whole install. ClawBio skills are plain Python, and every skill ships its own
demo data inside the repository, so there is nothing else to download.

## 2. Prove it works, before you have a key

```bash
python3 examples/nebius_agent.py --dry-run
```

**No key, no dependencies, no API call, no spend.** It prints the base URL, the model,
the tools the model will be offered, and then runs one skill locally to prove dispatch
works. You should see a report about rare high-impact variants.

If that prints, your setup is sound, and any later failure is the key or the network
rather than ClawBio. Do this before you arrive: it is the one step that can be done at
home and it is the one that most often eats the first half hour of a hackathon.

## 3. Get a key

Token Factory promo codes are handed out at the venue by QR code, so collect yours at the
door. Redeem it, then create a key at
[tokenfactory.nebius.com/project/api-keys](https://tokenfactory.nebius.com/project/api-keys).

```bash
export NEBIUS_API_KEY=paste-your-key-here
```

On Windows PowerShell that is `$env:NEBIUS_API_KEY = "paste-your-key-here"`.

The key lives in that terminal window only. Open a new tab and you will need to export it
again, which is the usual cause of a sudden `NEBIUS_API_KEY is not set`.

The API is OpenAI-compatible. Base URL `https://api.tokenfactory.nebius.com/v1/`,
authenticated with `Authorization: Bearer <key>`, and it supports native function
calling, which is the feature the whole day depends on.

## 4. Install the one dependency

```bash
python3 -m pip install openai
```

That is the only package needed, and only from here on: the dry run above deliberately
avoids it. If `pip` complains about an externally managed environment, make a virtual
environment first:

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
python3 -m pip install openai
```

## 5. Go live

```bash
python3 examples/nebius_agent.py \
  --ask "Which variants are genuinely rare and high-impact, and which can you not tell?"
```

This is a real run, on 12 August, trimmed only for length:

```
Model    : Qwen/Qwen3-235B-A22B-Instruct-2507
Question : Which variants are genuinely rare and high-impact, and which ones can you not tell either way?

[tool call 1] run_clawbio_skill(skill='rare_high_impact_variants')
             -> 1524 chars, starting '# Rare High-Impact Variants Report'

--- ANSWER ---
1. GENE1 (1:100000 C>T): nonsense, heterozygous, AF = 0.0002 (ultra-rare), ClinVar: Pathogenic
2. GENE7 (7:700000 C>T): splice_acceptor, heterozygous, AF = 0.002 (rare)
3. GENE5 (5:500000 C>G): nonsense, heterozygous, AF = 0.004 (rare)

The variant that cannot be confirmed either way is one high-impact nonsense
variant with no population-frequency data. The report explicitly states that
absence of frequency data is not evidence of rarity, so we cannot determine
if it is rare or common.

Tokens: 962 in, 306 out, over 1 skill call(s).
```

The tool-call line is the point. It is the provenance trail: not "the model said so" but
"the model ran this skill and here is what came back". And note the cost. A complete
question-to-grounded-answer cycle was **1,268 tokens**, so your credits are not the
constraint on what you attempt today.

## 6. Read what it refused to say

The demo genome has six carried annotated variants. Five are high impact. Of those, three
have a documented frequency below the threshold, one is common, and **one has no
population frequency data at all**.

That last variant is the whole event in miniature. Absence of a frequency is not evidence
of rarity, and a pipeline that quietly counts it as rare produces a confident, wrong,
clinically actionable answer. Check whether your agent reported it honestly or swept it
into the rare pile. Weak models sweep.

If it swept, that is not a bug to hide. It is the most interesting slide in your demo.

## 7. Now make it yours

The script is about 200 lines and deliberately small. Three obvious extensions, one per
challenge:

| Challenge | Extension |
|---|---|
| 1. Diagnostic odyssey | Add `cnv_acmg_classifier` to `SKILLS` and ask a question only answerable by combining it with the SNV skills |
| 2. Cancer target | Swap in `target_validation_scorer` and `clinical_trial_finder`, then make the agent argue against its own pick |
| 3. Whose genome fails | Add `gwas_prs`, ask for a percentile, and see whether the agent surfaces `Reference population: EUR` unprompted. Then make it refuse |

Skills are whitelisted in the `SKILLS` dict at the top. That is deliberate: the model
picks from a fixed menu rather than composing a shell command. Keep it that way.

## Choosing a model

**Do not trust the model ID in Nebius's own function-calling documentation.** It is
`meta-llama/Meta-Llama-3.1-8B-Instruct-fast` and it returns a 404: the docs are stale.
List the live catalogue instead, which is 29 models today:

```bash
python3 examples/nebius_agent.py --list-models
```

The default is `Qwen/Qwen3-235B-A22B-Instruct-2507`, verified working with tool calls.

### Reasoning models will surprise you

Measured on 12 August, same 150-word prompt, `max_tokens=1200`:

| Model | Billed | Delivered as answer | Wasted |
|---|---|---|---|
| `zai-org/GLM-5.2` | 1200 | **0** | **100%** |
| `MiniMaxAI/MiniMax-M3` | 905 | ~297 | ~67% |
| `openai/gpt-oss-120b` | 276 | ~262 | ~5% |
| `Qwen/Qwen3-235B-A22B-Instruct-2507` | 165 | ~230 | ~0% |

GLM-5.2 spent its entire budget in `reasoning_content` and returned an empty answer. It
was not slow, it emitted 341 tokens/sec, but a participant sees a blank response. If a
model returns nothing, raise `max_tokens` before assuming your code is broken.

This matters more in an agentic loop than in a single call, because the overhead
multiplies on every tool call. `openai/gpt-oss-120b` was the best balance of speed and
low overhead in this test.

Single samples on a shared endpoint, so treat as indicative. Re-measuring properly on the
day is itself a legitimate project.

### The comparison worth running

Ask the same question of a small model and a large one, and compare how each handles the
variant with no frequency data. Honest abstention is harder than it looks and weaker
models fail it. That comparison is a demo in its own right.

## Troubleshooting

| Symptom | Cause |
|---|---|
| `NEBIUS_API_KEY is not set` | Export it, or you redeemed the promo code without creating a key afterwards |
| 401 from the API | Key not created under the project that holds the credits |
| `--dry-run` fails | A checkout problem, nothing to do with Nebius. Ask in `#berlin-help` |
| Model ignores the tools | Some small models are weak at function calling. Try a larger one before assuming your code is wrong |
| Answer with no `[tool call]` lines | The model answered from memory. That is a finding: it is the failure this whole event is about |
| `404 model does not exist` | You used an ID from the Nebius docs. Run `--list-models` |
| Empty answer, `finish_reason: length` | A reasoning model burned the budget thinking. Raise `--max-tokens` or switch model |

## Next

[Pick a challenge](tracks.md). You now have the piece that makes any of them agentic
rather than a set of scripts run by hand.
