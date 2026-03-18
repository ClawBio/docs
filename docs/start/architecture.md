---
title: Architecture
description: How ClawBio skills are discovered, selected, and executed
---

# Architecture

## Execution Flow

```
User request → Agent reads SKILL.md metadata → Selects skill → Invokes endpoint → Deterministic Python execution → Reproducibility bundle returned
```

The agent's role is strictly **dispatch and presentation**. It parses the user's natural language request, matches it against skill metadata (domain tags, input types), confirms the input file format, invokes the skill via one of three endpoints, and presents the output. All domain computation runs in deterministic Python inside the skill.

## Three Invocation Endpoints

Every ClawBio skill exposes up to three endpoints:

### 1. CLI (Local)

```bash
python pharmgx_reporter.py --input file.txt --output report/
```

Zero network dependency. Genomic data never leaves the device.

### 2. MCP (Protocol)

Agent sends a standard MCP `tool_call` to the ClawBio MCP server, which routes to the skill's Python code. Works with Claude Desktop, Cursor, any MCP host.

### 3. HTTP API (Hosted, Optional)

```
POST https://clawbio.ai/api/v1/run/{skill_name}
```

Ephemeral UK-hosted compute. Data deleted after run. For teams preferring not to run locally.

## Discovery and Selection

### Registry API

```
GET https://clawbio.ai/api/v1/skills?domain=pharmacogenomics&input_type=vcf
```

Returns a JSON array of matching skills with metadata.

### MCP Discovery

Every skill on the hub registers as an MCP tool. Any MCP-compatible host auto-discovers available skills.

### JSON Schema for Agent Frameworks

SKILL.md metadata is projected into a minimal JSON schema:

```json
{
  "name": "pharmgx-reporter",
  "version": "2.1.0",
  "domain": ["pharmacogenomics", "clinical-genetics"],
  "inputs": [{"name": "genotype_file", "type": ["23andme_v5", "vcf"]}],
  "outputs": [{"name": "report/", "type": "reproducibility_bundle"}],
  "endpoints": {
    "cli": "python pharmgx_reporter.py --input {genotype_file}",
    "mcp": "clawbio/pharmgx-reporter",
    "http": "https://clawbio.ai/api/v1/run/pharmgx-reporter"
  },
  "validation_tier": "verified",
  "guideline_version": "CPIC-2024-01",
  "doi": "10.5281/zenodo.XXXXXXX"
}
```

## The Agent Boundary

The agent does **not** reason about biology. The SKILL.md does.

| Component | Role |
|-----------|------|
| **LLM/Agent** | Parse request, select skill, confirm format, present output |
| **SKILL.md** | Domain decisions, safety rules, guideline versions |
| **Python code** | Extract SNPs, call alleles, map phenotypes, statistical analysis |

## Ecosystem Integration

ClawBio integrates rather than competes:

- **Galaxy**: Tool interop via EDAM + RO-Crate
- **MCP**: Every skill is an MCP server
- **Cloud providers**: Hosted execution on AWS eu-west-2
- **Workflow languages**: Complement CWL/Nextflow by adding the domain-decision layer they lack
