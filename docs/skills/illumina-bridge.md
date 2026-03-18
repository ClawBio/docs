---
title: Illumina Bridge
description: Illumina ICA integration for DRAGEN bundle import
---

# Illumina Bridge

Import Illumina/DRAGEN result bundles into ClawBio for local tertiary analysis. Discovers VCF, SampleSheet, and QC files inside an export directory, normalises metadata, and optionally enriches with Illumina Connected Analytics (ICA) project metadata.

## Quick Demo

```bash
python skills/illumina-bridge/illumina_bridge.py \
  --demo \
  --output /tmp/illumina_demo
```

## CLI Reference

```bash
# Import a DRAGEN bundle
python skills/illumina-bridge/illumina_bridge.py \
  --input <bundle_dir> \
  --output <report_dir>

# With ICA metadata enrichment
python skills/illumina-bridge/illumina_bridge.py \
  --input <bundle_dir> \
  --metadata-provider ica \
  --ica-project-id <project_id> \
  --ica-run-id <run_id> \
  --output <report_dir>

# Demo mode
python skills/illumina-bridge/illumina_bridge.py \
  --demo \
  --output /tmp/illumina_demo
```

| Argument | Required | Description |
|----------|----------|-------------|
| `--input` | Yes* | Path to DRAGEN export directory |
| `--output` | Yes | Output directory for report and manifest |
| `--metadata-provider` | No | Set to `ica` to enable ICA enrichment |
| `--ica-project-id` | No | ICA project ID for metadata lookup |
| `--ica-run-id` | No | ICA run ID for metadata lookup |
| `--demo` | No | Run with synthetic DRAGEN bundle |

*Not required when using `--demo`.

Requires `ILLUMINA_ICA_API_KEY` and `ILLUMINA_ICA_BASE_URL` environment variables when using ICA enrichment.

## Output

- `report.md` -- Import summary with QC highlights and downstream routing hints
- `result.json` -- Machine-readable import envelope
- `tables/sample_manifest.csv` -- Normalised sample manifest
- `reproducibility/` -- `commands.sh`, `environment.yml`, `checksums.sha256`
