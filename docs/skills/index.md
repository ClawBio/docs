---
title: Skill Library
description: Browse all ClawBio bioinformatics skills
---

# Skill Library

ClawBio ships with **24+ skills** spanning pharmacogenomics, population genetics, single-cell biology, variant annotation, and more. Every skill includes demo data for instant testing.

## Production-Ready Skills

<div class="section-cards">

<a class="section-card" href="pharmgx-reporter/">
  <div class="section-card__icon">💊</div>
  <h3 class="section-card__title">PharmGx Reporter</h3>
  <p class="section-card__desc">Pharmacogenomics report from 23andMe/AncestryDNA/VCF data. CPIC guideline-backed drug-gene interactions.</p>
</a>

<a class="section-card" href="scrna-orchestrator/">
  <div class="section-card__icon">🧬</div>
  <h3 class="section-card__title">scRNA Orchestrator</h3>
  <p class="section-card__desc">End-to-end single-cell RNA-seq pipeline: QC, normalisation, clustering, marker genes, doublet removal.</p>
</a>

<a class="section-card" href="equity-scorer/">
  <div class="section-card__icon">⚖️</div>
  <h3 class="section-card__title">Equity Scorer (HEIM)</h3>
  <p class="section-card__desc">Health Equity Impact Metric — measures genomic dataset diversity and population representation.</p>
</a>

<a class="section-card" href="nutrigx-advisor/">
  <div class="section-card__icon">🥗</div>
  <h3 class="section-card__title">NutriGx Advisor</h3>
  <p class="section-card__desc">Personalised nutrition report from genetic data. 40+ nutritionally-relevant SNPs.</p>
</a>

<a class="section-card" href="genome-compare/">
  <div class="section-card__icon">🔬</div>
  <h3 class="section-card__title">Genome Compare</h3>
  <p class="section-card__desc">Pairwise genome comparison with IBS scoring. Compare against George Church's genome.</p>
</a>

<a class="section-card" href="gwas-prs/">
  <div class="section-card__icon">📊</div>
  <h3 class="section-card__title">GWAS PRS</h3>
  <p class="section-card__desc">Polygenic risk scores from consumer genetic data. 6 curated traits.</p>
</a>

<a class="section-card" href="gwas-lookup/">
  <div class="section-card__icon">🔍</div>
  <h3 class="section-card__title">GWAS Lookup</h3>
  <p class="section-card__desc">Federated variant query across 9 genomic databases.</p>
</a>

<a class="section-card" href="illumina-bridge/">
  <div class="section-card__icon">🌉</div>
  <h3 class="section-card__title">Illumina Bridge</h3>
  <p class="section-card__desc">Integration with Illumina Connected Analytics (ICA) platform.</p>
</a>

<a class="section-card" href="galaxy-bridge/">
  <div class="section-card__icon">🌌</div>
  <h3 class="section-card__title">Galaxy Bridge</h3>
  <p class="section-card__desc">Search, inspect, and run Galaxy tools from ClawBio.</p>
</a>

<a class="section-card" href="rnaseq-de/">
  <div class="section-card__icon">📈</div>
  <h3 class="section-card__title">RNA-seq DE</h3>
  <p class="section-card__desc">Bulk and pseudo-bulk RNA-seq differential expression with PyDESeq2.</p>
</a>

</div>

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
python3 skills/pharmgx-reporter/pharmgx_reporter.py \
  --input skills/pharmgx-reporter/demo_patient.txt --output /tmp/demo

python3 skills/gwas-prs/gwas_prs.py --demo --output /tmp/demo
python3 skills/scrna-orchestrator/scrna_orchestrator.py --demo --output /tmp/demo
python3 skills/clinpgx/clinpgx.py --demo --output /tmp/demo
```
