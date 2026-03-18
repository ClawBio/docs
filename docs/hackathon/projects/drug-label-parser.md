---
title: Drug Label Parser
description: Extract pharmacogenomic warnings, boxed warnings, and dosing information from FDA drug labels via DailyMed.
---

# Drug Label Parser

**Track**: A - AI Engineers
**Difficulty**: Intermediate
**Time estimate**: 2-4 hours

## What You'll Build

A ClawBio skill that queries the DailyMed API for a given drug name and extracts pharmacogenomic (PGx) warnings, FDA boxed warnings, and dosing adjustments. The output is a structured report that highlights genotype-specific prescribing information.

## Why This Matters

FDA drug labels contain critical PGx information, but it is buried in dense text across multiple sections. Clinicians rarely have time to read full labels. This skill surfaces the safety-critical genetic information that directly affects prescribing decisions.

## Inputs and Outputs

**Input**: Drug name (e.g. "warfarin", "codeine", "clopidogrel")
**Output**: Structured markdown report with: boxed warnings, PGx-relevant sections, recommended dose adjustments, and CYP enzyme mentions

## Key APIs / Data Sources

- [DailyMed SPL API](https://dailymed.nlm.nih.gov/dailymed/services) - search and retrieve Structured Product Labels
- Labels are returned as XML (SPL format); parse specific sections by LOINC codes

## Getting Started

1. Create your skill folder: `skills/drug-label-parser/`
2. Search for the drug: `GET /drugnames.json?drug_name=warfarin`
3. Fetch the SPL: `GET /spls/{setid}.xml`
4. Parse XML sections using LOINC codes: `34066-1` (boxed warning), `34068-7` (dosage), `43685-7` (warnings and precautions)
5. Scan text for PGx keywords: CYP2D6, CYP2C19, CYP2C9, VKORC1, HLA-B, poor metaboliser, etc.

## Domain Decisions for SKILL.md

- Target these LOINC sections: boxed warning (34066-1), dosage (34068-7), warnings (43685-7), clinical pharmacology (34090-1)
- Maintain a keyword list of 20+ PGx-relevant terms (enzyme names, metaboliser phenotypes, gene names)
- Flag "poor metaboliser" and "ultrarapid metaboliser" mentions with HIGH PRIORITY
- If multiple label versions exist, always use the most recent

## Demo Data

Search for "warfarin" (VKORC1/CYP2C9 dosing), "codeine" (CYP2D6 boxed warning), or "clopidogrel" (CYP2C19 warning). All are freely available on DailyMed with well-documented PGx content.

## Stretch Goals

- Cross-reference extracted warnings with CPIC guidelines
- Support batch processing of a full medication list
- Score each drug on a PGx relevance scale (high/medium/low)
- Generate a patient-friendly plain-language summary alongside the clinical report
