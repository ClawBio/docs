---
title: Protein Interaction Mapper
description: Query STRING for protein-protein interactions and produce a network table with hub scores and a network figure.
---

# Protein Interaction Mapper

**Track**: C - Proteomics
**Difficulty**: Beginner
**Time estimate**: 2-4 hours

## What You'll Build

A ClawBio skill that takes a list of gene or protein names, queries the STRING database API, and returns a protein-protein interaction (PPI) network. The output includes an interaction table with confidence scores, hub protein rankings, and a matplotlib network visualisation.

## Why This Matters

Proteins rarely act alone. Understanding interaction networks reveals functional modules, identifies central regulators (hubs), and highlights potential drug targets. STRING is the gold standard for PPI data, combining experimental and predicted interactions.

## Inputs and Outputs

**Input**: A list of gene/protein names (e.g. ["TP53", "BRCA1", "EGFR", "MYC", "AKT1"])
**Output**: Interaction table (protein A, protein B, combined score), hub scores (degree centrality), and a network figure PNG

## Key APIs / Data Sources

- [STRING API](https://string-db.org/api/) - REST API with JSON output
- Endpoint: `https://string-db.org/api/json/network?identifiers=PROTEIN_LIST&species=9606`

## Getting Started

1. Create your skill folder: `skills/protein-interaction/`
2. Format your protein list as a newline-separated string for the STRING API
3. Query the network endpoint with `species=9606` (human) and `required_score=400` (medium confidence)
4. Parse the JSON to extract interaction pairs and combined scores
5. Use networkx to build a graph, compute degree centrality, and draw the network with matplotlib

## Domain Decisions for SKILL.md

- Default species: Homo sapiens (NCBI taxon 9606)
- Minimum interaction confidence score: 400 (medium) by default, configurable
- Hub score: use degree centrality (number of connections per node)
- Limit network to first-shell interactors only (direct partners of input proteins)

## Demo Data

Use these five well-studied cancer proteins: TP53, BRCA1, EGFR, MYC, AKT1. They form a densely connected network in STRING with high-confidence interactions. The API call requires no authentication for small queries.

## Stretch Goals

- Add functional enrichment using STRING's enrichment endpoint
- Colour nodes by Gene Ontology category
- Support a second-shell expansion (friends of friends)
- Export the network in Cytoscape-compatible format (XGMML or SIF)
