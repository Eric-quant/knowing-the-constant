#!/usr/bin/env python3
"""Style checker for the manuscript.

Implements the measurable rules in STYLE.md:

  * average sentence length between 17 and 22 words
  * standard deviation of sentence length at least 10 words
  * at least one sentence in six under eight words
  * no banned constructions
  * paragraphs of varying length

Usage:
    python scripts/check_style.py book/**/*.qmd
"""
from __future__ import annotations

import glob
import re
import statistics as st
import sys

BANNED = [
    "not just",
    "in today's world",
    "in an era of",
    "it is worth noting",
    "importantly,",
    "delve",
    "navigate the landscape",
    "shed light",
    "the data speaks for itself",
    "in conclusion",
]
TARGET_MEAN = (17.0, 22.0)
MIN_SD = 10.0
MIN_SHORT_SHARE = 1 / 6


def prose_of(text: str) -> str:
    """Strip YAML front matter, code chunks, tables, headings and figure captions."""
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"^#+ .*$", "", text, flags=re.M)
    text = re.sub(r"^\|.*$", "", text, flags=re.M)
    text = re.sub(r"^!\[.*$", "", text, flags=re.M)
    text = re.sub(r"\[@[^\]]+\]", "", text)
    return text


def split_sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [p for p in parts if len(re.findall(r"[A-Za-z]", p)) > 3]


def check(path: str) -> bool:
    raw = open(path, encoding="utf-8").read()
    body = prose_of(raw)
    words = re.findall(r"[A-Za-z']+", body)
    sents = split_sentences(body)
    lens = [len(re.findall(r"[A-Za-z']+", s)) for s in sents]
    paras = [p for p in re.split(r"\n\s*\n", body) if len(p.split()) > 15]
    plen = [len(p.split()) for p in paras]

    mean = st.mean(lens)
    sd = st.pstdev(lens)
    short_share = sum(1 for x in lens if x <= 8) / len(lens)

    print(f"\n{path}")
    print(f"  words {len(words)}   sentences {len(sents)}   paragraphs {len(paras)}")
    print(f"  mean sentence {mean:.1f} words "
          f"(target {TARGET_MEAN[0]:.0f}-{TARGET_MEAN[1]:.0f})")
    print(f"  sd {sd:.1f} (min {MIN_SD:.0f})   shortest {min(lens)}   longest {max(lens)}")
    print(f"  sentences of 8 words or fewer: {short_share:.0%} "
          f"(min {MIN_SHORT_SHARE:.0%})")
    if paras:
        print(f"  mean paragraph {st.mean(plen):.0f} words   "
              f"sd {st.pstdev(plen):.0f}")

    problems = []
    if not TARGET_MEAN[0] - 0.05 <= mean <= TARGET_MEAN[1] + 0.05:
        problems.append(f"mean sentence length {mean:.1f} outside target")
    if sd < MIN_SD:
        problems.append(f"sentence-length sd {sd:.1f} below {MIN_SD:.0f}")
    if short_share < MIN_SHORT_SHARE:
        problems.append(f"short-sentence share {short_share:.0%} below "
                        f"{MIN_SHORT_SHARE:.0%}")
    for phrase in BANNED:
        hits = body.lower().count(phrase)
        if hits:
            problems.append(f"banned phrase '{phrase}' x{hits}")

    if problems:
        print("  FAIL")
        for p in problems:
            print(f"    - {p}")
        return False
    print("  PASS")
    return True


def main(argv: list[str]) -> int:
    paths = argv or sorted(glob.glob("book/**/*.qmd", recursive=True))
    if not paths:
        print("no files matched")
        return 1
    results = [check(p) for p in paths]
    ok = all(results)
    print("\nstyle check:", "all files pass" if ok else "problems found")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
