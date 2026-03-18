---
title: CLI Reference
description: Complete command-line reference for all ClawBio skills
---

# CLI Reference

Every ClawBio skill with a Python implementation is invocable via the command line. All skills follow a consistent argument pattern: `--input`, `--output`, and `--demo`.

## ClawBio CLI Tools

```bash
# Scaffold a new skill
clawbio init <skill-name>

# Validate a skill against the SKILL.md schema
clawbio validate skills/<skill-name>/

# Publish a skill to the registry
clawbio publish skills/<skill-name>/
```

## Skill Commands

### PharmGx Reporter

Pharmacogenomics report from 23andMe, AncestryDNA, or VCF data. CPIC guideline-backed drug-gene interactions.

```bash
python skills/pharmgx-reporter/pharmgx_reporter.py \
  --input <patient_file> --output <report_dir>

# Demo
python skills/pharmgx-reporter/pharmgx_reporter.py \
  --input skills/pharmgx-reporter/demo_patient.txt --output /tmp/pharmgx_demo
```

### Equity Scorer (HEIM)

Health Equity Impact Metric for genomic datasets.

```bash
python skills/equity-scorer/equity_scorer.py \
  --input <vcf_or_csv> [--pop-map <csv>] [--output <dir>] \
  [--weights 0.35,0.25,0.20,0.20]

# Demo (VCF)
python skills/equity-scorer/equity_scorer.py \
  --input examples/demo_populations.vcf \
  --pop-map examples/demo_population_map.csv --output /tmp/equity_demo

# Demo (ancestry CSV)
python skills/equity-scorer/equity_scorer.py \
  --input examples/sample_ancestry.csv --output /tmp/equity_csv_demo
```

### NutriGx Advisor

Personalised nutrition report from genetic data. 40+ nutritionally-relevant SNPs.

```bash
python skills/nutrigx_advisor/nutrigx_advisor.py \
  --input <patient_file> --output <report_dir>

# Demo
python skills/nutrigx_advisor/nutrigx_advisor.py \
  --input skills/nutrigx_advisor/synthetic_patient.txt --output /tmp/nutrigx_demo
```

### scRNA Orchestrator

End-to-end single-cell RNA-seq pipeline: QC, normalisation, clustering, marker genes, doublet removal.

```bash
python skills/scrna-orchestrator/scrna_orchestrator.py \
  --input <data.h5ad> --output <report_dir>

# Demo
python skills/scrna-orchestrator/scrna_orchestrator.py \
  --demo --output /tmp/scrna_demo

# Demo with Scrublet doublet detection
python skills/scrna-orchestrator/scrna_orchestrator.py \
  --demo --doublet-method scrublet --output /tmp/scrna_doublet_demo
```

### Genome Compare

Pairwise genome comparison with IBS scoring. Compare against George Church's genome.

```bash
python skills/genome-compare/genome_compare.py \
  --input <23andme_file> --output <report_dir>

# Demo
python skills/genome-compare/genome_compare.py \
  --demo --output /tmp/genome_compare_demo
```

### ClinPGx

Gene-drug pharmacogenomic database query via PharmGKB and CPIC.

```bash
python skills/clinpgx/clinpgx.py \
  --gene <symbol> --output <report_dir>

python skills/clinpgx/clinpgx.py \
  --genes "CYP2D6,CYP2C19" --drugs "warfarin" --output <report_dir>

# Demo
python skills/clinpgx/clinpgx.py --demo --output /tmp/clinpgx_demo
```

### GWAS PRS

Polygenic risk scores from consumer genetic data. 6 curated traits.

```bash
python skills/gwas-prs/gwas_prs.py \
  --input <23andme_file> --trait "type 2 diabetes" --output <report_dir>

python skills/gwas-prs/gwas_prs.py \
  --input <23andme_file> --pgs-id PGS000013 --output <report_dir>

# Demo
python skills/gwas-prs/gwas_prs.py --demo --output /tmp/prs_demo
```

### GWAS Lookup

Federated variant query across 9 genomic databases.

```bash
python skills/gwas-lookup/gwas_lookup.py \
  --rsid <rsid> --output <report_dir>

# Skip specific databases
python skills/gwas-lookup/gwas_lookup.py \
  --rsid <rsid> --skip gtex,bbj --output <report_dir>

# Demo
python skills/gwas-lookup/gwas_lookup.py --demo --output /tmp/gwas_lookup_demo
```

### Profile Report

Unified personal genomic profile report combining multiple skills.

```bash
python skills/profile-report/profile_report.py \
  --profile <profile.json> --output <report_dir>

# Demo
python skills/profile-report/profile_report.py --demo --output /tmp/profile_demo
```

### UKB Navigator

Semantic search across UK Biobank schema.

```bash
python skills/ukb-navigator/ukb_navigator.py \
  --query "blood pressure" --output <report_dir>

python skills/ukb-navigator/ukb_navigator.py \
  --field 21001 --output <report_dir>

# Demo
python skills/ukb-navigator/ukb_navigator.py --demo --output /tmp/ukb_demo
```

### Galaxy Bridge

Search, inspect, and run Galaxy tools from ClawBio.

```bash
python skills/galaxy-bridge/galaxy_bridge.py \
  --search "metagenomics profiling"

python skills/galaxy-bridge/galaxy_bridge.py --list-categories

python skills/galaxy-bridge/galaxy_bridge.py \
  --tool-details <tool_id>

python skills/galaxy-bridge/galaxy_bridge.py \
  --run <tool_id> --input <file> --output <dir>

# Demo
python skills/galaxy-bridge/galaxy_bridge.py --demo
```

### RNA-seq DE

Bulk and pseudo-bulk RNA-seq differential expression with PyDESeq2.

```bash
python skills/rnaseq-de/rnaseq_de.py \
  --counts <counts_csv_or_tsv> --metadata <metadata_csv_or_tsv> \
  --formula "~ batch + condition" \
  --contrast "condition,treated,control" --output <report_dir>

# Demo
python skills/rnaseq-de/rnaseq_de.py --demo --output /tmp/rnaseq_de_demo
```

### Bio Orchestrator

Auto-routes queries to the appropriate skill.

```bash
python skills/bio-orchestrator/orchestrator.py \
  --input <file_or_query> [--skill <name>] [--output <dir>]

# List all available skills
python skills/bio-orchestrator/orchestrator.py --list-skills
```

## Common Flags

| Flag | Description |
|------|-------------|
| `--input` | Path to input file |
| `--output` | Path to output directory |
| `--demo` | Run with built-in demo data |
| `--help` | Show help message |
