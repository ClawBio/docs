---
title: "Berlin Challenges"
description: Three genomics challenges for the ClawBio + Nebius hackathon in Berlin. Drive them with Claude Code or Codex, on real public data.
---

# Challenges

<div class="tutorial-card__header">
  <span class="difficulty-badge difficulty-badge--event">Event</span>
  <span class="time-estimate">3 h 20 min build time</span>
</div>

Three challenges, each a real problem in genomics that is still open. Pick one. The same
prize pool applies across all three and the judging criteria are identical.

**You are not here to type commands.** You drive a coding agent, and the agent reads the
skills, runs them, chains them and interprets what comes back. Each challenge below gives
you a prompt to paste. Start there and go wherever the science takes you.

[Get the data](data/index.md){ .md-button }
[Setup, if you have not done it](setup.md){ .md-button }

## Before anything else: five minutes of setup

You need three things. Your agent handles everything after that.

**1. Install `uv`.** Every ClawBio skill runs through it, and a system Python will fail on
missing packages. One line:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**2. Clone ClawBio.**

```bash
git clone --depth 1 https://github.com/ClawBio/ClawBio.git
cd ClawBio
```

**3. Open your agent in that folder.**

```bash
claude          # Claude Code
codex           # Codex
```

The repository ships `CLAUDE.md` and `AGENTS.md` at its root, so both agents pick up the
skill library, the routing rules and the safety boundaries on their own. Tell your agent
to read `CLAUDE.md` first and it will know what it is holding.

!!! tip "The first thing to ask it"

    ```text
    Read CLAUDE.md, then list the skills in skills/ that are relevant to
    [rare disease / cancer targets / polygenic scores] and tell me what each one
    actually does. Do not run anything yet.
    ```

    Ninety-eight skills is too many to browse. Let the agent triage them for you.

!!! warning "One thing that will trip your agent up"

    `clawbio.py run <name>` only knows 49 short aliases, and most challenge skills are
    not among them. `clawbio.py run gwas-prs` fails with "Unknown skill".

    The reliable form is the direct script path, which is what the prompts below use:
    `uv run python skills/gwas-prs/gwas_prs.py --demo --output /tmp/prs`

    If your agent gets stuck on the runner, tell it to call the script directly.

!!! info "Where your Nebius credits come in"

    ClawBio skills are plain Python and most need no model at all. Running them by hand
    consumes no credit and, on its own, is not an agentic workflow.

    Nebius enters at two points. First, **the agent**: a Token Factory model can take
    charge of the skill library instead of Claude or Codex, which is what the
    [Nebius Quickstart](nebius-quickstart.md) sets up in about fifteen minutes. Second,
    **hosted models as tools**: a skill can call a model over HTTP, and the `gi-*` family
    is the working reference to copy.

    Criterion four at judging, *did it need agents*, is asking exactly this.

!!! warning "Scope for the clock, not for the idea"

    Build runs 13:20 to 16:40, then demo rehearsal, then demos at 17:00. That is
    3 hours 20 minutes and it is the hardest constraint of the day.

    Every brief has an hour-one win and a stretch. Get the hour-one win working first,
    even if it is boring. Decide at 15:00 what you are cutting. A team that demos one
    thing working end to end beats a team that demos four things half-built, every time.

## Challenge 1: End the diagnostic odyssey

**The problem.** A family with an undiagnosed condition waits years for an answer. The
sequencing is not the bottleneck. Interpretation is: hundreds of candidate variants, most
of them uncertain, and a pipeline that has to decide which ones a human should ever see.

**Headline brief.** Use the publicly consented four-person Corpas exome pedigree: son,
father, mother and sister. Treat the son as a teaching proband, show the inheritance
logic and make the evidence behind every filter visible. Then state what the data does
not support. There is no phenotype and no HPO file, so a defensible agent must refuse to
turn segregation evidence into a diagnosis.

That last part is the point. Any tool can output a ranking. Very few say which variants
they were not entitled to have an opinion about.

**Your data is [here](data/index.md#challenge-1-end-the-diagnostic-odyssey).** 15 KB,
downloads instantly, and your agent can fetch it itself.

### Paste this into your agent

```text
I'm at a genomics hackathon, working in this ClawBio repo. Read CLAUDE.md first.

Challenge: end the diagnostic odyssey.

Get the data into data/challenge1/ (all three files):
https://docs.clawbio.ai/hackathon/berlin/data/challenge1-b37-segregation.vcf.gz
https://docs.clawbio.ai/hackathon/berlin/data/challenge1-b37-segregation.vcf.gz.tbi
https://docs.clawbio.ai/hackathon/berlin/data/challenge1-b37-segregation.tsv

It's a four-person exome pedigree on GRCh37/b37. Samples ISDBM322015 to ISDBM322018 are
son, father, mother, sister. 68 HIGH-effect records the son carries with exactly one
parent: 30 labelled paternal, 38 maternal, unphased.

Do this in order:
1. Load the pack and reproduce the 30/38 paternal/maternal split. Show me the filter
   logic, not just the counts.
2. Read skills/rare-high-impact-variants/SKILL.md, run its demo, and show me how it
   separates documented-rare variants from variants with NO frequency data at all.
   That distinction is the interesting part.
3. Build me an abstention list: for each record, what can this data NOT support, and
   why. There is no phenotype, no HPO terms, no valid population-frequency layer, and
   the EFF annotation is historical.

Rules: use `uv run python`, never bare python3. Call skills by their direct script path,
not through clawbio.py. Never call anything rare, pathogenic, diagnostic, de novo or
compound heterozygous. If you can't verify something, say so plainly instead of hedging.
```

| | |
|---|---|
| **Hour one** | Reproduce the 30 paternal and 38 maternal labels, with every filter visible. |
| **Hour two** | Add one missing evidence layer, such as build-matched population frequency or updated consequence annotation. Keep it separate from the inherited teaching labels. |
| **Stretch** | An explicit abstention list with a reason attached to every entry. |

**The gap worth attacking.** Variants with no gnomAD frequency at all. Absence of a
frequency is not evidence of rarity, but automated pipelines routinely treat it as though
it were. On a recent audit of one such pipeline, 16 of 27 flagged false-actionable calls
were genuine instances of this. A skill that names the blind spot is worth more than one
that guesses past it.

**Other angles.** Use `rare-disease-rnaseq` to find an expression outlier and demo one
case where blood RNA promotes or demotes a variant of uncertain significance. Or run
`cnv-acmg-classifier` over structural and copy-number variants and report what an
SNV-only pipeline silently drops.

??? note "The underlying commands, if you want to see them"

    Your agent runs these for you. They are here so you can check its work, and all were
    verified from a clean clone.

    ```bash
    # The gnomAD blind spot, already articulated in the report this prints
    uv run python skills/rare-high-impact-variants/rare_high_impact_variants.py \
      --demo --output /tmp/rhiv && cat /tmp/rhiv/report.md

    # VEP + ClinVar + gnomAD annotation, ranked by impact
    uv run python skills/vcf-annotator/vcf_annotator.py --demo --output /tmp/vcfann

    # ACMG/AMP 28-criteria classification with evidence codes
    uv run python skills/clinical-variant-reporter/clinical_variant_reporter.py \
      --demo --output /tmp/acmg

    # Structural and copy-number variants, ClinGen/ACMG 2019 points
    uv run python skills/cnv-acmg-classifier/cnv_acmg_classifier.py --demo --output /tmp/cnv

    # Blood RNA expression outliers, for the VUS tie-breaker angle
    uv run python skills/rare-disease-rnaseq/rare_disease_rnaseq.py --demo --output /tmp/rd
    ```

    Two traps to tell your agent about. Do not run `vcf-annotator` over a complete Corpas
    source VCF: it makes serial per-variant network calls, defaults to GRCh38 services and
    does not retain family genotypes. Do not feed the historical quartet directly to
    `rare-high-impact-variants`: it does not parse the legacy `EFF` field.

## Challenge 2: A cancer target you would defend

**The problem.** Target selection is where most of the money in oncology is lost. The
literature will support almost any gene if you go looking for support. The hard part is
the counter-argument.

**Headline brief.** Pick a tumour type in TCGA. Produce a shortlist of candidate targets.
For every target, make the case against it as visible as the case for it. You must demo
at least one target your agent killed, and why.

**Your data needs no download.** The Xena API is queried live and was verified working
this morning. See [challenge 2 data](data/index.md#challenge-2-a-cancer-target-you-would-defend).

### Paste this into your agent

```text
I'm at a genomics hackathon, working in this ClawBio repo. Read CLAUDE.md first.

Challenge: pick a cancer target you would defend.

1. Read skills/xena-tcga-gene-query/SKILL.md. Query the UCSC Xena API live for tumour
   vs normal expression and survival association, for a gene set in a TCGA cancer type.
   Watch the argument order: global flags come BEFORE the subcommand, like this:
   uv run python skills/xena-tcga-gene-query/scripts/query_tcga_api.py \
     --demo --output /tmp/xena diff-expr --gene TP53 --cancer BRCA
2. Shortlist three candidate targets. For each one, build the case FOR and the case
   AGAINST with equal effort. Use skills/target-validation-scorer and
   skills/omics-target-evidence-mapper.
3. Kill one target explicitly. Tell me what killed it.
4. Check prior art with skills/clinical-trial-finder and skills/pubmed-summariser.

CRITICAL: every PMID you cite must resolve. Before showing me any citation, fetch it and
confirm it exists. A fabricated PMID disqualifies this project from first place, so build
that check into the workflow and show it running. If a claim has no resolvable source,
drop the claim.

Use `uv run python` and call scripts by their direct path, not through clawbio.py.
```

| | |
|---|---|
| **Hour one** | Tumour versus normal expression and survival for a gene set, via `xena-tcga-gene-query`. |
| **Hour two** | Dependency and evidence. `target-validation-scorer` for a GO/NO-GO with reasoning, `omics-target-evidence-mapper` to aggregate across public sources. |
| **Stretch** | Prior art. `clinical-trial-finder` and `pubmed-summariser` or `lit-synthesizer`. |

!!! danger "Every PMID must resolve"

    This challenge is where language models fail most attractively. A fabricated citation
    that supports your target is worse than no citation, because it is persuasive. Any
    demo containing a PMID that does not resolve is out of contention for first place in
    this challenge, however good the rest of it is.

    Build the check in. It is three lines and it is the whole thesis of the day.

**Other angles.** Run `drug-repurposing-screen` on a pooled viability screen and pull out
context-selective candidates rather than pan-lethal ones. Or rebuild a figure from a
published TCGA analysis using the underlying public data and report where your numbers
differ from the paper's. Disagreement, stated precisely, is a result.

??? note "The underlying commands, if you want to see them"

    ```bash
    # Tumour vs normal, correlation and survival, via the UCSC Xena API
    uv run python skills/xena-tcga-gene-query/scripts/query_tcga_api.py \
      --demo --output /tmp/xena diff-expr --gene TP53 --cancer BRCA

    # GO/NO-GO target scoring with reasoning
    uv run python skills/target-validation-scorer/target_validation_scorer.py \
      --demo --output /tmp/tvs && cat /tmp/tvs/report.md

    # Aggregate public target evidence across omics sources
    uv run python skills/omics-target-evidence-mapper/omics_target_evidence_mapper.py \
      --demo --output /tmp/otem

    # Prior art: is somebody already running this?
    uv run python skills/clinical-trial-finder/clinical_trial_finder.py --demo --output /tmp/ctf
    uv run python skills/pubmed-summariser/pubmed_summariser.py --demo --output /tmp/pubmed
    ```

    `drug-repurposing-screen` needs one extra package: `uv pip install fastparquet`.
    Everything else runs as-is.

## Challenge 3: Whose genome does this fail?

**The problem.** Most of what genomics knows, it knows about Europeans. A polygenic risk
score trained on one population does not simply become less accurate elsewhere. It
becomes uninterpretable.

Every score in the demo is labelled `Reference population: EUR`, which is honest, and
every score still returns a confident percentile regardless of whose genome went in.
Disclosure is not abstention. The distance between those two is this challenge.

**Your data is bundled in the repo.** Nothing to download. See
[challenge 3 data](data/index.md#challenge-3-whose-genome-does-this-fail).

### Paste this into your agent

```text
I'm at a genomics hackathon, working in this ClawBio repo. Read CLAUDE.md first.

Challenge: whose genome does this polygenic score fail?

1. Read skills/gwas-prs/SKILL.md, then run:
   uv run python skills/gwas-prs/gwas_prs.py --demo --output /tmp/prs
   Now grep the report for "reference population". Every score says EUR, and every score
   still returns a confident percentile no matter whose genome went in. Show me that.
2. Quantify the gap. Run skills/claw-ancestry-pca on its demo, and run
   skills/equity-scorer over examples/demo_populations.vcf with
   examples/demo_population_map.csv for FST, heterozygosity and HEIM metrics.
3. Build the thing that matters: a wrapper that REFUSES to report a percentile when the
   individual's ancestry is too far from the score's reference population. Pick a
   threshold, justify it from the data, and demo it firing on a real input.

The plot is not the deliverable. The refusal is the deliverable. End by showing me it
declining to answer, with a message a clinician could act on.

Use `uv run python` and direct script paths, not clawbio.py.
```

| | |
|---|---|
| **Hour one** | Compute a PGS Catalog score with `gwas-prs`, on one individual, end to end. |
| **Hour two** | Stratify. `claw-ancestry-pca` against SGDP, then `equity-scorer` for heterozygosity, FST and composite HEIM metrics. |
| **Stretch** | Wire the abstention in, with a stated threshold and a message a clinician could act on. Show it firing. |

**Other angles.** Measure the blind spot genome-wide: which variants have no frequency
data in any gnomAD population, and how that count differs by the ancestry of the person
sequenced. Or audit a report generator by feeding it an input too thin to support an
ancestry call, a few dozen ancestry-informative markers, and see whether it abstains or
produces a confident pie chart. Most produce the pie chart.

??? note "The underlying commands, if you want to see them"

    ```bash
    # Six polygenic scores from the PGS Catalog, then what it admits to
    uv run python skills/gwas-prs/gwas_prs.py --demo --output /tmp/prs
    grep -i "reference population" /tmp/prs/prs_report.md   # EUR, on every single score

    # Ancestry decomposition against the Simons Genome Diversity Project
    uv run python skills/claw-ancestry-pca/ancestry_pca.py --demo --output /tmp/pca

    # equity-scorer has no --demo, but the repo ships an input
    uv run python skills/equity-scorer/equity_scorer.py \
      --input examples/demo_populations.vcf \
      --pop-map examples/demo_population_map.csv \
      --output /tmp/equity && cat /tmp/equity/report.md
    ```

    The equity run produces a HEIM score of 76.2/100, with pairwise FST and a PCA.

## Open challenge

Bring your own problem. Same rules, same judging, same prize pool.

If you work on a biology not covered above, plants, microbes, ageing, proteomics, neuro,
bring the question and we will scope it to the clock with you at 13:05. The library has
98 skills and a bridge to more than 8,000 Galaxy tools, so the odds that nothing touches
your field are low.

Two conditions. Public data only, and the question has to be one where being wrong
matters, because that is what the judging rewards.

## How you build it

The challenge is the science. This is the engineering, and it is your choice inside
whichever challenge you picked.

<div class="grid cards" markdown>

- **Route A: write a new skill**

    One skill, one job, a test, a pull request against ClawBio. The best artefact to take
    home and the clearest finish line. Ask your agent to scaffold it from an existing
    skill, or start from [Build a Skill](../first-skill.md) and the
    [SKILL.md specification](../../reference/skillmd-spec.md).

- **Route B: chain what exists**

    Compose existing skills into a workflow that answers the question end to end, with
    provenance visible at every step. Fastest route to a working demo, and the one to
    pick if your team is new to agents.

- **Route C: host your own model**

    If participant Serverless access is confirmed, put an open biology model behind a
    Nebius endpoint and have a ClawBio skill call it as a tool. Deepest route, most
    plumbing risk.

</div>

!!! tip "Serverless bonus, on any challenge"

    Any team on any challenge that stands up an open model on Nebius Serverless and has
    an agent genuinely call it gets that noted to the room at judging. You are not
    choosing between doing science and doing infrastructure.

    If you go this way, start it at 13:20 rather than at 15:00, and ask in `#berlin-help`
    early rather than at 16:00.

## What "done" looks like

Whichever challenge you picked, a finished demo is one where a sceptical person in the
room can ask **"how do you know that?"** about any step on screen and get an answer.

Concretely, by 16:40 you want:

1. It runs live, on real data, in front of people.
2. Every claim traces to a source, and the sources resolve.
3. There is at least one input where it correctly says it cannot answer.
4. Somebody else could run it on Wednesday from your repo.

Point three is the one teams skip and the one that wins. Build a deliberate failure case
and demo it on purpose.

## Judging

Everyone votes for their three favourite demos at 17:00. Four criteria, given to the room
so the vote is about the work rather than about who presented most confidently.

| Criterion | The question |
|-----------|--------------|
| **Does it run?** | Demonstrated live, on real data, not on slides |
| **Would you trust it?** | Provenance visible, uncertainty stated, failure handled |
| **Is it reusable?** | Could someone else pick it up on Wednesday |
| **Did it need agents?** | A shell script in a trenchcoat is not an agentic workflow |

One hard rule across all challenges: **claims that cannot be checked do not count.** A
confident answer with an invented source scores below an honest abstention.

## Submitting

Post in `#berlin-demos` **before 16:40** with your repo link and one line describing what
you built. Demos start at 17:00 and the order is fixed at the freeze, so late submissions
do not get a slot.

If you took Route A, also open your pull request against
[ClawBio](https://github.com/ClawBio/ClawBio); see [Submit](../submit.md) for the
mechanics.

Submissions are collected after the event into a write-up of what the room built.
