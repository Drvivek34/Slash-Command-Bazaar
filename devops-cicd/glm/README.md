# /glm

Slash command + skill for **Databricks GLM** local patch proxy (full tool calling with Grok and other agents).

## Full package

- [Custom-Instruction-Bazaar: coding-development/databricks-glm](https://github.com/Drvivek34/Custom-Instruction-Bazaar/tree/main/coding-development/databricks-glm)
- [Skill-Bazaar: coding-development/databricks-glm](https://github.com/Drvivek34/Skill-Bazaar/tree/main/coding-development/databricks-glm)

## Install

```powershell
# clone either package, then:
.\install.ps1 -AutoStart
```

```bash
./install.sh --auto-start
```

## Invoke

```
/glm
/glm start
/glm status
```

Requires env `DATABRICKS_TOKEN`. Proxy: `http://127.0.0.1:8787`.
