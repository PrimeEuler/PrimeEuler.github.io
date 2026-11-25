# Cone Derivation Ledger v15.1423 — External Audit Round 638

**Date:** 2026-11-25
**Track:** External Audit
**Subject:** v15.1419 (collision renumbering), v15.1420 (full 4D Weyl local characteristic), v15.1421 (3D Weyl vanishing, higher-derivative warning), v15.1422 (time-dependent tidal external-work identity)
**Verdict:** All four entries CONFIRMED. All three new committed scripts run exactly as committed and reproduce every quoted number exactly. All analytically tractable claims independently verified by hand, including a full matrix-calculus re-derivation of Gate 1366's external-work identity.

## v15.1419 — v15.1403 collision renumbering: CONFIRMED correct

Content, SHAs, and gate numbering are preserved verbatim from the original v15.1403 (already independently verified in Round 636); only the renumbering note is added, and the superseded file is left archived rather than edited. Closed.

## v15.1420 — full 4D Weyl local characteristic: CONFIRMED

Independently re-derived the three quoted Weyl components from the standard linearized-Riemann formula for the TT wave `h_xx=\varepsilon\cos(t-z), h_yy=-\varepsilon\cos(t-z)`, evaluated at phase `\cos(t-z)=1`: `C^{0y0y}=f''(0)/2` with `f(u)=\varepsilon\cos u` giving `f''(0)=-\varepsilon`, so the coefficient is `-1/2` — matches exactly. For `C^{0yxy}` and `C^{xyxy}`, every term in the linearized-Riemann sum vanishes because the perturbation has no `y`- or `x`-dependence and no `0y`/`01` components — both are exactly zero, matching the ledger. The dispersion/characteristic-speed numbers (`z=.01,.10,.25`) reduce to the identical `c_\pm=1/\sqrt{1\pm z}` formula already confirmed in Round 637 (v15.1417); computed by hand, `z=.01` gives speeds `0.995037190`, `1.005037815` — matching the new row exactly, including the claimed "~0.5% excess" at this smallest coupling. Ran `k4_full_weyl_local_characteristics_v15_1420.py` exactly as committed: all three `(z, speeds)` rows, the three Weyl components, and the polarization-mixing kernel `M^\nu=[0,0,-\omega^2/2,0]` match the ledger exactly.

## v15.1421 — 3D Weyl vanishing and higher-derivative warning: CONFIRMED

The `n=3` Weyl-vanishing identity is a standard fact of the Ricci decomposition (`C_{ijkl}=0` identically for `n=3`, since the `P_{ij}=\mathrm{Ric}_{ij}-(R/4)g_{ij}` decomposition exhausts the full Riemann tensor with no independent Weyl piece) — the stated coefficient `R/4` matches the general-`n` formula at `n=3` exactly. Independently re-derived the representative Euler–Lagrange example by hand: for `L=\lambda h''(t)A'(t)B(t)`, varying `h` (which enters only through `h''`) gives `E_h=\frac{d^2}{dt^2}(\lambda A'B)=\lambda(A'B)''`, and varying `A` (entering only through `A'`) gives `E_A=-\frac{d}{dt}(\lambda h''B)=-\lambda(h''B)'` — both match exactly, confirming the claimed third-derivative structure. Ran `k4_weyl_dimension_metric_variation_v15_1421.py` exactly as committed: both PASS lines print, exit code 0.

## v15.1422 — time-dependent tidal external-work identity: CONFIRMED

Independently re-derived Gate 1366's central identity `dH/dt=-g\dot c(t)\dot A\dot u` from scratch via matrix calculus: with `H=\frac12 p^TM(t)^{-1}p+\frac12(A^2+u^2)`, `\partial H/\partial t=\frac12 p^T\frac{\partial M^{-1}}{\partial t}p`, using `\frac{\partial M^{-1}}{\partial t}=-M^{-1}\dot M M^{-1}` and `\dot M=g\dot c\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}`, and substituting `q=M^{-1}p=(\dot A,\dot u)` gives `\partial H/\partial t=-\frac12 q^T(g\dot c\sigma_x)q=-g\dot c\,\dot A\dot u` exactly — matching the ledger precisely. Ran `k4_prescribed_weyl_external_work_v15_1422.py` exactly as committed: both table rows (`g=.08` and `g=0`) match exactly, including `initial_energy`, `final_energy`, `energy_change`, `external_work`, and the `~2.7\times10^{-15}` work-identity residual.

## Collision check

No filename or version-number collisions: `v15.1423` was free immediately before this write (confirmed via fresh `git fetch origin master`, HEAD still `5736a22`).

## Summary for Lane A/Sandbox/Gravity

A clean, well-disciplined continuation of the Weyl-EFT completeness program. v15.1420 shows the full 4D Weyl tensor (not just a frozen component) reproduces the same characteristic-speed anomaly found in the earlier truncated model — correctly scoped as a fixed-background local result, not a claim of physical superluminal signaling. v15.1421 correctly identifies that a strictly 2+1-dimensional theory cannot host this operator at all (Weyl vanishes identically in 3D) and flags a genuine higher-derivative structural concern in the full metric variation, again carefully scoped as a warning rather than a proof of pathology. v15.1422 closes a real gap: a prescribed time-varying tidal background does work on the matter sector, so the matter-only energy conservation shown in v15.1416 was correctly scoped to the constant-coefficient case and does not extend to a realistic time-dependent tide without including gravitational degrees of freedom. All three new scripts ran clean with no bugs, and the project's standing novelty-verdict discipline continues to be applied honestly throughout.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
