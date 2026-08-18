---
title: "Berlin Challenge Data"
description: Every dataset used by the Berlin hackathon challenges, with direct download links, checksums and attribution.
---

# Challenge data

Everything the three challenges need is either downloadable from this page, bundled
inside the ClawBio skills, or fetched live from a public API. Nothing requires an
account, a login or an organiser.

If you are stuck on data at any point, ask in `#berlin-help` rather than losing build
time to it.

## Challenge 1: End the diagnostic odyssey

The hour-one input is a small teaching pack hosted here. It is 68 records, so it
downloads instantly and works on any laptop.

| File | Size | Download |
|---|---:|---|
| Segregation VCF, bgzipped | 15 KB | [challenge1-b37-segregation.vcf.gz](challenge1-b37-segregation.vcf.gz) |
| Tabix index | 4 KB | [challenge1-b37-segregation.vcf.gz.tbi](challenge1-b37-segregation.vcf.gz.tbi) |
| Readable genotype table | 18 KB | [challenge1-b37-segregation.tsv](challenge1-b37-segregation.tsv) |

**In the BioNeMo Research Agent**, just paste the three URLs and ask it to fetch them.
The Challenge 1 prompt template already does this, and it asks the agent to say plainly
whether it can reach them rather than pretending either way. If it cannot fetch files,
the `.tsv` is small enough to paste in directly.

??? note "Fetching them on your own machine"

    ```bash
    mkdir -p data/challenge1 && cd data/challenge1
    curl -fsSLO https://docs.clawbio.ai/hackathon/berlin/data/challenge1-b37-segregation.vcf.gz
    curl -fsSLO https://docs.clawbio.ai/hackathon/berlin/data/challenge1-b37-segregation.vcf.gz.tbi
    curl -fsSLO https://docs.clawbio.ai/hackathon/berlin/data/challenge1-b37-segregation.tsv
    ```

**What is in it.** 68 autosomal, biallelic, PASS records from a four-person exome
pedigree: son, father, mother and sister. Sample IDs are `ISDBM322015` through
`ISDBM322018`. Every record is HIGH-effect by the historical SnpEff `EFF` annotation,
carried by the son and exactly one parent, with DP at least 10 and GQ at least 20 in all
four samples. There are 30 paternal and 38 maternal unphased teaching labels.
`bcftools +mendelian2 --rules GRCh37` reports 68 good sites, zero errors and zero missing
trio calls.

**Build.** GRCh37 / b37, `human_g1k_v37.fasta`. Do not relabel it as hg19. If you add an
annotation layer, match the build explicitly or say that you could not.

**Integrity.**

```text
c6c1185618c232d6b751dabb78a9678936f1fedf2633fbb7f35ccfa992e3dc90  challenge1-b37-segregation.vcf.gz
c4226f98a47b0036f163b8ead764932de1abfe3521e51b2b8592d9398cbf157b  challenge1-b37-segregation.vcf.gz.tbi
495b749ea3271e5b7e17e8d3609b3ad535fddc411ff4c636d74afa701147ac05  challenge1-b37-segregation.tsv
```

**Provenance and licence.** Derived subset of Corpasome by Manuel Corpas, DOI
[10.6084/m9.figshare.693052.v3](https://figshare.com/articles/dataset/Corpasome/693052),
licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Keep the attribution
in anything you publish or demo.

The full [joint four-person exome VCF](https://figshare.com/articles/dataset/Corpasome/693052)
and the [son-only exome VCF](https://f1000.figshare.com/articles/dataset/Son_exome_files/92584)
are extension sources if you want more than 68 records. They are large, so start from the
pack above and only reach for them if your project genuinely needs to.

!!! warning "Interpretation boundary, and it is part of the judging"

    `PARENT_OF_ORIGIN_UNPHASED` is a teaching label, not proof of molecular phase.

    These records must not be called rare, pathogenic, diagnostic, confirmed de novo or
    compound heterozygous. The source has no valid population-frequency layer, no
    phenotype and no HPO terms, and the historical `EFF` annotation is not current
    clinical evidence.

    Public human genomes remain potentially identifiable. Do not mix this pack with
    attendee data, and do not upload it to an unapproved service. Do not add the
    low-quality, build-undeclared aunt WGS as a fifth segregation sample.

    Stating these limits clearly scores better than working around them.

## Challenge 2: A cancer target you would defend

No downloads. The `xena-tcga-gene-query` skill queries the UCSC Xena API live, so your
data arrives as you ask for it. Verified working this morning.

The literature skills (`pubmed-summariser`, `lit-synthesizer`) and
`clinical-trial-finder` also call public APIs directly. `drug-repurposing-screen` works
on a single public CRISPR count table that downloads in seconds.

Sources in play: TCGA via [UCSC Xena](https://xenabrowser.net/),
[Open Targets](https://platform.opentargets.org/),
[ClinicalTrials.gov](https://clinicaltrials.gov/) and
[PubMed](https://pubmed.ncbi.nlm.nih.gov/).

!!! danger "The hard rule on this challenge"

    Any PMID that does not resolve puts your project out of contention for first place.
    Have your agent open every citation it produces and confirm it exists.

## Challenge 3: Whose genome does this fail?

Bundled in the repository. Nothing to download.

- `skills/gwas-prs/demo_patient_prs.txt` is the demo genotype file, and `--demo` uses it
  automatically.
- `skills/gwas-prs/curated_scores.json` holds six curated PGS Catalog scores. Live search
  against the [PGS Catalog REST API](https://www.pgscatalog.org/rest/) is available for
  any other trait.
- `skills/claw-ancestry-pca` ships its own demo reference panel, with SGDP and 1000
  Genomes as the extension route.

## What else is available

The repository bundles demo inputs for every skill command named in the briefs. That does
not mean every one of the 98 skills ships data, and it does not mean every public source
has an API. If a skill you want has no demo data, say so in your demo rather than
inventing an input.

Other public sources that are fair game: GIAB, ClinVar, gnomAD, 1000 Genomes, SGDP, GEO
and Expression Atlas.

Public data only. Nothing participant-supplied, and no patient data of any kind.

[Back to the challenges](../tracks.md){ .md-button }
