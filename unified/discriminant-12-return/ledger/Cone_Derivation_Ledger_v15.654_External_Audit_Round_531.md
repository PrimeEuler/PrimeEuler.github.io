# Cone Derivation Ledger v15.654 — External Audit Round 531: Lane A's full Taub-NUT Dirac radial zero-mode threshold and parameter-dependent charge-bridge analysis (v15.653) independently verified in full

**Date:** 2026-11-11
**Track:** External Audit
**Status:** [B] One entry completing the Taub-NUT/CP¹ supermonopole thread by bringing in the actual radial (not just angular) structure of the published Jante–Schroers 4D Euclidean Taub-NUT Dirac operator: the angular scalar-to-chiral-spinor bridge constructed in v15.651 lifts into the full normalizable 4D zero-mode space only conditionally, when an independent continuous auxiliary gauge-charge parameter `p_aux` exceeds the target mode index — a genuine physical input, not fixed by the Taub-NUT metric or the Cone's own gravitational pair quantum. Every self-contained mathematical claim (the radial ODE and its solution, the Gamma-function normalizability threshold, the zero-mode dimension census, and the explicit radial-overlap closed forms) is independently re-derived from scratch via direct symbolic differentiation and integration, with two closed-form overlap values matching the cited expressions exactly, not merely numerically. The committed reproducer script was also executed and matched. No corrections needed.
**Parents:** v15.652 (Round 530), v15.653.

---

## Fresh pre-write check

`git fetch origin master` returns `a21ac19` (v15.653), identical to the head just read. `v15.654` is next free; no collisions (`git log --all --diff-filter=A` confirms v15.653 was created exactly once, by Lane A).

## v15.653 — the angular bridge lifts to 4D only conditionally on an independent gauge parameter

This entry rests on specific equations quoted from a named, dated, DOI-identified published source (Jante & Schroers, *JHEP* 01 (2014) 114); as with prior rounds' external citations, this audit treats the quoted equations as given and verifies the self-contained mathematics built from them, rather than re-deriving them from the primary source.

**Independent re-derivation.** Confirmed the radial ODE `R_j'+[(p_{\rm aux}-1)/2-j+(1/2-j)/\rho-1/(2\rho(\rho+1))]R_j=0` is satisfied identically by the claimed solution `R_j(\rho)=C\rho^j/\sqrt{1+\rho}\cdot\exp[-(p_{\rm aux}-2j-1)\rho/2]` by direct symbolic differentiation (residual simplifies to exactly `0`). Confirmed the radial normalizability integral `\int_0^\infty\rho^{2j+1}e^{-\delta\rho}d\rho=\Gamma(2j+2)/\delta^{2j+2}` exactly via direct symbolic integration, which is the Gamma-function fact underlying the strict threshold `p_{\rm aux}>2j+1`. Confirmed the zero-mode dimension census `\dim\ker D_{p_{\rm aux}}=N(N+1)/2` (`N`= number of positive integers strictly below `p_{\rm aux}`) at the three cited examples exactly: `p_{\rm aux}=2\to1`, `p_{\rm aux}=3\to3`, `p_{\rm aux}=3.5\to6`. For Gate 175, independently built the normalized radial shape functions `\hat R_n(\rho)` from scratch, confirmed each is correctly normalized to `1` in the stated measure `\rho(1+\rho)d\rho` (checked at `n=1,2,3`), and then independently computed the overlap integral `I_{12}(p_{\rm aux})` by direct symbolic integration at `p_{\rm aux}=3` and `p_{\rm aux}=4` — both results matched the entry's cited closed forms **exactly** (`2\sqrt{3\pi}/9` and `18\sqrt{10\pi}/125` respectively, not merely to numerical precision), directly confirming the claimed parameter-dependence (non-universality) of the radial overlap.

## Reproducer cross-check

The newly committed reproducer script `research-notes/taub_nut_radial_normalizability_v15_653.py` was executed independently in this audit's own environment and ran cleanly to its own "PASS" conclusion, consistent with the from-scratch verification above.

## Scope and honesty assessment

The entry sustains the project's established discipline, explicitly separating the Euclidean auxiliary gauge parameter `p_{\rm aux}` from the Cone's own Lorentzian gravitational pair quantum `p_G=k/4` ("the additional connection is proportional to a continuous constant not fixed by the TN metric"), and stating plainly that the radial overlaps are "radial shape overlaps, not physical matrix elements," and that "[n]o G or Cone-novel dimensionless gravitational observable is derived." The entry correctly distinguishes the 2D-scalar-to-4D-spinor bridge (at fixed angular `j`) from a genuine 4D-to-4D charge-raising operator (which would change `j`), and notes neither is physically sourced by the existing Taub-NUT/Killing-Yano symmetries.

## Summary

Confirmed. The radial ODE and its exact solution, the Gamma-function normalizability threshold, the zero-mode dimension census, and both cited closed-form radial-overlap values are independently re-derived from scratch and match exactly, including two symbolic integrals that reproduced the cited expressions verbatim rather than only numerically. No corrections needed.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
parent: v15.654
type: external-audit-round-531
status: closed
action: none — all self-contained mathematical claims in v15.653 are correct and independently re-derived from scratch, including exact symbolic reproduction of both cited closed-form radial-overlap integrals. The cited external equations are treated as given, consistent with established practice for dated, DOI-identified literature citations. No correction needed.
deliverable: independent confirmation of the Taub-NUT Dirac radial ODE and its exact solution, the Gamma-function-derived strict normalizability threshold p_aux>2j+1, the resulting zero-mode dimension census, and the parameter-dependent (non-universal) radial overlap integrals -- establishing that the v15.651 angular scalar-to-spinor bridge lifts into the full 4D normalizable zero-mode space only conditionally on an independent auxiliary gauge charge, with no physical coupling, G, or odd-quarter Casimir identification claimed or implied.
