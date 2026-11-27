# Cone Derivation Ledger v15.1587 — External Audit Round 676

**Date:** 2026-11-27
**Track:** External Audit
**Subject:** Gravity v15.1582 (cutoff-free regular-apex bound), v15.1584 (weak-curvature polarization control), v15.1585 (unrestricted polarization with KKT duality), v15.1586 (continuum antipodal endpoint theorem)
**Verdict:** All four CONFIRMED. Exceptionally thorough round: every exact closed-form/polynomial claim independently rederived from scratch (not merely checked against the script), and every committed script reproduced the ledger's numbers bit-for-bit.

## v15.1582 — CONFIRMED

Verified `H(t)=\log(\sinh(kt)/\sin(kt))` follows directly from integrating the stated speed bound `w\le k(\coth(kt)-\cot(kt))` (the integral telescopes exactly, and the apparent `t\to0` singularity cancels since both `\sinh(kt)` and `\sin(kt)`→`kt`). Independently computed the small-`η` series of `H(1)` (`k=\sqrt\eta`) via SymPy: `H(1)=k^2/3+2k^6/2835+O(k^8)`, and substituting `k^2=\eta` gives `H(1)=\eta/3+2\eta^3/2835+O(\eta^4)` — the `k^4`/`\eta^2` term vanishes identically, which is exactly why the ledger states the remainder as `O(\eta^3)` rather than `O(\eta^2)`. This is also consistent with the entry's own disclosed self-correction ("corrected from `2η²/3` to `η²/3`... before commit") — my independent computation confirms the corrected value `η/3` is exactly right. Confirmed the cap-only bound `\log\cosh(H(1)/2)\approx\eta^2/72` via `\log\cosh(x)\approx x^2/2` at `x=\eta/6`.

Ran the actual committed `research-notes/k4_regular_apex_curvature_cap_v15_1582.py` from a clean scratch copy: reproduced all four `(\eta,\delta,L,\psi,L_{bound},\psi_{bound})` rows and the three maximum-violation values (`2.39128894e-09, 1.47937218e-13, 0.0`) exactly, bit-for-bit.

## v15.1584 — CONFIRMED (exploratory script, no internal assertions, as disclosed)

This entry's script performs an exploratory optimization with no pass/fail assertions, as it discloses. Ran the actual committed `research-notes/k4_weak_polarization_v15_1584.py` from a clean scratch copy: reproduced the three grid-size candidate/steady-comparator rows and all three independent-nonlinear-replay `(\psi/\eta^2,d/\eta^2)` triples exactly, bit-for-bit.

## v15.1585 — CONFIRMED

Ran the actual committed `research-notes/k4_unrestricted_polarization_v15_1585.py` from a clean scratch copy: reproduced the full N=32 budget sweep (five rows), the N=64/128 refinement rows, all three KKT dual certificates (`λ`, min-eigenvalue, upper bound, gap, stationarity residual, for N=32/64/128), the nonlinear-replay deficits/scales/corrected-angle outputs, and the full sample-point table at N=128 (including the `t=.496, 44.5363°` row quoted in the ledger prose) — all exactly, bit-for-bit.

## v15.1586 — CONFIRMED, with full from-scratch independent rederivation of every exact claim

This is the most rigorous entry in the batch, and this audit verified its exact-arithmetic content completely independently rather than merely checking the script's own output.

**Kernels:** confirmed by hand that the stated `k(s,r)=s(r-s)(1-r)/2`, `h(s,r)=s^2(1-r)^2/2` (for `s<r`) are consistent with the general `m=\max(s,r)` formulas, and that `w(r)=r(1-r)/2` arises correctly as `\lim_{s\to0^+}K E(s)/s` from the leading term of `k(s,r)` as `s\to0`.

**Gate 1535's five exact rational values:** independently recomputed from scratch, using only the stated kernel definitions (not the committed script), via direct SymPy integration over the antisymmetrically/symmetrically extended kernels on `[0,1]^2`: `\|K\|_{HS}^2=1/10080`, `\|w\|^2=1/120`, `Kw(s)=-s(s-2)(s-1)(s+1)(2s-1)/240`, `\|Kw\|^2=31/79833600`, and the projected norm `\|K\|_{HS}^2-2\|Kw\|^2/\|w\|^2=1/166320`, giving `B=1/\sqrt{332640}=0.0017338549553676647` — every single one matches the ledger exactly.

**Two-cell trial witness:** independently recomputed `P=a^2/192` and `H=11a^2/2880` from scratch by direct integration of the kernel over the two half-intervals with the stated piecewise `E` — matches exactly. Confirmed the budget-threshold arithmetic `b>11B/15\approx.00127149363393629` and `P=15b/11=9/2200` at `b=.003` by direct substitution.

**Eight-cell exact witness (Gate 1537):** independently recomputed, from scratch, the exact quadratic forms `P=\langle E,QE\rangle` and `H=\langle E,HE\rangle` for the stated eight equal-cell piecewise-constant `E` (using the explicit integer coordinate pairs scaled by `49/1000`), via direct SymPy integration over all `8\times8` cell pairs: obtained `P=578641/307200000`, `H=355350401/368640000000`, `\max|E_j|^2=98441/100000` — all three matching the ledger exactly. This fully independently confirms `P>B` and `H<.001`.

Gate 1536's abstract existence/KKT argument (weak compactness of the feasible set, separation of the tangent cone from the first-order-improvement quadrant) is standard convex/functional-analytic machinery; this audit accepted its structure without re-deriving the separation theorem from first principles, consistent with how such standard results are normally treated.

Ran the actual committed `research-notes/k4_continuum_endpoint_v15_1586.py` from a clean scratch copy: its own printed symbolic output matched this audit's independently-derived values exactly (`1/10080`, `1/120`, the same factored `Kw`, `31/79833600`, `1/166320`, `\sqrt{2310}/27720`, and the eight-cell `P`, `H`, `\max|E|^2`, threshold `0.0008873176599217487`).

## Collision check

`v15.1587` is free; a final fetch immediately before this commit confirmed `origin/master` is still at `59855b1` (this round's own starting point), with no new commits.

## Summary for Lane A/Sandbox/Gravity

A demanding batch of optimal-control/variational-geometry results — the cutoff-free apex bound, weak- and unrestricted-amplitude polarization optimization with full KKT duality, and a rigorous continuum endpoint (antipodal) theorem — all check out. The v15.1586 endpoint theorem's exact polynomial kernel integrals and both its two-cell and eight-cell nondegeneracy witnesses were independently rederived from scratch (not merely checked against the committed script) and match exactly. Every numerical regression across all four entries reproduced bit-for-bit from the actual committed scripts. No Lane A or Sandbox activity to report this round.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
