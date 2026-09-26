# Cone Derivation Ledger v13.825 — External Audit Round 108

Date: 2026-09-26

Auditor: External audit thread (Claude, independent instance).

Scope: v13.823 (the exact rank-four tail spectral projector and two-mode Feshbach reduction) and v13.824 (a residual-certified numerical basis for that projector).

Verdict: **PASS on both. v13.823 is a genuinely elegant piece of operator theory** — it combines the two already-audited theorems (ρ=0.10, ρ=0.02) into an exact, basis-free, infinite-dimensional spectral statement, purely by nested-projector logic and the standard resolvent-norm-equals-inverse-distance-to-spectrum fact for self-adjoint operators. **v13.824 turns that into a concrete, independently-reproduced numerical object**, complete with a correctly-applied Davis–Kahan subspace-error bound.

## 1. v13.823 — the P4 projector: verified by hand, logic checks out

The core move (§1) is worth stating plainly because it's the kind of step that's easy to wave through without checking: since `(-0.02,0.02) ⊂ (-0.10,0.10)`, the spectral projector `P_4 = 1_{(-0.02,0.02)}(J_T)` has range contained in `1_{(-0.10,0.10)}(J_T)`'s range. Both are already proven to have rank exactly 4 (v13.816, v13.821). A rank-4 subspace contained in another rank-4 subspace must equal it — so **nothing new enters between radius 0.02 and radius 0.10**, and the ρ=0.10 and ρ=0.02 four-resonance clusters are provably the *same* four resonances, not coincidentally-numbered different ones. This is correct and is the right way to combine the two theorems.

I checked the resulting moat bound directly: for a self-adjoint (normal) operator, `‖(J_T-δ)^{-1}‖ = 1/dist(δ, σ(J_T))`. Since `σ(J_T)` restricted to `Ran Q_4` avoids `[-0.10,0.10]` entirely, and `|δ|≤0.02`, the nearest possible spectrum is at distance `≥ 0.10-0.02 = 0.08`. That gives exactly the claimed `‖Q_4(J_T-δ)^{-1}Q_4‖ < 12.5 = 1/0.08` (and `<10` at `δ=0`) — confirmed by direct computation, not just accepted on the entry's word.

The rest (§3–8: Schur/Feshbach block reduction to a 2×2 meromorphic map, the pole-residue decomposition with `R_j = C(δ_j)^*P_jC(δ_j) ⪰ 0`) is standard finite-rank perturbation theory, correctly applied — the `C(δ)^*P_jC(δ) - C(δ_j)^*P_jC(δ_j)` divisibility argument used to isolate the holomorphic background is the standard trick and I don't find a gap in it.

I ran both diagnostic scripts referenced in §9–10 (correctly marked `[N]`, not theorem-bearing): `suzuki_endpoint_rho010_rho002_negative_space_angles.py` reproduced all eight principal angles exactly; `suzuki_tail_generalized_ritz_N96.py` reproduced six of eight reported Ritz values closely, with the two near-machine-epsilon values (`~5×10⁻¹⁶` scale, corresponding to the already-proven-exact zero kernel) differing at the noise floor — expected and not a finding, since neither the entry nor any downstream claim depends on that digit.

## 2. v13.824 — the numerical P4 basis: fully reproduced, including the heavy computation

I ran `suzuki_tail_P4_residual_basis_certificate.py` directly — a substantial computation (graph extension through mode 16001/16002, residual accumulation through two million). It completes with `PASS: residual-certified numerical basis for Ran P4`, and **every reported figure matched exactly**: both sets of M2 Ritz values, both finite/explicit-remote/far residuals, both `β` bulk-floor computations, both `B^{-1/2}` residual caps (`0.0331`, `0.0323`), and both final angle bounds.

I independently re-verified the Davis–Kahan arithmetic by hand rather than just trusting the printed numbers: `0.0331/0.08 = 0.41375` (`arcsin ≈ 24.4°`, matching the claimed primary bound) and, using the sharpened separation `0.08 → 0.0997` from the tighter Ritz-location caps, `0.0331/0.0997 = 0.332` (`arcsin ≈ 19.4°`, matching the sharpened bound). Same check for odd-v (`0.404`/`23.8°` primary, `0.361`/`21.2°` sharpened) — all confirmed.

Both entries are appropriately hedged: neither claims the four eigenvalues are simple, positive, or individually resolved; v13.824 explicitly flags itself as not-yet-frozen and requests external replay before being used as a residue payload — which is what this round provides.

## Self-audit note

No error of my own found this round.

## Result

\[
\boxed{\textbf{PASS: v13.823 and v13.824 fully confirmed, including hand-verification of the core spectral-nesting argument and the Davis–Kahan bound, plus direct execution of both heavy numerical scripts.} \operatorname{rank}P_4=4 \textbf{ with an exact 0.08 moat is now a rigorous, basis-free infinite-dimensional fact, and a concrete residual-certified numerical carrier for it now exists (}\theta_{\max}<19.4°/21.2°\textbf{ sharpened).}}
\]
