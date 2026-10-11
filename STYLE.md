# Style guide

The manuscript is written to these rules. They exist because the failure mode of this kind of
book is not being wrong. It is sounding like nobody wrote it.

## Voice

Write in plain, deliberate English for a reader who is intelligent, numerate, and not a
specialist in the field under discussion. Explain the mathematics in words first. Use a formula
only when the formula is the point.

Permitted: first person singular, when it records a judgement, a mistake, or a change of mind.
"The first time I read this I assumed..." is good. "In this chapter, we will explore..." is not.

Forbidden: "we" as a stand-in for the reader. The book has a narrator, and the narrator is a
person.

## Sentences

Target an **average sentence length of 17–22 words**, with a standard deviation of 10 or more.
That is the whole trick, and it cannot be faked by shortening everything: a uniform 18-word
paragraph reads exactly like machine output.

Practical rule: **at least one sentence in six should be under eight words.** Use it for the
turn, not for decoration.

> Volatility did not go up. It changed character.

Vary paragraph length too. A one-sentence paragraph is a tool, not a mistake.

## Constructions to avoid

These are the tells. Most of them are not wrong; they are just overused.

| Do not write | Why | Write instead |
| --- | --- | --- |
| "It is not just X, it is Y" | The single most common machine cadence in English nonfiction | State Y. If the contrast matters, give the evidence for it |
| "In today's world", "In an era of" | Empty framing | Start with the fact |
| "It is worth noting that", "Importantly" | Announces significance instead of showing it | Delete, then check whether the sentence still stands |
| Triads ("fast, cheap, and reliable") | Manufactured rhythm | Two items, or four |
| "delve into", "navigate the landscape", "shed light on" | Dead metaphors | Plain verbs |
| Every paragraph ending in a summary sentence | Reads like a slide deck | End on the sharpest point, not the roundest |
| "The data speaks for itself" | It never does | Say what you think the data shows |
| Rhetorical question followed by its answer | Predictable | Just answer it |

**Em dashes are fine.** English nonfiction uses them, and this manuscript uses them. The rule
about dashes that applies to the project's Chinese edition does not apply here. What matters is
that no punctuation habit becomes a tic: check for repeated sentence shapes, not repeated
glyphs.

## Claims and evidence

1. **Every quantitative claim gets a source**, inline or in `verify/refs.bib`.
2. **Every claim is entered in `verify/claims.csv`** with its verification status.
3. **If the full text was not available, say so in the sentence itself.** Not in a footnote, not
   in the appendix. In the sentence. Example: "The paper's own estimates are not quoted here:
   only the abstract and the citation record were accessible."
4. **Do not attribute a general criticism to a specific paper.** If a well-known objection was
   aimed at an idea rather than at this paper, say which one it was aimed at, or leave it out.
5. **Do not launder numbers through secondary sources.** If a figure circulates widely but does
   not appear in the original, write that it circulates and does not appear in the original.
6. **Give citation counts with the database and the snapshot date.** They are measurements, and
   measurements have provenance.
7. **Separate the claim from the tool.** Each chapter ends with a short section stating what the
   paper claimed, what survived, and which of its own preconditions it depends on.

## Terminology

Fix the vocabulary once and do not vary it for elegance. Repetition of a defined term is not a
style fault.

| Term | Definition used in this book |
| --- | --- |
| fat tail | A distribution whose tail decays slowly enough that large deviations occur far more often than under a Gaussian, and often slowly enough that some moments do not exist |
| Mediocristan / Extremistan | Shorthand for thin-tailed and fat-tailed domains of a random variable |
| ruin | An absorbing state: a loss from which one cannot continue |
| edge | A positive expected value in a bet or position, expressed relative to costs |
| log-optimal | The growth-maximising fraction under repeated compounding |
| discount | The factor applied to a theoretically optimal fraction to account for parameter uncertainty |
| fragility | Negative sensitivity to dispersion: a position that is harmed when uncertainty increases |
| precondition | A condition that must hold for a result to apply, stated with the result |

## Citations

Author-date, Chicago style, generated from `verify/refs.bib`. Cite the paper, not the book that
popularised it, unless the book is the object of discussion.

When the object of discussion is a paper whose text was not available, write "as cited in" only
if a quotation from the paper is reproduced elsewhere; otherwise describe the result and cite the
record.

## Numbers

- Percentages to one decimal place at most, and only when the extra digit is meaningful.
- Cite counts as integers, with database and date: "OpenAlex records 96 citations (snapshot
  2026-10)."
- Page numbers, volumes, and years exactly as recorded in `refs.bib`. No rounding.
- Where a figure is computed for this book, the caption says so: "computed for this book from the
  paper's stated parameters."

## Appendix: the Kahneman register

The manuscript targets the voice of *Thinking, Fast and Slow*. That book is the specification, so
it is worth saying what is actually being copied and what is not.

**Copied:**

1. **The narrator is a participant.** Kahneman reports his own errors, his own initial
   intuitions, and the moment a result became credible to him. The book's authority comes from
   the narrator being visibly subject to the effects being described.
2. **Anchoring claims in conditions rather than in confidence intervals.** His hedges are
   structural: this holds for this kind of problem, and here is the boundary. "This might be
   wrong" is not a hedge; it is noise.
3. **One sustained conceptual pair used everywhere.** System 1 and System 2 do work in every
   chapter. Here the pair is **the Constant** and **the Ledger**, and every chapter must use at
   least one of them in a way that changes what the chapter concludes — not as decoration.
4. **Illustration by experiment, not by analogy.** Kahneman's examples are studies with a
   manipulation and a result. This book's examples are computations the reader can run, with
   numbers stated in the text.
5. **Willingness to say a research programme failed.** His sections on priming and on ego
   depletion are, decades later, notably candid about the limits of the evidence. This book does
   the same for the stable-Paretian programme, for the long-memory literature, and for its own
   proposals.

**Not copied:**

- His subject matter, examples, or chapter structure.
- The device of labelling two mental "characters". This book's devices are measurement
  instruments, not agents, and they are never given voices.
- His length distribution. Kahneman's chapters are short and nearly uniform; this book
  deliberately alternates long expository chapters with short mathematical interludes.

**A concrete target for every chapter.** Somewhere in it, the narrator must record one of three
things: a judgement that changed, a computation that did not work the first time, or a reason to
distrust a result that the chapter otherwise uses. A chapter with none of the three reads like a
summary, and summaries are what the book exists to replace.

## Appendix: the creative/verified separation

This is a constructive book: it proposes models that no paper contains. The risk is obvious, and
it is managed by a hard rule.

> **A sentence that would be false if attributed to a source must be marked, in the text itself,
> as the book's own.**

Practically:

- Every use of the six constructed devices carries an inline phrase such as "the book's
  definition" or "proposed here".
- Constructed proposals go in `verify/constructed.csv`, verified facts in `verify/claims.csv`.
  Never both; never in the same row.
- A constructed proposal must state: definition, motivation, a test that could refute it, and its
  own precondition. A proposal without a refutation condition is not admitted to the manuscript.
- Constructions may be interesting, elegant, or useful. They may not be cited in the text as
  evidence for anything.

- The three thresholds in `scripts/check_style.py` — mean sentence length 17–22 words, sd ≥ 10, short-sentence share ≥ 17% — are author conventions, not measured from any reference text.
- To calibrate: `python scripts/calibrate_reference.py /path/to/reference.txt --skip-first 20000` (the reference text is not committed).
- TODO: replace the thresholds with the measured values and the measurement date, then delete this note.

