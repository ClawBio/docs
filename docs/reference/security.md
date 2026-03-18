---
title: Security
description: Security principles and best practices for ClawBio skills
---

# Security

ClawBio skills run locally, process sensitive genetic data, and are invoked by AI agents. These are the security principles we follow.

## Core Principles

1. **Local execution**: genetic data never leaves the user's machine
2. **No network access**: skills should not make outbound network calls during analysis
3. **Filesystem discipline**: skills should only read inputs and write to declared output paths
4. **No shell injection**: no `eval`, `exec`, or `subprocess` with `shell=True`

## Security Checklist for Skills

| Check | Description |
|-------|-------------|
| No network calls | No `requests`, `urllib`, `httpx`, `socket` imports in analysis code |
| Filesystem scope | Skills only access files under their declared input/output paths |
| No shell injection | No `os.system`, `subprocess.call` with `shell=True`, or `eval`/`exec` |
| No hardcoded secrets | No API keys, tokens, or credentials in source code |
| Input validation | All inputs validated before processing (type, format, size) |
| Pinned dependencies | All dependency versions pinned in requirements |

## Best Practices for Skill Authors

- Never import networking libraries in analysis code
- Never use `eval`, `exec`, or `subprocess` with `shell=True`
- Validate all inputs before processing (check file format, size, variant count)
- Pin all dependency versions in your requirements
- Include tests with expected output checksums
- Document all filesystem paths your skill accesses in the SKILL.md
- Always include the ClawBio safety disclaimer in report output

## Reporting Issues

If you discover a security issue in ClawBio or any published skill, please open a private security advisory on the [GitHub repository](https://github.com/ClawBio/ClawBio/security/advisories).
