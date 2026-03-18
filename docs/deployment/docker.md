---
title: Docker
description: Containerise ClawBio with Docker and docker-compose.
---

# Docker Deployment

Run ClawBio in a container for reproducible, isolated deployments. This guide covers Dockerfile patterns, docker-compose for multi-skill setups, and GPU passthrough.

---

## Dockerfile Pattern

A typical Dockerfile for ClawBio:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git curl && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the full ClawBio repo
COPY . .

# Default: run the bot
CMD ["python3", "bot/roboterri.py"]
```

!!! note
    This Dockerfile is an example pattern — it is not committed to the ClawBio repository. Adapt it to your needs.

## docker-compose for Multi-Skill Setups

Run ClawBio alongside supporting services:

```yaml
version: "3.8"

services:
  clawbio:
    build: .
    env_file: .env
    volumes:
      - ./data:/app/data          # Genomic input data
      - ./results:/app/results    # Skill output
    ports:
      - "8080:8080"
    restart: unless-stopped

  # Optional: local LLM with Ollama
  ollama:
    image: ollama/ollama
    volumes:
      - ollama-models:/root/.ollama
    ports:
      - "11434:11434"

volumes:
  ollama-models:
```

## Volume Mounts

| Mount | Purpose |
|---|---|
| `./data:/app/data` | Input genomic files (VCF, 23andMe .txt, FASTQ) |
| `./results:/app/results` | Skill output (reports, figures, JSON) |
| `./skills:/app/skills` | Custom skills (mount for live development) |

## Environment Variables

Pass your `.env` file or set variables directly:

```bash
docker run --env-file .env \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/results:/app/results \
  clawbio
```

Key environment variables:

| Variable | Description | Example |
|---|---|---|
| `LLM_API_KEY` | API key for your LLM provider | `sk-...` |
| `LLM_BASE_URL` | OpenAI-compatible endpoint | `https://api.openai.com/v1` |
| `CLAWBIO_MODEL` | Model to use | `gpt-4o` |
| `TELEGRAM_BOT_TOKEN` | Telegram bot token | From @BotFather |
| `RATE_LIMIT_PER_HOUR` | Per-user rate limit | `10` |

## GPU Passthrough

For ML-heavy skills (scRNA embedding, structure prediction), pass through your GPU:

### NVIDIA

```bash
docker run --gpus all --env-file .env clawbio
```

Requires [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) installed on the host.

### docker-compose with GPU

```yaml
services:
  clawbio:
    build: .
    env_file: .env
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
```

## Building and Running

```bash
# Build
docker build -t clawbio .

# Run interactively
docker run -it --env-file .env clawbio

# Run a specific skill
docker run --env-file .env clawbio \
  python skills/pharmgx-reporter/pharmgx_reporter.py \
  --input data/patient.txt --output results/

# Run in background
docker compose up -d
```

## Health Checks

Add a health check to your Dockerfile:

```dockerfile
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
  CMD python -c "import clawbio; print('ok')" || exit 1
```

---

**Next:** [Railway](railway.md) — deploy to the cloud with one click.
