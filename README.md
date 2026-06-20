# Voice Gate

Standalone, distributable home of the **`voice-gate`** Claude plugin: a single-voice writing
instrument that checks finished medium-form nonfiction against a supplied voice profile and
universal craft, and renders one scorecard. Diagnose-only; it never rewrites.

This repo is the canonical home of the plugin. It is intentionally free of any one writer's
private voice canon, corpus, or interior dossier.

## Layout

- `voice-gate/` — the plugin (`.claude-plugin/plugin.json`, two skills, README, SHARE-NOTE).
  - `skills/voice-gate/` — the diagnose-only runtime.
  - `skills/voice-gate-builder/` — generates a writer's supplied profile from their own corpus,
    proven through a human-graded calibration gate it never self-grades.
- `automation/package_voice_gate.py` — re-runnable preflight + packager (validates the plugin
  against the claude.ai desktop-uploader limits, scans for private leakage, builds the dist zip).
- `dist/` — built zip artifacts (gitignored; regenerate with the packager).

## Use

Start at `voice-gate/README.md`, then `voice-gate/SHARE-NOTE.md` for the share/install note.

Build or re-validate the distributable:

```sh
python3 automation/package_voice_gate.py        # preflight + build dist/voice-gate-<version>.zip
python3 automation/package_voice_gate.py --check-only   # preflight only
```
