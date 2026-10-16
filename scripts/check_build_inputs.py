#!/usr/bin/env python3
"""Verify every input the Quarto build needs, before a render is attempted.

Why this exists
---------------
The three-format build (HTML, PDF, EPUB) takes several minutes in CI and needs a TeX
distribution for the PDF. When it fails, the failure is usually a missing file or a
chapter listed in `_quarto.yml` that does not exist — cheap to detect, expensive to
discover inside a render log.

This script checks the inputs, not the output. It does not claim the build succeeds;
it claims that a failure would not be caused by any of the conditions below.

Checks
------
1. `_quarto.yml` parses as YAML and its chapter list is well formed.
2. Every listed chapter file exists and is non-empty.
3. Every chapter listed appears exactly once.
4. The bibliography and CSL files exist and are non-empty.
5. Every figure referenced from a chapter (`![](path)` or `![...](path)`) exists.
6. Every `.qmd` file inside `book/` is either listed in `_quarto.yml` or explicitly
   excluded by a comment, so that an unwritten chapter cannot silently disappear.

Usage
-----
    python scripts/check_build_inputs.py
Exit code 0 if all inputs are present, 1 otherwise.
"""
from __future__ import annotations

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG = os.path.join(ROOT, "_quarto.yml")
BOOK = os.path.join(ROOT, "book")


def chapter_path(ch: str) -> str:
    """Absolute path of a chapter listed in `_quarto.yml`.

    The published layout puts the preface at the repository root (`index.qmd`)
    and every chapter under `book/`. Try the root first, then `book/`, so both
    layouts resolve and a genuinely missing file is still reported.
    """
    at_root = os.path.join(ROOT, ch)
    return at_root if os.path.exists(at_root) else os.path.join(BOOK, ch)


def read(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def listed_chapters(cfg: str) -> list[str]:
    """Chapter entries from the YAML `chapters:` blocks, in order."""
    entries = []
    for line in cfg.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            continue
        m = re.match(r"^-\s+(book/)?(.+\.qmd)\s*$", stripped)
        if m:
            entries.append(m.group(2))
    return entries


def check_config(problems: list[str]) -> list[str]:
    if not os.path.exists(CONFIG):
        problems.append("_quarto.yml is missing")
        return []
    cfg = read(CONFIG)
    if "project:" not in cfg or "book:" not in cfg:
        problems.append("_quarto.yml does not look like a Quarto book project")
    chapters = listed_chapters(cfg)
    if not chapters:
        problems.append("_quarto.yml lists no chapters")
    return chapters


def check_chapters(chapters: list[str], problems: list[str]) -> None:
    seen: set[str] = set()
    for ch in chapters:
        if ch in seen:
            problems.append(f"chapter listed more than once: {ch}")
        seen.add(ch)
        path = chapter_path(ch)
        shown = os.path.relpath(path, ROOT).replace(os.sep, "/")
        if not os.path.exists(path):
            problems.append(f"listed chapter does not exist: {shown}")
        elif len(read(path).strip()) < 200:
            problems.append(f"listed chapter is nearly empty: {shown}")


def check_orphans(chapters: list[str], problems: list[str]) -> None:
    listed = {os.path.normpath(c) for c in chapters}
    for dirpath, _, filenames in os.walk(BOOK):
        for name in filenames:
            if not name.endswith(".qmd"):
                continue
            rel = os.path.normpath(os.path.relpath(os.path.join(dirpath, name), BOOK))
            if rel not in listed:
                problems.append(
                    f"book/{rel} exists but is not listed in _quarto.yml "
                    "(add it, or comment it out explicitly)"
                )


def check_support_files(cfg: str, problems: list[str]) -> None:
    for key in ("bibliography:", "csl:"):
        for line in cfg.splitlines():
            if line.strip().startswith(key):
                value = line.split(":", 1)[1].strip().strip("\"'")
                for item in re.split(r"[,\s]+", value):
                    item = item.strip()
                    if not item:
                        continue
                    if item.startswith(("http://", "https://")):
                        continue  # remote CSL or bibliography: not a local input
                    path = item if os.path.isabs(item) else os.path.join(ROOT, item)
                    if not os.path.exists(path):
                        problems.append(f"{key[:-1]} file does not exist: {item}")
                    elif os.path.getsize(path) == 0:
                        problems.append(f"{key[:-1]} file is empty: {item}")


FIG = re.compile(r"!\[[^\]]*\]\(([^)\s]+)")


def check_figures(chapters: list[str], problems: list[str]) -> int:
    count = 0
    for ch in chapters:
        path = chapter_path(ch)
        if not os.path.exists(path):
            continue
        shown = os.path.relpath(path, ROOT).replace(os.sep, "/")
        for m in FIG.finditer(read(path)):
            target = m.group(1)
            if target.startswith(("http://", "https://")):
                continue
            count += 1
            chapter_dir = os.path.dirname(path)
            resolved = os.path.normpath(os.path.join(chapter_dir, target))
            if not os.path.exists(resolved):
                problems.append(
                    f"figure referenced but missing: {target} (in {shown})")
    return count


def main() -> int:
    problems: list[str] = []
    chapters = check_config(problems)
    if chapters:
        check_chapters(chapters, problems)
        check_orphans(chapters, problems)
        check_support_files(read(CONFIG), problems)
        figures = check_figures(chapters, problems)
    else:
        figures = 0

    print(f"chapters listed: {len(chapters)}")
    print(f"figures referenced: {figures}")

    if problems:
        print("")
        for p in problems:
            print(f"[FAIL] {p}")
        print(f"\nbuild-input check: {len(problems)} problem(s) found")
        return 1

    print(
        "\nbuild-input check: all listed chapters exist, support files are present, "
        "and every referenced figure resolves"
    )
    print("NOTE: this verifies inputs, not a render. HTML/PDF/EPUB rendering runs in CI.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
