# Check 07 — preserve over polish (the anti-flattening governor)

Universal method, stripped from `max-preserve-over-polish-pass`. This check runs at **render
time** as a governor over the whole scorecard, not as just another finding source. The failure it
prevents: a piece edited past its voice by improving everything improvable. Over-editing is itself
a flattening mechanism. A piece that passes every craft check but reads like a competent stranger
has been edited past its voice.

Proposes a Protect list and weak-line findings only. Renders no verdict.

## Reads from

- The piece and the consolidated findings from all other checks.
- The supplied profile, if present: §Preserve list / signature moves. **Read this first.** It
  names what reads as the writer rather than as error.

## Method

1. **Name what not to touch first.** Before weighing any flag, read the piece for what is already
   working, cross-referenced against the profile's §Preserve list:
   - dry asides, including parenthetical ones
   - slightly jagged transitions that read as movement, not error
   - short plain sentences after long ones
   - odd constructions that break a rule but read as the writer
   - sentence openings that look repetitive but set a deliberate rhythm
   - local rawness that carries voice
   List these explicitly as the consolidated Protect list. This step is not optional.
2. **Then** review the other checks' findings against the Protect list. If a finding would, in
   the fixing, damage a preserved line or move, flag the **adjacency risk**: the revision must not
   touch the preserved line while fixing the weak one.
3. Add any weak-line findings the other checks missed: a line that could be sharper without
   requiring anything around it to change.
4. **Over-polish judgment.** If the Protect list is long and the flag count is low, say so: this
   piece may not need revision. This judgment goes into the close and can pull a borderline
   verdict back from "Good to go with fixes" toward "Good to go" when the only flags are Polish.

## Output

- **Protect list** (always first, consolidated from every check and the profile).
- **Weak-line findings** (scorecard rows): Check `Preserve: weak line` / `Preserve: weak move`,
  Severity, Evidence quote, Source rule (`checks/07-preserve.md §Revision discipline` or `profile
  §Preserve list`), What's off, Suggested fix direction (one word, one cut, one concrete swap).
- **Adjacency risks:** flagged item X is next to preserved item Y; do not touch Y while fixing X.
- **Over-polish note** (if applicable): this piece may not need revision.

## Hard rules

- The Protect list comes before the flags. Always.
- Do not globally polish. Do not improve the neighborhood of a flagged line.
- Do not normalize odd constructions or flatten jagged transitions.
- Do not convert rawness into correctness.
- Do not produce prose that reads like a competent stranger: technically correct, no longer the
  writer.
- Never recommend a revision without naming what should survive.
