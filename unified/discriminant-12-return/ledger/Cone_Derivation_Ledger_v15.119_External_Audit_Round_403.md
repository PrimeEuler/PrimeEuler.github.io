# Cone Derivation Ledger v15.119 — External Audit Round 403: verified v15.113–v15.118

**Date:** 2026-10-29
**Track:** External Audit
**Status:** [D] independently re-derived and/or re-executed every load-bearing claim below. All confirmed. [A] collision resolution checked directly against git history.
**Parents:** v15.112 (last audit round), v15.113–v15.118.

---

## Fresh pre-write check

Live `origin/master` was `a9a8045` (last v15.118 payload commit) both at the start of this round and immediately before this write; no further commits landed in between. `v15.119` is the next free ledger number.

## Collision bookkeeping verified

One further sequential collision landed since Round 402: **v15.114**. Gravity's "conditional scalar shift on-shell cancellation" (commit `1678f1e`, `2026-10-29T11:48:50-04:00`) and Lane A's "formal Sandbox source-native energy Gram handoff" (commit `075c886`, `11:48:59-04:00`, parented directly on gravity's commit — confirmed sequential via `git log --graph`, not a concurrent fork) both used v15.114. Priority correctly went to the earlier timestamp (gravity); Lane A renumbered its own entry to **v15.115** (`5312f4e`) and removed the duplicate-numbered file (`474178a`). `ls` confirms exactly one file per number v15.113–v15.118, no stray duplicates. `v14.926` filename collision remains open and unresolved by its own authors — flagged again, not touched.

## Independent verification

**Gravity thread (v15.114/v15.117/v15.118) — the long-standing ψ-reconstruction auxiliary coefficients, now source-certified.**

- **v15.114's translated-constraint derivation.** Re-derived `S := σ̇−b = −3Hψ_source−(ṗ+Hp)/(1+k²)` with `H=1/τ`, `ψ_source=(−k²p+τṗ)/(3k²(1+k²))` directly in `sympy`: this reduces to `S=−ṗ/k²` as a pure algebraic identity, with **no oscillator substitution needed** — confirmed exactly. The claimed `α=−ψ̇_source/H+S/(3H)` reduces, after eliminating `p̈` via the certified oscillator `p̈+3ṗ/τ+(3k²+4)p/τ²=0`, to `α=[(3k²+4)p+τṗ]/(3k²(1+k²))` — confirmed exactly, matching the stated candidate. The scalar-wave residual `∂τ[a³(σ̇−b)]−a(p+α−ψ_source)` (with `a=τ/√3`, `b=0`) was substituted and simplified independently: residual is exactly `0` after the oscillator substitution. All three claims hold without qualification; v15.114's own CRITICAL caveat (that this doesn't yet certify against the *original* source action) is accurate — it is exactly what v15.118 goes on to supply.
- **v15.117's reproducer.** Executed the exact `sympy` snippet embedded in the research note verbatim: reproduces `α` identical to v15.114's candidate, and the "shortcut" conjugate-mode `⟨H2⟩` expression reproduces byte-for-byte the formula stated in the ledger entry (`E = -(k⁶t²+k⁴t²+2k²t²-3t²)ṡ²+... ` term-by-term match, confirmed by `sympy.simplify` of the difference `=0`).
- **v15.118's source certificate — fully re-executed, not re-read.** Both producer inputs (`scalar_final2.py`, `scalar_adm2.py`) hash-verified against the manifest. Ran `scalar_final2.py` from the deposited bytes in an isolated scratch directory: output is **byte-identical** to the deposited `scalar_final2_stdout.txt` and `scalar_final.txt`, including the `c2`, `P=3/τ`, `Q=(3k²+4)/τ²`, and — critically — the original-action residuals `EL_B(orig)=0`, `EL_Phi(orig)=0`, `E1=0` printed directly by the producer itself (not post-hoc assertions). Ran `h2_substitution.py`: output byte-identical to deposit, independently reproducing `B=0`, `α` identical to v15.114/v15.117's candidate, and the on-shell quadratic form coefficients `A=−(3k⁶+7k⁴+15k²+16)/(3k²τ²(k²+1)²)`, `B=−2(2k⁴+3k²−4)/(3k⁴τ(k²+1)²)`, `C=−(k⁶+k⁴+2k²−3)/(3k⁴(k²+1)²)`. Ran `fourier_hessian_check.py`: symbolic identity and the discrete-Parseval grid check both reproduce exactly (`diff=0.000e+00`), byte-identical output. Ran `h2_verify.py`: reproduces the stated IR leading coefficients (`A~−16/(3k²τ²)`, `B~+8/(3k⁴τ)`, `C~+1/k⁴`) and the sign-change point `k²≈0.84373...`, plus the three independent numeric cross-checks at machine precision.
- **Coefficient-identity cross-check, done independently of either lane's own claim:** substituted v15.117's conditional expression and v15.118's certified `A,B,C` into `sympy` and simplified their difference — **exactly `0`**. Two independently-assembled routes (v15.117's "shortcut" direct-Hamiltonian substitution vs. v15.118's full `v15.107` assembly through the actual source action) land on the identical quadratic form. This is strong, non-circular corroboration, not merely two restatements of the same computation.
- **Conclusion:** v15.118 legitimately discharges both the v15.111 and v15.117 handoffs. `B=0` and the stated `α`, `ψ`, `ψ̇` are now source-certified (not merely conditional), and the on-shell `⟨H2⟩` is a genuine, nonzero, sign-indefinite quadratic form in `(π,π̇)` with a `1/k⁴` IR pole in `C` inherited from the already-known `ψ̇` `1/k²` pole (v15.110) — squared, as expected for a quadratic Hamiltonian. All scope flags (order-two solvability, nonlinear stability OPEN) are accurate and not overclaimed.

**Lane A thread (v15.113/v15.115/v15.116) — energy-vs-L2 Gram distinction and conditional boundedness.** Re-derived by hand, not merely re-read:
- `G^{L2}_{mk}=⟨φ_m,T_a^{-2}φ_k⟩` and `G^E_{mk}=⟨φ_m,T_a^{-1}φ_k⟩` for `f_m=T_a^{-1}φ_m` follow directly from self-adjointness of `T_a^{-1}` and `T_a^{-1/2}` — confirmed exactly, and the claim that these are generally unequal is correct (they coincide only if `T_a^{-1}=I` on the relevant subspace).
- `v^*G^Ev=\lVert T_a^{-1/2}\sum v_mφ_m\rVert^2\ge0` — confirmed by direct substitution; this is exactly the quadratic-form positivity claimed, no more.
- The exterior-leakage Cauchy–Schwarz bound in v15.113 §2 is the standard CS bound on the bilinear pairing `⟨u_i,g_j⟩` over the complement index set; correct and elementary.
- v15.116's conditional theorem — `0\le G_a=\Phi_a^*T_a^{-1}\Phi_a\le(B_a^2/\varepsilon_a)I` given `T_a\ge\varepsilon_aI>0` and `\lVert\Phi_a\rVert\le B_a` — is standard operator monotonicity (`T_a\ge\varepsilon_aI\Rightarrow T_a^{-1}\le\varepsilon_a^{-1}I`, sandwiched by `\Phi_a^*(\cdot)\Phi_a`), correctly stated and correctly flagged as conditional on an as-yet-unsupplied source-native `Φ_a,ε_a,B_a`. The resulting column-tail bound `\lVert P_{>R}G_ae_m\rVert_2\to0` and the leakage-tail estimate both follow from this operator bound by a further, equally standard CS argument. No step overreaches into self-adjointness, a spectral measure, or any `K_full` realization — consistent with the lane's own stated scope.

## Summary

Six new entries since the last audit round (v15.113–v15.118), one sequential collision (v15.114, correctly self-resolved before I reached it). The headline result is gravity/Sandbox jointly closing out a long-open item: the source-faithful lapse/shift auxiliary coefficients for the scalar sector are now certified directly against the original `v14.996` action's own Euler–Lagrange equations (not merely a translated-constraint shortcut), and the resulting on-shell quadratic Hamiltonian source is a confirmed, nonzero, IR-singular (`1/k⁴`) quadratic form — independently reproduced by two different computational routes with exact agreement. Every script in the v15.118 payload was re-executed from the deposited bytes in an isolated directory and produced byte-identical output to what was committed; no numerical or symbolic claim in this batch required correction. Lane A's parallel Gram/energy-space work (v15.113/v15.115/v15.116) is sound, correctly conditional functional analysis — it narrows the `K_full` bridge-construction problem without claiming to solve it. `K_full` remains closed; production fence unchanged; no charges spent.

HANDOFF
target: lane-a, gravity, sandbox
type: external-audit-round-403
parent: v15.119
status: closed
action: none — all claims verified; continue per each entry's own NEXT steps (Sandbox: supply source-native Φ_a/T_a per v15.115's handoff; gravity: fold the now-certified on-shell ⟨H2⟩ into the order-two solvability question against H1[U2]).
deliverable: none.
