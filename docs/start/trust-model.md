---
title: Trust Model
description: Three-tier validation system for ClawBio skills
---

# Trust Model

An agent framework author needs guarantees before routing clinical or research queries to an external skill. ClawBio provides three tiers of trust, each with explicit guarantees.

## Validation Tiers

| Guarantee | Community | Verified | Clinical-grade |
|-----------|-----------|----------|----------------|
| SKILL.md schema-valid | ✅ | ✅ | ✅ |
| Demo runs to completion | ✅ | ✅ | ✅ |
| Output checksums match | ✅ | ✅ | ✅ |
| Reproducibility bundle present | ✅ | ✅ | ✅ |
| Security scan clean | ✅ | ✅ | ✅ |
| Domain-expert review | | ✅ | ✅ |
| Guideline version declared and monitored | | ✅ | ✅ |
| DOI minted | | ✅ | ✅ |
| Cryptographically signed package | | | ✅ |
| Safety rules audited | | | ✅ |
| BioCompute Object (IEEE 2791) compliant | | | ✅ |
| Sandbox-ready (Docker/Singularity) | | | ✅ |

## Community Tier

The baseline for all submitted skills. Automated checks only:

- SKILL.md passes schema validation
- Demo data runs and produces expected output
- Output checksums are generated and match
- Reproducibility bundle (commands.sh, environment.yml, checksums.sha256) is present
- Security scan passes: no network calls, no filesystem access outside declared paths

## Verified Tier

Adds human review by domain experts:

- Advisory board member reviews domain decisions, parameter sources, and safety rules
- Guideline versions are declared and automatically monitored for updates
- DOI minted via Zenodo integration
- Skills flagged when source guidelines publish updates; badges suspended until skill is updated

## Clinical-grade Tier

For skills destined for clinical research or pre-clinical pathways:

- All Verified guarantees plus:
- Cryptographically signed packages
- Safety rules independently audited
- BioCompute Object (IEEE 2791) compliance
- Containerised execution (Docker/Singularity)

## Security Threat Model

| Threat | Mitigation |
|--------|-----------|
| Malicious skill submission | Automated scan on submission (no network calls, no fs access outside declared paths) |
| Prompt injection via crafted inputs | Input validation, sandboxed execution |
| Data exfiltration via network calls | Network access blocked during execution |
| Supply chain attack | Signed packages at Clinical tier; community flagging; no-execute-on-install policy |

## Governance

- **Advisory board**: 4+ domain experts (clinical pharmacogenomics, population genetics, single-cell biology, statistical genetics)
- **Schema evolution**: SKILL.md schema evolves via RFCs with 30-day public comment periods. Changes require 2+ advisory board approvals
- **Guideline monitoring**: Automated alerts when declared guideline sources publish updates
- **Deprecation policy**: Deprecated skills remain accessible for reproducibility, marked with pointer to successor
