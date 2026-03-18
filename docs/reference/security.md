---
title: Security
description: Security model, threat analysis, and trust guarantees for ClawBio skills
---

# Security

ClawBio skills run locally, process sensitive genetic data, and are invoked by AI agents. The security model is designed to ensure that skills cannot exfiltrate data, escalate privileges, or produce unsafe outputs.

## Core Principles

1. **Local execution**: genetic data never leaves the user's machine
2. **No network access**: skills cannot make outbound network calls during execution
3. **Filesystem sandboxing**: skills can only read inputs and write to declared output paths
4. **Signed packages**: cryptographic signatures verify skill integrity
5. **Sandboxed execution**: skills run in unprivileged containers or processes

## Security Scan

Every skill undergoes automated security scanning before publication:

| Check | Description |
|-------|-------------|
| No network calls | Static analysis confirms no `requests`, `urllib`, `httpx`, `socket` imports or usage |
| Filesystem scope | Skills only access files under their declared input/output paths |
| No shell injection | No `os.system`, `subprocess.call` with `shell=True`, or `eval`/`exec` |
| Dependency audit | All dependencies checked against known vulnerability databases |
| Secrets detection | No hardcoded API keys, tokens, or credentials |
| Input validation | All inputs validated before processing (type, format, size) |

## Signed Packages

Starting Q4 2026, published skills include a cryptographic signature:

- Skills are signed with the author's key at publication time
- Users verify signatures before installation
- Tampered packages are rejected automatically
- Signature chain: author key + ClawBio registry co-signature

## Validation Tiers

| Tier | Review Level | Use Case |
|------|-------------|----------|
| **Community** | Automated schema validation only | Research and exploration |
| **Verified** | Automated + human domain review | Production research workflows |
| **Clinical** | Automated + domain review + clinical safety review | Clinical-adjacent academic use |

Clinical tier skills undergo additional review:

- Guideline compliance verified by a domain expert
- Safety rules audited for completeness
- Test coverage threshold (>80%)
- Demo output compared against reference datasets

## Threat Model

| Threat | Vector | Mitigation | Severity |
|--------|--------|------------|----------|
| Malicious skill submission | Attacker publishes skill with exfiltration code | Automated scan + human review; no network access in sandbox | High |
| Prompt injection via SKILL.md | SKILL.md fields crafted to manipulate the invoking agent | SKILL.md fields are parsed as structured data, never as raw prompts | Medium |
| Data exfiltration | Skill attempts to send genetic data to external server | No network access; filesystem sandboxing | High |
| Dependency poisoning | Malicious package in skill's dependency tree | Pinned versions; checksum verification; vulnerability scanning | High |
| Guideline spoofing | Fake guideline DOI or authority reference | DOI verification against CrossRef/DataCite; authority whitelist | Medium |
| Privilege escalation | Skill attempts to gain root or elevated access | Unprivileged container execution; no `sudo`, no setuid | High |
| Output manipulation | Skill produces intentionally misleading results | Reference output checksums; reproducibility tests; human review for clinical tier | Medium |
| Denial of service | Skill consumes excessive resources | Execution timeout; memory limits; CPU quotas | Low |

## Reporting Vulnerabilities

If you discover a security vulnerability in ClawBio or any published skill:

1. **Do not open a public issue**
2. Email **security@clawbio.ai** with a description of the vulnerability
3. Include steps to reproduce if possible
4. We will acknowledge within 48 hours and provide a timeline for resolution

## Best Practices for Skill Authors

- Never import networking libraries (`requests`, `httpx`, `urllib`, `socket`)
- Never use `eval`, `exec`, or `subprocess` with `shell=True`
- Validate all inputs before processing (check file format, size, variant count)
- Pin all dependency versions in your requirements
- Include comprehensive tests with expected output checksums
- Document all filesystem paths your skill accesses in the SKILL.md
