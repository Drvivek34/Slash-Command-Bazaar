# /debug Log Analyzer Command

Parses error logs or stack traces and proposes direct code fixes targeting the file where the exception occurred.

> Part of **[Slash Command Bazaar](../../README.md)** · [Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)

## Details
- **Target Tool / Agent**: `Claude Code / Aider`
- **Source URL**: [https://aider.chat/docs/usage.html](https://aider.chat/docs/usage.html)
- **Author**: DevOps Toolkit
- **License**: MIT
- **Date Added**: 2026-06-21

## Prompt Instructions
```markdown
When '/debug <error_log>' is run, map the stack trace to files in the repository. Propose the exact replacement chunk to fix the root exception. Detail why it occurred.
```
