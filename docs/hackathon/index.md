---
title: "ClawBio Hackathon: Agentic Genomics"
description: Build a bioinformatics AI agent skill at Imperial College London
---

# ClawBio Hackathon: Agentic Genomics

![ClawBio Hackathon Banner](https://images.lumacdn.com/cdn-cgi/image/format=auto,fit=cover,dpr=2,anim=false,background=white,quality=75,width=500,height=500/event-covers/ue/48e9b48f-4f12-493c-8740-d1b7fe78b6ff.png){ width="100%" style="border-radius: 12px; margin-bottom: 1.5rem;" }

**19 March 2026 | 12:00 -- 19:00 UTC**
**Sir Michael Uren Hub, Imperial College London**

Organised by **Jay Moore**, **Manuel Corpas**, **Nathan Skene**, and **Josh Beale**.

[Register on Luma](https://luma.com/kolhdoi9){ .md-button .md-button--primary }

---

## The Problem

Modern bioinformatics knowledge is fragmented across papers, scripts, and private pipelines. Reproducing even simple analyses often requires reconstructing hidden decisions from incomplete documentation. Only about 1 in 4 computational biology papers can be reproduced without contacting the authors (Garijo et al., PLOS ONE 2013; Collberg and Proebsting, 2016). Meanwhile, general-purpose LLMs hallucinate gene-drug associations, use outdated clinical guidelines, and produce results with no audit trail.

## What is ClawBio?

ClawBio proposes a different unit of knowledge: a **skill** that packages the code, the scientific assumptions, the test data, and the execution contract in one inspectable artefact.

Each skill includes:

- A **SKILL.md** contract that explains the scientific decisions the tool makes (thresholds, databases, safety rules)
- **Demo data** that anyone can run without their own files
- A **Python script** with `--input`, `--output`, and `--demo` flags
- A **reproducibility bundle**: `commands.sh`, `environment.yml`, and `checksums.sha256`

SKILL.md is not just documentation. It is the contract that tells humans and AI agents how the skill should be used, what assumptions it makes, and when it should refuse to run.

---

## Who is this for?

| You are... | You already know | You do not need to know | Good first project |
|------------|-----------------|------------------------|--------------------|
| **AI / software engineer** | APIs, Python, automation | Any biology or genomics | [PubMed Summariser](projects/pubmed-summariser.md), [Clinical Trial Finder](projects/clinical-trial-finder.md) |
| **Genomics researcher** | VCFs, pipelines, domain expertise | Agentic AI or SKILL.md | [Variant Annotation](projects/variant-annotation.md), [QC Report](projects/qc-report.md) |
| **Proteomics / multi-omics** | Mass spec, protein databases | ClawBio (no skills exist yet) | [Protein Interaction Mapper](projects/protein-interaction.md), [Protein Domain Annotator](projects/protein-domain.md) |
| **Clinical / diagnostics** | Variant classification, PGx | Agent frameworks | [PGx Interaction Checker](projects/pgx-interaction-checker.md) |
| **Epidemiology / public health** | Population data, outbreak analysis | Python scripting (helpers available) | [Vaccine Equity Scorer](projects/vaccine-equity.md), [GBD Visualiser](projects/gbd-visualiser.md) |

---

## Quick Path

<div class="tutorial-cards">

<a class="tutorial-card" href="setup/">
  <div class="tutorial-card__header">
    <span class="tutorial-card__number">01</span>
    <span class="difficulty-badge difficulty-badge--beginner">Beginner</span>
    <span class="time-estimate">10 min</span>
  </div>
  <h3 class="tutorial-card__title">Setup</h3>
  <p class="tutorial-card__desc">Clone repo, install dependencies, run a demo.</p>
</a>

<a class="tutorial-card" href="first-skill/">
  <div class="tutorial-card__header">
    <span class="tutorial-card__number">02</span>
    <span class="difficulty-badge difficulty-badge--beginner">Beginner</span>
    <span class="time-estimate">20 min</span>
  </div>
  <h3 class="tutorial-card__title">Your First Skill</h3>
  <p class="tutorial-card__desc">Scaffold a skill, write SKILL.md, add demo data.</p>
</a>

<a class="tutorial-card" href="add-python/">
  <div class="tutorial-card__header">
    <span class="tutorial-card__number">03</span>
    <span class="difficulty-badge difficulty-badge--intermediate">Intermediate</span>
    <span class="time-estimate">20 min</span>
  </div>
  <h3 class="tutorial-card__title">Add Python</h3>
  <p class="tutorial-card__desc">Implement the skill logic with a CLI endpoint.</p>
</a>

<a class="tutorial-card" href="submit/">
  <div class="tutorial-card__header">
    <span class="tutorial-card__number">04</span>
    <span class="difficulty-badge difficulty-badge--beginner">Beginner</span>
    <span class="time-estimate">10 min</span>
  </div>
  <h3 class="tutorial-card__title">Test and Submit</h3>
  <p class="tutorial-card__desc">Validate, test, open a PR.</p>
</a>

</div>

Most participants will submit their first skill in **90 to 120 minutes**. The times above assume your environment is already set up. First-time Git or GitHub users should allow extra time; helpers will be available throughout.

**Starter template**: copy `templates/SKILL-TEMPLATE.md` into your skill directory to get the correct structure immediately. See [Your First Skill](first-skill.md) for the full walkthrough.

**Example completed skill**: see the [NutriGx Advisor PR](https://github.com/ClawBio/ClawBio/pull/1) by @drdaviddelorenzo, the first community contribution. It shows exactly what a successful submission looks like: SKILL.md with domain decisions, demo data, Python script, and a clean PR.

---

## What You'll Walk Away With

- **If you are a genomics researcher**: your existing pipeline wrapped as a one-command, reproducible tool that any AI agent or colleague can run without calling you.
- **If you are an AI engineer**: a working bioinformatics skill built on real public APIs, with domain decisions you can point to as evidence you understand the biology.
- **If you work in proteomics**: the first proteomics skill in ClawBio. Pioneer status.
- **If you work in clinical diagnostics**: a prototype skill with explicit safety rules and CPIC evidence levels, demonstrating how agentic tools can handle sensitive domain logic.
- **If you work in epidemiology or public health**: a population-level analysis tool with visual output that non-specialists can act on.

Everyone leaves with a concrete open-source artefact: a working skill, a documented scientific contract, and a pull request.

---

## What counts as a successful submission?

A valid hackathon submission is:

- [ ] One new skill directory under `skills/`
- [ ] A `SKILL.md` with frontmatter (name, version, inputs, outputs) and three body sections (Domain Decisions, Safety Rules, Agent Boundary)
- [ ] Synthetic demo data (never real patient data)
- [ ] A runnable `--demo` command that produces output
- [ ] A pull request to [github.com/ClawBio/ClawBio](https://github.com/ClawBio/ClawBio)

That is it. You do not need tests, figures, or a complete pipeline. A focused, well-documented skill with clear domain decisions is better than an ambitious but incomplete one.

---

## Three Themes

1. **Gaps in genomics tools**: What analyses are still manual, brittle, or unreproducible? Build a skill that fills one of those gaps.
2. **Trustworthy agentic approaches**: How do we make AI agents safe for biology? Encode domain decisions and safety rules into SKILL.md so agents execute with proven logic, not hallucinations.
3. **Accessible complexity**: Genomics data is vast and complex. Build skills that present results so clearly that a non-specialist can act on them.

---

## What to Bring

- A laptop with **Python 3.11+** and **Git** installed
- A **GitHub account**
- Curiosity about genomics, bioinformatics, or agentic AI (no genomics background required for several tracks)

**Recommended before arrival** (saves time on the day):

```bash
# Install GitHub CLI and authenticate
brew install gh          # macOS
gh auth login            # follow the prompts

# Clone the repo and run a demo
git clone https://github.com/ClawBio/ClawBio.git
cd ClawBio
pip install -r requirements.txt
python skills/pharmgx-reporter/pharmgx_reporter.py --demo
```

If you do not have `gh` installed, you can submit your PR through the GitHub web interface instead. Both routes are covered in the [Submit](submit.md) guide.

Food and drinks will be provided (pizza at 13:30).

---

## Timetable

| Time | What | Details |
|------|------|---------|
| **12:00** | **Doors open** | Arrive, get set up, connect to WiFi |
| **12:30** | **Welcome** | Nathan Skene (Imperial) and Manuel Corpas (Westminster) |
| **12:45** | **[Overview of the day](presentation/)** | Themes, tracks, how submissions work |
| **13:15** | **Scaling genomics** | Toz Ozturk (Databricks) -- how cloud infrastructure handles large-scale genomic workloads (~15 min) |
| **13:30** | **Pizza** | Lunch break, keep hacking if you want |
| **14:00** | **Guided Tutorial (Jay Moore)** | Hands-on with helpers. Follow the [Agentic Tools tutorial](agentic-tools.md) and the [ClawBio Setup](setup.md) |
| **14:30** | **Build** | Work on your skill (solo or in teams). Helpers circulate. |
| **15:30** | **Breakout Tables** | Rotate between themed discussions (pick 1-2): |
|  | | *The future of reproducibility in biological research* |
|  | | *Handling sensitive biodata with OpenClaw/ClawBio* |
|  | | *Your Theme?* (propose your own) |
| **16:30** | **Build** | Final stretch. Polish your skill, write SKILL.md, test demo mode. |
| **17:30** | **Show and Tell** | Each team/individual presents their skill (~3 min each) |
| **18:30** | **Menti Poll and Wrap-up** | Community vote, closing remarks |
| **19:00** | **End** | |

---

## Resources

Two guided tutorials are available to get you started. Both paths converge at the same goal: a working skill you can submit as a PR.

<div class="tutorial-cards">

<a class="tutorial-card" href="agentic-tools/">
  <div class="tutorial-card__header">
    <span class="difficulty-badge difficulty-badge--intermediate">Intermediate</span>
    <span class="time-estimate">15 min</span>
  </div>
  <h3 class="tutorial-card__title">Agentic Tools Tutorial</h3>
  <p class="tutorial-card__desc">How AI coding agents work, setup options (GitHub Copilot, Claude Code, OpenCode), your first AI-assisted analysis, and context management tips.</p>
</a>

<a class="tutorial-card" href="setup/">
  <div class="tutorial-card__header">
    <span class="difficulty-badge difficulty-badge--beginner">Beginner</span>
    <span class="time-estimate">10 min</span>
  </div>
  <h3 class="tutorial-card__title">ClawBio Setup</h3>
  <p class="tutorial-card__desc">Clone ClawBio, run a demo skill, then build your own following the step-by-step guide.</p>
</a>

</div>

---

## Choose Your Track

We have attendees ranging from AI agent engineers with no genomics background to researchers with 40+ years in computational biology. Pick the track that fits you. Each project is labelled as a **90-minute build** (achievable in the afternoon) or a **stretch build** (ambitious, likely a prototype).

### Track A: AI Engineers New to Genomics

You build agents, automation, and APIs professionally. You just haven't touched genomic data before. These skills let you apply your engineering strengths to biology using public APIs, no wet-lab knowledge required.

**90-minute builds:**

- [PubMed Research Summariser](projects/pubmed-summariser.md) -- query PubMed API, return structured summary of recent findings
- [Clinical Trial Finder](projects/clinical-trial-finder.md) -- query ClinicalTrials.gov, return active trials with phase and eligibility
- [Variant Frequency Dashboard](projects/variant-frequency.md) -- query gnomAD, visualise allele frequencies across populations
- [Protein Domain Annotator](projects/protein-domain.md) -- UniProt + InterPro + AlphaFold domain map

**Stretch builds:**

- [Drug Label Parser](projects/drug-label-parser.md) -- extract PGx warnings from FDA drug labels (DailyMed API)
- [Multi-Database Aggregator](projects/multi-db-aggregator.md) -- federate queries across ClinVar, gnomAD, Open Targets

### Track B: Genomics Researchers New to Agentic AI

You work with genomic data daily. Wrap your existing expertise into a skill that anyone can run reproducibly.

**90-minute builds:**

- [QC Report Generator](projects/qc-report.md) -- parse FastQC output, produce pass/fail report with thresholds
- [Gene Set Enrichment](projects/gene-set-enrichment.md) -- Enrichr API for KEGG/Reactome/GO pathway ranking
- [Differential Expression Wrapper](projects/de-wrapper.md) -- PyDESeq2 workflow with volcano plots and sensible defaults

**Stretch builds:**

- [Variant Annotation Pipeline](projects/variant-annotation.md) -- annotate a VCF with ClinVar significance, gnomAD frequencies, gene impact
- [Single-Cell Cluster Annotator](projects/cell-type-annotator.md) -- suggest cell type labels from marker gene databases

### Track C: Proteomics and Multi-Omics

ClawBio currently has zero proteomics skills. Build the first one. If you need a starting point, the [Protein Interaction Mapper](projects/protein-interaction.md) is a good template: it follows the same pattern as existing skills but queries the STRING API instead of genomic databases.

**90-minute builds:**

- [Protein Interaction Mapper](projects/protein-interaction.md) -- STRING API to PPI network with hub scores and figures
- [Protein Domain Annotator](projects/protein-domain.md) -- UniProt + InterPro + AlphaFold domain map

**Stretch builds:**

- [Mass Spec QC Skill](projects/mass-spec-qc.md) -- parse MaxQuant/DIA-NN output, generate quality report
- [Phosphoproteomics Enricher](projects/phospho-enricher.md) -- kinase-substrate enrichment from phosphosite list

### Track D: Clinical and Diagnostic Applications

For clinical genomics, molecular diagnostics, and health data backgrounds. **All clinical track outputs are educational prototypes only. They must not be used for clinical decision-making or patient management.**

**90-minute builds:**

- [Pharmacogenomics Interaction Checker](projects/pgx-interaction-checker.md) -- genotype + medication list to CPIC interaction report

**Stretch builds (prototype scope only):**

- [ACMG Variant Classifier](projects/acmg-classifier.md) -- prototype a subset of the 28-criteria ACMG/AMP pathogenicity framework
- [Diagnostic Yield Calculator](projects/diagnostic-yield.md) -- HPO phenotype terms to ranked candidate genes
- [Tumour Mutational Burden](projects/tmb-calculator.md) -- somatic VCF to TMB score with MSI estimation

### Track E: Epidemiology and Public Health

Population-level data, outbreak analysis, and health equity.

**90-minute builds:**

- [Vaccine Equity Scorer](projects/vaccine-equity.md) -- vaccination coverage equity analysis using HEIM framework
- [GBD Disease Burden Visualiser](projects/gbd-visualiser.md) -- IHME data to DALYs, prevalence, and regional trends

**Stretch builds:**

- [Outbreak Phylogenetic Clusterer](projects/outbreak-clusterer.md) -- consensus sequences to NJ tree and transmission clusters
- [Antimicrobial Resistance Profiler](projects/amr-profiler.md) -- detect AMR genes from metagenomic reads (CARD database)

---

## Not Sure Which Track?

- You have never written a bioinformatics pipeline: **Track A**
- You work with VCF files or NGS data daily: **Track B**
- Your primary data is protein or mass spec: **Track C**
- You interpret genetic variants in a clinical context: **Track D**
- Your work involves populations, surveillance, or disease burden: **Track E**
- None of the above: **pick any 90-minute build** from any track, or invent your own

The best skills come from scratching your own itch: what analysis do you do repeatedly that could be a one-command tool? If you want to team up, find someone from a different track. An AI engineer paired with a genomics researcher is a powerful combination.

---

## Judging Criteria

Skills will be evaluated on:

1. **Domain correctness** (40%): Does the SKILL.md encode real domain decisions? Are thresholds evidence-based?
2. **Reproducibility** (25%): Does demo data produce consistent results? Is the environment specified?
3. **Usefulness** (20%): Would a researcher actually use this?
4. **Code quality** (15%): Clean, readable, well-structured

---

## Communication

- **Primary channel**: [Discord](https://discord.gg/EEp4Neaz) -- for technical help, PR reviews, and post-event community. Monitored by maintainers.
- **On the day**: WhatsApp group (link shared at the venue) for logistics
- **GitHub**: [ClawBio/ClawBio Discussions](https://github.com/ClawBio/ClawBio/discussions) for longer-form questions and skill proposals
