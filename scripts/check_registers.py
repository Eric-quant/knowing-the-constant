#!/usr/bin/env python3
"""Validate the two claim registers.

The book keeps verified claims and the author's own constructions in separate files:

    verify/claims.csv       claims about the world, with a verification status
    verify/constructed.csv  devices this book proposes, with refutation conditions

Schemas (the files carry headers; this script is driven by them, not by fixed
column positions):

    claims.csv       claim_id, chapter, claim, value, source_doi,
                     verification_status, note
    constructed.csv  id, chapter, device, name, definition, motivation,
                     refutation_test, precondition, status

The script checks that the required columns exist, that identifiers are unique
within a register, that the status vocabulary is the one the book documents, that
every construction carries a refutation test and a precondition, and that the two
registers are not conflated.

It runs in CI before rendering, so a malformed register fails the build rather
than shipping.

Usage:
    python scripts/check_registers.py
    python scripts/check_registers.py --summary
Exit code 0 if both registers are valid, 1 otherwise.
"""
from __future__ import annotations

import csv
import os
import sys
from collections import Counter

CLAIMS = os.path.join("verify", "claims.csv")
CONSTRUCTED = os.path.join("verify", "constructed.csv")

CLAIM_COLUMNS = ["claim_id", "chapter", "claim", "value", "source_doi",
                 "verification_status", "note"]
CONSTRUCTED_COLUMNS = ["id", "chapter", "device", "name", "definition",
                       "motivation", "refutation_test", "precondition", "status"]

# The verification vocabulary as documented in Appendix C.
CLAIM_STATUSES = {
    "verified_metadata",
    "verified_via_text",
    "verified_via_secondary",
    "verified_via_preprint",
    "verified_absence",
    "verified_arithmetic",
    "verified_quotation",
    "verified_metric",
    "unverified_fulltext",
    "statistical_result",
    "interpretation",
    "unverified",
    "not_cited",
}

# Statuses that assert nothing about the world and therefore must carry a note.
NON_VERIFYING = {"interpretation", "unverified", "not_cited"}


def read_register(path: str) -> tuple[list[str], list[dict]]:
    if not os.path.exists(path):
        return [], []
    with open(path, encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        header = reader.fieldnames or []
        rows = [r for r in reader if any((v or "").strip() for v in r.values())]
    return header, rows


def check_header(path: str, header: list[str], required: list[str]) -> list[str]:
    problems = []
    if not header:
        return [f"{path}: file missing or has no header row"]
    missing = [c for c in required if c not in header]
    if missing:
        problems.append(f"{path}: missing required column(s): {', '.join(missing)}")
    return problems


def check_claims(header: list[str], rows: list[dict]) -> list[str]:
    problems = []
    seen: set[str] = set()
    for i, r in enumerate(rows, 2):
        cid = (r.get("claim_id") or "").strip()
        if not cid:
            problems.append(f"claims.csv line {i}: empty claim_id")
            continue
        if cid in seen:
            problems.append(f"claims.csv line {i}: duplicate identifier {cid}")
        seen.add(cid)
        chapter = (r.get("chapter") or "").strip()
        if not chapter.isdigit():
            problems.append(f"claims.csv line {i} ({cid}): chapter '{chapter}' is not a number")
        if len((r.get("claim") or "").strip()) < 12:
            problems.append(f"claims.csv line {i} ({cid}): claim text too short to be checkable")
        status = (r.get("verification_status") or "").strip()
        if status not in CLAIM_STATUSES:
            problems.append(
                f"claims.csv line {i} ({cid}): status '{status}' is not in the documented vocabulary"
            )
        if status and status not in NON_VERIFYING:
            has_doi = bool((r.get("source_doi") or "").strip())
            note = (r.get("note") or "")
            names_source = any(t in note.lower() for t in
                               ("arxiv", "http", "journal", "database", "openalex", "crossref",
                                "volume", "issue", "pages", "record", "publication", "source", "necsi"))
            if not has_doi and not names_source:
                problems.append(
                    f"claims.csv line {i} ({cid}): status '{status}' asserts verification but "
                    "records no source identifier in source_doi or note"
                )
        if not (r.get("note") or "").strip():
            problems.append(f"claims.csv line {i} ({cid}): no note on how it was checked")
    return problems


def check_constructed(header: list[str], rows: list[dict]) -> list[str]:
    problems = []
    seen: set[str] = set()
    for i, r in enumerate(rows, 2):
        bid = (r.get("id") or "").strip()
        if not bid:
            problems.append(f"constructed.csv line {i}: empty id")
            continue
        if bid in seen:
            problems.append(f"constructed.csv line {i}: duplicate identifier {bid}")
        seen.add(bid)
        for col in ("refutation_test", "precondition", "definition", "motivation"):
            if len((r.get(col) or "").strip()) < 12:
                problems.append(
                    f"constructed.csv line {i} ({bid}): '{col}' is empty or too short — "
                    "a construction without a refutation test is not falsifiable"
                )
    return problems


def check_separation(claim_rows: list[dict], cons_rows: list[dict]) -> list[str]:
    problems = []
    claim_ids = {(r.get("claim_id") or "").strip() for r in claim_rows}
    cons_ids = {(r.get("id") or "").strip() for r in cons_rows}
    overlap = {i for i in (claim_ids & cons_ids) if i}
    if overlap:
        problems.append(f"identifier appears in both registers: {sorted(overlap)}")
    return problems


def main(argv: list[str]) -> int:
    claim_header, claim_rows = read_register(CLAIMS)
    cons_header, cons_rows = read_register(CONSTRUCTED)

    problems: list[str] = []
    problems += check_header(CLAIMS, claim_header, CLAIM_COLUMNS)
    problems += check_header(CONSTRUCTED, cons_header, CONSTRUCTED_COLUMNS)
    if not problems:
        problems += check_claims(claim_header, claim_rows)
        problems += check_constructed(cons_header, cons_rows)
        problems += check_separation(claim_rows, cons_rows)

    print(f"claims.csv:      {len(claim_rows)} entries, {len(claim_header)} columns")
    print(f"constructed.csv: {len(cons_rows)} entries, {len(cons_header)} columns")

    if "--summary" in argv or not problems:
        counts = Counter((r.get("verification_status") or "").strip() for r in claim_rows)
        print("\nverification status distribution:")
        for status, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
            print(f"  {status:26} {n:3}")
        dev = Counter((r.get("status") or "").strip() for r in cons_rows)
        print("\nconstruction status distribution:")
        for status, n in sorted(dev.items()):
            print(f"  {status:26} {n:3}")

    if problems:
        print("")
        for p in problems:
            print(f"[FAIL] {p}")
        print(f"\nregister check: {len(problems)} problem(s) found")
        return 1

    print("\nregister check: both registers are well formed and remain separate")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
