# Security Auditor (/audit)

A custom slash command that scans code files for vulnerability vectors (secrets, injections, XSS) and proposes direct mitigation fixes.

> Part of **[Slash Command Bazaar](../../README.md)** · [Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)

## Details
- **Target Tool**: `Claude Code`
- **Source URL**: [https://github.com/anthropics/claude-code](https://github.com/anthropics/claude-code)
- **Author**: Security Community
- **License**: MIT
- **Date Added**: 2026-06-21

## Command Instruction
```markdown
Scan the active file or selected block of code for security vulnerabilities. Check for secrets/keys, SQL injections, XSS, CSRF, broken access control, dependency vulnerabilities, and unsafe imports. Detail the risks and provide the refactored code that resolves them.
```
