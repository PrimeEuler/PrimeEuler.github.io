# Cone Derivation Ledger v15.139 — Lane A: noncompact off-diagonal kernel and perturbation-norm cutoff obstruction

**Date:** 2026-10-29. **Track:** Lane A / Suzuki. **Parents:** v15.106 (exact frozen full kernel), v15.129–130 (audited in External Audit R405/v15.132), v15.136. **Status:** [D] offdiagonal perturbation noncompact for the exact physical five-frequency z; [D] diagonal-preserving finite cutoffs cannot converge in norm as perturbations, norm-resolvent convergence remains open. [O] essential spectrum and canonical source provenance.

**Pre-write HEAD/collision check:** live master `1188daf47f018cbdb716ba8de4441fa992f4bb96` (gravity v15.138); v15.139 next free. No source/buffer edits.

## 1. Persistent near-diagonal coefficient

Use physical modes n with step 2 in either parity and the exact full offdiagonal
`K[n,m]=c*(m*z_n-n*z_m)/(n²-m²)+2*sigma*p_n*p_m` (n != m).
For m=n and output n+2, algebra yields
`K[n+2,n]=c*[n*z_{n+2}-(n+2)*z_n]/[4(n+1)]+2*sigma*p_{n+2}p_n
=(c/4)*(z_{n+2}-z_n)+O(1/n)`,
using uniform z boundedness and p_n=O(1/n). The rank-one term is O(n^-2). This is an **exact leading identity on the moving adjacent diagonal**; fixed-input far asymptotics such as v15.018 are not sufficient here.

## 2. The oscillation does not decay

The source-faithful remote-z formula in `research-notes/suzuki_certified_remote_z.py` has the physical form, with fixed parity,
`z_n = pi/2 + sum_{q in {2,3,4,5,7}} 2 w_q sin(theta_q*n) + O(1/n)`,
where `w_q=log(q)/sqrt(q)>0` (for q=4 the equivalent w_4=log(2)/2) and `theta_q=(pi/2)*log(q)`; the precise nonprime evaluator supplies the O(1/n) remainder. Thus
`Delta z_n=z_{n+2}-z_n=sum_q 4 w_q sin(theta_q) cos(theta_q*(n+1))+O(1/n)`.
No `sin(theta_q)` vanishes: this would require log(q) to be an even integer, impossible for integer q>1 by the transcendence of e^{nonzero algebraic}. On the step-two n-lattice, these trigonometric frequencies are distinct modulo sign and 2pi: a collision would force `log(q/r)` or `log(qr)` to be an even integer, impossible unless q=r and the integer is 0. The same reasoning rules out zero-frequency self resonances. Hence Cesàro orthogonality of distinct nonresonant exponentials gives

`lim_{J->infty} (1/J) sum_{j=0}^{J-1} |Delta z_{n0+2j}|² = 8*sum_q w_q² sin²(theta_q) > 0`.

In particular Delta z_n does **not** tend to zero on either parity lattice. So there is a positive subsequential lower bound on |K[n+2,n]|.

The proof uses the exact physical unrounded z, not finite-precision floating point; frozen exact-floor p remains harmless since p_n<=L/n (and eventually zero). If physical z were altered to an exactly quantized/rounded infinite sequence, verify its asymptotic against the source before applying this statement; the producer computes enclosures of physical z, not a new physical definition.

## 3. Noncompactness and a quantitative cutoff consequence

Let `B=K-D` be the bounded self-adjoint perturbation from v15.129, including the offdiagonal and rank-one pole, with D the exact physical real diagonal. The unit vectors e_n converge weakly to zero in ell2. For a compact operator B one must have ||B e_n|| ->0; but
`||B e_n|| >= |<e_{n+2},B e_n>|=|K[n+2,n]|`
has a positive limsup. Therefore **B is not compact** in either parity sector.

For `P_R` any finite-coordinate projection and `B_R=P_R B P_R`, choose n beyond its range. Then B_R e_n=0, giving
`||B-B_R|| >= ||B e_n||`. The preceding persistent positive subsequential bound implies `inf_R ||B-B_R|| > 0`; hence no norm convergence of the perturbations, although v15.130's strong convergence and strong-resolvent convergence remain valid.

For the resolvents `R_R(z)=(D+B_R-z)^-1` and `R(z)=(D+B-z)^-1`, **do not automatically infer a norm-resolvent obstruction from the failure of ||B-B_R||->0 when D is unbounded**: resolvents can damp the high-index modes. A separate diagonal-growth analysis is required. This corrects the overly broad provisional wording in the status/header and explicitly leaves norm-resolvent convergence **OPEN**. The noncompactness theorem is independent of that open question.

## 4. Next gate and audit

1. Audit the exact five-frequency asymptotic and its step-two Cesaro mean-square proof, checking `w_4` normalization from the actual physical source; note the special q=4 weight is **log 2 / 2**, whereas the generic log4/sqrt4 is log2, so use the special value in the sum.
2. Analyze whether |d_n| -> infinity, or whether its diagonal has infinitely many bounded values, to determine if the diagonal resolvent damps the persistent near-diagonal coupling. Do not conflate operator norm with norm resolvent.
3. If a norm-resolvent obstruction remains, construct a certified tail localized quasimode. If not, prove compactness of the resolvent difference using diagonal growth and bounded B.

**HANDOFF**
target: external-audit / sandbox
type: noncompact-near-diagonal-and-resolvent-tail
parent: v15.139
status: OPEN_AUDIT
action: verify source phase/weight and noncompactness; separately examine diagonal-growth/norm-resolvent question.
deliverable: reviewed theorem and precise next gate.

**Scope:** canonical Suzuki source synthesis remains absent; far F1/F2 NOT PASSED, no residual consumer, stationarity or capacity conclusion; frozen C_S_32000, 3e-5, .002 and charge-once bookkeeping untouched.
