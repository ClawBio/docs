---
title: Benchmarks
description: Quantitative evidence for the SKILL.md approach
---

# Benchmarks

ClawBio's value proposition rests on measurable improvements in accuracy, reproducibility, and coverage. Four benchmarks provide the evidence base.

## 1. Agent Error Reduction

| Parameter | Value |
|-----------|-------|
| **Queries** | 100 pharmacogenomics questions |
| **Comparison** | SKILL.md-guided agent vs. unconstrained LLM |
| **Target** | < 2% error rate with SKILL.md |
| **Metrics** | Factual accuracy, guideline compliance, hallucination rate |

Queries span drug-gene interactions, dosing recommendations, and phenotype interpretation. Each answer is evaluated against CPIC guideline ground truth by two independent reviewers.

## 2. Reproduction Time

| Parameter | Value |
|-----------|-------|
| **Analyses** | 20 published bioinformatics workflows |
| **Comparison** | ClawBio skill vs. original GitHub repository |
| **Target** | > 90% success rate in < 5 minutes |
| **Metrics** | Time to first successful run, output match rate |

Each analysis is attempted by a researcher unfamiliar with the original tool. Success requires matching output within a defined tolerance (SHA-256 checksum for deterministic tools, statistical equivalence for stochastic ones).

## 3. Domain Coverage

| Parameter | Value |
|-----------|-------|
| **Target** | 200+ skills across 10+ sub-domains |
| **Sub-domains** | Pharmacogenomics, population genetics, single-cell, variant annotation, structural biology, metagenomics, transcriptomics, epigenomics, clinical genomics, proteomics |
| **Metric** | Skills per sub-domain, guideline authorities covered |

Coverage is tracked continuously on the clawbio.ai hub with real-time dashboards.

## 4. Correctness vs. Execution

| Parameter | Value |
|-----------|-------|
| **Method** | Checksum match + reference dataset validation |
| **Deterministic skills** | SHA-256 output checksum must match reference |
| **Stochastic skills** | Statistical equivalence test (KS test, p > 0.01) against reference dataset |
| **Scope** | All skills with demo data |

Every skill's demo output is checksummed at release. CI runs verify that subsequent versions produce identical (or statistically equivalent) results.

## Publication Plan

Both the agent error reduction and reproduction time benchmarks will be:

1. **Published as preprints** on bioRxiv (Q3 2026)
2. **Submitted for peer review** to Briefings in Bioinformatics or Nucleic Acids Research (Q4 2026)
3. **Data and code** deposited on Zenodo with DOIs

All benchmark protocols, raw data, and analysis scripts will be openly available under CC-BY 4.0.
