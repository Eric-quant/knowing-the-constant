# Publishing this repository

**Status: published.** This file is kept as the record of how publication was planned. The plan has
since been executed:

- Account: **Eric-quant** — created.
- Repository: <https://github.com/Eric-quant/knowing-the-constant> — created and pushed.
- First CI run: **passed** — the style gate, the register check, the build-input check, and the
  HTML, PDF and EPUB renders all succeeded.
- Live site: <https://eric-quant.github.io/knowing-the-constant/>
- Downloads: the PDF and EPUB are attached to each [release](https://github.com/Eric-quant/knowing-the-constant/releases).

The sections below record the original plan and the questions that were open at the time. They are
no longer blockers; they are kept because the reasoning is part of the record.

---

**Original status: deferred. The manuscript comes first.**

The decision, recorded so that it is auditable rather than implicit: publication is paused until the
book is finished, and the two blockers below are recorded but not acted on.

Reasons given by the author of the work:

- A GitHub account does not exist yet.
- GitHub is not reliably reachable from the author's location. Whether `git` itself is usable there has
  not been tested; `git ls-remote` against a public repository is the one command that settles it.
- If reachability proves to be a real constraint, the alternatives are a mirror on another host
  (Gitee, Codeberg, GitLab), pushing from a machine that can reach GitHub, or changing the objective's
  target host. **None of these is done unilaterally; each changes the deliverable.**

Everything needed for publication is in place and is checked by scripts. What follows is what a
future session, or the author, needs in order to finish it.

## 1. The account name

The account name to use is **Eric-quant**. The `OWNER` placeholder was carried in these files:

- `_quarto.yml` — the site URL
- `LICENSE` — the copyright line
- `OUTLINE.md` — the publishing plan

**No GitHub account exists for this project yet**, so the placeholder has been left in place rather
than replaced with an invented name. Nothing in the build depends on it: Quarto renders HTML, PDF
and EPUB with a placeholder site URL; the field only affects canonical links and the sitemap.

**To complete it, when an account exists:**

1. Create the repository, e.g. `https://github.com/Eric-quant/knowing-the-constant`.
2. Done in this workspace: `OWNER` was replaced with `Eric-quant` in `_quarto.yml` and `LICENSE`. In
   `OUTLINE.md` the placeholder appeared only in explanatory prose and that prose has been updated.
3. Nothing else needs substituting. `_quarto.yml` has no `site-url` key, and `README.md` contains no
   clone command; Quarto does not require a site URL for this build, and the Pages URL is produced by
   the workflow in step 4.
4. Push to `main`. The workflow at `.github/workflows/publish.yml` runs on push and will:
   regenerate every figure from its script, run the style gate, run the register check, run the
   build-input check, render HTML, PDF and EPUB, deploy the HTML to GitHub Pages, and attach the
   EPUB and PDF to a release.

## 2. The three-format build

`quarto render` produces the HTML, the PDF and the EPUB. **It has not been run locally**: Quarto is
not installed in the environment this repository was written in, and the PDF additionally requires a
TeX distribution.

What *has* been verified locally is every input the render needs:

```
python scripts/check_build_inputs.py
```

That script checks that `_quarto.yml` parses, that every listed chapter exists and is non-empty,
that no chapter file is silently orphaned, that the bibliography and CSL files exist, and that every
figure referenced from a chapter resolves. It verifies inputs, not a render, and it says so in its
output.

**The build itself therefore runs in CI, and the first CI run is the first verification of the
render.** To run it locally instead:

```
python scripts/check_style.py           # prose gate
python scripts/check_registers.py       # the two claim registers
python scripts/check_build_inputs.py    # build inputs
python scripts/make_figures.py          # regenerate figures from their scripts
quarto render --to html
quarto render --to pdf                  # requires TeX
quarto render --to epub
```

## The chosen verification path

**Decision: the first render happens in CI, at publication time.** No local Quarto installation is
attempted. The reasons, recorded so that the choice is auditable rather than implicit:

- The authoring environment has no network egress for shell processes, so Quarto cannot be
  downloaded there. Two clients were tried: `Invoke-WebRequest` failed during the TLS handshake, and
  `curl.exe` failed with Schannel `SEC_E_NO_CREDENTIALS`. Neither failure is a mistyped URL.
- The manuscript is still being expanded, so any artefact rendered today would be rebuilt anyway.
- The workflow already sequences the four checks and the three renders, so CI is the cheapest place
  for the first build to run.

**What this means for a reader arriving at the repository.** The configuration and inputs are
verified by `scripts/check_build_inputs.py`; the renders are not. `.github/workflows/publish.yml`
runs them on the first push to `main` and attaches the EPUB and PDF to a release.

## What is deliberately not claimed

The objective for this book includes "a Quarto build that produces HTML, PDF and EPUB". At the time
of writing, **that build is configured but not verified**, because the renderer is not available in
the authoring environment. The distinction is recorded here rather than left implicit, in the same
way the book's own registers record which claims were read and which were inferred.
