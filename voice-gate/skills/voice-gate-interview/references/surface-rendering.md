# Surface rendering — one interview, two deliveries

The interview content, the six-slot output, and the calibration gate are identical on every
surface. What changes is how the visualization reaches the writer. This file says how to choose and
what each path must do.

## The rule

- **In-chat visualization** on **Cowork, claude.ai chat, and the desktop app (Code)** — surfaces
  that render rich artifacts inline.
- **An HTML file** only for **terminal Claude Code** — a terminal cannot render inline, so the
  writer gets a file to open.

Pick by where this skill is running. When inline artifact rendering is available, render in chat.
When it is not (a terminal session), write the file. If you are unsure, write the file: an HTML
artifact opens everywhere and is never worse than a fallback. Also write the file, on any surface,
when the writer asks for one they can keep.

## Path A — in-chat visualization (Cowork / chat / desktop Code)

Render the interview as a live, inline visualization the writer works without leaving the
conversation:

- One slot at a time, in the order in `interview-script.md`, with a visible progress indicator
  (step N of 6).
- The questions for the current slot, with inputs appropriate to it: free-text lines, and for §4
  Native pressures the nine-pressure picker (danger, desire, secret, shame, contradiction, decision,
  dread, curiosity, longing) as selectable options.
- A **live profile preview** that fills in as the writer answers, so they see the six slots taking
  shape and can correct in place.
- A paste/upload affordance for optional samples (Step 3 grounding).
- On completion, the filled profile and the calibration stub are produced into the conversation and
  written to files per Steps 5-6.

The point of Path A is that the writer never leaves the chat. Keep the visualization legible on the
surface in use; do not block the interview on a widget feature a given surface lacks — degrade to
plain numbered questions in chat before you degrade the writer's experience.

## Path B — HTML file (terminal Claude Code)

Write `templates/kickoff.html` to a sensible location (default: the writer's working folder, or a
path they name) and hand back the path to open in a browser. The artifact carries the whole
interview itself:

- The six slots as a stepper, the nine-pressure picker for §4, a paste box and a file input for
  optional samples, and a live profile preview pane.
- Two export buttons: download the filled `voice-gate-profile.md` and the calibration stub. The
  writer fills the form in the browser, exports, and hands the files back for grounding (Step 3) and
  the calibration gate (Step 6).

**The HTML artifact must be offline-safe: zero external network references** — no CDN scripts, no web
fonts, no remote images, no analytics. Everything inline. This is what lets it open on any machine
and leak nothing. Verify it before handing it over: search the file for `http://`, `https://`, and
`//` resource references and confirm there are none that fetch over the network.

## What both paths share

- The same questions and the same order.
- The same six-slot contract output and the same `self-reported (unverified)` / `sample-grounded`
  basis marking per slot.
- The same hand-off to the human-graded calibration gate. Neither path self-grades, and neither
  path is a shortcut around the gate.
