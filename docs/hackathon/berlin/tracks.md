---
title: "Berlin Challenges"
description: Three genomics challenges for the ClawBio + Nebius hackathon in Berlin, with starter briefs, real public data, and how demos are judged.
---

# Challenges

<div class="tutorial-card__header">
  <span class="difficulty-badge difficulty-badge--event">Event</span>
  <span class="time-estimate">3 h 40 min build time</span>
</div>

Three challenges, each a real problem in genomics that is still open. Pick one. The
same prize pool applies across all three and the judging criteria are identical.

The challenge is the biology. **How** you build is a separate choice, and you make it
inside your track: a new skill, a chain of existing ones, or an open model you host
yourself. See [How you build it](#how-you-build-it) below.

!!! info "Where Nebius actually comes in"

    Worth understanding before you arrive, because it is not obvious.

    ClawBio skills are **plain Python**. Most need no language model at all:
    `rare-high-impact-variants` reads a VCF and does arithmetic. Running skills by hand
    in a terminal consumes no Nebius credit and, on its own, is not an agentic workflow.

    Nebius enters at two points:

    1. **The agent.** You are not meant to type these commands. You are meant to ask an
       agent, and the agent reads each `SKILL.md`, decides which skills to call, chains
       them, and interprets what comes back. That agent runs on a model served by Nebius
       Token Factory. This is where your credits go and where the interesting failures
       live.
    2. **Hosted models as tools.** A skill can call a model over HTTP. The working
       reference in the library is the `gi-*` family, which reaches a hosted DNA language
       model via a base URL and a key. Copy that shape, point it at your own Nebius
       Serverless endpoint, and you have Route C.

    The commands in each brief exist so you can see what a skill produces and check your
    environment. They are the floor, not the project. Criterion four at judging, *did it
    need agents*, is asking exactly this.

    **Start with the [Nebius Quickstart](nebius-quickstart.md).** It puts a Token Factory
    model in charge of these skills in about fifteen minutes, and every challenge below
    builds on it.

!!! warning "Scope for the clock, not for the idea"

    You have 3 hours 40 minutes, 13:20 to 17:00. That is the single hardest constraint
    of the day and it is what most hackathon projects get wrong.

    Every brief below has an hour-one win and a stretch. Get the hour-one win working
    first, even if it is boring. Decide at 15:00 what you are cutting. A team that
    demos one thing working end to end beats a team that demos four things half-built,
    every time.

### Running the commands

Every command in the briefs was run on a **source checkout** on 12 August 2026 and is
reproduced exactly as it worked:

```bash
git clone https://github.com/ClawBio/ClawBio.git && cd ClawBio
uv sync
```

Two things that catch people out:

- **Use `uv run python`, not a bare `python3`.** A system Python will be missing
  `requests` and friends and you will lose ten minutes to it.
- **The runner's short names are not the directory names.** `clawbio.py run` registers 49
  aliases: `prs` is `gwas-prs`, `acmg` is `clinical-variant-reporter`, `rdoutlier` is
  `rare-disease-rnaseq`. `uv run python clawbio.py list` shows them. The direct
  `skills/<name>/<script>.py` form works for the skills shown below, so the briefs use
  that form.

The local clone is the canonical environment for the day, so the paths below are the
paths you will use. If Nebius confirms a hosted alternative, it will be announced in the
final Luma update and `#berlin-general` only after the same commands have been tested
there.

---

## Challenge 1: End the diagnostic odyssey

**The problem.** A family with an undiagnosed condition waits, on average, years for an
answer. The sequencing is not the bottleneck. Interpretation is: hundreds of candidate
variants, most of them uncertain, and a pipeline that has to decide which ones a human
should ever see.

**Headline brief.** Use the publicly consented four-person Corpas exome pedigree: son,
father, mother and sister. Treat the son as a teaching proband, show the inheritance
logic and make the evidence behind every filter visible. Then state what the data does
not support. There is no phenotype or HPO file and this is not an undiagnosed clinical
case, so a defensible agent must refuse to turn segregation evidence into a diagnosis.

That last part is the point. Any tool can output a ranking. Very few say which variants
they were not entitled to have an opinion about.

| | |
|---|---|
| **Hour one** | Start from the supplied strict 68-record b37 quartet subset. Reproduce the 30 paternal and 38 maternal unphased teaching labels, then make every filter visible. |
| **Hour two** | Add one missing evidence layer, such as build-matched population frequency or updated consequence annotation. Keep it separate from the inherited teaching labels. |
| **Stretch** | Add an explicit abstention list with a reason attached to every entry. Refuse diagnosis without phenotype or HPO data, and do not claim molecular phase or compound heterozygosity. |

**The commands.** Every one below was run on a source checkout on 12 August and produced
output. Run them from the ClawBio directory.

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

Read `/tmp/rhiv/report.md` first. It already separates variants that are *documented* rare
from variants with *no frequency data at all*, and says why that distinction matters. That
is your starting point, not your finish line.

The commands above are verified demonstrations on bundled synthetic data. Do not run
`vcf-annotator` over either complete Corpas source VCF: it makes serial per-variant
network calls, uses current GRCh38 services by default and does not retain the family
genotypes. Do not feed the historical quartet directly to
`rare-high-impact-variants`: it does not parse the legacy `EFF` field or provide the
missing population-frequency layer.

**The gap worth attacking.** Variants with no gnomAD frequency at all. Absence of a
frequency is not evidence of rarity, but automated pipelines routinely treat it as
though it were. On a recent audit of one such pipeline, 16 of 27 flagged
false-actionable calls were genuine instances of this. A skill that names the blind spot
is worth more than one that guesses past it.

**Other angles in this challenge**

- **Expression as the tie-breaker.** DNA leaves you with a variant of uncertain
  significance. Blood RNA can promote or demote it. Use `rare-disease-rnaseq` to find an
  expression outlier and demo one case where the RNA changes the answer.
- **The variants nobody looked at.** Most pipelines are SNV-only. Run
  `cnv-acmg-classifier` over structural and copy-number variants and report what a
  SNV-only pipeline silently drops.

**Data.** The supplied event pack contains an indexed 68-record quartet subset as the
canonical starter. It was derived from the
[joint four-person Corpas exome VCF](https://figshare.com/articles/dataset/Corpasome/693052)
using autosomal, biallelic, PASS, historical HIGH-effect, family-wide DP and GQ, and
single-parent transmission filters. The complete quartet and the
[son-only exome VCF](https://f1000.figshare.com/articles/dataset/Son_exome_files/92584)
remain provenance and extension sources, not the hour-one input. These are GRCh37
teaching data. Retain the DOI and CC BY 4.0 attribution, and remember that public human
genomes remain potentially identifiable. GIAB, ClinVar and gnomAD can provide comparison
or annotation data only when the genome build and evidence semantics are made explicit.

!!! danger "Release gate"

    Before this page is published, insert the approved retrieval URL for
    `challenge1-b37-segregation.vcf.gz` and its `.tbi` index. The VCF SHA256 is
    `c6c1185618c232d6b751dabb78a9678936f1fedf2633fbb7f35ccfa992e3dc90`.
    Do not send participants to this page until the files resolve without organiser
    credentials.

---

## Challenge 2: A cancer target you would defend

**The problem.** Target selection is where most of the money in oncology is lost. The
literature will support almost any gene if you go looking for support. The hard part is
the counter-argument.

**Headline brief.** Pick a tumour type in TCGA. Produce a shortlist of candidate targets.
For every target on the list, make the case against it as visible as the case for it. You
must demo at least one target your agent killed, and why.

| | |
|---|---|
| **Hour one** | Tumour versus normal expression and survival association for a gene set, via `xena-tcga-gene-query`. No downloads, it queries the UCSC Xena API. |
| **Hour two** | Dependency and evidence. `target-validation-scorer` for a GO/NO-GO with reasoning, `omics-target-evidence-mapper` to aggregate across public sources. |
| **Stretch** | Prior art. `clinical-trial-finder` to check whether somebody is already running this, and `pubmed-summariser` or `lit-synthesizer` for the literature. |

**The commands.** All verified on 12 August. Note that `query_tcga_api.py` takes its
global flags **before** the subcommand, which is easy to get wrong.

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

!!! warning "One extra install for the repurposing angle"

    `drug-repurposing-screen` needs `fastparquet`, which is not in the base environment:
    `uv pip install fastparquet`. Everything else above runs as-is.

!!! danger "Every PMID must resolve"

    This challenge is where language models fail most attractively. A fabricated citation
    that supports your target is worse than no citation, because it is persuasive. Any
    demo containing a PMID that does not resolve is out of contention for first place in
    this challenge, however good the rest of it is.

    Build the check in. It is three lines and it is the whole thesis of the day.

**Other angles in this challenge**

- **Repurposing.** Run `drug-repurposing-screen` on a pooled viability screen and pull
  out context-selective candidates rather than pan-lethal ones. Guide-level count tables
  from public CRISPR screens are single CSVs and download in seconds.
- **Reproduce and disagree.** Rebuild a figure from a published TCGA analysis using the
  underlying public data, and report where your numbers differ from the paper's.
  Disagreement, stated precisely, is a result.

**Data.** TCGA via UCSC Xena, Open Targets, ClinicalTrials.gov, PubMed, public CRISPR
screens.

---

## Challenge 3: Whose genome does this fail?

**The problem.** Most of what genomics knows, it knows about Europeans. A polygenic risk
score trained on one population does not simply become less accurate elsewhere. It
becomes uninterpretable.

Run the first command below before you arrive and look at what comes back. Every score is
labelled `Reference population: EUR`, which is honest, and every score still returns a
confident percentile regardless of whose genome went in. Disclosure is not abstention.
The distance between those two is this challenge.

**The commands.** All verified on 12 August.

```bash
# Six polygenic scores from the PGS Catalog. Then look at what it admits to.
uv run python skills/gwas-prs/gwas_prs.py --demo --output /tmp/prs
grep -i "reference population" /tmp/prs/prs_report.md   # EUR, on every single score

# Ancestry decomposition against the Simons Genome Diversity Project
uv run python skills/claw-ancestry-pca/ancestry_pca.py --demo --output /tmp/pca

```

`equity-scorer` has no `--demo` because it works across a cohort, but the repo ships one:

```bash
# HEIM diversity metrics, FST between populations, ancestry PCA
uv run python skills/equity-scorer/equity_scorer.py \
  --input examples/demo_populations.vcf \
  --pop-map examples/demo_population_map.csv \
  --output /tmp/equity && cat /tmp/equity/report.md
```

Verified on 12 August: HEIM score 76.2/100, with pairwise FST and a PCA.

**Headline brief.** Take a published score from the PGS Catalog. Apply it across
ancestries. Find the point at which it stops meaning anything, and quantify it rather
than asserting it. Then build the behaviour that matters: an agent that declines to
report a score when the reference data does not support one.

The plot is not the deliverable. The refusal is the deliverable.

| | |
|---|---|
| **Hour one** | Compute a PGS Catalog score with `gwas-prs`, on one individual, end to end. |
| **Hour two** | Stratify. `claw-ancestry-pca` against the Simons Genome Diversity Project, then `equity-scorer` for heterozygosity, FST and composite HEIM metrics. |
| **Stretch** | Wire the abstention in, with a stated threshold and a message a clinician could act on. Show it firing. |

**Other angles in this challenge**

- **The blind spot, genome-wide.** Which variants in a genome have no frequency data in
  any gnomAD population, and how does that count differ by the ancestry of the person
  being sequenced. This is the same gap as Challenge 1, measured across a population
  rather than within a family.
- **Audit a report generator.** Feed a clinical or consumer report tool an input that is
  too thin to support an ancestry call, a few dozen ancestry-informative markers, and
  see whether it abstains or produces a confident pie chart. Most produce the pie chart.
  Document the failure and propose the guardrail.

**Data.** PGS Catalog, 1000 Genomes Phase 3, Simons Genome Diversity Project, gnomAD,
GWAS Catalog.

---

## Open challenge

Bring your own problem. Same rules, same judging, same prize pool.

If you work on a biology that is not covered above, plants, microbes, ageing, proteomics,
neuro, bring the question and we will help you scope it to the clock at 13:05. The
library has more than 90 skills and a bridge to more than 8,000 Galaxy tools, so the odds that
nothing touches your field are low.

Two conditions. Public data only, and the question has to be one where being wrong
matters, because that is what the judging rewards.

---

## How you build it

The challenge is the science. This is the engineering, and it is your choice inside
whichever challenge you picked.

<div class="grid cards" markdown>

- **Route A: write a new skill**

    One skill, one job, a test, a pull request against ClawBio. The best artefact to
    take home and the clearest finish line. Start from
    [Build a Skill](../first-skill.md) and the
    [SKILL.md specification](../../reference/skillmd-spec.md), or scaffold it with
    `skill-builder`.

- **Route B: chain what exists**

    Compose existing skills into a workflow that answers the question end to end, with
    provenance visible at every step. Fastest route to a working demo, and the one to
    pick if your team is new to agents.

- **Route C: host your own model**

    If participant Serverless access, billing and credits are confirmed, put an open
    biology model behind a Nebius endpoint and have a ClawBio skill call it as a tool.
    Deepest route, and the most plumbing risk. If access is not confirmed, this route is
    out for the day.

</div>

!!! tip "Serverless bonus, on any challenge"

    Any team on any challenge that stands up an open model on Nebius Serverless and has
    an agent genuinely call it gets that noted to the room at judging. You are not
    choosing between doing science and doing infrastructure.

    If you go this way, start it at 13:20 rather than at 15:00, and ask in
    `#berlin-help` early rather than at 16:00.

---

## What "done" looks like

Whichever challenge you picked, a finished demo is one where a sceptical person in the
room can ask **"how do you know that?"** about any step on screen and get an answer.

Concretely, by 17:00 you want:

1. It runs live, on real data, in front of people.
2. Every claim traces to a source, and the sources resolve.
3. There is at least one input where it correctly says it cannot answer.
4. Somebody else could run it on Wednesday from your repo.

Point three is the one teams skip and the one that wins. Build a deliberate failure case
and demo it on purpose.

---

## Data

Use public data only. Nothing participant-supplied. Public human genomes can remain
identifiable, so keep the approved teaching pack separate from attendee data and do not
upload it to an unapproved service.

| Dataset | What it is | Challenge |
|---------|-----------|-----------|
| Corpas exome quartet | Public GRCh37 joint VCF for son, father, mother and sister; teaching data, not an undiagnosed case | 1 |
| GIAB | Genome in a Bottle benchmark materials | 1, truth sets within their defined benchmark regions and variant classes |
| ClinVar | Clinical variant assertions | 1, 2 |
| gnomAD | Population allele frequencies, and their absence | 1, 3 |
| TCGA via UCSC Xena | Tumour expression, survival, clinical | 2 |
| Open Targets, ClinicalTrials.gov, PubMed | Target evidence and prior art | 2 |
| PGS Catalog | Published polygenic scores | 3 |
| 1000 Genomes, SGDP | Ancestry reference panels | 3 |
| GEO, Expression Atlas | Public expression data | Any |

The repository contains demo inputs for the exact skill commands shown in these briefs.
That does not mean every ClawBio skill bundles data or every public source has an API.
Challenge 1 also needs the separate 68-record event pack named above. Its approved link
will be included in the final Luma reminder and `#berlin-general` before the event.

---

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

---

## Submitting

Post in `#berlin-demos` before 17:00 with your repo link and one line describing what you
built. If you took Route A, also open your pull request against
[ClawBio](https://github.com/ClawBio/ClawBio); see [Submit](../submit.md) for the
mechanics.

Submissions are collected after the event into a write-up of what the room built.
