# Cone Derivation Ledger v15.126 — Lane A: plain-ell2 minimal K_full operator is closable and admits self-adjoint extensions (noncanonical)

**Date:** 2026-10-29. **Lane:** A / Suzuki. **Parents:** v14.967/969 (physical kernel and exact-floor tail), v15.018/019 (provenance obstruction), v15.097, v15.106 (formal symmetry), v15.115–116 (energy Gram handoff/conditional bound), Sandbox v15.125 (no source-native synthesis in examined corpus). **Status:** [D] algebraic minimal operator well-defined on c00, closable, equal deficiency indices and at least one self-adjoint extension; [O] uniqueness, canonical extension, spectral matching, original residual.

**Collision check:** immediately before this write, live master HEAD `8bd31acc34df204bdda5ff572f37c5c390edaa2c`, latest ledger v15.125; v15.126 next free.

## 1. Define an actual minimal operator on an explicitly chosen Hilbert space

Fix one parity sector's discrete positive physical mode lattice `L`. **Choose**, rather than attribute to Suzuki, `H=ell2(L)` with counting measure. Let `K_min:c00(L)->H` be the frozen complete real matrix action, including original diagonal and rank-one pole:
for `n != m`,
`K[n,m] = c*(m*z_n-n*z_m)/(n²-m²) + 2*sigma*p_n*p_m`,
and `K[n,n]=d_n+2*sigma*p_n²`.
Here c, sigma, all z_n, p_n, d_n are finite real physical coefficients, `sup_n|z_n|<=Zbar<infty` (certified remote-z representation), and the original pole `p_n` obeys `|p_n|<= L/n + 2^-256` in the quantized convention. **More strongly, the exact-floor definition** `p_n=floor(2^256*L*n/(n²+t))/2^256` satisfies `p_n=0` whenever `n>=L*2^256` (v15.106), and in any case `0<=p_n<=L/n`. Hence `p in ell2(L)`.

For any fixed input m and all n>2m, `n²-m² >= (3/4)n²` and
`|c*(m*z_n-n*z_m)/(n²-m²)| <= (4|c|/3)*(m*Zbar/n² + |z_m|/n)`.
The corresponding offdiagonal column is square summable. The finitely many entries n<=2m are finite because n!=m and the parity lattice has no repeated physical index; the diagonal is one finite number. The pole column `2*sigma*p_m*p_n` belongs to ell2 since p is in ell2. Thus **every individual column** `K e_m` belongs to ell2, not just the previously certified spike, and finite linear combinations define `K_min:c00->ell2` legitimately.

## 2. Formal symmetry, closure and extension existence

The exact exchange identity gives `K[n,m]=K[m,n]` offdiagonal, the pole is symmetric, and diagonal real. Since finite vectors have finitely many coefficients and each column is in ell2, `<K_min x,y>=<x,K_min y>` for all x,y in c00. Therefore `K_min` is **densely defined symmetric**, hence closable; its closure is a closed symmetric operator.

All matrix coefficients are real, so ordinary componentwise conjugation `C` preserves c00 and `CK_min=K_min C`. Its closure has the same property; conjugation carries `ker(K_min^*-i)` antiunitarily onto `ker(K_min^*+i)`. Therefore the deficiency indices are equal (possibly infinite), and the standard von Neumann extension theorem guarantees **at least one** self-adjoint extension of the closure on this chosen ell2. The argument applies separately to both parity sectors and to their direct sum.

This is **not** a canonical extension theorem: neither the deficiency dimensions, essential self-adjointness, an extension parameter, nor the relation of any extension to Suzuki's original energy-space realization is decided. The spectral theorem applies to any *chosen* self-adjoint extension but supplies **no unique source-selected spectral measure or projection**. Thus v15.018/v15.021's provenance obstruction is not contradicted; this result proves an existence branch on an explicitly imposed counting-measure Hilbert space, not the canonical branch.

## 3. Scope and potential follow-up

An informative next gate is the essential self-adjointness of the natural minimal operator on `c00`, *within the deliberately chosen counting measure*. Even a positive result would not establish that this Hilbert completion and operator are the Suzuki canonical realization. A separate source-based norm/limit theorem remains mandatory to restore that identification.

**HANDOFF**
target: external-audit, sandbox
type: count-measure-Kmin-closability-and-extension
parent: v15.126
status: OPEN_AUDIT
action: independently verify the uniform physical z bound, exact floor pole ell2, all-column ell2 estimate and conjugation/deficiency argument; investigate essential self-adjointness only as a separate noncanonical mathematical question.
deliverable: verified theorem or corrected assumptions. No far production.

**Fence:** K_full canonical provenance gate remains CLOSED_SCOPED_OBSTRUCTION_CURRENT_FROZEN_DATA; no Suzuki coefficient synthesis manufactured, no unique spectral measure, v14.406, far F1/F2, stationary or capacity closure. Frozen C_S_32000, 3e-5, 0.002 and exactly-once charges untouched.
