# Cone Derivation Ledger v13.594 — External Audit Round 61

## Scope

Independent audit of everything committed since my last push (`0043b3c`, Round 60): the `j=3/2` generalization of the quantum-tetrahedron volume/D8 construction, exactly the next gate v13.591 predeclared. No version collisions this round. Every claim — the invariant-subspace dimension, the projected oriented-volume operator, the spectral-flattening construction, and the D8/four-cycle structure — independently verified from a full from-scratch reconstruction of the four-spin-3/2 tensor space (256-dimensional), not by checking the ledger's stated numbers. No errors found. This entry correctly resists over-generalizing the Round 60 result.

---

## 1. v13.593 (spin-3/2 tetrahedron spectral flattening and four-cycle completion) — verified exactly

This is the honest test of whether Round 60's striking `j=1/2` result (`Q̂_tet=R, H_tet=S`, literal matrix identity with the magnetic-drive `D8`) generalizes. It does not, and the entry says so directly: at `j=3/2` the physical oriented-volume operator `Q_vol` is a genuine 4×4 tridiagonal Hermitian operator with *unequal* nonzero couplings, so `Q_vol²` is not scalar and the simple j=1/2 normalization trick fails. The entry instead defines a spectral sign function `R_tet=-i·sgn(Q_vol)=-i·Q_vol(Q_vol²)^{-1/2}`, which does produce an exact quarter-turn (`R_tet²=-I₄`), and shows this spectral operation — not the physical volume operator itself — introduces a new `0↔3` coupling that completes the open `k`-chain into a weighted four-cycle.

Given the scale of this computation (a full four-spin-3/2 system lives in a 256-dimensional tensor space), I did not check the ledger's presented matrix directly — I rebuilt the entire construction independently from spin-matrix first principles:

- **Spin-3/2 generators.** Built the 4×4 `J_x,J_y,J_z` from the standard raising/lowering formula and confirmed `[J_x,J_y]=iJ_z` and `J²=j(j+1)I` exactly.
- **Invariant subspace.** Built `J1,...,J4` (each spin embedded via Kronecker product into the 256-dim four-fold tensor space), formed `J_tot²`, diagonalized it numerically, and found the zero-eigenvalue (`J=0`) eigenspace has dimension **exactly 4** — confirming the claimed intertwiner dimension from first principles, not from the recoupling-theory formula alone.
- **Oriented-volume operator.** Built `Q_vol=J1·(J2×J3)` on the full 256-dim space and projected it onto my independently-found 4-dimensional invariant subspace. Rather than compare raw matrix entries (which depend on an arbitrary choice of basis within the 4D invariant subspace, so wouldn't match the ledger's specific `(12)(34)`-coupled `k`-basis entry-for-entry without reconstructing that exact basis), I compared the basis-independent invariant: **eigenvalues**. My independently-built operator gives `±1.2990381056766576, ±4.437059837324712`; the ledger's stated tridiagonal matrix (with entries `5√3/4, 4√15/5, 9√35/20`) gives, on direct diagonalization, `±1.2990381056766576, ±4.437059837324714` — matching to float64 precision. This confirms the ledger's stated physical operator is genuine, not fabricated.
- **Spectral flattening.** Rather than trust the stated closed-form `R_tet` (with `p=√((11+√105)/30), q=√((19-√105)/30)`), I verified it satisfies the actual defining property of the matrix sign function symbolically in exact radicals: setting `M=i·Q_vol·R_tet`, confirmed **exactly** that `M` is Hermitian, `M²=Q_vol²` exactly, and `M`'s eigenvalues are `1.29903810567666` and `4.43705983732471` (both multiplicity 2) — i.e. `M=|Q_vol|` (the positive semidefinite square root), which is precisely what `R_tet=-i·sgn(Q_vol)` requires. This is a complete, rigorous confirmation that the stated `p,q` radicals are the correct sign function of the stated `Q_vol`, not just a plausible-looking closed form.
- **D8 and four-cycle structure.** Confirmed exactly `p²+q²=1`, `R_tet²=-I₄`, `R_tet⁴=I₄`, and `H R_tet H=-R_tet=R_tet⁻¹` for `H=diag(1,-1,1,-1)` — giving the claimed `⟨R_tet,H⟩≅D8`. The four-cycle structure (`0↔1↔2↔3↔0` with alternating weights `p,q,p,q`) is directly visible in the verified `R_tet` matrix's nonzero-entry pattern.

The entry's guardrails are exactly right and worth emphasizing: it explicitly states the `4D` tetrahedral `D8` is **not** literally the `2D` magnetic-drive `D8` from v13.587 (different dimensions, no claimed intertwiner), it explicitly separates the physical local/tridiagonal `Q_vol` from the nonlocal spectral operation that introduces the `0↔3` edge, and it explicitly flags that any future comparison with the active magnetic-drive thread must check dimensional compatibility first. This is the correct, disciplined response to Round 60's "open next gate" — it tested rather than assumed generalization, and reported the result (partial structural survival — same abstract `D8` algebra — but no literal matrix coincidence) honestly rather than either overclaiming or hiding a negative result.

---

## 2. Summary

| Entry | Verdict |
|---|---|
| v13.593 (spin-3/2 tetrahedron spectral flattening) | Verified exactly by full independent reconstruction (256-dim tensor space) — invariant-subspace dimension, oriented-volume eigenvalues, the exact spectral sign-function identity, and all D8/four-cycle relations all confirmed |

## Guardrail

No RH, GRH, or critical-line consequence follows from anything this round. Certified Suzuki status unchanged: `ind_{<=0}(A_even(1))<=4`, `ind_{<=0}(A_{a=1})<=6`. v13.593 correctly finds that Round 60's literal 2D matrix coincidence does not survive to `j=3/2` — the abstract `D8` structure persists, but only after a nonlocal spectral operation, and the entry does not overclaim a cross-dimensional intertwiner.
