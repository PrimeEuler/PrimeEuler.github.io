# Cone Derivation Ledger v13.590 — External Audit Round 59

## Scope

Independent audit of everything committed since my last push (`08ba8c0`, Round 58): the first entry in a new quantum-tetrahedron/LQG thread, testing whether the audited v13.583 Schwinger/Casimir ladder data enters the standard SU(2) closure-constrained four-spin intertwiner construction (the "quantum tetrahedron" of loop quantum gravity). No version collisions this round. Every matrix, kernel dimension, and recoupling-channel identification independently reconstructed from first principles rather than checked against the ledger's own numbers. No errors found.

---

## 1. v13.589 (four-spin-1/2 quantum-tetrahedron closure kernel) — verified exactly, by independent reconstruction

This entry is explicit about its own standard: "The test is whether the exact v13.583 ladder data enters the closure-constrained four-spin intertwiner construction" — not whether the two constructions merely share tetrahedral language. For four spin-1/2 faces, it shows the answer is constructive: the v13.583 ladder amplitudes are literally the 0/1 entries of the total raising/lowering operators restricted to the zero-weight sector, and their common kernel is exactly the standard two-dimensional `k=0,1` SU(2) recoupling/intertwiner space.

Rather than check the ledger's stated matrices against themselves, I rebuilt everything independently from the definitions:

- **Zero-weight sector.** For four spin-1/2's, states with `J^z_tot=0` have exactly two `+` and two `-` — confirmed the claimed 6-dimensional basis is complete (`C(4,2)=6`).
- **Closure matrices `J⁺_tot`, `J⁻_tot`.** Built these from scratch in sympy by explicit combinatorial state-flipping (for each basis state, flip every admissible `-`→`+` for `J⁺`, or `+`→`-` for `J⁻`, landing in the `m_tot=±1` sectors) — not by trusting the ledger's presented matrices. The reconstructed matrices matched the ledger's stated `J⁺_tot` and `J⁻_tot` **exactly, entry for entry** (also independently hand-verified all 12 nonzero entries by direct combinatorics before running the script, as a second check).
- **Kernel dimension.** Both matrices have rank 4; the stacked closure matrix also has rank 4, giving `dim ker = 6-4=2` — confirmed exactly, matching the standard fact that four spin-1/2's have a 2-dimensional invariant subspace.
- **Nullspace/recoupling identification.** Confirmed the ledger's stated nullspace basis `u1,u2` are exactly annihilated by both `J⁺_tot` and `J⁻_tot`. Independently built the normalized `k=0` and `k=1` recoupling-channel vectors `v0,v1` from the standard Clebsch-Gordan singlet constructions and confirmed `u1=2v0`, `u2=v0+√3·v1` exactly, with `v0,v1` orthonormal.
- **Pair-Casimir eigenvalues (the actual `k=0`/`k=1` identification test).** This is the check I did fully independently of the ledger's own presentation: built the two-spin Casimir operator `(J₁+J₂)²` from explicit 2×2 Pauli spin matrices tensored into the 16-dimensional four-qubit space (not reusing any ledger-derived object), and confirmed `(J₁+J₂)²v0=0` and `(J₁+J₂)²v1=2v1` exactly — the defining eigenvalue test that these are genuinely the `k=0` and `k=1` recoupling channels, not just an arbitrary orthonormal basis of the same 2D space.
- **Centered Casimir completion.** `k(k+1)=(k+1/2)²-1/4` for `k=0,1` gives `0=1/4-1/4` and `2=9/4-1/4` — confirmed trivially, correctly identified as the same centered-half-lattice relation already established for the `j`-ladder in v13.583.

The entry's guardrails are exactly right: it explicitly states this reproduces standard SU(2) closure/recoupling and does **not** yet claim the cone/factor realization changes the quantum-tetrahedron spectrum or supplies new quantum-gravity dynamics, and it correctly identifies the actual next nontrivial test — the oriented triple-product/volume operator on `span{v0,v1}`, which is the first operator that probes genuine quantum geometry beyond closure and dimension-counting. This is precisely the right scope: a real, checkable link (the v13.583 ladder amplitudes literally are the closure-matrix entries) established before any interpretive claim, exactly the standard this thread's own recent work (v13.576, v13.587) has held to.

---

## 2. Summary

| Entry | Verdict |
|---|---|
| v13.589 (four-spin-1/2 quantum-tetrahedron closure kernel) | Verified exactly by full independent reconstruction — closure matrices, kernel dimension, nullspace basis, and both Casimir-eigenvalue recoupling-channel identifications all reproduced from scratch, not merely checked |

## Guardrail

No RH, GRH, or critical-line consequence follows from anything this round. Certified Suzuki status unchanged: `ind_{<=0}(A_even(1))<=4`, `ind_{<=0}(A_{a=1})<=6`. v13.589 establishes a genuine, checkable link between the audited SU(2)/Casimir ladder bridge (v13.583) and the standard quantum-tetrahedron closure construction; it correctly stops short of any quantum-gravity or new-physics claim pending the volume-operator test it proposes as the next gate.
