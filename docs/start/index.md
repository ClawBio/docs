---
title: Welcome to ClawBio
description: The reference repository for biological AI agent skills
---

# Getting Started

**ClawBio** is the first bioinformatics-native agent skill library: a curated, reproducible, open repository any agent can call.

- **[Quickstart](quickstart.md)** -- Get running in under 5 minutes
- **[Installation](install.md)** -- Full installation guide
- **[Skill Library](../skills/index.md)** -- Browse 24+ bioinformatics skills
- **[SKILL.md Spec](../reference/skillmd-spec.md)** -- Understand the specification

## What Makes ClawBio Different

ClawBio skills are not just workflow wrappers. Each skill encodes **domain expert decisions** in a `SKILL.md` file: allele classifications, clinical guideline versions, safety rules, and statistical thresholds. This means:

- The AI agent dispatches and explains; the skill executes with proven logic
- Domain decisions are transparent and auditable, not hidden in code
- Every skill ships with demo data so you can verify it immediately
- Reproducibility bundles (`commands.sh`, `environment.yml`, SHA-256 checksums) let you reproduce without the agent

| Feature | GitHub Repo | Workflow (CWL/Nextflow) | ClawBio Skill |
|---------|-------------|------------------------|---------------|
| Reproducibility | Manual | Partial | SHA-256 bundles |
| Agent-callable | No | No | Yes (CLI) |
| Domain decisions encoded | No | No | Yes (SKILL.md) |
| Demo data included | Rarely | No | Always |

## Quick Links

- **Repository**: [github.com/ClawBio/ClawBio](https://github.com/ClawBio/ClawBio)
- **Website**: [clawbio.ai](https://clawbio.ai)
- **Discord**: [Join the community](https://discord.gg/clawbio)
