# Cone Derivation Ledger v14.734 — Sandbox: Taub–NUT Hamilton–Jacobi equation derived directly from the inverse metric — R338's loose end closed

**Date:** 2026-10-22 EDT. **Lane:** sandbox (our Lane B). **Parents:** v14.731 (the dyon-pair deposit), v14.732 (Audit R338).
**Directive:** Jeremy, 2026-10-22 — "Ledger the HJ closure for Audit" (his tap on the offered option, after R338 reported one unresolved check).
**Collision check:** live HEAD checked via commits API immediately before drafting: max ledger version v14.733 (Audit liveness); v14.734 free.
**Deposit:** `research-notes/payloads/sandbox_tn_hj_closure_v14_734/tn_hj_from_metric.py` (producer; sympy, runs in ~2 s).

## The loose end

R338 (v14.732) verified every independently checkable identity in v14.731 — the forced Killing sign and triad uniqueness from from-scratch code, the charge identities symbolically and at 200 numeric points, the MIC separation, the TN−MIC radial difference, and γ_max by an independent two-line derivation. One intermediate check the auditor could not cleanly close on a first pass, and reported honestly as unresolved on their side: deriving the raw Taub–NUT Hamilton–Jacobi equation quoted at the top of `tn_sector.py` directly from the metric's inverse, rather than from the charge route.

## Closure [D, exact symbolic]

Build the Taub–NUT metric with f(r) arbitrary, invert it symbolically, and form the HJ expression g^μν p_μ p_ν with p = (−ε, p_r, p_θ, k). Then, with Σ = r² + l²:

  Σ·(g^μν p_μ p_ν + 1) − [ Σf p_r² + p_θ² + (k + 2εl cosθ)²/sin²θ − Σ(ε²/f − 1) ] = 0

exactly (sympy residual zero; producer prints it). So the quoted equation,

  Σf p_r² + p_θ² + (k + 2εl cosθ)²/sin²θ = Σ(ε²/f − 1),

follows directly from the inverse metric — no charge-based detour needed — and `tn_sector.py`'s starting point is confirmed from the metric itself.

Why a first pass misses it: the (t, φ) block determinant is −Σf sin²θ, so g^tt = (−4l²f cos²θ + Σ sin²θ)/(−Σf sin²θ) splits into two pieces that go to different places — the Σ sin²θ piece supplies the −Σε²/f on the right-hand side, while the 4l²f cos²θ piece joins the g^tφ cross term and the g^φφ term to complete the square (k + 2εl cosθ)². Drop or mis-sign either piece and no proportionality match appears; with both, it is an identity. This is consistent with R338's own assessment (a normalisation/convention mismatch on the auditor's side, not a defect in the deposit); the deposit's equation stands as quoted.

**Flags:** `R338_loose_end=CLOSED_from_metric_inverse_exact`; `v14.731_equations=UNCHANGED`; `G_derived=false`; `far_tail_touched=false`; `papers_modified=false`.
