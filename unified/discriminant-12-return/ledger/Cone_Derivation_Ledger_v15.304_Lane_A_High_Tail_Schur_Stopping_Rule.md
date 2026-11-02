# Cone Derivation Ledger v15.304 — Lane A: explicit finite stopping rule for high-tail Schur certification

Date: 2026-11-02. Lane A. Parents: v15.129/141, v15.227, v15.303. Status [D] conditional full-K reduction to a finite Schur matrix with explicit high-tail bounds and computable stopping rule; [O] practical-scale implementation and certified finite inertia. No Sandbox invocation.

## Exact split and norm data

In chosen counting-measure ell2 let K=D+B, with real physical diagonal d_n and bounded self-adjoint B. The source's certified uniform diagonal envelope gives d_n >= log(n/4)-C for n>=n0, with C=1.745855454249828 as cited in v15.227; using a conservative outward C=2 is permitted when its source certification is retained. The audited global ||B||<=M=15 is adequate but loose.

Let P_N be projection onto all parity modes n<=N (including the physical starting mode); Q_N=I-P_N. Define
A_N=P_N K P_N, V_N=Q_N B P_N, T_N=Q_N K Q_N=D_Q+Q B Q.
Write m_N=log((N+2)/4)-C for the next parity index, and M_N an independently justified norm bound for Q B Q, with M_N<=M.

For a declared real spectral interval [a,b], if
g_N=m_N-b-M_N>0,
then T_N-x >=g_N I for all x in [a,b]. Therefore:
(a) [a,b] subset rho(T_N);
(b) n_-(T_N-x)=0 throughout;
(c) ||(T_N-x)^-1||<=1/g_N.

The exact full-K inertia equals n_-(F_N(x)), where
F_N(x)=A_N-x - V_N* (T_N-x)^-1 V_N.
The strict endpoint-inertia/monotonicity criterion of v15.303 then decides full-K eigenvalue counts on [a,b]. This eliminates the earlier problem of ignoring tail eigenvalues, because the choice of N now **certifies** absence of negative tail directions at the target energy.

## Certified diagonal tail inverse with remainder

For x in [a,b], define R_D,N(x)=(D_Q-x)^-1, with
tau_N=1/(m_N-b) and alpha_N=M_N*tau_N<1.
A norm-convergent resolvent series for T_N gives
||(T_N-x)^-1-R_D,N(x)|| <= M_N*tau_N²/(1-alpha_N).

Consequently the computable diagonal-tail Schur proxy
Fhat_N(x)=A_N-x - V_N* R_D,N(x) V_N
has operator-norm error
epsilon_F<=||V_N||² M_N*tau_N²/(1-alpha_N) <= M² M_N*tau_N²/(1-alpha_N).

For certified finite-matrix eigenvalue intervals widened by epsilon_F, a strict exclusion of zero certifies invertibility of F_N at that x. Endpoint inertia agreement together with the exact monotonicity F_N'(x)<=-I_N certifies a gap; different endpoint inertias give the exact eigenvalue count within (a,b) (with endpoints invertible).

NOTE: Fhat_N is still a finite matrix but computing V_N*R_D,N V_N requires the **infinite diagonal-weighted tail sum**. It must be computed with an outward-certified remainder, not truncated silently. One can instead use A_N-x itself with the coarser bound ||V_N||²/g_N, avoiding that infinite sum entirely. This produces a fully finite, if conservative, acceptance test:
||F_N(x)-(A_N-x)|| <= ||V_N||²/g_N <= M²/g_N.
Exact interval inertia of A_N-x can then be promoted if all its finite eigenvalue intervals are separated from zero by more than M²/g_N.

## Explicit (not necessarily affordable) stopping criterion

The simple certified global choice M_N=M=15 and C=2 gives sufficient
log((N+2)/4) > b+17,
or N+2 > 4 exp(b+17).
For b about 10.45, this scale is ~3.3e12 in physical mode index (order 1e12 modes at step two), **not** the v15.227 order-1.4e5 strategy. Thus the theorem proves a finite possible stopping rule, but DOES NOT claim a practical computation or resolve the resource budget. Tight sector-specific estimates M_N, structured block preconditioning, or a different coupled-tail enclosure are needed for affordability.

The v15.227 order-1.4e5 scale only absorbs modes whose *diagonal* may be close to b under C~1.746. It does not itself establish T_N-b>0 when the coupling norm is as large as 15. This distinction must not be collapsed.

## Next direct Lane A gate

Determine an explicit strict upper bound for ||Q_N B Q_N|| using the actual five-frequency kernel, ideally substantially below global M, and an offblock bound ||V_N||. Any improvement yields a smaller finite stopping rule and sharper Schur residual. No source canonical identification or v14.406 replay.

Existing v14.405/v14.406 PASS and later v14.814 far FAIL preserved. C_S_32000, 3e-5 and .002 thresholds and charge-once accounting untouched. Full-K physical transfer remains INCONCLUSIVE until actual certified data exist.
