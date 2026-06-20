# Extraction method — pulling each slot from the corpus

The method for filling the schema slots with cited evidence. It is the universal core of
`voice-corpus-extractor` (corpus discipline), `voice-profile-builder` (the evidence rule), and a
deliberately *light* slice of `character-dossier` (only enough interior for native pressures). It
is self-sufficient where those skills are not installed.

## The corpus discipline (front end)

1. **Attribute or omit, never guess.** Use only text the writer actually wrote. A scraped quote
   with no clear attribution is dropped, not assigned. A corpus that includes words the writer did
   not write teaches a voice that is not real.
2. **Clean before you analyze.** Strip navigation, timestamps, other people's words, boilerplate,
   or the profile learns the cruft.
3. **Count, do not judge, at intake.** Record word count, sample count, and which forms (essay /
   newsletter / email) are represented, before interpreting anything. Interpretation is the slot
   work, not the intake.
4. **Clean failure on thin evidence.** Concrete floor (same as SKILL Step 1): clean-fail if any
   covered form has zero quotable samples, or the whole corpus is under roughly 400 words / 3
   distinct samples. Stop and say which slots cannot be evidenced; ask for more samples or narrow
   the form scope. Do not fabricate to fill a slot.

## The evidence rule (every slot)

**No quote, no trait.** Each slot value names a habit and cites at least one verbatim line that
proves it. Keep description and quotation separate: the trait line states the habit, the evidence
line quotes the proof. Adjectives without quotes ("warm", "punchy") drift between readers; a real
line does not.

One exception, marked: a *ban* (Slot 2) is often evidenced by absence — the writer never uses em
dashes across the whole corpus. Record it as inferred-from-absence so the calibration gate verifies
it rather than trusting it.

## Per-slot extraction notes

- **Identity and register map (Slot 1).** Lead from the plainest, most-frequent register. Find the
  writer's floor — how they sound when not performing — and describe that first; then the shifts by
  form, each with a cited line. The loud, quotable register is the least frequent and the most
  parody-prone; leading with it produces a profile that generates caricature.
- **Hard guardrails (Slot 2).** Scan for mechanical consistency: punctuation, contractions by
  register, fixed openings/closings, banned words. Record what is true of THIS writer. Fidelity to
  the evidence, not to anyone's house style.
- **Figurative signature (Slot 3).** Inventory figures; name the type the writer actually reaches
  for and the dose by register. A plain writer's evidenced answer is "near-zero figuration"; that
  is a finding, not a gap to fill with invented imagery.
- **Native pressures (Slot 4) — the light interior read.** Read the writer's strongest pieces for
  which of the nine pressures actually drive them. Evidence is the piece: "this essay runs on
  contradiction and dread — quote." Do NOT psychologize from biography, do NOT build a wants/wounds
  dossier, do NOT enumerate relationships. Name the pressures the writing runs on, cite them, stop.
  This is the only interior the gate consumes.
- **Preserve list (Slot 5).** List the recurring moves that read as the writer rather than as
  error, each cited. This is the anti-flattening anchor; be specific.
- **Known tells (Slot 6).** Any habitual move that flattens this writer when overused, cited.

## State confidence

Every filled profile names its evidence base and where it is thin. Thin slots are marked
low-confidence so the calibration gate verifies them first. A profile that hides its gaps gets
trusted where it should not be.

## What this method does NOT do

- It does not impose a house style on the writer.
- It does not build a full character dossier, a relationship matrix, or any narrative state.
- It does not grade its own output. Validation is the human calibration gate.
