---
title: Variant Frequency Dashboard
description: Look up a variant by rsID and display allele frequencies across global populations with a bar chart.
---

# Variant Frequency Dashboard

**Track**: A - AI Engineers
**Difficulty**: Intermediate
**Time estimate**: 2-4 hours

## What You'll Build

A ClawBio skill that takes an rsID, queries the gnomAD GraphQL API, and produces a population allele frequency report with a matplotlib bar chart comparing frequencies across ancestries (African, East Asian, European, Latino, South Asian, etc.).

## Why This Matters

Variant frequency varies dramatically across populations. A variant that is common in one ancestry may be rare or absent in another. Understanding these differences is essential for clinical interpretation, ACMG classification, and equitable genomic medicine.

## Inputs and Outputs

**Input**: An rsID (e.g. "rs1801133")
**Output**: Markdown table of allele frequencies per population, plus a saved bar chart (PNG) showing the frequency distribution

## Key APIs / Data Sources

- [gnomAD GraphQL API](https://gnomad.broadinstitute.org/api) - POST queries to the GraphQL endpoint
- Query the `variant` type with `rsid` field to retrieve `populations` and `ac`, `an`, `af` fields

## Getting Started

1. Create your skill folder: `skills/variant-frequency/`
2. Build a GraphQL query that fetches variant data by rsID from gnomAD v4
3. Extract population-level allele frequencies from the response
4. Create a horizontal bar chart using matplotlib with population labels on the y-axis
5. Save the chart as PNG and include frequency values in a markdown table

## Domain Decisions for SKILL.md

- Use gnomAD v4 (genome dataset) as the default; fall back to exome if genome returns no data
- Display the 8 top-level population groups, not sub-populations
- Flag variants with frequency > 0.01 as "common" and < 0.0001 as "rare"
- Include total allele count and allele number alongside frequency for transparency

## Demo Data

Use rs1801133 (MTHFR C677T), a well-studied variant with significant frequency variation across populations. European AF is roughly 0.33; East Asian AF is roughly 0.30; African AF is roughly 0.10. This makes for a clear and informative demo chart.

## Stretch Goals

- Support searching by HGVS notation as well as rsID
- Add ClinVar clinical significance alongside the frequency data
- Compare gnomAD frequencies with 1000 Genomes for validation
- Generate an interactive HTML chart using Plotly instead of static PNG
