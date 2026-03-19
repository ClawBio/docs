---
title: GWAS PRS
description: Polygenic risk scores from consumer genetic data
---

# GWAS PRS

Calculate polygenic risk scores (PRS) from 23andMe or AncestryDNA data using curated PGS Catalog scores. Supports trait-based lookup or direct PGS ID specification for diseases such as type 2 diabetes, coronary artery disease, and breast cancer.

## Quick Demo

```bash
python3 skills/gwas-prs/gwas_prs.py \
  --demo \
  --output /tmp/prs_demo
```

## CLI Reference

```bash
# Score by trait name
python3 skills/gwas-prs/gwas_prs.py \
  --input <23andme_file> \
  --trait "type 2 diabetes" \
  --output <report_dir>

# Score by PGS Catalog ID
python3 skills/gwas-prs/gwas_prs.py \
  --input <23andme_file> \
  --pgs-id PGS000013 \
  --output <report_dir>

# Demo mode
python3 skills/gwas-prs/gwas_prs.py \
  --demo \
  --output /tmp/prs_demo
```

| Argument | Required | Description |
|----------|----------|-------------|
| `--input` | Yes* | Path to 23andMe or AncestryDNA raw data file |
| `--trait` | No | Trait name for PGS Catalog lookup |
| `--pgs-id` | No | Direct PGS Catalog score ID |
| `--output` | Yes | Output directory for report and figures |
| `--demo` | No | Run with synthetic demo patient (~300 SNPs, 6 traits) |

*Not required when using `--demo`.

## Output

- `report.md` -- PRS report with risk percentiles and population context
- `figures/` -- Risk distribution plots per trait
- `tables/` -- Per-SNP effect allele contributions (CSV)
- `commands.sh` -- Reproducibility script
- `checksums.sha256` -- Output verification
