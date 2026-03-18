---
title: Installation
description: All installation methods for ClawBio
---

# Installation

## Claude Code Plugin (Recommended)

```bash
claude plugin install ClawBio/ClawBio
```

This gives you access to all ClawBio skills as slash commands within Claude Code.

## From Source

```bash
git clone https://github.com/ClawBio/ClawBio.git
cd ClawBio
pip install -r requirements.txt
```

### Requirements

- Python 3.11+
- Key libraries: pandas, numpy, matplotlib, seaborn, scanpy (for scRNA skills)

### Optional Dependencies

| Package | Required For |
|---------|-------------|
| `scanpy` | scRNA-seq skills |
| `reportlab` | PDF report generation |
| `requests` | Illumina ICA bridge, Galaxy bridge |
| `pydeseq2` | RNA-seq differential expression |

## Verify Installation

```bash
# List all skills
python skills/bio-orchestrator/orchestrator.py --list-skills

# Run a quick demo
python skills/pharmgx-reporter/pharmgx_reporter.py \
  --input skills/pharmgx-reporter/demo_patient.txt \
  --output /tmp/test_install
```

## Environment Variables

Some skills require API keys for external services (optional):

```bash
# Only needed for Illumina ICA bridge
export ILLUMINA_ICA_API_KEY=your_key_here
export ILLUMINA_ICA_BASE_URL=https://ica.illumina.com

# Only needed for Galaxy bridge (defaults to usegalaxy.org)
export GALAXY_URL=https://usegalaxy.org
export GALAXY_API_KEY=your_key_here
```

!!! note
    Core skills (PharmGx, NutriGx, Genome Compare, GWAS PRS, scRNA) require **no API keys** and run entirely offline.
