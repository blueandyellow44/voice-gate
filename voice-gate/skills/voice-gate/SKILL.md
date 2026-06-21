---
name: voice-gate
description: Check a finished medium-form nonfiction piece (essay, post, newsletter, email) against a supplied voice profile and universal craft standards, then render one locked scorecard with one verdict. Diagnose-only: detect and suggest, never edit. Use when someone says "run the voice gate", "check this piece against my voice", "is this ready to publish?", "does this sound like me?", "gate this draft", "voice check", "run the scorecard", "audit this nonfiction draft", or wants a finished essay/post/newsletter/email graded against a writer's voice before it ships. Diagnoses against a SUPPLIED voice profile; it does not generate the profile and does not rewrite the prose.
---

# voice-gate

A single-voice writing instrument. It models one writer's voice through a **supplied voice
profile**, then checks any finished medium-form nonfiction piece against that voice and against
universal craft standards, and renders **one scorecard** and **one verdict**.

It detects and suggests. It never edits. Ownership of the fix, not the size of the suggestion,
is the scope line: a one-word suggestion is fine, applying it is not this skill's job.

## What this is, and what it is not

**Is:** a line-altitude craft gate plus one light piece-level lens (does the piece compound),
for medium-form nonfiction, run against a supplied profile.

**Is not:** a profile generator (that is the builder, a later phase), a reviser (that is
`voice-reviser`, a later phase), or any kind of state machine. There is no story-state ledger,
no motif ledger, no continuity substrate, no multi-character modeling, no relationship matrix,
no developmental or structural altitude, no generation engine. If a requirement starts to need
state or multi-character reasoning, it belongs in a heavier tool, not here. If you find yourself
adding a ledger, stop.

## Inputs

1. **The piece** — a finished medium-form nonfiction draft.
2. **A supplied voice profile** (optional but recommended) — the single source of truth for the
   personalized checks. Its required shape is in `references/voice-profile-contract.md`. It fills
   the per-check calibration slots: the writer's hard guardrails, their figurative signature,
   their native pressures, their preserve list, their specific surface tells.

If no profile is supplied, run the **universal layer only** and say so explicitly in the close:
the voice-personalized checks are reported as `Skipped — no profile supplied`, not as passes.
Never infer a writer's voice profile from the piece itself; an absent profile is an absent
profile, not a green light.

## Reference resolution (dual-path)

Resolve every reference file by context. In any normal install, use the plugin-root path. The
local source path is the author's dev path only; ignore it unless you are working in that source
tree.

- Installed plugin (use this): `${CLAUDE_PLUGIN_ROOT}/skills/voice-gate/references/<file>`
- Author dev source only: `~/Voice Gate/voice-gate/skills/voice-gate/references/<file>`

The reference set:

- `references/scorecard.md` — the locked output contract. The only output format. Read it.
- `references/voice-profile-contract.md` — what a supplied profile must provide.
- `references/checks/00-measure-once.md` — the single deterministic measurement sheet.
- `references/checks/01-surface-tells.md` — AI-polish / surface flattening.
- `references/checks/02-narrator-clean.md` — too-clean narrator (first-person reflection only).
- `references/checks/03-propulsion.md` — the compounding test and pressure taxonomy (the one
  piece-level lens).
- `references/checks/04-figurative.md` — figurative landing, keep-or-cut.
- `references/checks/05-line-craft.md` — line aliveness, over-explanation, concreteness, rhythm.
- `references/checks/06-originality.md` — lane-pastiche / centroid detection.
- `references/checks/07-preserve.md` — preserve-over-polish, the anti-flattening governor.
- `references/worked-examples.md` — one fully worked flawed run and one clean-pass run.

## Architecture: measure once, grade isolated, render consolidated

This is the discipline. Do not run the checks as one blurred read.

1. **Measure once.** Parse and measure the piece a single time against the deterministic sheet
   in `00-measure-once.md`. Produce one measurement record (counts, the section map, the
   inventory of figures, the rhythm samples). Every check reads from this one record; no check
   re-measures from scratch.

2. **Grade isolated.** Run each applicable check against its own method file, in isolation, so
   no single check can rationalize the whole piece as fine. Each check **proposes findings only**
   — rows in the scorecard shape, plus a Protect list. A check may propose zero findings; that is
   a normal, valid result, reported as "no findings from this check," never as a verdict. **No
   check renders a readiness verdict. No check self-certifies.** (When you can run the checks as
   genuinely separate sub-agents, do; isolation is the point. True sub-agents matter most on a long
   or rhetorically persuasive piece, where one read is most tempted to forgive the whole on the
   strength of a few good lines; on a short piece, sequential isolated passes are good enough.
   Either way, do not let a later check see an earlier check's disposition.)

3. **Render consolidated.** Gather every check's proposed findings, dedupe and rank them across
   checks, and render exactly **one** scorecard and **one** verdict, per `references/scorecard.md`.
   **Dedupe precedence** when two checks fire on the same quote: the more specific check owns the
   row, by this order — hard-guardrail violation (most objective) > figurative > narrator >
   propulsion > line-craft > originality > surface-tells (most general). Keep the owning row, fold
   the other check's angle into its "What's off" so nothing is lost, and never render the same
   quote as two separate findings. This gate is the sole layer that renders a verdict. The verdict
   is *derived* from the scorecard by the stated rule, never asserted.

Isolation at grading, consolidation at rendering. One gate, one scorecard, one verdict.

## Which checks apply (by form)

- **Personal essay / Substack / public reflection:** surface-tells, narrator-clean, propulsion,
  figurative (when the piece carries imagery), line-craft, originality, preserve. The full set.
- **Newsletter / post (non-reflective):** surface-tells, propulsion, line-craft, originality,
  preserve. Run narrator-clean only if the piece is first-person reflection. Run figurative only
  if it carries imagery.
- **Email:** surface-tells and line-craft, plus the supplied profile's hard guardrails. Do not
  run narrator-clean, propulsion, or figurative on an email unless the writer explicitly asks.

Never run every check on every form. Running a personal-essay narrator check on an email
manufactures findings.

## Procedure (Steps A–F)

**A. Intake.** Confirm the form. Load the supplied profile if present; note its absence if not.
Read `references/scorecard.md` so the output shape is fixed before you start.

**B. Measure once.** Run `00-measure-once.md`. Produce the one measurement record.

**C. Select checks.** From the form, pick the applicable checks (above). Skip the rest; record
them as not-applicable so the reader sees the scope.

**D. Grade isolated.** Run each selected check against its method file and the relevant profile
slots, reading from the measurement record. Each returns proposed findings (scorecard rows) and a
Protect list. Every finding carries an exact quote and a named source rule, or it is dropped.

**E. Consolidate and render.** Dedupe and rank findings across checks. Render the one scorecard
and the one derived verdict per `references/scorecard.md`, greens included. Render the
consolidated Protect list. Render the close's "Out of scope (not graded)" line from the claim-shape
count in `00-measure-once.md §8`: it reports claim-shaped language and hands off to a ship-safety
gate or fact-checker. It is not a finding, carries no severity, and never moves the verdict. Apply
`07-preserve.md` as the render-time governor: if the preserve list is long and the flag count is
low, say the piece may not need revision.

**F. Log.** Append one run-log line (see `references/scorecard.md` "Run log"). Do not compute or
assert a confidence number; the run log measured against the writer's disposition is the only
confidence signal.

## Hard rules

- **Detect and suggest only.** Never edit the prose. The gate hands off to a reviser; it is not
  the reviser.
- **Every finding rests on an exact quote plus the specific rule it breaks.** No vibes. No "feels
  off," no "could be sharper" without a quote and a named rule. Quote plus rule, always.
- **A clean pass is a normal, valid result, stated explicitly.** Never invent findings to look
  thorough.
- **One output: the locked scorecard.** A verdict line, then one table (greens included), then the
  Protect list, then the close. Three verdict states only: Good to go / Good to go with fixes /
  Not ready. Severity per finding: Blocker / Should-fix / Polish. The verdict is derived from the
  scorecard, never invented; never a fourth state.
- **No check self-certifies.** Sub-checks propose findings; only this gate renders the verdict.
- **No self-asserted confidence.** Use the run log, not a number.
- **The supplied profile is the single source of truth** for personalized checks. The universal
  checks must not carry their own private voice standards that drift from it. No supplied profile
  means the personalized checks are Skipped, never silently passed.
- **No em dashes in the gate's rendered output** (the scorecard cells beyond the inherited `—`
  placeholder token, the suggestions, and the close). Use commas, periods, semicolons, colons, or
  restructure. This is the gate's own output discipline at render time, independent of any
  writer's profile. (It governs what the gate emits to a reader, not this methodology
  documentation.)
- **Universal where universal, supplied where personal.** Do not bake one writer's guardrails
  (a punctuation ban, a figurative signature, a list of native pressures) into a universal check.
  Those are profile slots.
- **Never grade facts, sourcing, or strategy.** The claim-shape scan detects and counts
  claim-shaped language so the close can hand off honestly; it never judges whether a claim is
  true, sourced, or on-strategy, and it never produces a finding or moves the verdict. World-truth
  and strategy belong to a ship-safety gate (de-slop) or a fact-checker. Run that first; run this
  for voice fidelity.

## Worked example

`references/worked-examples.md` contains one fully worked flawed run (a short flawed nonfiction
passage, then its populated scorecard with real quotes, real sources, a real verdict) and one
clean-pass run. Read it for a calibrated model of both outcomes before grading your first piece.

## Phase note

This is the diagnose-only runtime. Its sibling `voice-gate-builder` (shipped in this same plugin at
`skills/voice-gate-builder/`) generates the supplied profile this runtime reads, from a writer's
own corpus, and proves it through a human-graded calibration gate. If a writer has no profile yet,
route them to the builder first. `voice-gate-reviser` (shipped in this same plugin at
`skills/voice-gate-reviser/`) is the constrained, flag-bounded reviser, governed by
preserve-over-polish: hand it this scorecard's operator-approved findings as targets, then re-run
this gate to verify. The gate stays diagnose-only and never rewrites the prose itself; it never
generates a profile itself.
