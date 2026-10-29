# Cone Derivation Ledger v15.129 — Lane A: essential self-adjointness of the counting-measure K_full minimal operator

**Date:** 2026-10-29. **Lane:** A / Suzuki. **Parents:** v14.967/969, v15.018/019, v15.097, v15.106, v15.125–126, v15.128. **Status:** [D] essential self-adjointness in the explicitly CHOSEN plain ell2 completion, subject to the full kernel identity and certified bounded z; [O] canonical Suzuki-source identification and physical far residual.

**Collision:** immediately before deposit, live master HEAD `630f10da95b14c273eeda13c1de5cb2261f722da` (v15.128); v15.129 next free.

## Exact bounded offdiagonal decomposition

On each positive physical parity lattice n=2j+s (s=1 or 2, with any fixed lower cutoff), v15.106 fixes real symmetric full matrix

`K[n,m]= c*(m*z_n-n*z_m)/(n²-m²)+2*sigma*p_n*p_m` for n!=m, and `K[n,n]=d_n+2*sigma*p_n²`.

The algebraic identity for distinct n,m is

`(m*z_n-n*z_m)/(n²-m²) = (1/2)*[(z_n-z_m)/(n-m) - (z_n+z_m)/(n+m)]`.

Define Hminus[n,m]=1/(n-m) for n!=m and zero on diagonal; Hplus[n,m]=1/(n+m) for all n,m, and Z=diag(z_n). The offdiagonal non-pole part is exactly

`B0=(c/2)*(Z Hminus-Hminus Z-Z Hplus-Hplus Z+diag(2*z_n/(2*n)))`.

Here the diagonal correction `diag(z_n/n)` inside the final parentheses restores zero diagonal, because `(Z Hplus+Hplus Z)[n,n]=z_n/n`. The signs and factor of the correction are essential. Thus `B0[n,n]=0`; offdiagonal formula as required.

After identifying n=2j+s, Hminus is half the standard discrete Hilbert transform kernel 1/(j-k) and is bounded on ell2 by norm at most pi/2 (compression of the bilateral convolution discrete Hilbert transform). Hplus is the positive Hilbert matrix kernel 1/[2(j+k+s)] (after reindexing the parity lattice from its nonnegative start), a positive shifted Hilbert matrix or compression with norm at most pi/2, by the standard Hilbert inequality (the actual large starting physical mode only decreases entries). Z has norm <= Zbar from the certified remote physical z bound. Also `||diag(z_n/n)||<= Zbar/n_min`. Therefore

`||B0|| <= (|c|/2)*(4*Zbar*(pi/2)+Zbar/n_min) = |c|*pi*Zbar + |c|*Zbar/(2*n_min)`.

Alternatively, the harmless correction can be absorbed into the real diagonal operator; its inclusion here makes B0 exactly zero diagonal.

The full pole operator `P=2*sigma*|p><p|` is bounded self-adjoint since the exact-floor p_n satisfies 0<=p_n<=L/n, hence p in ell2. Its norm is <= 2*|sigma|*||p||².

Set D=diag(d_n) with maximal diagonal domain `D(D)={x in ell2: (d_n x_n) in ell2}`, where each d_n is finite and real as in the frozen original physical diagonal. D is self-adjoint and c00 is its graph core by coordinate truncation, regardless of the growth or oscillation of d_n. Since B=B0+P is a bounded self-adjoint operator, the bounded-perturbation theorem gives D+B self-adjoint on D(D), and c00 is still a graph core because graph norms of D and D+B are equivalent. On c00, D+B equals the exact frozen K_min. Hence

`closure(K_min) = D+B` is self-adjoint, and **K_min is essentially self-adjoint on c00**, independently in both parity sectors and on their direct sum.

This upgrades v15.126's mere existence of one extension to uniqueness *in this explicitly imposed unweighted counting measure*. It does NOT prove that unweighted ell2 is uniquely/canonically induced by Suzuki's finite-a construction; v15.125's missing source-indexed synthesis remains the block to that claim.

## Independent-audit requests

1. Re-derive numerator splitting and the offdiagonal diagonal-restoration sign/factor above; check finite 2x2 examples.
2. Verify both operator bounds on the half parity lattice and exact floor p in ell2, including true diagonal convention and any indexing/pole normalization.
3. Verify c00 is a core for D, graph-core stability under bounded perturbations, and the precise plain-ell2 (not source canonical) scope.
4. If original frozen K definition differs from v15.106 on any rows, flag immediately and withhold promotion.

**HANDOFF**
target: external-audit
type: Kfull-plain-l2-essential-selfadjointness
parent: v15.129
status: OPEN_AUDIT
action: verify full bounded-perturbation proof; do not infer Suzuki canonical spectral identification.
deliverable: independent derivation and correction if needed.

**Fence:** no corrected far F1/F2, v14.406 consumer, stationary pair or capacity closure; C_S_32000, 3e-5 and .002 thresholds and charge-once transport remain untouched.
