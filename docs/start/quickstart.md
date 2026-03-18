---
title: Quickstart
description: Get ClawBio running in under 5 minutes
---

# Quickstart

## Install as a Claude Code Plugin

The fastest way to use ClawBio:

```bash
claude plugin install ClawBio/ClawBio
```

Then in any Claude Code session:

```bash
# List all available skills
/clawbio:list-skills

# Run a demo analysis
/clawbio:run-demo

# Analyse your own data
/clawbio:analyse
```

## Install from Source

```bash
git clone https://github.com/ClawBio/ClawBio.git
cd ClawBio
pip install -r requirements.txt
```

## Run Your First Skill

### Pharmacogenomics Report (demo data)

```bash
python skills/pharmgx-reporter/pharmgx_reporter.py \
  --input skills/pharmgx-reporter/demo_patient.txt \
  --output /tmp/pharmgx_demo
```

### Nutrigenomics Report (demo data)

```bash
python skills/nutrigx_advisor/nutrigx_advisor.py \
  --input skills/nutrigx_advisor/synthetic_patient.txt \
  --output /tmp/nutrigx_demo
```

### GWAS Polygenic Risk Score (demo data)

```bash
python skills/gwas-prs/gwas_prs.py --demo --output /tmp/prs_demo
```

### Single-Cell RNA-seq (demo data)

```bash
python skills/scrna-orchestrator/scrna_orchestrator.py --demo --output /tmp/scrna_demo
```

## With Your Own Data

Most skills accept 23andMe, AncestryDNA, or VCF files:

```bash
# Pharmacogenomics from your 23andMe data
python skills/pharmgx-reporter/pharmgx_reporter.py \
  --input ~/Downloads/genome_Your_Name.txt \
  --output /tmp/my_pharmgx_report

# Genome comparison against George Church
python skills/genome-compare/genome_compare.py \
  --input ~/Downloads/genome_Your_Name.txt \
  --output /tmp/my_genome_compare
```

!!! warning
    All computation runs **locally**. Your genetic data never leaves your machine. No network calls are made during analysis.

## Next Steps

- Browse the [Skill Library](/skills/index) to see all available skills
- Read the [SKILL.md Specification](/reference/skillmd-spec) to understand how skills work
- Learn about the [Trust Model](/start/trust-model) for skill validation
