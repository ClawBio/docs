---
title: Mass Spec QC Skill
description: Generate a quality control report from MaxQuant or DIA-NN proteomics output with key metrics and distributions.
---

# Mass Spec QC Skill

**Track**: C - Proteomics
**Difficulty**: Intermediate
**Time estimate**: 2-4 hours

## What You'll Build

A ClawBio skill that reads proteomics search engine output (MaxQuant proteinGroups.txt or DIA-NN report.tsv) and produces a standardised QC report. The report covers protein identification count, missing value percentage, coefficient of variation distribution, and contaminant fraction.

## Why This Matters

Mass spectrometry experiments are expensive and technically demanding. QC failures caught late waste weeks of analysis time. A standardised QC skill catches problems at the data-loading stage, before any downstream biological interpretation.

## Inputs and Outputs

**Input**: MaxQuant proteinGroups.txt or DIA-NN main report TSV
**Output**: Markdown QC report with: total proteins identified, missing value % per sample, CV distribution plot (PNG), contaminant summary, and overall pass/fail verdict

## Key APIs / Data Sources

- No external API needed; this skill parses local output files
- [MaxQuant documentation](https://www.maxquant.org/) for column definitions
- [DIA-NN documentation](https://github.com/vdemichev/DiaNN) for report format

## Getting Started

1. Create your skill folder: `skills/mass-spec-qc/`
2. Auto-detect the input format (MaxQuant vs DIA-NN) from column headers
3. For MaxQuant: filter reverse hits (`Reverse == "+"`) and contaminants (`Potential contaminant == "+"`)
4. Calculate per-sample metrics: protein count, missing values, intensity distribution
5. Compute CVs across replicates and plot the distribution with matplotlib

## Domain Decisions for SKILL.md

- Remove reverse hits and contaminants before counting protein identifications
- Missing value threshold: warn above 20%, fail above 40% per sample
- CV threshold: median CV below 20% is acceptable for label-free quantification
- Contaminant fraction: warn above 2%, fail above 5%
- Report contaminant identities (keratins, BSA, trypsin) individually

## Demo Data

Create a synthetic proteinGroups.txt with 500 protein entries. Include columns: Protein IDs, Gene names, Intensity Sample1 through Sample6, Reverse, Potential contaminant. Set 10% of intensity values to 0 (missing), add 15 contaminant entries (CON__ prefix), and 10 reverse hits (REV__ prefix).

## Stretch Goals

- Add sample correlation heatmap (Pearson r across all pairs)
- Support TMT/iTRAQ reporter ion data
- Detect batch effects by PCA of intensity profiles
- Compare QC metrics against a reference dataset of published standards
