# Ask ClawBio in your browser

**Type a request. Watch an AI agent use a ClawBio skill. Inspect the evidence. Ask a follow-up.**

This prototype demonstrates agentic skill execution in a terminal-style Google Colab notebook. Colab provides the sandbox, its keyless Gemini integration supplies the model, and ClawBio supplies the scientific skill and analysis tools.

[Open the agent prototype in Colab](https://colab.research.google.com/github/ClawBio/ClawBio/blob/fix/colab-first-skill-demo/docs/tutorial-agent.ipynb){ .md-button }

**Prototype status:** local tool-loop tests pass. Keyless Gemini selected and read the skill in Colab. Google then returned HTTP 429 (heavy load), so a complete live agent conversation remains unverified. The link currently targets the development branch.

## Start the demo: you must click Run

**Opening the notebook does not start ClawBio. Click the ▶ play button to the left of “Launch ClawBio”.** Alternatively, select **Runtime > Run all**. If prompted, choose **Run anyway**, then wait for the console to appear. No code editing is needed.

## What you will do

1. Sign into Google and click the play button beside **Launch ClawBio**. The implementation code is hidden. Colab connects and prepares the console; if prompted, choose **Run anyway**.
2. In the ClawBio console, ask: "Check whether Manuel Corpas public genotype data supports PharmGx interpretation. Explain any withheld results."
3. Watch the agent read the PharmGx skill instructions, choose tools, run ClawBio and inspect results. Expand entries to see actual tool calls and outputs.
4. Ask: "Why were interpretations withheld, and what input does the skill require?"
5. Download the reports, commands and conversation trace.

The conversation drives tool selection. These are live actions, not a prerecorded transcript or a fixed sequence of analysis cells. The prototype supports one skill, Manuel Corpas’s public genotype file and a deliberately edited teaching copy; it does not provide general shell access or arbitrary data uploads.

## What you need

A Google account with access to Colab AI and a standard CPU runtime. No separate AI account or API key is configured. Available models and quotas depend on Google's current account eligibility and service limits. If access fails, the console reports the error.

This demo uses **Manuel Corpas’s real, publicly released 23andMe genotype data**, with his explicit authorisation. It is not synthetic data or the full 30x whole-genome sequencing dataset. [Inspect the pinned public source](https://github.com/ClawBio/ClawBio/blob/7290841dfc9c7e817c12af38a2dd1479f0babe8e/skills/genome-compare/data/manuel_corpas_23andme.txt.gz).

The missing-CYP2C19 exercise deliberately removes markers from a copy. That edited file is a teaching intervention, not a second observed genome. The original remains intact. The evidence bundle records the source and input checksum.

Prompts, skill instructions and analysis summaries are sent to Google. Do not enter any additional private, confidential or patient information.

Prefer a deterministic walkthrough? [Run the guided PharmGx tutorial](run-your-first-skill.md), which does not need model access.

ClawBio is a research and educational tool. It is not a medical device and does not provide clinical diagnoses. Consult a healthcare professional before making any medical decisions.

## Known limitation of this public input

The pinned PharmGx implementation does not recognise this file’s reference coordinates and withholds gene interpretations. The demo therefore shows the agent identifying and explaining an input limitation. It does not currently produce a usable drug-response interpretation from this genome. No coordinate remapping or genotype alteration is performed to bypass this check.
