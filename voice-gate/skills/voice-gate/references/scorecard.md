# The locked scorecard (the only output format)

This is the single output contract for `voice-gate`. It is inherited verbatim from the Phase 4.2
locked scorecard built into Max's `max-voice-auditor`, generalized so it serves any supplied
writer profile, not Max specifically. Render it every time, in this order. It is the same shape
every check proposes findings into; the gate is the sole layer that renders the verdict.

## 1. Verdict — one line, three states only

Render exactly one of:

- **Good to go** — every check is Pass. Nothing to fix.
- **Good to go with fixes** — no Blocker findings; one or more Should-fix or Polish findings.
- **Not ready** — at least one Blocker finding.

The verdict is **derived** from the scorecard by this rule, not asserted: any Blocker → **Not
ready**; else any Should-fix or Polish → **Good to go with fixes**; else → **Good to go**. Never
invent a fourth state.

## 2. Scorecard — one table, greens included

One row per check run, including passing checks (Status `Pass`) and skipped ones (Status
`Skipped`), so the reader sees what was verified, what failed, and what was out of scope — not
only the failures.

| Check | Status | Severity | Evidence quote | Source rule | What's off | Suggested fix direction |
|-------|--------|----------|----------------|-------------|------------|-------------------------|

- **Check** — the named diagnostic (e.g., "Surface: inflated significance", "Narrator:
  too-smooth self-understanding", "Propulsion: compounding test", "Figure: spine-metaphor
  landing", "Line: over-explanation", "Originality: lane-tic", "Preserve: over-polish risk").
- **Status** — `Pass` (no issue), `Flag` (issue found), or `Skipped` (check not applicable to
  this form, or a personalized check with no supplied profile).
- **Severity** — `—` for Pass and Skipped rows; `Blocker` / `Should-fix` / `Polish` for Flag
  rows. **Blocker** = the piece does not sound like the writer, or a flattening that breaks the
  voice, or a violation of a hard guardrail from the supplied profile. **Should-fix** = a real
  flattening worth fixing before this ships. **Polish** = optional sharpening.
- **Evidence quote** — the exact words from the piece the finding rests on. A finding with no
  quotable evidence is not a finding; drop it. For a Pass row, quote the line that earns the
  green, or `—`. For a Skipped row, `—`.
- **Source rule** — the named rule and file the finding ties to: a universal check file
  (e.g., `checks/01-surface-tells.md §Inflated significance`) or a slot in the supplied profile
  (e.g., `profile §Hard guardrails`, `profile §Figurative signature`). Every finding names one.
- **What's off** — one plain sentence. `—` for Pass and Skipped rows.
- **Suggested fix direction** — smallest-change direction, not a rewrite. `—` for Pass and
  Skipped rows.

## 3. Protect — always present

Below the scorecard, the consolidated Protect list gathered from every check: what is already
alive and particular and must not be touched in any revision. Not optional. Over-editing is
itself a flattening mechanism; a piece that passes every check but reads like a competent
stranger has been edited past its voice.

## 4. Close

- **Checks run** — which checks were run, which were skipped, and why (form scope, or no profile).
- **Profile status** — supplied (and which slots it filled) or not supplied (so the reader knows
  the personalized checks were skipped, not passed).
- **Recommended next action** — e.g., "hand to the reviser with the Blocker row as the approved
  target," or "Good to go — do not revise."
- **Run-log line** — append one record per run (see Run log).

## Run log

After each run, append one line so the gate's reliability is measured against the writer's
feedback over time, not asserted:

`<date> | <piece slug> | <verdict> | blocker:<n> should-fix:<n> polish:<n> | operator-disposition: pending`

Default path for a single-writer instance: a `voice-gate-runlog.md` beside the supplied profile
(create it from this header line if absent). For a multi-writer setup, segment the log by writer.
Leave `operator-disposition: pending`; it is updated when the writer accepts, overrides, or
corrects the verdict. The accumulating agreement/override record is the only legitimate confidence
signal — do not replace it with a self-computed number.

## Hard rules for the gate

- This gate is the sole layer that renders a readiness verdict. The checks propose findings only;
  none declares a piece clean, ready, compounding, or done.
- Use only the three verdict states. Derive the verdict from the scorecard by the rule above;
  never invent a fourth.
- Every finding ties to an exact quote and a named source rule, or it is dropped.
- Never assert a self-computed confidence or calibration number; confidence is the run log's job.
- Diagnose only. Do not rewrite.
- Do not render "Good to go" prematurely; run every applicable check on the full piece first.
- A personalized check with no supplied profile is `Skipped`, never `Pass`.
