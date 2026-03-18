---
title: ClawBio Documentation
description: Bioinformatics AI agent skills. Curated. Reproducible. Open.
---

<div class="hero" markdown>

# ClawBio Documentation
{: .hero__title }

Curated, reproducible, open-source bioinformatics skills that any AI agent can run.
{: .hero__subtitle }

</div>

**Today: [Hackathon at Imperial College London](hackathon/index.md)** | 19 March 2026

## Get Started
{: .section-heading }

<div class="tutorial-cards" markdown>

<a class="tutorial-card" href="hackathon/setup/">
  <div class="tutorial-card__header">
    <span class="difficulty-badge difficulty-badge--beginner">Beginner</span>
    <span class="time-estimate">10 min</span>
  </div>
  <h3 class="tutorial-card__title">Setup</h3>
  <p class="tutorial-card__desc">Clone ClawBio, install dependencies, and run your first demo skill.</p>
</a>

<a class="tutorial-card" href="tutorials/build-a-skill/">
  <div class="tutorial-card__header">
    <span class="difficulty-badge difficulty-badge--intermediate">Intermediate</span>
    <span class="time-estimate">30 min</span>
  </div>
  <h3 class="tutorial-card__title">Build a Skill</h3>
  <p class="tutorial-card__desc">Create a SKILL.md, add Python implementation, test it, and validate.</p>
</a>

<a class="tutorial-card" href="hackathon/agentic-tools/">
  <div class="tutorial-card__header">
    <span class="difficulty-badge difficulty-badge--intermediate">Intermediate</span>
    <span class="time-estimate">15 min</span>
  </div>
  <h3 class="tutorial-card__title">Agentic Tools</h3>
  <p class="tutorial-card__desc">Use Claude Code and AI coding assistants to build skills faster.</p>
</a>

</div>

## Tutorials — AI Coding Tools
{: .section-heading }

<div class="tutorial-cards" markdown>

<a class="tutorial-card" href="tutorials/setup/">
  <div class="tutorial-card__header">
    <span class="tutorial-card__number">01</span>
    <span class="difficulty-badge difficulty-badge--beginner">Beginner</span>
    <span class="time-estimate">20 min</span>
  </div>
  <h3 class="tutorial-card__title">Setup</h3>
  <p class="tutorial-card__desc">Get started with AI coding tools — install an agent, connect to a provider, and run your first prompt.</p>
</a>

<a class="tutorial-card" href="tutorials/penguins-analysis/">
  <div class="tutorial-card__header">
    <span class="tutorial-card__number">02</span>
    <span class="difficulty-badge difficulty-badge--beginner">Beginner</span>
    <span class="time-estimate">30 min</span>
  </div>
  <h3 class="tutorial-card__title">Penguins Analysis</h3>
  <p class="tutorial-card__desc">Data analysis with AI assistants — explore a real dataset, write code, and produce publication-ready plots.</p>
</a>

<a class="tutorial-card" href="tutorials/journal-club-slides/">
  <div class="tutorial-card__header">
    <span class="tutorial-card__number">03</span>
    <span class="difficulty-badge difficulty-badge--intermediate">Intermediate</span>
    <span class="time-estimate">25 min</span>
  </div>
  <h3 class="tutorial-card__title">Journal Club Slides</h3>
  <p class="tutorial-card__desc">Create presentations from papers — feed a PDF to an agent and receive a slide deck ready to present.</p>
</a>

<a class="tutorial-card" href="tutorials/single-cell-portal/">
  <div class="tutorial-card__header">
    <span class="tutorial-card__number">04</span>
    <span class="difficulty-badge difficulty-badge--intermediate">Intermediate</span>
    <span class="time-estimate">30 min</span>
  </div>
  <h3 class="tutorial-card__title">Single Cell Portal</h3>
  <p class="tutorial-card__desc">Build an interactive scRNA-seq viewer from CELLxGENE data using AI-assisted development.</p>
</a>

<a class="tutorial-card" href="tutorials/context-management/">
  <div class="tutorial-card__header">
    <span class="tutorial-card__number">05</span>
    <span class="difficulty-badge difficulty-badge--advanced">Advanced</span>
    <span class="time-estimate">20 min</span>
  </div>
  <h3 class="tutorial-card__title">Context Management</h3>
  <p class="tutorial-card__desc">Understand context windows, cost scaling, and how to use <code>/compact</code> to keep runs cheap and accurate.</p>
</a>

<a class="tutorial-card" href="tutorials/apm/">
  <div class="tutorial-card__header">
    <span class="tutorial-card__number">06</span>
    <span class="difficulty-badge difficulty-badge--advanced">Advanced</span>
    <span class="time-estimate">30 min</span>
  </div>
  <h3 class="tutorial-card__title">APM</h3>
  <p class="tutorial-card__desc">Dependency manager for AI context — declare, version, and inject context modules automatically.</p>
</a>

</div>

## Tutorials — ClawBio
{: .section-heading }

<div class="tutorial-cards" markdown>

<a class="tutorial-card" href="tutorials/run-your-first-skill/">
  <div class="tutorial-card__header">
    <span class="tutorial-card__number">01</span>
    <span class="difficulty-badge difficulty-badge--beginner">Beginner</span>
    <span class="time-estimate">15 min</span>
  </div>
  <h3 class="tutorial-card__title">Run Your First Skill</h3>
  <p class="tutorial-card__desc">Clone the repo, run the PharmGx demo, and understand ClawBio's input-output flow.</p>
</a>

<a class="tutorial-card" href="tutorials/build-a-skill/">
  <div class="tutorial-card__header">
    <span class="tutorial-card__number">02</span>
    <span class="difficulty-badge difficulty-badge--intermediate">Intermediate</span>
    <span class="time-estimate">30 min</span>
  </div>
  <h3 class="tutorial-card__title">Build a Skill</h3>
  <p class="tutorial-card__desc">Write a complete ClawBio skill from scratch — SKILL.md, Python, demo data, validation.</p>
</a>

<a class="tutorial-card" href="tutorials/telegram-bot/">
  <div class="tutorial-card__header">
    <span class="tutorial-card__number">03</span>
    <span class="difficulty-badge difficulty-badge--intermediate">Intermediate</span>
    <span class="time-estimate">20 min</span>
  </div>
  <h3 class="tutorial-card__title">Telegram Bot</h3>
  <p class="tutorial-card__desc">Deploy RoboTerri — a Telegram bot that runs ClawBio skills via any LLM provider.</p>
</a>

</div>

## Deploy
{: .section-heading }

<div class="section-cards" markdown>

<a class="section-card" href="deployment/docker/">
  <div class="section-card__icon">🐳</div>
  <h3 class="section-card__title">Docker</h3>
  <p class="section-card__desc">Containerise ClawBio with Docker and docker-compose. GPU passthrough for ML skills.</p>
</a>

<a class="section-card" href="deployment/railway/">
  <div class="section-card__icon">🚂</div>
  <h3 class="section-card__title">Railway</h3>
  <p class="section-card__desc">One-click cloud deployment with persistent storage and custom domains.</p>
</a>

<a class="section-card" href="deployment/private-cloud/">
  <div class="section-card__icon">🔒</div>
  <h3 class="section-card__title">Private Cloud</h3>
  <p class="section-card__desc">Self-hosted on AWS, GCP, or Azure. Air-gapped options for sensitive genomic data.</p>
</a>

</div>

## Quick Links
{: .section-heading }

<div class="section-cards" markdown>

<a class="section-card" href="skills/">
  <div class="section-card__icon">🧬</div>
  <h3 class="section-card__title">Skill Library</h3>
  <p class="section-card__desc">Browse 24+ bioinformatics skills with demo data.</p>
</a>

<a class="section-card" href="reference/skillmd-spec/">
  <div class="section-card__icon">📋</div>
  <h3 class="section-card__title">SKILL.md Spec</h3>
  <p class="section-card__desc">The contract format behind every ClawBio skill.</p>
</a>

<a class="section-card" href="contributing/">
  <div class="section-card__icon">🤝</div>
  <h3 class="section-card__title">Contributing</h3>
  <p class="section-card__desc">Submit skills, report bugs, and improve the docs.</p>
</a>

</div>
