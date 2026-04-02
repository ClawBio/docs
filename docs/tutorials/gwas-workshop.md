---
title: "GWAS Workshop"
description: Run a complete GWAS analysis with ClawBio in Google Colab. Variant lookup across 9 databases, polygenic risk scores, and SuSiE fine-mapping. No installation required.
---

# GWAS Workshop

<div class="tutorial-card__header">
  <span class="difficulty-badge difficulty-badge--intermediate">Intermediate</span>
  <span class="time-estimate">~30 min</span>
</div>

**No installation. No terminal. No API keys. No cost.** Everything runs in your browser via Google Colab. All you need is a Google account.

[:material-presentation-play: View slides](https://clawbio.ai/workshop-gwas-slides.html){ .md-button .md-button--primary }
[:material-open-in-new: Previous workshop: Variant Interpretation](variant-interpretation-workshop.md){ .md-button }

!!! tip "Runs in Google Colab"
    All code in this workshop runs in Google Colab. Open a new notebook, clone ClawBio (`!git clone https://github.com/ClawBio/ClawBio.git` then `%cd ClawBio` and `!pip install -q -r requirements.txt`), and follow along.

!!! tip "Follows on from the Variant Interpretation Workshop"
    This workshop picks up where the [Variant Interpretation Workshop](variant-interpretation-workshop.md) left off. In that session you annotated a single genome and found clinically relevant variants. Now we scale up to population-level analysis using GWAS summary statistics.

---

## Part 1: What is a GWAS?

### Association testing at scale

A genome-wide association study (GWAS) tests every common variant in the genome for statistical association with a trait or disease, across thousands or millions of participants. The output is a set of **summary statistics**: per-variant effect sizes, standard errors, and p-values.

| Field | Meaning | Example |
|-------|---------|---------|
| `rsid` | Variant identifier | rs7903146 |
| `beta` | Effect size (log-odds or per-allele) | 0.31 |
| `se` | Standard error of beta | 0.02 |
| `p` | P-value for association | 5.2 x 10^-38 |
| `MAF` | Minor allele frequency | 0.28 |

!!! info "Why summary statistics matter"
    Summary statistics are **public, free, and sufficient** to run polygenic risk scores, meta-analyses, and fine-mapping. No HPC infrastructure, no data access agreements, no individual-level data required. A researcher in Lima, Kampala, or Dhaka can run the same analyses as one at the Broad Institute.

### The ancestry gap

Over 86% of GWAS participants are of European ancestry. Effect sizes, allele frequencies, and linkage disequilibrium patterns differ between populations. Polygenic risk scores trained on European cohorts perform poorly in African and South Asian populations. This is not just a technical limitation; it risks widening health disparities.

ClawBio addresses this by querying **multiple biobanks** in a single call: UK Biobank (multi-ancestry), FinnGen (Finnish), and Biobank Japan (East Asian), alongside the GWAS Catalog and Open Targets.

---

## Part 2: Three ClawBio skills

This workshop uses three ClawBio skills that cover the full GWAS analysis workflow.

### Skill 1: GWAS Lookup

Give it an rsID. It queries **nine databases in parallel** and returns a unified report in seconds.

| Database | What it returns | Ancestry coverage |
|----------|----------------|-------------------|
| **GWAS Catalog** | Published trait associations | Mixed |
| **Open Targets** | Credible sets, locus-to-gene scores | Mixed |
| **UKB-TOPMed PheWeb** | PheWAS across 4,500 phenotypes | Multi-ancestry |
| **FinnGen r12** | Finnish disease endpoints | Finnish |
| **Biobank Japan** | East Asian PheWAS | Japanese |
| **GTEx v8** | eQTL tissue expression | Mostly European |
| **EBI eQTL Catalogue** | Multi-tissue eQTL associations | Mixed |
| **LocusZoom** | Regional association context | Both builds |
| **Ensembl** | Variant resolution, consequence | Reference |

```bash
python skills/gwas-lookup/gwas_lookup.py --rsid rs7903146 --output /tmp/gwas_demo
```

Or run the demo with pre-fetched data:

```bash
python skills/gwas-lookup/gwas_lookup.py --demo --output /tmp/gwas_demo
```

### Skill 2: Polygenic Risk Scores (PRS)

A PRS sums the effects of many variants into a single risk estimate:

**PRS = sum(dosage_i x effect_weight_i)** across all matched variants.

ClawBio ships with **6 curated scores** from the PGS Catalog for instant demos:

| Trait | PGS ID | Variants |
|-------|--------|----------|
| Type 2 diabetes | PGS000013 | 8 |
| Coronary artery disease | PGS000004 | 46 |
| Breast cancer | PGS000001 | 77 |
| Prostate cancer | PGS000057 | 147 |
| Atrial fibrillation | PGS000011 | 12 |
| BMI | PGS000039 | 97 |

Risk categories: **Low** (<20th percentile), **Average** (20-80th), **Elevated** (80-95th), **High** (>95th).

```bash
python skills/gwas-prs/gwas_prs.py --demo --output /tmp/prs_demo
```

### Skill 3: SuSiE Fine-Mapping

GWAS finds associated **regions**. Fine-mapping finds the **causal variants** within them.

A single GWAS signal can contain 10-200 correlated SNPs in high linkage disequilibrium. SuSiE (Sum of Single Effects) applies iterative Bayesian stepwise selection to produce:

- **Credible sets**: the minimal set of SNPs capturing 95% of causal probability
- **PIPs**: posterior inclusion probability per variant
- **Multiple signals**: handles multiple independent causal variants per locus

All from summary statistics alone. No individual-level data needed.

```bash
python skills/fine-mapping/fine_mapping.py --demo --output /tmp/finemapping_demo
```

---

## Part 3: How to run the workshop

### What you need

- A Google account (for Google Colab)
- A web browser
- Nothing else. No terminal, no installation, no API keys, no payment.

### Step-by-step guide

#### Step 1: Setup (2 minutes)

Install ClawBio in Colab. Same as the variant interpretation workshop: click play on the first two cells.

#### Step 2: GWAS Lookup (5 minutes)

Query rs7903146 (the strongest common Type 2 diabetes signal, in TCF7L2) across all nine databases. Examine the unified report: trait associations, PheWAS hits, eQTL data, and credible set membership.

Try additional variants:

| rsID | Gene | Trait | Why it matters |
|------|------|-------|----------------|
| rs7903146 | TCF7L2 | Type 2 diabetes | Strongest common T2D signal. OR 1.4 per allele. |
| rs429358 | APOE | Alzheimer's | You found this in the variant interpretation workshop. Now see the GWAS context. |
| rs3798220 | LPA | Cardiovascular | Lipoprotein(a), an independent risk factor for coronary events. |
| rs1801282 | PPARG | Type 2 diabetes | Drug target for thiazolidinediones (pioglitazone). |

#### Step 3: Cross-ancestry comparison (3 minutes)

Compare allele frequencies for your variant across UK Biobank, FinnGen, and Biobank Japan. Note how effect sizes and frequencies differ between populations.

#### Step 4: Polygenic Risk Scores (5 minutes)

Compute PRS for 6 traits using the Corpasome (Manuel Corpas's 23andMe data). The tool matches genotyped variants to published PGS Catalog scoring files and estimates percentile rank against reference populations.

#### Step 5: Fine-Mapping (5 minutes)

Run SuSiE on a demo locus containing 200 variants with 2 independent causal signals. Examine the credible sets, PIPs, and the locus plot showing which variants are most likely causal.

---

## Take-home messages

1. **GWAS summary statistics are free and public.** You do not need individual-level data to do meaningful population-level research.
2. **Three ClawBio skills cover the full workflow**: lookup, PRS, and fine-mapping.
3. **Cross-ancestry analysis is not optional.** Most GWAS are European-biased. Always query multiple biobanks to check transferability.
4. **Fine-mapping narrows GWAS hits to causal variants.** SuSiE credible sets are the current state of the art.
5. **Infrastructure is no longer a barrier.** Google Colab + ClawBio = publication-quality GWAS analysis, for free, anywhere in the world.

---

## Resources

| Resource | Link |
|----------|------|
| GWAS workshop slides | [clawbio.ai/workshop-gwas-slides.html](https://clawbio.ai/workshop-gwas-slides.html) |
| Variant Interpretation Workshop | [Previous workshop](variant-interpretation-workshop.md) |
| ClawBio GitHub | [github.com/ClawBio/ClawBio](https://github.com/ClawBio/ClawBio) |
| GWAS Catalog | [ebi.ac.uk/gwas](https://www.ebi.ac.uk/gwas/) |
| PGS Catalog | [pgscatalog.org](https://www.pgscatalog.org) |
| Open Targets Genetics | [genetics.opentargets.org](https://genetics.opentargets.org) |
| Corpasome dataset (Zenodo) | [doi:10.5281/zenodo.19297389](https://doi.org/10.5281/zenodo.19297389) |
| Ensembl VEP | [ensembl.org/vep](https://ensembl.org/vep) |
| gnomAD | [gnomad.broadinstitute.org](https://gnomad.broadinstitute.org) |
| CPIC Guidelines | [cpicpgx.org](https://cpicpgx.org) |
