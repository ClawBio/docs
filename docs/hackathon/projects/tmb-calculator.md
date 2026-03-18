---
title: Tumour Mutational Burden
description: Calculate TMB and estimate MSI status from a somatic VCF to assess immunotherapy relevance.
---

# Tumour Mutational Burden

**Track**: D - Clinical
**Difficulty**: Intermediate
**Time estimate**: 2-4 hours

## What You'll Build

A ClawBio skill that takes a somatic VCF file and calculates the tumour mutational burden (mutations per megabase), estimates microsatellite instability (MSI) status, and reports on immunotherapy relevance. The output is a structured clinical summary with key metrics.

## Why This Matters

TMB and MSI are approved biomarkers for immunotherapy response. The FDA has approved pembrolizumab for TMB-high tumours (>= 10 mut/Mb). Automating this calculation from a standard VCF brings precision oncology within reach of any sequencing lab.

## Inputs and Outputs

**Input**: A somatic VCF file (tumour-normal or tumour-only variant calls)
**Output**: Markdown report with: TMB score (mutations/Mb), MSI estimation, mutation type breakdown (SNV/indel), immunotherapy relevance statement, and a mutation spectrum bar chart (PNG)

## Key APIs / Data Sources

- No external API required; all computation is local
- Reference: coding region size from Ensembl (approximately 35 Mb for whole exome)
- [FDA TMB guidance](https://www.fda.gov/drugs/drug-approvals-and-databases/fda-approves-pembrolizumab-adults-and-children-tmb-h-solid-tumors) for clinical thresholds

## Getting Started

1. Create your skill folder: `skills/tmb-calculator/`
2. Parse the somatic VCF and filter variants by quality thresholds
3. Count qualifying mutations and divide by the target region size (in Mb)
4. Classify mutations by type: C>A, C>G, C>T, T>A, T>C, T>G for the mutation spectrum
5. Estimate MSI by counting indels at homopolymer regions (runs of 5+ identical bases)

## Domain Decisions for SKILL.md

- Variant allele frequency (VAF) threshold: minimum 0.05 (5%) to count as somatic
- Minimum read depth: 30x at the variant position
- Count only coding region variants (filter by BED file or VCF annotation)
- TMB thresholds: low (< 6 mut/Mb), intermediate (6-10), high (>= 10)
- MSI estimation: high indel fraction at homopolymers (> 20%) suggests MSI-H
- Include both SNVs and indels in the TMB count (per TMB Harmonization guidelines)

## Demo Data

Create a synthetic somatic VCF with 200 variants distributed across chromosomes 1-22. Include: 150 SNVs (mix of C>T transitions and other substitutions), 30 coding indels, and 20 filtered-out variants (low VAF or low depth). Set the target region to 1.5 Mb to give a TMB of approximately 100 mut/Mb (TMB-high).

## Stretch Goals

- Add trinucleotide context analysis for mutational signature detection
- Compare observed spectrum against COSMIC SBS signatures
- Support panel-based TMB calculation with user-defined BED file
- Generate a PDF clinical report suitable for tumour board review
