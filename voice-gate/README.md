# Voice Gate

A single-voice writing instrument. It checks a finished medium-form nonfiction piece (essay, post,
newsletter, email) against a supplied voice profile and against universal craft standards, then
renders one scorecard and one verdict.

It detects and suggests. It never edits. A clean pass is a normal, valid result.

## What it is

- **Diagnose-only.** It finds what is off and points at the smallest fix. Applying the fix is not
  its job.
- **Light.** Line altitude plus one piece-level lens (does the piece compound). No state machine,
  no continuity ledger, no multi-character modeling, no generation engine.
- **Profile-driven.** Personalized checks calibrate against a supplied voice profile (its shape is
  in `skills/voice-gate/references/voice-profile-contract.md`). With no profile, it runs the
  universal craft layer only and says so; it never infers a profile from the piece.
- **One output.** A locked scorecard: a verdict line, then a table (greens included), then a
  Protect list, then a close. Three verdict states only: Good to go / Good to go with fixes / Not
  ready. Severity per finding: Blocker / Should-fix / Polish. The verdict is derived from the
  scorecard, never asserted.

## The two layers

- **Universal layer** (ships verbatim, same for every writer): surface AI-polish tells, too-clean
  narrator, the compounding/propulsion lens, figurative landing, line craft, originality /
  lane-pastiche, and a preserve-over-polish governor. These are in
  `skills/voice-gate/references/checks/`.
- **Personalized layer** (supplied per writer): the writer's hard guardrails, figurative
  signature, native pressures, preserve list, and known tells. These fill the calibration slots
  the universal checks read.

## Architecture

Measure once (one deterministic sheet), grade isolated (each check proposes findings blind to the
others, no check self-certifies), render consolidated (one gate, one scorecard, one verdict).

## Use it

Install as a plugin, then: "run the voice gate on this draft" (and supply the writer's profile, or
say there is none). See `skills/voice-gate/SKILL.md` for the full procedure and
`skills/voice-gate/references/worked-examples.md` for one worked flawed run and one clean-pass run
on synthetic text.

## Status and roadmap

- **Phase 4.3: `voice-gate`, the diagnose-only runtime.** Built and shipped. (`skills/voice-gate/`)
- **Phase 4.4: `voice-gate-builder`, the profile generator.** Built and shipped.
  (`skills/voice-gate-builder/`) Generates the supplied voice profile from a writer's own corpus,
  matching the runtime's profile contract, and proves it through a human-graded calibration gate
  (a scenario quiz and a test passage) that it never self-grades. Reuses the existing extraction
  method rather than reinventing it; fails cleanly on a thin corpus.
- **Later: `voice-reviser`.** Constrained, flag-bounded revision in voice, governed by
  preserve-over-polish, handed off from the gate. The gate never edits; the reviser does, within
  the gate's approved flags. Not built yet.

The gate is the distributable entry point; the builder makes it generatable for any writer from
their own corpus. To build a profile: "build my voice profile for the gate" (see
`skills/voice-gate-builder/SKILL.md`). To gate a piece against it: "run the voice gate on this
draft" (see `skills/voice-gate/SKILL.md`).
