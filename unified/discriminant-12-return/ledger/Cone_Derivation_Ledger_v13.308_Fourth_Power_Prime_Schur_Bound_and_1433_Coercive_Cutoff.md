# Cone Derivation Ledger v13.308 — Fourth-Power Prime Schur Bound and 1433 Coercive Cutoff

## Scope
This checkpoint continues the Suzuki \(a=1\), even-\(v\) operator audit.  It sharpens the joint prime-shift norm by applying the positive-kernel Schur argument to \(A^4\), where

\[
A=-B_{\rm prime}=\sum_{q\in\{2,3,4,5,7\}} \frac{\Lambda(q)}{\sqrt q}\,S_{\log q}.
\]

No RH/GRH, kernel, or \(\lambda_1=0\) claim is made.

## Positive-kernel power bound
Because \(A\) is self-adjoint with nonnegative kernel,

\[
\|B_{\rm prime}\|=\|A\|,
\qquad
\|A\|^4=\|A^4\|.
\]

Schur applied to \(A^4\) gives

\[
\|A\|\le \left(\sup_{x\in[-1,1]} (A^4\mathbf 1)(x)\right)^{1/4}.
\]

The functions \(A^k\mathbf1\) are piecewise constant.  Their breakpoints are generated exactly by shifting the preceding breakpoint set by the finite family \(\pm\log q\) and retaining points in \([-1,1]\).  Hence each supremum reduces to a finite interval sweep.

The first four iterates give:

- \(k=1\): 11 intervals, \(\sup A\mathbf1=2.9262341821764086\), root bound \(2.9262341821764086\).
- \(k=2\): 31 intervals, \(\sup A^2\mathbf1=6.054238008078117\), root bound \(2.460536122083583\).
- \(k=3\): 59 intervals, \(\sup A^3\mathbf1=12.692957889252241\), root bound \(2.3326752407353215\).
- \(k=4\): 101 intervals, \(\sup A^4\mathbf1=25.69449057762533\), root bound

\[
\boxed{\|B_{\rm prime}\|\le 2.2514380572859216.}
\]

The reduction to the finite breakpoint maximum is exact.  The displayed decimal evaluation is ordinary floating point, not interval arithmetic.

## Tail coercivity update
Using the v13.304/v13.307 decomposition

\[
A_{\rm even}
=
D_{\log}-H_{\rm odd}+K_{\rm cusp}+B_{\rm prime}+K_{\rm smooth},
\]

with

\[
\|H_{\rm odd}\|=\frac\pi2,
\]

the fully analytic archimedean remainder bound

\[
\|K_{\rm arch\,rem}\|\le 2.0563386856144006,
\]

and the localized cusp/pole estimates, the tail inequality is

\[
\langle A_{\rm even}c,c\rangle
\ge
\bigl[\log(N/4)-C_{\rm tail}(N)\bigr]\|c\|_2^2.
\]

The first sufficient odd cutoff with the fourth-power prime bound is

\[
\boxed{N=1433.}
\]

At this cutoff:

\[
\|P_NK_{\rm cusp}P_N\|\lesssim 7.3122324438\times10^{-5},
\]

\[
\|P_NK_{\rm pole}P_N\|\lesssim 1.4404888224\times10^{-3},
\]

and the lower-bound margin is approximately

\[
1.1443858662\times10^{-3}>0.
\]

Thus the explicit sufficient cutoff has progressed

\[
5.56\times10^6
\to52363
\to3441
\to2809
\to1765
\to\boxed{1433}.
\]

## Interpretation
The prime-shift norm remains the largest improvable permanent term.  The power-Schur sequence is monotonically tightening toward the numerical Galerkin edge near \(1.94\), but no convergence theorem or certified limiting norm is claimed here.

A natural next checkpoint is to push the same exact piecewise-constant recursion to \(A^8\) and compare the gain against the growth of the breakpoint set, or to interval-certify the \(A^4\) finite maximum.

## Reproducibility
Script:

`research-notes/suzuki_joint_prime_fourth_power_schur.py`
