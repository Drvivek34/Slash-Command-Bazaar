#!/usr/bin/env python3
import os
import re
from datetime import datetime

SC_BAZAAR_DIR = "/root/bazaars/Slash-Command-Bazaar"

CURATED_COMMANDS = [
    {
        "name": "Git conventional commit helper (/commit)",
        "slug": "commit-helper",
        "category": "git-version-control",
        "desc": "A custom command that checks the git diff and generates structured conventional commit messages.",
        "tool": "Claude Code / Codex CLI",
        "author": "Claude Code Community",
        "source": "https://github.com/anthropics/claude-code",
        "instructions": "Run 'git diff' to inspect changes, then output 3 potential conventional commit messages in format: <type>(<scope>): <desc>. Use types: feat, fix, chore, docs, refactor, test, ci."
    },
    {
        "name": "Unit test generator (/test)",
        "slug": "unit-test-generator",
        "category": "testing",
        "desc": "A custom command that reads a source file and writes high-coverage unit tests using the matching testing framework.",
        "tool": "Claude Code / Cursor",
        "author": "Cursor Rules Community",
        "source": "https://github.com/cursor-ai/cursor",
        "instructions": "Read the selected source file, determine the language and matching test suite (e.g. pytest, jest, unittest), and write comprehensive unit tests covering edge cases, happy paths, and error scenarios. Save in the appropriate tests directory."
    },
    {
        "name": "Code quality & refactor helper (/refactor)",
        "slug": "code-refactor-helper",
        "category": "refactoring",
        "desc": "Command to analyze code style, performance, and formatting, suggesting drop-in replacements for anti-patterns.",
        "tool": "Agnostic",
        "author": "Codex CLI",
        "source": "https://github.com/google-gemini/gemini-cli",
        "instructions": "Analyze the active file or selected block of code. Identify formatting anti-patterns, complex nesting, performance inefficiencies, or styling issues. Suggest a refactored version with inline explanations of changes made."
    },
    {
        "name": "Project README & Doc builder (/docs)",
        "slug": "readme-builder",
        "category": "documentation",
        "desc": "Command to read all project filenames and generate/update the project master README file with a sitemap.",
        "tool": "Claude Code",
        "author": "Claude Code Custom Commands",
        "source": "https://github.com/anthropics/claude-code",
        "instructions": "List directories and files recursively up to depth 3, read package.json or metadata files, and construct a comprehensive README.md file highlighting setup, usage, directory structure, and developer guidelines."
    }
]

def main():
    today_str = datetime.today().strftime("%Y-%m-%d")
    count = 0

    for item in CURATED_COMMANDS:
        cat_dir = os.path.join(SC_BAZAAR_DIR, item["category"], item["slug"])
        os.makedirs(cat_dir, exist_ok=True)

        readme_content = f"""# {item['name']}

{item['desc']}

> Part of **[Slash Command Bazaar](../../README.md)** · [Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)

## Details
- **Target Tool**: `{item['tool']}`
- **Source URL**: [{item['source']}]({item['source']})
- **Author**: {item['author']}
- **License**: MIT
- **Date Added**: {today_str}

## Command Instruction
```markdown
{item['instructions']}
```
"""
        with open(os.path.join(cat_dir, "README.md"), "w") as f:
            f.write(readme_content)
        count += 1
        print(f"Imported Command: {item['name']} -> {item['category']}/{item['slug']}")

    print(f"Successfully imported {count} slash commands.")

if __name__ == "__main__":
    main()
