---
title: Pharmacogenomics Interaction Checker
description: Check a patient's genotypes against their medication list for drug-gene interactions using CPIC guidelines.
---

# Pharmacogenomics Interaction Checker

**Track**: D - Clinical
**Difficulty**: Intermediate
**Time estimate**: 2-4 hours

## What You'll Build

A ClawBio skill that takes a patient genotype file and a list of current medications, then checks for pharmacogenomic interactions using CPIC (Clinical Pharmacogenetics Implementation Consortium) guidelines. The output is an interaction report with evidence levels and dosing recommendations. This extends ClawBio's existing PharmGx Reporter with multi-drug awareness.

## Why This Matters

Adverse drug reactions are a leading cause of hospital admissions. Many are preventable with pharmacogenomic testing. This skill connects genotype data to real prescribing decisions, flagging interactions before they cause harm.

## Inputs and Outputs

**Input**: Patient genotype file (23andMe format or simple TSV with rsID, genotype columns) and a medication list (one drug per line or JSON array)
**Output**: Markdown interaction report with: drug name, gene, diplotype, phenotype, CPIC recommendation, evidence level (A/B/C/D)

## Key APIs / Data Sources

- [CPIC API](https://api.cpicpgx.org/) - guidelines, allele definitions, diplotype-phenotype mappings
- [PharmGKB](https://api.pharmgkb.org/) - clinical annotations and drug label information
- ClawBio PharmGx Reporter as the base skill to extend

## Getting Started

1. Create your skill folder: `skills/pgx-interaction-checker/`
2. Parse the genotype file to extract relevant PGx rsIDs (CYP2D6, CYP2C19, CYP2C9, VKORC1, SLCO1B1, etc.)
3. Call alleles using the CPIC allele definition tables (map rsIDs to star alleles)
4. Look up each medication against CPIC guidelines to find gene-drug pairs
5. For each match, retrieve the dosing recommendation based on the patient's diplotype and phenotype

## Domain Decisions for SKILL.md

- Limit to CPIC Level A and B evidence guidelines (strongest clinical evidence)
- Support these key genes: CYP2D6, CYP2C19, CYP2C9, CYP3A5, VKORC1, SLCO1B1, DPYD, TPMT, UGT1A1, HLA-B
- Use CPIC's standard phenotype assignments (e.g. *1/*2 = Intermediate Metaboliser for CYP2C19)
- Flag "actionable" interactions (dose change or alternative drug required) separately from "informative" ones
- Always include a disclaimer that results require clinical validation

## Demo Data

Create `demo_patient.txt` with genotypes for 20 key PGx rsIDs (rs1065852, rs4244285, rs1799853, rs1057910, rs9923231, etc.). Test with the medication list: ["warfarin", "codeine", "simvastatin", "clopidogrel", "tamoxifen"]. This combination should trigger interactions for CYP2C9/VKORC1, CYP2D6, SLCO1B1, CYP2C19, and CYP2D6 respectively.

## Stretch Goals

- Add drug-drug interaction checking alongside drug-gene interactions
- Generate a patient-friendly summary in plain language
- Support VCF input format with automatic rsID extraction
- Add a polypharmacy risk score based on the number and severity of interactions
