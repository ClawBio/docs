---
title: ClawBio Documentation
description: Technical documentation, tutorials, and skill reference for ClawBio, the bioinformatics-native AI agent skill library.
---

<div class="hero">
  <h1 class="hero__title">ClawBio Documentation</h1>
  <p class="hero__subtitle">Technical docs, tutorials, and presentations for the bioinformatics AI skill library</p>
  <p>
    <a href="https://clawbio.ai" class="md-button md-button--primary">ClawBio Home</a>
    &nbsp;
    <a href="https://github.com/ClawBio/ClawBio" class="md-button">GitHub</a>
  </p>
</div>

<h2 class="section-heading">Get Started</h2>

<div class="tutorial-cards">

<a class="tutorial-card" href="tutorials/setup/">
  <div class="tutorial-card__header">
    <span class="difficulty-badge difficulty-badge--beginner">Beginner</span>
    <span class="time-estimate">10 min</span>
  </div>
  <h3 class="tutorial-card__title">Setup</h3>
  <p class="tutorial-card__desc">Install an AI coding agent, connect it to a model provider, and run your first prompt.</p>
</a>

<a class="tutorial-card" href="tutorials/run-your-first-skill/">
  <div class="tutorial-card__header">
    <span class="difficulty-badge difficulty-badge--beginner">Beginner</span>
    <span class="time-estimate">15 min</span>
  </div>
  <h3 class="tutorial-card__title">Run Your First Skill</h3>
  <p class="tutorial-card__desc">Run PharmGx, Equity Scorer, or NutriGx with demo data and explore the output.</p>
</a>

<a class="tutorial-card" href="tutorials/build-a-skill/">
  <div class="tutorial-card__header">
    <span class="difficulty-badge difficulty-badge--intermediate">Intermediate</span>
    <span class="time-estimate">30 min</span>
  </div>
  <h3 class="tutorial-card__title">Build a Skill</h3>
  <p class="tutorial-card__desc">Write a SKILL.md, add Python implementation, and submit a PR.</p>
</a>

<a class="tutorial-card" href="skills/">
  <div class="tutorial-card__header">
    <span class="difficulty-badge difficulty-badge--tutorial">Reference</span>
  </div>
  <h3 class="tutorial-card__title">Skill Library</h3>
  <p class="tutorial-card__desc">Browse all available skills: pharmacogenomics, GWAS, scRNA-seq, equity scoring, and more.</p>
</a>

<a class="tutorial-card" href="presentations/">
  <div class="tutorial-card__header">
    <span class="difficulty-badge difficulty-badge--event">Slides</span>
  </div>
  <h3 class="tutorial-card__title">Presentations</h3>
  <p class="tutorial-card__desc">All ClawBio talks, workshops, and pitch decks in one place, newest first.</p>
</a>

<a class="tutorial-card" href="deployment/">
  <div class="tutorial-card__header">
    <span class="difficulty-badge difficulty-badge--intermediate">Intermediate</span>
  </div>
  <h3 class="tutorial-card__title">Deployment</h3>
  <p class="tutorial-card__desc">Deploy ClawBio via Docker, Railway, or private cloud.</p>
</a>

<a class="tutorial-card" href="tutorials/variant-interpretation-workshop/">
  <div class="tutorial-card__header">
    <span class="difficulty-badge difficulty-badge--beginner">Beginner</span>
    <span class="time-estimate">60 min</span>
  </div>
  <h3 class="tutorial-card__title">Variant Interpretation Workshop</h3>
  <p class="tutorial-card__desc">Annotate a real human genome in Google Colab. No installation, no terminal, no prior experience required.</p>
</a>

<a class="tutorial-card" href="tutorials/30x-wgs-workshop/">
  <div class="tutorial-card__header">
    <span class="difficulty-badge difficulty-badge--intermediate">Intermediate</span>
    <span class="time-estimate">40 min</span>
  </div>
  <h3 class="tutorial-card__title">30x WGS Workshop</h3>
  <p class="tutorial-card__desc">Explore a real 30x whole-genome sequence: structural variants, QC metrics, and pharmacogenomics beyond SNP arrays.</p>
</a>

</div>

---

## Quick Install

```bash
pip install clawbio                 # Python 3.11+
clawbio run pharmgx --demo
```

Prefer [conda](https://docs.conda.io/)? `conda install -c bioconda clawbio`.

Using [Claude Code](https://claude.com/claude-code)? Install the skills as a plugin:

```
/plugin marketplace add ClawBio/ClawBio
/plugin install clawbio
```

**Developing ClawBio, or want every skill with its full demo data?** Work from a source
checkout instead ([uv](https://docs.astral.sh/uv/) recommended):

```bash
git clone https://github.com/ClawBio/ClawBio.git && cd ClawBio
uv sync
uv run python clawbio.py run pharmgx --demo
```

---

[Skill Library](skills/index.md) · [SKILL.md Spec](reference/skillmd-spec.md) · [Contributing](contributing/index.md) · [All Tutorials](tutorials/index.md) · [Presentations](presentations/index.md)
