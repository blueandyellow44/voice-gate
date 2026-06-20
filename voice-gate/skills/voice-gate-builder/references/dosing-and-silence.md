# Interior dosing and the silence rule

The builder reads a *light* interior (Slot 4, native pressures) so the gate knows what drives the
writer's strongest work. But interior pressure is not meant to be poured onto every page. Two rules
govern how it is dosed and when it stays silent. Both are written INTO the existing profile slots,
so the `voice-gate` runtime consumes them through its existing checks with no runtime change.

## The dosing ladder

Interior pressure belongs in different amounts in different rooms. The same depth that makes a
personal essay land makes a formal email read as oversharing.

- **Personal essay / reflection:** interior pressure can run high. The form invites the writer's
  contradiction, dread, longing onto the page (steered, see the silence rule).
- **Newsletter / professional post:** lower. Some interior gives it a pulse; too much reads as a
  diary in a professional room.
- **Formal email:** near-zero or absent. The interior may steer a word choice, but the form does
  not host it. A formal email carrying essay-depth interior is **"deep in the wrong room."**

**"Deep in the wrong room" is a defect, not sophistication.** Depth dropped into a form that does
not host it is a failure of judgment, the same class of error as a flat essay. Do not reward it.

**Where it goes in the profile:** write the ladder into **Slot 1 (Identity and register map)** as an
explicit "interior dosing by form" line. The runtime's propulsion and narrator checks read the
register map; an essay-depth interior move in an email occasion then reads as off-form against the
stated ladder.

## The silence rule

Interior pressure should **steer** the writing. It should not necessarily **appear** on the page.
The wound that drives an essay is most powerful when it shapes which details the writer chooses,
which sentence they cut, where they stop — not when it is named outright. Naming the interior
directly ("this is about my fear of being left") usually drains it; letting it steer ("I kept
showing up to the empty office anyway") keeps it live.

So the builder records two things:

1. **What the interior steers** → **Slot 5 (Preserve list / signature moves)**, as a note: the
   writer lets [pressure] steer the prose without naming it; protect that restraint, do not "clarify"
   it into a stated feeling. The runtime's preserve governor then guards the restraint instead of
   sanding it.
2. **Interior leak as a tell** → **Slot 6 (Known surface tells)**, as a named tell:
   **over-rendered private subtext** — the writer (or a draft in the writer's voice) naming the
   wound directly, psychologizing, or over-explaining the feeling the scene already carried, instead
   of letting it steer. The runtime's surface check (01) and narrator check (02) already read Slot 6;
   with this tell present, they flag interior leak as a finding the same way they flag any surface
   tell, with an exact quote and this slot as the source rule.

This is how the builder "teaches the runtime to flag interior leak" without touching the runtime:
the teaching is data in the supplied profile's existing slots, not new code in the gate.

## How to phrase the two profile entries (templates)

For **Slot 1**, append a line like:

> Interior dosing by form: high in personal essay (steered, not stated); low in newsletter; near-
> zero in formal email. Essay-depth interior in a professional or email occasion is off-form ("deep
> in the wrong room").

For **Slot 5**, append:

> Steered, not stated: the writer lets [the writer's native pressure] drive detail selection and
> cuts without naming it. Protect this restraint; do not clarify a steered feeling into a stated one.

For **Slot 6**, append:

> Interior leak (over-rendered private subtext): naming the wound directly, psychologizing, or
> over-explaining a feeling the scene already carried. Flag in essay when the interior is stated
> rather than steered; flag in newsletter/email when essay-depth interior appears at all.

Fill the brackets from the writer's evidenced native pressures (Slot 4). Keep the writer's actual
material out of any distributed artifact; in the shipped worked example these are written for the
synthetic writer only.
