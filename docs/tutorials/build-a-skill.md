---
title: "Build a Skill"
description: Create a complete ClawBio skill from scratch — SKILL.md, Python, demo data, and validation.
---

# Build a Skill

<div class="tutorial-card__header">
  <span class="difficulty-badge difficulty-badge--intermediate">Intermediate</span>
  <span class="time-estimate">~30 min</span>
</div>

In this tutorial you'll create a complete ClawBio skill: write the SKILL.md contract, add a Python implementation, create demo data, and validate everything works.

---

## 1. Create Your Skill Directory

Pick a name for your skill. Skill names are lowercase with hyphens:

```bash
cd ClawBio
mkdir -p skills/my-awesome-skill
```

## 2. Write the SKILL.md

Copy the template and customise it:

```bash
cp templates/SKILL-TEMPLATE.md skills/my-awesome-skill/SKILL.md
```

Open `skills/my-awesome-skill/SKILL.md` and fill in:

### YAML Frontmatter

```yaml
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
```

### Markdown Body

Below the frontmatter, write three required sections:

```markdown
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

## 3. Add Demo Data

Create a small synthetic dataset so anyone can test your skill:

```bash
cat > skills/my-awesome-skill/demo_input.txt << 'EOF'
# Synthetic demo data for my-awesome-skill
# This is NOT real patient data
rsid	chromosome	position	genotype
rs1234567	1	12345678	AG
rs2345678	2	23456789	CC
rs3456789	3	34567890	TT
EOF
```

!!! warning "Demo data must be synthetic"
    Never commit real patient data. Generate synthetic variants that exercise
    your skill's logic without containing identifiable information.

## 4. Write the Python Implementation

Create `skills/my-awesome-skill/my_skill.py`:

```python
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

## 5. Test It

```bash
python skills/my-awesome-skill/my_skill.py \
  --input skills/my-awesome-skill/demo_input.txt \
  --output /tmp/my-skill-demo
```

Check the output:

```bash
cat /tmp/my-skill-demo/report.md
cat /tmp/my-skill-demo/summary.json
```

## 6. Validate Your SKILL.md

Check that the SKILL.md parses correctly:

```bash
python -c "
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
    print(f'SKILL.md valid: {meta[\"name\"]} v{meta[\"version\"]}')
"
```

## 7. Submit Your Skill

Once your skill works locally, submit it to the ClawBio repository:

```bash
git checkout -b skill/my-awesome-skill
git add skills/my-awesome-skill/
git commit -m "Add my-awesome-skill"
git push origin skill/my-awesome-skill
```

Then open a pull request on GitHub. See [Contributing](../contributing/index.md) for PR guidelines.

---

**Next:** [Telegram Bot](telegram-bot.md) — deploy a bot that runs your skills from Telegram.
