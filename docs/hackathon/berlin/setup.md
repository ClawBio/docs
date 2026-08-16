---
title: "Berlin Setup"
description: What to do before you arrive at the ClawBio + Nebius hackathon in Berlin, and how to get running on the day.
---

# Setup

<div class="tutorial-card__header">
  <span class="difficulty-badge difficulty-badge--beginner">Beginner</span>
  <span class="time-estimate">~15 min before the day</span>
</div>

Nebius provide the compute and the credits, and ClawBio installs with a clone, so there
is very little to do. The
few minutes below are worth spending in advance, because the difference between arriving
ready and arriving cold is most of an hour of build time.

## Before you arrive

### 1. Create a Nebius account

Sign up at [nebius.com](https://nebius.com) with the email you registered with. Do this
at home. Account creation and email verification is the single most common thing that
eats the first half hour of a hackathon.

### 2. Bring a laptop

Any operating system. You need a browser and a terminal.

### 3. Install ClawBio and prove it runs

**Do this at home. It is the difference between building from 13:20 and building from
14:00.** It takes about five minutes, needs no key, no account, and no Nebius credits,
and it downloads nothing beyond the repository itself.

First check you have git and Python 3.11 or newer:

```bash
git --version
python3 --version
```

Then clone and run the check:

```bash
git clone --depth 1 https://github.com/ClawBio/ClawBio.git
cd ClawBio
python3 examples/nebius_agent.py --dry-run
```

You should see a report about rare high-impact variants. That proves this checkout can
run the reference script and dispatch one bundled skill locally. It does not test every
skill, your Token Factory key, the venue network or room-scale capacity.

`--depth 1` skips the history and takes the download from about 145 MB to well under
half that. Please do this at home rather than in the room: seventy of us cloning the same
repository over one venue connection at 12:30 is a slow start for everybody.

**If it does not print a report, ask in `#berlin-help` now rather than on Tuesday
morning.** Solving it in advance costs you a message; solving it in the room costs you
build time.

If you do not have git or Python, the
[Nebius Quickstart](nebius-quickstart.md) has per-OS install commands and the full
walkthrough.

### 4. Optional: get familiar with ClawBio

Genuinely optional. If you want a head start, the
[Run Your First Skill](../../tutorials/run-your-first-skill.md) tutorial takes about
twenty minutes and will make the 12:35 primer land better.

## On the day

### 1. Collect your Token Factory credits

Nebius plan to issue promotional credits at the venue. Follow the confirmed QR or code
instructions at check-in, wait for the credit to appear in your Token Factory project,
then create an API key. The organisers are testing this exact external-user path before
the event.

### 2. Run ClawBio on Token Factory

This is the path to follow. The local agent and one organiser-key Token Factory call are
verified. The external promotional-credit route and room-scale capacity remain under
final test. A Token Factory model takes charge of the reference agent's allowlisted
ClawBio skills: it reads their contracts, picks one, runs it, reads the output, and
reports both what it found and what it could not conclude.

The [Nebius Quickstart](nebius-quickstart.md) walks it through in about fifteen minutes.
You need two things: your Token Factory key from the promo code above, and a clone of
ClawBio. There is a dry-run mode that exercises one local dispatch path with no API call
and no spend, so you can prove the reference checkout works before using a credit.

The reference agent starts with four verified skills:
`vcf-annotator`, `rare-high-impact-variants`, `clinical-variant-reporter` and
`gwas-prs`. Its `SKILLS` dictionary is deliberately a small allowlist. Add the skills
your project needs there rather than exposing arbitrary shell commands to the model.

!!! info "A hosted one-click agent may also be available"

    Nebius have been preparing a hosted agent that packages OpenClaw, Token Factory,
    Tavily web search, the ClawBio skills and hosted biology models such as Boltz-2 and
    DiffDock behind a single deploy button, with API keys provided.

    Participant access to that hosted route has not been confirmed. If it becomes
    available before the day, we will announce it in the final Luma update and
    `#berlin-general` with tested instructions.

    Do not wait for it. The local route above is the canonical path and works today.

??? note "If you do get access to the hosted agent"

    The ClawBio tools there are `clawbio__list_skills`, `clawbio__describe_skill` and
    `clawbio__run_skill`. Start by asking it to list the skills and report which have
    `demo_runnable_in_image: true`. Four do: `gwas-lookup`, `gwas-prs`,
    `pharmgx-reporter` and `profile-report`. Run one with `clawbio__run_skill` and
    `demo=true`.

    That image runs those four on bundled demo data only. `clawbio__run_skill` accepts an
    `input_path`, but ClawBio's MCP server refuses it unless started with
    `CLAWBIO_MCP_ALLOW_LOCAL_FILES=1`. That guard is ours, not a Nebius restriction: it
    stops a connected server handing an agent a genome on its own. For your own data, use
    the local route.

### 3. Check it works

Run the dry run in the quickstart. What you want to see is a result with a visible
provenance trail: which skill ran, and what it returned. If the dry run prints a report,
your checkout is sound, and any later failure is the key or the network rather than
ClawBio.

If you get an authentication error, it is almost always the Token Factory key rather
than anything else: usually the promo code was redeemed but no key was created
afterwards, or the key belongs to a different project from the credits. Ask in
`#berlin-help`.

## What is running underneath

You are talking to an agent configured to use open-weight models hosted by Nebius, with
the ClawBio skill library available as tools. You can point it at your own provider
instead if you prefer, but the sponsored path is the fastest and it is the one the
mentors can help with.

You do not need to download bulk reference data in advance. The exact skill commands in
the briefs use bundled demos or named APIs. Some other skills and real inputs need
separate files. Challenge 1 uses a small organiser-provided teaching pack whose approved
link will appear in the final Luma reminder and `#berlin-general`.

## Getting help

| Channel | For |
|---------|-----|
| `#berlin-help` | Anything technical. Nebius engineers are in here all day |
| `#berlin-general` | Announcements and joining details |
| `#berlin-teams` | Finding people to build with |

[Join the ClawBio Slack](https://join.slack.com/t/clawbioworkspace/shared_invite/zt-46i2vb0gl-k6XHMJdUWE48odbfmONGFg){ .md-button }

Ask early rather than at 16:00; the mentors are there precisely so that nobody loses an
hour to a fixable problem.

## Next

Once you have your Token Factory key, work through the
[Nebius Quickstart](nebius-quickstart.md). Fifteen minutes, and it is the piece that
makes any challenge agentic rather than a set of scripts run by hand.

[Read the challenges](tracks.md) before you arrive and turn up with a rough idea of which
one you want. Team formation at 13:05 goes much faster when people already know what
they fancy building.

Each brief names the skills that give you an hour-one win, so you can look at one or two
in advance if you like. You do not have to.
