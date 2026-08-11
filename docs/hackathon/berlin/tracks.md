---
title: "Berlin Tracks"
description: The three build tracks for the ClawBio + Nebius hackathon in Berlin, with starter problems, data, and how demos are judged.
---

# Tracks

<div class="tutorial-card__header">
  <span class="difficulty-badge difficulty-badge--event">Event</span>
  <span class="time-estimate">3 h 40 min build time</span>
</div>

Pick one track. The same prize pool applies across all three, and the judging criteria
are identical.

!!! warning "Scope for the clock, not for the idea"

    You have 3 hours 40 minutes, 13:20 to 17:00. That is the single hardest constraint of
    the day and it is what most hackathon projects get wrong.

    Decide at 15:00 what you will cut. A team that demos one thing working end to end
    beats a team that demos four things half-built, every time.

## Track 1: Build a new ClawBio skill

Write one skill that does a single useful thing, with a test, and open a pull request
against ClawBio.

This is the track with the clearest finish line and the best artefact to take home. The
library already ships more than forty skills, so there is a pattern to copy and nobody
starts from a blank page.

**Start here:** [Build a Skill](../first-skill.md) and the
[SKILL.md specification](../../reference/skillmd-spec.md).

### Starter problems

These are real gaps, not exercises.

- **The gnomAD blind spot.** Read a VCF and report which variants have no gnomAD
  frequency at all. Absence of a frequency is not evidence of rarity, and automated
  pipelines routinely treat it as though it were. A skill that names the blind spot is
  more useful than one that guesses past it.
- **Model discovery.** Given a gene or a problem statement, return the open models that
  can say something useful about it, with their input and output formats. Right now this
  knowledge lives in people's heads.
- **Cohort questions that refuse to guess.** Turn a plain-English cohort question into a
  validated query against a public dataset, and abstain rather than fabricate when the
  question cannot be answered from the data available.

### Done looks like

A `SKILL.md`, a working implementation, one test that passes, and a pull request.

## Track 2: Build an agentic workflow, end to end

Chain existing skills so an agent takes a real omics question and produces an answer a
human can check, with the provenance visible at every step.

The bar is not that it works on one input. The bar is that it says what it did and where
each claim came from.

!!! note "The judging line for this track"

    A workflow that abstains honestly beats one that answers confidently and wrongly.
    Build the second behaviour in deliberately: show us what your agent does when the
    evidence is not there.

### Starter problems

- **Variants to shortlist.** From raw variants to a ranked shortlist for a rare-disease
  case, with the evidence for each rank exposed rather than implied.
- **Expression to biology.** Take a differential expression table and produce the
  biology, not just the gene list, with every claim traceable to a source.
- **Reproduce a figure.** Rebuild a published figure from its underlying public data,
  and report honestly where your numbers differ from the paper's. Disagreement is a
  result.

### Done looks like

A demo on real data where a sceptical person in the room can ask "how do you know that?"
about any step and get an answer.

## Track 3: Open biology models on Nebius Serverless

Take an open genomics or biology model, put it behind a Serverless endpoint, and make a
ClawBio skill call it as a tool.

This is the newest path of the three, so it carries the most risk of losing an hour to
plumbing. Nebius engineers are in `#berlin-help` for exactly this. Ask early rather than
at 16:00.

### Starter problems

- Wrap a protein or variant-effect model as a skill an agent can call, with the input
  contract documented well enough that another team could use it.
- Build a skill that routes between two models and explains which it chose and why.
- Benchmark a hosted model against a deterministic reference on a small task, and report
  where it fails rather than only where it succeeds.

### Done looks like

An endpoint an agent calls, and a demo where the model is doing real work rather than
being name-checked.

## Data

Use public data only. Nothing participant-supplied, nothing patient-identifiable.

| Dataset | What it is | Good for |
|---------|-----------|----------|
| Corpas family of five | Openly consented family genomes | Variant interpretation, inheritance, family-level questions |
| GIAB | Genome in a Bottle reference materials | Anything needing ground truth |
| ClinVar | Clinical variant assertions | Classification, evidence trails |
| GEO / Expression Atlas | Public expression data | Differential expression, cell types |

A shared read-only volume with reference data is mounted on the day, so no team spends
the morning downloading files.

## Judging

Everyone votes for their three favourite demos at 17:00. Four criteria, given to the
room so the vote is about the work rather than about who presented most confidently.

| Criterion | The question |
|-----------|--------------|
| **Does it run?** | Demonstrated live, on real data, not on slides |
| **Would you trust it?** | Provenance visible, uncertainty stated, failure handled |
| **Is it reusable?** | Could someone else pick it up on Wednesday |
| **Did it need agents?** | A shell script in a trenchcoat is not an agentic workflow |

## Submitting

Post in `#berlin-demos` before 17:00 with your repo link and one line describing what you
built. For Track 1, also open your pull request against
[ClawBio](https://github.com/ClawBio/ClawBio); see [Submit](../submit.md) for the
mechanics.

Submissions are collected after the event into a write-up of what the room built.
