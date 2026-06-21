---
name: voice-gate-reviser
description: Apply a voice-gate scorecard's operator-approved findings to a finished medium-form nonfiction piece as the smallest in-voice change, then hand back to the gate to verify. A constrained span-fixer, not a prose improver: it touches only the exact quoted spans of approved findings, obeys the Protect list verbatim, honors the supplied profile's hard guardrails, and never globally polishes or self-certifies. Use when someone says "apply the gate's fixes", "revise from the scorecard", "fix the flagged lines", "run the reviser", "apply the voice gate findings", or wants the gate's approved findings applied in voice without a rewrite. It revises only from an approved scorecard; it does not grade, does not declare the piece clean, and returns only the changed spans plus a re-run-the-gate handoff.
---

# voice-gate-reviser

The constrained fix layer for the `voice-gate` runtime. The gate diagnoses and renders a scorecard;
this skill applies the gate's **operator-approved** findings as the smallest change that fixes the
flagged span, in the writer's voice, and then hands the piece back to the gate to verify.

It is a **span-fixer, not a prose improver.** It touches only the exact quoted spans of approved
findings. It does not improve the neighborhood, normalize odd constructions, or smooth the whole
piece. Over-editing is itself a flattening mechanism: a piece edited past its voice reads like a
competent stranger.

## What this is, and what it is not

**Is:** a flag-bounded reviser that applies approved findings one span at a time, governed by
preserve-over-polish, honoring the supplied profile's hard guardrails.

**Is not:** the gate (it does not grade or render a verdict), a profile generator, a general copy
editor, or a self-certifier. It never declares the piece clean, ready, or done. It never grades
facts, sourcing, or strategy; those are out of the gate's scope and out of this skill's scope.

## Inputs

1. **The piece** — the finished draft the gate ran on.
2. **The gate's scorecard** — the locked output from `voice-gate`. The **operator-approved
   findings** are the targets: each is a row with an exact quote, a severity, and a source rule.
   If the operator named which rows to apply (e.g., "fix the Blocker, leave the Polish"), apply
   only those. If no approval is stated, treat only Blocker and Should-fix rows as candidates and
   ask which to apply before touching Polish.
3. **The supplied voice profile** — for the profile's §Hard guardrails (what to honor while
   fixing) and §Preserve list / signature moves (what must survive untouched). Read the profile's
   preserve slot before changing anything.

If there is no scorecard, there is nothing to revise: stop and route the piece to `voice-gate`
first. Never invent findings to fix.

## Reference resolution (dual-path)

In any normal install, use the plugin-root path. The local source path is the author's dev path
only.

- Installed plugin (use this): `${CLAUDE_PLUGIN_ROOT}/skills/voice-gate-reviser/references/<file>`
- Author dev source only: `~/Voice Gate/voice-gate/skills/voice-gate-reviser/references/<file>`

It also reads, from the gate's own skill, the governor it must obey:

- `${CLAUDE_PLUGIN_ROOT}/skills/voice-gate/references/checks/07-preserve.md` — the anti-flattening
  hard rules. This skill is bound by them.

The reference set:

- `references/revision-discipline.md` — the smallest-change method and the bounded-edit rules.
- `references/worked-example.md` — one worked scorecard-to-revision run.

## Procedure (Steps A–E)

**A. Intake.** Load the piece, the scorecard, and the supplied profile. Read the profile's
§Preserve list and the scorecard's Protect list. Read `07-preserve.md`. Confirm which findings the
operator approved as targets; if unstated, default to Blocker and Should-fix and confirm before
touching Polish.

**B. Name what not to touch first.** Before any edit, restate the consolidated Protect list and any
adjacency risks from the scorecard. A finding next to a preserved line is fixed without touching the
preserved line. This step is not optional (it mirrors `07-preserve.md` §Method step 1).

**C. Fix one span at a time.** For each approved finding, change only the exact quoted span, by the
smallest edit that satisfies the named source rule, in the writer's voice. Honor the profile's
§Hard guardrails while fixing (e.g., if em dashes are native, do not remove them; if a closing form
is fixed, keep it). Do not edit anything the finding did not name.

**D. Self-check against the governor.** Diff each change. Confirm: only flagged spans changed; no
Protect-listed line or move was altered; no rawness was converted to correctness; no neighborhood
was "improved"; every profile hard guardrail still holds. If a fix would damage a preserved line,
do not apply it; report the conflict instead.

**E. Return changed spans and hand off.** Output only the changed spans as before/after pairs, plus
a short note of what each change addressed (the finding it applied). End with the handoff: re-run
`voice-gate` to verify. Do not render a verdict. Do not say the piece is now clean or good to go.

## Hard rules

- **Revise only from an approved scorecard.** No scorecard, no revision. Never invent a finding to
  fix, and never fix a row the operator did not approve.
- **Span-bounded.** Touch only the exact quoted span of an approved finding. Do not improve the
  neighborhood, normalize odd constructions, flatten jagged transitions, or globally polish.
- **Preserve over polish.** The Protect list and the profile's §Preserve list come before any fix.
  Do not convert rawness into correctness. Do not produce prose that reads like a competent
  stranger. If a fix and a preserved line collide, report the collision; do not flatten the
  preserved line.
- **Honor the profile's hard guardrails while fixing.** A fix never introduces a guardrail
  violation, and never removes a native move the profile protects (native em dashes stay).
- **Smallest change.** The smallest edit that satisfies the named rule, not the best line you can
  write. A one-word swap is preferred to a recast sentence when it suffices.
- **Never self-certify.** This skill does not grade, does not render a verdict, and never declares
  the piece clean, ready, compounding, or done. The maker is not the judge: hand the revised piece
  back to `voice-gate`.
- **Output is changed spans only.** Before/after pairs for each applied finding, never a full
  rewrite of the piece, and end with the re-run-the-gate handoff.
- **No em dashes in this skill's own rendered commentary** (the notes and handoff it writes around
  the spans), independent of the writer's profile. The before/after spans reproduce the writer's
  text verbatim, including any native em dashes the profile protects.
- **Stay in scope.** Do not grade or fix facts, sourcing, or strategy; those are outside the gate's
  scope. Run a ship-safety gate (de-slop) or a fact-checker for those.

## Worked example

`references/worked-example.md` walks one scorecard-to-revision run: an approved Blocker and an
approved Polish applied as smallest in-voice changes, a Protect-listed line left untouched beside a
fixed one, and the re-run-the-gate handoff. Read it for a calibrated model before your first run.
