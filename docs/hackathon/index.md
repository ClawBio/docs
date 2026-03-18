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

## Objectives

By the end of this hackathon, you will have:

1. **Built a working bioinformatics skill** that any AI agent can discover and run, with a SKILL.md contract, demo data, and a CLI endpoint
2. **Experienced agentic development first-hand** using coding assistants and AI agents to accelerate your work, not replace it
3. **Contributed to an open-source project** with a pull request to the ClawBio repository that others can use and build on
4. **Connected with a cross-disciplinary community** spanning AI engineering, genomics, proteomics, clinical diagnostics, and epidemiology across Imperial, KCL, the Crick, UCL, and industry

Whether you are an AI engineer who has never touched genomic data or a genomics researcher who has never used an AI agent, you will leave with a concrete, publishable artefact and practical experience bridging both worlds.

---

## Three Themes

This hackathon explores the intersection of genomics and agentic AI:

1. **Gaps in genomics tools**: Where do current bioinformatics pipelines fail? What analyses are still manual, brittle, or unreproducible? Build a skill that fills one of those gaps.
2. **Trustworthy agentic approaches**: How do we make AI agents safe for genomics? Encode domain decisions, safety rules, and reproducibility into skills that agents can call without hallucinating.
3. **Accessible complexity**: Genomics generates vast, complex data. Build skills that present results clearly, so researchers and clinicians can act on them.

---

## What You'll Build

A **ClawBio skill**: a self-contained bioinformatics module that any AI agent can discover, understand, and run. Each skill is defined by a `SKILL.md` file that encodes domain expertise in a machine-readable format.

## What to Bring

- A laptop with Python 3.11+ installed
- A GitHub account
- Curiosity about genomics, bioinformatics, or agentic AI (no genomics background required for several tracks below)

Food and drinks will be provided (pizza at 13:30).

---

## Timetable

| Time | What | Details |
|------|------|---------|
| **12:00** | **Doors open** | Arrive, get set up, connect to WiFi |
| **12:30** | **Welcome** | Nathan Skene (Imperial) and Manuel Corpas (Westminster) |
| **12:45** | **[Overview of the day](presentation/)** | Themes, tracks, how submissions work |
| **13:15** | **Databricks** | Toz Ozturk (Databricks) -- genomics on Databricks (~15 min) |
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

Two guided tutorials are available to get you started:

1. **[Agentic Tools Tutorial](agentic-tools.md)** -- How AI coding agents work, setup options (GitHub Copilot, Claude Code, OpenCode), your first AI-assisted analysis, and context management tips. Adapted from Jay Moore's Skills Cookbook.
2. **[ClawBio Setup](setup.md)** -- Clone ClawBio, run a demo skill, then build your own following the step-by-step guide.

Both paths converge at the same goal: a working skill you can submit as a PR.

---

## Quick Path

| Step | Time | What |
|------|------|------|
| 1. [Setup](setup.md) | 10 min | Clone repo, install dependencies, run a demo |
| 2. [Your First Skill](first-skill.md) | 20 min | Scaffold a skill, write SKILL.md, add demo data |
| 3. [Add Python](add-python.md) | 20 min | Implement the skill logic with a CLI endpoint |
| 4. [Test and Submit](submit.md) | 10 min | Validate, test, open a PR |

Also see the [Presentation](presentation/) for the full-screen slide deck.

---

## Choose Your Track

We have attendees ranging from AI agent engineers with no genomics background to researchers with 40+ years in computational biology. Pick the track that fits you.

### Track A: AI Engineers New to Genomics

You build agents, automation, and APIs professionally. You just haven't touched genomic data before. These skills let you apply your engineering strengths to biology using public APIs, no wet-lab knowledge required.

- [PubMed Research Summariser](projects/pubmed-summariser.md) -- query PubMed API, return structured summary of recent findings
- [Clinical Trial Finder](projects/clinical-trial-finder.md) -- query ClinicalTrials.gov, return active trials with phase and eligibility
- [Drug Label Parser](projects/drug-label-parser.md) -- extract PGx warnings from FDA drug labels (DailyMed API)
- [Variant Frequency Dashboard](projects/variant-frequency.md) -- query gnomAD, visualise allele frequencies across populations
- [Multi-Database Aggregator](projects/multi-db-aggregator.md) -- federate queries across ClinVar, gnomAD, Open Targets

### Track B: Genomics Researchers New to Agentic AI

You work with genomic data daily. Wrap your existing expertise into a skill that anyone can run reproducibly.

- [Variant Annotation Pipeline](projects/variant-annotation.md) -- annotate a VCF with ClinVar significance, gnomAD frequencies, gene impact
- [QC Report Generator](projects/qc-report.md) -- parse FastQC output, produce pass/fail report with thresholds
- [Differential Expression Wrapper](projects/de-wrapper.md) -- PyDESeq2 workflow with volcano plots and sensible defaults
- [Gene Set Enrichment](projects/gene-set-enrichment.md) -- Enrichr API for KEGG/Reactome/GO pathway ranking
- [Single-Cell Cluster Annotator](projects/cell-type-annotator.md) -- suggest cell type labels from marker gene databases

### Track C: Proteomics and Multi-Omics

ClawBio currently has zero proteomics skills. Build the first one.

- [Protein Interaction Mapper](projects/protein-interaction.md) -- STRING API to PPI network with hub scores and figures
- [Mass Spec QC Skill](projects/mass-spec-qc.md) -- parse MaxQuant/DIA-NN output, generate quality report
- [Phosphoproteomics Enricher](projects/phospho-enricher.md) -- kinase-substrate enrichment from phosphosite list
- [Protein Domain Annotator](projects/protein-domain.md) -- UniProt + InterPro + AlphaFold domain map

### Track D: Clinical and Diagnostic Applications

For clinical genomics, molecular diagnostics, and health data backgrounds.

- [ACMG Variant Classifier](projects/acmg-classifier.md) -- implement the 28-criteria ACMG/AMP pathogenicity framework
- [Pharmacogenomics Interaction Checker](projects/pgx-interaction-checker.md) -- genotype + medication list to CPIC interaction report
- [Diagnostic Yield Calculator](projects/diagnostic-yield.md) -- HPO phenotype terms to ranked candidate genes
- [Tumour Mutational Burden](projects/tmb-calculator.md) -- somatic VCF to TMB score with MSI estimation

### Track E: Epidemiology and Public Health

Population-level data, outbreak analysis, and health equity.

- [Outbreak Phylogenetic Clusterer](projects/outbreak-clusterer.md) -- consensus sequences to NJ tree and transmission clusters
- [Vaccine Equity Scorer](projects/vaccine-equity.md) -- vaccination coverage equity analysis using HEIM framework
- [GBD Disease Burden Visualiser](projects/gbd-visualiser.md) -- IHME data to DALYs, prevalence, and regional trends
- [Antimicrobial Resistance Profiler](projects/amr-profiler.md) -- detect AMR genes from metagenomic reads (CARD database)

---

## Not Sure Which Track?

Start with [Setup](setup.md) and run a few demos. See what clicks. Then pick a skill idea, or invent your own. The best skills come from scratching your own itch: what analysis do you do repeatedly that could be a one-command tool?

If you want to team up, find someone from a different track. An AI engineer paired with a genomics researcher is a powerful combination.

---

## Judging Criteria

Skills will be evaluated on:

1. **Domain correctness** (40%): Does the SKILL.md encode real domain decisions? Are thresholds evidence-based?
2. **Reproducibility** (25%): Does demo data produce consistent results? Is the environment specified?
3. **Usefulness** (20%): Would a researcher actually use this?
4. **Code quality** (15%): Clean, readable, well-structured

---

## Communication

- **On the day**: WhatsApp group (link shared at the venue) and Discord with RoboTerri
- **GitHub**: [ClawBio/ClawBio Discussions](https://github.com/ClawBio/ClawBio/discussions)
- **Discord**: [discord.gg/EEp4Neaz](https://discord.gg/EEp4Neaz)
- **Telegram**: [ClawBio Contributors](https://t.me/ClawBioContributors)
