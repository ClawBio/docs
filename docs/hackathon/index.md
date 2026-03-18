# Hackathon Guide

Welcome to the ClawBio Hackathon! This guide will get you from zero to a working bioinformatics skill in under an hour.

## What You'll Build

A **ClawBio skill**: a self-contained bioinformatics module that any AI agent can discover, understand, and run. Each skill is defined by a `SKILL.md` file that encodes domain expertise in a machine-readable format.

## Before You Start

You'll need:

- [Claude Code](https://claude.ai/claude-code) or any MCP-compatible agent
- Python 3.11+
- Git
- A GitHub account

## Quick Path

| Step | Time | What |
|------|------|------|
| 1. [Setup](setup.md) | 10 min | Clone repo, install dependencies, run a demo |
| 2. [Your First Skill](first-skill.md) | 20 min | Scaffold a skill, write SKILL.md, add demo data |
| 3. [Add Python](add-python.md) | 20 min | Implement the skill logic with a CLI endpoint |
| 4. [Test and Submit](submit.md) | 10 min | Validate, test, open a PR |

## Skill Ideas

Not sure what to build? Here are some ideas across different domains:

### Genomics & Variants
- **HLA Typer**: predict HLA alleles from genotype data
- **CNV Caller**: detect copy number variants from exome depth
- **Ancestry Deconvolution**: local ancestry inference from phased genotypes

### Clinical & Pharmacogenomics
- **Drug Interaction Checker**: flag contraindicated drug pairs from a patient genotype
- **Rare Disease Matcher**: match HPO phenotype terms to candidate genes
- **Dosing Calculator**: weight/genotype-adjusted dosing recommendations

### Multi-omics & Functional
- **Pathway Enricher**: gene set enrichment against KEGG/Reactome
- **Methylation Scorer**: differential methylation from array data
- **Protein Interaction Mapper**: PPI network from a gene list (STRING API)

### Population & Public Health
- **Outbreak Tracker**: phylogenetic clustering from consensus sequences
- **Vaccine Coverage Scorer**: equity analysis of vaccination data
- **Antimicrobial Resistance Profiler**: AMR gene detection from metagenomic reads

## Judging Criteria

Skills will be evaluated on:

1. **Domain correctness** (40%): Does the SKILL.md encode real domain decisions? Are thresholds evidence-based?
2. **Reproducibility** (25%): Does demo data produce consistent results? Is the environment specified?
3. **Usefulness** (20%): Would a researcher actually use this?
4. **Code quality** (15%): Clean, readable, well-structured

## Getting Help

- Ask questions in [GitHub Discussions](https://github.com/ClawBio/ClawBio/discussions)
- Join [Discord](https://discord.gg/clawbio)
- Tag `@ClawBio` on issues
