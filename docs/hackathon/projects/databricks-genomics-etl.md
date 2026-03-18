---
title: Genomics ETL on Databricks
description: Build a skill that transforms raw genetic files into structured Delta Lake tables ready for analysis at scale.
---

# Genomics ETL on Databricks

**Track**: F - Databricks
**Difficulty**: Intermediate
**Time estimate**: 2-4 hours

## What You'll Build

A ClawBio skill that takes raw genetic data (VCF or 23andMe format), parses and normalises it, and writes a structured Delta Lake table with summary statistics. The skill is designed to run locally for the hackathon but scale to thousands of genomes on Databricks Spark. Databricks is offering a week of Solutions Architect time to productionise the best output from this track.

## Why This Matters

Genomic data comes in dozens of formats and sizes. Before any analysis can happen, data must be parsed, validated, normalised, and stored in a queryable format. Delta Lake provides ACID transactions, schema enforcement, and time travel, making it the ideal foundation for a genomics data platform.

## Inputs and Outputs

**Input**: A raw genetic file (VCF 4.2 or 23andMe TSV format)
**Output**: A Delta Lake table (Parquet files + Delta log) with columns: chrom, pos, ref, alt, genotype, quality, rsid. Plus a summary stats JSON: total variants, het/hom ratio, transition/transversion ratio, variants per chromosome.

## Key APIs / Data Sources

- [Delta Lake](https://delta.io/) - open-source storage layer (`pip install delta-spark` or `pip install deltalake` for standalone)
- [Databricks Community Edition](https://community.cloud.databricks.com/) - free tier for testing with Spark
- No external bioinformatics API needed; parsing is local

## Getting Started

1. Create your skill folder: `skills/databricks-genomics-etl/`
2. Write a parser that handles both VCF and 23andMe formats, outputting a common schema
3. Validate each record: check chromosome naming (chr1 vs 1), position is numeric, alleles are valid bases
4. Write to Delta format using the `deltalake` Python library (no Spark required for local dev)
5. Compute summary statistics and write them as a JSON sidecar file

## Domain Decisions for SKILL.md

- Normalise chromosome names to "chr1" format (prepend "chr" if missing, convert "MT" to "chrM")
- Store genotypes as diploid strings: "0/0", "0/1", "1/1" (VCF-style)
- Partition the Delta table by chromosome for efficient querying
- Schema: chrom (string), pos (int64), ref (string), alt (string), genotype (string), quality (float), rsid (string)
- Reject records with invalid alleles (anything other than A, C, G, T, or .)

## Demo Data

Use ClawBio's existing demo genotype files, or create a synthetic 23andMe file with 1,000 variants across all chromosomes. Include a mix of SNPs and a few indels. Add 5 intentionally malformed rows to test validation (missing alleles, non-numeric position, invalid chromosome).

## Stretch Goals

- Add a Databricks notebook that reads the Delta table and runs a simple GWAS query
- Implement schema evolution: handle new columns gracefully when format versions change
- Add data lineage tracking: record source file, parse timestamp, and skill version in metadata
- Support streaming ingestion for real-time variant loading
