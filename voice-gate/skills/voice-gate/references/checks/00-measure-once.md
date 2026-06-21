# Check 00 — measure once

Run this **once**, before any grading. It produces the single measurement record every other
check reads from. No check re-measures the piece from scratch; that is what keeps the gate fast
and coherent and stops seven checks from reading the piece seven different ways.

This is a deterministic parse, not a judgment. It records what is there. The checks judge.

## Produce this record

### 1. Form and length

- Form (essay / newsletter / post / email), as confirmed at intake.
- Word count, paragraph count, and section count (if the piece has sections). Count
  mechanically, not by estimate: words are whitespace-separated tokens; paragraphs are blocks
  separated by a blank line; sections are explicit headers. Record exact integers, never a
  rounded or `~` figure. Every downstream count claim (rule-of-three lists, rhythm runs, echo
  tallies) inherits this one, so a loose count here propagates. If you cannot state it as an
  exact integer, you have not measured it yet.

### 2. Section map

An ordered list of the piece's sections or major beats, each with a one-clause summary of what it
does. For a piece with no explicit sections, segment by paragraph cluster. `03-propulsion.md`
reads this map to run the compounding test section by section.

### 3. Figure inventory

Every figure in the piece, listed with its location and type: metaphor, simile, image doing
figurative work, personification, metonymy/synecdoche, conceit/extended figure, or abstract
figurative noun. Mark the candidate **spine-figure**: the one figure (if any) carrying the
piece's central pressure. `04-figurative.md` grades from this inventory.

### 4. Surface-tell candidates

Flag, by quote and location, every instance of the mechanical surface patterns (do not judge yet,
just record locations):

- rule-of-three lists (three balanced items)
- "not X, but Y" / "X-not-Y" constructions
- sentence-final aphorism or wisdom-button paragraphs
- explanation clauses that follow an image and name its feeling
- motivational / newsletter-signoff cadence at paragraph ends
- filter words (felt, saw, noticed, realized, seemed, watched, etc.) before a perception

### 5. Rhythm samples

Sentence-length series for two or three representative paragraphs (just the word counts per
sentence, in order), so `05-line-craft.md` can see monotone runs without re-reading. Note any run
of four or more sentences of near-equal length.

### 6. Mechanical guardrail scan (if a profile is supplied)

For each hard guardrail in the supplied profile's §Hard guardrails slot, record every violation
by quote and location: em dashes if banned, contractions if banned in this register, banned
constructions, wrong greeting/sign-off form. This is the most objective measurement the gate
makes; record it precisely so `01-surface-tells.md` and the email path can flag Blockers from it.

When a dash guardrail is in play, count dashes by exact glyph so the tally cannot drift: the em
dash (U+2014 `—`), the en dash (U+2013 `–`), and the double-hyphen (`--`) are each dash
candidates, spaced or unspaced. Record each occurrence by quote and location and report an exact
integer per glyph; a single hyphen inside a compound word (`well-built`) is not a dash. Flag only
the glyphs the profile actually bans; the others are recorded for the count, not flagged.

### 7. Echo scan

Repeated distinctive words or phrases (not function words) appearing three or more times, with
locations. `05-line-craft.md` and `06-originality.md` read this to separate deliberate motif from
unintentional echo.

### 8. Claim-shape scan (scope-boundary handoff only)

Voice Gate does **not** check facts, sourcing, or strategy. This section exists so the gate can say
so honestly and point at the right tool, not so it can grade truth. Record, by quote and location,
every instance of claim-shaped language. **Detect the shape, never judge whether it is true,
sourced, or on-strategy.** That judgment is out of scope and belongs to a ship-safety gate
(de-slop) or a fact-checker.

- numeric / statistical claims (a `%`, a multiplier like `2.4x`, a hard count, "thousands")
- authority appeals ("studies show", "research shows", "experts say", "data proves", "it is
  well known that")
- named factual or strategy assertions (a capability, positioning, or world-fact claim stated as
  settled, e.g. "now scales to thousands of users")

A hedged or colloquial generalization with no number and no authority appeal (a dry aside like
"most people do", "it usually works out") is not claim-shaped; do not count it. Counting a writer's
native aside here would put a preserve-listed voice move into the scope-boundary line, which is
wrong: this scan is for facts/sourcing/strategy hand-off, not for voice.

Report an exact integer total. This count never becomes a finding, a scorecard row, or a Blocker;
it feeds only the "Out of scope (not graded)" line in the close (see `scorecard.md` §4). A piece
with zero detected claims is normal; a piece full of them is not thereby flawed in voice.

## Output

A compact record with the eight sections above. Hand it to the grading checks. Section 8 is the
only one that does not feed a grading check; it feeds the close's scope-boundary line. Do not draw
conclusions here; "three rule-of-three lists at paragraphs 2, 5, 9" is a measurement, "the piece
leans on rule-of-three" is a judgment the surface check makes. Likewise "two authority appeals at
paragraphs 1 and 4" is a measurement; whether they are true is not the gate's call.
