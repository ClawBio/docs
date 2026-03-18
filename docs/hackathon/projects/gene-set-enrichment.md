---
title: Gene Set Enrichment
description: Submit a gene list to Enrichr and return ranked pathway enrichment results from KEGG, Reactome, and GO.
---

# Gene Set Enrichment

**Track**: B - Genomics Researchers
**Difficulty**: Intermediate
**Time estimate**: 2-4 hours

## What You'll Build

A ClawBio skill that takes a list of gene symbols, submits them to the Enrichr API, and retrieves enrichment results from three major pathway databases: KEGG, Reactome, and Gene Ontology (Biological Process). The output is a ranked table of significant pathways with p-values and a bar chart of the top 15.

## Why This Matters

A list of differentially expressed genes is only the starting point. Pathway enrichment reveals the biological processes and mechanisms at play, turning a gene list into a biological story. Enrichr makes this accessible without local database installation.

## Inputs and Outputs

**Input**: A text file with one gene symbol per line (HGNC symbols)
**Output**: Markdown table of enriched pathways (name, p-value, adjusted p-value, overlapping genes) and a horizontal bar chart PNG of the top 15 pathways

## Key APIs / Data Sources

- [Enrichr API](https://maayanlab.cloud/Enrichr/) - POST gene list, then GET results per library
- Libraries to query: `KEGG_2021_Human`, `Reactome_2022`, `GO_Biological_Process_2023`

## Getting Started

1. Create your skill folder: `skills/gene-set-enrichment/`
2. POST your gene list to `https://maayanlab.cloud/Enrichr/addList` with the genes as a newline-separated string
3. Use the returned `userListId` to GET results: `https://maayanlab.cloud/Enrichr/enrich?userListId=ID&backgroundType=KEGG_2021_Human`
4. Parse the JSON response: each entry contains term name, p-value, adjusted p-value, z-score, and overlapping genes
5. Combine results from all three libraries, sort by adjusted p-value, and generate the chart

## Domain Decisions for SKILL.md

- Report pathways with adjusted p-value < 0.05 only
- Use combined score (Enrichr's log(p) * z-score) as the primary ranking metric
- Show overlapping genes for each pathway to aid interpretation
- Warn the user if fewer than 10 genes are submitted (low statistical power)

## Demo Data

Use a list of 50 well-known cancer-related genes: TP53, BRCA1, BRCA2, EGFR, KRAS, MYC, APC, RB1, PTEN, PIK3CA, BRAF, NRAS, CDH1, VHL, WT1, NF1, NF2, RET, KIT, PDGFRA, ALK, ERBB2, FGFR3, IDH1, IDH2, NPM1, FLT3, DNMT3A, TET2, JAK2, MPL, CALR, SF3B1, ASXL1, EZH2, NOTCH1, FBXW7, CTNNB1, SMAD4, STK11, CDKN2A, CDK4, MDM2, MET, ROS1, NTRK1, MAP2K1, ARID1A, KMT2A, CREBBP.

## Stretch Goals

- Add dot plot visualisation (bubble size = gene count, colour = p-value)
- Support ranked gene lists for GSEA-style pre-ranked analysis
- Compare enrichment between two gene lists side by side
- Include disease-specific libraries (e.g. OMIM, DisGeNET)
