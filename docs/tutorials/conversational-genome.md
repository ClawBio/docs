# Try Conversational Genome

**Ask questions about Manuel Corpas’s public genome in a hosted chat. No Colab runtime, installation or visitor API key is needed.**

[Open Conversational Genome](https://conversational.clawbio.ai){ .md-button }

## Start with a question

Try: "What can this genome tell me about codeine, and what are the limitations?"

The deployed service routes this question through a model and executes the PharmGx skill. Inspect the result and its limitations. You can also ask about missing evidence or the source of a finding.

This is an educational demonstration about Manuel’s public data, not a service for analysing your own genome. Do not enter private health information.

## Understand what runs

The app combines live ClawBio skill execution with precomputed findings. The codeine route was checked against the deployed service on 10 September 2026 and returned a live PharmGx result. This check does not validate every question or scientific conclusion.

Genome-wide findings and panel-based analyses use different inputs. Do not interpret a panel result as comprehensive whole-genome analysis. The whole-genome source linked by the app is [Manuel Corpas’s public sequencing deposit](https://doi.org/10.5281/zenodo.19326528).

**Input provenance checked:** all 23 stored PGx genotype strings match the [public genotype file at this pinned ClawBio revision](https://github.com/ClawBio/ClawBio/blob/7290841dfc9c7e817c12af38a2dd1479f0babe8e/skills/genome-compare/data/manuel_corpas_23andme.txt.gz). This was checked on 10 September 2026. The app’s older Figshare citation identifies the broader Corpasome deposit; the linked file provides the direct input reference.

**Interpretation limitation:** this app passes rsID/genotype pairs directly to the PharmGx API. It does not perform the file reader’s reference-coordinate check, which withholds interpretations for this file in the Colab prototype. Matching the genotype strings establishes input provenance, not reference-build compatibility, allele-orientation validation or clinical validity. Treat the outputs as an educational demonstration.

## Inspect execution yourself

[Explore the Colab agent prototype](ask-clawbio.md) for an inspectable tool loop, commands and downloadable evidence. It requires one explicit launch step and currently has model-availability and input-coordinate limitations.

[Run the guided PharmGx tutorial](run-your-first-skill.md) for a deterministic walkthrough without model access.

ClawBio is a research and educational tool. It is not a medical device and does not provide clinical diagnoses. Consult a healthcare professional before making any medical decisions.
