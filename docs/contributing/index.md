---
title: Contributing
description: How to contribute skills to ClawBio
---

# Contributing to ClawBio

ClawBio is an open project. Anyone can contribute a skill -- from a simple SKILL.md-only methodology description to a fully implemented Python skill with demo data and tests.

## Ways to Contribute

<div class="tutorial-cards">

<a class="tutorial-card" href="author-journey/">
  <div class="tutorial-card__header">
    <span class="difficulty-badge difficulty-badge--intermediate">Intermediate</span>
    <span class="time-estimate">30 min</span>
  </div>
  <h3 class="tutorial-card__title">Author a Skill</h3>
  <p class="tutorial-card__desc">Create a new bioinformatics skill from scratch using our scaffolding tools.</p>
</a>

<a class="tutorial-card" href="framework-integration/">
  <div class="tutorial-card__header">
    <span class="difficulty-badge difficulty-badge--advanced">Advanced</span>
    <span class="time-estimate">20 min</span>
  </div>
  <h3 class="tutorial-card__title">Integrate a Framework</h3>
  <p class="tutorial-card__desc">Connect your agent framework to ClawBio's registry and MCP bridge.</p>
</a>

</div>

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/ClawBio/ClawBio.git
cd ClawBio

# 2. Scaffold a new skill
clawbio init my-new-skill

# 3. Edit the generated SKILL.md
#    Fill in domain decisions, safety rules, inputs/outputs

# 4. Add demo data and implementation (optional for MVP)

# 5. Validate locally
clawbio validate skills/my-new-skill/

# 6. Submit a pull request
git checkout -b skill/my-new-skill
git add skills/my-new-skill/
git commit -m "Add my-new-skill"
git push origin skill/my-new-skill
```

## What Makes a Good Skill

- **Encodes domain decisions**: thresholds, classification rules, guideline references -- not just a wrapper around a tool
- **Includes demo data**: users can run the skill immediately without sourcing their own data
- **Declares its boundaries**: what the skill does and does not do, when to defer to a human expert
- **References authoritative guidelines**: CPIC, ACMG, EDAM, or other domain standards with DOIs where available
- **Is reproducible**: deterministic outputs for deterministic inputs, checksummed demo output

## Contribution Types

| Type | What You Provide | Review Process |
|------|-----------------|----------------|
| SKILL.md only | Methodology description, no code | Schema validation + domain review |
| Full skill | SKILL.md + Python + demo data + tests | Schema validation + CI pipeline + domain review |
| Bug fix | Fix to an existing skill | Standard PR review |
| Documentation | Docs improvements | Standard PR review |

## Code of Conduct

ClawBio follows the [Contributor Covenant](https://www.contributor-covenant.org/version/2/1/code_of_conduct/) code of conduct. Be respectful, constructive, and inclusive.

## Questions?

- Open a [GitHub Discussion](https://github.com/ClawBio/ClawBio/discussions)
- Join our [Discord](https://discord.gg/clawbio)
