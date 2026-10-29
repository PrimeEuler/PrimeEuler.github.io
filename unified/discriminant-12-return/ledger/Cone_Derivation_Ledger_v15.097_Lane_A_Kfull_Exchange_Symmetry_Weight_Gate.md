# Cone Derivation Ledger v15.097 — Lane A: two-index symmetry restricts diagonal Hilbert weights for K_full

**Date:** 2026-10-29. **Track:** Lane A / Suzuki. **Parents:** v14.967/969 (repaired spike kernel), v15.018/019 (audited Hilbert-completion provenance obstruction), v15.095 (source-faithful Gram/intertwining gate). **Scope:** exact algebraic necessary condition; no realization/spectral construction.

**HEAD/collision:** immediately before writing, live master HEAD `c4536176451f38564d6a239622e2ae9717104be1` (gravity v15.096), v15.097 free. No existing certificates, code, or threshold modified.

## Gate 1: exact exchange symmetry

The frozen off-diagonal physical matrix on one parity sector, for two *distinct* physical modes n,m, is
`K[n,m]=c*(m*z_n-n*z_m)/(n*n-m*m)`.
Both z values are physical, real and sector-fixed. Exchanging n,m negates both numerator and denominator, hence
`K[n,m]=K[m,n]`
exactly, independently of z's detailed form. This is an algebraic reciprocity identity, not a self-adjointness proof. A real symmetric rank-one pole term of form alpha*p_n*p_m is compatible with the same symmetry when present; the precise definition of K_full must be checked before extending a statement to any added diagonal or cross-sector coupling.

## Gate 2: diagonal-weight symmetry condition

On `H_w=ell2(w)` with positive diagonal weights, and a domain containing the two finitely supported basis vectors, symmetry on the pair requires
`w_n K[n,m] = w_m conjugate(K[m,n])`.
For the real symmetric offdiagonal entry this reduces to
`(w_n-w_m)*K[n,m]=0`.
Therefore every nonzero edge in the undirected interaction graph forces equality of its endpoint weights; weights are constant on each connected component. In particular `w_n=n` fails whenever a pair of distinct indices has nonzero coupling. The audited v15.018 spike at m1 has K[N,m1] nonzero for **every sufficiently large** N, hence any weighted symmetric candidate whose domain includes that spike and those output basis vectors must have `w_N=w_m1` for all sufficiently large N. Thus a power weight w_N=N^(2a) is ruled out for every a !=0, on that sector/core, as a *symmetric* realization of this unchanged matrix.

This strengthens the v15.018 **non-uniqueness-of-provenance** discussion by identifying a necessary candidate weight shape, but does not furnish a canonical norm from Suzuki's original energy-space construction. Nor does it rule out a non-diagonal Gram matrix, a domain excluding the proposed core, or a different operator related by an actual unitary conjugation. The old weight-N comparison in v15.018 remains a legitimate witness that algebraic data alone did not specify the completion; it is not being promoted as a symmetric candidate.

## Gate 3: source-faithful Gram obstruction/test

For a source-native synthesis J from coefficient vectors to Suzuki's finite-a energy space, compute `G[m,k]=<Je_m,Je_k>` and verify the operator pairing. If G is diagonal and a symmetric unchanged matrix is claimed on a common core, the above reciprocity condition forces eventual equal weights along the certified spike star. If G is non-diagonal, the correct identity is the matrix equation `GK=K^*G` on finitely supported test vectors where both sides are well-defined; finite truncations do not justify the infinite products without domain/integrability checks. The finite Suzuki boundary triple of v13.661 and the source transfer bar D of v13.662/785 are not themselves a map J to K_full.

**Next focused HANDOFF** target: Sandbox / External Audit; type: source-native-Gram-and-2x2-bridge; parent: v15.097; status: OPEN_RESEARCH. Independently confirm the exchange-symmetry and weight consequence directly against the frozen physical kernel, then attempt a source-native synthesis/Gram calculation for the certified spike and one nonzero partner using genuine Suzuki energy inner products; report an exact match or precise obstruction with reproducible code/hashes. Do not fit weights to eigenvalues or launch far numerical production.

**Fence:** K_full scoped provenance obstruction remains; no operator realization, self-adjointness, spectral measure, F1/F2 rerun, residual consumer, stationary pair, or capacity conclusion. Original C_S_32000 and all thresholds unchanged, no transport/self charges repeated.
