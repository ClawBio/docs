---
title: "Your First Skill"
description: Create a SKILL.md file that defines your skill's contract.
---

# Your First Skill

<div class="tutorial-card__header">
  <span class="difficulty-badge difficulty-badge--beginner">Beginner</span>
  <span class="time-estimate">~20 min</span>
</div>

Every ClawBio skill starts with a SKILL.md file — the contract that tells agents what your skill does, what inputs it needs, and what domain decisions it encodes.

---

## 1. Create Your Skill Directory

```bash
mkdir -p skills/my-awesome-skill
```

## 2. Copy the Template

```bash
cp templates/SKILL-TEMPLATE.md skills/my-awesome-skill/SKILL.md
```

## 3. Edit SKILL.md

Open `skills/my-awesome-skill/SKILL.md` in your editor. The file has two parts:

### YAML Frontmatter

Fill in the metadata block at the top:

```yaml
---
name: my-awesome-skill
version: 0.1.0
author: Your Name <you@example.com>
domain: genomics           # or: pharmacogenomics, clinical, population-genetics, multi-omics
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

Below the frontmatter, write three sections:

```markdown
## Domain Decisions

Document the scientific choices your skill makes. These are the decisions
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

Create a small synthetic dataset so anyone can test your skill without real patient data:

```bash
# Example: create a simple demo input file
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

## 5. Validate Your SKILL.md

Check that your SKILL.md is well-formed:

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

---

Next: [Add Python Implementation](add-python.md).
