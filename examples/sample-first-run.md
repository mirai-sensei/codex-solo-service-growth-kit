# Sample First Run

This fictional example follows `docs/getting-started.md` from a first funnel map to one weekly decision.

It uses generic data only. Do not copy customer names, payment records, private consultation notes, API keys, or credentials into this kind of working file.

## Workflow

Project: Fictional solo consultation service

Goal: Turn a free self-check into one paid consultation booking without changing prices, payment settings, or private customer data handling.

Owner: Solo operator

## Funnel Snapshot

| Step | Asset | Visitor intent | Desired action | Risk |
| --- | --- | --- | --- | --- |
| 1 | Short post | Understand the problem | Open profile link | Hook is too broad |
| 2 | Free self-check | Get quick clarity | Complete the form | Too many fields |
| 3 | Result page | See the next step | Click paid consultation CTA | Offer value is vague |
| 4 | Booking page | Decide whether to pay | Book a consultation | Scope feels unclear |

## Three-Day KPI Snapshot

| Date | Link clicks | Free starts | Free completions | Paid CTA clicks | Paid bookings |
| --- | ---: | ---: | ---: | ---: | ---: |
| 2026-06-01 | 48 | 31 | 18 | 7 | 2 |
| 2026-06-02 | 42 | 26 | 14 | 5 | 1 |
| 2026-06-03 | 51 | 33 | 17 | 6 | 1 |

## Bottleneck

The largest visible drop-off is between free starts and free completions.

Evidence: Across three days, 90 visitors started the free self-check, but only 49 completed it.

## One Safe Improvement

Rewrite the form intro so the visitor knows:

- It takes under 2 minutes.
- Optional details can be skipped.
- The result gives one practical next step.

## Weekly Decision

Next week, test a shorter free self-check intro and keep all other parts of the funnel unchanged.

## Codex Prompt Used

```text
Read this first-run example.
Find the single weakest step in the funnel.
Suggest one copy-only improvement that does not change production settings, payments, customer data, or prices.
Return the reason, the proposed text, and the number to watch next week.
```

## Number To Watch Next

Free completion rate from visitors who start the free self-check.
