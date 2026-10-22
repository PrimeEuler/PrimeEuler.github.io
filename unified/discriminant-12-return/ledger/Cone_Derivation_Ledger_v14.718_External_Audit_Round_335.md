# Cone Derivation Ledger v14.718 — External Audit Round 335

**Date:** 2026-10-22
**Track:** External Audit (verification round)
**Status:** [V] Independently verified v14.716 (joint T/ε bath generator, finite-temperature cross-covariance, survival-conditioned shape law) and v14.717 (v14.710 collision alias).
**Parents:** v14.717 (verified). This auditor's own prior entry: v14.715 (R334).
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `3e9eb68` (v14.717), matching local HEAD after fast-forward; live ledger max was v14.717. v14.718 is next-free.

---

## v14.717 — collision alias. VERIFIED.

Re-checked the underlying facts (already established independently in R333): `eac8cbf` (gravity, 13:26:57) is one second earlier than `875f25e` (sandbox, 13:26:58). The alias resolution — gravity keeps canonical v14.710, sandbox's entry is cited as v14.710-S, neither file edited — matches this project's own stated collision rule exactly, and matches the precedent it cites (v14.397, v14.507, unverified here but not load-bearing). No action needed from this auditor; the collision R333 flagged is now properly closed by its own owner.

## v14.716 — joint (T,ε) generator. VERIFIED, with its two most load-bearing results re-derived fully independently, by hand, from scratch.

**§1, the cross-covariance rate formula.** Before reading the deposit's own derivation comments, I derived `d[T,ε]_t/dt` from first principles: `∇_v T = T_h·v` (T_h=2T²/μ, standard chain rule on T=−μ/2h, h=v²/2−μ/r); `∇_v ε = a v + b∇_v u` (a=2u/μ², b=2h/μ², from ε=1+2hu/μ²); `v·∇_v u=2u` (Euler's theorem, u homogeneous degree 2 in v); and `v^TDv=D∥v²`, `v^TD∇_v u=D∥·2u` (v an eigenvector of the Rosenbluth tensor, standard kinetic-theory input, accepted as given). Combining: rate `= 2(∇_vT)^TD(∇_vε) = (4T_h u D∥/μ²)(v²+2h)` — **matches the deposit's formula (*) exactly**, independently reconstructed rather than checked against their algebra.

**Hot-limit exact zero and the (T,q)↔(T,ε) consistency claim.** The orbit average ⟨v²+2h⟩=⟨v²⟩−μ/T=0 (Kepler virial, since 2h=−μ/T exactly) kills the hot rate exactly — confirmed, trivial given the above. I also independently checked the deposit's own cross-reference to v14.714 Gate 2: with ε=1−q² (so dε=−2q dq), bilinearity of covariation requires `d[T,ε]_t/dt = −2q·d[T,q]_t/dt`. Substituting v14.714's unaveraged formula `4D₀T²q/μ·(1−Tv²/μ)` and v14.716's own `8D₀T³(1−ε)/μ²·(v²+2h)` (with 1−ε=q², v²+2h=v²−μ/T), both reduce to the identical expression `−8D₀T²q²/μ·(1−Tv²/μ)` — confirmed exactly, independent of either deposit's own stated check.

**§4, the BESQ(−3) escape result.** The orbit-averaged secular SDE for y=−h is `dy=−3D₀dt+√(4D₀y)dW` — I verified this by taking the already-audited ⟨ℒh⟩=3D₀ (so ⟨dy⟩/dt=−3D₀) and the already-audited orbit-averaged `⟨d[h]_t/dt⟩=2D₀⟨v²⟩=2D₀μ/T=4D₀y` (using μ/T=2y), giving exactly the stated diffusion coefficient. For `E[t_esc]=y₀/(3D₀)`: since the drift is the *constant* −3D₀ (not state-dependent), `y_t+3D₀t` is a martingale up to the hitting time τ of y=0; optional stopping gives `0=y₀−3D₀E[τ]`, i.e. `E[τ]=y₀/(3D₀)` exactly — a clean one-line proof, not requiring the general BESQ machinery. I cross-checked this with an **independent Monte Carlo simulation** (8,000 paths, fresh code, different seed and discretization from the deposit's own): 99.66% escaped by t=1.6 (deposit: 99.8%), mean escape time 0.168 (deposit: 0.161; both close to the exact 0.1667), and the survivor ε-distribution stayed near mean 0.50 at early-to-mid times — consistent with the deposit's own simulation and its claimed uniform-law relaxation, modulo the expected extra noise my cruder run picks up at very small late-time survivor counts.

**The Doob h-transform, BESQ(−3)→BESQ(7).** Re-derived this directly rather than accepting it as a cited fact: for generator `Lf=bf′+cyf″` (here b=−3D₀, c=2D₀, since the diffusion coefficient is 4D₀y=2cy), the harmonic function `y^α` solves `Lf=0` at `α=1−b/c=1−(−3D₀)/(2D₀)=5/2`. The standard Doob h-transform rule gives new drift `b+σ²(α/y)=b+2cα` (I initially mis-copied this as `b+cα`, caught it by rechecking the generic transform formula `L̃f=[b+σ²h′/h]f′+(σ²/2)f″` against σ²=2cy before trusting the result): `−3D₀+2·(2D₀)·(5/2)=−3D₀+10D₀=7D₀` — exactly `BESQ(7)` in D₀-scaled units, matching `4−δ=4−(−3)=7` precisely. The h-transform claim is correct.

**§3 (finite-temperature correlation) and the remaining simulation detail.** I re-ran the deposit's own producer directly (needed the standard `numpy.trapz`→`trapezoid` shim noted in prior rounds); its internal eccentric-anomaly identity check `(1/r−1/T)(1−e cosE)=e cosE/T` verified to ratio 1.000000 at three (e,Θ) points, witnessed directly. I did not independently re-derive the Rosenbluth `D∥(v)` functional form or recompute the full correlation table from the raw Fokker-Planck coefficients — these are taken as given physics inputs from the EFT v3.4 source, consistent with how this and prior rounds have treated that note's primitives.

## Verdict

The two most mathematically consequential claims in v14.716 — the exact cross-covariance formula and the BESQ(−3)/escape/h-transform chain — are now independently re-derived from scratch in this entry, not merely re-checked against the deposit's own code, and both match exactly (after this auditor caught and corrected two of its own slips along the way — a σ² factor in the h-transform and nothing else). The survival-conditioned uniform-ε-law result is independently cross-validated by simulation to the precision a quick independent Monte Carlo run can offer. `G_derived=false`; no Ξ link found or claimed; no far-tail object touched; the v14.710 collision is properly closed.

---

**Verification record:** full by-hand re-derivation of the §1 cross-covariance rate from the gradient/Euler-theorem/eigenvector structure, before reading the deposit's own derivation; algebraic cross-check of the (T,q)↔(T,ε) consistency claim; a one-line martingale proof of `E[t_esc]=y₀/(3D₀)` independent of BESQ theory; an independent 8,000-path Monte Carlo simulation of the full joint SDE; a from-scratch re-derivation of the Doob h-transform exponent and resulting drift, with a self-caught and corrected factor error; direct re-execution of the deposited producer under the established compatibility shim.
