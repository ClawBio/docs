---
title: "Berlin Setup"
description: What to do before you arrive at the ClawBio + Nebius hackathon in Berlin, and how to get running on the day.
---

# Setup

<div class="tutorial-card__header">
  <span class="difficulty-badge difficulty-badge--beginner">Beginner</span>
  <span class="time-estimate">~15 min before the day</span>
</div>

You get a pre-configured environment on Nebius, so there is very little to install. The
few minutes below are worth spending in advance, because the difference between arriving
ready and arriving cold is most of an hour of build time.

## Before you arrive

### 1. Create a Nebius account

Sign up at [nebius.com](https://nebius.com) with the email you registered with. Do this
at home. Account creation and email verification is the single most common thing that
eats the first half hour of a hackathon.

### 2. Bring a laptop

Any operating system. You need a browser and a terminal.

### 3. Optional: get familiar with ClawBio

Not required, and about a third of the room will not have. If you want a head start,
the [Run Your First Skill](../../tutorials/run-your-first-skill.md) tutorial takes
about twenty minutes and will make the 12:35 primer land better.

!!! tip "Worth cloning ClawBio before you arrive"

    The main route on the day runs ClawBio locally with a Nebius Token Factory model in
    charge of it, so a clone saves you a few minutes and a share of the venue wifi. It is
    a normal Python repo with no heavy dependencies, and every skill ships its own demo
    data, so nothing else needs downloading.

    ```bash
    git clone https://github.com/ClawBio/ClawBio.git
    ```

    Not essential. You can do it in the room. See also the standard
    [hackathon setup](../setup.md).

## On the day

### 1. Collect your Token Factory credits

Nebius issue promotional credits at the venue. Scan the QR code at the door and your
code arrives by email, usually within five minutes.

Codes are given out in the room rather than in advance, so arriving is the only way to
get one.

### 2. Run ClawBio on Token Factory

This is the path to follow, and it is verified working end to end. A Token Factory model
takes charge of the ClawBio skill library: it reads each skill's contract, picks the one
that answers your question, runs it, reads the output, and reports both what it found and
what it could not conclude.

The [Nebius Quickstart](nebius-quickstart.md) walks it through in about fifteen minutes.
You need two things: your Token Factory key from the promo code above, and a clone of
ClawBio. There is a dry-run mode that exercises the entire tool path with no API call and
no spend, so you can prove your setup works before using a single credit.

All 95 skills are available on this route, including the ones the briefs lean on:
`vcf-annotator`, `rare-high-impact-variants`, `clinical-variant-reporter`,
`target-validation-scorer` and `gwas-prs`. You can also point skills at your own files.

!!! info "A hosted one-click agent may also be available"

    Nebius have been preparing a hosted agent that packages OpenClaw, Token Factory,
    Tavily web search, the ClawBio skills and hosted biology models such as Boltz-2 and
    DiffDock behind a single deploy button, with API keys provided.

    As of Friday 15 August it is not yet published to participant accounts: searching the
    Nebius console under **Applications → Marketplace** returns only *JupyterHub with
    BioNeMo Framework*, which is a notebook environment rather than the agent. If it
    lands before the day, we will announce it in `#berlin-general` with instructions, and
    it will be the fastest way to see an agent work without installing anything.

    Do not wait for it. The route above needs nothing from anyone and works today.

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

### 4. Check it works

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

You do not need to download reference data in advance. Every ClawBio skill ships with its
own demo data inside the repository, and the public datasets in the briefs (ClinVar,
gnomAD, TCGA, the PGS Catalog) are reached over their APIs rather than downloaded.

## Getting help

| Channel | For |
|---------|-----|
| `#berlin-help` | Anything technical. Nebius engineers are in here all day |
| `#berlin-general` | Announcements, joining details, the walkthrough when it lands |
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
