---
title: Framework Integration
description: How agent framework authors can integrate ClawBio skills
---

# Framework Integration

ClawBio skills are designed to be called from any agent framework. No custom SDK is required.

## For Agent Framework Authors

### 1. Discover Skills

List all available skills programmatically:

```bash
python skills/bio-orchestrator/orchestrator.py --list-skills
```

Or read `skills/catalog.json` for a machine-readable index of all skills with metadata.

### 2. Read SKILL.md

Each skill's `SKILL.md` contains structured YAML frontmatter with:

- **name, version, author**: identity
- **inputs/outputs**: what the skill accepts and produces
- **endpoints**: how to invoke it (CLI command)
- **domain**: what area of biology it covers
- **demo_data**: bundled test data for verification

### 3. Invoke via CLI

Every skill follows the same CLI pattern:

```bash
python skills/<skill-name>/<script>.py \
  --input <input_file> \
  --output <output_dir>

# Or with demo data:
python skills/<skill-name>/<script>.py --demo --output /tmp/test
```

### 4. Handle Safety Rules

Every skill's SKILL.md includes a Safety Rules section. Your framework should:

- Display the ClawBio disclaimer from the report output
- Not override thresholds or domain decisions defined in SKILL.md
- Not invent gene-drug associations or clinical interpretations

## No SDK Required

ClawBio deliberately avoids requiring a custom SDK. The integration surface is:

- **SKILL.md**: plain Markdown with YAML frontmatter (machine-readable metadata)
- **catalog.json**: JSON index of all skills
- **CLI**: standard Python scripts with `--input`, `--output`, and `--demo` flags

Any framework that can read files and run shell commands can integrate ClawBio skills.

## Integration Checklist

- [ ] Read `catalog.json` or run `--list-skills` to discover available skills
- [ ] Parse SKILL.md frontmatter for input/output schemas
- [ ] Invoke skills via CLI with appropriate arguments
- [ ] Display safety disclaimers from report output
- [ ] Test with demo data (`--demo` flag)
