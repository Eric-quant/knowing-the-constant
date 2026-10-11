# Knowing the Constant — outline and specification

**Subtitle.** Mandelbrot, Taleb, and Thorp on Shape, Survival, and Bet Sizing in a Fat-Tailed World

**Target length.** 160,000 words of body text, excluding front matter, appendices, references,
and figure captions. That is roughly 32 chapters at 5,000 words each.

**Positioning.** This is not a survey and not a biography. It is a **constructive** book: it reads
nine papers closely, and then builds something out of them that none of the three authors built —
a single decision architecture, with its own definitions, its own procedures, and its own
failure conditions. Everything built is labelled as built, and kept in a separate register from
everything verified.

**Voice.** Daniel Kahneman's, as a target and not as an imitation. See `STYLE.md` for the
operational rules. The three properties that matter most:

1. **The narrator is present.** "I changed my mind about this" is a legitimate sentence. So is
   "I could not get this to work until I saw the following." The book argues in front of the
   reader.
2. **Claims arrive with their conditions attached.** Kahneman's prose hedges in a specific way:
   not "this might be wrong" but "this holds under these conditions, and here is what happens
   outside them."
3. **One sustained metaphor, used consistently.** Kahneman has System 1 and System 2. This book
   has **the Constant** and **the Ledger** (defined below). A metaphor earns its place by doing
   analytical work in every chapter, not by being memorable.

---

## Part 0 — The architecture of the book

Four parts, plus interleaved short chapters that carry the mathematics and keep the pace varied.
The long chapters are expository; the short ones (1,500–2,500 words) are where the machinery is
introduced and where the reader is asked to run a calculation.

| Part | Chapters | Words | Job |
| --- | --- | --- | --- |
| I — Shape | 1–8 | 38,000 | What the world is made of: thick tails, scale invariance, memory |
| II — Survival | 9–17 | 42,000 | What to do when the world cannot be averaged: ruin, proof burdens, non-existent means |
| III — Bets | 18–25 | 38,000 | What to do when an edge is real: detection, sizing, execution |
| IV — Construction | 26–32 | 42,000 | The book's own contribution: the Constant, the Ledger, the ordering |

---

## Part I — Shape (38,000 words)

The job of Part I is to establish that the world is not Gaussian, and then to show that this is
not a fact about numbers but a fact about **what can be summarised at all**.

| Ch | Title | Words | Core content |
| --- | --- | --- | --- |
| 1 | The tail that would not go away | 5,000 | Mandelbrot 1963; the Gaussian default; the variance that does not exist |
| 2 | How long is a coastline | 5,000 | Mandelbrot 1967; length as an undefined quantity; dimension as a replacement |
| 3 | Memory in a random walk | 5,000 | Mandelbrot & Van Ness 1968; long memory; why the tool left finance and came back |
| 4 | *Interlude: three ways for a number to fail* | 2,500 | The book's first original device: the failure taxonomy (noise / undefined / non-existent) |
| 5 | The estimator problem | 4,500 | Taqqu et al. 1995; Franzke et al. 2012; why an exponent is not a property |
| 6 | The scale-span rule | 3,500 | **Original:** a reporting standard for exponents, with a worked test |
| 7 | What a fractal is not | 4,000 | The nine misuses of dimension, mapped to their sources |
| 8 | Shape as a precondition | 4,000 | **Original:** shape claims as preconditions, not conclusions |

## Part II — Survival (42,000 words)

The job of Part II is to move from description to standard: not "what is the world like" but
"given that, what counts as a reason to act".

| Ch | Title | Words | Core content |
| --- | --- | --- | --- |
| 9 | Four quadrants, and what they are not | 5,000 | Taleb 2009; the two axes; the ludic fallacy |
| 10 | *Interlude: the two kinds of uncertainty* | 2,500 | Estimable vs non-estimable; the book's working distinction |
| 11 | The burden of proof | 5,000 | Taleb et al. 2014; irreversibility; the infinite-harm argument |
| 12 | When the average does not exist | 5,000 | Cirillo & Taleb 2020; mean divergence; the distribution-family dependence |
| 13 | *Interlude: existence before precision* | 2,500 | **Original:** the existence test, stated as a procedure |
| 14-17 | Chapters 13, 14 and 15 written (existence-before-precision; the existence-estimability grid; convexity and fragility), Chapter 16 written (irreversibility ledger with four mechanisms and five bounding moves); three register entries added | 46,000 |
| 18 | Chapter 17 written (precaution applied in four domains, with an explicit negative list); Chapters 15 and 16 style-balanced by computed sentence budgets rather than by trial and error; Part II body draft complete | 49,000 |
| 19 | Part III opened: Chapter 18 written (state dependence, the three kinds of advantage, computed versus estimated edges, graded); Chapter 17 style-balanced and its banned phrase removed | 52,000 |
| 20 | Chapter 19 interlude written (growth is multiplicative, the half-variance approximation and its failure in fat tails); Chapter 17 repaired using a revised balancing rule that adds extreme short sentences to raise both spread and short-share; Part III chapters enabled in the build | 54,000 |
| 21 | Chapter 20 written (objective-function switch, interior optimum, the two-times rule, the asymmetry of parameter error); Chapters 17 and 19 balanced; four claims registered | 57,000 |
| 22 | Chapter 21 written, proposing the discount function (device D1) with an explicit list of where its derivation is loose; Chapters 19 and 20 rebalanced using a computed sentence budget | 60,000 |
| 23 | Chapter 22 written (optimisers as error amplifiers, three responses, and why awareness of unreliability does not by itself change the objective); Chapter 20 spread widened; Chapter 21 rebalanced | 63,000 |
| 24 | Chapter 23 written (costs, capacity, visibility, and the seven practical rules); Chapters 20 to 22 rebalanced with a stronger spread recipe | 66,000 |
| 25 | Chapter 24 interlude written (the detection arithmetic, three degradations, and the sizing loophole); Chapters 20 and 23 rebalanced | 69,000 |
| 26 | Chapter 25 written (four decay mechanisms, durability by source, the success paradox, three obligations); Part III body draft complete; Chapters 23 and 24 rebalanced | 72,000 |
| 27 | Chapter 27 written (the ledger as an instrument, the forced order of the three devices, three possible outputs including refusal, and two failure modes); Chapter 25 rebalanced | 75,000 |
| 28 | Chapter 28 written (four-column reading protocol, the naming test, the transfer rule, and three failure modes including one the author commits); Chapter 27 rebalanced | 78,000 |
| 29 | Chapter 29 written (the forced ordering, its three outputs, its one falsifiable prediction, and the entangling case where stages cannot be separated); Chapters 27 and 28 rebalanced | 81,000 |
| 30 | Chapter 30 written (three worked cases ending in Bound, Bound and Avoid, with the scale-availability criterion for reaching stage three); Chapters 27 and 29 rebalanced | 84,000 |
| 31 | Chapter 31 written (the failure table with signals, the institutional demand for a number, four abandonment settings, and an explicit list of what the book does not claim); Chapter 29 rebalanced with the minimum necessary addition | 87,000 |
| 32 | Chapter 32 written. **All 32 chapters of the body now exist in draft.** Remaining: four appendices, three figures to be generated, and the GitHub publication (Actions workflow, issue templates, OWNER substitution, Quarto HTML/PDF/EPUB build verification) | 90,000 |
| 33 | Appendix A (timeline) and Appendix B (glossary, including the six constructed devices in one table and a list of terms the book avoids) written and enabled; Chapter 32 rebalanced | 92,000 |
| 34 | Appendices C (the two registers, the five verification classes, the deliberately uncited list, and how to check the book) and D (four reading paths plus an explicit gap list) written and enabled; Appendices A and B rebalanced | 95,000 |
| 35-38 | Appendices A-D all passing the style gate. Systematic expansion begun: Chapters 1, 2, 3, 5 and 6 each gained a substantive new section. **Whole manuscript now 64419 words (40.3% of target)**; expansion continues chapter by chapter | 64419 |
| 39 | Corrected a reporting error: earlier rounds misattributed style-check failures because two chapter filenames contain the string 'fail' and the output was being filtered. Chapters 4 to 8 expanded and repaired; manuscript now 65155 words (40.7%) | 65155 |
| 40 | The self-check now imports `scripts/check_style.py` instead of reimplementing it, so there is one measurement definition. Chapters 9 to 12 each gained a section. Manuscript 66343 words (41.5%) | 66343 |
| 14 | The Existence–Estimability grid | 5,000 | **Original:** a 2×2 of (does it exist?) × (can it be estimated?) with four action regimes |
| 15 | What convexity is, and what it is not | 5,000 | Convexity, fragility, and the two ways people mis-buy insurance |
| 16 | The irreversibility ledger | 5,000 | **Original:** an accounting device for classifying exposures |
| 17 | Precaution without paralysis | 5,000 | Applied: climate, technology, medicine, personal decisions; where the grid says "no" |

## Part III — Bets (38,000 words)

The job of Part III is execution: given a real edge, what do you do on Monday morning.

| Ch | Title | Words | Core content |
| --- | --- | --- | --- |
| 18 | Finding an edge | 5,000 | Thorp 1961; state-dependence; the condition where a game is beatable |
| 19 | *Interlude: expected value is not growth* | 2,000 | The arithmetic/geometric distinction in one page and one figure |
| 20 | How much to bet | 5,000 | Thorp 1969; internal optimum; the two-times rule |
| 21 | The discount | 5,000 | **Original:** the discount function, with assumptions and a sensitivity table |
| 22 | Estimation risk as a first-class input | 4,500 | Why the input distribution matters more than the point estimate |
| 23 | Execution: costs, capacity, and being noticed | 5,000 | Thorp 1997; the seven practical rules; why half-Kelly became the default |
| 24 | *Interlude: the sampling problem of skill* | 2,500 | How many observations are needed before a track record means anything |
| 25 | When the edge decays | 5,000 | Erosion, crowding, and the maintenance obligation |

## Part IV — Construction (42,000 words)

This is where the book stops reading and starts building. It is the part that justifies the
title, and it must be held to a higher evidentiary standard than the rest: everything here is
labelled as the book's own proposal, with its own refutation conditions.

| Ch | Title | Words | Core content |
| --- | --- | --- | --- |
| 26 | The Constant | 6,000 | **Original:** definition of the Constant, three grades, and the test that separates them |
| 27 | The Ledger | 5,000 | **Original:** the book's central metaphor as an instrument; how the two devices interact |
| 28 | Claim, tool, vocabulary, technique | 5,000 | **Original:** the four-column reading protocol for research |
| 29 | The ordering: Ruin → Estimability → Size | 6,000 | **Original:** the decision procedure, stated formally, with a flowchart |
| 30 | The architecture applied: three worked cases | 6,000 | One financial, one technological, one personal |
| 31 | Where this architecture fails | 5,000 | Adversarial chapter, written against the book's own proposal |
| 32 | Knowing the constant | 4,000 | Closing essay on what stays invariant and how little that is |

Plus appendices: timeline; glossary; claims register; creative-claims register; figure
provenance; further reading.

---

## The original contributions, stated precisely

The book proposes six things. Each is given a definition, a motivation, a test, and a
stated precondition. **None is presented as established; all are presented as constructed.**

### 1. The Constant (K)

**Definition.** A *constant* is a quantity, relation, or procedure that survives a specified
transformation of the observing conditions. A constant is always indexed to a transformation
class: K(scale), K(distribution family), K(instrument), K(regime).

**Three grades.**

- **Grade I — scale constant.** Survives a change of measurement scale (Mandelbrot's dimension
  is one, within a stated span).
- **Grade II — distributional constant.** Survives a change of the assumed distribution family
  (the qualitative shape claim "tails are thick" is one; a fitted exponent is not).
- **Grade III — structural constant.** Survives a change of regime, instrument, or population
  (the survival-first ordering is proposed as Grade III).

**Test.** For any candidate constant, name the transformation it is supposed to survive, then
apply the transformation and re-measure. Grade I claims are refuted by a scale sweep; Grade II
claims by a family sweep; Grade III claims by regime change or out-of-sample survival.

**Motivation.** The nine papers share a failure mode: a result that is robust at one grade is
quoted at a higher grade. "Returns are fat-tailed" (Grade II) gets quoted as an exponent
(Grade I), which gets quoted as a rule for sizing (Grade III).

**Precondition.** The transformation class must be specified in advance. A constant with no
stated transformation is not a constant; it is a slogan.

### 2. The Existence–Estimability grid

**Definition.** Two binary questions asked in order:

1. Does the quantity exist? (does the defining integral converge?)
2. Can it be estimated from available data?

**Four regimes.**

| | Estimable | Not estimable |
| --- | --- | --- |
| **Exists** | *Compute.* Estimate, report with an interval, act proportionally | *Bound.* Do not point-estimate; use bounds and worst cases |
| **Does not exist** | *Replace.* The formula has no object; change the question | *Avoid.* No quantity, no estimate: use structural criteria only |

**Motivation.** Most disagreement about risk is really disagreement about which cell a problem
sits in, argued as though it were about the numbers.

**Test.** State the quantity's defining expression; check convergence; then run two independent
estimators and compare. Disagreement between estimators is evidence for the "not estimable"
column, not a nuisance to be averaged away.

**Precondition.** The user must be willing to abandon a quantity. Regime three is empty of
numbers on purpose.

### 3. The ordering: Ruin → Estimability → Size

**Definition.** A three-stage decision procedure, executed in fixed order.

1. **Ruin screen.** Enumerate irreversible exposures; any option that can produce an absorbing
   state is either removed or structurally altered (bounded loss) before anything else is
   considered.
2. **Estimability screen.** Classify the problem in the Existence–Estimability grid.
3. **Size.** Only in the *Compute* regime does the optimal-fraction machinery apply, and only
   with a discount.

**Why the order cannot change.** Sizing before the ruin screen means computing a fraction for a
problem that may not have a tomorrow. Sizing before the estimability screen means computing a
fraction from a quantity whose defining integral may not converge.

**Test.** The procedure makes a specific prediction: decision quality should be more sensitive
to errors in stages 1 and 2 than to errors in stage 3. This is testable, at least in simulation,
and Chapter 31 attacks it.

**Precondition.** Only applies to decisions that are repeated or that carry an absorbing state.
For a single, reversible decision, the ordering adds cost without benefit.

### 4. The discount function

**Proposed model.** For a log-optimal fraction estimated as f̂ = μ̂ / σ̂², the book proposes a
discount

[F] δ = 1 / (1 + κ · CV(μ̂)²), with CV(μ̂) = SE(μ̂) / μ̂

so that the executed fraction is f = δ · f̂. κ = 1 corresponds to a shrinkage rule; κ > 1 is
appropriate where estimation is itself unstable (fat tails, short samples, regime change).

**Motivation.** The standard practical answer is "use half Kelly", a constant with no argument
behind it. The discount function makes the size of the discount a function of how well the
parameter is known, which is the honest input.

**Properties asserted (and to be checked).** δ → 1 as SE(μ̂) → 0; δ falls quadratically with
relative uncertainty; δ = 0.5 requires CV ≈ 1, so half-Kelly is the right answer only for one
specific (and rather poor) level of knowledge. Chapter 21 derives the properties and states
where the derivation is loose.

**Precondition.** Requires a usable estimate of SE(μ̂), which is exactly what is unavailable in
the *Bound* and *Avoid* regimes. **The discount function is therefore not a universal rule; it
is the third-stage instrument of the *Compute* regime.**

### 5. The four-column reading protocol

**Definition.** Every research result is decomposed into:

| Column | Question | Transfer of trust |
| --- | --- | --- |
| **Claim** | What does it assert about the world? | Lowest: decays as evidence accumulates |
| **Tool** | What does it make possible to ask or compute? | Highest: usually outlives the claim |
| **Vocabulary** | What does it name that was unnamed? | Durable but can be emptied by overuse |
| **Technique** | What procedure does it specify? | Durable until superseded |

**Motivation.** The nine papers each show the same pattern: claim weakened, tool retained. A
reader with four columns stops discarding papers whose claims failed.

**Test.** For any paper, fill the four columns, then find one later paper that uses the tool while
rejecting the claim. If none can be found, the tool column is probably imaginary.

### 6. The irreversibility ledger

**Definition.** A two-sided account. On one side, exposures that are reversible at acceptable
cost; on the other, exposures that can produce an absorbing state. The ledger's only rule:
**the irreversible side is closed to new entries until it is empty or bounded.**

**Template.** Each entry records: the exposure, the mechanism of irreversibility, the cost of
exit, and the bound (if any) that converts it into a reversible one.

**Motivation.** Reversibility is easier to assess than probability, so it is the right first
question, and it is a question about structure rather than about forecasts.

**Precondition.** Requires a realistic estimate of exit cost, which people systematically
underestimate in illiquid or socially committed positions.

---

## Keeping the two registers apart

The book's rigour depends on never blurring what was read with what was built.

| Register | File | Contents | Evidence standard |
| --- | --- | --- | --- |
| **Verified claims** | `verify/claims.csv` | Statements about published work | Source required; status recorded; gaps labelled |
| **Constructed claims** | `verify/constructed.csv` | The six proposals above and everything derived from them | Labelled as the book's own; assumptions stated; refutation conditions given |

A constructed claim may be interesting. It may not be cited as though it were a finding.
Every chapter that uses one of the six devices says so at the point of use, in the text.

---

## Production plan

**Order adopted: hybrid A→B.** Write Chapters 1–3 first so that Part I is a complete, readable
unit. Then, before starting Part II, write Chapter 26 (*The Constant*) to internal-final standard,
because every later chapter will use the device it defines. After that, proceed in order.

| Milestone | Content | Words |
| --- | --- | --- |
| M1 | Ch 1–3 (Part I core) + figures + build pipeline green | 15,000 |
| M1b | Ch 26 written as the internal standard (ahead of order) | +6,000 |
| M2 | Part I complete | 38,000 |
| M3 | Part II complete | 80,000 |
| M4 | Part III complete | 118,000 |
| M5 | Part IV complete; v1.0 release with EPUB/PDF | 160,000 |

### Progress log

| Round | Delivered | Body words |
| --- | --- | --- |
| 1 | Preface (`index.qmd`); Chapter 1 complete draft (15 sections, 1 figure); build config limited to existing chapters so the project renders; style checker and figure generator working | 5,171 |
| 2 | Chapter 1 finalized at budget (17 sections, 2 figures); Chapter 2 complete draft (12 sections, Koch figure) enabled in the build; 7 further claims registered | 7,982 |
| 3 | Chapter 2 finalized at budget (15 sections, 3 figures total); Chapter 3 drafted (memory and long dependence); 1 further claim registered | 12,000 |
| 4 | Chapter 3 expanded (15 sections); Chapter 4 interlude written, defining device F1 in full; 7 further claims registered | 15,000 |
| 5 | Chapter 2 expanded (17 sections); Chapter 5 written on estimator unreliability; 3 further claims registered | 18,000 |
| 6 | Chapter 5 expanded (identifiability vs uncertainty; five-step grid protocol); Chapter 6 written, defending device S1 against three attacks and two false positives | 21,000 |
| 7 | Part I drafted: Chapter 7 (nine misuse patterns with sources) and Chapter 8 (shape claims as preconditions, four-line sheet) written; Part I now eight chapters | 30,000 |
| 8 | Chapter 26 written ahead of order as the internal standard: definition of the Constant, four transformation classes, three grades with tests, five documented instances of grade inflation, three refutation conditions, and the device graded against itself (grade II) | 34,000 |
| 9 | Part II opened: Chapter 9 written on the two axes, the four cells, the ludic fallacy, the verified absence of commentaries, and the paper's own hedges; 5 claims registered | 37,000 |
| 10 | Chapter 10 interlude written (three cases, the deferral fallacy, the two-question table); Chapters 7 and 8 thickened toward budget | 30,000 |
| 11-12 | Round 11 established ground truth (10 of 12 files passing) and repaired Chapter 4; Round 12 wrote Chapter 11 | 39,000 |
| 13 | Chapter 12 written (moments and the missing mean, the distributional objection, the adjacent-pages debate, graded against Chapter 26); Chapter 11 style repaired | 42,000 |


Cadence: three chapters per working session, then a style and claims check. Every session ends
with `python scripts/check_style.py` and a claims-register update.

**Quality gates (automated):**

1. `check_style.py` — sentence-length distribution, paragraph variation, banned constructions.
2. `check_claims.py` — every `[@cite]` key exists in `refs.bib`; every chapter's quantitative
   claims appear in one of the two registers.
3. `check_voice.py` — flags chapter-level tells: uniform paragraph lengths, every paragraph
   ending in a summary, and three-part lists at paragraph ends.
4. Figure provenance check — no figure file without a script that generates it.

**Where the 160,000 words come from.** 32 chapters averaging 5,000 words is the plan, but the
count is not the goal. The chapters are sized so that each one can carry an argument from
question to boundary condition without padding. If a chapter cannot reach 4,000 words honestly,
it merges with its neighbour rather than growing.
| 61-85 | Expansion continued at roughly six sections per round. The manuscript reached 159651 words (99.8 per cent of the target) across 37 files, with the style gate, the register check and the build-input check all passing. Publication deferred; the first render is configured to run in CI. | 159651 |

## Final state

*Recorded after the manuscript reached its word target. Everything below is checkable by running the
three scripts named.*

**Manuscript.** 37 files, 161571 words (raw count including markup) against a target of
160,000 — 101.0 per cent. Thirty-two chapters in four parts plus four appendices and a preface,
all listed in `_quarto.yml` in reading order.

**Checks, all passing.**

- `scripts/check_style.py` — per-file prose gate (mean sentence 17–22 words, sd at least 10, at least
  17 per cent of sentences of eight words or fewer, no banned phrases).
- `scripts/check_registers.py` — `verify/claims.csv` (80 entries) and `verify/constructed.csv`
  (13 entries) well formed, no identifier collisions, construction fields present, and the two files
  kept separate.
- `scripts/check_build_inputs.py` — every listed chapter exists and is non-empty, no orphaned chapter
  files, bibliography and CSL present, every referenced figure resolves.

**Constructed devices.** Six, each with a definition, a motivation, a precondition and a refutation test
in `verify/constructed.csv`. **Status of every entry: `proposal`. None has been tested**, and the
book says so wherever they appear and in the closing chapter's self-grading.

**Figures.** Two, generated by `scripts/make_figures.py`; no figure appears in the manuscript without a
generating script.

**Not done, with its precondition.**

- GitHub publication — the account name is known (`Eric-quant`) and the `OWNER` placeholder has been
  substituted in `_quarto.yml` and `LICENSE`, so the file set is ready to push. What remains is creating
  the repository and pushing from a machine that can reach GitHub, which this authoring environment cannot
  do: a hosts-file entry redirects `github.com` to `127.0.0.1` and `git` is not installed.
  `PUBLISHING.md` records the alternatives, none of which has been taken unilaterally.
- Quarto HTML/PDF/EPUB render — never executed locally, because the authoring environment has no network
  egress for shell processes and Quarto cannot be installed there. By the author's decision the first
  render happens in CI. `.github/workflows/publish.yml` runs the four checks and the three renders and
  attaches the EPUB and PDF to a release.
- Testing the constructed devices — requires the three studies named in the closing chapter, none of
  which has been run.

