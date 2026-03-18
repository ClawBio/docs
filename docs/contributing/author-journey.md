---
title: The Contributor Journey
description: From idea to merged skill in under an hour
---

# The Contributor Journey

You can go from idea to a merged ClawBio skill in under an hour. Here is the step-by-step path.

## Step 1: Scaffold (~15 minutes)

Create a skill directory and copy the template:

```bash
mkdir -p skills/my-skill-name
cp templates/SKILL-TEMPLATE.md skills/my-skill-name/SKILL.md
```

Edit `SKILL.md` to fill in the YAML frontmatter: name, version, author, domain, inputs, outputs, guideline references.

## Step 2: Add Demo Data (~10 minutes)

Create a small synthetic dataset in your skill directory. These should be:

- Small enough to run in seconds
- Realistic enough to demonstrate the skill's purpose
- Free of any real patient or sensitive data

## Step 3: Encode Domain Decisions (~20 minutes)

This is the core of a ClawBio skill. In the `SKILL.md` body sections, document:

- **Domain Decisions**: thresholds, classification rules, allele mappings, statistical parameters. Cite real sources.
- **Safety Rules**: what the skill must never do, when to defer to a human expert
- **Agent Boundary**: what questions this skill can and cannot answer

These decisions are what distinguish a ClawBio skill from a generic script wrapper.

## Step 4: Implement and Test (~15 minutes)

Write the Python implementation (see the [hackathon guide](/hackathon/add-python/) for the standard template). Then test:

```bash
python skills/my-skill-name/my_skill.py --demo --output /tmp/test_output
```

Verify the demo runs, the report generates, and the safety disclaimer is included.

## Step 5: Submit a PR

```bash
git checkout -b skill/my-skill-name
git add skills/my-skill-name/
git commit -m "Add skill: my-skill-name"
git push -u origin skill/my-skill-name
gh pr create --title "Add skill: my-skill-name" --body "Description of what this skill does"
```

A maintainer will review the domain correctness and code quality. Once approved and merged, the skill appears in the ClawBio catalog.

## Example Timeline

| Time | Activity |
|------|----------|
| 0:00 | Copy template, create directory |
| 0:15 | SKILL.md frontmatter complete |
| 0:25 | Demo data added |
| 0:45 | Domain decisions, safety rules, and Python implementation written |
| 0:50 | Demo runs successfully |
| 0:55 | PR submitted |
