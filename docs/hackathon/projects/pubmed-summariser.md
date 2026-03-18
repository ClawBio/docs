---
title: PubMed Research Summariser
description: Query PubMed for recent papers on a gene or disease and produce a structured markdown summary.
---

# PubMed Research Summariser

**Track**: A - AI Engineers
**Difficulty**: Beginner
**Time estimate**: 2-4 hours

## What You'll Build

A ClawBio skill that takes a gene name or disease term, queries the PubMed E-utilities API, and returns a structured markdown summary of the top recent papers. The summary includes titles, authors, journals, publication dates, and key findings extracted from abstracts.

## Why This Matters

Researchers spend hours manually searching PubMed and reading abstracts to stay current. An automated summariser turns a keyword into an actionable briefing in seconds, helping clinicians and researchers make faster evidence-based decisions.

## Inputs and Outputs

**Input**: A gene name (e.g. "BRCA1") or disease term (e.g. "type 2 diabetes")
**Output**: Structured markdown with paper titles, authors, journal, date, and a one-sentence abstract highlight for each of the top 10 results

## Key APIs / Data Sources

- [PubMed E-utilities](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/) - esearch.fcgi for IDs, efetch.fcgi for records
- Use retmode=xml and parse with Python's xml.etree.ElementTree

## Getting Started

1. Fork the ClawBio repo and create a new skill folder: `skills/pubmed-summariser/`
2. Use `esearch.fcgi?db=pubmed&term=BRCA1&retmax=10&sort=date` to get PMIDs
3. Use `efetch.fcgi?db=pubmed&id=PMID1,PMID2&retmode=xml` to fetch full records
4. Parse the XML to extract title, authors, journal, date, and abstract text
5. Format results as a markdown table or structured list

## Domain Decisions for SKILL.md

- Sort by publication date (most recent first) rather than relevance
- Limit to 10 results by default, configurable up to 50
- Extract the first sentence of each abstract as the "key finding"
- Filter to English-language articles only using `AND english[la]`

## Demo Data

Search for "BRCA1" or "type 2 diabetes" as your test queries. PubMed is freely accessible with no API key required (though an API key raises the rate limit from 3 to 10 requests per second). Register for a free key at https://www.ncbi.nlm.nih.gov/account/.

## Stretch Goals

- Add MeSH term expansion to improve recall
- Include citation counts using the elink API
- Generate a word cloud from combined abstracts
- Support date range filtering (e.g. last 6 months only)
