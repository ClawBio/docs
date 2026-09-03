---
title: "MCP Server (deprecated)"
description: The ClawBio MCP server is deprecated as of 0.7.0 and will be removed in 0.8.0. How to migrate, and the reference for configurations still using it.
---

# MCP Server (deprecated)

!!! warning "Deprecated as of ClawBio 0.7.0, removed in 0.8.0"
    The MCP server keeps working through the 0.7.x series and prints a notice on stderr
    when it starts. Nothing in an existing client configuration breaks yet. Plan the move
    before 0.8.0.

## Why

The server shipped in 0.6.0 so that editors other than Claude Code could use the library.
Every ClawBio skill is a plain [Agent Skills](https://agentskills.io) folder, and the
editors the server was built for (Cursor, VS Code, Codex, Zed) now read such folders
directly from `~/.agents/skills/`. A remote-call shim in
front of them adds a process, a dependency pin (`mcp<2`) and a second code path, for no
capability the skills do not already have. Removing it leaves one contract to keep
correct: the `SKILL.md` and the script beside it.

Skills that wrap third-party MCP servers (`bioqc-mcp`, `bgpt-mcp`, `just-prs-mcp`) are
unaffected. This page is about ClawBio's own server only.

## Migrate

=== "Claude Code"

    Install the plugin. It ships the skills themselves, not a remote-call shim:

    ```
    /plugin marketplace add ClawBio/ClawBio
    /plugin install clawbio
    ```

=== "Cursor, VS Code, Codex, Zed, other Agent Skills readers"

    All four read `~/.agents/skills/` (and a project's `.agents/skills/`). Copy or
    symlink the skill folders you need there. Each folder is self-contained: `SKILL.md`,
    the script, demo data and tests.

    ```bash
    git clone https://github.com/ClawBio/ClawBio
    mkdir -p ~/.agents/skills
    cp -r ClawBio/skills/pharmgx-reporter ClawBio/skills/clinical-variant-reporter ~/.agents/skills/
    ```

=== "Any framework, any language"

    Use the CLI or the Python API. Both return the same structured result and
    reproducibility bundle the MCP tools returned.

    ```bash
    pip install clawbio
    clawbio run pharmgx --demo
    ```

    ```python
    from clawbio import run_skill, list_skills
    result = run_skill("pharmgx", demo=True)
    ```

The three MCP tools map directly: `clawbio_list_skills` is `clawbio list` or
`list_skills()`, `clawbio_describe_skill` is the skill's `SKILL.md`, and
`clawbio_run_skill` is `clawbio run <skill>` or `run_skill()`.

## Reference for existing configurations

Everything below still works until 0.8.0.

ClawBio ships a [Model Context Protocol](https://modelcontextprotocol.io) server, so any
MCP-capable client can discover, read, and run bioinformatics skills. It runs locally over
stdio. Your data never leaves your machine.

## Quick start

No installation required. `uvx` fetches and runs it in a throwaway environment:

```bash
uvx --from 'clawbio[mcp]' clawbio mcp
```

If you prefer a permanent install:

```bash
pip install 'clawbio[mcp]'
clawbio mcp
```

## Client configuration

The same three lines work across clients; only the file location differs.

=== "Cursor"

    `~/.cursor/mcp.json` (global) or `.cursor/mcp.json` (per project):

    ```json
    {
      "mcpServers": {
        "clawbio": {
          "command": "uvx",
          "args": ["--from", "clawbio[mcp]", "clawbio", "mcp"]
        }
      }
    }
    ```

=== "Claude Desktop"

    `~/Library/Application Support/Claude/claude_desktop_config.json` on macOS,
    `%APPDATA%\Claude\claude_desktop_config.json` on Windows:

    ```json
    {
      "mcpServers": {
        "clawbio": {
          "command": "uvx",
          "args": ["--from", "clawbio[mcp]", "clawbio", "mcp"]
        }
      }
    }
    ```

=== "VS Code"

    `.vscode/mcp.json` in your workspace:

    ```json
    {
      "servers": {
        "clawbio": {
          "type": "stdio",
          "command": "uvx",
          "args": ["--from", "clawbio[mcp]", "clawbio", "mcp"]
        }
      }
    }
    ```

=== "Zed"

    `settings.json`:

    ```json
    {
      "context_servers": {
        "clawbio": {
          "command": {
            "path": "uvx",
            "args": ["--from", "clawbio[mcp]", "clawbio", "mcp"]
          }
        }
      }
    }
    ```

Restart the client, then ask it something like *"list the ClawBio pharmacogenomics skills
and run the pharmgx demo"*.

## Tools

| Tool | Purpose |
|---|---|
| `clawbio_list_skills(query)` | Search the skill catalog. An empty query returns everything. Each result carries a `runnable` flag. |
| `clawbio_describe_skill(name)` | Return a skill's full `SKILL.md` contract: inputs, outputs, safety rules, demo command. Accepts either the skill name or its CLI alias. |
| `clawbio_run_skill(skill, demo, input_path, output_dir, extra_args)` | Execute a skill and return its structured result, including output file paths. |

### Not every skill is executable

The catalog contains both executable skills and agent-readable ones that ship only a
`SKILL.md` contract. `clawbio_list_skills` marks each with a `runnable` boolean, and
`clawbio_run_skill` refuses non-runnable skills with an explicit message rather than
failing obscurely. Agents should not have to guess.

## Data safety

By default the server runs **demo data only**. Passing `input_path` or `output_dir` is
refused:

```
This ClawBio MCP server is restricted to demo data. To let it read and write
local files, restart it with CLAWBIO_MCP_ALLOW_LOCAL_FILES=1.
```

This is deliberate. Adding an MCP server to a client config is a low-friction action,
often done once and forgotten, and it should not silently grant an agent read access to
a patient genome. To analyse your own files, opt in explicitly:

```json
{
  "mcpServers": {
    "clawbio": {
      "command": "uvx",
      "args": ["--from", "clawbio[mcp]", "clawbio", "mcp"],
      "env": { "CLAWBIO_MCP_ALLOW_LOCAL_FILES": "1" }
    }
  }
}
```

Skill runs still write a `reproducibility/` bundle (`commands.sh`, `environment.yml`,
SHA-256 checksums) next to their output, so an agent-initiated analysis can be replayed
and checked without the original session.

There is no hosted ClawBio MCP endpoint, and this is a design decision rather than a gap.
Genomic data should not traverse a third-party server to be analysed.

## Requirements

- Python 3.11+
- `mcp>=1.9,<2` — installed automatically by the `[mcp]` extra

!!! warning "mcp 2.0"
    `mcp` 2.0 removed `mcp.server.fastmcp`. The `clawbio[mcp]` extra pins below 2.0. If you
    installed `mcp` yourself and see a startup error naming the version, install the extra
    instead of a bare `mcp`.

## Troubleshooting

**Client shows no tools.** Confirm the server starts on its own first:

```bash
uvx --from 'clawbio[mcp]' clawbio mcp
```

It should wait silently for input on stdin. Press `Ctrl-C` to exit. If it exits
immediately with a message, the message names the cause.

**`uvx: command not found`.** Install [uv](https://docs.astral.sh/uv/), or use the
`pip install 'clawbio[mcp]'` route and set `"command": "clawbio", "args": ["mcp"]`.

**A skill fails with a missing dependency.** Some skills declare extra requirements. Run
`clawbio_describe_skill` and check the `dependencies` field.
