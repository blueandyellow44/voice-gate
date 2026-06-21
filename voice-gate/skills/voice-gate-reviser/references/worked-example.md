# Worked example — scorecard to revision

A calibrated model of one reviser run. Synthetic writer, synthetic piece, nothing private. It shows
two approved findings applied as smallest in-voice changes, one preserved line left untouched beside
a fix, and the re-run-the-gate handoff.

## The inputs

**Writer (from the supplied profile, abbreviated):** a plain operator-voice newsletter writer.
§Hard guardrails: em dashes are **native and protected**; no exclamation points. §Figurative
signature: near-zero, concrete hand-tool images only. §Preserve list: dry parenthetical asides;
short plain sentences after long ones.

**Piece (excerpt):**

> We rebuilt onboarding this quarter. The first version asked for everything up front, which is the
> kind of mistake you only make once. Onboarding, at the end of the day, is the foundation upon
> which every customer relationship is built. The new flow asks for three things, and you can skip
> two of them (most people do). It felt good to ship.

**Gate scorecard (operator-approved targets):**

| Check | Status | Severity | Evidence quote | Source rule | What's off |
|-------|--------|----------|----------------|-------------|------------|
| Surface: inflated significance | Flag | Blocker | "Onboarding, at the end of the day, is the foundation upon which every customer relationship is built." | `checks/01-surface-tells.md §Inflated significance` | A wisdom-button generality in a piece that is otherwise concrete and plain. Does not sound like the writer. |
| Line: over-explanation | Flag | Polish | "It felt good to ship." | `checks/05-line-craft.md §Over-explanation` | Names the feeling the concrete detail already carried. |

**Protect list (from the scorecard + profile):** the dry aside "(most people do)"; the native em
dash construction.

Operator approved both rows. No em dash row was flagged (native, protected).

## The run

**B. Name what not to touch first.** Protect: "(most people do)" stays verbatim. Native em dashes
stay. The fix to the inflated-significance sentence sits two sentences before the aside; the aside
is not adjacent to either flagged span, so there is no adjacency conflict, but it is named so it is
seen to survive.

**C and D. Fix one span at a time, smallest change, checked against the governor.**

Finding 1 (Blocker, inflated significance). Smallest change that clears the rule: cut the
wisdom-button sentence. It adds no concrete information; the surrounding sentences already carry the
point. A recast would manufacture a generality the writer does not make.

- Before: `Onboarding, at the end of the day, is the foundation upon which every customer relationship is built.`
- After: (cut)
- Applied: `01-surface-tells.md §Inflated significance`. Removed the generality; the concrete
  before/after sentences now sit together.

Finding 2 (Polish, over-explanation). Smallest change: cut the naming-the-feeling sentence. The
detail "you can skip two of them (most people do)" already carries the satisfaction; stating it
flattens it.

- Before: `It felt good to ship.`
- After: (cut)
- Applied: `05-line-craft.md §Over-explanation`. The aside "(most people do)" is preserved
  unchanged.

**Untouched-but-adjacent:** "(most people do)" preserved verbatim. The em dash construction
elsewhere in the piece was not touched (native, protected).

**E. Handoff.** Changed spans returned above. No verdict rendered. Re-run `voice-gate` on the
revised piece to verify the Blocker is cleared and nothing protected was damaged.

## The revised excerpt (for reference, not the deliverable)

The deliverable is the before/after spans above. For context, the excerpt now reads:

> We rebuilt onboarding this quarter. The first version asked for everything up front, which is the
> kind of mistake you only make once. The new flow asks for three things, and you can skip two of
> them (most people do).

Two cuts, nothing added, the aside intact, the voice unflattened. The gate decides whether it is
ready; the reviser does not.
