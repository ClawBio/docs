---
title: Framework Integration
description: How agent framework authors can integrate ClawBio skills
---

# Framework Integration

ClawBio skills are designed to be called from any agent framework. No custom SDK is required -- skills are accessible through three standard endpoints.

## For Agent Framework Authors

Integrating ClawBio into your agent framework takes three steps:

### 1. Read the Registry API Docs

The [Registry API](/reference/api) provides programmatic access to skill discovery and metadata. Use it to:

- List available skills with filtering by domain, validation tier, or keyword
- Retrieve full SKILL.md metadata for any skill
- Check skill versions and update status

### 2. Add ClawBio as an MCP Server

The simplest integration path is via the [Model Context Protocol](/reference/mcp). Every ClawBio skill auto-registers as an MCP tool. Your framework can:

- Discover available skills through MCP tool listing
- Read skill metadata (inputs, outputs, domain decisions, safety rules)
- Invoke skills and receive structured responses

### 3. Or Call via CLI / HTTP

If MCP is not suitable for your framework, skills are also callable via:

- **CLI**: direct Python script invocation with standard arguments
- **HTTP**: REST API for remote execution (available Q4 2026)

## Three Endpoints

| Endpoint | When to Use | Availability |
|----------|-------------|--------------|
| **CLI** | Local execution, scripting, CI/CD pipelines | Now |
| **MCP** | Agent frameworks with MCP support | Q2 2026 |
| **HTTP** | Web applications, remote execution, serverless | Q4 2026 |

### CLI Example

```bash
# Discover skills
python skills/bio-orchestrator/orchestrator.py --list-skills

# Run a skill
python skills/pharmgx-reporter/pharmgx_reporter.py \
  --input patient_data.txt --output /tmp/report
```

### MCP Example

```json
{
  "method": "tools/call",
  "params": {
    "name": "clawbio-pharmgx-reporter",
    "arguments": {
      "input": "patient_data.txt",
      "output": "/tmp/report"
    }
  }
}
```

### HTTP Example (Q4 2026)

```bash
curl -X POST https://api.clawbio.ai/v1/run/pharmgx-reporter \
  -H "Authorization: Bearer $CLAWBIO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"input": "base64-encoded-data", "output_format": "json"}'
```

## No SDK Required

ClawBio deliberately avoids requiring a custom SDK. The integration surface is:

- **SKILL.md**: a plain Markdown file with YAML frontmatter (machine-readable metadata)
- **CLI**: standard Python scripts with `--input`, `--output`, and `--demo` flags
- **MCP**: standard Model Context Protocol
- **HTTP**: standard REST API with JSON payloads

This means any framework that can read files, run shell commands, or make HTTP requests can integrate ClawBio skills without installing anything.

## Integration Checklist

- [ ] Read [Registry API](/reference/api) documentation
- [ ] Choose your endpoint (CLI, MCP, or HTTP)
- [ ] Implement skill discovery (list available skills)
- [ ] Implement skill invocation (call with inputs, receive outputs)
- [ ] Handle safety rules (display disclaimers from SKILL.md)
- [ ] Test with demo data (`--demo` flag)
