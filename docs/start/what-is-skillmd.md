---
title: What is SKILL.md?
description: The declarative contract that encodes domain expertise for AI agents
---

# What is SKILL.md?

SKILL.md is a declarative contract that encodes a domain expert's analytical decisions — allele classifications, clinical guideline versions, safety rules, statistical thresholds — in a format any agent framework can read, validate, and execute.

## What SKILL.md Encodes That No Workflow Language Can

CWL, Nextflow, Snakemake, WDL, and Galaxy tool wrappers specify **how to run a tool**: inputs, outputs, parameters, dependencies. SKILL.md specifies **what the correct analytical decisions are and why**, in a format an AI agent enforces at execution time:

| Feature | Workflow Languages | SKILL.md |
|---------|-------------------|----------|
| Input/output specification | Yes | Yes |
| Dependency management | Yes | Yes |
| Domain decision blocks | No | Yes |
| Safety rules | No | Yes |
| Guideline versioning | No | Yes |
| Parameter provenance (DOI) | No | Yes |
| LLM boundary declaration | No | Yes |

### Domain Decision Blocks

```yaml
# CYP2D6*4 is no-function (not reduced)
# Source: CPIC v2024-01
# Consequence: avoid codeine if homozygous
```

### Safety Rules

```yaml
# IF DPYD*2A detected AND fluorouracil in drug list:
#   output MUST include lethal-dose warning
#   skill MUST NOT suppress this under any condition
```

### Guideline Versioning

```yaml
guideline_authority: CPIC
guideline_version: 2024-01
guideline_doi: 10.1002/cpt.2091
```

### LLM Boundary Declaration

```yaml
# Agent Boundary
# - LLM: parse request, select skill, confirm format, present output
# - Skill: extract SNPs, call alleles, map phenotypes, look up drugs
# - All domain logic in Python. LLM is a dispatcher, not a reasoner.
```

## Concrete Example: PharmGx Reporter

```yaml
---
name: pharmgx-reporter
version: 2.1.0
author: Manuel Corpas (ORCID: 0000-0002-5765-9827)
domain: [pharmacogenomics, clinical-genetics]
inputs:
  - name: genotype_file
    type: [23andme_v5, ancestrydna_v2, vcf]
outputs:
  - name: report/
    type: reproducibility_bundle
    contains: [report.md, figures/, tables/, commands.sh,
               environment.yml, checksums.sha256]
guideline_authority: CPIC
guideline_version: 2024-01
guideline_doi: 10.1002/cpt.2091
endpoints:
  cli: python pharmgx_reporter.py --input {genotype_file}
  mcp_tool: clawbio/pharmgx-reporter
  http: POST https://clawbio.ai/api/v1/run/pharmgx-reporter
---
```

## Why SKILL.md Over Bespoke Tool Wrappers

SKILL.md provides a single schema that gives the agent everything it needs — tool invocation AND domain correctness constraints — in one file. Bespoke wrappers require the agent to improvise domain decisions from its training data. SKILL.md eliminates that improvisation.
