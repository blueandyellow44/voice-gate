---
name: voice-gate-builder
description: Build a writer-specific supplied voice profile from that writer's own corpus, for the voice-gate runtime to gate prose against. Generates the profile schema voice-gate requires (identity and register map, hard guardrails, figurative signature, native pressures, preserve list, known tells), then proves it through a human-graded calibration gate (a scenario quiz and a test passage) that the builder never self-grades. Use when someone says "build my voice profile for the gate", "make a voice-gate profile", "generate the supplied profile", "onboard a writer to voice-gate", "calibrate my voice profile", or wants to create the per-writer profile the gate reads. Detect and build with evidence; stop for the operator to grade; fail cleanly if the corpus is too thin.
---

# voice-gate-builder

Generate the **supplied voice profile** that the `voice-gate` runtime gates prose against. The
runtime checks a finished piece against a supplied profile; this builder creates that profile from
a writer's own corpus, then proves it with a calibration gate a human grades. The builder detects
and builds with evidence. It never certifies its own output, and it never edits prose.

One writer per run. The deliverable is one profile file matching the runtime schema, plus a
calibration file the operator grades.

## What this is, and what it is not

**Is:** an evidence-driven profile generator plus a human calibration gate, for the `voice-gate`
runtime, distributable to any writer.

**Is not:** the runtime (that is `voice-gate`, which only reads the profile this produces), a
reviser, a general character engine, or a Literary Engine. It builds a line-altitude voice profile
plus exactly enough interior to set the native pressures and the dosing rules. It does not build a
full interior dossier, a story-state ledger, or any multi-character model. If a requirement starts
to need a relationship matrix or narrative state, it is out of scope here.

## The single source of truth for the output

The profile this builder emits **must** match the runtime's contract. Read it first and treat it
as the schema authority; this builder fills its slots, it does not redefine them.

- Installed plugin (use this): `${CLAUDE_PLUGIN_ROOT}/skills/voice-gate/references/voice-profile-contract.md`
- Author dev source only: `~/Voice Gate/voice-gate/skills/voice-gate/references/voice-profile-contract.md`

The six required slots: (1) Identity and register map, (2) Hard guardrails, (3) Figurative
signature, (4) Native pressures, (5) Preserve list / signature moves, (6) Known surface tells.
Plus optional calibration examples. `references/profile-schema.md` maps each slot to how it is
filled from corpus evidence.

## Reference resolution (dual-path)

Use the plugin-root path in any normal install; the local path is the author's dev path only.

- `references/profile-schema.md` — the output schema, slot by slot, and how each is evidenced.
- `references/extraction-method.md` — how to pull each slot from the corpus with citations.
- `references/calibration-gate.md` — the two-stage gate, the grading surface, the headless fallback.
- `references/dosing-and-silence.md` — the interior-dosing ladder and the silence / interior-leak
  rule, and how each maps into the runtime's existing slots so the gate consumes them with no change.
- `references/worked-example.md` — one full synthetic build (corpus to schema to ungraded quiz).
- `templates/profile-template.md` — the blank profile to fill.
- `templates/calibration-template.md` — the blank calibration file to write and hand to the operator.

## Reuse, do not reinvent

Where these richer extraction skills are available, orchestrate them rather than re-deriving their
work. Where they are absent (the common case for a distributed install), the method embedded in
this skill's references is self-sufficient.

- `voice-corpus-extractor` — the deterministic corpus front end (attribute-or-omit, count-don't-judge).
- `voice-profile-builder` — evidence-cited trait extraction and the no-quote-no-trait rule.
- `voice-profile-iteration` — the graded calibration loop and the un-scened-occasion rule.
- `character-dossier` — the interior read and the two-stage calibration gate (quiz, then scene),
  used here ONLY to the depth that sets native pressures and dosing; not a full dossier.

The builder's own new work is small: map the universal method onto the runtime's six slots,
generate the per-writer calibration, and stop for grading.

## Never (the five that protect the output)

- **Never self-grade the calibration gate.** A model grading its own predictions validates nothing.
- **Never fabricate a trait to fill a slot.** No quote, no trait; a thin corpus is a clean failure.
- **Never write a fake completed calibration.** An ungraded gate ships `pending`, never a fake pass.
- **Never invent a seventh slot or rename one.** The runtime contract owns the schema.
- **Never ship a Max-private artifact.** Max instance zero is a local validation path only.

## Procedure

### Step 1: scope and gather the corpus

Confirm the writer, the forms the profile must cover (essay / newsletter / email), and where the
corpus lives. Collect every sample for those forms. Strip non-voice cruft (nav, timestamps, other
people's words). Note word count and how many distinct samples and registers are represented.

**Clean-failure gate (mandatory).** If the corpus is too thin to evidence the slots, stop. Concrete
floor: clean-fail if any form the profile must cover has zero quotable samples, or the whole corpus
is under roughly 400 words / 3 distinct samples (enough to draft lightly but mark thin slots
low-confidence; below it, the slots cannot be honestly evidenced). On a clean failure, say which
slots cannot be evidenced and ask for more samples or a narrower form scope. Never fabricate a trait
to fill a slot; an invented profile produces confident wrong gating every time it is used. A thin
corpus is reported, not papered over.

### Step 2: extract evidence-cited traits per slot

Read `references/extraction-method.md` in full, then work each of the six slots. **Every trait
cites at least one verbatim quote from the corpus. No quote, no trait.** Profile the writer as the
evidence shows them, not against any house style: if the writer uses em dashes and contractions,
the Hard guardrails slot records that, it does not impose another writer's bans.

For §4 Native pressures, do the *light* interior read in `extraction-method.md`: which of the nine
pressures (danger, desire, secret, shame, contradiction, decision, dread, curiosity, longing) the
writer's strongest work runs on, evidenced by the pieces, not psychologized. This is the only
interior the gate needs; do not build a dossier.

### Step 3: set the dosing ladder and the silence rule

Read `references/dosing-and-silence.md` in full. Write the interior-dosing ladder into the
profile's §Identity register map (high interior pressure in personal essay, lower in newsletter,
near-zero in formal email) and the interior-leak tell into §Known surface tells and §Preserve
list, exactly as that file specifies. This is what lets the runtime flag "deep in the wrong room"
and over-rendered private subtext through its existing checks, with no runtime change.

### Step 4: draft the profile from the template

Fill `templates/profile-template.md` into the writer's profile file, every slot cited. State the
confidence level and the thin spots honestly. Lead the register map from the writer's plainest,
most-frequent register, not the flashiest, or the gate will calibrate to parody.

### Step 5: calibration gate (human-graded, never self-graded)

Read `references/calibration-gate.md` in full. Produce the two-stage gate into a calibration file
from `templates/calibration-template.md`:

1. **Scenario quiz — 8 to 12 novel-response items.** Each item is an occasion the corpus never
   staged; the builder writes a candidate line or names a register/voice choice in the drafted
   profile's voice and cites which profile slots drove it. The operator grades each
   (perfect / close / not quite).
2. **Test passage.** One short passage written in the voice on an un-scened occasion. The operator
   grades it.

Then **stop and hand the calibration file to the operator.** The builder does not grade its own
quiz or passage; a model grading its own predictions of its own model is circular and validates
nothing. A failed item is a profile bug: route the fix back into the slot, do not just redraft the
line. If the same dimension fails twice, name the resisting dimension and its cause and ask for
direction rather than grinding a third draft.

**Headless fallback.** When no operator is available mid-run (agent or pipeline), make the build
judgment calls, log each to a `DECISIONS.md` in the output folder, write the calibration file with
every grade slot left `pending`, and stop. Never self-grade; never write a grade the operator did
not give.

### Step 6: deliver

On a graded pass, finalize the profile file and link the calibration file beside it. Report
confidence and thin spots. The profile is now ready to hand to the `voice-gate` runtime as its
supplied profile. Set up a `voice-gate-runlog.md` beside the profile from the runtime scorecard's
run-log header.

## Hard rules

- **No quote, no trait.** Every slot value cites verbatim corpus evidence. A thin corpus is a
  clean failure, never a fabrication.
- **Profile the writer, not a house style.** Each writer's guardrails come from their corpus. Do
  not impose any other writer's bans (no em dashes, no contractions) on a different writer.
- **The builder never self-certifies.** The calibration gate is human-graded. Headless runs write
  the gate and stop with grades pending.
- **Never write a fake completed calibration.** An ungraded gate ships with `pending`, never a
  fabricated pass.
- **Match the runtime schema exactly.** Fill the six contract slots; do not invent a seventh or
  rename one. The runtime contract is the authority.
- **Light interior only.** Build only the interior the gate needs (native pressures, dosing). No
  full dossier, no relationship matrix, no narrative state.
- **Em-dash scope.** The profile and calibration files this builder writes are config and grading
  worktables, not prose published under a writer's name, so normal punctuation (including em dashes)
  is fine there, the same way the runtime's methodology docs keep theirs. The only em-dash
  discipline is the runtime's render-time rule on the *gate's* rendered scorecard, which the builder
  does not produce. A writer whose own §Hard guardrails ban em dashes still has that enforced by the
  gate on their prose; the profile that records the rule does not have to follow it.
- **Keep Max-private material out of any distributed artifact.** Max instance zero is a local
  validation path only (see below); no Max corpus, profile, or graded calibration is committed
  here.

## Max instance zero (private, local validation path — not shipped)

To validate the builder against a known target, run it locally on Max's own corpus and confirm the
generated supplied profile makes `voice-gate` reproduce what `max-voice-auditor` already catches on
a known flawed piece. That run, its corpus, and its graded calibration stay **local and private**;
they are never committed to this plugin. The distributable plugin ships only the synthetic worked
example. Keeping the interior depth in a local run and out of the shipped artifact is what keeps
this builder shareable. Detail and the reproduction test live in the Phase 4.4 / 4.5 notes in
`~/Voice Profile/`.

## Phase note

This is the builder (Phase 4.4). The runtime it feeds is `voice-gate` (Phase 4.3, shipped). The
reviser that acts on the gate's approved flags (`voice-reviser`) ships after the gate and builder
prove out. Packaging the two-skill plugin for distribution and an optional real Max instance-zero
calibration run are Phase 4.5.
