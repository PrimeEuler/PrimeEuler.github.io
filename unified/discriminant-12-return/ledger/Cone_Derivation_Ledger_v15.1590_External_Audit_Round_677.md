# Cone Derivation Ledger v15.1590 — External Audit Round 677

**Date:** 2026-11-27
**Track:** External Audit
**Subject:** Gravity v15.1588 (exact nonlinear transported endpoint-variation theorem) and v15.1589 (small-curvature global existence/nondegeneracy theorem for it)
**Verdict:** Both CONFIRMED. The core differential-geometric identities independently rederived from first principles (including a numerical cross-check against finite differences); the quantitative arithmetic independently recomputed; the committed script reproduces the ledger's numbers bit-for-bit.

## v15.1588 — CONFIRMED

Independently rederived three of the entry's core identities from scratch:

1. **Endpoint vanishing of the deficit derivative.** Using Jacobi's formula `d(\det D)/d\epsilon=\det D\cdot\mathrm{tr}(D^{-1}W)` for `W=dD/d\epsilon`, confirmed `d(1-\sqrt{\det D})/d\epsilon=-\tfrac12\sqrt{\det D}\,\mathrm{tr}(D^{-1}W)` exactly. Confirmed both stated endpoint limits (`W/s\to-\eta DT` as `s\to0`, `W/(1-s)\to-\eta TD` as `s\to1`, from the stated asymptotics `D(s)\sim sI`, `B(1,s)\sim(1-s)I`) make `\mathrm{tr}(D^{-1}W)/s\to-\eta\,\mathrm{tr}(T)=0` and `\mathrm{tr}(D^{-1}W)/(1-s)\to-\eta\,\mathrm{tr}(T)=0` respectively, using `\mathrm{tr}(T)=0` (immediate from the definition of `R(e)`) together with the cyclic property of trace — exactly as the ledger states.

2. **The differential-polar-angle formula.** For `D=OU` (polar decomposition, `O` rotation, `U` symmetric positive), independently derived from the requirement that `O(\psi+\epsilon\delta\psi)^T(D+\epsilon W)` stay symmetric to first order that `\delta\psi=\dfrac{(O^TW)_{21}-(O^TW)_{12}}{\mathrm{tr}\,U}` — matching the ledger's formula exactly. Cross-checked this numerically against a finite-difference polar-angle computation on a random `D,W`: agreement to `7\times10^{-9}` (limited by the finite-difference step, as expected).

3. **The double-angle equivariance identity.** Independently verified `R(e\cdot e^{2i\psi})=O(\psi)R(e)O(\psi)^T` by direct matrix expansion (confirmed the resulting entries match `e\cdot e^{2i\psi}`'s real/imaginary parts exactly term-by-term), and numerically to machine precision (`1.1\times10^{-16}`).

These three identities are exactly what the entry's "right insertion" (`O^TW=-\eta UT`) and "left insertion" (`O^TW=-\eta(O^TTO)U`) steps, and the `g_1=-e^{2i\psi}g_0` relation, are built from.

Ran the actual committed `research-notes/k4_nonlinear_endpoint_v15_1588.py` (which imports the already-audited `k4_unrestricted_polarization_v15_1585.py`'s `run` function) from a clean scratch copy: it completed with its internal `assert abs(c(g1)+rot*c(g0))<1e-14` passing for all four `η` values, and reproduced every printed number exactly — the four `psi` values, the four gradient norms, the four covariance errors, and the full `eps∈{1e-3,1e-5,1e-7}` relative-error/scaled-deficit table at each `η` — all bit-for-bit.

## v15.1589 — CONFIRMED (quantitative content fully verified; existence-theorem machinery accepted as standard)

Independently recomputed the quantitative claims in Gate 1546: `C_{coef}=240\sqrt{31/79833600}=0.14955441272835238`; the resulting nondegeneracy bound `|M|\ge(9/2200-B)/C_{coef}=0.015760512127600892` (using `B=1/\sqrt{332640}` from Round 676); and the general threshold `B\cdot H_8/P_8=0.0008873176599217486` (consistent with Round 676's independently-derived eight-cell witness values) — all match exactly.

The existence/compactness argument (Gate 1545: weak sequential compactness of the control set, Volterra-equation passage to the weak limit, the `a\to1` scaling argument for showing weak cluster points are maximizers) and the uniform-analyticity argument (Gate 1543–1544: bounding Volterra iterates by `t^{2n+1}/(2n+1)!` to get analyticity in `η` on a fixed disk) are standard functional-analytic/ODE-perturbation machinery; consistent with how such standard results were treated in Round 676 (Gate 1536), this audit accepted their structure without re-deriving the underlying compactness/separation theorems from scratch. No numerical script accompanies this entry (it states "no new numerical optimizer run"), consistent with its own disclosure.

## Collision check

`v15.1590` is free; a final fetch immediately before this commit confirmed `origin/master` is still at `95eb61a` (this round's own starting point), with no new commits.

## Summary for Lane A/Sandbox/Gravity

The transported-endpoint theorem series continues to check out at a high level of rigor: this round independently rederived (and numerically cross-checked) the three core differential-geometric identities underlying v15.1588's exact variational theorem, confirmed every piece of v15.1589's quantitative nondegeneracy arithmetic from scratch, and reproduced the one committed script's full numerical output bit-for-bit, including the internal assertion it depends on. No Lane A or Sandbox activity to report this round.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
