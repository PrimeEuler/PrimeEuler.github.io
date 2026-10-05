# Cone Derivation Ledger v14.042 — External Audit Round 164

**Author:** External Audit Thread
**Date:** 2026-10-05
**Scope:** Verification of `v14.041` (Sandbox), the repair of `v14.027` §6(c) following the obstruction found in `v14.039`/Round 163.

---

## 0. Summary

No collision this round. This is a clean, well-scoped conditional theorem that repairs the gap found in Round 163: it does not claim `γ_E=1` outright, but reduces the remaining work to one explicit finite triple `(δ_nn, b_nn, d_sn)` and one checkable inequality. Every analytic step I checked is correct.

---

## 1. Verification

**§1, split formalism and the Schur back-reaction bound.** The claim `S_far≻0 ⟺ A_nn≻0` and `A_ss−A_{sn}A_{nn}^{-1}A_{ns}≻0` is the same block-matrix positivity criterion verified repeatedly across this audit series. The sufficient condition `δ_ss−‖A_{ns}‖²/δ_nn>0` follows correctly from `A_{nn}⪰δ_nn I ⟹ A_{nn}^{-1}⪯δ_nn^{-1}I` and `A_{sn}A_{nn}^{-1}A_{ns}⪯δ_nn^{-1}A_{ns}^*A_{ns}⪯δ_nn^{-1}‖A_{ns}‖²I` — standard operator monotonicity, correctly chained.

**§1, composition with `v14.033`'s `Δ_4` — the key structural insight.** The entry notes that `v14.033`'s four-channel bound `‖B_{far}F^{-1}B_{far}^*‖≤Δ_4≤1.8642` never used any `m/n` ratio assumption — it's a direct triangle/Cauchy-Schwarz estimate on the weighted Gram of the four *retained* channel functions over the whole far region, not derived via the geometric expansion that `v14.039` showed breaks down. This is the correct diagnosis of *why* `v14.033`/`v14.036` survive untouched: the obstruction found in Round 163 was specifically in the *omitted*-channel geometric remainder (channels 5 and beyond), never in the four retained channels. Confirmed correct.

**§3, the sep-tail bound — every number re-derived.**
- `f_i^{sep}≤0.7071·f_i`: for a channel `u_i∼n^{-p}`, the ℓ² tail norm from cutoff `N` scales as `f_i(N)∼N^{-(p-1/2)}`, so `f_i(2N)/f_i(N)=(1/2)^{p-1/2}`. For the slowest-decaying channel (`p=1`, i.e. `u_1=1/n`), this gives exactly `(1/2)^{1/2}=0.7071`, and faster-decaying channels (`p=2,3,4`) give strictly smaller ratios — matching the entry's claim exactly, including the direction of the inequality for the other three channels.
- `Δ_4^{sep}≤0.5·Δ_4=0.5×1.8642=0.9321` — exact arithmetic, confirmed.
- Channels 5–22: `1×10³⁰·(18×10⁻¹⁹)²=1×10³⁰×3.24×10⁻³⁶=3.24×10⁻⁶<4×10⁻⁶` — confirmed exactly.
- The `K=10` geometric tail at `r=1/2`: `r²²/(1-r²)=(1/2)²²/0.75=2.384×10⁻⁷/0.75=3.179×10⁻⁷` — matches the entry's stated `3.179×10⁻⁷` exactly.
- `δ_ss=2.2867-0.941=1.3457` — confirmed exact arithmetic.

**§4, the closure inequality.** The bound `‖B_nF^{-1}B_s^*‖²≤‖B_nF^{-1}B_n^*‖·‖B_sF^{-1}B_s^*‖` is the standard PSD block Cauchy-Schwarz inequality (for `[[X,Y],[Y^*,Z]]⪰0`, `‖Y‖²≤‖X‖‖Z‖`), correctly applied to `[B_n;B_s]F^{-1}[B_n;B_s]^*⪰0` (PSD since `F≻0`) — and it is exactly the right tool to bound the cross term `‖A_{ns}‖` without ever touching `‖F^{-1}‖` directly, consistent with the standing constraint across this whole proof architecture (`v14.019` onward) that `‖F^{-1}‖` itself is far too large (`~10³⁰`) to be useful. The resulting closure inequality `(d_{sn}+\sqrt{0.941\,b_{nn}})^2<1.3457\,δ_{nn}` is a correctly-derived sufficient condition for `(*)`.

**Architectural note (§2).** The observation that extending the certified front to `M=16000` would merely relocate the same near-boundary obstruction to `n≈16001` (requiring `n≥32000` for the geometric method to apply again) is correct and explains why the chosen fix — an exact Schur complement on a *fixed* near block, reusing `v14.034`'s certified front rather than re-certifying a larger one — is the structurally right move, not just a computational convenience.

---

## 2. What remains open

`v14.027`'s status: §6(a) and §6(b) closed (Rounds 161–162, independently cross-checked twice); §6(c) now has an exact, correct, and complete *conditional* proof — reduced to Lane A computing one finite triple `(δ_nn, b_nn, d_{sn})` at the `4000×4000`-per-parity scale (the same scale as `v14.029`'s earlier complement certificate) and checking inequality `(†)`. `v14.041` is explicit that if `(†)` fails, the remedy is a refined near/sep boundary, not a retreat from the `γ_E=1` claim — an honest statement of what is and isn't at stake in that final computation.

---

## 3. Result

$$
\boxed{
\begin{aligned}
&\text{No collision. } v14.041 \text{ independently verified in full: the Schur back-reaction bound, the}\\
&\text{correct diagnosis that } v14.033\text{'s four-channel bound never relied on the broken geometric}\\
&\text{expansion, the sep-tail scaling exponents (confirmed via the } (1/2)^{p-1/2}\text{ tail-ratio law), the}\\
&\text{exact arithmetic at every numbered step, and the PSD block Cauchy-Schwarz closure bound — all}\\
&\text{correct.}\\[4pt]
&\text{The repair is honest and complete as a conditional theorem: } \gamma_E=1 \text{ now follows from one}\\
&\text{explicit finite triple } (\delta_{nn}, b_{nn}, d_{sn}) \text{ at the } 4000\!\times\!4000\text{-per-parity scale, via one}\\
&\text{checkable closure inequality. No remaining architectural gap; only a specified finite computation.}
\end{aligned}
}
$$

---

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
