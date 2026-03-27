---
title: "Variant Interpretation Workshop"
description: Annotate a real human genome with ClawBio in Google Colab. Covers variant annotation, pharmacogenomics, ACMG classification, and equity in genomics.
---

# Variant Interpretation Workshop

<div class="tutorial-card__header">
  <span class="difficulty-badge difficulty-badge--beginner">Beginner</span>
  <span class="time-estimate">~60 min</span>
</div>

Hands-on workshop: annotate a real human genome, interpret pharmacogenomic findings, and understand what AI changes (and does not change) about genomic analysis. Everything runs in Google Colab. No installation required.

[:material-open-in-new: Open in Google Colab](https://colab.research.google.com/github/ClawBio/ClawBio/blob/main/docs/tutorial-variant-interpretation.ipynb){ .md-button .md-button--primary }
[:material-file-presentation-box: Full workshop page](https://clawbio.ai/workshop-variant-interpretation.html){ .md-button }

---

## What is ClawBio?

ClawBio is the first bioinformatics-native AI agent skill library. It provides curated, reproducible, open-source skills that any AI agent can call. Each skill handles a specific task: annotating variants, scoring pharmacogenomic risk, running differential expression, searching clinical trials, and more.

**Three principles:**

- **Local-first**: your genomic data never leaves your machine. Skills process everything in-place.
- **Reproducible**: every skill exports `commands.sh`, `environment.yml`, and SHA-256 checksums.
- **Grounded, not hallucinated**: all gene-drug mappings trace to published CPIC guidelines and ClinVar assertions. The AI agent routes to the right skill; the skill does the grounded analysis.

### The problem ClawBio addresses

| Problem | Impact |
|---------|--------|
| Reproducing published bioinformatics is broken | Dependency hell, dead links, hardcoded paths |
| AI hallucinates biology | Invented star alleles, fabricated gene-drug associations |
| Manual pipelines take weeks | VEP, ClinVar, gnomAD, CPIC each require separate tools |
| Equity gaps persist | 86% of GWAS participants are European; PRS loses up to 80% accuracy in other populations |

ClawBio solves this by packaging each analysis as a self-contained skill with pinned dependencies, demo data, and reproducibility metadata.

### Community and growth

| Metric | Value |
|--------|-------|
| GitHub stars | 488 |
| Forks | 85 |
| Skills | 39 |
| Contributors | 13 |

**Milestones:**

- **v0.4** (Mar 2026): Galaxy integration, 8,000+ tools via BioBlend SDK
- **v0.3.1** (Mar 2026): Agent-friendly (`llms.txt`, `AGENTS.md`, `catalog.json`)
- **v0.3** (Mar 2026): Imperial College AI Agent Hackathon, security audit (32 fixes)
- **v0.2** (Feb 2026): 57 automated tests, GitHub Actions CI, ClawHub registry
- **v0.1** (Jan 2026): First public release with core skills

---

## Background: variant interpretation

### Genomic variation

Every human genome carries 4 to 5 million single nucleotide polymorphisms (SNPs) compared to the reference. Most are benign. A small fraction affect protein function, drug metabolism, or disease risk. Beyond SNPs, variation includes insertions/deletions (indels), copy number variants (CNVs), and structural rearrangements. This workshop focuses on SNPs and small indels because they are what consumer genotyping platforms measure.

### The ACMG five-tier classification

The American College of Medical Genetics and Genomics (ACMG) defines five categories:

| Category | Meaning | Action |
|----------|---------|--------|
| **Pathogenic** | Directly contributes to disease | Report. Genetic counselling. |
| **Likely pathogenic** | Strong evidence, not conclusive | Report with caveat. |
| **VUS** | Uncertain significance | Do not act on. May be reclassified. |
| **Likely benign** | Probably no clinical effect | Generally not reported. |
| **Benign** | No disease association | Not reported. |

!!! warning "VUS is the honest answer"
    Over half of all variants in ClinVar are VUS. The backlog grows faster than reclassification efforts. Learning to communicate uncertainty is a core clinical skill.

### The annotation pipeline

A standard variant interpretation workflow:

```
VCF --> VEP --> ClinVar --> gnomAD --> ACMG --> Report
```

- **VCF**: Variant Call Format, the standard file for genomic variants
- **VEP**: Ensembl Variant Effect Predictor, determines functional consequence
- **ClinVar**: NCBI database of variant-disease associations
- **gnomAD**: Genome Aggregation Database, population allele frequencies (76,000+ genomes)
- **ACMG**: Classification framework combining all evidence into a verdict

### Pharmacogenomics

Pharmacogenomics (PGx) studies how genetic variation affects drug response:

| Gene | Drugs affected | Clinical consequence |
|------|---------------|---------------------|
| **CYP2D6** | Codeine, tamoxifen, SSRIs (51 drugs) | Poor metabolisers get no pain relief from codeine |
| **CYP2C19** | Clopidogrel, PPIs | Poor metabolisers: clopidogrel does not work |
| **CYP2C9 + VKORC1** | Warfarin | Wrong dose causes dangerous bleeding or clotting |
| **TPMT** | Azathioprine, 6-MP | Poor metabolisers: severe bone marrow toxicity |
| **DPYD** | 5-fluorouracil, capecitabine | Deficiency can be fatal at standard chemo doses |

[CPIC](https://cpicpgx.org/) publishes evidence-based guidelines mapping genotype to drug recommendation. ClawBio's `pharmgx-reporter` skill implements these directly.

### The equity problem

Genomic databases are heavily biased toward European populations:

- **86%** of GWAS participants are of European ancestry
- BRCA variant databases have **30x more** entries for European populations
- Polygenic risk scores lose up to **80% accuracy** in non-European populations
- AI trained on biased data amplifies existing disparities

A variant classified as "benign" in European databases may be pathogenic in another population but simply unstudied.

### The Corpasome

In 2013, Manuel Corpas published his 23andMe genotype data under CC0 (public domain), making it one of the first fully open personal genomes. This workshop uses the Corpasome as its primary dataset.

Real findings from this genome include Factor V Leiden (thrombophilia carrier), HFE C282Y (haemochromatosis carrier), CFTR deltaF508 (cystic fibrosis carrier), VKORC1 + CYP2C9 (warfarin AVOID), MTHFR C677T (folate metabolism), and APOE e3/e4 (Alzheimer's risk factor).

> Corpas, M. (2013). Crowdsourcing the Corpasome. *Source Code for Biology and Medicine*, **8**, 13. [doi:10.1186/1751-0473-8-13](https://doi.org/10.1186/1751-0473-8-13)

---

## Workshop materials

### Essential links

| Resource | Link | Notes |
|----------|------|-------|
| **Google Colab notebook** | [Open in Colab](https://colab.research.google.com/github/ClawBio/ClawBio/blob/main/docs/tutorial-variant-interpretation.ipynb) | Main practical. Free tier. |
| **Full workshop page** | [clawbio.ai/workshop](https://clawbio.ai/workshop-variant-interpretation.html) | Slides, background, results guide |
| **ClawBio GitHub** | [github.com/ClawBio/ClawBio](https://github.com/ClawBio/ClawBio) | Source code, skills, documentation |
| **Corpasome paper** | [doi:10.1186/1751-0473-8-13](https://doi.org/10.1186/1751-0473-8-13) | Corpas (2013), Source Code Biol Med |
| **Ensembl VEP** | [ensembl.org/vep](https://www.ensembl.org/info/docs/tools/vep/index.html) | Variant Effect Predictor (free REST API) |
| **ClinVar** | [ncbi.nlm.nih.gov/clinvar](https://www.ncbi.nlm.nih.gov/clinvar/) | Variant-disease associations |
| **gnomAD** | [gnomad.broadinstitute.org](https://gnomad.broadinstitute.org/) | Population allele frequencies |
| **CPIC** | [cpicpgx.org](https://cpicpgx.org/) | Pharmacogenomics guidelines |
| **ACMG Standards** | [Richards et al. (2015)](https://doi.org/10.1038/gim.2015.30) | Genetics in Medicine 17(5):405-24 |

### Skills used

- **variant-annotation**: Annotates VCF variants via Ensembl VEP REST. ClinVar significance, gnomAD frequencies, Tier 1-4 priority.
- **pharmgx-reporter**: PGx report from 23andMe/AncestryDNA. 12 genes, 31 SNPs, 51 drugs. CPIC-grounded, zero external dependencies.
- **clinpgx**: Deep gene-drug lookup via ClinPGx API. CPIC guideline context, PharmGKB, FDA labels.

### Requirements

- A Google account (for Colab)
- A web browser
- No installation, no API keys, no payment
- Approximately 60 minutes

---

## Step-by-step walkthrough

### Step 0: Setup (2 min)

Run the first two code cells to clone ClawBio and install dependencies (`pysam`, `requests`, `pandas`, `matplotlib`).

```
ClawBio loaded successfully
Skills available: 39
```

!!! tip "If Colab is slow"
    The git clone takes 10-20 seconds. If it times out, click **Runtime > Restart and run all**.

### Step 1: Explore the Corpasome (5 min)

The notebook loads Manuel Corpas's 23andMe file (~600,000 SNPs). You will see:

- The 23andMe format: rsID, chromosome, position, genotype
- Total SNP count
- Per-chromosome breakdown (Chr 1 largest, Chr 22 smallest)

**Discussion**: Why does chromosome 1 have the most SNPs? (It is the largest chromosome, ~249 Mb.)

### Step 2: Convert to VCF (3 min)

The notebook extracts 21 clinically relevant variants and converts them to VCF:

- **Pharmacogenomics**: CYP2C19, CYP2C9, CYP2D6, VKORC1, TPMT, MTHFR
- **Cancer risk**: BRCA1, TP53
- **Cardiovascular**: Factor V (F5), Prothrombin (F2), HFE
- **Mendelian**: CFTR, APOE, SERPINA1

### Step 3: Run variant annotation (5 min)

The `variant-annotation` skill sends 21 variants to Ensembl VEP and enriches them with ClinVar and gnomAD. Output:

- `report.md` with a prioritised summary
- `annotated_variants.tsv` with per-variant details
- `result.json` for programmatic access

!!! info "VEP API"
    The 21 variants are submitted in a single batch (under the 200-variant limit). If the API is slow, the skill retries automatically.

### Step 4: Pharmacogenomic interpretation (5 min)

The `clinpgx` skill maps variants to CPIC drug recommendations. The warfarin finding is the highlight: VKORC1 TT (high sensitivity) + CYP2C9 *1/*2 (intermediate metaboliser) = **AVOID standard dose**.

### Step 5: Exercises (15 min)

| Exercise | Task | Status |
|----------|------|--------|
| **5a** | Run variant-annotation on the bundled 20-variant synthetic panel (`--demo`). Compare with Corpasome results. | Required |
| **5b** | Upload your own 23andMe/AncestryDNA file and re-run Steps 2-4. Privacy: data stays in Colab, deleted on session end. | Optional |
| **5c** | Pick one gene. Research function, ACMG classification, gnomAD frequency. Would you report this to a patient? | Required |

---

## Understanding your results

### Priority tiers

| Tier | Criteria | Corpasome example |
|------|----------|-------------------|
| **Tier 1** | Pathogenic/likely pathogenic in ClinVar. Rare (AF < 0.001). | CFTR deltaF508, cystic fibrosis carrier |
| **Tier 2** | Drug response or established risk factor. CPIC-actionable. | VKORC1 rs9923231 TT, warfarin sensitivity |
| **Tier 3** | Variant of uncertain significance. | Rare missense, no ClinVar entry |
| **Tier 4** | Benign/likely benign. Common (> 1%). | MTHFR A1298C, common polymorphism |

### Key findings from the Corpasome

#### Factor V Leiden (rs6025) -- Tier 1

**Gene:** F5 (coagulation factor V). **Genotype:** heterozygous carrier.

3-8x increased risk of venous thromboembolism. The most common inherited thrombophilia in Europeans (~5% carrier frequency). Relevant for oral contraceptive prescribing, surgery planning, and long-haul travel. Reportable finding; cascade testing recommended.

#### HFE C282Y (rs1800562) -- Tier 1

**Gene:** HFE (homeostatic iron regulator). **Genotype:** heterozygous carrier.

Carrier for hereditary haemochromatosis. Homozygotes accumulate excess iron causing liver damage, diabetes, and heart failure. Heterozygous carriers have mildly elevated iron but rarely develop clinical disease. Monitor serum ferritin periodically.

#### CFTR deltaF508 (rs113993960) -- Tier 1

**Gene:** CFTR (cystic fibrosis transmembrane conductance regulator). **Genotype:** heterozygous carrier.

Carrier for cystic fibrosis, the most common lethal autosomal recessive condition in Europeans (~1 in 25 carrier frequency). Two copies needed for disease. Partner testing recommended before family planning.

#### Warfarin: CYP2C9 + VKORC1 -- Tier 2

**Genes:** CYP2C9 (*1/*2, intermediate metaboliser) + VKORC1 (rs9923231 TT, high sensitivity).

This combination means warfarin is metabolised more slowly AND the drug target is more sensitive. Standard dosing would cause dangerously high drug levels and serious bleeding risk.

!!! danger "CPIC recommendation"
    **AVOID standard dose.** Use pharmacogenomic-guided dosing or consider alternative anticoagulants (DOACs). Warfarin has a narrow therapeutic window: too little means clotting, too much means haemorrhage.

#### APOE e3/e4 (rs429358 + rs7412) -- Risk factor

**Gene:** APOE (apolipoprotein E). **Genotype:** e3/e4.

The e4 allele is the strongest common genetic risk factor for late-onset Alzheimer's (~3x risk with one copy). Many e4 carriers never develop Alzheimer's. APOE status is an ACMG secondary finding (SF v3.2). Disclosure recommended but must be accompanied by counselling. Probabilistic, not deterministic.

#### MTHFR C677T (rs1801133) -- Tier 2

**Gene:** MTHFR (methylenetetrahydrofolate reductase). **Genotype:** heterozygous.

Reduced enzyme activity for folate metabolism. Heterozygotes retain ~65% activity (not clinically significant for most). Homozygotes (~35% activity) may benefit from methylfolate supplementation during pregnancy. Extremely common (~30-40% carrier frequency in Europeans). Frequently over-interpreted in direct-to-consumer reports.

### Reading the annotated variants table

| Column | Meaning |
|--------|---------|
| `gene` | Gene symbol (e.g., CYP2D6, CFTR) |
| `consequence` | Functional effect: missense_variant, synonymous, frameshift, etc. |
| `impact` | VEP tier: HIGH, MODERATE, LOW, MODIFIER |
| `clinvar_significance` | ClinVar classification: Pathogenic, Likely pathogenic, VUS, Benign, Drug response |
| `gnomad_af` | Global allele frequency. Below 0.001 (0.1%) = rare. |
| `priority_tier` | ClawBio tier (1-4) combining all evidence |
| `priority_score` | Numeric rank within a tier. Higher = more clinically relevant. |

!!! warning "Limitations"
    Consumer genotyping arrays test ~600,000 of ~3 billion positions. They miss structural variants, most rare variants, and copy number changes. A "clear" result does not mean the genome is free of pathogenic variants. Clinical-grade whole genome sequencing covers far more.

---

## Take-home messages

1. **The fundamentals have not changed.** Variant interpretation still requires molecular biology, population genetics, clinical context, and the ACMG framework. AI accelerates the mechanical steps, not the judgement.

2. **Speed has changed dramatically.** What took days (tools, environments, VEP, parsing, cross-referencing) now takes minutes. The bottleneck shifts from data processing to interpretation.

3. **Pharmacogenomics is actionable today.** Drug-gene interactions like warfarin/CYP2C9/VKORC1 are well-established, guideline-supported, and directly affect prescribing. This is not hypothetical.

4. **VUS is the honest answer.** Over half of ClinVar variants are VUS. The backlog grows faster than reclassification. Communicating uncertainty is a core skill.

5. **Equity gaps are real and growing.** AI trained on biased data amplifies disparities. Every analysis should consider the ancestry context of the individual and the reference databases.

6. **Open data enables open science.** This entire workshop runs on a CC0-licensed genome, open-source skills, free APIs, and a free notebook. Anyone can reproduce the same results. That is the standard.

!!! danger "Medical disclaimer"
    ClawBio is a research and educational tool. It is not a medical device and does not provide clinical diagnoses. Consult a healthcare professional before making any medical decisions based on genetic data.

---

## Further reading

- [ACMG Standards: Richards et al. (2015)](https://doi.org/10.1038/gim.2015.30)
- [CPIC Guidelines](https://cpicpgx.org/)
- [Ensembl VEP documentation](https://www.ensembl.org/info/docs/tools/vep/index.html)
- [gnomAD browser](https://gnomad.broadinstitute.org/)
- [ClinVar database](https://www.ncbi.nlm.nih.gov/clinvar/)
- [Corpas (2013) Crowdsourcing the Corpasome](https://doi.org/10.1186/1751-0473-8-13)
