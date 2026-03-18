---
title: PharmGx Reporter
description: Pharmacogenomics report from consumer genetic data
---

# PharmGx Reporter

Generate a personalised pharmacogenomics report from 23andMe, AncestryDNA, or VCF data. Maps genotypes to drug-gene interactions using CPIC clinical guidelines.

## Quick Demo

```bash
python skills/pharmgx-reporter/pharmgx_reporter.py \
  --input skills/pharmgx-reporter/demo_patient.txt \
  --output /tmp/pharmgx_demo
```

## What It Does

1. Parses consumer genetic data (23andMe v5, AncestryDNA v2, VCF)
2. Extracts pharmacogenomically relevant SNPs (CYP2D6, CYP2C19, CYP2C9, DPYD, SLCO1B1, VKORC1, etc.)
3. Calls star alleles and maps to metaboliser phenotypes
4. Looks up CPIC drug-gene interactions
5. Generates a Markdown report with drug recommendations, risk flags, and reproducibility bundle

## CLI Reference

```bash
python skills/pharmgx-reporter/pharmgx_reporter.py \
  --input <patient_file> \
  --output <report_dir>
```

| Argument | Required | Description |
|----------|----------|-------------|
| `--input` | Yes | Path to 23andMe, AncestryDNA, or VCF file |
| `--output` | Yes | Output directory for report and figures |

## Safety Rules

- If DPYD*2A detected and fluorouracil in drug list: report MUST include lethal-dose warning
- All drug-gene mappings traced to CPIC guideline version (declared in SKILL.md)
- Guideline version monitored; skill flagged when CPIC publishes updates

## Output

- `report.md` — Full pharmacogenomics report
- `figures/` — Metaboliser phenotype charts
- `tables/` — Drug interaction tables (CSV)
- `commands.sh` — Reproducibility script
- `environment.yml` — Pinned dependencies
- `checksums.sha256` — Output verification
