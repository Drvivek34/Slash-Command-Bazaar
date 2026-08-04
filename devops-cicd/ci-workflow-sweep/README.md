# CI workflow expert (/ci-sweep)

A maintenance command for inspecting GitHub Actions failures, checking workflow drift, and preparing a minimal verified fix.

> Part of **[Slash Command Bazaar](../../README.md)** · [Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)

## Details
- **Target Tool**: `GitHub Copilot / Claude Code`
- **Source URL**: [https://github.com/github/awesome-copilot/blob/main/agents/github-actions-expert.agent.md](https://github.com/github/awesome-copilot/blob/main/agents/github-actions-expert.agent.md)
- **Author**: GitHub Copilot community (adapted)
- **License**: MIT
- **Date Added**: 2026-08-04
- **Last Reviewed**: 2026-08-04

## Command Instruction
```markdown
Inspect the latest failing GitHub Actions run and the workflow files it executed. Separate flaky or environmental failures from reproducible configuration and code failures. Propose the smallest fix, pin or update action versions only with evidence, run local validation where possible, and leave generated or unrelated workflow files unchanged.
```
