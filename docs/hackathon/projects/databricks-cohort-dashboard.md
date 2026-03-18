---
title: Cohort Analytics Dashboard
description: Run ClawBio PharmGx across multiple patients and produce a cohort-level pharmacogenomics dashboard.
---

# Cohort Analytics Dashboard

**Track**: F - Databricks
**Difficulty**: Intermediate
**Time estimate**: 2-4 hours

## What You'll Build

A ClawBio skill that takes multiple patient genotype files, runs the PharmGx Reporter on each, and aggregates results into a cohort-level dashboard. The dashboard shows drug risk distributions, metaboliser phenotype frequencies, and population-level prescribing implications. Designed to scale to thousands of patients on Databricks Spark.

## Why This Matters

Individual pharmacogenomics is valuable, but cohort-level analysis reveals population patterns that inform hospital formulary decisions, clinical guideline updates, and health system planning. A hospital running PharmGx across all patients can identify which drugs pose the greatest population-level risk.

## Inputs and Outputs

**Input**: A directory of patient genotype files (23andMe or VCF format, one per patient)
**Output**: Cohort dashboard with: metaboliser phenotype frequency table, drug risk distribution bar charts (PNG), high-risk patient summary, and a CSV of all patient-drug interactions

## Key APIs / Data Sources

- ClawBio PharmGx Reporter (existing skill) for per-patient analysis
- [CPIC API](https://api.cpicpgx.org/) for guideline data
- [Databricks Community Edition](https://community.cloud.databricks.com/) for scaled execution (optional)

## Getting Started

1. Create your skill folder: `skills/databricks-cohort-dashboard/`
2. Write a batch runner that iterates over all genotype files in a directory and calls PharmGx Reporter on each
3. Collect per-patient results into a single pandas DataFrame
4. Compute cohort-level summaries: phenotype frequencies per gene, drug risk counts, patients needing dose adjustment
5. Generate dashboard figures: stacked bar chart of phenotypes per gene, heatmap of drug risks across the cohort

## Domain Decisions for SKILL.md

- Process patients in parallel using `concurrent.futures.ProcessPoolExecutor` (local) or Spark map (Databricks)
- Focus on the 10 most clinically actionable genes: CYP2D6, CYP2C19, CYP2C9, CYP3A5, VKORC1, SLCO1B1, DPYD, TPMT, UGT1A1, HLA-B
- Flag any drug where > 20% of the cohort requires dose adjustment as a "formulary alert"
- De-identify patient data in the output: use patient_001, patient_002, etc.
- Report Hardy-Weinberg equilibrium p-values per variant as a data quality check

## Demo Data

Use ClawBio's existing demo genotype files. Create 10 synthetic patient files with varying genotypes across key PGx loci. Ensure diversity: include at least one poor metaboliser, one ultrarapid metaboliser, and one intermediate metaboliser per gene to demonstrate the full phenotype spectrum.

## Stretch Goals

- Add a Databricks notebook that runs the same pipeline on 1,000+ patients using Spark
- Include ancestry-stratified analysis (if self-reported ancestry is available)
- Generate a cost-impact estimate: "switching 15 patients from codeine to morphine would prevent X ADRs per year"
- Build an interactive HTML dashboard with Plotly for clinical pharmacists
