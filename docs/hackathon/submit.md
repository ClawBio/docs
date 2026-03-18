# Test and Submit (~10 minutes)

## 1. Run the Validation Check

Make sure your SKILL.md and Python script are correct:

```bash
# Validate SKILL.md structure
python -c "
import yaml
from pathlib import Path

skill = Path('skills/my-awesome-skill/SKILL.md').read_text()
front = skill.split('---')[1]
meta = yaml.safe_load(front)

checks = []
checks.append(('name' in meta, 'name field'))
checks.append(('version' in meta, 'version field'))
checks.append(('author' in meta, 'author field'))
checks.append(('domain' in meta, 'domain field'))
checks.append(('inputs' in meta, 'inputs field'))
checks.append(('outputs' in meta, 'outputs field'))
checks.append(('demo_data' in meta, 'demo_data field'))
checks.append(('## Domain Decisions' in skill, 'Domain Decisions section'))
checks.append(('## Safety Rules' in skill, 'Safety Rules section'))
checks.append(('## Agent Boundary' in skill, 'Agent Boundary section'))

for ok, label in checks:
    status = 'PASS' if ok else 'FAIL'
    print(f'  [{status}] {label}')

failed = [label for ok, label in checks if not ok]
if failed:
    print(f'\n{len(failed)} check(s) failed. Fix these before submitting.')
else:
    print('\nAll checks passed!')
"
```

## 2. Test Demo Mode

```bash
python skills/my-awesome-skill/my_skill.py --demo --output /tmp/submission_test
```

Verify:

- [ ] Script runs without errors
- [ ] `report.md` is generated in the output directory
- [ ] Report contains the safety disclaimer
- [ ] No real patient data in demo files or output

## 3. Check Your Files

Your skill directory should look like this:

```
skills/my-awesome-skill/
  SKILL.md            # Required: skill definition
  my_skill.py         # Required: Python implementation
  demo_input.txt      # Required: synthetic demo data
  figures/            # Optional: generated plots
  tests/              # Optional: pytest tests
    test_my_skill.py
```

## 4. Fork and Branch

```bash
# If you haven't already forked
gh repo fork ClawBio/ClawBio --clone

# Create a feature branch
git checkout -b skill/my-awesome-skill

# Add your files
git add skills/my-awesome-skill/
git commit -m "Add my-awesome-skill: one-line description"

# Push
git push -u origin skill/my-awesome-skill
```

## 5. Open a Pull Request

```bash
gh pr create \
  --title "Add skill: my-awesome-skill" \
  --body "## New Skill

- **Name**: my-awesome-skill
- **Domain**: genomics
- **Description**: One-line description

## Checklist
- [x] SKILL.md with frontmatter and all three sections
- [x] Python script with --demo flag
- [x] Synthetic demo data (no real patient data)
- [x] Safety disclaimer in report output
- [x] Demo runs successfully

## Demo output
\`\`\`
paste your demo output here
\`\`\`
"
```

## What Happens Next

1. **CI runs**: automated tests check your SKILL.md structure and demo execution
2. **Review**: a maintainer reviews domain correctness and code quality
3. **Merge**: once approved, your skill is live in the ClawBio catalog

## Tips for a Strong Submission

- **Domain decisions matter most**. Judges weight these at 40%. Cite real papers, guidelines, or databases for your thresholds.
- **Demo data should exercise edge cases**. Include at least one variant that triggers a warning or special handling.
- **Keep it focused**. A skill that does one thing well beats a skill that does three things poorly.
- **Add a figure**. Visual output makes your skill more compelling and earns bonus points.

---

Good luck! If you get stuck, ask in [GitHub Discussions](https://github.com/ClawBio/ClawBio/discussions) or [Discord](https://discord.gg/clawbio).
