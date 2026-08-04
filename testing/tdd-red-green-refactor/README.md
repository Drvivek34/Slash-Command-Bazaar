# TDD red-green-refactor loop (/tdd)

A compact command that turns a feature or bug fix into a test-first red-green-refactor cycle with explicit evidence at each stage.

> Part of **[Slash Command Bazaar](../../README.md)** · [Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)

## Details
- **Target Tool**: `Agnostic coding agent`
- **Source URL**: [https://github.com/github/awesome-copilot/blob/main/agents/tdd-red.agent.md](https://github.com/github/awesome-copilot/blob/main/agents/tdd-red.agent.md)
- **Author**: GitHub Copilot community (adapted)
- **License**: MIT
- **Date Added**: 2026-08-04
- **Last Reviewed**: 2026-08-04

## Command Instruction
```markdown
Translate the request into a focused behavioral test. Add the test and run it to confirm the expected failure, implement the smallest change that makes it pass, then refactor without changing behavior. Run the focused test and the relevant broader suite, and stop if the failure does not match the hypothesis.
```
