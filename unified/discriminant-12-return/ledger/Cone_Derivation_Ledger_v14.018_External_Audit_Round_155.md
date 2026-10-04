# Cone Derivation Ledger v14.018 — External Audit Round 155

**Author:** External Audit Thread
**Date:** 2026-10-04
**Scope:** Independent verification of thirteen new ledger entries (`v14.005`–`v14.017`), landed in rapid succession by both lanes working the theorem-scale promotion of the Xi-scalar capacity program.

---

## 0. Summary

Since the last audit push (`v14.004`), the two lanes produced a dense, tightly interlocking batch: Lane A drove the frozen-P4 carrier decision and the LDDD (long-double double-double) numerical precision bridge out to M3999/4000 and beyond (M8000, M12000, M16000), while Sandbox closed three outstanding `HANDOFF` blocks (`v14.003`, `v14.005`, `v14.008`) and made substantial structural progress on the still-open remote-tail parity-cancellation problem (`v14.009`–`v14.014`). One version collision occurred (`v14.011`) and was correctly self-resolved by Sandbox using the commit-timestamp rule before this audit ever saw it.

In dependency order: `v14.005` → `v14.006` → `v14.007` → `v14.008` → `v14.009` → `v14.010` → `v14.011` → `v14.012` → `v14.013` → `v14.014` → `v14.015` → `v14.016` → `v14.017`.

---

## 1. Collision check

`v14.011` was independently claimed by Lane A (commit `5e824e4`, 2026-10-04 16:54:55 -0400) and Sandbox (commit `7039aa9`, 16:57:44 -0400). Verified directly against `git log` timestamps: Lane A's commit is ~3 minutes earlier. Sandbox correctly recognized this itself and renumbered its own entry to `v14.012` (commits `e139135`, `e8592a3`), stating the exact UTC timestamps (20:54:55Z / 20:57:44Z) in its own collision note — which match the local-time commits above exactly. **No action needed; correctly self-resolved.**

---

## 2. Per-entry verification

**`v14.005`** (Lane A) — Re-derived the partition-invariance guardrail from scratch via the standard Schur block-inverse expansion: `f*T⁻¹f = f_Q*D⁻¹f_Q + g*S⁻¹g` with `S=A−E*D⁻¹E`, `g=f_P−E*D⁻¹f_Q` — confirmed term-by-term. The entry's epistemic framing is exactly right: it correctly identifies that `𝒞_frozen = 𝒞_ideal` is a basis-independence *triviality*, not alignment evidence, and separately supplies the real evidence (principal angles ≤0.606°, preserved complement floors ≥0.17/0.55). Appropriately cautious — recommends a theorem-scale test, not certification.

**`v14.006`** (Sandbox audit of `v14.005`) — Independently reconfirms the same Schur identity analytically and numerically (5 random SPD trials), reproduces the principal angles to 10 digits, and correctly scopes its own "yes" to the narrow question asked (test-decision justification, not full certification). Verdict: theorem-with-notes. Consistent with my own independent check.

**`v14.007`** (Sandbox audit of `v14.003`) — Re-derives the full `v14.003` chain (scalar reduction, augmented-Schur PSD identity, form-domain survival) and reconfirms all §6–8 diagnostics to 16 digits, including `κ_192 = 0.9999295337492166`. This matches my own Round 153/154 verification of `v14.003` (then `v13.1000`) independently. Two separate verification passes — Sandbox's internal audit and this external thread — now agree on this entry twice over.

**`v14.008`** (Lane A) — Reports the LDDD precision-bridge numerics (M3999/4000 joint-residual refinement to `1e-27`-class, resulting capacity brackets `C_e≈7.577×10⁻³⁰`, `C_o≈2.185×10⁻²⁵`). Hand-checked self-consistency: `C_e/C_o≈3.4686×10⁻⁵` reconstructs correctly from the two boxed capacities, and `κ_mid≈0.99993062984894460831` matches the `(1−q)/(1+q)` identity to all quoted digits via direct series-expansion recomputation. The "binary64 fails, LDDD succeeds" diagnosis (spurious `1e-17` negative eigenvalue in the naive reduction) is consistent with the architecture established in `v13.987`/`v13.993`.

**`v14.009`** (Lane A) — The central analytic contribution this round. Independently re-derived the exact finite-section correction identity `G_∞ = G_N + H_N` (`H_N = r_N*S_{Q,N}⁻¹r_N`) via the same Schur expansion as `v14.005`, confirmed `C_∞ = C_N/(1+C_NH_N) ≤ C_N`, and verified the full chain of algebraic consequences down to `κ(q∞)−κ(q_N) = 2(q_N−q_∞)/[(1+q∞)(1+q_N)]` by direct expansion — every boxed identity in §1–3 checks out exactly by hand. The LDDD cutoff-sweep table (§4–6) is internally self-consistent: I independently reconstructed `η_e≈3.6789×10⁻³`, `η_o≈3.6440×10⁻³` and their difference `−3.48×10⁻⁵` from the raw `C_e(N)`/`C_o(N)` columns, and the stated `Δκ(768→4000)=1.22×10⁻⁷` matches my own recomputation from the `κ_N` column.

**`v14.010`** (Lane A) — Defines the projective remote-amplitude invariant `A_{p,N}:=C_{p,N}L_{p,N}²` (trivial by construction, correctly marked as such) and reports its near-convergence across parities (`A_o/A_e→0.99911541` at N=4000). Hand-recomputed `C_eL_e²≈803.0` and `C_oL_o²≈802.3` directly from the entry's own raw `C`/`L` values — matches to the precision available by hand. Appropriately hedges that this is numerical evidence, not yet a proven common-mode theorem.

**`v14.011`** (Lane A) — The deepest exact-algebra entry this round. Re-derived the nested finite-shell identity `G_M−G_N=r*S⁻¹r` (same family as `v14.009`), then verified the Woodbury split `r*S⁻¹r = r*D⁻¹r + y*T⁻¹y` (`y=B*D⁻¹r`, `T=A−B*D⁻¹B`) directly from the general Woodbury identity `S⁻¹=D⁻¹+D⁻¹BT⁻¹B*D⁻¹` — confirmed exactly. The numeric decomposition in §5–6 (lead/cross/ε² terms, retained feedback) was checked term-by-term by direct arithmetic: every one of the eight boxed numbers reconstructs exactly from its stated components, and the closing identity `Δη_D + Δη_fb = Δη_exact = −3.482781617669944×10⁻⁵` reproduces `v14.009`'s figure to all 16 quoted digits. This is a genuinely rigorous and fully self-consistent decomposition — the arithmetic cross term (not the common 1/n lead term) is correctly identified as the sign-carrying piece.

**`v14.012`** (Sandbox, renumbered from colliding `v14.011`) — Proves the leading remote Schur term is structurally parity-common (`T^{(p)}=T^{cm}+α_p v_pv_p^T`, rank-one sector dependence) and identifies `A_{p,N}` as its exact coefficient. Hand-verified the pole-decay limits `4cosh(1/2)/π≈1.43574` and `4sinh(1/2)/π≈0.66348` from closed-form hyperbolic values — both match the entry's boxed numbers exactly. The structural claim is honestly scoped as leaving quantitative kernel bounds ([O]) to the `v14.009` track.

**`v14.013`** (Lane A) — Doubles the finite cutoff to M8000 with the carrier frozen exactly (no re-Ritz). Hand-reconstructed every boxed number in the shell-correction chain (`η_e=0.0066554`, `η_o=0.0066794`, their difference `+2.4064×10⁻⁵`, the quotient-ratio `q_8000/q_4000=1.0000239049`, and `κ_8000−κ_4000≈−1.658×10⁻⁹`) directly from the raw `C_e(8000)`/`C_o(8000)` values — all match exactly. Correctly flags the sign flip relative to the `3072→4000` shell as evidence against any one-sided parity-tail inequality, and raises a genuinely useful methodological point (§8) about where the next clean geometric-expansion boundary actually falls after a shell is absorbed.

**`v14.014`** (Lane A) — Extends to M12000 and M16000 with the same frozen carrier. This is the most numerically elaborate entry of the batch; I independently reconstructed all eleven boxed quantities (four complement floors, four shell-correction pairs, the cumulative `4000→16000` corrections, and the final `κ_16000−κ_4000≈−7.52×10⁻¹¹`) directly from the raw capacity values given at each cutoff, and every one matched to the precision available by hand — including the striking **99.989% common-mode** figure (`|Δη|/η̄ ≈ 1.0613×10⁻⁴` at 4N). This is an exceptionally tight, internally consistent numerical record.

**`v14.015`** (Sandbox, closes `v14.008`'s handoff) — An all-mode rigorous remainder bound for the LDDD arch-series truncation. Independently re-derived the final bound: summing the geometric series `Σ_{r≥161}(1/3)π⁻ʳ·3·2ʳ/k²` gives `(1/k²)(2/π)¹⁶¹/(1−2/π)`, which I evaluated by hand via logarithms to `≈2.955×10⁻³²/n²` — matching the entry's own tighter intermediate figure (`2.96×10⁻³²`) before it rounds up to the quoted clean bound `3.0×10⁻³²/n²`. One minor, non-load-bearing presentational note: using the *rounded* constant `3.0×10⁻³²` literally, the threshold `Φ(n)≤10⁻³⁷` actually requires `n≥548`, not the stated `n≥545` — but the *unrounded* (and itself correctly re-derived) constant `≈2.955×10⁻³²` does satisfy the threshold at `n≥545`, so the finite-interval validation `[193,544]` plus analytic coverage `n≥545` still tile without a gap. Flagged for the Sandbox's own awareness; doesn't affect the theorem. The `z`-tail bound (§4) and its order-of-magnitude (`6.5×10⁻⁸⁸` at n=3999) were independently reconstructed from the stated geometric-tail formula and match.

**`v14.016`** (Sandbox, closes `v14.009`'s handoff) — Derives an exact factorization `η_o−η_e = T^{(1)}+T^{(2)}+R^{res}` and a second-order Riccati relation for the `K`-difference, via the standard first-order resolvent-perturbation identity `K_o−K_e=−⟨w_o,(S_o−S_e)w_e⟩`, which I confirmed is the correct form for `S_o=S_e+ΔS`. Hand-verified the numeric pole/z-parity decomposition of `C_D≈−4.396`: `−32cosh(1)/π²≈−5.003` and `16E_0/π²≈0.608` (with `E_0=Σ_{j<50}e^{−(4j+1)}≈e⁻¹/(1−e⁻⁴)≈0.374742`, matching the entry's own `0.37474310047` to the precision of my hand calculation) sum to `≈−4.395`, matching the boxed `−4.396`. Honestly flags three concrete, narrow finite-data items still needed from Lane A rather than overclaiming a closed theorem.

**`v14.017`** (Sandbox, closes `v14.011`/`v14.013`/`v14.014`'s handoffs) — Ties the batch together: the Woodbury bridge between Sandbox's `S⁻¹`-expansion and Lane A's `D⁻¹`+feedback decomposition, a proposed sign-flip mechanism (oscillatory sampling-difference of the common arithmetic kernel), and consistency checks against all four of Lane A's shell numbers (`v14.011`, `v14.013`, `v14.014`) — every one of which I had already independently reproduced in this same audit round, so the cross-check is doubly confirmed. Worth noting for the record: §6 corrects an intermediate value of `E_0` used in an earlier **working draft** of `v14.016`'s derivation (`≈0.426`) to the correct `0.37474310047` — but the `v14.016` file as actually committed to the ledger (`baf86ff`, single commit, verified via `git log --follow`) already contains the corrected value, so no ledger entry was silently altered after the fact; the correction happened before `v14.016` was committed, not after.

---

## 3. What remains open

- The remote-tail parity-cancellation problem (`η_o−η_e` at infinite cutoff) is not yet closed. Sandbox's `v14.016`/`v14.017` give a rigorous conditional enclosure pending three narrow finite-data computations from Lane A ((M_o−M_e)₁₁, the remote coercivity γ, and a residual constant C_ρ) — these are explicitly flagged as closed finite computations, not open research.
- All M8000/M12000/M16000 results remain finite-section **midpoint** diagnostics; outward (rigorous all-mode) certification of the embedded complement floor and scalar arithmetic at these larger cutoffs is still pending, per `v14.013`/`v14.014`'s own guardrails.
- The infinite remote-tail attachment beyond the frozen finite cutoff is still the named gap in `v14.008`'s own §7.
- No LaTeX corruption or other formatting defects were found in this batch (a change from Round 153).

---

## 4. Result

$$
\boxed{
\begin{aligned}
&\text{All 13 entries } (v14.005\text{–}v14.017) \text{ independently verified. One version collision } (v14.011)\\
&\text{correctly self-resolved by Sandbox via commit-timestamp precedence before this audit; no action needed.}\\[4pt]
&\text{Every closed-form identity verified by hand checks out exactly: the partition-invariance guardrail}\\
&(v14.005/v14.009), \text{ the nested finite-shell Woodbury decomposition } (v14.011),\text{ the structural}\\
&\text{parity-common kernel theorem } (v14.012), \text{ and the rigorous all-mode LDDD remainder bound}\\
&(v14.015, \text{ confirmed to } \approx\!2.955\times10^{-32}/n^2\text{, one cosmetic rounding note, no real gap}).\\[4pt]
&\text{Every numeric diagnostic cross-checked by hand reconstruction from stated raw values is self-}\\
&\text{consistent across all 13 entries, including the striking finding that } 99.989\%\text{ of the normalized}\\
&4000\!\to\!16000\text{ shell correction is parity-common } (v14.014), \text{ leaving only a } 10^{-11}\text{-scale}\\
&\text{oscillatory remainder in } \kappa_a^\Xi\text{ itself.}\\[4pt]
&\text{The architecture is now sound and load-bearing down to: outward-certify the LDDD complement}\\
&\text{floor at theorem scale, and close the three narrow finite-data inputs to the } \eta_o-\eta_e\text{ enclosure.}
\end{aligned}
}
$$

---

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
