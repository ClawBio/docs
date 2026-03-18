---
title: AMR Profiler
description: Detect antimicrobial resistance genes in metagenomic data using the CARD database.
---

# AMR Profiler

**Track**: E - Epidemiology
**Difficulty**: Advanced
**Time estimate**: 2-4 hours

## What You'll Build

A ClawBio skill that takes metagenomic sequence data (FASTA or FASTQ), searches against the CARD (Comprehensive Antibiotic Resistance Database), and produces a resistance profile. The output lists detected AMR genes, their drug class targets, resistance mechanisms, and a summary heatmap.

## Why This Matters

Antimicrobial resistance is one of the greatest global health threats. Environmental and clinical metagenomics can detect resistance genes circulating in communities, hospitals, and ecosystems. This skill turns raw sequence data into a structured resistance report.

## Inputs and Outputs

**Input**: A FASTA or FASTQ file of metagenomic reads or assembled contigs
**Output**: TSV of detected AMR genes (gene name, drug class, resistance mechanism, percent identity, coverage), summary by drug class, and a heatmap PNG if multiple samples are provided

## Key APIs / Data Sources

- [CARD Database](https://card.mcmaster.ca/) - download the CARD protein homolog model FASTA
- [RGI (Resistance Gene Identifier)](https://github.com/arpcard/rgi) - the standard tool for CARD-based detection
- Alternative: BLAST+ against CARD sequences for a simpler implementation

## Getting Started

1. Create your skill folder: `skills/amr-profiler/`
2. Download the CARD protein homolog model sequences from https://card.mcmaster.ca/download
3. For a Python-native approach: use BLAST+ (via subprocess) to align input sequences against CARD
4. Parse BLAST output: filter by percent identity >= 80% and query coverage >= 60%
5. Map each hit to its AMR gene family, drug class, and resistance mechanism using the CARD ontology (ARO)

## Domain Decisions for SKILL.md

- Minimum percent identity: 80% for "strict" hits, 60-80% for "loose" hits (report both, labelled)
- Minimum query coverage: 60% of the reference gene length
- Group results by drug class (e.g. beta-lactams, aminoglycosides, tetracyclines)
- Report resistance mechanism type: antibiotic inactivation, efflux, target alteration, target protection
- For multiple samples: generate a presence/absence heatmap across samples and drug classes

## Demo Data

Create a synthetic FASTA with 5 known resistance gene sequences spiked into 200 random background sequences. Use: blaTEM-1 (beta-lactam), aac(6')-Ib (aminoglycoside), tetM (tetracycline), ermB (macrolide), and vanA (glycopeptide). Truncate each to 80% length and introduce 5% mismatches to test sensitivity thresholds.

## Stretch Goals

- Add mobile genetic element detection (is the AMR gene on a plasmid or integron?)
- Calculate relative abundance of resistance classes normalised by total reads
- Compare a sample's resistance profile against a pre-antibiotic baseline
- Support Oxford Nanopore long reads alongside Illumina short reads
