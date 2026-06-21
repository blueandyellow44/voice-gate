# Revision discipline — the bounded-edit method

This is the method `voice-gate-reviser` runs. It is the generation-side mirror of the gate's
`07-preserve.md`: where that check guards the gate against recommending an over-edit, this method
guards the reviser against making one. The reviser is bound by `07-preserve.md`'s hard rules; read
that file too.

## The span is the unit

A finding names an **exact quoted span**. That span, and only that span, is the unit of revision.
The fix changes the words inside the span so the named source rule is satisfied, and changes
nothing outside it.

- A surface-tell finding on a wisdom-button sentence is fixed by cutting or recasting that
  sentence, not the paragraph around it.
- A line-craft finding on an over-explained image is fixed by cutting the explanation clause, not
  by rewriting the image.
- A figurative finding on an off-signature figure is fixed by replacing or cutting that figure,
  not by re-figuring the passage.
- A hard-guardrail finding (a banned construction) is fixed by the smallest change that removes the
  violation while keeping the writer's meaning and rhythm.

If you cannot fix the span without changing text outside it, the finding is bigger than a span fix:
report that to the operator and stop. Do not expand the edit to make it work.

## Smallest change, in voice

Prefer, in order: a one-word swap, a single cut, a local recast of the flagged clause, a recast of
the flagged sentence. Stop at the first option that satisfies the rule. The goal is not the best
line you could write; it is the smallest change that clears the finding while still sounding like
the writer. A reviser that writes a "better" sentence than the writer would write has flattened the
voice even if every word is correct.

Match the writer from the profile: register by form, figurative signature (which figures are
native), native pressures, and the preserve list. The fix should read as the writer on a good day,
not as a competent editor.

## Honor the guardrails while fixing

Every fix is checked against the profile's §Hard guardrails before it is applied:

- Never introduce a violation (do not add a banned construction, do not break a fixed closing form).
- Never remove a native move the profile protects. If em dashes are native and protected, a fix
  near one keeps it. If a guardrail and a finding seem to require opposite changes, the guardrail
  wins and the conflict is reported.

## Preserve list first, adjacency always

Restate the Protect list and adjacency risks before editing. When a flagged span sits next to a
preserved line or move:

- Fix the flagged span; leave the preserved line byte-for-byte unchanged.
- If the only available fix would alter the preserved line, do not apply it. Report the adjacency
  conflict and let the operator decide.

Do not normalize odd constructions, flatten jagged transitions, regularize deliberate repetition,
or convert local rawness into correctness. Those are voice, not error, unless a finding named them.

## What the reviser returns

- **Changed spans only**, as before/after pairs, one per applied finding, each with a one-line note
  naming the finding it applied and the rule it satisfied.
- **Untouched-but-adjacent note** where relevant: the preserved line next to a fix, named so the
  operator can see it survived.
- **Any conflicts**: findings not applied because the fix would damage a preserved line or break a
  guardrail.
- **Handoff:** re-run `voice-gate` to verify. The reviser renders no verdict and never declares the
  piece clean. The maker is not the judge.
