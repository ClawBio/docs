---
title: "Agent Package Manager (APM)"
description: Dependency manager for AI context — declare, version, and inject context modules automatically.
---

# Agent Package Manager (APM)

<div class="tutorial-card__header">
  <span class="difficulty-badge difficulty-badge--advanced">Advanced</span>
  <span class="time-estimate">~30 min</span>
</div>

APM is a dependency manager for AI agent context, built by Microsoft. Think **npm or pip, but for prompts, instructions, and agent configurations**.

---

## The Problem

Without APM, teams end up with:

- **Ad-hoc prompting** — everyone writes their own system prompts, results vary wildly
- **Manual sharing** — "copy this YAML into `~/.opencode/skills/`" doesn't scale
- **Vendor lock-in** — a set of rules written for Claude Code won't work in Copilot or Cursor
- **No versioning** — when a shared prompt improves, everyone has to re-copy it

APM solves this with a single manifest file (`apm.yml`) that declares what context your project depends on, and a compile step that generates the right config files for whichever AI tool you use.

---

## How It Works

```
apm.yml                  <- declare dependencies
    | apm install
apm_modules/             <- downloaded packages (like node_modules/)
    | apm compile
AGENTS.md + CLAUDE.md    <- auto-generated config for each AI tool
```

1. **`apm.yml`** — your manifest. Lists packages (prompts, skills, instructions) your project needs.
2. **`apm install`** — pulls packages from GitHub into `apm_modules/`.
3. **`apm compile`** — scans your project and installed packages, then generates optimised context files:
   - `AGENTS.md` for GitHub Copilot, Cursor, Codex, Gemini
   - `CLAUDE.md` for Claude Code

The compile step deduplicates, orders by proximity, and strips irrelevant context so you're not wasting tokens.

---

## Install APM

```bash
# Quick install (recommended)
curl -sSL https://raw.githubusercontent.com/microsoft/apm/main/install.sh | sh

# Or via Homebrew
brew install microsoft/apm/apm

# Or via pip
pip3 install apm-cli
```

Verify:

```bash
apm --version
```

---

## Initialise a Project

```bash
cd your-project
apm init
```

This creates:

- `apm.yml` — your manifest
- `SKILL.md` — describes your package if you want to share it
- `.apm/` — directory for instructions, prompts, and agent definitions

---

## The `apm.yml` Manifest

Here's a minimal example for a life-sciences project:

```yaml
name: my-genomics-project
version: 0.1.0
description: scRNA-seq analysis pipeline

dependencies:
  apm:
    - github/awesome-copilot/skills/commit-message   # reusable skill
    - microsoft/apm-sample-package                     # reference package
```

To add a dependency:

```bash
apm install owner/repo
```

This downloads the package into `apm_modules/` and adds it to `apm.yml`. An `apm.lock` file pins exact commit hashes — commit this for reproducible builds.

### Dependency formats

```yaml
dependencies:
  apm:
    - owner/repo                          # latest HEAD
    - owner/repo#v2.1.0                   # pinned tag
    - owner/repo#main                     # pinned branch
    - owner/repo/path/to/subdir           # monorepo subdirectory
    - ghe.company.com/owner/repo          # GitHub Enterprise
  mcp:
    - microsoft/azure-devops-mcp          # MCP server from GitHub registry
```

---

## Compile and Use

```bash
# Auto-detect which AI tools you use and generate their config files
apm compile

# Or target a specific tool
apm compile --target claude    # -> CLAUDE.md
apm compile --target vscode    # -> AGENTS.md
apm compile --target all       # -> both
```

Auto-detection logic: if your project has a `.claude/` folder, it generates `CLAUDE.md`. If it has `.github/`, it generates `AGENTS.md`. If both, it generates both.

After compiling, your AI tool picks up the generated file automatically — Claude Code reads `CLAUDE.md` on every session start, Copilot reads `AGENTS.md`.

---

## Writing Reusable Prompts

APM uses markdown files with YAML frontmatter. These live in `.apm/prompts/`:

```markdown
---
description: Differential expression analysis workflow
input: [dataset_path, condition_column]
---

# DESeq2 Analysis

Analyse ${input:dataset_path} for differential expression.

## Steps
1. Load the count matrix from ${input:dataset_path}
2. Set up the DESeq2 design using the ${input:condition_column} column
3. Run the analysis with default parameters
4. Generate MA plot and volcano plot
5. Export significant genes (padj < 0.05) to results/
```

Run it:

```bash
apm run deseq --param dataset_path="counts.csv" --param condition_column="treatment"
```

---

## Writing Instructions

Instructions are project-wide rules that get compiled into your context files. Store them in `.apm/instructions/`:

```markdown
<!-- .apm/instructions/data-standards.instructions.md -->

# Data Standards

- All input data must be in `data/raw/`, processed data in `data/processed/`
- Never modify raw data files
- Use Parquet for large dataframes, CSV only for outputs under 50MB
- Column names must be snake_case
- Include a data dictionary for every new dataset
```

These get folded into `CLAUDE.md` / `AGENTS.md` at compile time, so every AI tool in your project sees the same rules.

---

## Useful Commands

```bash
apm deps list              # show installed packages
apm deps tree              # dependency tree
apm compile --watch        # auto-recompile on changes
apm compile --dry-run      # preview without writing
apm mcp search "genomics"  # search MCP server registry
apm preview prompt.md      # render a prompt without executing
```

---

## Making Your Project APM-Compatible

Any Git repo becomes an APM package by adding one of:

- `apm.yml` — full APM package
- `SKILL.md` — lightweight skill package (no `apm.yml` needed)

---

## APM + What You Already Know

| Tutorial concept | APM equivalent |
|---|---|
| `~/.opencode/skills/` (manual copy) | `apm install` (versioned, one command) |
| `CLAUDE.md` (hand-written) | `apm compile --target claude` (auto-generated) |
| Sharing agents via "copy this file" | Publish as Git repo, `apm install owner/repo` |
| `PLAN.md` session handoff | Still manual — APM handles context, not workflow |

APM doesn't replace your workflow — it manages the **context** that feeds into it. Your `PLAN.md` and `/compact` habits all still apply. APM just makes the *rules, skills, and instructions* portable and versioned.

---

## Further Reading

- [microsoft/apm on GitHub](https://github.com/microsoft/apm) — source and full documentation
- [APM Manifesto](https://github.com/microsoft/apm/blob/main/MANIFESTO.md) — design philosophy
- [awesome-copilot](https://github.com/github/awesome-copilot) — community prompts and skills
- [Making Agents](making-agents.md) — custom agent configs guide
