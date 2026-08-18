---
title: "Berlin Setup"
description: Five minutes of setup for the ClawBio + Nebius hackathon in Berlin. Install uv, clone ClawBio, open Claude Code or Codex, and let the agent do the rest.
---

# Setup

<div class="tutorial-card__header">
  <span class="difficulty-badge difficulty-badge--beginner">Beginner</span>
  <span class="time-estimate">~5 min</span>
</div>

Three commands, then you hand over to an agent. You will not be typing skill commands all
day: your coding agent reads the skill library and runs it for you.

## The five-minute setup

### 1. Install `uv`

Every ClawBio skill runs through `uv`. A system Python will fail on missing packages, and
`pip install -e .` does not work on this repository, so this step is not optional.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows PowerShell:

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then restart your terminal and check it:

```bash
uv --version
```

### 2. Clone ClawBio

```bash
git clone --depth 1 https://github.com/ClawBio/ClawBio.git
cd ClawBio
```

`--depth 1` skips the history. Please do this on your own connection rather than the
venue WiFi if you can.

### 3. Open your agent in that folder

```bash
claude          # Claude Code
codex           # Codex
```

The repository ships `CLAUDE.md` and `AGENTS.md` at its root, so both agents pick up the
skill library, the routing rules and the safety boundaries automatically. Tell your agent
to read `CLAUDE.md` first.

### 4. Prove it works

Ask your agent:

```text
Read CLAUDE.md, then run the reference agent's dry check:
uv run python examples/nebius_agent.py --dry-run
Tell me what it printed and what it proves.
```

You should see a rare high-impact variants report. That proves your checkout can run a
skill locally. It needs no key, no account and no credits.

If it does not print a report, ask in `#berlin-help` straight away rather than losing
build time to it.

!!! warning "The first thing that will confuse your agent"

    `clawbio.py run <name>` only registers 49 short aliases, and most of the challenge
    skills are not among them. `clawbio.py run gwas-prs` fails with "Unknown skill".

    The reliable form is the direct script path:
    `uv run python skills/gwas-prs/gwas_prs.py --demo --output /tmp/prs`

    Tell your agent this once and it will stop fighting the runner.

!!! tip "If you do not have Claude Code or Codex"

    Everything still works. Every challenge brief has a collapsed
    **"The underlying commands"** block with the exact verified commands, so you can run
    the skills directly and build your workflow around them.

    You can also put a Nebius Token Factory model in charge of the skills instead. The
    [Nebius Quickstart](nebius-quickstart.md) does that in about fifteen minutes.

## Your data

All three challenges have their data sorted, and none of it needs an account.

- **Challenge 1** downloads a 15 KB teaching pack from
  [the data page](data/index.md). Your agent can fetch it itself.
- **Challenge 2** queries the UCSC Xena API live. Nothing to download.
- **Challenge 3** uses demo data bundled in the repository.

[Get the data](data/index.md){ .md-button .md-button--primary }

## On the day

### Collect your Token Factory credits

Nebius issue promotional credits at the venue. Follow the QR or code instructions at
check-in, wait for the credit to appear in your Token Factory project, then create an API
key.

### Point an agent at the skills

You have two ways to make this agentic, and both count for judging.

**Claude Code or Codex**, driving the ClawBio skills locally. This is the fastest route
and it works right now.

**A Nebius Token Factory model**, taking charge of the reference agent's skills. The
[Nebius Quickstart](nebius-quickstart.md) walks it through in about fifteen minutes. This
is where your credits go.

The reference agent starts with four verified skills: `vcf-annotator`,
`rare-high-impact-variants`, `clinical-variant-reporter` and `gwas-prs`. Its `SKILLS`
dictionary is deliberately a small allowlist. Add the skills your project needs there
rather than exposing arbitrary shell commands to a model.

If you get an authentication error, it is almost always the Token Factory key: usually
the promo code was redeemed but no key was created afterwards, or the key belongs to a
different project from the credits. Ask in `#berlin-help`.

!!! info "A hosted one-click agent may also be available"

    Nebius have been preparing a hosted agent that packages OpenClaw, Token Factory,
    Tavily web search, the ClawBio skills and hosted biology models such as Boltz-2 and
    DiffDock behind a single deploy button.

    Participant access to that route is not confirmed. If it becomes available we will
    announce it in `#berlin-general` with tested instructions.

    Do not wait for it. The local route above is the canonical path and works today.

??? note "If you do get access to the hosted agent"

    The ClawBio tools there are `clawbio__list_skills`, `clawbio__describe_skill` and
    `clawbio__run_skill`. Start by asking it to list the skills and report which have
    `demo_runnable_in_image: true`. Four do: `gwas-lookup`, `gwas-prs`, `pharmgx-reporter`
    and `profile-report`. Run one with `clawbio__run_skill` and `demo=true`.

    That image runs those four on bundled demo data only. `clawbio__run_skill` accepts an
    `input_path`, but ClawBio's MCP server refuses it unless started with
    `CLAWBIO_MCP_ALLOW_LOCAL_FILES=1`. That guard is ours, not a Nebius restriction: it
    stops a connected server handing an agent a genome on its own. For your own data, use
    the local route.

## Getting help

| Channel | For |
|---------|-----|
| `#berlin-help` | Anything technical. Organisers and Nebius engineers are in the workspace |
| `#berlin-general` | Announcements and joining details |
| `#berlin-teams` | Finding people to build with |
| `#berlin-demos` | Your repo and one line, before 16:40 |

[Join the ClawBio Slack](https://join.slack.com/t/clawbioworkspace/shared_invite/zt-46i2vb0gl-k6XHMJdUWE48odbfmONGFg){ .md-button }

Ask early rather than at 16:00. The mentors are there precisely so that nobody loses an
hour to a fixable problem.

## Next

[Read the challenges](tracks.md) and turn up with a rough idea of which one you want.
Team formation at 13:05 goes much faster when people already know what they fancy
building.

Each brief has a prompt you can paste straight into your agent, so your first hour starts
with science rather than setup.
