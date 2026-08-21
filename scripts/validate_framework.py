#!/usr/bin/env python3
"""Validate repository contracts for the white-box learning framework."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = {
    ".github/workflows/validate-framework.yml",
    "README.md",
    "docs/WHITEBOX_LEARNING_FRAMEWORK.md",
    "docs/LEARNING_MECHANISM.md",
    "docs/LEARNING_BRANCH_WORKFLOW.md",
    "docs/framework-review.md",
    "scripts/validate_framework.py",
    "templates/MECHANISM_UNIT.md",
    "templates/EXPERIMENT.md",
    "templates/MERGE_REVIEW.md",
    "topics/unix/README.md",
    "topics/unix/coverage.md",
}

DEPRECATED_FILES = {
    "docs/experiment-evidence.md",
    "docs/learning-workflow.md",
    "docs/mechanism-unit-spec.md",
    "docs/merge-gate.md",
    "docs/source-linking.md",
}

REQUIRED_SNIPPETS = {
    "docs/WHITEBOX_LEARNING_FRAMEWORK.md": {
        "Claim–Evidence traceability",
        "Coverage status",
        "Mechanism Unit lifecycle",
        "Claim epistemic status",
    },
    "templates/MECHANISM_UNIT.md": {
        "## 6. Claims and Evidence",
        "## 7. Source Evidence",
        "## 12. Boundaries / Counterexamples",
        "Unit status: `draft | investigating | review-ready | learned | falsified | abandoned`",
    },
    "templates/EXPERIMENT.md": {
        "## 3. Falsification Criteria",
        "## 8. Raw Evidence",
        "## 9. Observations",
        "## 10. Interpretation",
    },
    "templates/MERGE_REVIEW.md": {
        "## 3. Claim-Evidence Audit",
        "## 5. Falsifiability and Reproducibility",
        "## 9. Decision",
    },
}

ALLOWED_COVERAGE_STATUSES = {
    "not-started",
    "in-progress",
    "source-reviewed",
    "mapped",
}

MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
COVERAGE_ROW = re.compile(r"^\|\s*([0-9]+|[A-Z])\s*\|.*\|\s*([a-z-]+)\s*\|\s*$")


def relative_markdown_links(path: Path) -> list[tuple[str, Path]]:
    links: list[tuple[str, Path]] = []
    text = path.read_text(encoding="utf-8")
    for raw_target in MARKDOWN_LINK.findall(text):
        target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
        if not target or target.startswith(("#", "http://", "https://", "mailto:")):
            continue
        target = unquote(target.split("#", 1)[0])
        if not target:
            continue
        resolved = (path.parent / target).resolve()
        links.append((raw_target, resolved))
    return links


def validate() -> tuple[list[str], int, int]:
    errors: list[str] = []

    for relative in sorted(REQUIRED_FILES):
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    for relative in sorted(DEPRECATED_FILES):
        if (ROOT / relative).exists():
            errors.append(f"deprecated parallel specification still exists: {relative}")

    for relative, snippets in REQUIRED_SNIPPETS.items():
        path = ROOT / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for snippet in sorted(snippets):
            if snippet not in text:
                errors.append(f"{relative}: missing contract text: {snippet!r}")

    link_count = 0
    for path in sorted(ROOT.rglob("*.md")):
        for raw_target, resolved in relative_markdown_links(path):
            link_count += 1
            if not resolved.exists():
                display_path = path.relative_to(ROOT)
                errors.append(f"{display_path}: broken internal link {raw_target!r}")

    coverage_rows = 0
    for path in sorted(ROOT.glob("topics/*/coverage.md")):
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            match = COVERAGE_ROW.match(line)
            if not match:
                continue
            coverage_rows += 1
            status = match.group(2)
            if status not in ALLOWED_COVERAGE_STATUSES:
                display_path = path.relative_to(ROOT)
                errors.append(
                    f"{display_path}:{line_number}: invalid coverage status {status!r}"
                )

    normative_paths = [
        ROOT / "README.md",
        ROOT / "docs/WHITEBOX_LEARNING_FRAMEWORK.md",
        ROOT / "docs/LEARNING_MECHANISM.md",
        ROOT / "docs/LEARNING_BRANCH_WORKFLOW.md",
        ROOT / "templates/MECHANISM_UNIT.md",
        ROOT / "templates/EXPERIMENT.md",
        ROOT / "templates/MERGE_REVIEW.md",
    ]
    normative_markdown = "\n".join(
        path.read_text(encoding="utf-8") for path in normative_paths if path.is_file()
    )
    if "learn/<topic>-<mechanism>" in normative_markdown:
        errors.append("legacy branch convention remains in normative documents")

    readme = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").is_file() else ""
    for canonical in (
        "docs/WHITEBOX_LEARNING_FRAMEWORK.md",
        "docs/LEARNING_MECHANISM.md",
        "docs/LEARNING_BRANCH_WORKFLOW.md",
    ):
        if canonical not in readme:
            errors.append(f"README.md does not link canonical document: {canonical}")

    return errors, link_count, coverage_rows


def main() -> int:
    errors, link_count, coverage_rows = validate()
    if errors:
        print("Framework validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Framework validation passed: "
        f"{len(REQUIRED_FILES)} required files, "
        f"{link_count} internal links, "
        f"{coverage_rows} coverage rows."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
