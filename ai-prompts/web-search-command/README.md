# /web-search Command

Runs a live web search from Claude Code using the best available provider, with automatic
free-tier quota awareness and provider fallback.

> Part of **[Slash Command Bazaar](../../README.md)** · [Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)

## Details

- **Target Tool / Agent**: `Claude Code` (portable to Aider / Codex)
- **Source URL**: https://github.com/Drvivek34/Slash-Command-Bazaar/tree/main/ai-prompts/web-search-command
- **Author**: Slash Command Bazaar Community
- **License**: MIT
- **Date Added**: 2026-08-24

## Prompt Instructions

```markdown
When '/web-search <query>' is run:

1. PROVIDER ORDER — try in this sequence, stop at first success:
   a. Tavily (TAVILY_API_KEY) — POST https://api.tavily.com/search, api_key IN THE JSON
      BODY (not header). Basic depth = 1 credit; free tier 1,000/month, no card.
   b. Exa (EXA_API_KEY) — POST https://api.exa.ai/search with x-api-key header.
      Free tier $10/month credits (+$20 signup bonus), no card.
   c. Firecrawl (FIRECRAWL_API_KEY) — POST https://api.firecrawl.dev/v2/search,
      Authorization: Bearer header. Free tier 1,000 credits/month, no card.
   d. Brave (BRAVE_SEARCH_API_KEY — exact name, never BRAVE_API_KEY) — GET
      https://api.search.brave.com/res/v1/web/search with X-Subscription-Token header.
      $5/month free credits since Aug 2025 change; CARD REQUIRED at signup.
   e. Serper (SERPER_API_KEY) — POST https://google.serper.dev/search with X-API-KEY
      header. 2,500 one-time signup credits.
   f. Google CSE (GCS_API_KEY + GCS_CX) — GET www.googleapis.com/customsearch/v1.
      100 queries/day free.
2. QUOTA RULES — count only HTTP 200 against local usage tracking; on 429 or 403
   quota-exceeded, move to the next provider instead of retrying.
3. OUTPUT — report top 5 results as a table: Title | URL | Snippet (≤200 chars) |
   Provider used. Note which provider answered so the user can track burn.
4. HYGIENE — never print API keys; read them from the environment only. Cache identical
   repeat queries within the session.
```

## Notes

- Free-tier facts verified **2026-08-24** against official pricing pages.
- Deep-dive per-provider pages:
  [Free-API-Bazaar/search-web](https://github.com/Drvivek34/Free-API-Bazaar/tree/main/search-web).
