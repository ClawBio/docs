---
title: Equity Scorer
description: HEIM equity scoring for genomic datasets
---

# Equity Scorer

Compute the HEIM (Health Equity Index Metric) score for a genomic dataset. Measures population representation, allele frequency divergence (FST), heterozygosity balance, and sample-size equity across cohorts.

## Quick Demo

```bash
python skills/equity-scorer/equity_scorer.py \
  --input examples/demo_populations.vcf \
  --pop-map examples/demo_population_map.csv \
  --output /tmp/equity_demo
```

## CLI Reference

```bash
# From a multi-sample VCF with population map
python skills/equity-scorer/equity_scorer.py \
  --input <vcf_or_csv> \
  --pop-map <population_map.csv> \
  --output <report_dir>

# From an ancestry CSV (no VCF needed)
python skills/equity-scorer/equity_scorer.py \
  --input <ancestry.csv> \
  --output <report_dir>

# Custom dimension weights
python skills/equity-scorer/equity_scorer.py \
  --input <vcf_or_csv> \
  --pop-map <csv> \
  --weights 0.35,0.25,0.20,0.20 \
  --output <report_dir>
```

| Argument | Required | Description |
|----------|----------|-------------|
| `--input` | Yes | Path to multi-sample VCF or ancestry CSV |
| `--pop-map` | No | CSV mapping sample IDs to population labels |
| `--output` | Yes | Output directory for report and figures |
| `--weights` | No | Comma-separated weights for the four HEIM dimensions (default: 0.35,0.25,0.20,0.20) |

## Output

- `report.md` -- HEIM equity report with per-dimension scores and overall index
- `figures/` -- Population distribution charts, FST heatmap, heterozygosity plots
- `tables/` -- Per-population metrics (CSV)
- `commands.sh` -- Reproducibility script
- `environment.yml` -- Pinned dependencies
- `checksums.sha256` -- Output verification
