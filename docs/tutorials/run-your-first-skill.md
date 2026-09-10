---
title: "Try ClawBio in Google Colab"
description: Run a guided PharmGx demo on synthetic teaching data, inspect the evidence, and download your results. No AI account or API key required.
---

# Try ClawBio in Google Colab

Run a pharmacogenomics analysis in your browser, inspect its results, and test what happens when evidence is missing.

[Open the ClawBio demo in Colab](https://colab.research.google.com/github/ClawBio/ClawBio/blob/main/docs/tutorial-first-skill.ipynb){ .md-button }

**You need a Google account. No AI account, API key, GPU or paid Colab plan is required for this exercise.** Colab's free computing resources are subject to availability. The notebook downloads its code and dependencies during setup, then runs the analysis using bundled rules with online evidence enrichment disabled.

The input is synthetic teaching data. You do not need to upload personal genetic data or connect Google Drive.

## 1. Open and run

1. Open the notebook using the button above and sign into Google if prompted.
2. Select **Connect** if Colab asks you to choose a runtime. Use a standard CPU runtime.
3. Select **Runtime > Run all**, or click the play button beside each code cell in order.
4. If Colab asks whether you trust this public notebook, review the code before continuing.

The first cell prepares a pinned ClawBio revision and its locked dependencies in a separate environment. Allow several minutes for the first download. Setup errors stop execution; a success message appears only when setup has completed.

## 2. Inspect the result

The PharmGx demo produces an inline report and a structured `result.json`. The displayed counts and gene profiles are computed during your run.

Find **CYP2C19** in the report. The bundled teaching example has a phase-ambiguous allele combination, so the pinned implementation reports uncertainty. The notebook checks that this uncertainty is present rather than silently presenting a definite call.

This demonstrates the behaviour of a fixed software version. It does not establish clinical validity or provide treatment advice.

## 3. Test missing evidence

The next cell copies the teaching input and removes its three CYP2C19 markers. It preserves the original file and runs the same analysis again.

Compare the two outputs. CYP2C19 should now be `NOT_TESTED`. The notebook also checks that the DPYD gene profile remains unchanged.

**The lesson: missing genotype evidence must not be interpreted as a normal genotype.**

## 4. Download your evidence

The final cell downloads a ZIP containing:

- Both generated reports and structured results.
- The modified teaching input.
- A tutorial provenance record with the code revision, exact commands and file checksums.

Colab runtimes are temporary. Download results you want to retain before leaving.

## Repeat or reset

Rerunning the analysis cells creates new output folders. If setup was interrupted, rerun the setup cell first. For a fully clean start, choose **Runtime > Disconnect and delete runtime**, reconnect, then **Run all**.

## What this sandbox demonstrates

ClawBio skills execute scientific procedures and produce inspectable outputs. An AI agent can call those same skills, but this first exercise runs directly without a language model.

The notebook uses a fixed source revision and a locked environment. Its automated notebook check executes the lesson and verifies the missing-evidence behaviour. Live Colab resource availability remains outside that check.

ClawBio is a research and educational tool. It is not a medical device and does not provide clinical diagnoses. Consult a healthcare professional before making any medical decisions.

**Next:** [Build a Skill](build-a-skill.md), or continue to the [Variant Interpretation Workshop](variant-interpretation-workshop.md).
