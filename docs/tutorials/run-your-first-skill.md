---
title: "Run Your First Skill"
description: Run a ClawBio skill demo in Google Colab — no installation, no terminal, no cost.
---

# Run Your First Skill

<div class="tutorial-card__header">
  <span class="difficulty-badge difficulty-badge--beginner">Beginner</span>
  <span class="time-estimate">~15 min</span>
</div>

**No installation. No terminal. No cost.** Everything runs in your browser via Google Colab. All you need is a Google account.

[:material-open-in-new: Launch in Google Colab](https://colab.research.google.com/github/ClawBio/ClawBio/blob/main/docs/tutorial-variant-interpretation.ipynb){ .md-button .md-button--primary }

!!! tip "Also works locally"
    Prefer to run on your own machine? Every code cell below works in a terminal too. Just remove the `!` prefix.

---

## 1. Install ClawBio

Open a new Google Colab notebook and run:

```python
!git clone https://github.com/ClawBio/ClawBio.git
%cd ClawBio
!pip install -q -r requirements.txt
```

That is it. ClawBio is ready to use.

## 2. Run the PharmGx Demo

Every ClawBio skill ships with synthetic demo data. Run the **PharmGx Reporter** — it generates a pharmacogenomics report from a sample 23andMe-format file:

```python
!python3 skills/pharmgx-reporter/pharmgx_reporter.py \
  --input skills/pharmgx-reporter/demo_patient.txt \
  --output /tmp/pharmgx-demo
```

You should see output like:

```
✓ Loaded 47 variants from demo_patient.txt
✓ Matched 12 actionable pharmacogenes
✓ Report written to /tmp/pharmgx-demo/report.md
✓ Summary written to /tmp/pharmgx-demo/summary.json
```

## 3. Inspect the Output

```python
!cat /tmp/pharmgx-demo/report.md
```

The report includes:

- **Patient summary** — matched pharmacogenes and star alleles
- **Drug-gene interactions** — CPIC guideline-backed recommendations
- **Safety warnings** — flagged high-risk variants (e.g. DPYD*2A for fluorouracil toxicity)
- **Research-use disclaimer** — ClawBio is not a medical device

View the structured JSON:

```python
import json
with open("/tmp/pharmgx-demo/summary.json") as f:
    data = json.load(f)
print(json.dumps(data, indent=2))
```

## 4. Try Another Skill

Run any other skill with `--demo`:

```python
# Polygenic risk scores
!python3 skills/gwas-prs/gwas_prs.py --demo --output /tmp/prs-demo

# Single-cell RNA-seq pipeline
!python3 skills/scrna-orchestrator/scrna_orchestrator.py --demo --output /tmp/scrna-demo

# Health equity scoring
!python3 skills/equity-scorer/equity_scorer.py --demo --output /tmp/equity-demo

# GWAS variant lookup across 9 databases
!python3 skills/gwas-lookup/gwas_lookup.py --demo --output /tmp/gwas-demo
```

## 5. Understand the Flow

Every ClawBio skill follows the same pattern:

1. **SKILL.md** defines the contract — inputs, outputs, domain decisions, safety rules
2. **Python script** implements the analysis — reads inputs, runs the pipeline, writes outputs
3. **Demo data** provides synthetic test data — no real patient data needed
4. **An AI agent** (optional) dispatches the skill, passes parameters, and explains the results

The agent reads the SKILL.md to understand what the skill does and how to call it. The agent **never overrides** domain decisions or safety rules defined in the SKILL.md.

---

**Next:** [Build a Skill](build-a-skill.md) — create your own skill from scratch.
