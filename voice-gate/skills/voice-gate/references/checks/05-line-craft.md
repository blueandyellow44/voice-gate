# Check 05 — line craft

Universal line-altitude craft check, drawn from the prose-critic craft sheet. Catches the line-
level failures that make competent prose read derivative: dead lines, over-explanation, abstraction
where concreteness is needed, monotone rhythm, filter words, cliché, and unintentional echo.

Proposes findings only. Renders no verdict. May propose zero findings.

## Reads from

- The measurement record (§4 surface-tell candidates, §5 rhythm samples, §7 echo scan).
- The supplied profile, if present: §Hard guardrails (mechanical line rules), §Preserve list (so
  a deliberate rhythm or repetition is not flagged as monotone or echo).

## Method, six dimensions

1. **Line aliveness.** Does each load-bearing line have a particular pressure, or is it inert and
   replaceable? Flag lines that are correct but dead.
2. **Over-explanation.** A clause that re-states what the previous clause or image already
   delivered. The most common fix is a cut, not an addition. This is the same pattern
   `01-surface-tells` calls "explanation after image"; when both fire on one quote, line-craft
   owns the row by dedupe precedence (line-craft outranks surface-tells), so claim it here.
3. **Concreteness vs abstraction.** Where the piece reaches for a feeling-word or an abstraction
   ("connection", "presence", "the weight of it") instead of the concrete thing that would carry
   it. Flag the abstraction; suggest the concrete swap direction.
4. **Filter words.** "felt / saw / noticed / realized / seemed / watched" placed between the
   reader and a perception. Flag where removing the filter sharpens the line; do not flag where
   the filter is doing real work.
5. **Rhythm.** From the rhythm samples, flag any run of four or more sentences of near-equal
   length that reads as monotone. Check the §Preserve list first: a deliberate cadence is not a
   defect.
6. **Cliché and echo.** Flag dead phrasing (cliché) and, from the echo scan, distinctive words or
   phrases repeated unintentionally. Separate unintentional echo from deliberate motif (a motif is
   placed and earns its return; an echo is the same word reached for twice by accident).

## Output

Proposed findings (scorecard rows): Check `Line: <dimension>` (e.g., `Line: over-explanation`,
`Line: abstraction`, `Line: filter word`, `Line: monotone rhythm`, `Line: echo`), Severity,
Evidence quote, Source rule (`checks/05-line-craft.md §<dimension>` or `profile §Hard guardrails`),
What's off, Suggested fix direction (smallest change). Plus a Protect list of lines already alive.

If nothing fails, report "no line-craft findings from this check."

## Hard rules

- Must be allowed to propose zero findings; must not declare the piece clean.
- Cut before add: the fix for over-explanation and a landed image is almost always a deletion,
  because adding words to a line that already works buries the thing that was working.
- Do not flatten a deliberate rhythm or a placed motif into "monotone" or "echo." Read the
  Preserve list first.
- Line-craft findings are usually Should-fix or Polish; reserve Blocker for a line that breaks the
  voice or a hard-guardrail violation.
