---
title: Vaccine Equity Scorer
description: Calculate equity scores for vaccination coverage data across demographic groups using the HEIM framework.
---

# Vaccine Equity Scorer

**Track**: E - Epidemiology
**Difficulty**: Beginner
**Time estimate**: 2-4 hours

## What You'll Build

A ClawBio skill that takes vaccination coverage data broken down by demographic group and calculates equity scores using principles from the HEIM (Health Equity Impact Metrics) framework. The output includes disparity scores, gap analysis, and visualisations showing where coverage falls short of equitable targets.

## Why This Matters

Vaccination programmes save millions of lives, but coverage is rarely distributed equitably. Identifying and quantifying disparities is the first step to addressing them. This skill turns routine coverage data into actionable equity intelligence.

## Inputs and Outputs

**Input**: A CSV file with columns: region, demographic_group, population_size, vaccinated_count, coverage_percentage
**Output**: Equity report with: overall coverage, disparity index (range/mean ratio), group-level gap analysis, and a grouped bar chart PNG comparing coverage across regions and demographics

## Key APIs / Data Sources

- No external API required; all computation is local
- WHO immunisation data format as reference: [WHO Immunization Dashboard](https://immunizationdata.who.int/)

## Getting Started

1. Create your skill folder: `skills/vaccine-equity/`
2. Load the CSV and compute coverage percentages if not already present
3. Calculate the disparity index: (max coverage - min coverage) / mean coverage, per region
4. Compute the equity gap: difference between each group's coverage and the highest-coverage group
5. Generate a grouped bar chart with regions on the x-axis and demographic groups as colour-coded bars

## Domain Decisions for SKILL.md

- Equity target: 90% coverage for all groups (WHO target for routine immunisation)
- Disparity index: use the range/mean ratio (simple, interpretable, widely used)
- Flag any group with coverage below 80% as "critical gap"
- Weight disparities by population size (a 10% gap in a large group matters more than in a small one)
- Report both absolute gaps (percentage points) and relative gaps (ratio to highest group)

## Demo Data

Create a synthetic CSV with 5 regions (North, South, East, West, Central) and 4 demographic groups (Urban, Rural, Indigenous, Migrant). Set overall coverage at 85% but introduce realistic disparities: Urban 92%, Rural 81%, Indigenous 68%, Migrant 74%. Vary by region to show geographic patterns.

## Stretch Goals

- Add trend analysis if multi-year data is provided
- Calculate the Slope Index of Inequality (SII) for a more sophisticated equity measure
- Generate a choropleth map if geographic coordinates are available
- Compare against WHO targets and flag regions failing the 80-80-80 benchmark
