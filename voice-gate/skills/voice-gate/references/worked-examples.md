# Worked examples

Two fully worked runs on synthetic, non-private text, so the gate has a calibrated model of both
outcomes. All prose and both writer profiles below are invented for illustration. They contain no
real person's private material.

To make the personalized checks concrete, both runs use the same short synthetic profile:

> **Synthetic profile — "Writer R" (medium-form nonfiction).**
> §Hard guardrails: no em dashes (use commas, periods, or restructure); no contractions in
> composed essays. §Figurative signature: one dominant spine-figure per piece, drawn from
> physical work and weather; near-zero simile; abstraction-nouns are off-voice. §Native pressures:
> contradiction and dread; longing is overused, easy energy is off-voice. §Preserve list: short
> plain sentences after long ones; dry parenthetical asides; sentence fragments used for emphasis.

---

## Example 1 — a flawed run

### The piece (synthetic, flawed)

> We need to talk about rest.
>
> For years I treated recovery as a reward you earn after the work is done, a luxury, a soft thing
> you allow yourself once the hard part is over. I was wrong about that, and being wrong about it
> cost me more than I can say. Rest is not the absence of work but the other half of it.
>
> Last spring I burned out so badly I could not read a paragraph without losing the thread. The
> exhaustion sat on my chest like a heavy weight, a crushing pressure that showed me just how
> depleted I had become. That was the moment everything changed.
>
> Here is what I learned. Rest is not weakness. Rest is not laziness. Rest is the engine that makes
> everything else possible. Protect it, and the rest of your life will thank you.

### Measurement record (abbreviated)

- Form: personal essay. 168 words, 4 paragraphs.
- Surface candidates: stock opening ("We need to talk about rest."); rule-of-three list ("a
  reward... a luxury, a soft thing"); X-not-Y ("not the absence of work but the other half");
  explanation-after-image ("a crushing pressure that showed me just how depleted I had become");
  motivational closer ("the rest of your life will thank you"); stacked aphorisms ("Rest is not
  weakness. Rest is not laziness.").
- Guardrail scan (profile §Hard guardrails): one em dash candidate? No literal em dash, but
  "could not" / "I was wrong" are non-contracted, compliant. **One contraction-register check:
  none found. Clean on contractions.** (Note: had the draft read "I couldn't read a paragraph,"
  that is a Blocker against §Hard guardrails.)
- Figure inventory: spine-figure candidate "Rest is the engine" (abstract, generic); simile "sat
  on my chest like a heavy weight" (off-voice for Writer R, who is near-zero simile); abstraction
  noun "the exhaustion."
- Rhythm: paragraph 4 is four short equal-length sentences in a row (monotone, but possibly the
  aphoristic-button tell rather than rhythm).

### Grade isolated → consolidated scorecard

**Verdict: Not ready**

| Check | Status | Severity | Evidence quote | Source rule | What's off | Suggested fix direction |
|-------|--------|----------|----------------|-------------|------------|-------------------------|
| Surface: stock opening | Flag | Should-fix | "We need to talk about rest." | checks/06-originality.md §Lane-tics + checks/01 | Lane-centroid opening; any author could write it | Open on the concrete spring it broke down, not an announcement |
| Surface: rule-of-three | Flag | Polish | "a reward you earn... a luxury, a soft thing" | checks/01-surface-tells.md §Rule-of-three | Three balanced items satisfying by symmetry, not truth | Keep the truest one, cut the other two |
| Surface: explanation after image | Flag | Should-fix | "a crushing pressure that showed me just how depleted I had become" | checks/01-surface-tells.md §Explanation after image | The clause names the feeling the image already gave | Cut everything after "chest"; let the image stand |
| Surface: motivational closer | Flag | Should-fix | "the rest of your life will thank you" | checks/01-surface-tells.md §Motivational cadence | Newsletter-signoff aimed at the reader, not the thing itself | End on the exhaustion or the return, not a benediction |
| Narrator: too-smooth self-understanding | Flag | Blocker | "That was the moment everything changed." | checks/02-narrator-clean.md §Too-smooth self-understanding | He knows exactly what it meant before it is over; reconciled too cleanly | Let the change be partial or misread at the time; remove the clean hinge |
| Propulsion: restatement | Flag | Should-fix | "Rest is not weakness. Rest is not laziness. Rest is the engine..." | checks/03-propulsion.md §The compounding test | Paragraph 4 restates the thesis at the same intensity; no cost rises | Cut the buttons; end where the cost is highest |
| Propulsion: single-pressure | Flag | Polish | (whole piece) | profile §Native pressures | Runs on easy uplift; Writer R's contradiction and dread are absent | Return to what was frightening about not being able to read |
| Figure: off-voice simile | Flag | Should-fix | "sat on my chest like a heavy weight" | profile §Figurative signature | Simile is off-voice for Writer R; also a dying metaphor | Demote to a plain physical image, no "like" |
| Figure: abstract spine | Flag | Should-fix | "Rest is the engine that makes everything else possible" | checks/04-figurative.md §Abstract figurative noun | The spine-figure rests on a generic abstraction | Replace with the physical/weather register the profile names |
| Line: monotone rhythm | Pass | — | (paragraph 4) | checks/05-line-craft.md §Rhythm | — (folded into the propulsion/aphorism flags; not a separate defect) | — |
| Originality: stock metaphor | Flag | Polish | "Rest is the engine" | checks/06-originality.md §Lane-tics | Stock productivity-lane metaphor (the engine/the unlock family) | Reach for Writer R's own work/weather figure |
| Preserve: over-polish risk | Pass | — | — | checks/07-preserve.md | Protect list is short; the piece needs work, not protection | — |

**Protect:** "I could not read a paragraph without losing the thread" — concrete, particular,
the one line doing real work. Do not touch it while fixing the surrounding flags.

**Close.** Checks run: all (personal essay). Narrator was in scope (first-person reflection).
Profile status: supplied; filled Hard guardrails, Figurative signature, Native pressures, Preserve
list. Verdict **Not ready**: one Blocker (the narrator is reconciled before the experience is over,
which breaks the voice the profile describes). Recommended next action: hand to the reviser with
the narrator Blocker as the approved target; the surface and figure flags are secondary.
Run-log line: `2026-06-20 | rest-essay-synthetic | Not ready | blocker:1 should-fix:6 polish:3 | operator-disposition: pending`

---

## Example 2 — a clean-pass run

### The piece (synthetic, clean)

> The week I quit, I kept showing up to the empty office anyway.
>
> I told myself it was for the plants. Someone had to water them, and I was the one with a key.
> That was true. It was also not the reason. The reason was that I did not yet know who I was
> without the badge, and the building still let me in.
>
> On Thursday the lock had been changed. I stood in the hallway with a watering can, useless, and
> felt the thing I had been avoiding all week arrive on schedule. Not grief. Closer to vertigo. The
> floor was still there. I just could not feel it.
>
> I left the can by the door. I do not know who waters them now.

### Measurement record (abbreviated)

- Form: personal essay. 150 words, 4 paragraphs.
- Surface candidates: none firing. No stock opening (concrete scene), no rule-of-three, no
  motivational closer, no explanation-after-image (the vertigo image stands unglossed).
- Guardrail scan: no em dashes; no contractions ("did not", "do not", "could not"). Compliant with
  §Hard guardrails.
- Figure inventory: spine-figure "the floor was still there. I just could not feel it" (physical,
  carries the dread; on-voice for Writer R). No simile. No abstraction noun.
- Rhythm: varied; short fragments ("Not grief.", "useless,") after long sentences, which the
  profile's §Preserve list names as a signature move.

### Grade isolated → consolidated scorecard

**Verdict: Good to go**

| Check | Status | Severity | Evidence quote | Source rule | What's off | Suggested fix direction |
|-------|--------|----------|----------------|-------------|------------|-------------------------|
| Surface: AI-polish tells | Pass | — | "I left the can by the door." | checks/01-surface-tells.md | — | — |
| Narrator: self-understanding | Pass | — | "I did not yet know who I was without the badge" | checks/02-narrator-clean.md | — (contradiction enacted, not named; mixed motive shown) | — |
| Propulsion: compounding | Pass | — | "felt the thing I had been avoiding all week arrive on schedule" | checks/03-propulsion.md §The compounding test | — (cost rises to the changed lock; dread, on-voice) | — |
| Figure: spine landing | Pass | — | "The floor was still there. I just could not feel it." | profile §Figurative signature | — (physical spine-figure carrying dread; on-voice) | — |
| Line craft | Pass | — | "Not grief. Closer to vertigo." | checks/05-line-craft.md | — | — |
| Originality: lane-tics | Pass | — | "I kept showing up to the empty office anyway" | checks/06-originality.md | — (no lane-centroid moves) | — |
| Preserve: over-polish risk | Flag | Polish | "useless," | checks/07-preserve.md §Revision discipline | The fragment is doing voice work; a reflexive editor might "fix" it | Do not touch it; flagged only to protect it |

**Protect:** the fragments ("Not grief.", "useless,"), the flat closing line ("I do not know who
waters them now."), and the withheld naming of the feeling (vertigo, not grief). These are the
voice. Any revision that smooths them flattens the piece.

**Close.** Checks run: all (personal essay). Profile status: supplied; all slots used. Verdict
**Good to go**: every craft check passes; the single Preserve row is a Polish-level protect note,
not a fix, so the derived verdict stays Good to go (no Blocker, no Should-fix, and the lone Polish
row is a do-not-touch flag rather than a defect). Recommended next action: do not revise.
Run-log line: `2026-06-20 | empty-office-synthetic | Good to go | blocker:0 should-fix:0 polish:1 | operator-disposition: pending`

> Note on the derived verdict: a strict reading of the rule (any Polish → Good to go with fixes)
> would land on "Good to go with fixes." Because the only Polish row is a protect-this note with no
> fix attached, the gate records it but reports **Good to go** and says so in the close. When a real
> fix is attached to a Polish row, the verdict is **Good to go with fixes**. Document the call in the
> close either way; never silently override the derivation rule.
