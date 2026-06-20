# Check 06 — originality (lane-pastiche / centroid)

Universal method, drawn from originality-guard. Catches prose that reads like the centroid of its
lane: the phrasing, structure, and moves that a thousand pieces in the same genre already share.
Distinct from `05-line-craft` (a dead line can still be original) and from `01-surface-tells`
(an AI-polish tell can appear in otherwise original prose). This check asks: has the piece
defaulted to its lane's average?

Proposes findings only. Renders no verdict. May propose zero findings.

## Reads from

- The piece, plus the measurement record (§4 surface candidates, §7 echo scan).
- The supplied profile, if present: §Identity and register map, §Known surface tells (so the
  writer's own signature is not mistaken for lane-pastiche).

## Method

1. Name the **lane**: the genre/format the piece sits in (founder essay, productivity newsletter,
   personal-growth Substack, technical explainer, etc.). The lane has a centroid: its stock
   openings, stock transitions, stock metaphors, stock closings.
2. Scan for **lane-tics** — moves that belong to the lane's average rather than to this writer:
   - stock openings ("We need to talk about...", "Here's the thing.", a rhetorical question cold)
   - stock transitions ("But here's where it gets interesting", "And that's when it hit me")
   - stock metaphors for the lane (the iceberg, the muscle, the journey, the unlock)
   - stock closings (the call-to-reflection, the zoom-out to a universal, the one-line button)
3. For each, ask whether **this writer** would reach for it, or whether it is the lane reaching
   through the writer. If a profile is supplied, judge against §Identity and §Known surface tells;
   without one, judge against lane convention and whether the move is generic enough that any
   lane author could have produced it.
4. Separate a writer's earned signature move (it recurs across their work and carries their
   pressure) from a lane-tic (it is the genre's default, not the writer's choice).
5. For each flag: quote it, name the lane-tic, give a smallest-change direction toward the
   writer's own move, not a generic "be more original."

## Output

Proposed findings (scorecard rows): Check `Originality: <lane-tic type>` (stock opening / stock
transition / stock metaphor / stock closing / lane-centroid phrasing), Severity, Evidence quote,
Source rule (`checks/06-originality.md §Lane-tics` or `profile §Identity`), What's off, Suggested
fix direction. Plus a Protect list of the writer's earned signature moves.

If nothing fails, report "no originality findings from this check."

## Hard rules

- Must be allowed to propose zero findings.
- Do not flag a writer's earned signature move as a lane-tic. The Preserve and Identity slots
  exist to prevent exactly this.
- Do not prescribe "be more original" with no quote and no direction. Quote the lane-tic, name the
  lane, point at the writer's own move.
- A single lane-tic is usually Polish; a piece built entirely from lane-centroid moves (it could
  carry any author's byline) is Should-fix or, if it erases the writer's voice, Blocker.
