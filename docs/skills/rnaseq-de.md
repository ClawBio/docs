---
title: RNA-seq DE
description: RNA-seq differential expression analysis
---

# RNA-seq DE

Run differential expression analysis on bulk or pseudo-bulk RNA-seq count matrices using PyDESeq2. Specify a design formula and contrast to identify differentially expressed genes, generate volcano plots, and export ranked gene lists.

## Quick Demo

```bash
python3 skills/rnaseq-de/rnaseq_de.py \
  --demo \
  --output /tmp/rnaseq_de_demo
```

## CLI Reference

```bash
# Standard DE analysis
python3 skills/rnaseq-de/rnaseq_de.py \
  --counts <counts.csv> \
  --metadata <metadata.csv> \
  --formula "~ batch + condition" \
  --contrast "condition,treated,control" \
  --output <report_dir>

# Demo mode
python3 skills/rnaseq-de/rnaseq_de.py \
  --demo \
  --output /tmp/rnaseq_de_demo
```

| Argument | Required | Description |
|----------|----------|-------------|
| `--counts` | Yes* | Path to gene count matrix (CSV or TSV, genes as rows) |
| `--metadata` | Yes* | Path to sample metadata (CSV or TSV) |
| `--formula` | Yes* | DESeq2-style design formula (e.g. `~ batch + condition`) |
| `--contrast` | Yes* | Contrast specification: `factor,level,reference` |
| `--output` | Yes | Output directory for report and figures |
| `--demo` | No | Run with built-in synthetic dataset |

*Not required when using `--demo`.

## Output

- `report.md` -- DE analysis report with summary statistics
- `figures/` -- Volcano plot, MA plot, PCA of samples
- `tables/` -- Full DE results table, significant genes list (CSV)
- `commands.sh` -- Reproducibility script
- `checksums.sha256` -- Output verification
