---
title: Galaxy Bridge
description: Galaxy tool integration for NGS pipelines
---

# Galaxy Bridge

Search, inspect, and run tools on a Galaxy server (usegalaxy.org) from the ClawBio CLI. Browse tool categories, view tool details, and execute NGS workflows without leaving your terminal.

## Quick Demo

```bash
python skills/galaxy-bridge/galaxy_bridge.py --demo
```

## CLI Reference

```bash
# Search for tools
python skills/galaxy-bridge/galaxy_bridge.py \
  --search "metagenomics profiling"

# List tool categories
python skills/galaxy-bridge/galaxy_bridge.py \
  --list-categories

# Get tool details
python skills/galaxy-bridge/galaxy_bridge.py \
  --tool-details <tool_id>

# Run a tool
python skills/galaxy-bridge/galaxy_bridge.py \
  --run <tool_id> \
  --input <file> \
  --output <dir>

# Demo mode (offline FastQC example)
python skills/galaxy-bridge/galaxy_bridge.py --demo
```

| Argument | Required | Description |
|----------|----------|-------------|
| `--search` | No | Search Galaxy toolshed by keyword |
| `--list-categories` | No | List all available tool categories |
| `--tool-details` | No | Show full details for a tool ID |
| `--run` | No | Execute a Galaxy tool by ID |
| `--input` | No | Input file for tool execution |
| `--output` | No | Output directory for results |
| `--demo` | No | Run offline FastQC demo |

## Output

- Search results with tool IDs, descriptions, and versions
- Tool detail pages with parameter schemas
- Execution results downloaded to the output directory
- Demo mode outputs a pre-cached FastQC report
