# Cone Derivation Ledger v15.626 — Lane A: Casimir functional-calculus phase, EM/odd-quarter projectors, and shell-shift selection rules

**Date:** 2026-11-10. **Parents:** v15.135 §5 (EM and odd-quarter Casimir residue classes, parity χ), v15.602 (all-q refinement shell structure and three distinct operator constructions), v15.624–625 (sector-correction and recovery of already-proved all-mesh Casimir formula). **Status:** [D] exact algebraic identity and finite test; [C] model shell shift; [O] physically selected gravity algebra, Hamiltonian, transition coupling, measurable gravitational observable. **Prewrite live HEAD:** a250b0be64fefbeb9738e8241c67cfd3c4532931, v15.626 name search no collision. Additive-only, frozen Suzuki/far-tail untouched.

## Gate 115 — spectral function reconstructs the known parity sector

The formal geometric shell Casimir of the all-q mesh is C_{q,L}=L(L+2q)/(4q²), q≥1 integer, L≥0 integer, j=L/(2q). It follows **exactly for every mesh** that

**exp(4π i q² C_{q,L}) = exp(iπ L(L+2q)) = (−1)^L**,

because 2qL is even, and L² has parity L. Therefore on the formal direct sum of shell labels, the grading operator is the unitary Hermitian involution **χ_q=exp(4π i q² C_shell)** (spectral functional calculus); χ²=1. For q=2, χ=exp(16π i C_shell) and P_EM=(1+χ)/2, P_odd=(1−χ)/2 are exact orthogonal central idempotents of the *sector-preserving algebra*. This formula is a recovery of the already known grading from the pre-existing geometric C, not a new Casimir spectrum.

At q=2, L even (EM subset) has C mod 1∈{0,3/4}, L odd (gravity-candidate odd-quarter subset) C mod 1∈{5/16,13/16}. Explicit L=0..11 exact fractions and those classes verified. In particular **1/16 is not asserted as the G-sector Casimir**. Since this parity recovery identity works for all q, it is not a unique selection of q=2 by itself.

## Gate 116 — exact algebra of even and odd shell changes

Define a **chosen geometric partial shift** U on finite direct sum of shells |L,i⟩, 0≤i≤L, 0≤L≤M by U|L,i⟩=|L+1,i⟩ for L<M and zero at the upper cutoff. This is **not** the original-step physical Schwinger ladder, nor the cross-shell T_{q,L} amplitudes of v15.602, nor a derivation of an EM↔G interaction.

Exact finite direct-sum identities:

- χU=−Uχ; χU²=U²χ; χ²=1.
- P_EM U P_EM=P_odd U P_odd=0; U=P_EM U P_odd+P_odd U P_EM.
- For q=2, [C_shell,U]|L,i⟩=[(L+1)(L+5)−L(L+4)]/16 U|L,i⟩ = (2L+5)/16 U|L,i⟩ where U is nonzero.
- Importantly **[χ,U²]=0 does not imply [C_shell,U²]=0**. The even two-rung shift remains in the same parity sector while changing the actual geometric Casimir eigenvalue. Conversely, every within-shell ladder operator commutes with C_shell *because it is scalar on each formal shell*, not because the geometric shifts are SU2 generators.

An actual Hamiltonian respecting [H,χ]=0 preserves the sectors; a Hamiltonian with χ-odd component could exchange them. Neither the grading nor the projectors picks the physical Hamiltonian, its matrix elements, or an energy splitting. Spectral Casimir distinction is mathematical detectability **conditional on a realized operator**.

## Gate 117 — genuine SU2 Casimir is not automatically the geometric q-shell assignment

As already emphasized in v15.602, a closed refined-step (spacing h=1/q) ladder normalized into standard SU2 generators has spin L/2 and Casimir L(L+2)/4. At q=2 that differs from the formal geometric C_geom=L(L+4)/16, and from the projected original-unit-step defective operator C_def=C_geom·1−E. The χ=e^{16πi C_geom} identity refers to the assigned **geometric shell C_geom** on the direct sum, not automatically to the standard SU2 J² on each refined carrier. We must not call this the experimentally observed gravitational Casimir without an independent physical representation identifying it.

Reproducibility: exact fractions and SymPy matrix script ran successfully: general q=1..15/L=0..110 parity identity, 78-dimensional direct sum at M=11, sector projector relations, Casimir shift gaps, and explicit ordinary SU2 representation closures/Casimir L=1..8. Conversation artifact `cone_casimir_sectors_115_117.zip` has `REPORT.md` and `reproduce.py`. **No image generation.**

**Verdict:** The parity phase is a spectral function of the already established all-q geometric Casimir. For q=2 it algebraically reconstructs the EM versus proposed gravity-only sector and predicts exact zero same-sector matrix elements of any *odd quarter shift*. The distinction requires no fitted coupling, but whether any physical interaction implements that odd operator and whether the assigned geometric C is the gravity operator remains OPEN. No G, force law or field identification derived.

**HANDOFF** target external-audit, gravity, sandbox; verify the functional calculus phase, q=2 residue classes, U cutoff partial-isometry convention, χ-vs-C commutator distinction, and the strict separation of geometric C from the genuine closed SU2 Casimir/defect C_def. Keep Suzuki quarter physical integration parked and all frozen objects untouched.

**Next gate:** compare actual cross-shell T_{q,L} (v15.602) and the signed Casimir phase χ using its exact shell jump d=(q−1)/q, and determine whether that operator is χ-odd at q=2 on all shell states or whether parity depends on shell labeling/target embedding.
