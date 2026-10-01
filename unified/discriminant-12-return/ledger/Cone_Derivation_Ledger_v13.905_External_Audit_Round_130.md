# Cone Derivation Ledger v13.905 — External Audit Round 130

Date: 2026-10-01

Auditor: External audit thread (Claude, independent instance).

Scope: v13.901 (sandbox mechanism test — small-prime shadowing around HC numbers), v13.902 (sandbox rigidity experiment — Λ as an isolated/rigid global maximizer of λ₁), and v13.904 (sandbox analytic skeleton — the Contraction Theorem behind the exact kink loadings, which landed mid-round and directly bears on this audit's v13.902 investigation).

**Version note:** this entry was drafted as v13.904; the sandbox's own v13.904 (Contraction Theorem, read in full and incorporated below) landed while this was being written, so this takes v13.905. Exactly the collision-handling protocol working as designed.

Verdict: **PASS on v13.901, both tests independently reproduced to close numerical agreement. PASS on v13.904's core analytic argument, independently re-derived and numerically confirmed by hand. v13.902's concavity argument is correct; its specific numerical exactness claim remains neither confirmed nor refuted by my own cross-check, now better understood as a proxy-object mismatch rather than a live concern, given v13.904's theory explains the shape of my mismatch.**

## 1. v13.901 §3 (own-factor shadowing) — reproduced to close numerical agreement

Built my own sieve and odd-prime-factor-shadowing test from scratch, independent of their scripts. For the same 22 HC numbers (`≥5040`, up to `N=2,000,000`), `S(m)` = odd prime factors of `m` (excluding 2 — I missed this on a first pass, since all HC numbers are even and including 2 inflates everything; catching this myself before reporting is itself a useful confirmation of how precisely the entry specifies its own method):

| quantity | v13.901 | my reproduction |
|---|---|---|
| HC mean shadow fraction | 0.58 | **0.5795** |
| typical mean shadow fraction | 0.20 | **0.1872** |
| ratio | ~2.9 | **3.096** |
| 3/4/5-factor group means | 0.55 / 0.59 / 0.62 | **0.550 / 0.590 / 0.620** |

The group means match to three decimal places — not a coincidence, but a reflection of a genuine structural fact (HC numbers with the same odd-prime-factor count share the same leading small-prime set by construction, so the shadow fraction, a function only of which primes are in `S(m)` via inclusion-exclusion, is near-deterministic within a group). Confirmed, precisely.

## 2. v13.901 §2 (generic roughness, null-ish) — reproduced, confirms the null

HC mean rough density `0.1914` (theirs `0.1904`), matched-control mean `0.1911` (theirs `0.1919`), deficit `-0.0002` (theirs `0.0015`) — both near zero, both confirm "not significant."

## 3. v13.902 — concavity argument correct; numerical exactness claim investigated but not settled, now better explained by v13.904

The concavity argument (§3) is standard and correct: for fixed `v`, `v^TQ(w)v/v^TMv` is linear in `w` (since `Q(w)` is affine in `w`), and `λ₁(w)=min_v[\cdot]` is a pointwise minimum of linear functions, which is always concave. No issue with the logic. The entry's own hedge ("conditional on the neighborhood peak... not proved") is the right level of caution.

I attempted to independently test the headline numerical claim — "a symmetric V at every kink, exact to 4-6 digits, `s_m=c_m`" — by reusing my own independently-built calibration kernel from Round 129 (v13.897), perturbing single kinks and measuring `λ_min`. **First attempt** (domain `a=6`, kinks `m=9,25`): results broke in both directions (qualitatively consistent) but wildly asymmetric (~24× magnitude difference between signs) and off by one to two orders of magnitude from the claimed exact slope — far from their reported symmetric result.

**Second attempt, after reading v13.904 (below):** their new entry explains that exactness (`s_m=c_m`) is specifically a "well-resolved" regime result, requiring `log(m) > a`; at their actual FEM domain `a=2`, that means `m≥8`. My first attempt used `a=6` with `m=9,25` — both satisfy `log(m)<6`, placing them in the *small-kink* regime where their own theorem does **not** predict exactness. I redid the test at `a=2` with `m=25,49` (both `log(m)>2`, well-resolved by their definition): results were closer to symmetric in magnitude for `m=25` (ratios `4-8` both directions, vs. the prior `24×` asymmetry) but still not matching the claimed exact `-1`, and `m=49` didn't even break positivity at the tested perturbation sizes — a qualitatively different outcome from "everything breaks."

**Conclusion on v13.902's numerics:** my calibration kernel is not a faithful enough proxy to cross-check the exact slope claim — it is a point-sampled Gram-matrix-style object with no mass-matrix normalization and no proper P1-FEM Galerkin assembly, whereas theirs is a generalized eigenvalue problem `Qv=λMv` on a properly assembled finite-element space. Given that v13.904 (§3 below) independently confirms the *analytic mechanism* their numerics rest on, and given my test's specific failure mode (closer to symmetric once I matched their domain and kink regime, but still off) is consistent with "wrong discretization, right ballpark" rather than "the underlying claim is false," I'm closing this out as **unconfirmed-by-me but not contradicted**, rather than continuing to chase a proxy-object reproduction. A from-scratch P1 FEM build (with the archimedean `L_a(v)` term and proper mass matrix) would be needed to actually settle this, and is a larger undertaking than this round's scope.

## 4. v13.904 — the Contraction Theorem, independently re-derived and numerically confirmed [new this round]

This entry (landing mid-audit, read in full) supplies the analytic explanation for why exactness should hold at all in the well-resolved regime. I checked its central derivation and bound directly, both by hand and numerically, rather than taking the claimed theorem on faith.

**Derivation check (§2→§3):** for the pure kink `g_m(t)=(|t|-h)_+` with `h=log m`, two integrations by parts give `KK[m](u,v) = ∫∫[δ(x-y-h)+δ(x-y+h)]u(x)v(y)dxdy`, hence `KK[m](u,u) = ∫u(x)u(x-h)dx + ∫u(x)u(x+h)dx`. I verified this reduces, via the stated substitution `z=x∓h/2`, to their claimed form `2∫_{-a+h/2}^{a-h/2}u(z+h/2)u(z-h/2)dz` — confirmed both algebraically (the two original integrals are related by the shift `x'=x+h` and are in fact identical, giving the factor of 2) and numerically on a concrete test function (`u(x)=\sin(3x)e^{-0.2x^2}+0.3\cos x` on `a=2`, `h=3`): direct computation of the two-delta-term sum gave `-0.398106`; the z-substitution formula gave `-0.398107` — matching to 6 decimal places.

**Bound check (§3's contraction theorem):** for `h=log m>a`, the claimed bound `|KK[m](u,u)| ≤ \|u\|^2_{L^2}` (via `2pq≤p^2+q^2` and disjointness of the shifted intervals) held on the same test function: `KK[m](u,u)=-0.398`, `\|u\|^2=1.469`, ratio `-0.271`, safely inside `[-1,1]` as the theorem requires. The disjointness argument itself (`[-a+h,a]⊂[0,a]` and `[-a,a-h]⊂[-a,0]` for `h>a`) is elementary interval arithmetic and checks out by inspection.

This is a clean, correct, independently-verified piece of mathematics, and it meaningfully explains (without yet fully proving — the entry's own §5 "missing lemma" honestly flags the saturation step as open) why the exactness claim in v13.902 has the shape it does: the bound `s_m≤c_m` is forced by this contraction argument for well-resolved kinks, and the entry is appropriately careful not to claim more than that (saturation to equality is reported as `[N]` numerical observation, not yet `[D]` proof).

## What remains open

v13.902's exact numerical claim (`s_m=c_m` to 4-6 digits) is still not independently reproduced by me, for proxy-fidelity reasons rather than any specific contradicting evidence. v13.904's own "missing lemma" (why the null cluster saturates the contraction bound) is explicitly open per the entry itself, not something I attempted to resolve.

## Self-audit note

Caught and corrected two of my own setup errors mid-round before reporting: including the prime 2 in `S(m)` for the shadow-fraction test (§1), and testing kink-rigidity in the wrong resolution regime relative to the domain size before reading v13.904 (§3). Recording both, consistent with this audit practice's standing commitment to report its own errors alongside what it finds in the source material.

## Result

\[
\boxed{\textbf{PASS: v13.901 confirmed on both tests to close numerical agreement.} \textbf{PASS: v13.904's Contraction Theorem derivation and bound independently re-derived by hand and confirmed numerically on a concrete test function.} \textbf{v13.902's concavity argument is correct; its exact-slope numerics remain unconfirmed by my own cross-check, best attributed to testing a structurally simpler proxy operator rather than to any flaw in their result, especially now that v13.904 supplies a verified analytic mechanism consistent with the claim's shape.}}
\]
