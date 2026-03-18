---
title: "Run Your First Skill"
description: Clone ClawBio, run the PharmGx demo, and understand the input-output flow.
---

# Run Your First Skill

<div class="tutorial-card__header">
  <span class="difficulty-badge difficulty-badge--beginner">Beginner</span>
  <span class="time-estimate">~15 min</span>
</div>

In this tutorial you'll clone the ClawBio repository, install dependencies, run a demo skill, and inspect the output files.

---

## 1. Clone the Repository

```bash
git clone https://github.com/ClawBio/ClawBio.git
cd ClawBio
```

## 2. Install Dependencies

Create a virtual environment and install the required packages:

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 3. Run the PharmGx Demo

Every ClawBio skill ships with synthetic demo data. Run the **PharmGx Reporter** — it generates a pharmacogenomics report from a sample 23andMe-format file:

```bash
python skills/pharmgx-reporter/pharmgx_reporter.py \
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

## 4. Inspect the Output

Open the generated report:

```bash
cat /tmp/pharmgx-demo/report.md
```

The report includes:

- **Patient summary** — matched pharmacogenes and star alleles
- **Drug-gene interactions** — CPIC guideline-backed recommendations
- **Safety warnings** — flagged high-risk variants (e.g. DPYD*2A for fluorouracil toxicity)
- **Research-use disclaimer** — ClawBio is not a medical device

The `summary.json` file contains the same data in a structured format for programmatic use.

## 5. Try Another Skill

Run any other skill with `--demo`:

```bash
# Polygenic risk scores
python skills/gwas-prs/gwas_prs.py --demo --output /tmp/demo

# Single-cell RNA-seq pipeline
python skills/scrna-orchestrator/scrna_orchestrator.py --demo --output /tmp/demo

# Health equity scoring
python skills/equity-scorer/equity_scorer.py --demo --output /tmp/demo
```

## 6. Understand the Flow

Every ClawBio skill follows the same pattern:

1. **SKILL.md** defines the contract — inputs, outputs, domain decisions, safety rules
2. **Python script** implements the analysis — reads inputs, runs the pipeline, writes outputs
3. **Demo data** provides synthetic test data — no real patient data needed
4. **An AI agent** (optional) dispatches the skill, passes parameters, and explains the results

The agent reads the SKILL.md to understand what the skill does and how to call it. The agent **never overrides** domain decisions or safety rules defined in the SKILL.md.

---

**Next:** [Build a Skill](build-a-skill.md) — create your own skill from scratch.
