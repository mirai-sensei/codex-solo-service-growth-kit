# Codex Maintenance Prompt

Use this prompt when asking Codex to improve the project safely.

```text
Read README.md, templates/funnel-map.md, templates/daily-kpi.md, and templates/weekly-review.md.

Goal:
[Describe the business or maintenance goal.]

Constraints:
- Do not expose secrets, customer data, payment data, or private records.
- Do not change production settings.
- Do not change product prices or payment provider settings.
- Keep changes small and reviewable.
- Prefer existing templates before creating new ones.

Task:
Identify the single highest-impact improvement.
If editing files, change only the smallest necessary set.
Afterward, summarize what changed, what was not changed, and how to verify it.
```

