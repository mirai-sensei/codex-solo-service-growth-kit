from pathlib import Path


REQUIRED_HEADINGS = {
    "daily-kpi.md": ["# Daily KPI", "## Acquisition", "## Conversion", "## Revenue", "## One Next Action"],
    "funnel-map.md": ["# Funnel Map", "## Audience", "## Positioning", "## Flow", "## Bottlenecks", "## Do Not Touch"],
    "offer-positioning.md": ["# Offer Positioning", "## Problem", "## Desire", "## Specific Position", "## CTA"],
    "short-video-brief.md": ["# Short Video Brief", "## Audience State", "## Hook", "## Beat Sheet", "## Safety Check"],
    "weekly-review.md": ["# Weekly Review", "## Results", "## Bottleneck", "## Decision", "## Codex Task"],
    "codex-maintenance-prompt.md": ["# Codex Maintenance Prompt"],
}


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    template_dir = root / "templates"
    errors = []

    for file_name, headings in REQUIRED_HEADINGS.items():
        path = template_dir / file_name
        if not path.exists():
            errors.append(f"Missing template: {file_name}")
            continue

        text = path.read_text(encoding="utf-8")
        for heading in headings:
            if heading not in text:
                errors.append(f"{file_name}: missing heading {heading}")

    if errors:
        print("Template validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Template validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

