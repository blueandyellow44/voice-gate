# Check 01 — surface tells (AI-polish / surface flattening)

Universal method, stripped from `max-humanizer-surface-pass`. Catches prose that is grammatically
clean but reads as if anyone could have written it. This is a surface-register check, not a
structural one.

Proposes findings only. Renders no verdict. May propose zero findings.

## Reads from

- The measurement record (§4 surface-tell candidates, §6 guardrail scan).
- The supplied profile, if present: §Hard guardrails, §Known surface tells.

## Method

1. Read the piece once for what is alive and particular before hunting for problems. The default
   posture is protective.
2. Judge each surface-tell candidate from the measurement record. The universal tells:
   - **Generic warmth** — warm language attached to no specific referent.
   - **Inflated significance** — a clause telling the reader why a detail matters after the
     detail already did the work.
   - **Motivational cadence** — TED-closer or newsletter-signoff rhythm; paragraphs building
     toward a lesson aimed at the reader.
   - **Rule-of-three smoothness** — three balanced items satisfying because symmetrical, not
     because true. The third item especially.
   - **Beautiful-but-anyone line** — correct, even nice, but no particular person had to write it.
   - **Explanation after image** — the clause naming the feeling the image already gave.
   - **Overly clean final wisdom** — a closing sentence arriving as packaged truth rather than
     the thing itself.
   - **Stacked X-not-Y kicker** — repeated "not X, but Y" as a structural punchline.
   - **Aphoristic paragraph structure** — several paragraphs each closing on a stand-alone
     mini-wisdom.
3. **Hard-guardrail violations (if a profile is supplied).** Every violation recorded in
   measurement §6 is a finding here, severity **Blocker** by default (em dash where banned,
   contraction where banned, wrong sign-off form, banned construction). These are the most
   objective findings the gate makes. Source rule: `profile §Hard guardrails`.
4. For each flag: quote the exact line, name the tell, state the flattening risk in one sentence,
   give a smallest-change direction (not a rewrite).
5. Note what to preserve: lines already alive and particular.

## Output

Proposed findings (scorecard rows) + a Protect list. For each: Check `Surface: <tell>` (or
`Surface: guardrail violation`), Severity, Evidence quote, Source rule (`checks/01-surface-tells.md
§<tell>` or `profile §Hard guardrails`), What's off, Suggested fix direction.

If no tells are present, report "no surface findings from this check." Do not call the piece clean.

## Hard rules

- Must be allowed to propose zero findings; must not declare the piece clean or ready.
- Must not sand clean prose further.
- Must not apply a generic 24-pattern humanizer checklist. Judge the named tells above.
- "Human" does not mean messier, louder, more emotional, or more casual. It means particular.
- A surface tell on its own is rarely a Blocker; a hard-guardrail violation usually is. Do not
  inflate a polish-level tell to Blocker.
