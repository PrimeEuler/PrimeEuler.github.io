# Cone Derivation Ledger v15.130 — Lane A: strong-resolvent finite-cutoff convergence for the chosen plain-ell2 realization

**Date:** 2026-10-29. **Lane:** A / Suzuki. **Parents:** v15.125–126, v15.129 (essential SA proof awaiting independent audit). **Status:** [D, conditional on v15.129's verified bounded B] strong-resolvent convergence and explicit vector error bound; [O] norm-resolvent convergence, canonical Suzuki provenance, physical residual.

**Collision check:** immediately before deposit live master HEAD `ae5f467a05cf1690693383f1435eca99e95bac11` (v15.129); v15.130 next free.

## The correct approximants

Fix the **chosen, noncanonical** counting-measure Hilbert space H=ell2 on one parity lattice or their direct sum. Let K=D+B on Dom(D), with D real diagonal self-adjoint and B the **full bounded symmetric off-diagonal-plus-pole** operator of v15.129. Write P_R for an increasing sequence of finite-coordinate orthogonal projections satisfying P_R -> I strongly. Define

`B_R=P_R B P_R`,
`K_R=D+B_R` on Dom(D).

Crucially, this is the full-space diagonal-preserving truncation; the literal finite numerical matrix is its restriction to Ran P_R, whereas the remaining diagonal D acts on the complement. Every K_R is self-adjoint on Dom(D) by bounded perturbation. Since B is bounded, B_R -> B strongly: for any f,
`||(B-B_R)f|| <= ||(I-P_R)Bf|| + ||P_R B (I-P_R)f|| ->0`.
Also `||B_R||<=||B||` uniformly.

For nonreal z and fixed f, the second resolvent identity gives exactly

`(K_R-z)^(-1)f-(K-z)^(-1)f = (K_R-z)^(-1)(B-B_R)(K-z)^(-1)f`.

Thus the rigorous estimate

`||[(K_R-z)^(-1)-(K-z)^(-1)]f|| <= (1/|Im z|)*||(B-B_R)(K-z)^(-1)f|| ->0`.

Hence `K_R -> K` in **strong resolvent sense**, and bounded continuous functional calculus `g(K_R)f -> g(K)f` holds for g in C_0(R); it also holds for bounded continuous g under the corresponding standard strong-resolvent functional calculus theorem. In particular spectral measures converge weakly for fixed f (bounded continuous test functions), with no implication that isolated approximate eigenvalues or zeros individually converge without additional spectral isolation / no-pollution arguments.

## Distinguish finite computation from spectral certification

The finite Ritz matrix `P_R K P_R|_{Ran P_R}` is not by itself an operator on a fixed Hilbert space, so strong-resolvent language must refer to the diagonal-preserving extension K_R (or a separately justified embedding). It has a direct-sum complement `D|_{Ran(I-P_R)}`. Strong-resolvent convergence alone does NOT establish norm-resolvent convergence, convergence of every eigenvalue, absence of spectral pollution in gaps, any canonical projector onto a target Xi subspace, or a Suzuki-source spectral equivalence.

The v15.125 source-native Phi_a synthesis remains absent in the examined source base. Thus v15.018's canonical-provenance obstruction is NOT lifted. The v15.129 operator identification is an explicitly chosen counting-measure realization. The proof supplies a rigorous convergence statement conditional on the audited v15.129 boundedness/kernel identification, not a pass of frozen far residual gates.

## Audit and next gate

**HANDOFF**
target: external-audit
type: finite-cutoff-strong-resolvent
parent: v15.130
status: OPEN_AUDIT
action: independently check v15.129 exact Hilbert-transform/Hilbert-matrix splitting and physical pole/diagonal conventions, and the strong-resolvent argument above; flag any noncanonical-source extrapolation. Evaluate possible resolvent norm convergence only with additional tail/compactness assumptions, not by assertion.
deliverable: audited exact theorem scope and any corrections.

**Fence:** no v14.406 residual consumer, F1/F2 rerun, stationary/capacity conclusion; C_S_32000, 3e-5, .002 thresholds unchanged and charge-once transports untouched.
