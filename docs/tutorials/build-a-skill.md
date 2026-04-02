---
title: "Build a Skill"
description: Create a complete ClawBio skill from scratch in Google Colab — SKILL.md, Python, demo data, and validation.
---

# Build a Skill

<div class="tutorial-card__header">
  <span class="difficulty-badge difficulty-badge--intermediate">Intermediate</span>
  <span class="time-estimate">~30 min</span>
</div>

**No installation required.** This tutorial runs entirely in Google Colab. You will create a complete ClawBio skill: write the SKILL.md contract, add a Python implementation, create demo data, and validate everything works.

!!! tip "Also works locally"
    Every code cell below works in a terminal too. Just remove the `!` prefix and `%%writefile` magic.

---

## 1. Setup

Open a new Google Colab notebook and install ClawBio:

```python
!git clone https://github.com/ClawBio/ClawBio.git
%cd ClawBio
!pip install -q -r requirements.txt
```

## 2. Create Your Skill Directory

Pick a name for your skill. Skill names are lowercase with hyphens:

```python
!mkdir -p skills/my-awesome-skill
```

## 3. Write the SKILL.md

```python
%%writefile skills/my-awesome-skill/SKILL.md
---
name: my-awesome-skill
version: 0.1.0
author: Your Name <you@example.com>
domain: genomics
description: One-line description of what this skill does
license: MIT

inputs:
  - name: input_file
    type: file
    format: [vcf, csv, tsv, txt]
    description: Input data file
    required: true

outputs:
  - name: report
    type: file
    format: md
    description: Analysis report

dependencies:
  python: ">=3.11"
  packages:
    - pandas>=2.0
    - numpy>=1.24

tags: [genomics, variants, your-tags-here]

demo_data:
  - path: demo_input.txt
    description: Synthetic test data with 50 variants

endpoints:
  cli: python skills/my-awesome-skill/my_skill.py --input {input_file} --output {output_dir}
---

## Domain Decisions

Document the scientific choices your skill makes — the decisions
a domain expert would make that an AI agent should NOT override.

- **Threshold for significance**: p < 0.05 after Bonferroni correction
- **Reference database**: ClinVar (release 2025-12)
- **Population frequency filter**: exclude variants with gnomAD AF > 0.01

## Safety Rules

- Never report a clinical diagnosis; always include the research-use disclaimer
- Flag DPYD*2A carriers with an urgent warning (fluorouracil toxicity risk)
- Do not extrapolate results across ancestries unless the model was trained on that population

## Agent Boundary

The agent (LLM) dispatches and explains. The skill (Python) executes.
The agent must NOT override thresholds, invent gene-drug associations,
or skip safety warnings defined in this SKILL.md.
```

## 4. Add Demo Data

Create a small synthetic dataset so anyone can test your skill:

```python
%%writefile skills/my-awesome-skill/demo_input.txt
# Synthetic demo data for my-awesome-skill
# This is NOT real patient data
rsid	chromosome	position	genotype
rs1234567	1	12345678	AG
rs2345678	2	23456789	CC
rs3456789	3	34567890	TT
```

!!! warning "Demo data must be synthetic"
    Never commit real patient data. Generate synthetic variants that exercise
    your skill's logic without containing identifiable information.

## 5. Write the Python Implementation

```python
%%writefile skills/my-awesome-skill/my_skill.py
#!/usr/bin/env python3
"""My Awesome Skill — one-line description."""

import argparse
import json
from pathlib import Path

import pandas as pd


def run(input_path: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load input data
    df = pd.read_csv(input_path, sep="\t", comment="#")
    print(f"✓ Loaded {len(df)} variants from {input_path.name}")

    # --- Your analysis logic here ---
    results = {"variants_loaded": len(df), "status": "complete"}

    # Write report
    report_path = output_dir / "report.md"
    report_path.write_text(
        f"# My Awesome Skill Report\n\n"
        f"Processed **{len(df)} variants**.\n\n"
        f"*ClawBio is a research tool. Not a medical device.*\n"
    )
    print(f"✓ Report written to {report_path}")

    # Write structured output
    summary_path = output_dir / "summary.json"
    summary_path.write_text(json.dumps(results, indent=2))
    print(f"✓ Summary written to {summary_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="My Awesome Skill")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    run(args.input, args.output)
```

## 6. Test It

```python
!python3 skills/my-awesome-skill/my_skill.py \
  --input skills/my-awesome-skill/demo_input.txt \
  --output /tmp/my-skill-demo
```

Check the output:

```python
!cat /tmp/my-skill-demo/report.md
!cat /tmp/my-skill-demo/summary.json
```

## 7. Validate Your SKILL.md

Check that the SKILL.md parses correctly:

```python
import yaml
from pathlib import Path

skill_path = Path('skills/my-awesome-skill/SKILL.md')
text = skill_path.read_text()
front = text.split('---')[1]
meta = yaml.safe_load(front)

required = ['name', 'version', 'author', 'domain', 'description', 'inputs', 'outputs']
missing = [f for f in required if f not in meta]
if missing:
    print(f'Missing fields: {missing}')
else:
    print(f'SKILL.md valid: {meta["name"]} v{meta["version"]}')
```

## 8. Submit Your Skill

Once your skill works, submit it to the ClawBio repository. From a local terminal (or Colab):

```python
# Fork ClawBio on GitHub first, then:
!git checkout -b skill/my-awesome-skill
!git add skills/my-awesome-skill/
!git commit -m "Add my-awesome-skill"
# Push to your fork and open a pull request on GitHub
```

See [Contributing](../contributing/index.md) for PR guidelines.

---

**Next:** [Variant Interpretation Workshop](variant-interpretation-workshop.md) — analyse a real genome hands-on.
