---
title: Governance
description: How the SKILL.md standard evolves, who oversees it, and how threats are managed
---

# Governance

ClawBio is an open standard. Its governance model ensures that the specification evolves transparently, that domain expertise guides decisions, and that security threats are addressed proactively.

## Advisory Board

The advisory board comprises **4+ domain experts** spanning:

- **Clinical genomics** -- ensuring skills meet clinical relevance standards
- **Bioinformatics workflows** -- aligning with existing pipeline ecosystems (Galaxy, Nextflow, Snakemake)
- **AI/ML in biology** -- guiding agent interaction patterns and safety
- **Research reproducibility** -- validating that the standard delivers on its reproducibility promise

Board members serve 2-year renewable terms. The board meets quarterly and publishes meeting summaries.

## SKILL.md Schema Evolution

The specification evolves through a formal RFC (Request for Comments) process:

1. **Proposal**: any contributor opens an RFC issue on GitHub with a rationale and proposed changes
2. **Comment period**: 30-day public comment window; all feedback is recorded
3. **Review**: the advisory board reviews comments and votes (simple majority)
4. **Merge or reject**: accepted RFCs are merged into the next spec version; rejected RFCs receive a written rationale
5. **Release**: new spec versions are tagged, documented, and announced

Breaking changes require a major version bump and a 90-day migration window.

## Guideline Monitoring

Skills that reference clinical guidelines (CPIC, ACMG, PharmGKB) must stay current:

- **Automated alerts**: a monitoring service checks guideline authority websites for updates weekly
- **Staleness flag**: skills referencing outdated guidelines are flagged in the registry
- **Grace period**: authors have 60 days to update after a guideline revision before the skill is marked as stale
- **Community reporting**: any user can flag a skill as potentially outdated

## Deprecation Policy

Skills may be deprecated when:

- The underlying guideline is withdrawn
- A superior replacement skill exists
- The author requests removal
- Security vulnerabilities cannot be resolved

Deprecated skills remain accessible for 6 months with a visible deprecation banner. After 6 months, they are archived but not deleted.

## Security Threat Model

| Threat | Mitigation |
|--------|------------|
| Malicious skill submission | Automated validation pipeline + human review for clinical tier |
| Prompt injection via SKILL.md | Sandboxed execution; SKILL.md fields are never passed as raw prompts |
| Data exfiltration | Skills cannot make network calls; no filesystem access outside declared paths |
| Dependency poisoning | Pinned dependencies; checksum verification on install |
| Guideline spoofing | Guideline DOIs verified against authority registries |
| Privilege escalation | Skills run in unprivileged containers; no root access |

The full threat model is maintained in the [Security](/reference/security) reference page and reviewed quarterly by the advisory board.
