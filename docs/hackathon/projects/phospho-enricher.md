---
title: Phosphoproteomics Enricher
description: Perform kinase-substrate enrichment analysis on a list of phosphosites to identify active kinases.
---

# Phosphoproteomics Enricher

**Track**: C - Proteomics
**Difficulty**: Advanced
**Time estimate**: 2-4 hours

## What You'll Build

A ClawBio skill that takes a list of phosphorylation sites, performs kinase-substrate enrichment analysis using the KEA3 API, and returns a ranked list of kinases predicted to be active. The output includes a ranked kinase table and a bar chart of the top enriched kinases.

## Why This Matters

Phosphoproteomics experiments identify thousands of regulated phosphosites, but the key biological question is: which kinases are driving those changes? Kinase enrichment analysis bridges the gap between phosphosite lists and actionable signalling biology.

## Inputs and Outputs

**Input**: A list of phosphosites in gene_position format (e.g. "AKT1_S473", "MAPK1_T185")
**Output**: Ranked table of enriched kinases (kinase name, p-value, substrate overlap count), bar chart PNG of top 15 kinases

## Key APIs / Data Sources

- [KEA3 API](https://maayanlab.cloud/kea3/api) - POST a gene list, receive kinase enrichment results
- Alternative: PhosphoSitePlus (requires downloaded dataset, free for academic use)

## Getting Started

1. Create your skill folder: `skills/phospho-enricher/`
2. Parse the input phosphosite list and extract gene names (KEA3 uses gene symbols)
3. POST the gene list to `https://maayanlab.cloud/kea3/api/enrich/` as JSON
4. Parse the response to extract kinase rankings from the "Integrated--meanRank" result set
5. Generate a horizontal bar chart of the top 15 kinases ranked by mean rank

## Domain Decisions for SKILL.md

- Use KEA3's integrated ranking (mean rank across all libraries) as the primary result
- Also report results from individual libraries: ChengKSIN, PTMsigDB, PhosphoSitePlus
- Minimum input size: warn if fewer than 5 phosphosites are submitted
- Map phosphosite format (GENE_POSITION) to gene symbols before querying KEA3
- Preserve the original phosphosite identifiers in the output for traceability

## Demo Data

Use 30 known AKT substrates as your test set: GSK3B_S9, TSC2_T1462, FOXO1_S256, FOXO3_S253, BAD_S136, PRAS40_T246, AS160_T642, MDM2_S166, CREB1_S133, PFKFB2_S483, NOS3_S1177, CHEK1_S345, CDKN1B_T157, WNK1_T60, ACLY_S455, THEM4_S46, ATP6V1H_S16, SRPK2_T492, PALLD_S893, BNIP3L_S104, RPS6_S235, TBC1D4_T642, PDCD4_S67, SKP2_S72, MCL1_S159, XIAP_S87, GSK3A_S21, BRCA1_S694, KAT5_S86, CASP9_S196.

## Stretch Goals

- Add substrate motif analysis using the phosphosite flanking sequences
- Visualise kinase-substrate relationships as a network graph
- Cross-reference enriched kinases with known drug targets (e.g. kinase inhibitors)
- Support quantitative input (fold changes) for weighted enrichment
