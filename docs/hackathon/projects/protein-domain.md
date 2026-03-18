---
title: Protein Domain Annotator
description: Fetch domain architecture, known variants, and AlphaFold structure links for any protein from UniProt.
---

# Protein Domain Annotator

**Track**: C - Proteomics
**Difficulty**: Beginner
**Time estimate**: 2-4 hours

## What You'll Build

A ClawBio skill that takes a UniProt accession ID and retrieves the protein's domain architecture, known disease-associated variants, and links to the AlphaFold predicted structure. The output is a structured markdown report with a domain map diagram.

## Why This Matters

Understanding protein domain architecture is fundamental to interpreting variant pathogenicity and predicting functional impact. A variant in a catalytic domain is very different from one in a linker region. This skill brings together structural and clinical information in one place.

## Inputs and Outputs

**Input**: A UniProt accession ID (e.g. "P04637" for TP53)
**Output**: Markdown report with: protein name and function, domain table (name, start, end, description), variant list with clinical significance, and AlphaFold structure URL

## Key APIs / Data Sources

- [UniProt REST API](https://rest.uniprot.org/) - protein features and function
- [InterPro API](https://www.ebi.ac.uk/interpro/api/) - detailed domain annotations
- [AlphaFold DB](https://alphafold.ebi.ac.uk/) - predicted structure links

## Getting Started

1. Create your skill folder: `skills/protein-domain/`
2. Fetch protein data: `GET https://rest.uniprot.org/uniprotkb/P04637.json`
3. Extract features of type "Domain", "Region", and "Binding site" from the features array
4. Fetch variants: filter features of type "Natural variant" with disease associations
5. Construct the AlphaFold link: `https://alphafold.ebi.ac.uk/entry/{UNIPROT_ID}`

## Domain Decisions for SKILL.md

- Show all annotated domains, not just Pfam (include PROSITE, SMART, and InterPro)
- For variants, prioritise those with disease associations and reviewed evidence
- Include the protein's recommended name and gene name in the header
- Link each domain to its InterPro entry for further reading

## Demo Data

Use P04637 (TP53, tumour protein p53). It has well-annotated domains (transactivation, DNA-binding, tetramerisation), hundreds of disease-associated variants, and a high-confidence AlphaFold structure. A second good test case is P00533 (EGFR).

## Stretch Goals

- Generate a visual domain map using matplotlib (rectangles for domains, markers for variants)
- Add post-translational modification sites (phosphorylation, ubiquitination)
- Cross-reference variants with ClinVar classifications
- Support batch lookup for a list of UniProt IDs
