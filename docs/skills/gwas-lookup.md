---
title: GWAS Lookup
description: Federated variant query across genomic databases
---

# GWAS Lookup

Query a variant by rsID across nine genomic databases in a single call: GWAS Catalog, ClinVar, gnomAD, GTEx, Open Targets, PheWAS, Biobank Japan, FinnGen, and UK Biobank. Returns unified trait associations, allele frequencies, eQTL data, and clinical significance.

## Quick Demo

```bash
python skills/gwas-lookup/gwas_lookup.py \
  --demo \
  --output /tmp/gwas_lookup_demo
```

## CLI Reference

```bash
# Look up a single variant
python skills/gwas-lookup/gwas_lookup.py \
  --rsid rs3798220 \
  --output <report_dir>

# Skip specific databases
python skills/gwas-lookup/gwas_lookup.py \
  --rsid rs3798220 \
  --skip gtex,bbj \
  --output <report_dir>

# Demo mode (pre-fetched rs3798220)
python skills/gwas-lookup/gwas_lookup.py \
  --demo \
  --output /tmp/gwas_lookup_demo
```

| Argument | Required | Description |
|----------|----------|-------------|
| `--rsid` | Yes* | Variant rsID to query |
| `--output` | Yes | Output directory for report and tables |
| `--skip` | No | Comma-separated list of databases to skip |
| `--demo` | No | Run with pre-fetched demo data for rs3798220 |

*Not required when using `--demo`.

## Output

- `report.md` -- Unified variant report with cross-database findings
- `tables/` -- Per-database association tables (CSV)
- `commands.sh` -- Reproducibility script
- `checksums.sha256` -- Output verification
