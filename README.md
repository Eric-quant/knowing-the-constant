# Knowing the Constant

[![Read online](https://img.shields.io/badge/read%20online-eric--quant.github.io-1f6feb?style=flat-square&logo=githubpages&logoColor=white)](https://eric-quant.github.io/knowing-the-constant/)
[![PDF](https://img.shields.io/badge/PDF-download-b30b0b?style=flat-square&logo=adobeacrobatreader&logoColor=white)](https://eric-quant.github.io/knowing-the-constant/Knowing-the-Constant.pdf)
[![EPUB](https://img.shields.io/badge/EPUB-download-2e7d32?style=flat-square&logo=bookstack&logoColor=white)](https://eric-quant.github.io/knowing-the-constant/Knowing-the-Constant.epub)
[![Build and publish](https://github.com/Eric-quant/knowing-the-constant/actions/workflows/publish.yml/badge.svg)](https://github.com/Eric-quant/knowing-the-constant/actions/workflows/publish.yml)
[![Licence: CC BY-NC-SA 4.0](https://img.shields.io/badge/licence-CC%20BY--NC--SA%204.0-lightgrey?style=flat-square)](LICENSE)

**Mandelbrot, Taleb, and Thorp on Shape, Survival, and Bet Sizing in a Fat-Tailed World**

A book about three people who never worked together, never cited each other, and spent their
careers answering different versions of the same question: what do you do when the world will
not average out?

The title comes from chapter 16 of the *Tao Te Ching*: 知常曰明 — to know the constant is
called enlightenment — followed by the line that gives the book its spine: 不知常，妄作凶.
Not knowing the constant leads to reckless action, and reckless action ends badly.

## What this book is, and what it is not

It is a reading of **nine papers**, three per author, chosen because they carry the load:

| Part | Papers |
| --- | --- |
| I — Shape | Mandelbrot (1963) on fat tails; Mandelbrot (1967) on coastlines; Mandelbrot & Van Ness (1968) on fractional Brownian motion |
| II — Survival | Taleb (2009) on the fourth quadrant; Taleb et al. (2014) on the precautionary principle; Cirillo & Taleb (2020) on the tail risk of epidemics |
| III — Bets | Thorp (1961) on blackjack; Thorp (1969) on optimal betting; Thorp (1997) on the Kelly criterion in practice |
| IV — Synthesis | Three layers, five points of agreement, three real disagreements, and the boundary conditions |

It is **not** a biography, and it is not a summary of three famous books. The unit of analysis is
the paper, because a paper can be checked and a reputation cannot.

## The one thing this book does differently

**Every quantitative claim is traceable, and every gap is labelled.**

When the full text of a paper could not be obtained, this book says so and does not quote it.
When a number circulates widely but cannot be found in the original source, the book says so and
does not use it. When a criticism is aimed at a general idea rather than at the specific paper
under discussion, the book says so and does not attribute it.

The claims are kept in a machine-readable file: [`verify/claims.csv`](verify/claims.csv).
References are kept in [`verify/refs.bib`](verify/refs.bib). If a claim is wrong, the file says
what it was based on, which makes it possible to correct.

This is not modesty. It is the argument of the book applied to the book.

## Repository layout

```
book/            chapter sources (English, source of truth)
figures/         generated PNGs, English labels only
scripts/         figure-generation scripts (deterministic, no external data)
verify/          claims.csv, constructed.csv, refs.bib, and the vendored CSL
STYLE.md         the style guide this manuscript is written to
_quarto.yml      build configuration
styles.css       HTML site styling
favicon.png      site icon
```

## Building

Requires [Quarto](https://quarto.org). Then:

```bash
quarto preview          # local preview
quarto render           # build HTML, PDF, and EPUB into _book/
```

Each `quarto render --to <format>` clears `_book/`, so when building the formats one at a time,
collect each format's output before rendering the next. CI does exactly that — see
[`publish.yml`](.github/workflows/publish.yml).

Figures are regenerated with:

```bash
python scripts/make_figures.py
```

Every figure in this book is computed from the formulas or parameters in the papers it
describes. **No figure is reproduced from any published paper.**

## Licensing

This project is deliberately split-licensed:

- **Prose and figures:** CC BY-NC-SA 4.0 — share and adapt freely for non-commercial use, with
  attribution, under the same licence.
- **Code and scripts:** MIT.

See [LICENSE](LICENSE) for details.

## Status

**Manuscript complete in draft: 32 chapters in four parts, four appendices and a preface, 37 files,
about 161,000 words against a target of 160,000.** Every file passes the prose gate, the registers
are well formed and separate, and every build input resolves. Three checks, each runnable:

```bash
python scripts/check_style.py          # per-file prose gate
python scripts/check_registers.py      # claims.csv and constructed.csv, and their separation
python scripts/check_build_inputs.py   # chapters, support files, figures
```

**One thing is not done, and is recorded here rather than left implicit.**

- **The six constructed devices are proposals. None has been tested.** Their status in
  [`verify/constructed.csv`](verify/constructed.csv) is `proposal` on every row, and each carries a
  refutation test. The closing chapter names the three studies that would test them.

Two earlier gaps are now closed by CI rather than on the authoring machine: the HTML, PDF and EPUB
are rendered on every push to `main`, and the book is published — readable at
<https://eric-quant.github.io/knowing-the-constant/>, with the PDF and EPUB attached to each
[release](https://github.com/Eric-quant/knowing-the-constant/releases).

Anything in this repository may still change, including the argument. The registers are what make
the changes checkable.

## Errata and challenges

If a claim is wrong, or the source given for it does not say what this book says it says, open
an issue. Two templates are provided: `Erratum` and `Verification challenge`. The second one is
the more useful of the two.
