# Cone Derivation Ledger v15.113 — Lane A: exact energy-versus-L2 Gram separation and certified exterior-tail criterion

**Date:** 2026-10-29. **Track:** Lane A / Suzuki. **Parents:** v13.661–662, v13.785, v15.018–021, v15.095–097, v15.106, v15.108, External Audit R402 v15.112. **Status:** [D] exact conditional Gram formulas, positivity and leakage estimate; [O] source-native synthesis and intertwiner existence.

**Collision check:** immediately before deposit, live master HEAD `cce45bbe34e8a32e4e577916689a0ade254e7025` (v15.112); v15.113 next free. Additive only, no existing numerical or Suzuki source payload touched.

## 1. Do not conflate source Hilbert norms

Suppose `T_a=A_a-lambda I` is the strictly positive self-adjoint finite-a Suzuki operator on its actual source L2 Hilbert space `H_a^0`; its inverse is bounded when `T_a>=epsilon_a I>0`. Given source functions `phi_m in H_a^0`, define the **candidate**, not yet a proven bridge, `f_m=T_a^{-1} phi_m`.

There are two distinct exact Gram identities:

- **L2 Gram:** `G^L2_{mk}=<f_m,f_k>_{H_a^0}=<phi_m,T_a^{-2}phi_k>_{H_a^0}`.
- **T-energy Gram:** if `H(T_a)` has the quadratic-form inner product `<f,g>_T=<T_a^(1/2)f,T_a^(1/2)g>_{H_a^0}`, then `G^E_{mk}=<f_m,f_k>_T=<phi_m,T_a^{-1}phi_k>_{H_a^0}`.

They are generally unequal. Both Gram matrices are positive semidefinite. For any finite coefficient vector v, `v*G^E v = ||T_a^(-1/2) sum v_m phi_m||² >=0`. Strict positivity requires that the chosen source functions are linearly independent in this image; it does not follow from merely labeling modes by n. If T_a has a different source-defined energy form, the exact form must be used rather than imposed by analogy.

## 2. Finite-block leakage estimate with explicit missing hypothesis

In v15.108, `G_II K_II-K_II*G_II = K_OI*G_OI-G_IO K_OI`. For `i,j in I`, let `u_j=(K_{oj})_{o in O}` and `g_i=(G_{oi})_{o in O}`. If both vectors are in the **same unweighted ell2** (or another specified dual-paired sequence space), the absolute exterior entry is bounded by

`|[K_OI*G_OI-G_IO K_OI]_{ij}| <= ||u_i||_2 ||g_j||_2 + ||g_i||_2 ||u_j||_2`.

This is just Cauchy–Schwarz, but it is **not** available merely from knowing finite principal Gram blocks. A Gram column `g_i` has to be shown ell2 on the exterior; `f_i in H` by itself need not imply this for a non-Bessel synthesis family. Likewise, if a source-native Gram requires a weighted/non-diagonal completion, the appropriate dual pairing must replace the formula. The audited frozen spike gives `u_j~1/o` and therefore an ell2 tail in the unweighted candidate; it does not certify `g_i in ell2`.

A sufficient concrete route is to prove the candidate synthesis `J:ell2 -> H_a` bounded, so `G=J*J` is bounded on ell2 and `g_i=G e_i in ell2`. This would permit tail norms `||P_O G e_i||_2` to be bounded and driven to zero for increasing finite windows, but **does not** prove `J` is an isometry or that `BJ=JK`. If J is unbounded, use direct column estimates instead.

## 3. Next handoff / acceptance test

Sandbox should first name the actual finite-a Suzuki source Hilbert space and T_a energy form, then specify the canonical `phi_m` from the source (if one exists). Compute the spike/partner Gram entries using the correct T^(-1) form, compare them to T^(-2) L2 entries as a guard against inadvertent norm substitution, and test whether J is a bounded synthesis or at least whether the required exterior Gram columns have certified decay. Only then assess the full intertwining identity with v15.108 leakage terms. Failing to find a source-native `phi_m` is a valid obstruction report: one must not choose `phi_m` to fit K.

**HANDOFF**
target: sandbox / external-audit
type: energy-Gram-and-exterior-column
parent: v15.113
status: OPEN_RESEARCH
action: certify source-native finite-a energy Gram for spike/partner and exterior decay (or obstruction); independently check T^-1 vs T^-2 distinction and the Cauchy-Schwarz leakage estimate; no far compute.
deliverable: source-faithful formulas, actual domain, replayable witness and hashes.

**Scope:** K_full provenance blocker remains, formal symmetry is not self-adjointness; no v14.406 residual consumer, revised F1/F2, stationary/capacity claim; original thresholds and charge-once bookkeeping untouched.
