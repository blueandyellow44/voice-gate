# Voice Gate — share / install note

A standalone Claude plugin (`voice-gate`, v0.2.0) with two skills. It models one writer's
voice and checks finished medium-form nonfiction against it. Diagnose-only: it tells you what
is off and points at the smallest fix. It never rewrites your prose.

## What this plugin does

- **`voice-gate`** (the runtime). Takes a finished piece (essay, post, newsletter, email) and a
  supplied voice profile, and renders **one locked scorecard**: a verdict line, a findings table
  (greens included), a Protect list, and a close. Three verdict states only — *Good to go /
  Good to go with fixes / Not ready* — derived from the scorecard by rule, never asserted.
  Every finding rests on an exact quote plus the named rule it breaks. It runs a universal craft
  layer (AI-polish tells, too-clean narrator, the compounding/propulsion lens, figurative
  landing, line craft, originality, and a preserve-over-polish governor) plus a personalized
  layer that calibrates against the supplied profile.
- **`voice-gate-builder`** (the generator). Builds the supplied voice profile the runtime needs,
  from a writer's own corpus, then proves it through a human-graded calibration gate.

## How to use `voice-gate-builder`

1. Gather a corpus of the writer's own finished pieces (a handful of real essays/posts/emails).
2. Run it: **"build my voice profile for the gate."**
3. It extracts the profile into the runtime's six contract slots (identity & register map, hard
   guardrails, figurative signature, native pressures, preserve list, known tells), every trait
   tied to a real quote.
4. It then hands you a **calibration gate**: a scenario quiz (8–12 novel occasions) and one
   un-scened test passage. **You grade it.** The builder does not grade its own output.
5. On a pass, you have a profile the runtime can gate against. On a thin corpus it fails cleanly
   and tells you what is missing rather than inventing a profile.

## How to use `voice-gate`

1. Have a supplied voice profile (from the builder, or hand-written to the contract shape in
   `skills/voice-gate/references/voice-profile-contract.md`).
2. Run it: **"run the voice gate on this draft"** and supply the profile (or say there is none,
   and it runs the universal craft layer only and says so).
3. Read the scorecard. Apply the fixes yourself — the gate does not.

## What it does NOT do

- It does **not** rewrite your prose. Diagnose and suggest only. (A constrained `voice-reviser`
  is a planned later phase; it is not built.)
- It does **not** infer a profile from the piece under test. No supplied profile means the
  universal layer only.
- It carries **no** story-state ledger, motif ledger, multi-character modeling, or generation
  engine. Line altitude plus one piece-level lens is the ceiling. (For deeper, multi-character
  work, that is a different, heavier tool.)
- It ships **no** personal data. The universal layer is identical for every writer; the
  personalized layer is whatever profile *you* supply. Your corpus never ships with the plugin.

## Calibration must be human-graded

This is the load-bearing rule. The builder **never certifies its own profile.** The calibration
gate (quiz + test passage) is graded by a person. In a headless run the builder writes the
profile and calibration file with every grade set to `pending` and stops — it will not fake a
pass. A profile is only trustworthy once a human has graded its calibration and it passed.

## Install

- **Plain handoff (lightest):** share `dist/voice-gate-<version>.zip` (built by
  `automation/package_voice_gate.py`) or the `voice-gate/` directory. It is already a valid
  `.claude-plugin` plugin; drop it into a plugin marketplace / install path.
- **claude.ai desktop upload:** the same zip is pre-flighted against the uploader limits
  (plugin description ≤ 500, every SKILL.md description ≤ 1024, no angle-bracket placeholders).
  Re-run `python3 automation/package_voice_gate.py` to rebuild and re-validate.

Start at `README.md`, then `skills/voice-gate/SKILL.md` (the runtime) and
`skills/voice-gate-builder/SKILL.md` (the builder).
