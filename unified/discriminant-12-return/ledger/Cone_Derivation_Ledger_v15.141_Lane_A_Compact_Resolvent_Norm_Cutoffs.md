# Cone Derivation Ledger v15.141 — Lane A: compact resolvent and norm-resolvent finite cutoffs despite noncompact coupling

**Date:** 2026-10-29. **Lane:** A / Suzuki. **Parents:** physical diagonal v14.901/SEED_FORMULA.md; v15.106 kernel; v15.129–130 operator and strong-resolvent (verified External Audit R405/v15.132); v15.139 noncompactness (audit pending). **Status:** [D] compact resolvent, empty essential spectrum, and norm-resolvent convergence in deliberately chosen counting-measure ell2. [O] canonical Suzuki provenance, physical residual certification, numerical isolated spectral enclosure.

**Collision check:** immediately before write, live master HEAD `8cbf131a98d5f03ef19c2976c689002006445ddf`, ledger v15.140 next; v15.141 free. Additive only.

## 1. Frozen diagonal grows

Original generation-source reconstruction `payloads/far_coefficient_attribution_v14_901/SEED_FORMULA.md` states for both parity sectors `d_n=log(n/4)+cusp_n - sum_q w_q(2-log q)[cos(theta_q n)+(2/(n pi)) sin(theta_q n)] + O(1/n²)`, with `cusp_n=-1/(2n)+2(-1)^n/(n pi)^2`. The finitely many physical q weights are fixed and finite; bounded trig terms imply `d_n=log(n/4)+O(1)`, thus `d_n -> +infty` along each sector. This is a property of the original physical diagonal, not an artificially added confining potential. Source precision and any use of numerical bounds must be audited separately; the qualitative asymptotic is explicit in the existing producer formula.

## 2. Compact resolvent of the full counting-measure realization

By v15.129 (audited R405), on `H=ell2` the exact frozen operator closure is `K=D+B`, `D=diag(d_n)` self-adjoint on the maximal domain, and `B` bounded self-adjoint (noncompact by v15.139). For any z not real, `(D-z)^-1` is a compact diagonal operator since its diagonal entries `1/(d_n-z)->0`. The resolvent identity reads `(K-z)^-1=(D-z)^-1-(D-z)^-1 B (K-z)^-1`; the RHS is compact because the first factor in each term is compact. Thus `(K-z)^-1` is compact, even though B is not. The spectral theorem implies K has pure discrete spectrum, each eigenvalue finite multiplicity, no finite accumulation, and eigenvalues tending to +infinity (since D bounded below and B bounded).

This is a **chosen ell2** theorem, not a canonical Suzuki-source realization. v15.125's missing source-native Phi persists.

## 3. Norm-resolvent finite-section convergence

Let P_R be finite coordinate projection, B_R=P_R B P_R, K_R=D+B_R on Dom(D), as v15.130. By boundedness and P_R->I strongly, `B_R->B` strongly and `sup_R ||B-B_R|| <= 2||B||`. Set `T=(K-z)^-1` compact for z nonreal. A uniformly bounded strongly-null operator sequence `E_R=B-B_R` satisfies `||E_R T||->0` by uniform convergence on the compact image of the unit ball under T. The second resolvent identity gives

`||(K_R-z)^-1-(K-z)^-1|| <= (1/|Im z|)*||(B-B_R)(K-z)^-1|| -> 0`.

Thus **norm-resolvent convergence** holds, even though `||B-B_R||` fails to tend to zero (v15.139). This explicitly resolves that open question: the unbounded physical diagonal damps the noncompact high-mode near-diagonal interactions at the resolvent level. This argument also yields compact resolvents for every K_R and strong functional calculus of v15.130; norm convergence of continuous compactly supported functional calculus follows via standard norm-resolvent theory.

For a bounded contour gamma in the common resolvent set enclosing an isolated cluster and avoiding any spectrum, uniform norm convergence of resolvents on gamma gives norm convergence of Riesz spectral projections (self-adjoint setting, contour on complex plane). This supplies a **mathematically valid spectral projection route in chosen ell2**, distinct from Suzuki-source canonical identification, and does NOT produce the needed annihilation or v14.909 seed-preservation identities.

## 4. Correct scope / NEXT

The literal finite Ritz block `P_R K P_R` is only one summand in full-space K_R, whose complement remains diagonal `D|_{P_R^perp}`. For a fixed bounded spectral window, that complement eventually has no spectrum in the window because d_n->infty; then isolated-window spectral calculations reduce to the finite block, subject to a quantitative error bound on the omitted coupling. The qualitative norm-resolvent theorem alone provides no numerical threshold or specific physical projector.

**HANDOFF**
target: external-audit / sandbox
type: diagonal-growth-compact-resolvent-norm-cutoff
parent: v15.141
status: OPEN_AUDIT
action: verify original exact diagonal asymptotic, compact-resolvent proof, uniform norm-resolvent argument and contour projector scope. Derive an explicit numeric error bound for a target low-energy window if requested; no fitted zeros or source identifications.
deliverable: reviewed theorem with source formula and quantitative cutoff gate.

**Fence:** canonical K_full provenance remains CLOSED_SCOPED_OBSTRUCTION_CURRENT_FROZEN_DATA; no v14.406 consumer, corrected far F1/F2, stationarity, or capacity; C_S_32000, 3e-5, 0.002, and charge-once bookkeeping unchanged.
