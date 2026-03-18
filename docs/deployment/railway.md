---
title: Railway
description: Deploy ClawBio to Railway for managed cloud hosting.
---

# Railway Deployment

[Railway](https://railway.app) provides managed cloud hosting with GitHub integration. Deploy ClawBio with a few clicks — no Dockerfile required.

---

## 1. Connect Your Repository

1. Sign up at [railway.app](https://railway.app) and link your GitHub account
2. Click **New Project → Deploy from GitHub Repo**
3. Select your ClawBio fork or the `ClawBio/ClawBio` repository

Railway auto-detects Python projects and installs `requirements.txt` dependencies.

## 2. Set Environment Variables

In the Railway dashboard, go to **Variables** and add:

| Variable | Value |
|---|---|
| `LLM_API_KEY` | Your LLM provider API key |
| `LLM_BASE_URL` | Provider endpoint (optional — defaults to OpenAI) |
| `CLAWBIO_MODEL` | Model name (e.g. `gemini-2.0-flash`) |
| `TELEGRAM_BOT_TOKEN` | From @BotFather |
| `RATE_LIMIT_PER_HOUR` | `10` (or your preferred limit) |

!!! tip "Use Google Gemini for free hosting"
    Pair Railway's free tier with Gemini's free API (1,500 req/day) for a zero-cost bot deployment.

## 3. Configure the Start Command

In **Settings → Deploy**, set the start command:

```bash
python3 bot/roboterri.py
```

Or for Discord:

```bash
python3 bot/roboterri_discord.py
```

## 4. Persistent Storage

By default, Railway containers are ephemeral — files written during a session are lost on redeploy. For persistent skill output:

1. Go to **New → Database → Volume**
2. Mount the volume at `/app/results`
3. Configure skills to write output to `/app/results`

This keeps genomic reports and analysis results across deploys.

## 5. Custom Domains

1. Go to **Settings → Networking → Custom Domain**
2. Add your domain (e.g. `bot.clawbio.ai`)
3. Add the CNAME record Railway provides to your DNS

## 6. Monitoring

Railway provides built-in logging and metrics:

- **Logs**: Real-time stdout/stderr from your bot
- **Metrics**: CPU, memory, and network usage
- **Deploy history**: Rollback to any previous deployment

## Cost Considerations

| Plan | Included | Overage |
|---|---|---|
| Hobby | $5/mo, 8 GB RAM, 8 vCPU | $0.000231/min |
| Pro | $20/mo, more resources | Usage-based |

A Telegram bot running ClawBio skills typically uses minimal resources — the LLM provider handles the heavy computation. The main cost is your LLM API usage, not Railway hosting.

## Example: Full Stack

Deploy the bot with a local Ollama instance for fully self-hosted LLM:

```
Railway project
├── clawbio (GitHub deploy)
│   ├── Start: python3 bot/roboterri.py
│   └── Env: LLM_BASE_URL=http://ollama:11434/v1
└── ollama (Docker image: ollama/ollama)
    └── Volume: /root/.ollama
```

!!! warning "GPU not available on Railway"
    Railway does not currently offer GPU instances. For ML-heavy skills (scRNA embedding, structure prediction), use [Docker with GPU passthrough](docker.md#gpu-passthrough) or a [private cloud](private-cloud.md) deployment.

---

**Next:** [Private Cloud](private-cloud.md) — self-hosted deployment for sensitive data.
