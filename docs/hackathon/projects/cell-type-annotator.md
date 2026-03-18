---
title: Single-Cell Cluster Annotator
description: Annotate single-cell RNA-seq clusters with predicted cell types using marker gene databases.
---

# Single-Cell Cluster Annotator

**Track**: B - Genomics Researchers
**Difficulty**: Advanced
**Time estimate**: 2-4 hours

## What You'll Build

A ClawBio skill that takes a Scanpy AnnData object with pre-computed clusters and marker genes, then matches those markers against PanglaoDB and CellMarker databases to suggest cell type labels for each cluster. The output is an annotated cluster table and a dotplot of top markers per predicted cell type.

## Why This Matters

Cell type annotation is the interpretive bottleneck in single-cell analysis. Researchers spend hours manually comparing marker genes against databases. Automated annotation standardises this process and reduces subjective bias in cell type assignment.

## Inputs and Outputs

**Input**: A Scanpy AnnData object (H5AD file) with clustering and rank_genes_groups results
**Output**: TSV mapping each cluster to predicted cell types with confidence scores, plus a dotplot PNG of top markers

## Key APIs / Data Sources

- [PanglaoDB](https://panglaodb.se/markers.html) - downloadable TSV of cell type markers (no API; bundle the marker file)
- [CellMarker 2.0](http://bio-bigdata.hrbmu.edu.cn/CellMarker/) - downloadable marker database
- Scanpy for data handling and plotting

## Getting Started

1. Create your skill folder: `skills/cell-type-annotator/`
2. Download PanglaoDB markers TSV and parse it into a dict: `{cell_type: [gene_list]}`
3. For each cluster, get the top 20 marker genes from `adata.uns['rank_genes_groups']`
4. Score each cell type by counting overlapping markers (weighted by log fold change)
5. Assign the top-scoring cell type to each cluster, with a confidence score based on the overlap ratio

## Domain Decisions for SKILL.md

- Use human markers only (filter PanglaoDB by species)
- Require at least 3 overlapping markers for a confident assignment
- Report the top 3 candidate cell types per cluster, not just the best
- Flag clusters with no confident match as "Unresolved" rather than forcing an assignment
- Weight markers by their specificity score (PanglaoDB sensitivity/specificity columns)

## Demo Data

Use the `--demo` flag from ClawBio's existing scRNA Orchestrator skill to generate a demo AnnData object. Alternatively, download the PBMC 3k dataset from 10x Genomics (freely available) and run basic Scanpy preprocessing: filter, normalise, PCA, neighbours, leiden clustering, rank_genes_groups.

## Stretch Goals

- Add tissue-specific filtering (e.g. only consider brain cell types for brain samples)
- Support automated sub-clustering of ambiguous clusters
- Cross-reference with the Human Cell Atlas ontology for standardised cell type names
- Generate a UMAP coloured by predicted cell type
