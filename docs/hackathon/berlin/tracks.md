---
title: "Berlin Challenges"
description: Three genomics challenges for the ClawBio + Nebius hackathon in Berlin. Paste a prompt into the BioNeMo Research Agent and build on real public data.
---

# Challenges

<div class="tutorial-card__header">
  <span class="difficulty-badge difficulty-badge--event">Event</span>
  <span class="time-estimate">3 h 20 min build time</span>
</div>

Three challenges, each a real problem in genomics that is still open. Pick one. The same
prize pool applies across all three and the judging criteria are identical.

**You are not here to type commands, and there is nothing to install.** Your Nebius link
and token are in `#berlin-general` on Slack. They open the **BioNeMo Research Agent**,
and you work by talking to it. It reads the ClawBio skills, runs them, chains them and
interprets what comes back.

Each challenge below gives you a **prompt template to paste**. Start there, then go
wherever the science takes you.

[Get the data](data/index.md){ .md-button }
[How to connect](setup.md){ .md-button }

## Getting in: two minutes, nothing to install

Your **link and token** are posted in **`#berlin-general`** on the ClawBio Slack. That is
the whole setup.

1. Open the link. You land on the **OpenClaw Gateway Dashboard**.
2. The **WebSocket URL** is already filled in. Paste your token into **Gateway Token**.
   Leave **Password** empty.
3. Click **Connect**.
4. You arrive at the **BioNeMo Research Agent** chat, running **Nemotron 3 Super**.

Type into the message box. That is it. No clone, no install, no keys of your own.

!!! tip "Start every session with this"

    Capabilities differ between environments, so find out what yours has before you
    build on an assumption. Paste this first:

    ```text
    Before we start, tell me exactly what you can do:
    1. List every tool you have available, with its name.
    2. Use your ClawBio skill-listing tool to show me the skills you can actually run.
    3. Can you fetch a file from a public URL? Can you read or write local files?
    4. Can you run code you write yourself?

    Answer only from what you can actually see. If you are not sure whether something
    works, say so rather than assuming, and we will test it.
    ```

    Whatever it answers is your real toolkit for the day. Build to that, not to what
    you hoped it had.

!!! info "Your ClawBio tools"

    The agent reaches the skill library through three tools. Names may be prefixed in
    your environment, so let the agent find them rather than typing them yourself.

    | Tool | What it does |
    |---|---|
    | `clawbio_list_skills(query)` | Search the library. Empty query lists everything. |
    | `clawbio_describe_skill(name)` | Read a skill's contract: inputs, outputs, safety rules |
    | `clawbio_run_skill(skill, demo, input_path, output_dir, extra_args)` | Run it |

    Two things worth knowing. Skills are called by their **short alias**, so it is
    `prs`, not `gwas-prs`, and `acmg`, not `clinical-variant-reporter`. Ask the agent to
    list them and it will show you the real names. And `demo=true` always works, while
    `input_path` may be refused for local files depending on how your image is
    configured. If it is refused, that is a boundary to report, not a bug to fight.

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

### Paste this into the BioNeMo Research Agent

```text
I'm at a genomics hackathon. You are my analysis partner for the next three hours.

CHALLENGE: End the diagnostic odyssey.

THE DATA
A four-person exome pedigree, GRCh37/b37, publicly consented teaching data:
https://docs.clawbio.ai/hackathon/berlin/data/challenge1-b37-segregation.vcf.gz
https://docs.clawbio.ai/hackathon/berlin/data/challenge1-b37-segregation.vcf.gz.tbi
https://docs.clawbio.ai/hackathon/berlin/data/challenge1-b37-segregation.tsv

Samples ISDBM322015 to ISDBM322018 are son, father, mother, sister. It holds 68
HIGH-effect records the son carries with exactly one parent: 30 labelled paternal,
38 maternal, unphased. The TSV is the readable version if the VCF is awkward.

STEP 0, before anything else
Tell me whether you can fetch those URLs, and use your ClawBio skill-listing tool to
show me which relevant skills you can actually run. If you cannot fetch the files, say
so plainly and we will work from skill demo data instead. Do not pretend either way.

THEN, in order
1. Reproduce the 30 paternal / 38 maternal split. Show me the logic you used, not just
   the two numbers. If you cannot load the file, reason from the description instead
   and label it clearly as reasoning rather than measurement.
2. Use your ClawBio tools to describe and run a relevant variant-interpretation skill on
   its demo data. Show me how it distinguishes variants that are DOCUMENTED rare from
   variants with NO population-frequency data at all. That distinction is the whole
   point: absence of a frequency is not evidence of rarity.
3. Build me an abstention list. For the pedigree, what can this data NOT support, and
   why. There is no phenotype, no HPO terms, no valid population-frequency layer, and
   the effect annotation is historical rather than current clinical evidence.

RULES
Never call anything rare, pathogenic, diagnostic, de novo or compound heterozygous.
The parent-of-origin labels are unphased teaching labels, not molecular phase.
Every claim must trace to something you actually ran or read. If you cannot verify
something, say so plainly instead of hedging. An honest "I cannot determine this"
scores higher today than a confident guess.

Start with step 0.
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

??? note "Running locally instead, if you prefer your own machine"

    You do not need any of this: the hosted agent is the supported route. But if you
    would rather work on your own machine, clone ClawBio, install `uv`
    (`curl -LsSf https://astral.sh/uv/install.sh | sh`) and run these directly. All were
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

### Paste this into the BioNeMo Research Agent

```text
I'm at a genomics hackathon. You are my analysis partner for the next three hours.

CHALLENGE: A cancer target you would defend.

The premise: the literature will support almost any gene if you go looking for support.
The hard part is the counter-argument. I want targets you have genuinely tried to kill.

STEP 0, before anything else
Use your ClawBio skill-listing tool to show me which oncology, target-evidence and
literature skills you can actually run. Tell me whether you can query public APIs
(UCSC Xena, Open Targets, PubMed, ClinicalTrials.gov) and whether you can fetch a URL
to verify a citation. Answer from what you can see, not from what you assume.

THEN, in order
1. Pick a TCGA tumour type with me. Get tumour versus normal expression and survival
   association for a candidate gene set, using whichever of your tools can reach that
   data. Show me the numbers and where they came from.
2. Shortlist three candidate targets. For each one, build the case FOR and the case
   AGAINST with equal effort. I want the against column to be as full as the for column.
3. Kill one target explicitly. Tell me exactly what evidence killed it. This is the part
   I will demo, so make it sharp.
4. Check prior art: is somebody already running a trial on your surviving target?

THE HARD RULE
Every PMID or citation you give me must resolve to a real paper. Before you show me any
citation, verify it exists and tell me how you verified it. If you cannot verify a
citation, do not cite it: say "I could not verify a source for this claim" and drop the
claim. A fabricated citation puts this project out of contention for first place, and a
persuasive fake is worse than no citation at all.

Build that verification step into your workflow and show it running when we demo.

Start with step 0.
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

??? note "Running locally instead, if you prefer your own machine"

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

### Paste this into the BioNeMo Research Agent

```text
I'm at a genomics hackathon. You are my analysis partner for the next three hours.

CHALLENGE: Whose genome does this polygenic score fail?

The premise: a polygenic score trained on one population does not simply become less
accurate elsewhere, it becomes uninterpretable. I want to find where that happens and
build the behaviour that responds to it.

STEP 0, before anything else
Use your ClawBio skill-listing tool to show me what you can run. I am looking for the
polygenic score skill and the equity or ancestry skills. They may be under short
aliases like "prs" and "equity" rather than their full names. Describe each one's
contract before you run it, and tell me what inputs it will and will not accept.

THEN, in order
1. Run the polygenic score skill on its demo data. Then find, in its own output, the
   reference population for each score. Every one of them is EUR. Show me that, and
   show me that it still returns a confident percentile regardless of whose genome
   went in. Disclosure is not abstention, and the gap between them is this challenge.
2. Quantify the gap rather than asserting it. Use the ancestry and equity skills to get
   real numbers: population representation, FST between populations, heterozygosity.
   Give me a figure I can put on screen.
3. Build the deliverable: a wrapper or decision rule that REFUSES to report a percentile
   when the individual's ancestry is too far from the score's reference population.
   Pick a threshold, justify it from the numbers in step 2, and demo it firing.

THE POINT
The plot is not the deliverable. The refusal is the deliverable. End by showing me it
declining to answer, with a message a clinician could actually act on.

RULES
Every number must come from something you ran, not from your training data. If a skill
will not accept an input, tell me the boundary rather than working around it silently.
An honest "I cannot score this person" is the winning output today.

Start with step 0.
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

??? note "Running locally instead, if you prefer your own machine"

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

    Standing up an open model on Nebius Serverless and having an agent genuinely call it
    counts directly towards the implementation criterion. You are not choosing between
    doing science and doing infrastructure.

    If you go this way, start it at 13:20 rather than at 15:00, and ask in `#berlin-help`
    early rather than at 16:00.

## What "done" looks like

Whichever challenge you picked, a finished demo is one where a sceptical person in the
room can ask **"how do you know that?"** about any step on screen and get an answer.

Concretely, by 16:40 you want:

1. It runs live, on real data, in front of people.
2. Every claim traces to a source, and the sources resolve.
3. There is at least one input where it correctly says it cannot answer.
4. It does something that was not obvious before you built it.

Point three is the one teams skip and the one that impresses a jury. Build a deliberate
failure case and demo it on purpose.

## Judging

**A jury picks three winners.** The room picks a fourth, the community prize.

Three criteria, weighted equally, and they apply the same way to all challenges.

| Criterion | The question |
|-----------|--------------|
| **Originality** | Is this a genuinely new angle, or a familiar demo with new branding? |
| **Impact** | If it worked at scale, would it change what someone can actually do? |
| **Nebius and ClawBio implementation** | How well does it use the agent, the skill library and the Nebius stack? A shell script in a trenchcoat is not an agentic workflow. |

One hard rule across all challenges: **claims that cannot be checked do not count.** A
confident answer with an invented source scores below an honest abstention, and in
Challenge 2 an unresolvable PMID puts a project out of contention for first place.

What that means in practice, whichever criterion you are chasing: demo it live on real
data rather than on slides, make the provenance visible, and show the case where it
correctly refuses to answer.

## Submitting

Post in `#berlin-demos` **before 16:40** with your repo link and one line describing what
you built. Demos start at 17:00 and the order is fixed at the freeze, so late submissions
do not get a slot.

If you took Route A, also open your pull request against
[ClawBio](https://github.com/ClawBio/ClawBio); see [Submit](../submit.md) for the
mechanics.

Submissions are collected after the event into a write-up of what the room built.
