# Codex Solo Service Growth Kit

Reusable operating templates for solo service businesses that want to use Codex to improve acquisition, conversion, content production, and weekly maintenance without building a custom internal tool first.

This project is intentionally lightweight. It is a public, vendor-neutral template kit for coaches, consultants, creators, local service providers, educators, and spiritual/wellness practitioners who need repeatable workflows more than complex software.

## What Problem It Solves

Solo service businesses often run on scattered notes, manual checklists, and one-off prompts. That makes growth work hard to repeat. This kit turns common operating tasks into reusable Markdown templates that Codex can read, review, and improve safely.

The core loop is simple:

1. Map the free entry point and paid offer path.
2. Track a few daily acquisition and conversion numbers.
3. Find the weakest step in the funnel.
4. Make one small improvement.
5. Review results weekly and repeat.

## Who This Is For

- Solo founders and small teams selling appointments, consultations, courses, memberships, or digital offers.
- Non-engineers who use Codex to maintain documents, check funnels, review landing pages, and turn insights into small action plans.
- Open-source maintainers who want reusable templates for issue triage, KPI review, release notes, and operational documentation.

## What Is Included

- Funnel review templates for free-to-paid service flows.
- Daily KPI templates for acquisition and conversion tracking.
- Offer positioning worksheets.
- Short-form content briefs for scripts, hooks, and CTA alignment.
- Weekly review templates for deciding what to improve next.
- Codex maintenance prompts that keep changes small, auditable, and safe.
- A tiny validation script that checks whether templates keep their required sections.

## Repository Structure

```text
.
|-- README.md
|-- LICENSE
|-- CONTRIBUTING.md
|-- SECURITY.md
|-- CHANGELOG.md
|-- ROADMAP.md
|-- .gitignore
|-- docs/
|   `-- codex-for-oss-application-notes.md
|-- examples/
|   |-- sample-funnel-map.md
|   `-- sample-weekly-review.md
|-- scripts/
|   `-- validate_templates.py
`-- templates/
    |-- codex-maintenance-prompt.md
    |-- daily-kpi.md
    |-- funnel-map.md
    |-- offer-positioning.md
    |-- short-video-brief.md
    `-- weekly-review.md
```

## Quick Start

1. Copy the templates into your project workspace.
2. Fill in `templates/funnel-map.md` for your main free entry point.
3. Track daily numbers with `templates/daily-kpi.md`.
4. Use `templates/weekly-review.md` to decide the next bottleneck.
5. Ask Codex to make one small improvement at a time using `templates/codex-maintenance-prompt.md`.

For concrete scenarios, see [docs/use-cases.md](docs/use-cases.md).
For a repeatable weekly operating rhythm, see [docs/weekly-maintenance-loop.md](docs/weekly-maintenance-loop.md).

## Weekly Decision Rule

At the end of each week, choose the next task with this rule:

1. Pick the funnel step with the clearest drop-off.
2. Choose one improvement that can be reviewed in under 30 minutes.
3. Avoid changes to prices, payment settings, production secrets, or private customer data.
4. Write down what changed and what number should move next week.

This keeps the kit focused on steady compounding improvements instead of broad, hard-to-review rewrites.

## Try It in 10 Minutes

Use this flow when you want to test the kit before adapting it to a real business:

1. Open `examples/sample-funnel-map.md` and identify the free entry point.
2. Open `examples/sample-daily-kpi.md` and check where the funnel loses people.
3. Paste both files into Codex with the prompt below.
4. Ask for one improvement only.
5. Record the decision in `templates/weekly-review.md`.

This keeps the first run small, concrete, and easy to review.

## Example Codex Prompt

```text
Read examples/sample-funnel-map.md and examples/sample-daily-kpi.md.
Find the single weakest conversion step.
Suggest one low-risk improvement that does not change production settings, payments, customer data, or prices.
Return the finding, the reasoning, and the exact file or copy change to consider.
```

## Validate Templates

The validation script checks that every template keeps the expected heading structure.

```bash
python scripts/validate_templates.py
```

## Maintenance Workflow

This repository is maintained as a practical template library rather than a large application. Good maintenance work includes:

- Improving example clarity.
- Adding small reusable templates.
- Tightening safety language.
- Keeping template headings consistent.
- Turning repeated Codex workflows into documented prompts.
- Reviewing changes for accidental secrets or private business data.

## Open Source Fit

This project is useful as a small OSS maintainer workflow because the same templates can be reused across many service-business repositories. Codex can help maintain it by reviewing pull requests, improving examples, checking template completeness, generating issue summaries, and creating release notes.

## Safety Principles

- Do not commit secrets, API keys, customer data, payment logs, private consultation records, or production credentials.
- Treat templates as operating guidance, not legal, financial, medical, or psychological advice.
- When adapting competitor content, use only structure-level analysis and create original copy, visuals, audio, and examples.
- Keep every change small enough to review.

## License

MIT. See [LICENSE](LICENSE).
