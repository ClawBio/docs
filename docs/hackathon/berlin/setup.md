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

!!! tip "You do not need to install ClawBio locally"

    The environment on the day comes with ClawBio and the models already wired up. A
    local install is a useful fallback, not a prerequisite. If you would rather have one
    anyway, follow the standard [hackathon setup](../setup.md).

## On the day

### 1. Collect your Token Factory credits

Nebius issue promotional credits at the venue. Scan the QR code at the door and your
code arrives by email, usually within five minutes.

Codes are given out in the room rather than in advance, so arriving is the only way to
get one.

### 2. Choose your route

There are two ways to run on the day. **Both spend Token Factory credits, both are
legitimate, and you can switch.** They differ in setup cost and in what they can reach.

| | **A. Hosted agent** | **B. Local ClawBio** |
|---|---|---|
| Setup | One button, keys provided | Clone the repo, paste a key |
| Time to first answer | ~2 minutes | ~15 minutes |
| Skills you can run | 4, on bundled demo data | All 95, on demo or your own files |
| Your own data files | Not by default (see below) | Yes |
| Best for | A first look at agents, and anyone who would rather not install anything | Challenges 1 and 2, which need skills the hosted image does not run |

If you have never used an AI coding agent, start with A, then move to B when you know
what you want to build. If you already know your challenge, go straight to B.

### 3a. Route A: the hosted agent

In the Nebius console at [console.nebius.com/ai](https://console.nebius.com/ai), find
**Deploy BioNeMo Agent** and start it. Nebius provide the API keys, so there is nothing
to procure.

What you get is an OpenClaw chat interface with several things already wired together:
Token Factory for reasoning, with a model picker; Tavily for agentic web search;
the ClawBio skill library exposed as tools; and hosted biology models you can call,
including Boltz-2 and DiffDock for structure prediction and docking.

The ClawBio tools are `clawbio__list_skills`, `clawbio__describe_skill` and
`clawbio__run_skill`. Start with:

```
List every ClawBio skill available in this image. Call clawbio__list_skills exactly once.
For each skill report its name and whether demo_runnable_in_image is true.
Do not run any skill.
```

Four skills report `demo_runnable_in_image: true`, meaning their demo runs entirely
inside the image with no external data: `gwas-lookup`, `gwas-prs`, `pharmgx-reporter`
and `profile-report`. Run one with `clawbio__run_skill`, `demo=true`.

!!! note "Pointing the hosted agent at your own file"

    `clawbio__run_skill` accepts an `input_path`, but ClawBio's MCP server refuses it
    unless it was started with `CLAWBIO_MCP_ALLOW_LOCAL_FILES=1`. That is our safety
    default, not a Nebius restriction: it stops a connected server handing an agent a
    genome on its own. If you need your own data on the day, use Route B, or ask in
    `#berlin-help`.

### 3b. Route B: local ClawBio on Token Factory

This is the route the [Nebius Quickstart](nebius-quickstart.md) documents end to end, and
it is the one to use for Challenges 1 and 2, because skills like `vcf-annotator`,
`rare-high-impact-variants`, `clinical-variant-reporter` and `target-validation-scorer`
run here and are not among the four in the hosted image.

You need a Token Factory key from your promo code, and a clone of ClawBio. There is a
dry-run mode that proves the whole tool path works before you spend a single credit.

### 4. Check it works

On Route A, run one of the four demo-qualified skills and read the output. On Route B,
run the dry run in the quickstart. Either way, what you want to see is a result with a
visible provenance trail: which skill ran, and what it returned.

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
