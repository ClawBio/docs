---
title: ClawBio Documentation
description: Technical documentation, tutorials, skill reference, and research projects for ClawBio, the bioinformatics-native AI agent skill library.
---

<div class="hero">
  <h1 class="hero__title">ClawBio Documentation</h1>
  <p class="hero__subtitle">Technical docs, tutorials, and research for the bioinformatics AI skill library</p>
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
  <p class="tutorial-card__desc">Clone ClawBio, install dependencies, and run your first demo skill.</p>
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

<a class="tutorial-card" href="research/">
  <div class="tutorial-card__header">
    <span class="difficulty-badge difficulty-badge--event">Research</span>
  </div>
  <h3 class="tutorial-card__title">Research Projects</h3>
  <p class="tutorial-card__desc">Active research built on ClawBio: Genomebook, HEIM, and more.</p>
</a>

<a class="tutorial-card" href="deployment/">
  <div class="tutorial-card__header">
    <span class="difficulty-badge difficulty-badge--intermediate">Intermediate</span>
  </div>
  <h3 class="tutorial-card__title">Deployment</h3>
  <p class="tutorial-card__desc">Deploy ClawBio via Docker, Railway, or private cloud.</p>
</a>

</div>

---

## Quick Install

```bash
git clone https://github.com/ClawBio/ClawBio.git && cd ClawBio
pip install -r requirements.txt
python clawbio.py run pharmgx --demo
```

---

[Skill Library](skills/index.md) · [SKILL.md Spec](reference/skillmd-spec.md) · [Contributing](contributing/index.md) · [All Tutorials](tutorials/index.md) · [Research](research/index.md)
