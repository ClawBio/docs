---
title: "Berlin Setup"
description: How to connect to the Nebius BioNeMo Research Agent at the ClawBio + Nebius hackathon in Berlin. A URL and a token, nothing to install.
---

# Setup

<div class="tutorial-card__header">
  <span class="difficulty-badge difficulty-badge--beginner">Beginner</span>
  <span class="time-estimate">~2 min</span>
</div>

**There is nothing to install.** Everything runs in your browser on Nebius. Bring a
laptop that can open a web page.

## Where to get your link and token

Both are posted in **`#berlin-general`** on the ClawBio Slack, along with every other
joining detail. Join before you arrive so you are not hunting for credentials at 12:00.

[Join the ClawBio Slack](https://join.slack.com/t/clawbioworkspace/shared_invite/zt-46i2vb0gl-k6XHMJdUWE48odbfmONGFg){ .md-button .md-button--primary }

Organisers have spares at the desk if anything goes wrong.

## Connecting

1. **Open the link** from `#berlin-general`. You land on the **OpenClaw Gateway Dashboard**.
2. The **WebSocket URL** field is already filled in for you.
3. Paste your token into **Gateway Token**. Leave **Password** empty.
4. Click **Connect**.
5. You arrive at the **BioNeMo Research Agent** chat, running **Nemotron 3 Super**.

Type into the message box at the bottom and you are working.

!!! warning "If it says Could not connect"

    Check these in order, and ask in `#berlin-help` rather than losing build time:

    - The WebSocket URL must start with `wss://`, not `ws://`.
    - Make sure the token went into **Gateway Token** and not into **Password**.
    - Check for a trailing space when you pasted the token.
    - Try a private or incognito window, in case a stale session is interfering.

    Organisers have spare credentials. This is the one thing worth interrupting someone
    for.

## The first thing to type

Capabilities differ between environments. Find out what yours actually has before you
build on an assumption:

```text
Before we start, tell me exactly what you can do:
1. List every tool you have available, with its name.
2. Use your ClawBio skill-listing tool to show me the skills you can actually run.
3. Can you fetch a file from a public URL? Can you read or write local files?
4. Can you run code you write yourself?

Answer only from what you can actually see. If you are not sure whether something
works, say so rather than assuming, and we will test it.
```

Whatever it answers is your real toolkit for the day. Build to that.

## Your ClawBio tools

The agent reaches the skill library through three tools. Tool names may be prefixed in
your environment, so let the agent find them rather than typing them yourself.

| Tool | What it does |
|---|---|
| `clawbio_list_skills(query)` | Search the library. An empty query lists everything. |
| `clawbio_describe_skill(name)` | Read a skill's contract: inputs, outputs, safety rules |
| `clawbio_run_skill(skill, demo, input_path, output_dir, extra_args)` | Run a skill |

Two things worth knowing:

**Skills use short aliases.** It is `prs`, not `gwas-prs`. It is `acmg`, not
`clinical-variant-reporter`. Ask the agent to list them and work from what it shows you.

**`demo=true` always works.** Passing a local file through `input_path` may be refused
depending on how your image is configured. If it is refused, that is a boundary worth
reporting in your demo, not a bug to fight for an hour.

## Your data

All three challenges have their data sorted, and none of it needs an account.

- **Challenge 1** uses a 15 KB teaching pack published at
  [the data page](data/index.md). Ask your agent to fetch the URLs.
- **Challenge 2** queries public APIs live. Nothing to download.
- **Challenge 3** uses demo data already inside the skills.

[Get the data](data/index.md){ .md-button .md-button--primary }

## Then pick a challenge

Each brief has a **prompt template you paste straight in**. That is your starting point,
and your first hour should be science rather than setup.

[Read the challenges](tracks.md){ .md-button }

??? note "Prefer to work on your own machine?"

    The hosted agent is the supported route today, but everything is open source and
    runs locally if you would rather.

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    git clone --depth 1 https://github.com/ClawBio/ClawBio.git
    cd ClawBio
    python3 examples/nebius_agent.py --dry-run
    ```

    Every skill runs through `uv`, so a bare `python3` will fail on missing packages.
    Note also that `clawbio.py run` only knows 49 short aliases: if a skill is not found,
    call its script directly, for example
    `uv run python skills/gwas-prs/gwas_prs.py --demo --output /tmp/prs`.

    Each challenge brief has a collapsed block with the exact verified commands. You can
    also open Claude Code or Codex in the clone: the repo ships `CLAUDE.md` and
    `AGENTS.md`, so both pick up the library on their own.

## Getting help

| Channel | For |
|---------|-----|
| `#berlin-general` | **Your Nebius link and token**, plus announcements |
| `#berlin-help` | Anything technical, including connection problems |
| `#berlin-teams` | Finding people to build with |
| `#berlin-demos` | Your repo and one line, before 16:40 |

[Join the ClawBio Slack](https://join.slack.com/t/clawbioworkspace/shared_invite/zt-46i2vb0gl-k6XHMJdUWE48odbfmONGFg){ .md-button }

Ask early rather than at 16:00. The mentors are there precisely so that nobody loses an
hour to a fixable problem.
