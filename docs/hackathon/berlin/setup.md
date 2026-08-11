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

### 2. Deploy the environment

From the Nebius Serverless console you deploy the prepared ClawBio template, paste your
Token Factory key, and start. It is a one-click deploy: you do not choose GPUs, deploy
models, or configure endpoints. That is all abstracted away so the afternoon goes on
building rather than on infrastructure.

!!! info "Step-by-step screenshots land before the event"

    Nebius are preparing an illustrated walkthrough of the console flow, published here
    and posted in `#berlin-general` ahead of the day. If you are reading this before it
    appears, nothing is missing on your side: turn up and it takes two minutes with
    someone standing next to you.

### 3. Check it works

Ask the agent to run any skill against the shared reference data. If you get a result
back with a provenance trail, you are ready.

If you get an authentication error, it is almost always the Token Factory key rather
than anything else. Ask in `#berlin-help`.

## What is running underneath

You are talking to an agent configured to use open-weight models hosted by Nebius, with
the ClawBio skill library available as tools. You can point it at your own provider
instead if you prefer, but the sponsored path is the fastest and it is the one the
mentors can help with.

The shared read-only volume carries reference data (GIAB, ClinVar, reference genomes) so
no team spends build time downloading files.

## Getting help

| Channel | For |
|---------|-----|
| `#berlin-help` | Anything technical. Nebius engineers are in here all day |
| `#berlin-general` | Announcements, joining details, the walkthrough when it lands |
| `#berlin-teams` | Finding people to build with |

The Slack invite link is in your joining email. Ask early rather than at 16:00; the
mentors are there precisely so that nobody loses an hour to a fixable problem.

## Next

[Read the tracks](tracks.md) before you arrive and turn up with a rough idea of which
one you want. Team formation at 13:05 goes much faster when people already know what
they fancy building.
