---
title: MCP Integration
description: How ClawBio skills register as MCP tools for agent framework discovery and invocation
---

# MCP Integration

Every ClawBio skill automatically registers as a [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) tool. This allows any MCP-compatible agent framework to discover, inspect, and invoke ClawBio skills without custom integration code.

## How It Works

### Discovery

When an agent framework connects to ClawBio as an MCP server, it receives a list of all available skills as MCP tools. Each tool includes:

- **Name**: the skill identifier (e.g., `clawbio-pharmgx-reporter`)
- **Description**: what the skill does, drawn from the SKILL.md
- **Input schema**: required and optional parameters, derived from the SKILL.md `inputs` field
- **Metadata**: domain, guideline authority, validation tier

### Invocation

Agents invoke skills using the standard MCP `tools/call` method:

```json
{
  "method": "tools/call",
  "params": {
    "name": "clawbio-pharmgx-reporter",
    "arguments": {
      "input": "/path/to/patient_data.txt",
      "output": "/tmp/report"
    }
  }
}
```

### Response Format

Skills return structured responses via MCP:

```json
{
  "content": [
    {
      "type": "text",
      "text": "PharmGx report generated successfully."
    },
    {
      "type": "resource",
      "resource": {
        "uri": "file:///tmp/report/pharmgx_report.json",
        "mimeType": "application/json",
        "text": "{...}"
      }
    }
  ],
  "isError": false
}
```

## Connecting to ClawBio MCP Server

### Claude Code / Claude Desktop

Add ClawBio to your MCP configuration:

```json
{
  "mcpServers": {
    "clawbio": {
      "command": "python",
      "args": ["-m", "clawbio.mcp_server"],
      "env": {}
    }
  }
}
```

### Generic MCP Client

Connect to ClawBio's MCP server using any MCP-compatible client:

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command="python",
    args=["-m", "clawbio.mcp_server"]
)

async with stdio_client(server_params) as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()

        # List available skills
        tools = await session.list_tools()

        # Run a skill
        result = await session.call_tool(
            "clawbio-pharmgx-reporter",
            arguments={"input": "patient.txt", "output": "/tmp/report"}
        )
```

## Skill-to-MCP Mapping

| SKILL.md Field | MCP Tool Property |
|----------------|-------------------|
| `name` | `tool.name` (prefixed with `clawbio-`) |
| Description (body) | `tool.description` |
| `inputs` | `tool.inputSchema.properties` |
| `outputs` | Included in response `content` |
| `domain` | Custom metadata field |
| `guideline_authority` | Custom metadata field |
| `validation_tier` | Custom metadata field |

## Safety

- Skills execute locally -- no data leaves the machine
- The MCP server enforces the same safety rules defined in each SKILL.md
- The disclaimer from the SKILL.md is included in every response
- Sandboxed execution: skills cannot access filesystem paths outside their declared scope
