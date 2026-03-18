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
- Curiosity about genomics, bioinformatics, or agentic AI

Food and drinks will be provided.

---

## Quick Path

| Step | Time | What |
|------|------|------|
| 1. [Setup](setup.md) | 10 min | Clone repo, install dependencies, run a demo |
| 2. [Your First Skill](first-skill.md) | 20 min | Scaffold a skill, write SKILL.md, add demo data |
| 3. [Add Python](add-python.md) | 20 min | Implement the skill logic with a CLI endpoint |
| 4. [Test and Submit](submit.md) | 10 min | Validate, test, open a PR |

Also see the [Presentation](presentation.md) for context on what ClawBio is and why it exists.

---

## Skill Ideas

Not sure what to build? Here are some ideas aligned with the three themes:

### Filling Gaps in Genomics Tools
- **HLA Typer**: predict HLA alleles from genotype data
- **CNV Caller**: detect copy number variants from exome depth
- **Pathway Enricher**: gene set enrichment against KEGG/Reactome
- **Protein Interaction Mapper**: PPI network from a gene list (STRING API)

### Trustworthy Agentic Approaches
- **Drug Interaction Checker**: flag contraindicated drug pairs from a patient genotype
- **Dosing Calculator**: weight/genotype-adjusted dosing recommendations with CPIC guidelines
- **Rare Disease Matcher**: match HPO phenotype terms to candidate genes
- **AMR Profiler**: antimicrobial resistance gene detection from metagenomic reads

### Making Complexity Accessible
- **Variant Summary Dashboard**: turn a VCF into a plain-language report for non-specialists
- **Methylation Scorer**: differential methylation from array data with visual output
- **Outbreak Tracker**: phylogenetic clustering from consensus sequences with clear visualisation
- **Vaccine Coverage Scorer**: equity analysis of vaccination data across populations

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
