---
title: Registry API
description: RESTful API for skill discovery and remote execution
---

# Registry API

!!! note
    The Registry API is under development and will launch in **Q2 2026**. This page documents the planned specification.

The ClawBio Registry API provides programmatic access to skill discovery, metadata retrieval, and remote execution.

## Base URL

```
https://api.clawbio.ai/v1
```

## Authentication

All API requests require an API key passed via the `Authorization` header:

```
Authorization: Bearer <your-api-key>
```

API keys are available from your ClawBio account dashboard.

## Endpoints

### List Skills

Retrieve a paginated list of skills with optional filtering.

```
GET /api/v1/skills
```

**Query Parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| `domain` | string | Filter by domain (e.g., `pharmacogenomics`) |
| `tier` | string | Filter by validation tier (`community`, `verified`, `clinical`) |
| `q` | string | Full-text search across skill names and descriptions |
| `page` | integer | Page number (default: 1) |
| `per_page` | integer | Results per page (default: 20, max: 100) |

**Response**

```json
{
  "skills": [
    {
      "name": "pharmgx-reporter",
      "version": "2.1.0",
      "author": "Manuel Corpas",
      "domain": "pharmacogenomics",
      "description": "Pharmacogenomics report from 23andMe/AncestryDNA/VCF data",
      "guideline_authority": "CPIC",
      "validation_tier": "verified",
      "doi": "10.5281/zenodo.12345678",
      "endpoints": ["cli", "mcp", "http"],
      "downloads": 1542,
      "updated_at": "2026-03-01T12:00:00Z"
    }
  ],
  "total": 200,
  "page": 1,
  "per_page": 20
}
```

### Get Skill Metadata

Retrieve full metadata for a specific skill.

```
GET /api/v1/skills/{skill_name}
```

**Response**

Returns the complete SKILL.md frontmatter as JSON, plus download statistics and version history.

### Run a Skill

Execute a skill remotely with provided input data.

```
POST /api/v1/run/{skill_name}
```

**Request Body**

```json
{
  "input": "<base64-encoded input data>",
  "input_format": "txt",
  "output_format": "json",
  "parameters": {
    "weights": "0.35,0.25,0.20,0.20"
  }
}
```

**Response**

```json
{
  "status": "success",
  "skill": "pharmgx-reporter",
  "version": "2.1.0",
  "output": {
    "report": "<base64-encoded output>",
    "format": "json",
    "checksum": "sha256:abc123..."
  },
  "execution_time_ms": 2340,
  "disclaimer": "ClawBio is a research and educational tool. It is not a medical device and does not provide clinical diagnoses."
}
```

### Error Responses

| Status Code | Description |
|-------------|-------------|
| 400 | Invalid input format or missing required parameters |
| 401 | Missing or invalid API key |
| 404 | Skill not found |
| 422 | Input validation failed (e.g., too few variants) |
| 429 | Rate limit exceeded |
| 500 | Internal execution error |

```json
{
  "error": "validation_failed",
  "message": "Input file contains fewer than 10 variants (insufficient data)",
  "skill": "pharmgx-reporter"
}
```

## Rate Limits

| Tier | Requests/min | Executions/day |
|------|-------------|----------------|
| Free | 60 | 100 |
| Pro | 300 | 10,000 |
| Enterprise | Custom | Custom |

## SDK

No SDK is required. The API uses standard REST conventions with JSON payloads. Any HTTP client (curl, requests, fetch) works.
