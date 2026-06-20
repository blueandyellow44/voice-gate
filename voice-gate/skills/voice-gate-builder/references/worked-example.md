# Worked example — building a profile for "Writer R" (synthetic)

One full synthetic build: a small corpus, the extraction, the filled profile, and a sample
calibration quiz left ungraded. Everything below is invented for illustration. It contains no real
person's material. "Writer R" is the same synthetic writer used in the runtime's
`worked-examples.md`, so the two skills demonstrate against one consistent target.

This is the only worked example shipped in the plugin. The real Max instance-zero build is a local,
private validation path and is never committed here.

---

## Step 1 — corpus and intake

Three short synthetic samples were supplied for Writer R, covering two forms.

**Essay sample (excerpt):**
> "The week I quit, I kept showing up to the empty office anyway. I told myself it was for the
> plants. That was true. It was also not the reason. On Thursday the lock had been changed. I stood
> in the hallway with a watering can, useless, and felt the thing I had been avoiding all week
> arrive on schedule. Not grief. Closer to vertigo."

**Newsletter sample (excerpt):**
> "Two updates this week, and one of them is late, which is on me. The build shipped Tuesday. It is
> slower than I want and I am not going to pretend otherwise. Here is what we changed and what we
> did not get to."

**Email sample (excerpt):**
> "Hi Dana. Thank you for the quick turnaround. I do not have notes on the draft; it reads clean.
> One scheduling question and then I will get out of your way. All my best, R."

Intake (count, do not judge): 3 samples, ~110 words, forms covered: essay, newsletter, email.
Sufficient to draft, thin on essay figuration (one figure only) — mark Slot 3 low-confidence for the
calibration gate to verify. Not a clean-failure case; enough to evidence every slot at least lightly.

## Step 2–3 — extraction and dosing

Evidence-cited traits, with the dosing ladder and silence rule folded into Slots 1, 5, 6.

## Step 4 — filled profile (the deliverable)

> Confidence: medium. Evidence base: 3 samples, ~110 words, essay + newsletter + email. Thin spots:
> figurative signature (one figure in corpus) — verify at calibration. Built by voice-gate-builder
> (synthetic). Calibration: ungraded.

**1. Identity and register map.** Plain, declarative floor; states cost without softening it; admits
fault directly. Floor — short plain sentences that concede before they explain: "It is slower than I
want and I am not going to pretend otherwise." Essay register — concrete scene, withheld naming of
feeling: "Not grief. Closer to vertigo." Email register — brief, warm-plain, fixed close: "All my
best, R." Interior dosing by form: high in personal essay (steered, not stated); low in newsletter;
near-zero in formal email. Essay-depth interior in a professional or email occasion is off-form
("deep in the wrong room").

**2. Hard guardrails.** No contractions in composed essay and email ("I do not", "it was not", "I am
not") — evidence across all composed samples; inferred-as-rule from consistent absence, verify at
calibration. No em dashes in any sample — inferred-from-absence; verify. Fixed email close "All my
best, R." — evidence: email sample.

**3. Figurative signature (low-confidence).** Near-zero figuration; one physical spine-figure when
present, drawn from the body and built environment: "felt the thing... arrive on schedule", "Closer
to vertigo. The floor was still there." No simile in corpus. Off-voice: decorative simile, abstract
figurative nouns. Verify the single-figure read at calibration.

**4. Native pressures.** Contradiction ("That was true. It was also not the reason.") and dread
("the thing I had been avoiding all week arrive on schedule"). Off-voice: easy uplift, motivational
energy (absent from all samples).

**5. Preserve list / signature moves.** Sentence fragments for emphasis ("Not grief.", "useless,").
Short plain sentence after a long one. Direct admission of fault as a move, not an apology ("which is
on me"). Steered, not stated: Writer R lets dread and contradiction drive detail selection and cuts
without naming them; protect this restraint, do not clarify a steered feeling into a stated one.

**6. Known surface tells.** (No corpus-specific overuse tic observed yet — thin corpus.) Interior
leak (over-rendered private subtext): naming the wound directly, psychologizing, or over-explaining
a feeling the scene already carried. Flag in essay when the interior is stated rather than steered;
flag in newsletter/email when essay-depth interior appears at all.

## Step 5 — calibration quiz (sample, ungraded)

The builder produced this and stopped. The operator grades it. Three of the planned 8 to 12 items
are shown; a real run writes the full set.

| # | Occasion (un-scened) | Form | Candidate (in voice) | Slots driving it | Grade | Note |
|---|----------------------|------|----------------------|------------------|-------|------|
| 1 | Telling a team a launch slipped a week | newsletter | "The launch moved to next Thursday. That is a week later than I told you, and the reason is mine, not the build's." | 1 (floor), 2 (no contractions), 5 (fault as move) | pending | |
| 2 | The morning after a hard decision, alone | essay | "I made the coffee I do not drink anymore and let it go cold while I decided nothing further." | 1 (essay), 4 (contradiction), 5 (steered, not stated) | pending | dosing+silence item: interior steers, stays unnamed |
| 3 | Declining a meeting invite by email | email | "Hi Sam. I am going to pass on Thursday so the team can focus. Thank you for thinking of me. All my best, R." | 1 (email), 2 (close), dosing (near-zero interior) | pending | dosing item: deep interior here would be "deep in the wrong room" |

**Test passage (sample, ungraded).** Occasion: returning a borrowed tool to a neighbor months late.
Form: essay.

> "The drill sat by my door for four months with his name still on the masking tape. I walked past it
> every morning and decided, each time, that today was not the day. When I finally knocked he did not
> remember lending it. That should have been a relief. I stood on his step holding the thing a little
> too long, and did not say the part where I had needed a reason to knock."

Grade: pending. (Note for the operator: does this read like Writer R — steered dread, withheld
naming, fragmentless but plain — or like a competent stranger?)

## Step 6 — stop

operator-disposition: pending. The builder hands this file to the operator and stops. No grade is
written. On a graded pass, the profile is finalized and handed to the voice-gate runtime as its
supplied profile.

---

## Contrast — a thin-corpus run that correctly clean-fails

Suppose only one sample was supplied: a single 40-word email, no essay, no newsletter, and the
profile is meant to cover all three forms.

Intake: 1 sample, ~40 words, only the email form represented. This trips the clean-failure floor
(a covered form has zero quotable samples; total under ~400 words). The builder stops and reports:

> Cannot build. The corpus covers only the email form (~40 words). Slots 1 (essay/newsletter
> register), 3 (figurative signature), 4 (native pressures), and 5 (preserve moves) have no quotable
> evidence; building them would mean fabricating a voice, which produces confident wrong gating.
> Supply essay and newsletter samples (roughly 400+ words across 3+ pieces), or narrow the profile
> to the email form only, and re-run.

No profile is written. No traits are invented. This is the correct unhappy-path outcome, not an
error to work around.
