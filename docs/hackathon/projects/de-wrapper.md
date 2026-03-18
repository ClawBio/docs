---
title: Differential Expression Wrapper
description: Run differential expression analysis on a counts matrix using PyDESeq2 and produce results with volcano and MA plots.
---

# Differential Expression Wrapper

**Track**: B - Genomics Researchers
**Difficulty**: Intermediate
**Time estimate**: 2-4 hours

## What You'll Build

A ClawBio skill that takes a gene counts matrix and sample metadata, runs differential expression analysis using PyDESeq2, and outputs a results table sorted by adjusted p-value, a volcano plot, and an MA plot. Everything runs in pure Python with no R dependency.

## Why This Matters

Differential expression is one of the most common analyses in genomics, but setting up the statistical framework correctly requires careful attention to normalisation, dispersion estimation, and multiple testing correction. This skill encapsulates those decisions.

## Inputs and Outputs

**Input**: A counts matrix CSV (genes as rows, samples as columns) and a metadata CSV (sample names, condition labels)
**Output**: TSV of DE results (gene, baseMean, log2FoldChange, pvalue, padj), volcano plot PNG, MA plot PNG

## Key APIs / Data Sources

- [PyDESeq2](https://pydeseq2.readthedocs.io/) - Python implementation of DESeq2
- No external API needed; all computation is local

## Getting Started

1. Create your skill folder: `skills/de-wrapper/`
2. Install PyDESeq2: `pip install pydeseq2`
3. Load the counts matrix into a pandas DataFrame and the metadata into an AnnData-compatible format
4. Run `DeseqDataSet` and `DeseqStats` from PyDESeq2
5. Generate a volcano plot (log2FC vs -log10 padj) and MA plot (baseMean vs log2FC) using matplotlib

## Domain Decisions for SKILL.md

- Filter genes with fewer than 10 total counts across all samples before analysis
- Use Benjamini-Hochberg correction with a significance threshold of padj < 0.05
- Label the top 10 genes by adjusted p-value on the volcano plot
- Colour scheme: red for upregulated (log2FC > 1), blue for downregulated (log2FC < -1), grey for non-significant

## Demo Data

Generate a synthetic dataset: 100 genes, 6 samples (3 treated, 3 control). Use numpy to simulate counts from a negative binomial distribution. Spike in 10 truly differentially expressed genes with a 4-fold change. Save as `demo_counts.csv` and `demo_metadata.csv`.

## Stretch Goals

- Add PCA plot of samples coloured by condition
- Support multi-factor designs (e.g. condition + batch)
- Export results in a format compatible with gene set enrichment tools
- Add shrinkage estimation for log2 fold changes (apeglm-style)
