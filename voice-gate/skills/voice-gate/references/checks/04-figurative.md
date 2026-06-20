# Check 04 — figurative landing

Universal method, stripped from `max-figurative-language-pass`. A figure-level craft check: does
each metaphor, simile, image, personification, or symbol actually land, or is it decorative,
cliché, over-explained, mixed, strained, or too clever? It diagnoses; it does not rewrite.

Proposes findings only. Renders no verdict. May propose zero findings.

## Applicability

Run when the piece carries imagery. On emails, instructional posts, or plain-register pieces with
no figuration, this check is `Skipped` (record it). Never flag low figure density as a problem in
the abstract; a plain sentence beats a weak figure.

## Reads from

- The measurement record (§3 figure inventory, including the candidate spine-figure).
- The supplied profile, if present: §Figurative signature (which figures are native to the
  writer, which are off-voice, the dose by register). **This slot is what makes the check judge
  figure *choice*, not just landing.** Without it, run the universal landing/keep-cut tests only
  and do not judge a figure as off-voice.

## Method

1. Read once for what is alive. Note figures that land before hunting for ones that fail. Default
   posture is protective.
2. Confirm the **spine-figure**: the one figure carrying the piece's central pressure. Everything
   else is a local figure that should serve it or stay out of its way.
3. For each figure in the inventory, run the keep/cut tests:
   - **ground test** — is there a real tenor/vehicle/ground, or just a vibe?
   - **interaction, not label** — does the figure do work, or just decorate?
   - **novelty dial** — is it fresh, or a dying metaphor?
   - **image, not gloss** — does a literal image do the work without an explanatory clause after?
   - **effort vs reward** — does decoding cost more than it repays?
4. Flag failures by name:
   - **cliché / dying metaphor**
   - **constructed conceit / clever button** (a manufactured frame written for effect)
   - **abstract figurative noun** (the figure rests on "warmth/connection/presence")
   - **over-explanation after the image** (the gloss naming what the image already gave)
   - **mixed metaphor / catachresis** (two images that cannot share one scene)
   - **strained / far-fetched** (decoding costs more than it repays)
5. Check **dose against register**: dense figuration suits creative prose; one spine-figure plus
   restrained local figures suits an essay; a governing conceit and near-zero figure suits an
   academic register. If a profile names the writer's dose, judge against it; otherwise judge
   against register convention.
6. For each flag: quote the figure, name the failure and the test it fails in one sentence, give a
   smallest-change direction (demote, concretize, cut the gloss, replace), not a rewrite.
7. Note figures to **protect**: especially the spine-figure and any concrete-object closer.

## Output

- **Spine-figure:** the dominant figure and the pressure it carries (or "none found" if the
  register expects one and the piece lacks it).
- Proposed findings (scorecard rows): Check `Figure: <failure type>`, Severity, Evidence quote
  (the figure, quoted), Source rule (`checks/04-figurative.md §<test/failure>` or `profile
  §Figurative signature`), What's off, Suggested fix direction.
- **Protect:** figures already landing.

If no figures fail, report "no figurative findings from this check" and note the spine-figure to
protect.

## Hard rules

- Must be allowed to propose zero findings and to say "protect this figure."
- Never add a metaphor because a passage lacks one, and never force lyricism: a figure inserted to
  fill a gap reads as the editor's voice intruding, not the writer's, which is the exact flattening
  this gate exists to catch.
- Never over-explain an image that already landed; the fix for a strong image is usually to cut
  the sentence after it.
- Never import generic creative-writing advice wholesale. If a profile names the writer's
  figurative signature, that governs; without it, judge landing and register only.
- Do not measure figuration by simile count; that is a flatness backstop only.
- Skip on emails, texts, and plain/academic pieces unless imagery is explicitly in question.
