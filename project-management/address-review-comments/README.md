# Address review comments (/address-comments)

A review-loop command that gathers unresolved comments, maps each to the current diff, and proposes or applies bounded fixes with verification.

> Part of **[Slash Command Bazaar](../../README.md)** · [Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)

## Details
- **Target Tool**: `GitHub Copilot / Claude Code`
- **Source URL**: [https://github.com/github/awesome-copilot/blob/main/agents/address-comments.agent.md](https://github.com/github/awesome-copilot/blob/main/agents/address-comments.agent.md)
- **Author**: GitHub Copilot community (adapted)
- **License**: MIT
- **Date Added**: 2026-08-04
- **Last Reviewed**: 2026-08-04

## Command Instruction
```markdown
Collect the unresolved review comments for the active change. Group duplicates, identify the exact files and behavior each comment refers to, and state the smallest compliant fix. Apply only in-scope changes, run the relevant tests or checks, and report which comments were resolved, deferred, or require reviewer clarification.
```
