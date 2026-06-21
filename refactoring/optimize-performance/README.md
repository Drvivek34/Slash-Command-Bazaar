# Optimize Performance (/optimize)

Analyzes the selected code block for performance bottlenecks (memory allocations, quadratic loops) and provides an optimized version.

> Part of **[Slash Command Bazaar](../../README.md)** · [Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)

## Details
- **Target Tool**: `Claude Code / Cursor`
- **Source URL**: [https://github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
- **Author**: Codex CLI Community
- **License**: MIT
- **Date Added**: 2026-06-21

## Command Instruction
```markdown
Analyze the selected code block for performance bottlenecks. Specifically check for unnecessary memory allocations, quadratic loops, redundant database queries (N+1 queries), resource leaks, and lack of caching. Provide an optimized version of the code and describe the algorithmic improvement (e.g. O(N^2) to O(N)).
```
