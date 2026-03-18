---
title: The Contributor Journey
description: From idea to DOI-minted, citeable skill in under an hour
---

# The Contributor Journey

The median time-to-skill is **under 1 hour**. Here is the step-by-step path from idea to published, DOI-minted skill.

## Step 1: Scaffold (~15 minutes)

```bash
clawbio init my-skill-name
```

This creates a skill directory with:

```
skills/my-skill-name/
  SKILL.md          # Pre-filled template with all required fields
  demo_data/        # Empty directory for demo inputs
  tests/            # Test harness stub
  my_skill_name.py  # Python implementation stub (optional)
```

Edit `SKILL.md` to fill in the YAML frontmatter: name, version, author, domain, inputs, outputs, guideline references.

## Step 2: Add Demo Data (~10 minutes)

Place representative input files in `demo_data/`. These should be:

- Small enough to run in seconds
- Realistic enough to demonstrate the skill's purpose
- Free of any real patient or sensitive data

## Step 3: Encode Domain Decisions (~20 minutes)

This is the core of a ClawBio skill. In the `SKILL.md` body sections, document:

- **Domain Decisions**: thresholds, classification rules, allele mappings, statistical parameters
- **Safety Rules**: what the skill must never do, when to defer to a human expert
- **Agent Boundary**: what questions this skill can and cannot answer

These decisions are what distinguish a ClawBio skill from a generic script wrapper.

## Step 4: Validate Locally (~5 minutes)

```bash
clawbio validate skills/my-skill-name/
```

The validator checks:

- SKILL.md schema compliance (all required fields present, correct types)
- Demo data exists and is loadable
- Python implementation passes tests (if provided)
- Safety rules section is non-empty
- No network calls or filesystem access outside declared paths

## Step 5: Publish (~5 minutes)

```bash
clawbio publish skills/my-skill-name/
```

This submits the skill to the ClawBio registry for review. The automated pipeline runs validation, and a domain reviewer checks the skill's scientific accuracy.

## Step 6: DOI Minting (Automatic)

Once approved, the skill is automatically:

- Assigned a **DOI** via Zenodo
- Listed in the **clawbio.ai registry**
- Discoverable via **MCP** for any agent framework
- Tracked for **citations** and **downloads**

## Credit and Recognition

| Benefit | Details |
|---------|---------|
| DOI | Persistent identifier for your skill, citeable in publications |
| Citation tracking | Track who uses and cites your skill |
| Leaderboard | Ranked by skill count, downloads, and citations |
| Badges | Contributor, reviewer, and domain expert badges on your profile |
| Co-authorship | Top contributors invited as co-authors on the platform paper |

## Example Timeline

| Time | Activity |
|------|----------|
| 0:00 | `clawbio init` |
| 0:15 | SKILL.md frontmatter complete |
| 0:25 | Demo data added |
| 0:45 | Domain decisions and safety rules written |
| 0:50 | `clawbio validate` passes |
| 0:55 | `clawbio publish` submitted |
| ~1:00 | Skill live on registry with DOI |
