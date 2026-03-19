---
title: NutriGx Advisor
description: Nutrigenomics recommendations from consumer genetic data
---

# NutriGx Advisor

Generate personalised nutrigenomics recommendations from 23andMe or AncestryDNA data. Maps genotypes for MTHFR, lactose tolerance, caffeine metabolism, vitamin D, omega-3, and other diet-relevant variants to actionable dietary guidance.

## Quick Demo

```bash
python3 skills/nutrigx_advisor/nutrigx_advisor.py \
  --input skills/nutrigx_advisor/synthetic_patient.txt \
  --output /tmp/nutrigx_demo
```

## CLI Reference

```bash
python3 skills/nutrigx_advisor/nutrigx_advisor.py \
  --input <patient_file> \
  --output <report_dir>
```

| Argument | Required | Description |
|----------|----------|-------------|
| `--input` | Yes | Path to 23andMe or AncestryDNA raw data file |
| `--output` | Yes | Output directory for report and figures |

## Output

- `report.md` -- Personalised nutrigenomics report with dietary recommendations
- `figures/` -- Nutrient metabolism charts
- `tables/` -- Genotype-to-nutrient mappings (CSV)
- `commands.sh` -- Reproducibility script
- `environment.yml` -- Pinned dependencies
- `checksums.sha256` -- Output verification
