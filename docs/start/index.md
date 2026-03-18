---
title: Welcome to ClawBio
description: The reference repository for biological AI agent skills
---

# ClawBio Documentation

**ClawBio** is the first bioinformatics-native agent skill library and the reference repository for biological AI agent skills.

- **[Quickstart](/start/quickstart)** — Get running in under 5 minutes
- **[Skill Library](/skills/index)** — Browse 24+ bioinformatics skills
- **[SKILL.md Spec](/reference/skillmd-spec)** — Understand the specification
- **[Roadmap](/roadmap/index)** — Strategic roadmap for 2026

## What Makes ClawBio Different

ClawBio skills are not just workflow wrappers. Each skill encodes **domain expert decisions** — allele classifications, clinical guideline versions, safety rules, statistical thresholds — in a format any agent framework can read, validate, and execute.

| Feature | GitHub Repo | Workflow (CWL/Nextflow) | ClawBio Skill |
|---------|-------------|------------------------|---------------|
| Reproducibility | Manual | Partial | SHA-256 bundles |
| Trust | None | None | 3-tier validation |
| Citability | None | None | DOI-minted |
| Agent-callable | No | No | Yes (CLI, MCP, HTTP) |
| Domain decisions encoded | No | No | Yes (SKILL.md) |

## Thesis

SKILL.md is a declarative contract that encodes a domain expert's analytical decisions in a format any agent framework (OpenClaw, Lobster, custom stacks) can read, validate, and execute in a uniform way. Depositing a skill in ClawBio beats a GitHub repository on three axes:

1. **Reproducibility** — SHA-256-verified bundles
2. **Trust** — governed validation tiers with domain-expert review
3. **Citability** — DOI-minted, citation-tracked artefacts

ClawBio is LLM-agnostic, agent-framework-agnostic, and built to serve as the shared neutral specification layer for the entire bio-agent ecosystem.

## Quick Links

- **Repository**: [github.com/ClawBio/ClawBio](https://github.com/ClawBio/ClawBio)
- **Website**: [clawbio.ai](https://clawbio.ai)
- **Discord**: [Join the community](https://discord.gg/clawbio)
- **Claude Code Plugin**: `claude plugin install ClawBio/ClawBio`
