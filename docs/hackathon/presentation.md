---
title: ClawBio Hackathon Presentation
description: What ClawBio is, why it exists, and how to build a skill
---

# ClawBio Hackathon Presentation

![ClawBio Hackathon Banner](https://images.lumacdn.com/cdn-cgi/image/format=auto,fit=cover,dpr=2,anim=false,background=white,quality=75,width=500,height=500/event-covers/ue/48e9b48f-4f12-493c-8740-d1b7fe78b6ff.png){ width="100%" style="border-radius: 12px; margin-bottom: 1.5rem;" }

**ClawBio Hackathon: Agentic Genomics**
19 March 2026 | Sir Michael Uren Hub, Imperial College London

---

## The Problem

Reproducing a single figure from a published paper should take 30 seconds. Instead it takes weeks, or fails entirely.

```
$ git clone repo && cd repo
# Wrong Python version...
# Reference data link is dead...
# Paths hardcoded to /home/jsmith/data/
# Email first author. Wait 3 weeks.
# Give up.
```

A 2023 study found that **only 26% of computational biology papers could be reproduced** without contacting the authors.

Meanwhile, general-purpose LLMs hallucinate star allele calls, use outdated guidelines, and produce results with no audit trail. A pharmacogenomics report from ChatGPT is dangerous: it gets CYP2D6 \*4 wrong as "reduced function" when it is actually **no function**. For a patient on codeine, that is the difference between pain relief and zero therapeutic effect.

---

## The Solution: ClawBio

ClawBio is the **first bioinformatics-native AI agent skill library**. It packages published research methods as installable, composable skills that anyone can run with a single command.

```bash
python skills/pharmgx-reporter/pharmgx_reporter.py \
  --input my_23andme.txt --output report/

# 12 genes. 51 drugs. CPIC guidelines. < 1 second. SHA-256 verified.
```

---

## What We Have Today

### 28 skills across 5 domains

| Domain | Skills | Examples |
|--------|--------|----------|
| **Personal genomics** | 6 | PharmGx Reporter, NutriGx Advisor, Drug Photo, Genome Compare, ClinPGx, Profile Report |
| **Population genetics** | 5 | Equity Scorer (HEIM), Ancestry PCA, GWAS PRS, GWAS Lookup, Semantic Similarity |
| **Single-cell & omics** | 3 | scRNA Orchestrator, RNA-seq DE, Metagenomics Profiler |
| **Research infrastructure** | 4 | UKB Navigator, Galaxy Bridge, Bio Orchestrator, Data Extractor |
| **Quality & security** | 2 | PR Audit, Repro Enforcer |

Every skill includes:

- **SKILL.md**: domain decisions, safety rules, agent boundary
- **Demo data**: synthetic test data so you can try it immediately
- **CLI**: `--input`, `--output`, `--demo` flags
- **Reproducibility bundle**: `commands.sh`, `environment.yml`, `checksums.sha256`

---

## Traction (3 weeks since launch)

| Metric | Value |
|--------|-------|
| GitHub stars | **444** |
| Forks | **70** |
| Contributors | **5** (across 3 countries) |
| Skills | **28** |
| Releases | **3** |
| Page views (14 days) | **10,972** from **3,587 unique visitors** |
| Repo clones (14 days) | **3,107** from **645 unique cloners** |

First community PR merged within 48 hours of launch. Presented at the London Bioinformatics Meetup (26 Feb) and Imperial College DoraHacks Demo Day (7 Mar).

---

## Architecture

**Three layers:**

**1. Bio Orchestrator** (routing)

Routes queries to the right skill based on file type, keywords, and analysis intent.

**2. Specialist Skills** (28 production-ready)

Each skill encodes domain expert decisions: allele classifications, clinical guideline versions, statistical thresholds, safety rules. The AI agent dispatches; the skill executes with proven logic.

**3. Reproducibility Bundle** (every output)

| File | Purpose |
|------|---------|
| `report.md` | Full analysis with figures and tables |
| `figures/` | Publication-quality PNGs |
| `commands.sh` | Exact commands to reproduce |
| `environment.yml` | Conda environment snapshot |
| `checksums.sha256` | SHA-256 of every input and output file |

---

## Why This Matters

**~7% of people are CYP2D6 Poor Metabolisers.** Codeine gives them zero pain relief but they keep getting prescribed it.

**~0.5% carry DPYD variants** where a standard fluorouracil chemotherapy dose can be lethal.

These are not hypothetical risks. ClawBio catches both in under one second from a consumer genetic test.

Health equity research is systematically biased toward well-studied European populations. ClawBio's Equity Scorer quantifies that gap across 175 diseases, making the invisible visible.

---

## Live Demo

### PharmGx Reporter (< 1 second)

```bash
python skills/pharmgx-reporter/pharmgx_reporter.py \
  --input skills/pharmgx-reporter/demo_patient.txt \
  --output /tmp/pharmgx_demo
```

Output: personalised drug report. 10 drugs AVOID, 20 drugs CAUTION, 21 drugs OK for this genotype.

### Genome Compare (< 2 seconds)

```bash
python skills/genome-compare/genome_compare.py \
  --demo --output /tmp/genome_demo
```

Output: pairwise IBS comparison (Manuel Corpas vs George Church), ancestry estimation, population context.

### GWAS Lookup (federated, ~5 seconds)

```bash
python skills/gwas-lookup/gwas_lookup.py \
  --demo --output /tmp/gwas_demo
```

Output: variant associations across 9 genomic databases (gnomAD, ClinVar, GTEx, UK Biobank PheWAS, Open Targets, GWAS Catalog, Biobank Japan, FinnGen, LDlink).

---

## Design Principles

- **Local-first**: genetic data never leaves your machine
- **Open source**: MIT licensed, full source code, no hidden dependencies
- **Agent-native**: `SKILL.md` + `catalog.json` make skills discoverable by any AI agent
- **Composable**: skills chain together (Drug Photo calls PharmGx; Profile Report aggregates all results)
- **Reproducible by default**: every output includes the exact commands and checksums to reproduce it

---

## Your Turn: Build a Skill

Follow the [Setup Guide](setup.md) to get started, then work through [Your First Skill](first-skill.md).

**Judging criteria:**

1. **Domain correctness** (40%): real domain decisions, evidence-based thresholds
2. **Reproducibility** (25%): demo data, consistent results, environment specified
3. **Usefulness** (20%): would a researcher actually use this?
4. **Code quality** (15%): clean, readable, well-structured

**Skill ideas** and full instructions are in the [Hackathon Guide](index.md).

---

## Links

- **Repository**: [github.com/ClawBio/ClawBio](https://github.com/ClawBio/ClawBio)
- **Website**: [clawbio.ai](https://clawbio.ai)
- **Documentation**: [docs.clawbio.ai](https://docs.clawbio.ai)
- **Discord**: [discord.gg/EEp4Neaz](https://discord.gg/EEp4Neaz)
- **Telegram**: [ClawBio Contributors](https://t.me/ClawBioContributors)

---

*ClawBio is a research and educational tool. It is not a medical device and does not provide clinical diagnoses. Consult a healthcare professional before making any medical decisions.*
