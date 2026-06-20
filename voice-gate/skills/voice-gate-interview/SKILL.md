---
name: voice-gate-interview
description: Build a writer-specific supplied voice profile for the voice-gate runtime by a consent-first interview, for a writer who has no corpus or does not want to hand one over. Elicits the six profile-contract slots (identity and register map, hard guardrails, figurative signature, native pressures, preserve list, known tells) through a guided, visual interview, optionally quote-grounding any writing samples the writer pastes or uploads, then proves the profile through the same human-graded calibration gate voice-gate-builder uses and never self-grades. Renders an interactive in-chat visualization on Cowork, chat, and desktop surfaces, or writes an interactive HTML file in a terminal. Use when someone says "build my voice profile by interview", "I have no corpus", "kickoff a voice profile", "interview me for the voice gate", or wants the consent-first alternative to corpus-mining.
---

# voice-gate-interview

Generate the **supplied voice profile** that the `voice-gate` runtime gates prose against, by
**interviewing the writer** instead of sweeping a corpus. This is the consent-first on-ramp: a
writer with no body of work to hand over, or who does not want to share sensitive material, answers
a guided visual interview, and the skill fills the same six contract slots from their answers. Any
writing samples the writer chooses to paste or upload are **quote-grounded** against those answers.
Then the profile is proved through the **same human-graded calibration gate** the corpus builder
uses, which this skill never self-grades.

One writer per run. The deliverable is one profile file matching the runtime schema, plus a
calibration file the operator grades.

## What this is, and what it is not

**Is:** an interview-driven profile generator plus a human calibration gate, for the `voice-gate`
runtime, for writers without a corpus. It renders the interview as an interactive visualization.

**Is not:** the runtime (`voice-gate`, which only reads the profile), the corpus builder
(`voice-gate-builder`, which extracts the same profile from a body of work), a reviser, or a
character engine. It builds a line-altitude profile plus exactly enough interior to set the native
pressures and the dosing rules. No full dossier, no relationship matrix, no narrative state. If a
requirement starts to need any of those, it is out of scope here.

## The one thing that makes this skill different: self-report is aspirational

A corpus does not lie about itself; a writer describing their own voice often does. People name the
voice they wish they had: they say "I never use clichés," "my figures are subtle," "I write plain,"
while their actual prose does the opposite. The corpus builder's rule is **no quote, no trait**.
This skill cannot hold that rule on an interview answer, so it holds the next-strongest one:

- **An ungrounded answer is provisional, not a fact.** Every slot value sourced only from the
  interview is marked `self-reported (unverified)` and is the calibration gate's first job to test.
- **When samples are offered, they outrank the claim.** Quote-grounding (see
  `references/sample-grounding.md`) checks each answer against the writer's real lines. If the
  sample contradicts the claim ("you said near-zero simile; here are three"), the **sample wins**
  and the slot records what the prose shows, with the contradiction noted for calibration.
- **The calibration gate matters more here, not less.** With no corpus to anchor the slots, the
  two-stage human-graded gate is the only thing standing between a flattering self-portrait and a
  profile the runtime can trust. Never skip it; never self-grade it.

This is why the interview is a kickoff, not a shortcut: it gets a usable profile fast, then the gate
earns the trust.

## The single source of truth for the output

The profile this skill emits **must** match the runtime's contract. Read it first and treat it as
the schema authority; this skill fills its slots, it does not redefine them, invent a seventh, or
rename one.

- Installed plugin (use this): `${CLAUDE_PLUGIN_ROOT}/skills/voice-gate/references/voice-profile-contract.md`
- Author dev source only: `~/Voice Gate/voice-gate/skills/voice-gate/references/voice-profile-contract.md`

The six required slots: (1) Identity and register map, (2) Hard guardrails, (3) Figurative
signature, (4) Native pressures, (5) Preserve list / signature moves, (6) Known surface tells.

## Reference resolution (dual-path)

Use the plugin-root path in any normal install; the local path is the author's dev path only. This
skill's own references plus the shared builder references it reuses:

This skill's own:

- `references/interview-script.md` — the question bank per slot, with the aspirational-voice probes.
- `references/surface-rendering.md` — the two delivery paths and how to choose between them.
- `references/sample-grounding.md` — quote-grounding pasted/uploaded samples against the answers.
- `templates/kickoff.html` — the offline-safe interactive kickoff artifact.

Reused from `voice-gate-builder` (do not duplicate; read them where they live):

- `${CLAUDE_PLUGIN_ROOT}/skills/voice-gate-builder/references/dosing-and-silence.md` — the
  interior-dosing ladder and the silence / interior-leak rule, mapped into the existing slots.
- `${CLAUDE_PLUGIN_ROOT}/skills/voice-gate-builder/references/calibration-gate.md` — the two-stage
  gate, the grading surface, the headless fallback.
- `${CLAUDE_PLUGIN_ROOT}/skills/voice-gate-builder/references/extraction-method.md` — the evidence
  rule and corpus discipline, applied here only to pasted/uploaded samples.
- `${CLAUDE_PLUGIN_ROOT}/skills/voice-gate-builder/templates/profile-template.md` — the blank
  profile to fill.
- `${CLAUDE_PLUGIN_ROOT}/skills/voice-gate-builder/templates/calibration-template.md` — the blank
  calibration file to write and hand to the operator.

## Surface rendering: one interview, two deliveries

The interview content and the output contract are identical on every surface. Only how the
visualization reaches the writer changes. Choose by where this skill is running (full spec in
`references/surface-rendering.md`):

- **Cowork, claude.ai chat, or the desktop app (Code):** render the interview as an **in-chat
  visualization** — step by step, with the profile filling in live as the writer answers. The
  surface renders rich artifacts inline, so the writer never leaves the conversation.
- **A terminal Claude Code session:** the terminal cannot render inline, so **write the
  `templates/kickoff.html` artifact to a file and hand back the path** for the writer to open in a
  browser. Same questions, same live preview, same exports.

Default to the in-chat visualization where inline rendering is available; fall back to the written
HTML file when it is not, or when the writer asks for a file they can keep. The HTML artifact must
be offline-safe: zero external network references.

## Never (the five that protect the output)

- **Never treat an interview answer as verified.** Ungrounded answers are `self-reported
  (unverified)` and the calibration gate tests them first.
- **Never let a claim override a sample.** When a pasted sample contradicts the writer's answer, the
  sample wins and the contradiction is recorded.
- **Never self-grade the calibration gate.** A model grading its own predictions validates nothing.
- **Never write a fake completed calibration.** An ungraded gate ships `pending`, never a fake pass.
- **Never invent a seventh slot or rename one.** The runtime contract owns the schema.

## Procedure

### Step 1: scope and choose the surface

Confirm the writer, the forms the profile must cover (essay / newsletter / email), and whether they
have any samples to paste or upload (optional, never required). Choose the surface and rendering per
`references/surface-rendering.md`. Tell the writer plainly: the interview gets a usable profile, and
the calibration gate at the end is what proves it.

### Step 2: run the interview

Work `references/interview-script.md` slot by slot, rendered through the chosen surface. Ask the
questions for each of the six slots in order; show the profile filling in live. For §4 Native
pressures, present the nine pressures (danger, desire, secret, shame, contradiction, decision,
dread, curiosity, longing) and have the writer pick the two or three their strongest work runs on,
plus any that are off-voice or overused. Use the aspirational-voice probes: ask for a concrete
example behind every abstract claim, and never accept an adjective ("punchy", "warm", "plain") as a
slot value without a behavior or a line behind it.

### Step 3: ground any samples

If the writer pastes or uploads samples, run `references/sample-grounding.md`: clean them, then
check each interview answer against the real lines. Confirm what the prose confirms, flag what it
contradicts (the sample wins), and upgrade those slots from `self-reported (unverified)` to
`sample-grounded` with the citing line. Samples are evidence, not a second corpus sweep; a few
hundred words is enough to catch the big aspirational gaps. No samples is a valid run; the slots stay
`self-reported (unverified)` and the gate carries the grounding.

### Step 4: set the dosing ladder and the silence rule

Read the reused `dosing-and-silence.md` in full. Write the interior-dosing ladder into the profile's
§Identity register map and the interior-leak notes into §Preserve list and §Known surface tells,
exactly as that file specifies, filling the brackets from the writer's chosen native pressures
(Step 2). This is what lets the runtime flag "deep in the wrong room" and over-rendered private
subtext through its existing checks, with no runtime change.

### Step 5: draft the profile from the template

Fill the reused `profile-template.md` into the writer's profile file. Lead the register map from the
writer's plainest, most-frequent register, not the flashiest, or the gate calibrates to parody. Mark
every slot's evidence basis honestly: `sample-grounded` (a real line behind it) or `self-reported
(unverified)` (interview only). State overall confidence and the thin spots in the header. A profile
that hides its gaps gets trusted where it should not be.

### Step 6: calibration gate (human-graded, never self-graded)

Read the reused `calibration-gate.md` in full. Produce the two-stage gate into a calibration file
from the reused `calibration-template.md`: an 8-to-12-item scenario quiz on un-scened occasions, and
one test passage. **Grade the `self-reported (unverified)` slots first** — they are the highest-risk.
Then **stop and hand the calibration file to the operator.** The skill does not grade its own quiz
or passage. A failed item is a profile bug: route the fix back into the implicated slot. Headless
fallback (no operator mid-run): make the build calls, log them to a `DECISIONS.md`, write the
calibration file with every grade `pending`, and stop. Never self-grade.

On a graded pass, finalize the profile, link the calibration file beside it, and set up a
`voice-gate-runlog.md` from the runtime scorecard's run-log header. The profile is now ready to hand
to the `voice-gate` runtime as its supplied profile.

## Hard rules

- **Interview answers are provisional.** Ungrounded slots are `self-reported (unverified)`; the gate
  tests them first. Samples, when offered, outrank the claim.
- **Probe every abstraction.** No adjective becomes a slot value without a behavior or a line behind
  it. "I write plain" is a starting question, not an answer.
- **Match the runtime schema exactly.** Fill the six contract slots; do not invent a seventh or
  rename one. The runtime contract is the authority.
- **The skill never self-certifies.** The calibration gate is human-graded; headless runs write the
  gate and stop with grades pending.
- **Never write a fake completed calibration.** An ungraded gate ships `pending`, never a fabricated
  pass.
- **Light interior only.** Build only the interior the gate needs (native pressures, dosing). No
  full dossier, no relationship matrix, no narrative state.
- **The HTML artifact is offline-safe.** Zero external network references, so it opens anywhere and
  leaks nothing.
- **Em-dash scope.** The profile and calibration files this skill writes are config and grading
  worktables, not prose published under a writer's name, so normal punctuation is fine there. The
  only em-dash discipline is the runtime's render-time rule on the gate's rendered scorecard, which
  this skill does not produce.

## Phase note

This is the interview kickoff, the consent-first sibling of `voice-gate-builder` (corpus) in the
same plugin. Both feed the `voice-gate` runtime the same six-slot profile and both prove it through
the same human-graded calibration gate. A writer with a corpus they are happy to share can use the
builder; a writer without one, or who prefers not to share, uses this. The reviser that acts on the
gate's approved flags (`voice-reviser`) ships after the gate proves out.
