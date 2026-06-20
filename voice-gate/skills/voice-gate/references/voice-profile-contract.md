# Supplied voice profile — the contract

`voice-gate` diagnoses a piece against a **supplied** voice profile. It does not generate the
profile (that is the builder, a later phase) and it never infers the profile from the piece being
graded. This file states what a supplied profile must provide so the personalized checks have
something to calibrate against.

A profile is the single source of truth for the personalized layer. The universal checks must not
carry their own private voice standards that could drift from it. One clean target, calibrated
once.

The profile is plain markdown with the sections below. Any section may be absent; an absent
section means the checks that depend on it are reported `Skipped — profile slot not supplied`,
never silently passed.

## Required slots

### 1. Identity and register map

One or two paragraphs: who the writer is on the page, and how their register shifts by form
(essay vs newsletter vs email). Enough that a check can tell "this reads like the writer" from
"this reads like a competent stranger." Names the forms this profile covers.

### 2. Hard guardrails (mechanical, non-negotiable)

The writer's absolute mechanical rules, each one testable by quote. Examples of the *kind* of
rule (not prescriptions — fill in the writer's actual ones):

- punctuation bans or requirements (for one writer: no em dashes; for another: Oxford comma always)
- contraction policy by register (composed prose vs casual)
- banned constructions or words the writer never uses
- fixed openings and closings (greeting form, sign-off form)

A violation of a hard guardrail is a **Blocker** by default — it is the most objective failure
the gate can find. The `01-surface-tells` and `05-line-craft` checks read this slot; an email run
reads it directly.

### 3. Figurative signature

How this writer uses figuration natively, so `04-figurative.md` measures the right thing instead
of generic creative-writing rules. State:

- which figures the writer actually uses (e.g., personification and one dominant spine-metaphor;
  or dense simile; or near-zero figuration in a plain register)
- which figures are off-voice for them
- the dose by register (creative vs essay vs academic)

Without this slot, `04-figurative` runs the universal landing/keep-cut tests only and does not
judge figure *choice* against the writer's signature.

### 4. Native pressures

Which of the nine pressures (danger, desire, secret, shame, contradiction, decision, dread,
curiosity, longing) this writer's strongest work actually runs on, and which are off-voice or
overused. `03-propulsion.md` uses this to tell "running on a third of the engine" from "this is
simply how the writer compounds." Without it, the propulsion check diagnoses presence/absence of
*some* live pressure but cannot say the writer is underusing their own range.

### 5. Preserve list / signature moves

What reads as the writer's voice rather than as error, so `07-preserve.md` protects it instead of
sanding it. Examples of the *kind*: dry parenthetical asides, deliberately jagged transitions,
short plain sentences after long ones, rule-breaking constructions that feel like the writer,
deliberate repetition. This is the anti-flattening anchor; the more specific it is, the better the
gate protects the voice.

### 6. Known surface tells (optional)

The writer's specific recurring tics, if known, that `01-surface-tells.md` should watch for beyond
the universal set. Optional; the universal surface check runs without it.

## Calibration examples (optional but strong)

If the profile includes a few short before/after pairs (a flattened line and the writer's repair),
the gate can calibrate severity more accurately. Keep these to the writer's own non-private
material; the gate never needs, and must never be handed, a personal dossier to do its job. The
gate's altitude is line plus one propulsion lens; it does not consume interior biographical
material.

## What the profile is NOT

- Not a generation engine. The gate diagnoses; it does not write.
- Not an interior dossier. The gate works at line altitude plus one propulsion lens. It does not
  need, and should not be given, the writer's private wants, wounds, relationships, or biography.
  That depth belongs to a heavier tool and a later phase; keeping it out is what makes this gate
  shareable.
