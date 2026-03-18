---
title: Author a Skill
description: Step-by-step guide to creating a new ClawBio skill from scratch
---

# Author a Skill

This guide walks you through creating a new bioinformatics skill for ClawBio, from initial idea to submitted pull request.

## Overview

A complete skill consists of:

1. A `SKILL.md` describing the methodology, domain decisions, and safety rules
2. Demo data that anyone can run without their own files
3. A Python script with `--input`, `--output`, and `--demo` flags
4. Reproducibility files: `commands.sh`, `environment.yml`, and `checksums.sha256`

You do not need all of these to start. A SKILL.md-only contribution is valuable on its own.

## Step 1 — Scaffold

```bash
cd ClawBio
clawbio init my-skill-name
```

This creates `skills/my-skill-name/` with template files.

## Step 2 — Write SKILL.md

The SKILL.md is the most important file. It encodes the domain decisions a trained scientist would make. Fill in:

- **Frontmatter**: name, version, inputs, outputs, domain tags
- **Domain Decisions**: thresholds, classification rules, guideline references with DOIs
- **Safety Rules**: what the skill must never do, when to defer to a human
- **Agent Boundary**: what the skill does and does not cover

See the [SKILL.md specification](../reference/skillmd-spec.md) for the full schema.

## Step 3 — Add Demo Data

Create synthetic or public-domain test data in `demo/`. Requirements:

- Must not contain real patient data
- Should be small enough to run in under 30 seconds
- Should exercise all major code paths

## Step 4 — Implement

Write your Python script with a standard CLI interface:

```python
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="Input file path")
    parser.add_argument("--output", help="Output directory")
    parser.add_argument("--demo", action="store_true", help="Run with demo data")
    args = parser.parse_args()

    if args.demo:
        args.input = "demo/sample_input.tsv"
        args.output = args.output or "/tmp/demo"

    # Your skill logic here

if __name__ == "__main__":
    main()
```

## Step 5 — Validate and Submit

```bash
# Validate your skill structure
clawbio validate skills/my-skill-name/

# Run demo mode
python skills/my-skill-name/my_skill_name.py --demo --output /tmp/demo

# Create a branch and submit
git checkout -b skill/my-skill-name
git add skills/my-skill-name/
git commit -m "Add my-skill-name skill"
git push origin skill/my-skill-name
```

Then open a pull request at [github.com/ClawBio/ClawBio](https://github.com/ClawBio/ClawBio).

## Tips

- Start with SKILL.md — the domain decisions are harder and more valuable than the code
- Reference authoritative guidelines (CPIC, ACMG, EDAM) with DOIs where possible
- Keep demo data small and deterministic
- Look at [PharmGx Reporter](../skills/pharmgx-reporter.md) as a reference implementation
