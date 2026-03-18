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
| **13:00** | **Databricks** | Toz Ozturk (Databricks) -- genomics on Databricks (~15 min) |
| **13:15** | **Guided Tutorial** | Hands-on with helpers. Follow the [Agentic Tools tutorial](agentic-tools.md) and the [ClawBio Setup](setup.md) |
| **13:30** | **Pizza** | Lunch break, keep hacking if you want |
| **14:00** | **Build** | Work on your skill (solo or in teams). Helpers circulate. |
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

You build agents, automation, and APIs professionally. You know how to wire systems together. You just haven't touched genomic data before. These skills let you apply your engineering strengths to real biological problems using public APIs and databases, no wet-lab knowledge required.

- **PubMed Research Summariser**: given a gene name or disease, query the PubMed API and return a structured summary of recent findings. You know API orchestration; PubMed is just another endpoint.
- **Clinical Trial Finder**: query ClinicalTrials.gov for active trials matching a gene or condition. Return structured results with eligibility, phase, and location.
- **Drug Label Parser**: extract pharmacogenomic warnings from FDA drug labels (DailyMed API). Turn unstructured PDF data into structured, queryable output.
- **Variant Frequency Dashboard**: given an rsID, query gnomAD and return allele frequencies across populations with a clear visual. Pure API work, high clinical value.
- **Multi-Database Aggregator**: federate queries across two or more public genomics APIs (ClinVar, gnomAD, Open Targets) and return a unified report. This is orchestration engineering applied to biology.

### Track B: Genomics Researchers New to Agentic AI

You work with genomic data daily. You know what good analysis looks like. You may have scripts that do useful things but are not packaged for anyone else to run. Wrap your domain expertise into a skill that an AI agent (or any colleague) can call reproducibly.

- **Variant Annotation Pipeline**: take a VCF and annotate variants with ClinVar significance, gnomAD frequencies, and gene impact. You already know how to do this; now make it a one-command skill.
- **QC Report Generator**: take FASTQ quality metrics (from FastQC or similar) and produce a pass/fail report with clear thresholds. Encode the QC decisions you make by eye every day.
- **Differential Expression Wrapper**: wrap your DESeq2/PyDESeq2 workflow into a ClawBio skill with sensible defaults, contrasts, and volcano plots. Make your analysis reproducible by someone who has never used R or Python.
- **Gene Set Enrichment**: take a gene list, run enrichment against KEGG/Reactome/GO, return ranked pathways with figures. Package the analysis you do after every experiment.
- **Single-Cell Cluster Annotator**: given a Scanpy AnnData object with clusters, suggest cell type labels using marker gene databases. Extend the existing scRNA Orchestrator skill.

### Track C: Proteomics and Multi-Omics

Several attendees work in proteomics and multi-omics. ClawBio currently has no proteomics skills, making this a high-impact area.

- **Protein Interaction Mapper**: given a gene or protein list, query STRING API and return a PPI network with visualisation and hub scores. No proteomics data needed, just API calls.
- **Mass Spec QC Skill**: parse MaxQuant or DIA-NN output and generate a quality report (peptide counts, missing values, CV distributions). If you work with mass spec data, you know what to check.
- **Phosphoproteomics Enricher**: take a list of phosphosites, run kinase-substrate enrichment, return activated kinases with confidence scores.
- **Protein Domain Annotator**: given a UniProt ID, fetch domain architecture, known variants, and structural data. Combine UniProt, InterPro, and AlphaFold APIs.

### Track D: Clinical and Diagnostic Applications

For those with clinical genomics, molecular diagnostics, or health data backgrounds.

- **ACMG Variant Classifier**: implement the ACMG/AMP evidence framework for variant pathogenicity classification. Encode the 28 criteria as explicit rules in SKILL.md.
- **Pharmacogenomics Interaction Checker**: given a patient genotype and a medication list, flag all gene-drug interactions with CPIC evidence levels. Extend the existing PharmGx Reporter.
- **Diagnostic Yield Calculator**: given a set of variants and phenotype terms (HPO), calculate the diagnostic yield and rank candidate genes. Useful for rare disease panels.
- **Tumour Mutational Burden**: calculate TMB from a somatic VCF with configurable filters (VAF, depth, region). Output includes MSI estimation and immunotherapy relevance score.

### Track E: Epidemiology and Public Health

For researchers working with population-level data, outbreak analysis, or health equity.

- **Outbreak Phylogenetic Clusterer**: given consensus sequences, build a quick neighbour-joining tree and identify transmission clusters. Visualise with a timeline.
- **Vaccine Equity Scorer**: analyse vaccination coverage data across demographic groups. Apply the HEIM equity framework from the existing Equity Scorer to public health data.
- **GBD Disease Burden Visualiser**: query the IHME Global Burden of Disease data for a condition and produce a clear summary of DALYs, prevalence, and trends across regions.
- **Antimicrobial Resistance Profiler**: detect AMR genes from metagenomic reads using public databases (CARD/ResFinder). Build on the existing Metagenomics Profiler.

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
