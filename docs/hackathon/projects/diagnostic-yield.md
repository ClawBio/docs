---
title: Diagnostic Yield Calculator
description: Rank candidate genes for a set of HPO phenotype terms and calculate a diagnostic yield score.
---

# Diagnostic Yield Calculator

**Track**: D - Clinical
**Difficulty**: Advanced
**Time estimate**: 2-4 hours

## What You'll Build

A ClawBio skill that takes a variant list and a set of HPO (Human Phenotype Ontology) phenotype terms, then ranks candidate genes by how well they explain the patient's phenotype. The output is a scored list of candidate diagnoses with supporting evidence.

## Why This Matters

Whole exome sequencing typically identifies thousands of variants, but only one or a few explain the patient's condition. Phenotype-driven prioritisation is how clinical geneticists narrow the list. Automating this process improves diagnostic yield and reduces time to diagnosis.

## Inputs and Outputs

**Input**: A list of candidate variants (gene, consequence, frequency) and a list of HPO terms (e.g. HP:0001166, HP:0000545)
**Output**: Ranked gene table with diagnostic yield score, phenotype match details, and inheritance pattern compatibility

## Key APIs / Data Sources

- [HPO API](https://hpo.jax.org/api/) - gene-phenotype associations and term relationships
- [OMIM API](https://api.omim.org/) - gene-disease relationships (requires free API key)
- [Exomiser](https://exomiser.github.io/Exomiser/) - reference algorithm for validation

## Getting Started

1. Create your skill folder: `skills/diagnostic-yield/`
2. For each HPO term, fetch associated genes from the HPO API: `GET https://hpo.jax.org/api/hpo/term/{HPO_ID}/genes`
3. Build a gene-to-phenotype score matrix: count how many input HPO terms each gene is associated with
4. Weight by information content (rare phenotypes score higher than common ones)
5. Intersect with the variant list: only score genes that have at least one rare, damaging variant

## Domain Decisions for SKILL.md

- Use information content (IC) weighting: a gene matching a specific term like "arachnodactyly" scores higher than one matching "tall stature"
- Require variant frequency < 0.01 for dominant and < 0.05 for recessive conditions
- Inheritance pattern check: for autosomal recessive, require two qualifying variants in the same gene
- Diagnostic yield score = sum of IC-weighted phenotype matches, normalised to 0-1 scale
- Flag genes in OMIM with established gene-disease relationships as higher confidence

## Demo Data

Simulate a Marfan syndrome case. Use these 5 HPO terms: HP:0001166 (arachnodactyly), HP:0000545 (myopia), HP:0001382 (joint hypermobility), HP:0002705 (high narrow palate), HP:0002816 (genu recurvatum). Create a variant list with 50 variants across 30 genes, ensuring FBN1 has a rare missense variant. The skill should rank FBN1 at the top.

## Stretch Goals

- Add phenotype term expansion using HPO hierarchy (parent and child terms)
- Integrate CADD and REVEL scores for variant-level prioritisation
- Support trio analysis (proband + parents) for de novo variant detection
- Generate a clinical report suitable for inclusion in a genetic counselling letter
