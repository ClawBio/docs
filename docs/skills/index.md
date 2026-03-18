---
title: Skill Library
description: Browse all ClawBio bioinformatics skills
---

# Skill Library

ClawBio ships with **24+ skills** spanning pharmacogenomics, population genetics, single-cell biology, variant annotation, and more. Every skill includes demo data for instant testing.

## Production-Ready Skills

- **[PharmGx Reporter](/skills/pharmgx-reporter)** — Pharmacogenomics report from 23andMe/AncestryDNA/VCF data. CPIC guideline-backed drug-gene interactions.
- **[scRNA Orchestrator](/skills/scrna-orchestrator)** — End-to-end single-cell RNA-seq pipeline: QC, normalisation, clustering, marker genes, doublet removal.
- **[Equity Scorer (HEIM)](/skills/equity-scorer)** — Health Equity Impact Metric — measures genomic dataset diversity and population representation.
- **[NutriGx Advisor](/skills/nutrigx-advisor)** — Personalised nutrition report from genetic data. 40+ nutritionally-relevant SNPs.
- **[Genome Compare](/skills/genome-compare)** — Pairwise genome comparison with IBS scoring. Compare against George Church's genome.
- **[GWAS PRS](/skills/gwas-prs)** — Polygenic risk scores from consumer genetic data. 6 curated traits.
- **[GWAS Lookup](/skills/gwas-lookup)** — Federated variant query across 9 genomic databases.
- **[Illumina Bridge](/skills/illumina-bridge)** — Integration with Illumina Connected Analytics (ICA) platform.
- **[Galaxy Bridge](/skills/galaxy-bridge)** — Search, inspect, and run Galaxy tools from ClawBio.
- **[RNA-seq DE](/skills/rnaseq-de)** — Bulk and pseudo-bulk RNA-seq differential expression with PyDESeq2.

## Additional Skills

| Skill | Domain | Status |
|-------|--------|--------|
| Bio Orchestrator | Routing | Production |
| ClinPGx | Pharmacogenomics | Production |
| Profile Report | Multi-skill | Production |
| UKB Navigator | UK Biobank | Production |
| Ancestry PCA | Population genetics | SKILL.md only |
| Metagenomics | Microbiome | SKILL.md only |
| Semantic Similarity | Research gaps | SKILL.md only |
| VCF Annotator | Variant annotation | SKILL.md only |
| Lit Synthesizer | Literature | SKILL.md only |
| Struct Predictor | Protein structure | SKILL.md only |
| Repro Enforcer | Reproducibility | SKILL.md only |
| Seq Wrangler | Sequence QC | SKILL.md only |
| Labstep | Lab notebook | SKILL.md only |
| scRNA Embedding | Single-cell | Production |

## Run Any Demo

Every skill has demo data. Just add `--demo`:

```bash
python skills/pharmgx-reporter/pharmgx_reporter.py \
  --input skills/pharmgx-reporter/demo_patient.txt --output /tmp/demo

python skills/gwas-prs/gwas_prs.py --demo --output /tmp/demo
python skills/scrna-orchestrator/scrna_orchestrator.py --demo --output /tmp/demo
python skills/clinpgx/clinpgx.py --demo --output /tmp/demo
```
