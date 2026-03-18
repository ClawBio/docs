---
title: Outbreak Phylogenetic Clusterer
description: Build a neighbour-joining tree from consensus sequences and identify transmission clusters.
---

# Outbreak Phylogenetic Clusterer

**Track**: E - Epidemiology
**Difficulty**: Intermediate
**Time estimate**: 2-4 hours

## What You'll Build

A ClawBio skill that takes a FASTA file of consensus sequences (e.g. from a pathogen outbreak), builds a neighbour-joining phylogenetic tree, identifies transmission clusters based on genetic distance, and produces a tree figure and a cluster assignment table with a timeline.

## Why This Matters

During infectious disease outbreaks, phylogenetic analysis reveals which cases are linked by transmission and which are independent introductions. This information guides public health response: contact tracing, quarantine decisions, and intervention targeting.

## Inputs and Outputs

**Input**: A multi-FASTA file of aligned consensus sequences with date metadata in headers
**Output**: Newick tree file, cluster assignment TSV (sequence ID, cluster number, date), tree visualisation PNG, and a timeline figure showing clusters over time

## Key APIs / Data Sources

- [BioPython](https://biopython.org/) - sequence parsing, alignment, tree construction
- No external API needed; all computation is local
- Optional: [Nextstrain](https://nextstrain.org/) datasets for validation

## Getting Started

1. Create your skill folder: `skills/outbreak-clusterer/`
2. Parse the FASTA file using BioPython's `SeqIO`
3. Compute a pairwise distance matrix using Hamming distance (proportion of differing sites)
4. Build a neighbour-joining tree using BioPython's `DistanceTreeConstructor`
5. Define clusters: sequences within a genetic distance threshold (e.g. < 5 SNPs) belong to the same cluster
6. Draw the tree using BioPython's `Phylo.draw` or matplotlib

## Domain Decisions for SKILL.md

- Clustering threshold: 5 SNPs for SARS-CoV-2 (approximately 2 weeks of evolution); make configurable for other pathogens
- Require sequences to be pre-aligned (same length); reject input if lengths differ
- Extract dates from FASTA headers in format `>SAMPLE_ID|YYYY-MM-DD`
- Label clusters as Cluster_1, Cluster_2, etc., ordered by earliest sample date
- Singleton sequences (not within threshold of any other) are labelled "Sporadic"

## Demo Data

Generate 20 synthetic SARS-CoV-2-like sequences (29,903 bp). Create 3 clusters: Cluster A (8 sequences, 0-3 SNP differences, dates in week 1-2), Cluster B (7 sequences, 0-4 SNP differences, dates in week 2-3), Cluster C (3 sequences, 0-2 SNP differences, dates in week 4), plus 2 singletons. Introduce 50+ SNP differences between clusters.

## Stretch Goals

- Add bootstrap support values to internal nodes
- Detect potential super-spreader events (nodes with high branching)
- Integrate epidemiological metadata (location, age group) into the visualisation
- Support maximum likelihood tree building using IQ-TREE (external tool)
