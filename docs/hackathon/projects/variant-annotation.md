---
title: Variant Annotation Pipeline
description: Annotate a VCF file with ClinVar classifications, gnomAD frequencies, and gene impact using Ensembl VEP.
---

# Variant Annotation Pipeline

**Track**: B - Genomics Researchers
**Difficulty**: Intermediate
**Time estimate**: 2-4 hours

## What You'll Build

A ClawBio skill that reads a VCF file, sends each variant to the Ensembl VEP REST API, and produces an annotated output with gene name, consequence type, ClinVar clinical significance, and gnomAD allele frequency. The result is a clean TSV and a markdown summary.

## Why This Matters

Raw VCF files from sequencing pipelines contain thousands of variants with no clinical context. Annotation is the critical first step in any genomic analysis, turning coordinates into actionable biological information.

## Inputs and Outputs

**Input**: A VCF file (standard format, single or multi-sample)
**Output**: Annotated TSV with columns: CHROM, POS, REF, ALT, Gene, Consequence, ClinVar, gnomAD_AF. Plus a markdown summary of pathogenic/likely pathogenic findings.

## Key APIs / Data Sources

- [Ensembl VEP REST API](https://rest.ensembl.org/documentation/info/vep_region_post) - POST up to 200 variants per request
- VEP returns consequence, gene symbol, and links to ClinVar and frequency databases

## Getting Started

1. Create your skill folder: `skills/variant-annotation/`
2. Parse the input VCF using Python (skip header lines starting with `#`)
3. Batch variants into groups of 200 and POST to VEP: `POST https://rest.ensembl.org/vep/homo_sapiens/region`
4. Extract gene, consequence, ClinVar, and frequency fields from the JSON response
5. Write annotated results to TSV and generate a markdown summary of clinically relevant findings

## Domain Decisions for SKILL.md

- Use GRCh38 as the default genome assembly
- Prioritise the most severe consequence per variant (VEP returns multiple)
- Flag variants with gnomAD AF < 0.001 and a ClinVar pathogenic classification
- Rate-limit API calls to 15 requests per second (Ensembl fair usage policy)

## Demo Data

Create a synthetic VCF with 20 variants at well-known positions. Include: rs1801133 (MTHFR), rs1799853 (CYP2C9), rs1057910 (CYP2C9), rs9923231 (VKORC1), and 16 others from ClinVar with mixed pathogenicity. Use standard VCF 4.2 format with a single sample column.

## Stretch Goals

- Support GRCh37 input with automatic liftover
- Add CADD scores via the CADD API for variants of uncertain significance
- Generate a summary plot showing consequence type distribution
- Filter output to a gene panel (user-provided gene list)
