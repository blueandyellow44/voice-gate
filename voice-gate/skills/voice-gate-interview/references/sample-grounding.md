# Sample grounding — checking the interview against real lines

When the writer pastes or uploads samples, they outrank the interview. This file says how to use a
small amount of real prose to confirm or correct the self-reported answers. It applies the evidence
rule and corpus discipline from the reused
`${CLAUDE_PLUGIN_ROOT}/skills/voice-gate-builder/references/extraction-method.md`, scoped to the
samples on hand, not run as a full corpus sweep.

Samples are optional. A run with none is valid; the slots stay `self-reported (unverified)` and the
calibration gate carries the grounding.

## What samples are for

Not to rebuild the corpus path. To catch the **aspirational gaps** — the places where the writer's
self-description and their actual prose part company. A few hundred words usually exposes the big
ones (claimed-plain-but-figurative, claimed-no-clichés, claimed-rich-imagery-but-flat).

## Method

1. **Clean first.** Strip navigation, timestamps, other people's words, boilerplate. Use only text
   the writer actually wrote; attribute or omit, never guess.
2. **Take each interview answer to the prose.** For every slot the writer asserted, look for lines
   that confirm it or contradict it:
   - Slot 2 guardrails: does the writer claim "no em dashes" while the sample uses them? Does the
     "always non-contracted" claim survive the actual sentences?
   - Slot 3 figurative signature: count the figures. "Near-zero" with three similes on the page is a
     contradiction. "Rich imagery" with none is the other one.
   - Slot 1 register / Slot 5 preserve moves: do the claimed moves actually appear?
3. **The sample wins.** Where prose contradicts the claim, record what the prose shows, and note the
   contradiction for the calibration gate ("writer reported near-zero simile; samples show three —
   grade this first"). Do not split the difference; do not let the flattering claim stand against
   the evidence.
4. **Upgrade the basis.** A slot value a sample line supports moves from `self-reported (unverified)`
   to `sample-grounded`, citing the line. A slot the samples neither confirm nor contradict stays
   `self-reported (unverified)`.

## Limits — what grounding does not become

- **Not a full corpus build.** If the writer turns out to have a real corpus and wants the
  evidence-first treatment, route them to `voice-gate-builder`. This skill grounds a handful of
  samples; it does not promise corpus-grade coverage.
- **Not a license to skip the gate.** Grounded slots are stronger than ungrounded ones, but samples
  are still a thin slice. The human-graded calibration gate runs either way.
- **No quote, no upgrade.** A slot only becomes `sample-grounded` with a citing line. Absent that,
  it stays unverified; never mark a slot grounded to look thorough.

## After grounding

Carry the basis marks into the profile draft (Step 5): each slot reads `sample-grounded` (with its
line) or `self-reported (unverified)`. The calibration gate (Step 6) grades the unverified slots
first, because those are where an interview is most likely to have recorded the writer the writer
wishes they were.
