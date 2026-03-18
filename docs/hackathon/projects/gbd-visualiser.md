---
title: GBD Disease Burden Visualiser
description: Visualise Global Burden of Disease data showing DALYs, prevalence, and mortality trends for any disease.
---

# GBD Disease Burden Visualiser

**Track**: E - Epidemiology
**Difficulty**: Beginner
**Time estimate**: 2-4 hours

## What You'll Build

A ClawBio skill that takes a disease name, loads GBD (Global Burden of Disease) summary data, and produces publication-quality figures showing DALYs (Disability-Adjusted Life Years), prevalence, and mortality trends with regional comparisons. The output is a set of figures and a summary markdown report.

## Why This Matters

The Global Burden of Disease study is the most comprehensive effort to quantify health loss worldwide, but navigating its data tools is cumbersome. A skill that instantly generates disease burden visualisations saves researchers hours and makes GBD data accessible to non-specialists.

## Inputs and Outputs

**Input**: A disease name (e.g. "malaria", "diabetes mellitus")
**Output**: Markdown summary of disease burden, trend line plot (DALYs over time, PNG), regional comparison bar chart (PNG), prevalence vs mortality scatter plot (PNG)

## Key APIs / Data Sources

- [IHME GBD Results](https://vizhub.healthdata.org/gbd-results/) - downloadable summary CSV files
- Bundle a curated subset of GBD 2021 summary data covering the top 50 diseases (free to redistribute with attribution)
- Alternative: [Global Health Data Exchange API](http://ghdx.healthdata.org/)

## Getting Started

1. Create your skill folder: `skills/gbd-visualiser/`
2. Download GBD 2021 summary data for your target diseases from the IHME results tool (CSV format)
3. Bundle the CSV in your skill's `data/` directory (or fetch on demand)
4. Match the user's input disease name against the GBD cause hierarchy (fuzzy matching recommended)
5. Generate three figures: DALYs trend (line), regional comparison (horizontal bar), prevalence vs mortality (scatter)

## Domain Decisions for SKILL.md

- Use GBD 2021 data (most recent available)
- Show both sexes combined by default; support sex-stratified views as an option
- Display 7 GBD super-regions for the regional comparison
- Use age-standardised rates (not counts) for fair cross-regional comparison
- Include 95% uncertainty intervals as shaded bands on trend plots

## Demo Data

Pre-bundle summary data for at least 10 diseases: malaria, diabetes mellitus type 2, ischaemic heart disease, HIV/AIDS, lower respiratory infections, neonatal disorders, road injuries, depressive disorders, chronic kidney disease, tuberculosis. This covers a range of communicable, non-communicable, and injury causes.

## Stretch Goals

- Add an interactive HTML dashboard using Plotly
- Support sub-national data for countries with available estimates
- Compare two diseases side by side on the same axes
- Generate a "disease fact sheet" combining burden data with PubMed evidence counts
