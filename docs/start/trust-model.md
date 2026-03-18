---
title: Trust Model
description: How ClawBio skills earn trust through transparency and reproducibility
---

# Trust Model

ClawBio skills earn trust through transparency, not black boxes. Every skill ships with its methodology, demo data, and reproducibility bundle so you can verify before you rely on it.

## What Every Skill Provides

| Guarantee | How |
|-----------|-----|
| Methodology is readable | SKILL.md documents all domain decisions, thresholds, and data sources |
| Demo data included | Every skill ships synthetic test data so you can run it immediately |
| Output is reproducible | `commands.sh` and `environment.yml` let you reproduce without the agent |
| Checksums verify integrity | SHA-256 checksums on outputs confirm nothing changed |
| Safety rules are explicit | SKILL.md declares what the agent must NOT override |
| Source is open | MIT licensed, full source code, no hidden dependencies |

## How to Evaluate a Skill

Before using a skill on real data:

1. **Read the SKILL.md** -- check that domain decisions cite real sources (CPIC guidelines, published papers, established databases)
2. **Run the demo** -- use `--demo` to verify the skill runs cleanly on your system
3. **Check the output** -- review the report for the safety disclaimer and sensible results
4. **Inspect the code** -- the Python implementation is open source, read it if you need to

## Safety Rules

Every skill must include a Safety Rules section in its SKILL.md. These rules constrain what the AI agent can do:

- The agent dispatches and explains; the skill executes
- The agent must not override thresholds defined in SKILL.md
- The agent must not invent gene-drug associations or clinical interpretations
- Every report must include the research-use disclaimer

## Limitations

ClawBio is a research and educational tool. It is not a medical device and does not provide clinical diagnoses. Skills have not been validated for clinical use. Always consult a healthcare professional before making medical decisions based on genomic data.
