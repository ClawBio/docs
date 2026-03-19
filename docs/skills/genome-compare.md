---
title: Genome Compare
description: Pairwise genome comparison with identity-by-state scoring
---

# Genome Compare

Compare two personal genomes and compute identity-by-state (IBS) similarity. The demo compares Manuel Corpas against George Church using their public 23andMe data and provides ancestry estimation.

## Quick Demo

```bash
python3 skills/genome-compare/genome_compare.py \
  --demo \
  --output /tmp/demo
```

## CLI Reference

```bash
# Compare your genome against the reference (George Church)
python3 skills/genome-compare/genome_compare.py \
  --input <23andme_file> \
  --output <report_dir>

# Demo mode (Corpas vs Church)
python3 skills/genome-compare/genome_compare.py \
  --demo \
  --output <report_dir>
```

| Argument | Required | Description |
|----------|----------|-------------|
| `--input` | Yes* | Path to 23andMe raw data file |
| `--output` | Yes | Output directory for report and figures |
| `--demo` | No | Run built-in Corpas vs Church comparison |

*Not required when using `--demo`.

## Output

- `report.md` -- Pairwise comparison report with IBS score and ancestry estimates
- `figures/` -- IBS distribution plots, chromosome-level similarity
- `tables/` -- Per-chromosome IBS breakdown (CSV)
- `commands.sh` -- Reproducibility script
- `checksums.sha256` -- Output verification
