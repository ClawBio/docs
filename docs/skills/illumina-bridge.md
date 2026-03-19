---
title: Illumina Bridge
description: Integration with Illumina Connected Analytics (ICA) platform
---

# Illumina Bridge

Connect ClawBio to the Illumina Connected Analytics (ICA) platform. List projects, browse pipeline runs, and pull analysis outputs into your local environment for downstream processing.

## Quick Demo

```bash
python3 skills/illumina-bridge/illumina_bridge.py --demo
```

## CLI Reference

```bash
# List ICA projects
python3 skills/illumina-bridge/illumina_bridge.py \
  --list-projects

# List pipeline runs in a project
python3 skills/illumina-bridge/illumina_bridge.py \
  --project <project_id> --list-runs

# Pull output from a pipeline run
python3 skills/illumina-bridge/illumina_bridge.py \
  --project <project_id> --run <run_id> --output /tmp/demo
```

## Requirements

- An Illumina Connected Analytics account
- An ICA API key (set via `ICA_API_KEY` environment variable)
- `requests` Python package

## Domain Decisions

- Pipeline outputs are downloaded as-is without transformation
- File integrity is verified via checksums provided by ICA
- Large files (>1 GB) are streamed to avoid memory issues
