---
title: Integrate a Framework
description: Connect your agent framework to ClawBio's skill registry and MCP bridge
---

# Integrate a Framework

ClawBio skills are framework-agnostic by design. This guide explains how to connect your agent framework to the ClawBio skill registry so your agents can discover and execute skills.

## Architecture

```
Your Agent Framework
        │
        ▼
  ClawBio Registry  ──▶  SKILL.md (contract)
        │
        ▼
  Python CLI skill  ──▶  --input / --output / --demo
```

Each skill exposes a standard CLI interface. Your framework needs to:

1. **Discover** skills from the registry
2. **Read** the SKILL.md to understand inputs, outputs, and domain rules
3. **Execute** the Python script with the correct arguments
4. **Capture** the output directory contents

## MCP Bridge

ClawBio provides an MCP (Model Context Protocol) server that exposes skills as tools. If your framework supports MCP, this is the simplest integration path:

```bash
# Start the MCP bridge
clawbio mcp serve

# Your MCP-compatible agent can now discover and call skills as tools
```

## Direct Integration

If your framework does not support MCP, integrate directly with the CLI:

```python
import subprocess
import json

def run_skill(skill_name, input_path, output_dir):
    """Execute a ClawBio skill and return the output path."""
    result = subprocess.run(
        ["python", f"skills/{skill_name}/{skill_name}.py",
         "--input", input_path,
         "--output", output_dir],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr)
    return output_dir
```

## Registry API

The skill registry provides metadata for discovery:

```python
from clawbio import registry

# List all available skills
skills = registry.list_skills()

# Get skill metadata (parsed from SKILL.md frontmatter)
meta = registry.get_skill("pharmgx-reporter")
print(meta["inputs"])   # Expected input formats
print(meta["outputs"])  # What the skill produces
```

## Testing Your Integration

```bash
# Verify your framework can discover skills
clawbio list

# Run a demo skill to test the execution path
python3 skills/pharmgx-reporter/pharmgx_reporter.py --demo --output /tmp/test

# Check output was produced
ls /tmp/test/
```

## Questions?

- Open a [GitHub Discussion](https://github.com/ClawBio/ClawBio/discussions)
- Join our [Discord](https://discord.gg/clawbio)
