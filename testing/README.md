# Testing

Commands for generating and running tests.

> Part of **[Slash Command Bazaar](../README.md)** · Browse all bazaars at the **[Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)**.

## How entries are stored
Each slash command lives in **its own sub-folder** inside this category, named in `kebab-case`:

```
testing/
└── <entry-name>/
    ├── README.md     # what it is, source, author, license, link
    └── ...           # the actual files (full copy)
```

## Add to this category
- Open a PR following the [contribution guide](../CONTRIBUTING.md), **or**
- Submit via the [submission form](https://github.com/Drvivek34/Slash-Command-Bazaar/issues/new/choose).

## Entries

| Entry | Description |
|---|---|
| [Test Command](test-command/) | Generates a complete test suite for the current file using standard testing frameworks (pytest, jest, mocha). |
| [Unit Test Generator](unit-test-generator/) | A custom command that reads a source file and writes high-coverage unit tests using the matching testing framework. |
