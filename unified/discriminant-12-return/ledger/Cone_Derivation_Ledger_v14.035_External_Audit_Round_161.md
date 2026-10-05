# Cone Derivation Ledger v14.035 — External Audit Round 161

**Author:** External Audit Thread
**Date:** 2026-10-05
**Scope:** Resolve a `v14.032` collision, and verify two major Lane A entries that between them close two of the three remaining items in `v14.027`'s Euclidean-coercivity checklist — leaving only the geometric remainder before `γ_E=1` is fully certified.

---

## 0. The collision

This thread's own Round 160 entry (`9790e1c`, 2026-10-05 03:28:15 UTC) and a Lane A entry ("Outward M8000 mu=1 Protected Six-Plane and Finite-Front Positivity," `6f82afe`, 09:52:09 -0400 = 13:52:09 UTC) both claimed `v14.032` — Round 160 landed roughly ten and a half hours earlier. Per the standing commit-timestamp precedence rule, Round 160 keeps `v14.032`; the Lane A entry is renumbered to `v14.034` (next free slot, since `v14.033` was already taken by a separate, non-colliding entry). Four cross-references inside `v14.033` that pointed at the contested number (its `Parents:` field and three in-body citations) were updated to `v14.034`; no other file referenced it. No mathematical content altered in either entry.

---

## 1. Verification of `v14.034` (ex-`v14.032`, "Protected Six-Plane and Finite-Front Positivity")

This is the most significant single result in the discriminant-12-return ledger since the `γ_E` gap was first identified in Round 156: it closes `v14.027` §6(a) completely, certifying positivity of the full finite shifted front `F_p` (both the large complement, already closed in Rounds 159–160, and the previously-untouched six-dimensional protected block).

**§2, graph congruence identity — re-derived from scratch.** The entry claims `B^*SB = W^*FW - R^*F_{QQ}^{-1}R` for a graph trial `W` with invertible protected-coordinate matrix `B=(P^*P)^{-1}P^*W`, normalized graph `Ŵ=WB^{-1}=P+X`, and `R=QFW`. I re-derived this independently via completion-of-squares on the bilinear form `F` restricted to the subspace spanned by `Ŵ`'s columns: writing `Ŵ*FŴ = S + (X+F_{QQ}^{-1}F_{QP})^*F_{QQ}(X+F_{QQ}^{-1}F_{QP})` (completing the square in the `Q`-component, with `S` the exact Schur complement), then substituting `X+F_{QQ}^{-1}F_{QP}=F_{QQ}^{-1}RB^{-1}` (derived from `R=QFW=QF\hat{W}B` and `QF\hat W = F_{QP}+F_{QQ}X`), and finally using `Ŵ*FŴ=B^{-*}W^*FWB^{-1}` to clear `B^{-1}`/`B^{-*}` from both sides. The result matches the entry's boxed identity exactly. Since `B` is invertible (confirmed by `v14.034`'s own near-identity `σ_min(B)` computation in §3), congruence preserves the positivity sign, so `B^*SB≻0 ⟺ S≻0` — meaning the entry only needs to show `W^*FW-R^*F_{QQ}^{-1}R≻0` using the *specific* numerically-represented graph trial, never resolving the exact Schur complement's own exponentially-small spectrum directly. This is an elegant and correct technique.

**§5–8, arithmetic chain — independently reproduced exactly.** I recomputed the full charge-subtraction chain from the entry's own stated inputs:
- `E_DD ≤ 4096·N·u²·Q_comp` with `u=2⁻⁶⁴`, `N=4000`, `Q_comp≤32`: `4096·4000·(2⁻⁶⁴)²·32 ≈ 1.5409×10⁻³⁰`, matching the boxed `1.5407439555097887×10⁻³⁰`.
- `E_{R,e} = ‖R‖²/δ_e = (10⁻²⁰)²/7.795385618610192746×10⁻⁶ ≈ 1.2828×10⁻³⁵`, matching exactly; `E_{R,o}` likewise matches exactly.
- The final subtractions `λ_{p,out}=λ_{p,mid}-E_{src,p}-E_{DD}-E_{R,p}`: on a first pass I mis-scaled `E_{R,e}` by one decimal place and got a result differing from the boxed value in the 6th significant figure; redoing the conversion correctly, both `λ_{e,out}=3.9749575208499314×10⁻³⁰` and `λ_{o,out}=1.4355391835167209×10⁻²⁶` reproduce **exactly** from the stated midpoint pivots and charges. (Noting my own slip and its correction here, per standing practice.) The retention percentages (69.79% even, 99.989% odd) also check out from these values.

**§9, finite-front theorem.** Given `F_{QQ}^{(p)}≻0` (rigorously, from `v14.031`, already verified in Round 160) and the exact protected Schur matrix `S≻0` (established by §8 above), the standard block-matrix positive-definiteness criterion (a block matrix is PD iff one diagonal block is PD and its Schur complement is PD) gives `F_p≻0` directly — correctly applied. `v14.027` §6(a) is therefore genuinely closed, not merely narrowed.

---

## 2. Verification of `v14.033` ("Scaled Four-Channel Far-Gram Outward Bound")

This entry closes `v14.027` §6(b), the four-channel far Schur correction, consuming `v14.034`'s result. It is built from a chain of deliberately loose, round "public caps" rather than tight computed values throughout (`0.15`, `1.02`, a final `×1.5` inflation) — a valid but less exhaustively tight style than `v14.034`'s. I verified every individual link:

- The inverse-perturbation inflation factors: `1/(1-θ_e)` with `θ_e<0.01004` gives `≈1.01014`; `1/(1-θ_o)` with `θ_o<7.51×10⁻⁷` gives `≈1.000000752` — both match, and both are correctly superseded by the looser consumed public cap of `1.02`.
- The combination arithmetic: `1.02×(1.2428000003133972+0.15)≈1.420656`, `1.02×(1.1869700135759420+0.15)≈1.363709` — both match the stated intermediate values.
- The final public theorem caps are explicitly **not** these tighter values but `1.5×` the original raw midpoint budgets instead (`1.5×1.2428...=1.864200000470096`, `1.5×1.1869700...=1.780455020363913`) — both reproduce exactly; this is a looser-but-still-valid substitution, correctly flagged as a deliberate simplification.
- The final margins: `m_e = 2.2867753186523356094-1.864200000470096 = 0.4225753181822396` and `m_o = 2.2869152822833307687-1.780455020363913 = 0.5064602619194178` — both match the boxed `m_e>0.422575318182240` and `m_o>0.506460261919418` exactly.

The residual-propagation formula `|b^TD^{-1}r|≤\sqrt{h_i}·‖r‖/\sqrt δ` with `h_i≤16/δ_p` was checked numerically against the stated single-entry error caps (`4.105×10⁻³` even, `9.809×10⁻⁴` odd) and reproduces both to the precision available by hand.

---

## 3. What remains open

Only `v14.027` §6(c) — the outward enclosure of the high-order geometric remainder beyond the four retained signed-moment channels. Both new entries note this already has enormous headroom: the midpoint `ℓ²` scale is `~10⁻¹⁰` (`v14.020`/`v14.022`) against margins of `~0.42`–`0.51` now established above. Once the finite moment intervals behind that `10⁻¹⁰` figure are stated outwardly (rather than at midpoint precision), `v14.027` promotes `S_{p,4000}⪰I` rigorously in both parities, and `v14.016`/`v14.022`'s enclosure may consume the certified Euclidean constant `γ_E=1`.

---

## 4. Result

$$
\boxed{
\begin{aligned}
&\text{Collision resolved: Round 160 keeps } v14.032\text{; the Lane A finite-front theorem renumbered to}\\
&v14.034\text{, content and four internal cross-references in } v14.033 \text{ updated, no mathematical change.}\\[4pt]
&v14.034\text{ independently verified in full, including an exact re-derivation of its central graph-}\\
&\text{congruence identity and the complete numeric charge-subtraction chain (one self-caught,}\\
&\text{self-corrected decimal-place slip in my own recomputation). } v14.027\text{ §6(a) — finite shifted-}\\
&\text{front positivity — is genuinely closed, not merely narrowed.}\\[4pt]
&v14.033\text{ independently verified: every public-cap substitution and the final margin arithmetic}\\
&\text{reproduce exactly. } v14.027\text{ §6(b) is closed.}\\[4pt]
&\text{Of the three items tracked since Round 156, only §6(c) — the geometric remainder, already}\\
&\text{known to be many orders smaller than the now-certified margins — remains before } \gamma_E=1\\
&\text{is fully certified.}
\end{aligned}
}
$$

---

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
