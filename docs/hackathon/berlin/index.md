---
title: "ClawBio + Nebius Hackathon Berlin"
description: One day building AI agents that do real genomics work. Tuesday 18 August 2026, Impact Hub Berlin, hosted with Nebius.
---

# ClawBio + Nebius Hackathon Berlin

<div class="tutorial-card__header">
  <span class="difficulty-badge difficulty-badge--event">Event</span>
  <span class="time-estimate">Tuesday 18 August 2026</span>
</div>

![ClawBio Berlin](img/berlin-cover.png){ width="420" style="border-radius: 12px; margin: 1.5rem 0;" }

**Agentic AI for Genomics.** One day, real data, real compute. You build with ClawBio
skills on Nebius infrastructure and demo what you made at five.

[Register on Luma](https://luma.com/clawbio-q8pw){ .md-button .md-button--primary }

## Where and when

| | |
|---|---|
| **Date** | Tuesday 18 August 2026 |
| **Doors** | 11:30, subject to final venue confirmation |
| **Programme** | 12:00 to 18:00 |
| **Venue** | Impact Hub Berlin, room "The Loop", confirmed 28 July and awaiting final reconfirmation |
| **Address** | Rollbergstraße 28a, 12053 Berlin |
| **Cost** | Free. Lunch planned, with final service details pending. |

Come at 11:30 if you can. We start at 12:00 sharp, and the earlier you are set up on
Nebius the more you build.

## What you will build

AI agents can now plan multi-step work, call tools, run analyses, read their own outputs
and recover from failure. Biology is where that gets hard, because it demands
reproducibility, provenance, traceable evidence, and knowing when to abstain.

ClawBio is the open infrastructure for that: agents perform scientific work through
explicit, versioned, auditable skills, so what an agent did can be inspected, reproduced
and challenged. The library ships more than 90 skills and bridges to more than 8,000 Galaxy tools,
so you start from a working pattern rather than a blank page.

You will spend the afternoon on a real genomics problem, not on plumbing. The local
ClawBio route is small and verified. Nebius plans to provide compute and promotional
credits; the organisers are testing the external redemption path and room-scale capacity
before the final participant instructions are released. The programme provides 3 hours
40 minutes of build time.

The premise for the day is one sentence. **A model that confidently invents a citation is
worse than one that says it does not know.** Everything is built around grounding and
provenance rather than making a model sound convincing.

## Running order

| Time | Session |
|------|---------|
| 11:30 | Doors open. Arrive, get set up on Nebius |
| 12:00 | Welcome, then genomics in an agentic world, an overview (20 min) |
| 12:20 | Introduction to Nebius products (15 min) |
| 12:35 | Using and developing ClawBio skills on Nebius, a primer (30 min) |
| 13:05 | Challenges announced, team formation, lunch |
| 13:20 | Build |
| 17:00 | Demos. Everyone votes for their three favourites |
| 18:00 | Close |

Build time is **3 hours 40 minutes**. That is the constraint every challenge is designed
around, and it is worth internalising before you scope your idea.

## Challenges

Three real problems in genomics. Pick one. The same prize pool applies across all three.

<div class="grid cards" markdown>

- **1. End the diagnostic odyssey**

    A public four-person exome pedigree and hundreds of candidate variants. Show the
    segregation evidence, then be explicit about what cannot be concluded without a
    clinical phenotype.

- **2. A cancer target you would defend**

    Pick a tumour type in TCGA and shortlist targets. For each one, make the case against
    it as visible as the case for it. Show us a target you killed.

- **3. Whose genome does this fail?**

    Take a published polygenic score, apply it across ancestries, and find where it stops
    meaning anything. Then build the agent that declines to report it.

</div>

Not your field? There is an **open challenge** too: bring your own question and we will
scope it with you at 13:05.

**How** you build is a separate choice you make inside your challenge: write a new skill,
chain existing ones, or, if participant Serverless access is confirmed, host an open
model on Nebius and call it as a tool. Any available route counts on any challenge.

[Full briefs, data and judging](tracks.md){ .md-button }

## Prizes

The best projects receive Nebius AI Cloud and Token Factory credits to keep building
after the day.

| Place | Nebius AI Cloud | Token Factory |
|-------|-----------------|---------------|
| 1st | $1,500 | $500 |
| 2nd | $1,000 | $250 |
| 3rd | $500 | $100 |

Winners are chosen by the room. Everyone votes for their three favourite demos.

## What to bring

A laptop, and enough Python to be dangerous.

You do **not** need prior ClawBio experience, and you do not need to have used AI coding
agents before.

The planned sponsored route uses Nebius Token Factory promotional credits. The exact
participant redemption flow is under final test. The only local setup is ClawBio itself,
which is a clone and one command.

**Do that part at home.** It needs no key, no account and no credits, and it proves your
machine is ready before you arrive:

```bash
git clone --depth 1 https://github.com/ClawBio/ClawBio.git
cd ClawBio
python3 examples/nebius_agent.py --dry-run
```

On the day you add a Token Factory key and put a Nebius model in charge of the skill
library. [Setup](setup.md) covers the rest.

## Teams

Teams of four to five, formed at 13:05. Four to five is the sweet spot: smaller teams
stall, larger ones leave people idle.

You do not need to arrive with a team. Most people do not.

## Getting help

Support runs in Slack for the whole day, and starts now rather than on Tuesday. Team
formation happens in `#berlin-teams` before the event, so the earlier you join the better
your first hour goes.

[Join the ClawBio Slack](https://join.slack.com/t/clawbioworkspace/shared_invite/zt-46i2vb0gl-k6XHMJdUWE48odbfmONGFg){ .md-button .md-button--primary }

| Channel | For |
|---------|-----|
| `#berlin-general` | Announcements and joining details |
| `#berlin-help` | Stuck on anything. Nebius engineers are in here |
| `#berlin-teams` | Say what you want to build, find people to build it with |
| `#berlin-demos` | Post your repo and one line before 17:00 |

## Hosts

Run by [ClawBio](https://github.com/ClawBio/ClawBio) with
[Nebius](https://nebius.com), who provide the compute and the Token Factory credits.

ClawBio is open source and the skills you write on the day can be contributed back to
the library.
