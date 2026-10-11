#!/usr/bin/env python3
"""Calibrate the manuscript's style thresholds against a reference text.

WHY THIS EXISTS

The thresholds in STYLE.md (mean sentence 17-22 words, sd >= 10, share of
sentences of 8 words or fewer >= 17%) were set by the author as conventions.
They were NOT measured from any reference corpus, including the book named as
the register target. This script exists to replace convention with measurement.

USAGE

Put a plain-text copy of the reference book in the repository (it is not
committed, for copyright reasons), then:

    python scripts/calibrate_reference.py /path/to/reference.txt
    python scripts/calibrate_reference.py /path/to/reference.txt --chapter-split

The metrics are computed with exactly the same definitions as
scripts/check_style.py, so the output is directly comparable.

NOTES

* Front matter, tables of contents and reference lists will distort the result;
  use --skip-first N and --skip-last N to trim, and inspect the reported
  sentence count to confirm the trim worked.
* Prose and quoted dialogue have different distributions. Where the reference
  contains long quotations, the measured mean will be pulled toward the
  quoted material.
"""
from __future__ import annotations

import re
import statistics as st
import sys

SENT_SPLIT = r"(?<=[.!?])\s+"


def metrics(text: str) -> dict:
    sents = [s for s in re.split(SENT_SPLIT, text)
             if len(re.findall(r"[A-Za-z]", s)) > 3]
    lens = [len(re.findall(r"[A-Za-z']+", s)) for s in sents]
    paras = [p for p in re.split(r"\n\s*\n", text) if len(p.split()) > 15]
    plen = [len(p.split()) for p in paras]
    return {
        "sentences": len(sents),
        "words": len(re.findall(r"[A-Za-z']+", text)),
        "mean": st.mean(lens),
        "sd": st.pstdev(lens),
        "p10": sorted(lens)[max(0, len(lens) // 10)],
        "p50": st.median(lens),
        "p90": sorted(lens)[min(len(lens) - 1, len(lens) * 9 // 10)],
        "short_share": sum(1 for x in lens if x <= 8) / len(lens),
        "long_share": sum(1 for x in lens if x >= 30) / len(lens),
        "paragraphs": len(paras),
        "para_mean": st.mean(plen) if plen else float("nan"),
        "para_sd": st.pstdev(plen) if plen else float("nan"),
    }


def report(label: str, m: dict) -> None:
    print(f"\n{label}")
    print(f"  words {m['words']}   sentences {m['sentences']}   paragraphs {m['paragraphs']}")
    print(f"  mean sentence {m['mean']:.1f} words   sd {m['sd']:.1f}")
    print(f"  percentiles: p10 {m['p10']}   median {m['p50']}   p90 {m['p90']}")
    print(f"  share of sentences <= 8 words: {m['short_share']:.0%}")
    print(f"  share of sentences >= 30 words: {m['long_share']:.0%}")
    print(f"  mean paragraph {m['para_mean']:.0f} words   sd {m['para_sd']:.0f}")


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 1
    path = argv[0]
    skip_first = 0
    skip_last = 0
    if "--skip-first" in argv:
        skip_first = int(argv[argv.index("--skip-first") + 1])
    if "--skip-last" in argv:
        skip_last = int(argv[argv.index("--skip-last") + 1])

    raw = open(path, encoding="utf-8", errors="replace").read()
    # OCR line wrapping: join single newlines so sentence splitting works.
    text = re.sub(r"(?<!\n)\n(?!\n)", " ", raw)

    if skip_first or skip_last:
        chars = text.split(" ")
        print(f"[info] skipping first {skip_first} and last {skip_last} chunks of the text")
        text = " ".join(chars[skip_first: len(chars) - skip_last or None])

    report(f"reference: {path}", metrics(text))

    if "--chapter-split" in argv:
        parts = re.split(r"\n\s*\n\s*(?:Chapter|CHAPTER)\s+\d+", text)
        for i, part in enumerate(parts[1:], 1):
            if len(part.split()) > 800:
                report(f"  chapter {i}", metrics(part))

    print("\nCompare with the manuscript thresholds in STYLE.md:")
    print("  mean sentence target 17-22 | sd minimum 10 | short share minimum 17%")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
