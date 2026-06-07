# Use Cases

These examples show where the kit is meant to be useful.

## 1. Free-to-Paid Funnel Review

A solo operator can copy `templates/funnel-map.md`, describe the free entry point, the follow-up path, and the paid offer. Codex can then review the map and suggest one low-risk improvement.

Useful files:

- `templates/funnel-map.md`
- `templates/daily-kpi.md`
- `examples/sample-daily-kpi.md`
- `templates/codex-maintenance-prompt.md`

## 2. Weekly Growth Review

At the end of each week, a maintainer can fill in `templates/weekly-review.md` and ask Codex to identify the most important bottleneck.
The weekly decision rule keeps the output narrow: one weak step, one reviewable improvement, one metric to watch next.

Useful files:

- `templates/weekly-review.md`
- `examples/sample-weekly-review.md`
- `examples/sample-daily-kpi.md`

## 3. Short-Form Content Planning

Creators and consultants can use `templates/short-video-brief.md` to keep hooks, pain points, CTA, and offer alignment in one place before producing posts.

Useful files:

- `templates/short-video-brief.md`
- `templates/offer-positioning.md`

## 4. Safe Repository Maintenance

Maintainers can use the PR template, release checklist, and security policy to keep changes small and avoid accidental private data exposure.

Useful files:

- `.github/pull_request_template.md`
- `docs/release-checklist.md`
- `SECURITY.md`

## 5. First Offer Audit for a New Service

When a new solo service project is still small, the operator can use this kit before building more software. The first audit checks whether the free entry point, follow-up message, and first paid offer are clear enough to test.

Useful files:

- `templates/offer-positioning.md`
- `templates/funnel-map.md`
- `templates/weekly-review.md`

Suggested Codex task:

```text
Read templates/offer-positioning.md and templates/funnel-map.md.
Identify the single place where a new visitor is most likely to hesitate.
Suggest one copy or structure improvement that can be reviewed in under 30 minutes.
Do not suggest price changes, payment changes, production settings, or private data collection.
```

Expected output:

- One bottleneck.
- One low-risk improvement.
- One metric to watch next week.

