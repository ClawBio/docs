---
title: ClawBio Documentation
description: Technical documentation, tutorials, and skill reference for ClawBio, the bioinformatics-native AI agent skill library.
---

<div class="hero">
  <h1 class="hero__title">ClawBio Documentation</h1>
  <p class="hero__subtitle">Run real genomics with an AI agent in about ten minutes. No coding experience needed.</p>
  <p>
    <a href="#start-here" class="md-button md-button--primary">Start here</a>
    &nbsp;
    <a href="tutorials/conversational-genome/" class="md-button">Try Conversational Genome</a>
    &nbsp;
    <a href="https://clawbio.ai" class="md-button">ClawBio Home</a>
    &nbsp;
    <a href="https://github.com/ClawBio/ClawBio" class="md-button">GitHub</a>
  </p>
</div>

## Start here { #start-here }

This is for a biologist who has never opened a terminal. You will install one AI agent, then let the agent install ClawBio and run your first analysis for you. Budget ten minutes.

!!! tip "What is an AI agent?"
    A chatbot answers questions. An agent also does things on your computer: it can install software, run programs and read the files they produce. You will type plain English and the agent will do the terminal work. Two good agents are Claude Code (Anthropic) and Codex (OpenAI). Pick whichever company you already have a paid account with; the free tiers do not include these agents.

### Step 1. Open a terminal

The terminal is the text window agents live in. You only need it to run three commands.

=== "Mac"

    Press ++cmd+space++, type **Terminal**, press ++enter++.

=== "Windows"

    Press the Windows key, type **PowerShell**, press ++enter++. Your prompt starts with `PS C:\`.

=== "Linux"

    Press ++ctrl+alt+t++, or open **Terminal** from your applications menu.

### Step 2. Install an agent

Copy one line, paste it into the terminal, press ++enter++, and wait for it to finish.

=== "Claude Code"

    Needs a Claude **Pro, Max, Team or Enterprise** account ([claude.ai](https://claude.ai)).

    **Mac and Linux**

    ```bash
    curl -fsSL https://claude.ai/install.sh | bash
    ```

    **Windows (PowerShell)**

    ```powershell
    irm https://claude.ai/install.ps1 | iex
    ```

    Close the terminal, open a new one, and check it worked:

    ```bash
    claude --version
    ```

    Prefer clicking to typing? The [Claude Code desktop app](https://claude.com/download) does the same job without a terminal.

=== "Codex"

    Needs a ChatGPT **Plus, Pro, Business or Enterprise** account ([chatgpt.com](https://chatgpt.com)).

    **Mac and Linux**

    ```bash
    curl -fsSL https://chatgpt.com/codex/install.sh | sh
    ```

    **Windows (PowerShell), or any machine that already has Node.js**

    ```powershell
    npm install -g @openai/codex
    ```

    Close the terminal, open a new one, and check it worked:

    ```bash
    codex --version
    ```

### Step 3. Make a folder and start the agent in it

Agents work inside one folder at a time. Make an empty one for your genomics work and start the agent there. The first start opens your browser to sign in; say yes.

=== "Claude Code"

    ```bash
    mkdir clawbio-lab
    cd clawbio-lab
    claude
    ```

=== "Codex"

    ```bash
    mkdir clawbio-lab
    cd clawbio-lab
    codex
    ```

### Step 4. Paste this prompt

Copy the whole block into the agent and press ++enter++. The agent installs Python if you do not have it, installs ClawBio, runs a pharmacogenomics report on bundled demo data, and explains the result. Approve each action it proposes.

```text
I am a biologist with no programming experience. Please set up ClawBio for me
and run its first demo, explaining what you are doing in plain language.

1. Check whether Python 3.11 or newer is installed. If it is not, install it
   for my operating system and confirm it works.
2. Install ClawBio with: pip install clawbio
3. Run: clawbio run pharmgx --demo
4. Open the report it produces and explain the findings to me as you would to
   a colleague: which genes were tested, what each result means, and what the
   reproducibility bundle is for.
5. Then run: clawbio list
   and tell me which three skills you think I should try next and why.
```

### Step 5. What you should see

In under two seconds after install, the PharmGx demo writes a report with CYP2D6, CYP2C19 and other drug-metabolism gene calls, a Markdown summary, and a `reproducibility/` folder holding the exact commands, environment and SHA-256 checksums. The agent will walk you through it. From here you can ask it anything in English: "run the GWAS PRS demo", "explain what a polygenic score is before you run it", "which of these skills works on my own 23andMe file".

!!! note "Where the skills live"
    Once ClawBio is installed, both agents can already run every skill through the `clawbio` command. Claude Code users can also load the skills as a plugin so the agent knows when to use each one without being told: type `/plugin marketplace add ClawBio/ClawBio` and then `/plugin install clawbio` inside Claude Code. Codex, Cursor and other editors that read [Agent Skills](https://agentskills.io) folders can copy any skill from `skills/` in the repository into `~/.agents/skills/`.

Next: [Step 1 of the ClawBio tutorial series](tutorials/run-your-first-skill.md) picks up from exactly this point.

## Quick install (already have Python?)

```bash
pip install clawbio                 # Python 3.11+
clawbio run pharmgx --demo
```

Prefer [conda](https://docs.conda.io/)? `conda install -c bioconda clawbio`.

Using [Claude Code](https://claude.com/claude-code)? Install the skills as a plugin:

```
/plugin marketplace add ClawBio/ClawBio
/plugin install clawbio
```

**Developing ClawBio, or want every skill with its full demo data?** Work from a source
checkout instead ([uv](https://docs.astral.sh/uv/) recommended):

```bash
git clone https://github.com/ClawBio/ClawBio.git && cd ClawBio
uv sync
uv run python clawbio.py run pharmgx --demo
```

<h2 class="section-heading">Explore</h2>


<div class="tutorial-cards">

<a class="tutorial-card" href="tutorials/conversational-genome/">
  <div class="tutorial-card__header">
    <span class="difficulty-badge difficulty-badge--beginner">Beginner</span>
    <span class="time-estimate">15 min</span>
  </div>
  <h3 class="tutorial-card__title">Try Conversational Genome</h3>
  <p class="tutorial-card__desc">Ask questions about a public genome in a hosted chat. No notebook setup. Includes live skill execution and precomputed findings, with limitations explained.</p>
</a>

<a class="tutorial-card" href="hackathon/berlin/">
  <div class="tutorial-card__header">
    <span class="difficulty-badge difficulty-badge--event">Past workshop</span>
    <span class="time-estimate">Tue 18 Aug 2026</span>
  </div>
  <h3 class="tutorial-card__title">ClawBio + Nebius Hackathon Berlin</h3>
  <p class="tutorial-card__desc">One day building agents that do real genomics, at Impact Hub Berlin. Free, lunch provided, Nebius credits for the best builds. Setup, tracks and running order.</p>
</a>

<a class="tutorial-card" href="tutorials/setup/">
  <div class="tutorial-card__header">
    <span class="difficulty-badge difficulty-badge--beginner">Beginner</span>
    <span class="time-estimate">10 min</span>
  </div>
  <h3 class="tutorial-card__title">Setup</h3>
  <p class="tutorial-card__desc">Install an AI coding agent, connect it to a model provider, and run your first prompt.</p>
</a>



<a class="tutorial-card" href="tutorials/build-a-skill/">
  <div class="tutorial-card__header">
    <span class="difficulty-badge difficulty-badge--intermediate">Intermediate</span>
    <span class="time-estimate">30 min</span>
  </div>
  <h3 class="tutorial-card__title">Build a Skill</h3>
  <p class="tutorial-card__desc">Write a SKILL.md, add Python implementation, and submit a PR.</p>
</a>

<a class="tutorial-card" href="skills/">
  <div class="tutorial-card__header">
    <span class="difficulty-badge difficulty-badge--tutorial">Reference</span>
  </div>
  <h3 class="tutorial-card__title">Skill Library</h3>
  <p class="tutorial-card__desc">Browse all available skills: pharmacogenomics, GWAS, scRNA-seq, equity scoring, and more.</p>
</a>

<a class="tutorial-card" href="presentations/">
  <div class="tutorial-card__header">
    <span class="difficulty-badge difficulty-badge--event">Slides</span>
  </div>
  <h3 class="tutorial-card__title">Presentations</h3>
  <p class="tutorial-card__desc">All ClawBio talks, workshops, and pitch decks in one place, newest first.</p>
</a>

<a class="tutorial-card" href="deployment/">
  <div class="tutorial-card__header">
    <span class="difficulty-badge difficulty-badge--intermediate">Intermediate</span>
  </div>
  <h3 class="tutorial-card__title">Deployment</h3>
  <p class="tutorial-card__desc">Deploy ClawBio via Docker, Railway, or private cloud.</p>
</a>

<a class="tutorial-card" href="tutorials/variant-interpretation-workshop/">
  <div class="tutorial-card__header">
    <span class="difficulty-badge difficulty-badge--beginner">Beginner</span>
    <span class="time-estimate">60 min</span>
  </div>
  <h3 class="tutorial-card__title">Variant Interpretation Workshop</h3>
  <p class="tutorial-card__desc">Annotate a real human genome in Google Colab. No installation, no terminal, no prior experience required.</p>
</a>

<a class="tutorial-card" href="tutorials/30x-wgs-workshop/">
  <div class="tutorial-card__header">
    <span class="difficulty-badge difficulty-badge--intermediate">Intermediate</span>
    <span class="time-estimate">40 min</span>
  </div>
  <h3 class="tutorial-card__title">30x WGS Workshop</h3>
  <p class="tutorial-card__desc">Explore a real 30x whole-genome sequence: structural variants, QC metrics, and pharmacogenomics beyond SNP arrays.</p>
</a>

</div>


[Skill Library](skills/index.md) · [SKILL.md Spec](reference/skillmd-spec.md) · [Contributing](contributing/index.md) · [All Tutorials](tutorials/index.md) · [Presentations](presentations/index.md)
