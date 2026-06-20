# Profile schema — the builder's output, slot by slot

The builder emits one supplied profile matching the runtime contract
(`voice-gate/skills/voice-gate/references/voice-profile-contract.md`). That contract is the schema
authority. This file maps each slot to how the builder fills it from corpus evidence. Do not invent
a seventh slot or rename one; the runtime reads exactly these.

Every slot value cites at least one verbatim quote from the writer's corpus. No quote, no trait.

## Slot 1 — Identity and register map

**What it is:** who the writer is on the page, and how the register shifts by form (essay vs
newsletter vs email). It must let a check tell "this reads like the writer" from "this reads like a
competent stranger." Names the forms this profile covers.

**How the builder fills it:** from the cleaned corpus, state the writer's plainest, most-frequent
register first (lead from the floor, not the flashiest register, or the gate calibrates to
parody). Then describe how the register changes per form, citing a representative line from each
form. **This slot also carries the interior-dosing ladder** (Slot work shared with
`dosing-and-silence.md`): high interior pressure in personal essay, lower in newsletter, near-zero
in formal email.

## Slot 2 — Hard guardrails (mechanical, non-negotiable)

**What it is:** the writer's absolute mechanical rules, each testable by quote. A violation is a
Blocker in the runtime — the most objective failure the gate finds.

**How the builder fills it:** read the corpus for mechanical consistency and record what is
actually true of this writer: punctuation policy (does the writer use em dashes, or never?),
contraction policy by register, banned constructions or words, fixed openings and closings.
**Profile the writer, not a house style.** If the corpus shows em dashes and contractions, the
guardrail records that; do not import another writer's bans. Each guardrail cites a line that
demonstrates it (or, for a ban, note the absence across the corpus and mark it inferred-from-
absence so calibration verifies it).

## Slot 3 — Figurative signature

**What it is:** how the writer uses figuration natively, so the runtime's figurative check
measures the right thing instead of generic creative-writing rules.

**How the builder fills it:** inventory the corpus's figures, name which the writer actually uses
(e.g., one dominant spine-figure and personification; or dense simile; or near-zero figuration in
a plain register), which are off-voice, and the dose by register. Cite a landed figure for each
claim. If the corpus is too plain to show a signature, say so; a plain writer's signature is "near
zero, plain register," which is a valid, evidenced answer.

## Slot 4 — Native pressures

**What it is:** which of the nine pressures (danger, desire, secret, shame, contradiction,
decision, dread, curiosity, longing) the writer's strongest work runs on, and which are off-voice
or overused. The runtime's propulsion check uses it to tell "running on a third of the engine"
from "this is how the writer compounds."

**How the builder fills it:** the *light* interior read in `extraction-method.md`. Identify, from
the pieces themselves, which pressures recur in the writer's best work; cite the piece. This is
evidenced from the writing, not psychologized from biography. Do not build a dossier; name the
pressures and stop.

## Slot 5 — Preserve list / signature moves

**What it is:** what reads as the writer's voice rather than as error, so the runtime's preserve
governor protects it instead of sanding it.

**How the builder fills it:** from the corpus, list the recurring moves that are the writer (dry
parenthetical asides, jagged transitions that read as movement, short plain sentences after long
ones, rule-breaking constructions that feel like the writer, deliberate repetition). Cite an
instance of each. The more specific this slot, the better the gate protects the voice. **It also
carries the interior-leak preserve note** from `dosing-and-silence.md`: what the writer lets steer
the prose without naming it.

## Slot 6 — Known surface tells (optional)

**What it is:** the writer's specific recurring tics the runtime's surface check should watch for
beyond the universal set.

**How the builder fills it:** from the corpus, any habitual move that flattens *this* writer
specifically when overused. **This slot also carries the interior-leak tell** from
`dosing-and-silence.md`: over-rendered private subtext (naming the wound directly rather than
letting it steer), so the runtime flags it through the existing surface and narrator checks.

## Optional — calibration examples

A few short before/after pairs from the writer's own non-private material (a flattened line and the
writer's repair), to help the runtime calibrate severity. Keep these to non-private material; the
gate never needs a personal dossier. The builder produces these only if the corpus supports them.

## Output location and confidence

Write the filled profile to the writer's chosen location (default: a `voice-gate-profile.md` in the
writer's working folder), not into this plugin. State the confidence level and the thin spots in a
short header. A profile that hides its gaps gets trusted where it should not be.
