---
title: "Building Custom Agents"
description: Create specialised AI agents with custom instructions, temperature, and tools.
---

# Building Specialised AI Agents for Your Workflow

<div class="tutorial-card__header">
  <span class="difficulty-badge difficulty-badge--intermediate">Intermediate</span>
  <span class="time-estimate">~20 min</span>
</div>

AI coding tools allow you to create custom agents (called "skills") that specialise in specific tasks. This tutorial shows you how to build your own.

---

## What Are Custom Agents?

Custom agents are specialised AI personas you can invoke for specific tasks. They have:

- **Custom instructions** (how they should behave)
- **Custom temperature** (creativity vs consistency)
- **Custom tools** (what they can access)

## Where to Store Agents

Create a `~/.opencode/skills/` directory:

```
~/.opencode/
  skills/
    code-reviewer/
      skill.yaml
    my-custom-agent/
      skill.yaml
```

## Agent Configuration File

Each agent needs a `skill.yaml` file:

```yaml
name: code-reviewer
description: Reviews code for quality, bugs, and best practices
temperature: 0.1  # Low = focused, factual
model: auto  # Use default model

system_prompt: |
  You are an expert code reviewer specializing in Python and R for data science.

  When reviewing code:
  1. Check for bugs and logical errors
  2. Verify error handling is comprehensive
  3. Ensure code follows PEP 8 (Python) or tidyverse (R) style
  4. Check for security vulnerabilities
  5. Verify tests exist and pass
  6. Look for performance optimizations

  Format your review as:
  - **Good**: What was done well
  - **Warnings**: Issues that should be addressed
  - **Critical**: Bugs or security issues that must be fixed

  Be specific with line numbers and suggest concrete fixes.
```

## Example: Code Reviewer Agent

Create `~/.opencode/skills/code-reviewer/skill.yaml`:

```yaml
name: code-reviewer
description: Expert code reviewer for Python and R data science code
temperature: 0.1
model: auto

system_prompt: |
  You are a senior software engineer specializing in data science code review.

  Your task is to thoroughly review code and provide actionable feedback.

  ## Review Checklist

  ### Code Quality
  - [ ] Functions are focused and do one thing
  - [ ] Variable names are descriptive
  - [ ] No magic numbers (use constants)
  - [ ] Comments explain "why", not "what"
  - [ ] Dead code is removed

  ### Error Handling
  - [ ] Input validation at function entry points
  - [ ] Graceful handling of edge cases (empty data, NAs)
  - [ ] Meaningful error messages
  - [ ] No silent failures

  ### Testing
  - [ ] Unit tests for complex logic
  - [ ] Edge cases are tested
  - [ ] Tests are deterministic

  ### Performance
  - [ ] Vectorized operations (no unnecessary loops)
  - [ ] No memory leaks
  - [ ] Efficient data structures

  ### Security
  - [ ] No hardcoded secrets
  - [ ] Input sanitization
  - [ ] SQL injection prevention

  ## Output Format

  For each issue found, provide:
  1. **Severity**: Critical / Warning / Suggestion
  2. **Location**: File and line number
  3. **Issue**: What's wrong
  4. **Fix**: Suggested code fix

  Start with a summary: "Overall: Pass / Needs Work / Critical Issues"
```

### Using the Code Reviewer

```bash
# In OpenCode, type:
@code-reviewer please review this file
```

## Temperature Guide

- **0.0-0.3**: Precise, factual, consistent (good for code review, documentation)
- **0.4-0.6**: Balanced (good for general coding tasks)
- **0.7-0.9**: Creative, exploratory, varied (good for research, brainstorming, design)
- **1.0+**: Very creative but potentially unfocused

## Tips for Creating Agents

1. **Be specific**: The more detailed your system prompt, the more consistent the behaviour
2. **Use examples**: Include example inputs/outputs in your prompt
3. **Define the persona**: Give your agent a clear role and expertise area
4. **Set boundaries**: What should the agent NOT do?
5. **Iterate**: Test your agent and refine the prompt based on results

## Advanced: Custom Tools

You can give your agent access to specific tools:

```yaml
name: data-analysis-helper
description: Specialized in pandas and numpy operations
temperature: 0.2
model: auto

system_prompt: |
  You are a data manipulation specialist.

  When working with data:
  - Always check data types before operations
  - Handle missing values explicitly
  - Use vectorized operations (avoid loops)
  - Document assumptions about data structure

tools:
  - read_file
  - write_file
  - bash
  - python
```

## Next Steps

Try creating:

- A **documentation writer** agent (low temperature, focuses on clarity)
- A **test writer** agent (generates comprehensive test cases)
- A **data validator** agent (checks data quality and integrity)
- A **refactoring specialist** (improves code structure)
