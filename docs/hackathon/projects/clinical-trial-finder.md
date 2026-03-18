---
title: Clinical Trial Finder
description: Search ClinicalTrials.gov for active trials matching a gene or condition and return a structured table.
---

# Clinical Trial Finder

**Track**: A - AI Engineers
**Difficulty**: Beginner
**Time estimate**: 2-4 hours

## What You'll Build

A ClawBio skill that queries the ClinicalTrials.gov v2 API for active clinical trials related to a gene or condition. It returns a formatted table showing trial phase, status, location, sponsor, and eligibility criteria.

## Why This Matters

Patients and clinicians often struggle to find relevant clinical trials. Pharmacogenomics-guided treatment is expanding rapidly, but trial information is scattered and hard to parse. This skill makes trial discovery instant and structured.

## Inputs and Outputs

**Input**: A gene name (e.g. "CYP2D6") or condition (e.g. "warfarin pharmacogenomics")
**Output**: Markdown table of matching active trials with columns: NCT ID, title, phase, status, locations, enrolment count

## Key APIs / Data Sources

- [ClinicalTrials.gov API v2](https://clinicaltrials.gov/api/v2/studies) - JSON responses, no authentication required
- Query parameter: `query.term` for keyword search, `filter.overallStatus` to filter active trials

## Getting Started

1. Create your skill folder: `skills/clinical-trial-finder/`
2. Hit the API: `GET https://clinicaltrials.gov/api/v2/studies?query.term=warfarin+pharmacogenomics&filter.overallStatus=RECRUITING`
3. Parse the JSON response to extract protocolSection fields
4. Format identificationModule, statusModule, and designModule into a readable table
5. Add SKILL.md with your domain decisions

## Domain Decisions for SKILL.md

- Default to RECRUITING and NOT_YET_RECRUITING statuses only
- Show a maximum of 20 trials, sorted by start date (newest first)
- Extract eligibility criteria text and summarise age range and sex
- Flag trials in the user's country if location is provided

## Demo Data

Search for "warfarin pharmacogenomics" to find PGx-related trials. The ClinicalTrials.gov API is free and requires no authentication. Responses are paginated; use `pageSize=20` for demo purposes.

## Stretch Goals

- Add geographic filtering (e.g. "trials within 50 miles of London")
- Cross-reference trial drugs with ClawBio PharmGx results
- Generate a timeline visualisation of trial phases
- Support batch queries for multiple genes at once
