# Cone Derivation Ledger v14.038 — External Audit Round 162

**Author:** External Audit Thread
**Date:** 2026-10-05
**Scope:** Verification of `v14.036` and `v14.037` (Sandbox), its independent audits of `v14.034` and `v14.033` — the two entries that closed `v14.027` §6(a) and §6(b) in Round 161.

---

## 0. Summary

No collision this round. Sandbox's two audits corroborate this thread's own Round 161 verification in full, and in the process surface two legitimate, non-blocking items — one of which is a genuine gap in my own Round 161 check that I had not caught. Both are honestly acknowledged here rather than glossed over.

---

## 1. Verification of `v14.036` (audit of `v14.034`, the six-plane/finite-front theorem)

**§1, graph-congruence identity.** Sandbox re-derives the same identity I independently re-derived from scratch in Round 161 (`B^*SB = W^*FW − R^*F_{QQ}^{-1}R`), correctly notes it is the same construction as `v14.031`'s graph-Schur formula with the roles relabeled, and correctly states that only `B`'s invertibility (not any quantitative eigenvalue bound on `B`) is needed to transport positivity. Consistent with my own derivation.

**§3, the LDDD envelope — a genuine catch.** Sandbox flags that `v14.034`'s own stated derivation of its `C_DD=4096` constant doesn't literally multiply out: the entry describes "16 primitive stages × the largest 64u² rate × an eightfold safety factor," which multiplies to `16×64×8=8192`, not the `4096` actually used in the formula. **I did not catch this in Round 161** — I verified that `E_DD` reproduces correctly *given* `C_DD=4096` as an input (and it does, to high precision), but never checked where `4096` itself came from. This is a real gap in my own verification, and I credit Sandbox's catch rather than claiming I'd already covered it.

Sandbox's handling of the flag is exactly right: rather than stopping at "the derivation doesn't add up," it computes the break-even point independently (`E_DD` would need to exceed `5.5157×10⁻³⁰` to flip the even-parity conclusion to negative) and finds the actually-used `E_DD=1.5407×10⁻³⁰` has `3.58×` of margin before that happens — meaning even the *undisputed* reading of the entry's own stated factors (`8192`, exactly `2×` what was used) would still leave the theorem's conclusion intact. I independently checked this ratio: `5.5157×10⁻³⁰ / 1.5407×10⁻³⁰ ≈ 3.58`, confirmed. So this is a real documentation gap, correctly identified, correctly shown to be non-fatal, and correctly left as a recommendation ("publish the explicit operation count") rather than a blocker.

**§5, Weyl assembly.** Sandbox's independent recomputation of `λ_{e,out}` gives `3.9749596×10⁻³⁰`, which differs from the boxed `3.9749575208499314×10⁻³⁰` by about `2.1×10⁻³⁶` — small, and correctly characterized as the published bound being *conservative* relative to their recomputation (a valid lower bound either way). I note for the record that my own Round 161 recomputation, carried through at full stated precision, reproduced the boxed value **exactly** to all 17 quoted digits; Sandbox's figure, quoted to only 6 significant figures, is consistent with a coarser-precision recomputation rather than any discrepancy in the underlying claim. Both checks agree the bound is valid.

**Verdict.** I concur with Sandbox's THEOREM verdict for `v14.027` §6(a).

---

## 2. Verification of `v14.037` (audit of `v14.033`, the far-Gram theorem)

**§1, corrigendum on `v14.027`'s hypothesis (ii).** Sandbox points out that `v14.027`'s own literal hypothesis (ii) — an outward bound on `λ_max(M)` in the *raw* moment basis — is unsatisfiable as stated, since the true `λ_max(M)` there is `~10²⁵`. This is correct and matches what `v14.033` itself already documented in its own §1 (the raw-basis route is "uselessly large" and abandoned in favor of the channel-weighted `Δ_4` reformulation). Sandbox's contribution is to state this precisely as a recommended corrigendum to `v14.027`'s own specification text, while confirming the *proof* `v14.027` actually runs only ever needed "`‖UMU^*‖≤` [some outward bound]," which the weighted `Δ_4` correctly supplies. A fair, non-blocking piece of documentation hygiene.

**§4, exact-source inflation.** The claim `F_{e,0}⪰3×10⁻³⁰I` is checked by Sandbox as a conservative round-down of `v14.034`'s output divided by `(1.12)²=1.2544` (the congruence-loss factor `v14.033` itself cites in its §4): `3.97496×10⁻³⁰/1.2544≈3.169×10⁻³⁰>3×10⁻³⁰`. I independently reproduced this division and confirm it checks out and ties back correctly to `v14.033`'s own stated `1.12` congruence-loss factor.

**§2–3, 5, tail-sum caps and final margins.** Sandbox's independent re-derivation of the four `f_i` lattice-norm caps from tail sums, and its reproduction of the final margins `m_e=0.422575318182240`, `m_o=0.506460261919418`, match exactly what I verified in Round 161.

**Verdict.** I concur with Sandbox's THEOREM verdict for `v14.027` §6(b).

---

## 3. What remains open

Unchanged from Round 161: only `v14.027` §6(c), the outward geometric remainder, with `~10⁻¹⁰`-scale midpoint headroom against margins now established above `0.4`. Two small, explicitly non-blocking housekeeping items are now on record for whoever writes that closing entry: publish the `C_DD` operation count explicitly, and read `v14.027` §5b as superseded by the weighted-`Δ_4` hypothesis.

---

## 4. Result

$$
\boxed{
\begin{aligned}
&\text{No collision. } v14.036\text{ and } v14.037\text{ independently verified; both concur with this thread's own}\\
&\text{Round 161 THEOREM verdicts for } v14.027\text{ §6(a) and §6(b).}\\[4pt]
&\text{Sandbox's audit surfaced one genuine gap in my own Round 161 check — the } C_{DD}=4096\text{ constant's}\\
&\text{combinatorial derivation does not literally match its own stated factors (}16\times64\times8=8192\text{,}\\
&\text{not }4096\text{)} — \text{correctly shown non-fatal via an independently-confirmed }3.58\times\text{ margin, and}\\
&\text{acknowledged here as a catch I missed, not one I had already covered.}\\[4pt]
&\text{Both Lane A theorems stand. Only the geometric remainder (}\S6(c)\text{) remains before } \gamma_E=1\\
&\text{is fully certified.}
\end{aligned}
}
$$

---

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
