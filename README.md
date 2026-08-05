# Voice Gate

A diagnostic that checks whether a draft actually sounds like the person it is supposed to sound like.

## What it does

Most writing tools rewrite. This one refuses to. Voice Gate reads a finished piece of medium-form nonfiction against a supplied voice profile, renders one locked scorecard, and gives one verdict. It diagnoses and stops there, because a tool that both judges and edits will quietly grade its own work.

The problem it was built for is narrow. A draft can pass every rule you can name, no em dashes, no filler, no corporate hedging, and still not sound like the writer. What gives it away is register-flattening, where every sentence arrives at the same even altitude and the writing stops fitting the person and the moment. Rule checkers cannot see that. The gate is built to.

## What is inside

Four skills, in the order you would use them.

| Skill | What it does |
| --- | --- |
| `voice-gate-builder` | Generates a voice profile from a writer's own corpus |
| `voice-gate-interview` | Builds the same profile by consent-first interview, when there is no corpus |
| `voice-gate` | The diagnose-only runtime. Scorecard and verdict, no edits |
| `voice-gate-reviser` | Applies approved findings as the smallest in-voice change |

Both profile builders prove their output through a human-graded calibration gate that they never grade themselves. That separation is the whole design. A profile that certified itself would be worth nothing.

Four subagents back the skills, in `voice-gate/agents/`.

## How it works

The gate runs eight checks in a fixed order, from surface tells through narrator cleanliness, propulsion, figurative language, line craft, originality, and preservation. `voice-gate/skills/voice-gate/references/checks/` holds one file per check. The scorecard shape and the profile contract are both pinned in that same references directory, so a run cannot drift into inventing its own rubric.

The profile itself is supplied, never assumed. `voice-profile-contract.md` defines what the gate requires from it.

## Install

```sh
python3 automation/package_voice_gate.py        # preflight, then build dist/voice-gate-<version>.zip
python3 automation/package_voice_gate.py --check-only
```

The packager validates the plugin against the claude.ai desktop uploader limits and scans for private leakage before it will build. Start at `voice-gate/README.md`, then `voice-gate/SHARE-NOTE.md`.

## Status

Version 0.5.0, working. Deliberately free of any one writer's private voice canon, corpus, or interior dossier, and the packager enforces that rather than trusting it.

## License

MIT
