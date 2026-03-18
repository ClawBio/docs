---
title: SKILL.md Specification
description: Formal specification of the SKILL.md declarative contract
---

# SKILL.md Specification

SKILL.md is a declarative contract that encodes a domain expert's analytical decisions in a format any agent framework can read, validate, and execute. This page documents the formal specification.

## Structure

Every SKILL.md file consists of two parts:

1. **YAML frontmatter** -- machine-readable metadata between `---` delimiters
2. **Markdown body** -- human-readable methodology, domain decisions, and safety rules

## YAML Frontmatter Fields

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Unique skill identifier (lowercase, hyphens) |
| `version` | string | Semantic version (e.g., `1.0.0`) |
| `author` | string | Skill author name |
| `domain` | string | Primary domain (e.g., `pharmacogenomics`, `population-genetics`) |
| `inputs` | list | Input file types and descriptions |
| `outputs` | list | Output file types and descriptions |

### Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `guideline_authority` | string | Governing body (e.g., `CPIC`, `ACMG`, `EDAM`) |
| `guideline_version` | string | Version of the referenced guideline |
| `guideline_doi` | string | DOI of the referenced guideline |
| `endpoints` | list | Supported invocation methods (`cli`, `mcp`, `http`) |
| `dependencies` | list | Python packages or system requirements |
| `demo_data` | string | Path to demo input files |
| `tags` | list | Searchable keywords |
| `license` | string | SPDX license identifier (default: `MIT`) |
| `validation_tier` | string | One of `community`, `verified`, `clinical` |

### Example Frontmatter

```yaml
---
name: pharmgx-reporter
version: 2.1.0
author: Manuel Corpas
domain: pharmacogenomics
guideline_authority: CPIC
guideline_version: "2024-01"
guideline_doi: "10.1002/cpt.2350"
inputs:
  - type: txt
    description: "23andMe or AncestryDNA raw genotype file"
  - type: vcf
    description: "VCF file with pharmacogenomic variants"
outputs:
  - type: json
    description: "Structured pharmacogenomics report"
  - type: html
    description: "Human-readable report with drug-gene interaction table"
endpoints:
  - cli
  - mcp
  - http
tags:
  - pharmacogenomics
  - drug-gene
  - CPIC
  - 23andMe
validation_tier: verified
license: MIT
---
```

## Markdown Body Sections

### Domain Decisions

The core of a SKILL.md. Documents every analytical decision the skill encodes:

- Classification thresholds (e.g., "Poor Metaboliser if activity score < 1.0")
- Allele-to-phenotype mappings
- Statistical parameters (e.g., p-value thresholds, effect size cutoffs)
- Reference datasets and their versions

```markdown
## Domain Decisions

### Metaboliser Classification
- Poor Metaboliser: activity score < 1.0
- Intermediate Metaboliser: activity score 1.0 -- 1.5
- Normal Metaboliser: activity score 1.5 -- 2.0
- Ultrarapid Metaboliser: activity score > 2.0

Source: CPIC 2024-01, Table 2
```

### Safety Rules

What the skill must never do and when it must defer to a human expert:

```markdown
## Safety Rules

1. Never recommend dosing changes -- only report phenotype and flag interactions
2. Always include disclaimer: "Consult a healthcare professional"
3. Flag unknown or novel alleles as "unclassified" rather than guessing
4. Refuse to process files with fewer than 10 variants (insufficient data)
```

### Agent Boundary

Defines the scope of the skill -- what questions it can and cannot answer:

```markdown
## Agent Boundary

### In Scope
- Drug-gene interaction lookup for CPIC Level A/B genes
- Metaboliser phenotype classification
- Interaction severity flagging

### Out of Scope
- Dosing recommendations (requires clinical context)
- Drug-drug interactions (not a pharmacogenomic question)
- Diagnosis of genetic conditions
```

## JSON Schema

The formal JSON schema for SKILL.md frontmatter validation is available at:

```
https://clawbio.ai/schemas/skillmd-v2.0.json
```

Use `clawbio validate` to check a SKILL.md against this schema locally.

## Versioning

SKILL.md follows semantic versioning:

- **Major**: breaking changes to inputs, outputs, or domain decisions
- **Minor**: new optional fields, expanded coverage, non-breaking enhancements
- **Patch**: bug fixes, typo corrections, documentation updates
