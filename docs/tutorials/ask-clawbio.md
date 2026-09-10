# Ask ClawBio in your browser

**Type a request. Watch an AI agent use a ClawBio skill. Inspect the evidence. Ask a follow-up.**

This prototype demonstrates agentic skill execution in a terminal-style Google Colab notebook. Colab provides the sandbox, its keyless Gemini integration supplies the model, and ClawBio supplies the scientific skill and analysis tools.

[Open the agent prototype in Colab](https://colab.research.google.com/github/ClawBio/ClawBio/blob/fix/colab-first-skill-demo/docs/tutorial-agent.ipynb){ .md-button }

**Prototype status:** local tool-loop tests pass. Live Gemini access and a complete agent conversation still need verification in Colab. The link currently targets the development branch.

## What you will do

1. Sign into Google and run the notebook setup cells.
2. In the ClawBio console, ask: "Analyse this synthetic sample for drug-response implications. Flag incomplete evidence."
3. Watch the agent read the PharmGx skill instructions, choose tools, run ClawBio and inspect results. Expand entries to see actual tool calls and outputs.
4. Ask: "Remove the CYP2C19 markers, rerun and explain what changes."
5. Download the reports, commands and conversation trace.

The conversation drives tool selection. These are live actions, not a prerecorded transcript or a fixed sequence of analysis cells. The prototype supports one skill and two synthetic samples; it does not provide general shell access or arbitrary data uploads.

## What you need

A Google account with access to Colab AI and a standard CPU runtime. No separate AI account or API key is configured. Available models and quotas depend on Google's current account eligibility and service limits. If access fails, the console reports the error.

Prompts, skill instructions and synthetic result summaries are sent to Google. Use only the bundled teaching data; do not enter personal, confidential or patient information.

Prefer a deterministic walkthrough? [Run the guided PharmGx tutorial](run-your-first-skill.md), which does not need model access.

ClawBio is a research and educational tool. It is not a medical device and does not provide clinical diagnoses. Consult a healthcare professional before making any medical decisions.
