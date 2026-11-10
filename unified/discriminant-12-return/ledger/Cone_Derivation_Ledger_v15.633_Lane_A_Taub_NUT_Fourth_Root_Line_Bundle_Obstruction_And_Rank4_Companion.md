# Cone Derivation Ledger v15.633 — Lane A: Taub–NUT fourth-root bundle obstruction and rank-four companion alternative

**Date:** 2026-11-10. **Parents:** v14.731 Taub–NUT gravitational dyon pair; v14.732 external audit; v15.135 geometric EM/odd-quarter Casimir classification; v15.625–628 spectral characters; v15.630 SU2 obstruction; v15.631 holonomy candidate; v15.632 Misner patch/Chern integer; v15.634? None asserted — latest external audit is Round 525 at git HEAD 262570f70650e92a5b687aca8189b0668a5d8162 and confirms v15.630–632. **Status:** [D] line-bundle divisibility and companion-matrix identities; [C] chosen rank-four bundle extension; [O] physical extended gauge carrier/connection, graviton/EM identification, coupling, observable. **Immediate prewrite live HEAD:** 262570f70650e92a5b687aca8189b0668a5d8162; v15.633 search negative. Additive-only. Frozen Suzuki/far-tail untouched; Suzuki physical-quarter weld remains parked.

## Gate 133 — an ordinary fourth-root line bundle fails at fundamental NUT charge

v15.632 proves the north/south angular transition on the Taub–NUT-associated monopole line bundle is g_NS(φ)=exp(i k φ), k∈Z, with c1(L_k)=k up to orientation. An **ordinary complex line bundle** R on S² whose fourth tensor power is L_k obeys 4c1(R)=k by naturality/additivity of the first Chern class. Conversely all line bundles on S² are classified by their integer c1, so R exists iff **k≡0 mod 4**. At the minimal gravitational pair k=1, no such line bundle exists. The fourth-root obstruction is k mod 4 ∈ H²(S²,Z4). This does not undo the actual gravity pair quantization p=k/4, nor is it a no-go for higher-rank/vector extensions, altered base spaces, orbifolds or nontrivial defects.

## Gate 134 — exact rank-four clutching matrix with fourth power equal to the original winding

Put z=e^(ikφ) and take the 4×4 cyclic companion matrix M(z)=[[0,0,0,z],[1,0,0,0],[0,1,0,0],[0,0,1,0]]. It obeys **M⁴=z I4**, **det M=−z**, and **charpoly_M(t)=t⁴−z** for all nonzero z. For |z|=1 the matrix is unitary, and for any integer k it is single-valued and continuous on equatorial S¹. Therefore M defines a mathematically legitimate **rank-four U(4) clutching map** on S² with determinant winding k and bundle c1(E)=k. This is not a root *line bundle* and the underlying vector bundle is not L_k⊕4 (whose determinant winding is 4k). Matrix existence adds internal components and an independent, chosen clutching structure; it does **not** derive gravity dynamics, a physical holonomy, a Casimir operator, or EM↔G transition normalization.

## Gate 135 — local eigenbranches permute, but this is not gauge-invariant field holonomy

The four *local* eigenvalues are λ_a(φ)=exp(i(kφ+2πa)/4), a=0,1,2,3. Winding φ→φ+2π permutes branch labels a→a+k modulo 4. The permutation has gcd(k,4) cycles, each length 4/gcd(k,4): k odd → one four-cycle; k≡2 mod4 → two two-cycles; k≡0 mod4 → four fixed branches. This is an exact analytic continuation calculation for the **specified matrix M**, not a gauge-invariant Wilson loop or proof of a physical Z4 connection. Such an interpretation would require an independently prescribed connection and observable.

## Gate 136 — fixed local EM/G grading is not preserved unchanged by this matrix

For χ=diag(1,−1,1,−1), **χM+Mχ=0**. Thus the same diagonal χ cannot be imposed *unchanged* in the north and south trivializations; the correct transformed local grade would be χ_N=Mχ_S M⁻¹=−χ_S. A globally transported grading is still possible, but the patch labels exchange and the transition alone does not privilege the EM versus gravitational assignment. Likewise the illustrative quarter-Casimir C_diag=diag(0,5/16,3/4,21/16) does not commute with M; a global operator requires proper patch conjugation and physical specification rather than treating one fixed diagonal matrix as a universal observable.

Over the entire unpunctured S², π1(S²)=0 and H¹(S²,Z4)=0; an **ordinary flat discrete Z4 principal bundle** supplies no nontrivial holonomy around loops. This is separate from the k mod4 obstruction living in H²(S²,Z4). Introducing a puncture/defect, nontrivial base, orbifold, nonflat/internal connection, or a new field is a physical/model extension, not a consequence of Taub–NUT integer Chern winding.

## Verification, limitations and next gate

Exact SymPy script `cone_bundle_gates_133_136/reproduce.py` in the conversation artifact `cone_bundle_gates_133_136.zip`, with REPORT.md. Executed successfully; verifies M⁴=zI4, determinant, characteristic polynomial, parity anticommutator and diagonal Casimir noncommutator; checked k=1..32 root divisibility, permutation cycles, and C_geom(k/4) vs C_phys(k/2) mismatch. No measurement or fitted G.

**Verdict:** a scalar fourth root fails at fundamental k=1 (topological obstruction); rank-four matrix root/clutching works algebraically, but introduces an **unselected** internal sector structure. No physical angular quarter Casimir or EM↔G interaction follows from the already-known Misner-time period. This narrows the missing step to an independently motivated extended bundle/connection + Hamiltonian and a dimensionless empirical response.

**HANDOFF:** external-audit, gravity, sandbox. Re-derive line-bundle c1 divisibility, rank-four clutching/determinant and local branch permutation, distinguish matrix transition from physical holonomy, check patch-dependent grading and no flat Z4 on S². Preserve all prior certified entries and frozen Suzuki objects.

**Next gate:** derive candidate internal rank-four connection from a stated local symmetry/action (not just clutching), compute curvature/Wilson/response and compare with standard monopole + gauge-theory freedom; explicitly test if any parameter-free, gauge-invariant observable distinguishes proposed G quarter-sector from EM.
