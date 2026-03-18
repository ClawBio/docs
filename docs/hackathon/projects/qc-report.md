---
title: QC Report Generator
description: Parse FastQC output and produce a structured pass/fail quality report with configurable thresholds.
---

# QC Report Generator

**Track**: B - Genomics Researchers
**Difficulty**: Beginner
**Time estimate**: 2-4 hours

## What You'll Build

A ClawBio skill that reads FastQC output files (either the zip archive or summary.txt) and generates a clean quality control report. The report applies configurable thresholds and produces a pass/fail verdict for each QC metric, with a final overall recommendation.

## Why This Matters

Every sequencing experiment starts with quality control, but FastQC output requires manual inspection and interpretation. An automated QC skill standardises the assessment, catches problems early, and saves hours of repetitive review across large batches.

## Inputs and Outputs

**Input**: FastQC output zip file or extracted summary.txt
**Output**: Markdown report with per-module pass/warn/fail status, overall quality verdict, and specific recommendations for failed metrics

## Key APIs / Data Sources

- No external API required; this skill parses local FastQC output files
- [FastQC documentation](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) for module descriptions and default thresholds

## Getting Started

1. Create your skill folder: `skills/qc-report/`
2. Download sample FastQC data from the FastQC website (or run FastQC on any public FASTQ)
3. Parse `summary.txt` for module-level PASS/WARN/FAIL verdicts
4. Parse `fastqc_data.txt` for detailed metrics: per-base quality scores, adapter content percentages, duplication levels
5. Apply your thresholds and generate a structured markdown report

## Domain Decisions for SKILL.md

- Per-base quality: fail if median drops below Q20 in any position
- Adapter content: fail if any adapter exceeds 5% at any position
- Duplication: warn above 30%, fail above 50%
- Overall verdict: PASS (no fails), CONDITIONAL (warns only), FAIL (any fail)

## Demo Data

Download the example "Good Illumina Data" and "Bad Illumina Data" FastQC reports from https://www.bioinformatics.babraham.ac.uk/projects/fastqc/. Alternatively, use public FASTQ files from the SRA (e.g. SRR000001) and run FastQC locally.

## Stretch Goals

- Support batch processing of multiple FastQC outputs (e.g. all samples in a run)
- Generate a comparison heatmap showing QC status across samples
- Auto-detect sequencing platform (Illumina, Nanopore, PacBio) from encoding
- Suggest trimming parameters based on identified quality issues
