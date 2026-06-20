# Calibration gate — two stages, human-graded, never self-graded

A drafted profile can be accurate and still fail to generate the voice: description drifts, and the
loud traits crowd out the plain ones. The calibration gate catches that gap. It has two stages a
human grades. The builder produces the gate and stops; it does not grade its own work. A model
grading its own predictions of its own model is circular and validates nothing.

Write the gate into a calibration file from `templates/calibration-template.md`, beside the profile.

## The load-bearing rule: change the occasion, do not trust discipline

Every quiz item and the test passage sit on an **un-scened occasion** — a situation the writer's
corpus never covered. This is a structural safeguard, not a stylistic preference. An item built on
a piece the writer actually published gets graded against the reader's memory of the original and
proves nothing about the profile; worse, a model told to "be original" will paraphrase a real
piece without noticing. Remove the real piece from reach: pick an occasion the corpus never staged,
and there is no published line to drift toward. Verify any fact an item leans on before presenting
it; a sample built on a wrong premise spends the operator's correction budget on a fact instead of
the voice.

## Stage 1 — scenario quiz (8 to 12 novel-response items)

Generate 8 to 12 items. Each item:

1. Names an un-scened occasion (a fresh prompt the corpus never covered), and which **form** it is
   in (essay / newsletter / email), because the dosing ladder makes the right answer form-dependent.
2. Gives the builder's candidate response in the drafted profile's voice — either a short line
   written in the voice, or a named voice/register choice (e.g., "in this email the writer would
   open plain and drop the figure entirely").
3. Cites which profile slots drove the candidate (e.g., "Slot 1 register map, Slot 4 native
   pressures: dread").

Spread the items across the forms the profile covers and across the slots, so the grade tests the
whole profile, not one corner. Include at least one item that should trigger the dosing rule (an
email or newsletter occasion where deep interior would be "deep in the wrong room") and one that
should trigger the silence rule (an occasion where the honest move is to let the pressure steer
without naming it).

The operator grades each item: **perfect** locks it; **close** and **not quite** route back to the
profile. A wrong item is a profile bug — a wrong or missing slot value — not a wrong guess. Fix the
slot, then re-quiz the failed dimension. Premises are claims too: an item that fails because its
occasion was implausible or off-form gets regenerated, it does not touch the profile.

## Stage 2 — test passage

Write one short passage (a paragraph or two) in the writer's voice, on an un-scened occasion, in a
named form. It must be new prose, never a paraphrase of a published piece; dramatizing a real piece
proves memory, not the profile. The operator grades it against the profile and the writer's actual
voice.

Common failure-to-fix mappings (name the failure before redrafting):

- **Every line plausible, none sounds like the writer** → profile problem: the loud traits are
  crowding the plain baseline. Reorder Slot 1 to lead from the floor, add a Slot 6 tell. Fix the
  profile, not the passage.
- **"Parody" / "too much"** → a signature move is over-performing. Ration it toward the plain
  baseline.
- **Right voice, wrong room** → the passage rendered interior the form should keep near-silent.
  This is the dosing/silence rule firing; fix the dosing note in Slot 1, not the sentences.
- **A fact is wrong** → fix the fact, re-verify; do not touch the voice slots.

If the same dimension fails twice, stop redrafting: the fault is in the profile, not the wording.
Fold the fix into the slot and move on, or name the resisting dimension and ask the operator for
direction.

## Grading surface

Present both stages through an in-thread grading surface the operator fills without opening a file
side by side: a numbered list they grade inline, or an interactive widget whose submit posts the
grades back into the conversation. Default to the numbered inline list unless an interactive widget
surface is actually available; do not block grading on a widget. The calibration file is the durable
record written beside the profile; the operator does not grade from a file open next to the chat.

## The builder stops here

After producing both stages, **hand the calibration file to the operator and stop.** Do not write a
grade. Do not declare the profile validated. Validation is the operator's grade. On a graded pass,
Step 6 of the SKILL finalizes; on fails, route each back into the slot it implicates.

## Headless fallback (no operator mid-run)

When the builder runs inside an agent or pipeline with no operator available:

1. Make the build judgment calls yourself and log each to a `DECISIONS.md` in the output folder —
   one unique, descriptive heading per decision, the options considered, and why the winner won, so
   the operator can audit them later.
2. Write the full calibration file: all 8 to 12 quiz items and the test passage, with **every grade
   slot left `pending`** and `operator-disposition: pending`.
3. Stop. Do not self-grade. Do not write a grade the operator did not give. Do not mark the profile
   validated.

A headless run produces a ready-to-grade gate, never a graded one. The next operator session grades
it and routes the fixes.
