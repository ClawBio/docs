---
title: Variant Warehouse
description: Ingest variants from multiple sources into a deduplicated, queryable warehouse built on Delta Lake.
---

# Variant Warehouse

**Track**: F - Databricks
**Difficulty**: Advanced
**Time estimate**: 2-4 hours

## What You'll Build

A ClawBio skill that ingests variant data from multiple sources (ClinVar, gnomAD downloads, user VCF files), deduplicates on genomic coordinates, and creates a unified queryable warehouse. The warehouse uses Delta Lake for storage, enabling ACID transactions, schema evolution, and time travel. Designed to scale to billions of variants on Databricks.

## Why This Matters

Genomic variant data is scattered across dozens of databases, each with different formats, identifiers, and update schedules. A unified warehouse eliminates redundant lookups, enables cross-source queries, and provides a single source of truth for variant annotation in any downstream analysis.

## Inputs and Outputs

**Input**: One or more data sources: ClinVar VCF, gnomAD sites VCF, user-provided VCF files
**Output**: A Delta Lake table with unified schema: chrom, pos, ref, alt, rsid, sources (list), clinvar_significance, gnomad_af, gene, consequence. Plus an ingestion log tracking what was loaded and when.

## Key APIs / Data Sources

- [ClinVar FTP](https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/) - monthly VCF releases
- [gnomAD Downloads](https://gnomad.broadinstitute.org/downloads) - sites VCF files
- [Delta Lake](https://delta.io/) - `pip install deltalake` for local, or Databricks for scale
- User VCF files as the third source

## Getting Started

1. Create your skill folder: `skills/databricks-variant-warehouse/`
2. Define the unified schema with all target columns and source-tracking metadata
3. Write source-specific parsers for ClinVar VCF and gnomAD VCF (extract the fields each provides)
4. Implement deduplication: merge on (chrom, pos, ref, alt) as the unique key
5. Write to Delta format with merge/upsert logic: new variants are inserted, existing variants gain additional source annotations

## Domain Decisions for SKILL.md

- Unique key: (chrom, pos, ref, alt) after left-alignment and normalisation
- Normalise chromosome names to "chr1" format across all sources
- Store source provenance as a list column: ["clinvar", "gnomad", "user_vcf"]
- Use Delta Lake merge (UPSERT) for incremental updates: `MERGE INTO warehouse USING new_data ON key_match`
- Track ingestion metadata: source, file name, record count, timestamp, schema version
- Partition by chromosome for query performance

## Demo Data

For hackathon purposes, use small subsets: ClinVar chromosome 22 only (approximately 5,000 variants), gnomAD exome sites chromosome 22 (approximately 500,000 variants), and a user VCF with 100 variants on chromosome 22. This keeps file sizes manageable while demonstrating the full merge workflow. Download ClinVar chr22 from the FTP site or pre-bundle it in your skill's data directory.

## Stretch Goals

- Add automated monthly refresh from ClinVar FTP with change detection
- Implement a query interface: "show me all pathogenic variants in BRCA1 with AF < 0.001"
- Add PharmGKB as a fourth source for pharmacogenomic annotations
- Build a Databricks notebook that demonstrates warehouse queries at scale with Spark SQL
- Track data lineage with Delta Lake's history and time travel features
