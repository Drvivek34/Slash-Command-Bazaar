---
description: GLM proxy start/status/change (token, base URL, model)
argument-hint: "[start|status|stop|switch|change|config|install]"
---

# /glm

- `/glm` or `/glm start` — ensure proxy
- `/glm status` — masked config
- `/glm change` or `/glm config` — ask user for token, upstream URL, API model, ports; apply via change-config.ps1; restart proxy
- Config: `~/.grok/proxies/glm.env` (never commit tokens)

Full package: https://github.com/Drvivek34/Custom-Instruction-Bazaar/tree/main/coding-development/databricks-glm
