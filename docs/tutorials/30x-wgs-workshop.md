---
title: "30x Whole-Genome Sequencing Workshop"
description: Explore a real 30x whole-genome sequence with ClawBio in Google Colab. Structural variants, QC metrics, pharmacogenomics. No installation required.
---

# 30x Whole-Genome Sequencing Workshop

<div class="tutorial-card__header">
  <span class="difficulty-badge difficulty-badge--intermediate">Intermediate</span>
  <span class="time-estimate">~40 min</span>
</div>

**No installation. No terminal. No API keys. No cost.** Everything runs in your browser via Google Colab. All you need is a Google account.

[:material-open-in-new: Launch the workshop in Google Colab](https://colab.research.google.com/github/ClawBio/ClawBio/blob/main/docs/workshop-30x-wgs.ipynb){ .md-button .md-button--primary }
[:material-presentation-play: View introductory slides](https://clawbio.ai/workshop-30x-wgs.html){ .md-button }

!!! warning "Early release: testers welcome"
    This workshop has not been fully tested end-to-end. If you hit errors, please [file an issue on GitHub](https://github.com/ClawBio/ClawBio/issues) or message Manuel directly. Your feedback makes this better for everyone.

---

## Part 1: What is this dataset?

### A real genome, fully open

In 2013, Manuel Corpas published his 23andMe genotype data under CC0, creating one of the first fully open personal genomes (the Corpasome). In 2026, he published the full 30x whole-genome sequence from Dante Labs, also under CC0.

This workshop uses that 30x WGS dataset. It is hosted on Zenodo and citable:

> Corpas, M. (2026). Personal Whole Genome Sequencing Variant Calls (SNPs, Indels, SVs, CNVs) of Manuel Corpas from Dante Labs 30x WGS. Zenodo. [doi:10.5281/zenodo.19297389](https://doi.org/10.5281/zenodo.19297389)

!!! danger "Research and education only"
    This dataset is provided for research and educational purposes only. It must not be used for clinical decision-making. ClawBio is not a medical device.

!!! info "Ethics approval"
    Use of this personal genome data for research was approved by the UNIR Research Ethics Committee (Comite de Etica de la Investigacion) on 28 January 2021, under protocol **PI:029/2020** ("Healthy Genome Project"), with Manuel Corpas as principal investigator.

### What WGS captures that SNP arrays miss

Consumer genotyping platforms (23andMe, AncestryDNA) test around 600,000 pre-selected positions using a SNP array. Whole-genome sequencing reads every base. The difference is significant:

|  | SNP Array (~600K) | 30x WGS |
|--|-------------------|---------|
| **SNPs** | ~600,000 | 3,716,648 |
| **Indels** | 0 | 912,009 |
| **Structural variants** | 0 | 8,925 |
| **Copy number variants** | 0 | 1,387 |
| **Gene coverage** | Sparse (pre-selected positions) | Complete (every base) |
| **Ti/Tv ratio** | N/A | 2.03 |
| **Het/Hom ratio** | N/A | 1.63 |

SNP arrays answer pre-defined questions. WGS lets you ask questions you did not know to ask.

### Pre-built subsets for instant analysis

ClawBio ships lightweight VCF subsets extracted from the full genome, committed to the repository so you do not need to download the full 224 MB dataset:

| Subset | What it contains | Purpose |
|--------|-----------------|---------|
| **chr20 SNPs + indels** | Chromosome 20 variants | Tutorial exploration |
| **PGx loci** | 5 pharmacogenomic variant calls | WGS vs chip comparison |
| **NutriGx loci** | 11 nutrigenomics variant calls | Dietary genetics |
| **SV calls** | 8,925 structural variants | SV exploration |
| **CNV calls** | 1,387 copy number variants | CNV exploration |

---

## Part 2: Background you need for this workshop

You do not need to memorise this before starting. Read through it once so the terms are familiar, then refer back as needed.

### QC metrics: how to tell if a genome is good

When you receive whole-genome sequencing data, the first thing you check is quality. Three metrics matter most:

| Metric | Expected range | This genome | What it tells you |
|--------|---------------|-------------|-------------------|
| **Ti/Tv ratio** | ~2.0 for WGS | 2.03 | Ratio of transitions (A/G, C/T) to transversions (all other changes). Values well below 2.0 suggest sequencing errors or contamination. |
| **Het/Hom ratio** | 1.5 to 1.7 | 1.63 | Ratio of heterozygous to homozygous alternate calls. Values outside this range may indicate sample contamination or consanguinity. |
| **Variant count** | 3.5M to 4.5M SNPs | 3,716,648 | Total number of SNP calls. Significantly fewer suggests low coverage; significantly more suggests contamination or a calling error. |

!!! tip "Why is Ti/Tv expected to be ~2.0?"
    Transitions (purine to purine, or pyrimidine to pyrimidine) are chemically more likely than transversions (purine to pyrimidine or vice versa) due to the molecular structure of the bases. A random collection of errors would give Ti/Tv ~0.5, so a value near 2.0 confirms that most calls are real biological variants.

### Structural variants: the hidden layer

Structural variants (SVs) are genomic rearrangements larger than 50 base pairs. They are invisible to SNP arrays but captured by WGS.

| Type | Full name | What happens | Count in this genome |
|------|-----------|-------------|---------------------|
| **DEL** | Deletion | A segment of DNA is missing | 5,854 |
| **BND** | Breakend | A translocation or complex rearrangement joins distant genomic positions | 1,413 |
| **DUP** | Duplication | A segment is copied (can alter gene dosage) | 778 |
| **INV** | Inversion | A segment is flipped in orientation | 673 |
| **INS** | Insertion | New DNA is inserted (often mobile elements like Alu or LINE) | 207 |

SVs are estimated to cause around 20% of rare genetic disease, but they remain underexplored because older technologies could not detect them reliably.

### From SNP chip to WGS: what changes clinically

WGS does not just find "more of the same." It finds qualitatively different types of variation:

- **CYP2D6 gene deletions and duplications**: The most important pharmacogene has common structural variants that change metaboliser status entirely. SNP chips cannot detect these.
- **HLA typing**: The immune system's HLA genes are too complex and variable for array-based genotyping. WGS captures the full haplotype.
- **Coding indels**: Insertions and deletions in protein-coding regions can cause frameshifts. Arrays test only SNPs.
- **Novel variants**: Arrays can only report positions they were designed to test. WGS discovers variants never seen before.

### The Corpasome: 13 years of open genomics

| Year | Event |
|------|-------|
| 2013 | Manuel Corpas publishes his 23andMe data under CC0 (one of the first open personal genomes) |
| 2013 | "Crowdsourcing the Corpasome" paper in Source Code for Biology and Medicine |
| 2026 | 30x whole-genome sequence published on Zenodo under CC0 |
| 2026 | Integrated into ClawBio as the default reference genome for demos, tutorials, and CI |

---

## Part 3: How to run the workshop

### What you need

- A **Google account** (any free Gmail account works)
- A **web browser** (Chrome, Firefox, or Safari)
- That is it. No software to install, no API keys, no payment.

### Prerequisite

This workshop assumes basic familiarity with genomic concepts (what a variant is, what a VCF file contains). If you are new to genomics, start with the [Variant Interpretation Workshop](variant-interpretation-workshop.md) first.

### Opening the notebook

Click the button below to open the workshop notebook in Google Colab:

[:material-open-in-new: Launch in Google Colab](https://colab.research.google.com/github/ClawBio/ClawBio/blob/main/docs/workshop-30x-wgs.ipynb){ .md-button .md-button--primary }

When it opens, click the **play button** on each code cell in order, from top to bottom.

!!! tip "First time using Google Colab?"
    Google Colab is a free service that lets you run Python code in your browser. You do not need to know Python. Just click the play button on each code cell and read the output. If Colab asks you to "connect to a runtime", click **Connect** in the top right corner.

### Step-by-step guide

#### Step 0: Setup (2 minutes)

Run the first two code cells. They clone ClawBio and install dependencies. You should see:

```
ClawBio loaded successfully
Skills available: 39
WGS subsets available: 5
```

!!! tip "If something goes wrong"
    Click **Runtime > Restart and run all** in the Colab menu bar. This resets everything and runs all cells from the beginning.

#### Step 1: Explore the genome (5 minutes)

The notebook loads pre-computed QC baselines from the full 30x genome and displays summary statistics:

- **3,716,648** SNPs across all chromosomes
- **912,009** indels
- **Ti/Tv ratio: 2.03** (excellent quality)
- **Het/Hom ratio: 1.63** (normal for an outbred individual)
- **8,925** structural variants broken down by type
- **1,387** copy number variants

Then it loads the chr20 subset and shows the VCF format: CHROM, POS, ID, REF, ALT, QUAL, FILTER.

#### Step 2: Explore structural variants (8 minutes)

The notebook loads all 8,925 structural variants and computes:

- Count by type (DEL, DUP, INV, INS, BND)
- Size distribution (from 50 bp to megabases)
- The largest and smallest SVs

This is the section that distinguishes WGS from SNP arrays. None of these variants would be visible on a genotyping chip.

#### Step 3: Pharmacogenomic variants from WGS (5 minutes)

The notebook loads PGx variants from both the WGS and the 23andMe data and compares them side by side. The key insight: the SNP chip reports genotypes at 21 pre-selected positions (including reference-homozygous calls). WGS only outputs positions where the individual differs from reference. Positions with no WGS variant call are homozygous reference, which is itself informative.

#### Step 4: Annotate chr20 variants (5 minutes)

The notebook extracts 20 PASS variants from chromosome 20 and runs ClawBio's variant-annotation skill. This calls the Ensembl VEP REST API (free, public, no API key needed) and returns gene names, consequence types, ClinVar classifications, and gnomAD population frequencies.

!!! info "No API key needed"
    The Ensembl VEP REST API is free and public. ClawBio handles all the formatting and submission automatically.

#### Step 5: Exercises (15 minutes, independent work)

| Exercise | What to do | Required? |
|----------|-----------|-----------|
| **5a** | Compare WGS and SNP chip findings at pharmacogenomic loci. Why does the chip report more "variants" than the WGS? Which platform gives you more confidence? | Yes |
| **5b** | Find the largest deletion in the SV calls. What chromosome is it on? Does it overlap any known genes? (Use the [UCSC Genome Browser](https://genome.ucsc.edu) with the GRCh37/hg19 assembly.) | Yes |
| **5c** | How many chr20 variants have no rsID (ID column is ".")? What does a missing rsID mean? If you found a novel missense variant in a disease gene, what steps would you take to determine if it is pathogenic? | Yes |

---

## Part 4: Understanding your results

### QC interpretation

| Metric | Your value | Verdict |
|--------|-----------|---------|
| Ti/Tv ratio | 2.03 | Within expected range (1.9 to 2.2). No evidence of systematic errors. |
| Het/Hom ratio | 1.63 | Normal for a single outbred individual (expected 1.5 to 1.7). |
| Total SNPs | 3,716,648 | Within expected range for a European genome at 30x (3.5M to 4.5M). |
| Total indels | 912,009 | Consistent with WGS calling standards. |

### Structural variant breakdown

| SV type | Count | What to look for |
|---------|-------|-----------------|
| DEL | 5,854 | Large deletions overlapping coding genes. CYP2D6 whole-gene deletions change metaboliser phenotype. |
| BND | 1,413 | Breakends at or near gene boundaries may indicate translocations. |
| DUP | 778 | Gene duplications can increase expression (e.g., CYP2D6 ultrarapid metabolisers carry extra copies). |
| INV | 673 | Inversions at gene breakpoints can disrupt function. |
| INS | 207 | Mobile element insertions (Alu, LINE) are usually benign but can disrupt regulatory regions. |

### What WGS found that the SNP chip missed

!!! success "Key insight"
    The 23andMe chip tested 21 pharmacogenomic positions and found genotypes at all of them (including reference-homozygous calls). The WGS found 5 variant calls at those same positions: the others are homozygous reference. Both platforms agree on the result, but WGS also captures the surrounding genomic context: nearby indels, structural variants, and novel SNPs that the chip was not designed to test.

    In clinical practice, this matters most for genes like CYP2D6, where whole-gene deletions and duplications (detectable by WGS, invisible to arrays) can completely change a patient's metaboliser status and drug response.

---

## Take-home messages

1. **WGS is the gold standard for variant discovery.** It captures SNPs, indels, structural variants, and copy number variants in a single assay. Arrays test only what they were designed for.

2. **Structural variants are clinically significant but underexplored.** They account for an estimated 20% of rare disease, yet most diagnostic pipelines still focus on SNPs and small indels.

3. **QC metrics are your first line of defence.** Ti/Tv, Het/Hom, and total variant count tell you immediately whether the data is trustworthy. Always check before interpreting.

4. **The same genome tells different stories at different resolution.** The Corpasome at 600K positions (SNP chip) and at 30x coverage (WGS) reveal overlapping but complementary biology. The chip is faster and cheaper; the WGS is deeper and more complete.

5. **Open data accelerates science.** This entire workshop runs on a CC0-licensed genome, open-source tools, and free public APIs. Anyone in the world can reproduce it.

6. **Agent-driven analysis makes WGS accessible.** ClawBio reduces a multi-tool, multi-day annotation pipeline to a single command with a structured, reproducible output.

!!! danger "Medical disclaimer"
    ClawBio is a research and educational tool. It is not a medical device and does not provide clinical diagnoses. The findings discussed in this workshop are for educational purposes only. Consult a healthcare professional before making any medical decisions based on genetic data.

---

## Resources

| Resource | Link |
|----------|------|
| Google Colab notebook | [:material-open-in-new: Open](https://colab.research.google.com/github/ClawBio/ClawBio/blob/main/docs/workshop-30x-wgs.ipynb) |
| Zenodo dataset | [doi:10.5281/zenodo.19297389](https://doi.org/10.5281/zenodo.19297389) |
| ClawBio GitHub | [github.com/ClawBio/ClawBio](https://github.com/ClawBio/ClawBio) |
| Variant Interpretation Workshop | [Previous workshop](variant-interpretation-workshop.md) |
| Corpasome paper | [doi:10.1186/1751-0473-8-13](https://doi.org/10.1186/1751-0473-8-13) |
| Ensembl VEP | [ensembl.org/vep](https://www.ensembl.org/info/docs/tools/vep/index.html) |
| ClinVar | [ncbi.nlm.nih.gov/clinvar](https://www.ncbi.nlm.nih.gov/clinvar/) |
| gnomAD | [gnomad.broadinstitute.org](https://gnomad.broadinstitute.org/) |
| UCSC Genome Browser | [genome.ucsc.edu](https://genome.ucsc.edu) |
| CPIC Guidelines | [cpicpgx.org](https://cpicpgx.org/) |
