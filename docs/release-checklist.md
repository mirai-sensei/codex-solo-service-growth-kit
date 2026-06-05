# Release Checklist

Use this checklist before tagging or announcing a new version of the kit.

## Documentation

- README describes the current templates accurately.
- CHANGELOG includes the new changes.
- ROADMAP reflects any newly completed or deferred work.
- Examples use fake data only.

## Safety

- No `.env` files or real credentials are included.
- No customer records, payment records, or private consultation notes are included.
- New prompts tell Codex to keep changes small and reviewable.
- Any competitor analysis guidance focuses on structure, not copying protected content.

## Validation

Run:

```bash
python scripts/validate_templates.py
```

## Release Notes

Before publishing, summarize:

- What changed
- Who benefits
- How to try it
- Any safety notes

