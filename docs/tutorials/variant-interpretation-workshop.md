---
title: "Variant Interpretation Workshop"
description: Annotate a real human genome with ClawBio in Google Colab. No installation, no terminal, no prior experience required.
---

# Variant Interpretation Workshop

<div class="tutorial-card__header">
  <span class="difficulty-badge difficulty-badge--beginner">Beginner</span>
  <span class="time-estimate">~60 min</span>
</div>

**No installation. No terminal. No prior experience required.** Everything runs in your browser via Google Colab. All you need is a Google account.

[:material-open-in-new: Launch the workshop in Google Colab](https://colab.research.google.com/github/ClawBio/ClawBio/blob/main/docs/tutorial-variant-interpretation.ipynb){ .md-button .md-button--primary }

---

## Part 1: What is ClawBio?

### The short version

ClawBio is an open-source toolkit that uses AI to automate genomic analysis. You give it genetic data, it runs the analysis, and you get a structured report. No bioinformatics experience needed to get started.

### The problem it solves

Interpreting a person's genome today involves a chain of manual steps: downloading specialist software, configuring databases, submitting queries to web APIs, parsing raw output files, and cross-referencing results across multiple sources. Each step requires a different tool, different expertise, and different file formats. A single analysis can take hours or days.

Meanwhile, AI language models (like ChatGPT or Claude) can answer genomics questions, but they frequently make things up. They invent gene-drug associations that do not exist, cite retracted papers, and produce star-allele calls with no basis in evidence. In clinical genomics, hallucinated results are dangerous.

ClawBio bridges that gap:

| Problem | How ClawBio solves it |
|---------|----------------------|
| Manual pipelines are slow and error-prone | Each analysis is packaged as a one-click "skill" with built-in demo data |
| AI hallucinates biology | Every skill is grounded in published databases (ClinVar, CPIC, gnomAD), not language model guesses |
| Reproducibility is broken | Every run produces a reproducibility bundle (exact commands, checksums, versions) |
| Genetic data is sensitive | All processing happens on your machine (or your Colab session). Nothing is uploaded to ClawBio servers. |

### Who uses it

ClawBio is used by students, researchers, and bioinformaticians. It is open-source (MIT licence), free, and has a growing community:

| | |
|---|---|
| **GitHub stars** | 488 |
| **Forks** | 85 |
| **Available skills** | 39 (variant annotation, pharmacogenomics, GWAS, single-cell RNA-seq, equity scoring, and more) |
| **Contributors** | 13 |

The project launched in January 2026 and has been used at hackathons (Imperial College, DoraHacks), university courses (Westminster, UCL), and research labs.

---

## Part 2: Background you need for this workshop

You do not need to memorise any of this before starting the practical. Read through it once so the terms are familiar, then refer back as you work through the notebook.

### What is genomic variation?

Every person's DNA differs from the "reference genome" at about 4 to 5 million positions. These differences are called variants. The most common type is a single nucleotide polymorphism (SNP): one DNA letter changed to another (e.g., A to G at a specific position).

Most variants have no effect on health. A small number affect how proteins work, how drugs are metabolised, or whether someone is at risk for a disease. The challenge is finding the important ones.

### How are variants classified?

The American College of Medical Genetics and Genomics (ACMG) uses five categories:

| Category | What it means | What happens clinically |
|----------|---------------|------------------------|
| **Pathogenic** | This variant causes or strongly contributes to disease | Reported to patient. Genetic counselling offered. |
| **Likely pathogenic** | Strong evidence, but not conclusive | Reported with a caveat that evidence is still accumulating. |
| **VUS** (Variant of Uncertain Significance) | Not enough evidence to say whether it matters | **Not acted upon.** May be reclassified as more data becomes available. |
| **Likely benign** | Probably does not affect health | Usually not reported. |
| **Benign** | Definitively does not cause disease | Not reported. |

!!! warning "More than half of all known variants are VUS"
    The classification backlog is enormous and growing. "We don't know yet" is often the most honest answer in genomics. This is true for humans and AI alike.

### What is the annotation pipeline?

When you have a list of variants (in a file called a VCF), you need to find out what each one does. The standard pipeline is:

```
Your variants (VCF file)
    |
    v
VEP (Ensembl Variant Effect Predictor)
    --> What gene is affected? What type of change? (missense, synonymous, frameshift...)
    |
    v
ClinVar (NCBI clinical database)
    --> Has this variant been seen in patients? Is it pathogenic?
    |
    v
gnomAD (population frequency database)
    --> How common is this variant across 76,000+ genomes?
    |
    v
ACMG classification
    --> Combining all evidence: Pathogenic / Likely pathogenic / VUS / Likely benign / Benign
    |
    v
Report
```

In this workshop, ClawBio runs this entire pipeline for you in one step.

### What is pharmacogenomics?

Some genetic variants change how your body processes medications. This field is called pharmacogenomics (PGx). Knowing your PGx profile before starting a medication can prevent serious side effects.

Key examples:

| Gene | What it affects | Why it matters |
|------|----------------|----------------|
| **CYP2D6** | Codeine, tamoxifen, antidepressants (51 drugs total) | "Poor metabolisers" get zero pain relief from codeine because they cannot convert it to morphine |
| **CYP2C19** | Clopidogrel (blood thinner), stomach acid drugs | "Poor metabolisers" on clopidogrel remain at full stroke/heart attack risk because the drug is not activated |
| **CYP2C9 + VKORC1** | Warfarin (blood thinner) | Wrong dose causes dangerous bleeding (too much) or blood clots (too little). Dosing depends on both genes together. |
| **TPMT** | Azathioprine (immunosuppressant) | "Poor metabolisers" suffer life-threatening bone marrow suppression at standard doses |
| **DPYD** | 5-fluorouracil (chemotherapy) | Deficiency can be fatal at standard chemo doses |

[CPIC](https://cpicpgx.org/) (Clinical Pharmacogenetics Implementation Consortium) publishes evidence-based guidelines that map genetic results to drug recommendations. ClawBio's skills implement these guidelines directly.

### The equity problem in genomics

Most genomic research has been conducted on people of European descent:

- **86%** of genome-wide association study (GWAS) participants are European
- Databases have **30 times more** BRCA variant data for Europeans than for other populations
- Polygenic risk scores (genetic risk predictions) lose up to **80% accuracy** in non-European populations

This means a variant that looks "benign" in current databases may simply be unstudied in the relevant population. AI systems trained on this biased data amplify the problem rather than fixing it.

### The genome we are analysing

In this workshop, you will analyse the genome of Dr Manuel Corpas, published in 2013 under a CC0 (public domain) licence. It is one of the first fully open personal genomes.

Real clinically relevant findings from this genome include:

- **Factor V Leiden**: carrier for increased blood clotting risk
- **HFE C282Y**: carrier for hereditary haemochromatosis (iron overload)
- **CFTR deltaF508**: carrier for cystic fibrosis
- **VKORC1 + CYP2C9**: warfarin sensitivity (standard dose is dangerous)
- **APOE e3/e4**: elevated Alzheimer's disease risk factor

> Corpas, M. (2013). Crowdsourcing the Corpasome. *Source Code for Biology and Medicine*, **8**, 13. [doi:10.1186/1751-0473-8-13](https://doi.org/10.1186/1751-0473-8-13)

---

## Part 3: How to run the workshop

### What you need

- A **Google account** (any free Gmail account works)
- A **web browser** (Chrome, Firefox, or Safari)
- That is it. No software to install, no terminal commands, no API keys, no payment.

### Opening the notebook

Click the button below to open the workshop notebook in Google Colab:

[:material-open-in-new: Launch in Google Colab](https://colab.research.google.com/github/ClawBio/ClawBio/blob/main/docs/tutorial-variant-interpretation.ipynb){ .md-button .md-button--primary }

When it opens, you will see a document with text blocks and code blocks. Code blocks have a **play button** on the left. Click the play button to run each block in order, from top to bottom.

!!! tip "First time using Google Colab?"
    Google Colab is a free service that lets you run Python code in your browser. You do not need to know Python. Just click the play button on each code cell and read the output. If Colab asks you to "connect to a runtime", click **Connect** in the top right corner.

### Step-by-step guide

#### Step 0: Setup (2 minutes)

Run the first two code cells. They will:

1. Download the ClawBio toolkit (takes ~15 seconds)
2. Install the required analysis libraries

You should see:

```
ClawBio loaded successfully
Skills available: 39
```

!!! tip "If something goes wrong"
    If you see an error, click **Runtime > Restart and run all** in the Colab menu bar. This resets everything and runs all cells from the beginning.

#### Step 1: Explore the genome (5 minutes)

The notebook loads the Corpasome (Manuel Corpas's 23andMe genotype file). You will see:

- The file contains approximately **600,000 SNPs**
- Each line has four columns: rsID (variant name), chromosome, position, genotype
- A table showing how many variants are on each chromosome (chromosome 1 has the most because it is the largest)

#### Step 2: Select clinically relevant variants (3 minutes)

Out of 600,000 variants, the notebook extracts **21 that are known to be clinically important**. These include variants in genes for:

- Drug metabolism (CYP2C19, CYP2D6, CYP2C9, VKORC1, TPMT, MTHFR)
- Cancer risk (BRCA1, TP53)
- Blood clotting (Factor V, Prothrombin)
- Iron metabolism (HFE)
- Cystic fibrosis (CFTR)
- Alzheimer's risk (APOE)

The notebook converts these into VCF format, which is the standard input for genomic analysis tools.

#### Step 3: Run the variant annotation (5 minutes)

This is the main analysis. The notebook sends the 21 variants to the Ensembl VEP API (a free, public service run by the European Bioinformatics Institute) and retrieves:

- What gene each variant is in
- What effect it has on the protein (missense, synonymous, etc.)
- Whether ClinVar has classified it (pathogenic, benign, VUS, drug response)
- How common it is across world populations (gnomAD frequency)
- A priority tier (Tier 1 = most clinically relevant, Tier 4 = benign)

!!! info "No API key needed"
    The Ensembl VEP REST API is free and public. ClawBio handles all the formatting and submission automatically. You just click the play button.

#### Step 4: Pharmacogenomic interpretation (5 minutes)

The notebook runs a second analysis focused on drug-gene interactions. It maps the variants to CPIC guideline recommendations: which drugs to avoid, which need dose adjustments, and which are safe at standard doses.

The warfarin finding is the standout result (see "Understanding your results" below).

#### Step 5: Exercises (15 minutes, independent work)

| Exercise | What to do | Required? |
|----------|-----------|-----------|
| **5a** | Run the analysis again on a different set of 20 synthetic variants (one click, using the `--demo` flag). Compare the findings with the Corpasome results. | Yes |
| **5b** | If you have your own 23andMe or AncestryDNA file, upload it and analyse your own genome. Your data stays in the Colab session and is deleted when you close the tab. | Optional |
| **5c** | Pick one gene from the results. Look up its function, its ACMG classification, and its population frequency. Write a short paragraph: would you report this to a patient? Why or why not? | Yes |

---

## Part 4: Understanding your results

### Priority tiers

ClawBio assigns every variant a priority tier:

| Tier | What it means | Example from this workshop |
|------|---------------|---------------------------|
| **Tier 1** | Pathogenic or likely pathogenic. Rare (less than 0.1% of the population). Highest clinical relevance. | CFTR deltaF508: carrier for cystic fibrosis |
| **Tier 2** | Drug response variant or established risk factor. Actionable under CPIC guidelines. | VKORC1 rs9923231 TT: warfarin high sensitivity |
| **Tier 3** | Variant of uncertain significance (VUS). Not enough evidence to classify. | Rare missense variants with no ClinVar entry |
| **Tier 4** | Benign or likely benign. Common in the population (over 1%). | MTHFR A1298C: common polymorphism |

### Key findings explained

#### Factor V Leiden (rs6025): Tier 1

**What the result says:** Heterozygous carrier (one copy of the variant).

**What it means:** Factor V is a protein involved in blood clotting. The Leiden variant makes the clotting system overactive, increasing the risk of deep vein thrombosis (blood clots) by 3 to 8 times.

**Why it matters:** About 5% of Europeans carry this variant. It is relevant for decisions about oral contraceptives (which also increase clotting risk), surgery planning, and advice about long-haul flights. Family members should be offered testing.

#### HFE C282Y (rs1800562): Tier 1

**What the result says:** Heterozygous carrier.

**What it means:** The HFE gene controls iron absorption. People with two copies of C282Y absorb too much iron, which accumulates in the liver, heart, and pancreas, causing serious organ damage (hereditary haemochromatosis). Carriers with one copy have mildly elevated iron but almost never develop the disease.

**Why it matters:** Simple blood tests (serum ferritin, transferrin saturation) can monitor iron levels. Early detection in homozygotes is life-saving because treatment (regular blood donation) is cheap and effective.

#### CFTR deltaF508 (rs113993960): Tier 1

**What the result says:** Heterozygous carrier.

**What it means:** CFTR mutations cause cystic fibrosis, a serious condition affecting the lungs and digestive system. You need two copies (one from each parent) to have the disease. Carriers with one copy are healthy. About 1 in 25 Europeans is a carrier.

**Why it matters:** Carrier status is relevant for family planning. If both partners carry a CFTR mutation, each child has a 25% chance of having cystic fibrosis. Partner testing is recommended.

#### Warfarin sensitivity (CYP2C9 + VKORC1): Tier 2

**What the result says:** CYP2C9 *1/*2 (intermediate metaboliser) + VKORC1 rs9923231 TT (high sensitivity).

**What it means:** Warfarin is a blood-thinning medication with a very narrow "safe zone". Too little and blood clots form; too much and dangerous bleeding occurs. Two genes determine how much warfarin a person needs:

- **CYP2C9** breaks down warfarin. The *2 variant slows this down, so the drug stays active longer.
- **VKORC1** is the drug's target. The TT genotype makes the target more sensitive, so less drug is needed.

This combination means the Corpasome individual needs a **significantly lower dose than standard**, or should use an alternative anticoagulant entirely.

!!! danger "This is the textbook example of pharmacogenomics saving lives"
    Without genetic testing, a doctor might prescribe the standard warfarin dose. In this individual, that dose could cause a haemorrhage. Pre-emptive pharmacogenomic testing catches this before the first prescription.

#### APOE e3/e4 (rs429358 + rs7412): Risk factor

**What the result says:** APOE genotype e3/e4.

**What it means:** The APOE gene comes in three common forms: e2, e3, and e4. The e4 variant is the strongest common genetic risk factor for late-onset Alzheimer's disease. One copy (e3/e4) increases risk about 3-fold compared to the most common genotype (e3/e3). Two copies (e4/e4) increase risk about 12-fold.

**Important context:** APOE e4 is a risk factor, not a diagnosis. Many carriers never develop Alzheimer's, and many Alzheimer's patients do not carry e4. This is a probabilistic finding, not a deterministic one. Disclosure should always be accompanied by genetic counselling.

#### MTHFR C677T (rs1801133): Tier 2

**What the result says:** Heterozygous (one copy).

**What it means:** MTHFR helps process folate (vitamin B9). The C677T variant reduces enzyme activity to about 65% in heterozygotes and about 35% in homozygotes. This is extremely common: 30 to 40% of Europeans carry at least one copy.

**Important context:** MTHFR is one of the most over-interpreted variants in consumer genomics. For the vast majority of carriers, it has no clinical significance. Homozygotes may benefit from methylfolate supplementation during pregnancy, but heterozygotes generally do not need any action.

### Reading the output table

The annotated variants table has one row per variant. Here is what each column means:

| Column | Plain English |
|--------|--------------|
| `gene` | Which gene the variant is in (e.g., CYP2D6, CFTR) |
| `consequence` | What the variant does to the protein: `missense_variant` (changes an amino acid), `synonymous_variant` (no change), `frameshift_variant` (disrupts the protein), etc. |
| `impact` | Severity: HIGH (likely disrupts protein), MODERATE (changes protein but may be tolerated), LOW (unlikely to matter), MODIFIER (non-coding region) |
| `clinvar_significance` | What ClinVar says: Pathogenic, Likely pathogenic, VUS, Benign, Drug response |
| `gnomad_af` | How common the variant is globally. Values below 0.001 (0.1%) are considered rare. |
| `priority_tier` | ClawBio's overall assessment: Tier 1 (most important) to Tier 4 (benign) |

!!! warning "What this analysis cannot tell you"
    Consumer genotyping arrays (23andMe, AncestryDNA) test about 600,000 positions out of 3 billion in the genome. They miss structural variants, most rare variants, and copy number changes. A "clear" result from a genotyping array does **not** mean the genome is free of pathogenic variants. Clinical-grade whole genome sequencing is far more comprehensive.

---

## Part 5: Take-home messages

1. **The biology has not changed.** AI makes the mechanical steps faster (database lookups, file conversions, prioritisation), but the fundamentals of variant interpretation, molecular biology, population genetics, and clinical context, remain essential. You still need to understand what VUS means before you can explain it to a patient.

2. **Speed has changed dramatically.** An analysis that used to take a bioinformatician days (setting up tools, running VEP, parsing output, cross-referencing ClinVar and gnomAD) now takes minutes. The bottleneck shifts from data processing to clinical interpretation and decision-making.

3. **Pharmacogenomics is already saving lives.** Drug-gene interactions like warfarin/CYP2C9/VKORC1 are not hypothetical future medicine. They are implemented today in hospitals that offer pre-emptive PGx testing. The evidence base and clinical guidelines already exist.

4. **"We don't know yet" is a valid answer.** Over half of all variants in ClinVar are classified as VUS. Communicating uncertainty honestly, rather than overpromising what genomics can deliver, is one of the most important skills in this field.

5. **Equity gaps are real.** When 86% of research has been done on European populations, genomic tools are inherently less reliable for everyone else. AI systems trained on biased data amplify this problem. Every analysis should acknowledge which populations the reference data represents.

6. **Open data makes open science possible.** This entire workshop, a real genome, open-source tools, free APIs, a free notebook, is reproducible by anyone in the world. That transparency is the standard to aim for.

!!! danger "Medical disclaimer"
    ClawBio is a research and educational tool. It is not a medical device and does not provide clinical diagnoses. The findings discussed in this workshop are for educational purposes only. Consult a healthcare professional before making any medical decisions based on genetic data.

---

## Links and references

### Workshop resources

| Resource | Link |
|----------|------|
| Google Colab notebook | [:material-open-in-new: Open in Colab](https://colab.research.google.com/github/ClawBio/ClawBio/blob/main/docs/tutorial-variant-interpretation.ipynb) |
| ClawBio GitHub repository | [github.com/ClawBio/ClawBio](https://github.com/ClawBio/ClawBio) |
| ClawBio documentation | [docs.clawbio.ai](https://docs.clawbio.ai) |
| ClawBio Discord community | [discord.gg/EEp4Neaz](https://discord.gg/EEp4Neaz) |

### Databases used in this workshop

| Database | What it does | Link |
|----------|-------------|------|
| Ensembl VEP | Predicts the functional effect of variants | [ensembl.org/vep](https://www.ensembl.org/info/docs/tools/vep/index.html) |
| ClinVar | Curated variant-disease associations | [ncbi.nlm.nih.gov/clinvar](https://www.ncbi.nlm.nih.gov/clinvar/) |
| gnomAD | Population allele frequencies (76,000+ genomes) | [gnomad.broadinstitute.org](https://gnomad.broadinstitute.org/) |
| CPIC | Pharmacogenomics clinical guidelines | [cpicpgx.org](https://cpicpgx.org/) |

### Key papers

- Richards et al. (2015). Standards and guidelines for the interpretation of sequence variants. *Genetics in Medicine*, 17(5), 405-424. [doi:10.1038/gim.2015.30](https://doi.org/10.1038/gim.2015.30)
- Corpas, M. (2013). Crowdsourcing the Corpasome. *Source Code for Biology and Medicine*, 8, 13. [doi:10.1186/1751-0473-8-13](https://doi.org/10.1186/1751-0473-8-13)
