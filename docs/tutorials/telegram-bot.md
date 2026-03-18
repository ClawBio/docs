---
title: "Telegram Bot"
description: Set up the RoboTerri Telegram bot to run ClawBio skills from your phone.
---

# Telegram Bot

<div class="tutorial-card__header">
  <span class="difficulty-badge difficulty-badge--intermediate">Intermediate</span>
  <span class="time-estimate">~20 min</span>
</div>

Deploy **RoboTerri** — a Telegram bot that runs ClawBio bioinformatics skills using any LLM as the reasoning engine. Send genetic data, medication photos, or natural language questions and get personalised genomic reports back.

---

## Prerequisites

- Python 3.11+
- ClawBio cloned and working (`python3 clawbio.py run pharmgx --demo`)
- A Telegram account
- An API key from any OpenAI-compatible LLM provider

## 1. Install Bot Dependencies

```bash
cd ClawBio
pip install -r bot/requirements.txt
```

## 2. Create a Telegram Bot

1. Open Telegram and search for **@BotFather**
2. Send `/newbot`, choose a name and username
3. Save the **bot token** BotFather gives you

### Get your chat ID (optional)

The bot is open to all users by default. To identify yourself as admin (bypasses rate limits):

1. Start a conversation with your new bot
2. Send any message
3. Visit `https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates`
4. Find `"chat":{"id":123456789}` — that number is your chat ID

## 3. Configure Your LLM Provider

Create a `.env` file in the ClawBio root directory:

```bash
# Telegram
TELEGRAM_BOT_TOKEN=your-bot-token-here

# LLM provider
LLM_API_KEY=your-api-key-here
CLAWBIO_MODEL=gemini-2.0-flash

# Optional
TELEGRAM_CHAT_ID=your-chat-id-here
RATE_LIMIT_PER_HOUR=10
```

### Provider Examples

Any provider that speaks the OpenAI chat completions API works. Set `LLM_BASE_URL` to point to your provider:

=== "Google Gemini (free)"

    ```bash
    LLM_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
    LLM_API_KEY=your-google-api-key
    CLAWBIO_MODEL=gemini-2.0-flash
    ```

    Get a free API key at [aistudio.google.com/apikey](https://aistudio.google.com/apikey) — 1,500 requests/day.

=== "OpenAI"

    ```bash
    LLM_API_KEY=sk-...
    CLAWBIO_MODEL=gpt-4o
    ```

=== "Anthropic (via OpenRouter)"

    ```bash
    LLM_BASE_URL=https://openrouter.ai/api/v1
    LLM_API_KEY=sk-or-...
    CLAWBIO_MODEL=anthropic/claude-sonnet-4-5-20250929
    ```

=== "Ollama (local, free)"

    ```bash
    LLM_BASE_URL=http://localhost:11434/v1
    LLM_API_KEY=ollama
    CLAWBIO_MODEL=llama3.1
    ```

!!! tip "Vision and tool calling"
    Photo/drug detection requires a model with vision capabilities (e.g. GPT-4o, Claude Sonnet, Gemini Pro). Tool calling requires function calling support. Most major providers support both.

## 4. Run the Bot

```bash
python3 bot/roboterri.py
```

You should see:

```
🤖 RoboTerri is running...
```

## 5. Try It Out

Open your bot in Telegram and try these:

| Action | What happens |
|---|---|
| `/start` | Welcome message and available commands |
| `/skills` | List all available ClawBio skills |
| `/demo pharmgx` | Run PharmGx with demo data — returns a pharmacogenomics report |
| Send a `.txt` file | Analyses a 23andMe-format genetic file |
| Send a medication photo | Identifies the drug and checks for gene-drug interactions |
| Ask a question | Routes to the most relevant skill via the LLM |

## 6. Discord Support

RoboTerri also supports Discord. The setup is similar:

1. Create a bot at [discord.com/developers/applications](https://discord.com/developers/applications)
2. Enable **Message Content Intent** under Privileged Gateway Intents
3. Add to your `.env`:

```bash
DISCORD_BOT_TOKEN=your-discord-bot-token-here
DISCORD_CHANNEL_ID=your-channel-id-here
```

4. Run: `python3 bot/roboterri_discord.py`

Discord commands use `!` instead of `/` (e.g. `!demo pharmgx`).

## Security Notes

- All genetic data is processed locally — nothing leaves your machine
- Per-user rate limiting prevents abuse (default: 10 messages/hour)
- Never commit your `.env` file (already in `.gitignore`)

---

**Next:** [Context Management](context-management.md) — understand context windows and keep agent runs efficient.
