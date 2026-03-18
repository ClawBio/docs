---
title: Multi-Database Aggregator
description: Federate queries across ClinVar, gnomAD, and Open Targets to produce a unified variant or gene report.
---

# Multi-Database Aggregator

**Track**: A - AI Engineers
**Difficulty**: Advanced
**Time estimate**: 2-4 hours

## What You'll Build

A ClawBio skill that takes an rsID or gene name and queries three major databases in parallel: ClinVar (clinical significance), gnomAD (population frequencies), and Open Targets (drug associations and disease links). It merges the results into a single unified report.

## Why This Matters

Researchers and clinicians currently visit multiple websites and manually cross-reference data. A federated query skill reduces a 30-minute manual process to a single command, and catches connections that manual searching often misses.

## Inputs and Outputs

**Input**: An rsID (e.g. "rs3798220") or gene name (e.g. "LPA")
**Output**: Unified markdown report combining: ClinVar classification and review status, gnomAD population frequencies, Open Targets associated diseases and drugs

## Key APIs / Data Sources

- [ClinVar E-utilities](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/) - esearch + esummary for variant records
- [gnomAD GraphQL API](https://gnomad.broadinstitute.org/api) - population allele frequencies
- [Open Targets Platform API](https://platform-api.opentargets.io/api/v4/graphql) - gene-disease and gene-drug associations

## Getting Started

1. Create your skill folder: `skills/multi-db-aggregator/`
2. Build three query functions, one per database, each returning a standardised dict
3. Use `concurrent.futures.ThreadPoolExecutor` to run all three queries in parallel
4. Merge results into a single structured report with clear section headers
5. Handle partial failures gracefully: if one API is down, still return results from the others

## Domain Decisions for SKILL.md

- For rsID input, query ClinVar and gnomAD directly; map to gene for Open Targets
- For gene input, fetch top 5 ClinVar variants by review stars, gnomAD constraint metrics, and Open Targets top 10 associations
- Always include data freshness: show the date of each database query
- Confidence tier: label each finding as Reviewed, Preliminary, or Computational based on source evidence level

## Demo Data

Use rs3798220 (LPA gene, associated with heart disease risk and lipoprotein(a) levels). This variant has ClinVar entries, clear population frequency differences in gnomAD, and strong Open Targets disease associations, making it an ideal demonstration of cross-database value.

## Stretch Goals

- Add a fourth source: PharmGKB for pharmacogenomic annotations
- Cache results locally to avoid repeated API calls during development
- Generate a confidence-weighted summary score for clinical actionability
- Support batch input: a list of rsIDs producing a combined report
