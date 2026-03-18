---
title: "Context Management"
description: Understand context windows, cost scaling, and how to keep ClawBio agent runs cheap and accurate.
---

# Context Management

<div class="tutorial-card__header">
  <span class="difficulty-badge difficulty-badge--advanced">Advanced</span>
  <span class="time-estimate">~20 min</span>
</div>

Long agent sessions fill the context window, burying your instructions under noise. The model forgets your conventions, hallucinates file contents, and every reply costs more. This tutorial explains how to manage context effectively when running ClawBio skills.

---

## What Is Context?

Every message re-sends the **entire conversation** to the API — your rules, all previous messages, every tool output. This bundle is the **context window**, measured in tokens (~0.75 words each).

**What fills it:**

- **System prompt / CLAUDE.md** — fixed overhead every session
- **Chat history** — grows ~1k tokens per turn
- **File reads** — one 500-line file ≈ 3k tokens
- **Bash/test output** — a single stack trace ≈ 5k–20k tokens (the silent killer)
- **Web search results** — 5k–10k per search

## Context Rot and Cost

**Context rot** happens past ~70% capacity: early instructions get buried, the model attends to recent noise over old rules, and hallucinations increase.

**Cost scales linearly** — every message re-sends the full window.

| Model | $/MTok input | Context window | Cost at 50k | Cost at 150k |
|---|---|---|---|---|
| GPT-4o mini | $0.15 | 128k | $0.01 | $0.02 |
| Kimi K2.5 | $0.60 | 256k | $0.03 | $0.09 |
| Claude Haiku 4.5 | $1.00 | 200k | $0.05 | $0.15 |
| Claude Sonnet 4.6 | $3.00 | 200k | $0.15 | $0.45 |
| Claude Opus 4.6 | $5.00 | 200k | $0.25 | $0.75 |

50 messages at 150k tokens on Sonnet = **$22.50 in input costs alone**. Context management is a billing issue, not just a quality issue.

For up-to-date pricing, see [models.dev](https://models.dev/).

## Why This Matters for ClawBio

ClawBio skills generate substantial output — genomic reports, variant tables, pipeline logs. A typical multi-skill session can fill 50% of the context window in 10–15 turns. If you're chaining skills (e.g. PharmGx → NutriGx → Profile Report), context management becomes essential.

## The Solutions

### `/clear` — Full Reset

Resets the conversation entirely. Zero history, zero tool outputs, back to just the system prompt. Use it **between unrelated tasks** or when a session has gone off track.

### `/compact` — Summarise and Continue

Summarises the entire conversation into a structured digest (~5k tokens) and discards the raw history — typically a **97% reduction**. Unlike `/clear`, it preserves continuity: decisions, file states, and completed work survive in the summary.

| | `/clear` | `/compact` |
|---|---|---|
| History after | Gone | Summarised (~5k tokens) |
| When to use | Between tasks | Mid-task, keep continuity |
| Cost | Free | One summary call |

### Check Your Context

Use `/context` at any time to see how full the window is:

```
❯ /context

  Context Usage
  claude-sonnet-4-6 · 56k/200k tokens (28%)

  Estimated usage by category
  System prompt:   3.5k tokens  (1.7%)
  System tools:     21k tokens (10.5%)
  Messages:        28.2k tokens (14.1%)
  Free space:       140k tokens (69.8%)
```

## Best Practices for ClawBio Sessions

1. **One skill per session** when possible — run PharmGx, compact, then run NutriGx
2. **Compact after large outputs** — if a skill dumps a 500-line report into the context, compact before continuing
3. **Use `--output` flags** — write results to files instead of printing them all to the terminal
4. **Start fresh for unrelated tasks** — `/clear` is free and instant
5. **Watch for hallucinations** — if the agent starts inventing gene names or mixing up variant data, it's probably context rot

!!! warning "Auto-compact is not reliable"
    The automatic trigger at 80% only saves titles and brief excerpts — not full content. Use `/compact` manually before you hit that threshold.

---

**Further reading:** [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
