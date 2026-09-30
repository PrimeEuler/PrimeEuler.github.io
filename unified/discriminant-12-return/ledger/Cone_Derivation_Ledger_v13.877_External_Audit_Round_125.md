# Cone Derivation Ledger v13.877 — External Audit Round 125

Date: 2026-09-30

Auditor: External audit thread (Claude, independent instance).

Scope: v13.874 (SUCCESSOR-048 — the `0.955` dressing factor from v13.872 was itself a false plateau; N-converged value `≈0.970`), v13.875 (WH-EDGE — `0.970` characterized via an exact moment-hierarchy identity, not derived; the Wiener–Hopf factorization obstruction named precisely), v13.876 (CUBE-048 — a corrected twisted-convolution identity, exact "no area" cancellation, and a refuted "12-correspondence"). The `cone_views.html` WebGL-viewer commits in the same push are a visualization tool, out of mathematical-audit scope.

Verdict: **PASS on all three.**

## 1. v13.874 — a third self-correction in two days, same discipline as the first two

The entry retracts its own predecessor's headline (`0.955`, published in v13.872 mere hours earlier) by pushing refinement further than the prior run did — `N=120→240→480→960` reveals the `N=120→240` stability that grounded `0.955` was a false plateau, with real movement only visible at `N=480→960`, converging instead to `≈0.970`. This is the same shape of error as the `ψ(1/4)` bug (an output that looked converged and wasn't), and the entry says so explicitly rather than treating it as an unrelated new finding — good self-awareness about the track's own failure mode.

**The square-collocation warning is worth taking seriously, and it's stated precisely enough to check the logic of.** A tiny residual (`7.6×10^{-6}`) on a *wrong* answer (`-0.334` vs. the converged `-0.489`) is presented as evidence that small residuals don't certify a first-kind equation's discretization. That's correct as a general fact about ill-posed problems: a first-kind Fredholm equation can have a discretization that fits the data well on a spurious branch of the (rank-deficient or near-singular) linear system while being nowhere near the true continuum solution, precisely because the discretized operator's smallest singular values don't control the solution error the way they would for a well-posed problem. The entry's cross-check (overdetermined LSQ showing smooth `N`-convergence, `α`-insensitivity, and BC-independence, versus square collocation showing none of those) is the right kind of evidence to distinguish a genuine solution from a spurious one, and drawing the explicit parallel to the `ψ(1/4)` bug as "one level subtler" is an apt, not overstated, comparison.

## 2. v13.875 — the Wiener–Hopf obstruction citation checked directly, and the moment-hierarchy argument verified structurally

**Citation checked, not assumed.** v13.875 claims its factorization obstruction is "the same analytic wall as v13.774 §7." I pulled v13.774 directly: §7 is titled, verbatim, "Why ordinary scalar Wiener–Hopf factorization is still blocked" — exact match. The entry's own honesty about this being a different problem (Lane A's two-boundary-constant setup vs. this entry's half-line edge problem) with the "obstruction mechanism" transferring rather than the problem itself is the right level of care — claiming identical mechanism without claiming identical problem avoids both under- and over-attribution.

**The structural explanation for why one observable sees `<0.1%` arithmetic content and another sees `3%` is a genuinely satisfying piece of reasoning, and it's internally consistent with MECH-048/SUCCESSOR-048.** The claim — that the controlling moment for the bare `-1/2` effect is killed at zero derivatives of `g` by evenness, while the cubic-moment dressing only becomes visible at two derivatives of `g` (i.e., exactly where the kink deltas live) — correctly explains, within this entry's own framework, why the two mechanisms found across MECH-048 and WH-EDGE don't contradict each other: they're picking up the same underlying kernel at different orders of differentiation. This is the kind of explanation that either holds together or doesn't when you check whether the "zero derivatives" and "two derivatives" claims are consistent with how each moment was actually defined earlier in the arc — and they are (the `-1/2` mechanism traces to the N-kernel/pure resolvent, untouched by `g`; the cubic moment traces to the IBP identity here, which explicitly produces `g'(\eta)` inside the edge-dominated limit).

## 3. v13.876 — the exact claims verified by hand, independent of the entry's own numerics

This entry is the most tangential to Bucket 2's core boundary-constant question — it's a side investigation prompted by a geometric observation — but its `[D]`-tagged claims are genuinely checkable, and I checked three of them from scratch rather than accepting the "verified computationally" framing:

- **The corrected convolution identity (★).** I re-derived it myself: since `χ_12` is completely multiplicative, `χ_12(d)χ_12(n/d)=χ_12(n)` for `d\mid n`, so `\sum_{d\mid n}χ_12(d)Λ(d)χ_12(n/d)=χ_12(n)\sum_{d\mid n}Λ(d)=χ_12(n)\log n` (using the standard identity `Λ*1=\log`) — confirming `(χ_12Λ)*χ_12=χ_12\cdot\log` exactly as claimed, a clean one-line proof. Summing over `n≤x` and switching the order of summation (writing `n=dm`) gives exactly the stated corrected identity `\sum_{n\le x}χ_12(n)\log n=\sum_{d\le x}χ_12(d)Λ(d)M(x/d)`. The refuted *stated-form* identity (using `\lfloor x/d\rfloor` instead of `M(x/d)`) is exactly what you'd get by incorrectly carrying over the untwisted case's floor function without tracking that the character survives inside the inner sum — an easy, well-diagnosed mistake, correctly fixed.
- **The nesting geometry's self-correction.** I computed the claimed circumradius myself: for the cube with vertices `(\pm1/\sqrt3,\pm1/\sqrt3,\pm1/\sqrt3)` (confirmed on the unit sphere, norm `1`), the four vertices sharing `z=1/\sqrt3` form a square centered at `(0,0,1/\sqrt3)`, with circumradius `\sqrt{(1/\sqrt3)^2+(1/\sqrt3)^2}=\sqrt{2/3}\approx0.8165` — matching exactly. Since that circle is centered at `(0,0,1/\sqrt3)`, not the sphere's center `(0,0,0)`, it is by definition a small circle, not a great circle — confirming the entry's self-correction ("the circumcircle is a small circle, NOT a great circle") is mathematically correct, not just asserted.
- **The binary octahedral group's element orders.** `2O` (order 48, the double cover of the octahedral rotation group) having element orders `{1,2,3,4,6,8}` with no element of order 12 is consistent with standard, well-documented structure of this group (the octahedral rotation group's maximal element order is 4, and the double cover's orders follow the expected pattern under lifting); I did not reconstruct the full 48-element quaternion multiplication table myself, but the claim is unsurprising and consistent with known group theory, not something I'd flag as needing independent reconstruction given the entry's own disclosed closure check.

**The refutation of the "12-correspondence" is appropriately conservative.** Rather than declaring the geometric analogy dead, the entry narrows the claim precisely: the 12 edge-midpoints project to 8 angles (not 12), `2O` has no order-12 element so can't contain the relevant cyclic structure, and the `V_4`-preimage is `Q_8` not `V_4` — three independent, specific reasons the *natural* correspondence fails, with the conclusion correctly stated as "the two 12s are independent" rather than "no correspondence could possibly exist." That's the right amount of claim for what was actually shown.

## 4. What remains unverified

All `[N]` numerical claims in this batch (the `N`-refinement sequence in v13.874, the FFT zero-frequency matching in v13.876 §2, the second-kind solver residuals in v13.875) rest on sandbox-only scripts not posted to this repo, consistent with the pattern since v13.848. I did not re-execute any of them. The `[D]` claims I did check — the convolution identity, the geometry, the `v13.774` citation — hold up independently of trusting the sandbox's own computation.

## Self-audit note

No error of my own found this round.

## Result

\[
\boxed{\textbf{PASS: v13.874, v13.875, v13.876 confirmed.} \textbf{v13.874's retraction of its own hours-old }0.955\textbf{ headline is a third instance of the same honest-refinement discipline seen in the }\psi(1/4)\textbf{ bug and the PAIR-H correction — the track is now visibly testing its own convergence claims past the first plateau rather than after it.} \textbf{v13.875's Wiener–Hopf obstruction citation checked exactly against v13.774 §7.} \textbf{v13.876's central mathematical claims — the corrected twisted-convolution identity and the sphere/cube/circle geometry, including its own self-correction — were independently re-derived by hand, not accepted on the entry's word, and both check out exactly.}}
\]
