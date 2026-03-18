---
title: ACMG Variant Classifier
description: Implement the ACMG/AMP 28-criteria framework to classify variants as Pathogenic through to Benign.
---

# ACMG Variant Classifier

**Track**: D - Clinical
**Difficulty**: Advanced
**Time estimate**: 2-4 hours

## What You'll Build

A ClawBio skill that takes variant information (gene, consequence, population frequency, functional data) and applies the ACMG/AMP 2015 guidelines to produce a five-tier classification: Pathogenic, Likely Pathogenic, Variant of Uncertain Significance (VUS), Likely Benign, or Benign. Each classification includes the specific evidence codes that support it.

## Why This Matters

ACMG classification is the international standard for clinical variant interpretation, but manually applying all 28 criteria is time-consuming and error-prone. Automating the framework ensures consistent, auditable classifications that meet clinical-grade standards.

## Inputs and Outputs

**Input**: JSON or dict with fields: gene, hgvs_c, hgvs_p, consequence, gnomad_af, clinvar_entries, functional_assay_result, inheritance_pattern, computational_predictions
**Output**: Classification (Pathogenic/LP/VUS/LB/Benign), list of triggered evidence codes (e.g. PVS1, PM2, PP3), and a plain-language explanation of the reasoning

## Key APIs / Data Sources

- [ClinGen Sequence Variant Interpretation](https://clinicalgenome.org/working-groups/sequence-variant-interpretation/) - official rule specifications
- [InterVar](https://wintervar.wglab.org/) - reference implementation for validation
- gnomAD for population frequency checks; ClinVar for prior classifications

## Getting Started

1. Create your skill folder: `skills/acmg-classifier/`
2. Implement the 28 evidence criteria as individual functions that return True/False
3. Build the combining logic: PVS1 + PM1 = Likely Pathogenic; 2x Strong = Pathogenic; etc.
4. Wire up automatic checks: population frequency for BA1/BS1/PM2, consequence type for PVS1, computational tools for PP3/BP4
5. Return the final classification with all triggered codes and explanations

## Domain Decisions for SKILL.md

- BA1 stand-alone benign threshold: allele frequency > 0.05 (5%) in any gnomAD population
- BS1 benign strong threshold: allele frequency > 0.01 (1%) for dominant conditions
- PM2 supporting threshold: absent or below 0.0001 in gnomAD
- PVS1 applies to null variants (nonsense, frameshift, canonical splice) in genes where loss of function is a known disease mechanism
- Use ClinGen-curated gene-specific rule modifications where available
- Computational predictions (PP3/BP4): require consensus from at least 3 of 5 tools (REVEL, CADD, MetaSVM, BayesDel, GERP)

## Demo Data

Test with well-characterised variants: BRCA1 c.68_69delAG (Pathogenic, founder mutation), TP53 R175H (Pathogenic, hotspot), and a common benign polymorphism like rs1801133 (MTHFR C677T, gnomAD AF 0.33). Include at least one VUS to demonstrate intermediate classification.

## Stretch Goals

- Add ClinGen gene-specific rule modifications for BRCA1, TP53, RASopathy genes
- Support automated gnomAD and ClinVar lookups (not just pre-supplied data)
- Generate a visual evidence summary showing each criterion's status
- Implement the 2023 ClinGen quantitative framework for PP3/BP4 (calibrated REVEL thresholds)
