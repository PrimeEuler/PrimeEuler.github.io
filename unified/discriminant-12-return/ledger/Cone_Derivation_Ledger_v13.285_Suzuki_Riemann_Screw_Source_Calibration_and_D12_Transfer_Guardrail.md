# Cone Derivation Ledger v13.285 — Suzuki Riemann Screw Source Calibration and D12 Transfer Guardrail

Date: 2026-09-07

Status: PRIMARY-SOURCE KERNEL CALIBRATION + RIEMANN CONTROL IMPLEMENTATION — D12 TRANSFER NOT YET NUMERICALLY CLAIMED — GRH NOT PROVED

## 0. Synchronization

Immediately before the write, the authoritative README and `master` tip were re-fetched.  The tip was `acf41e04843d7d75860ae157454590f9824fee3b`, containing the new Riemann calibration script and no newer external-audit checkpoint.

The primary source is Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v2, especially equations (1.3), (2.2), (8.1), and Sections 8.1–8.3.

---

## 1. Exact Suzuki Riemann screw function

Suzuki's current v2 gives the continuous real even screw function

\[
\boxed{
\begin{aligned}
g_\zeta(t)=&-4(e^{|t|/2}+e^{-|t|/2}-2)\\
&+\sum_{n\le e^{|t|}}\frac{\Lambda(n)}{\sqrt n}(|t|-\log n)\\
&-\frac{|t|}{2}\bigl(\psi(1/4)-\log\pi\bigr)\\
&-\frac14\left[\Phi(1,2,1/4)-e^{-|t|/2}\Phi(e^{-2|t|},2,1/4)\right].
\end{aligned}}
\]

This is equation (1.3) of the source.  It gives a direct source-faithful kernel for calibrating the Section-8 numerical machinery before any D12 modification is introduced.

We separate it as

\[
\boxed{g_\zeta=g_{\rm pole}+g_{\rm prime}+g_{\Gamma}.}
\]

The three pieces are

\[
g_{\rm pole}(t)=-4(e^{|t|/2}+e^{-|t|/2}-2),
\]

\[
g_{\rm prime}(t)=\sum_{n\le e^{|t|}}\frac{\Lambda(n)}{\sqrt n}(|t|-\log n),
\]

and

\[
\begin{aligned}
g_\Gamma(t)=&-\frac{|t|}{2}(\psi(1/4)-\log\pi)\\
&-\frac14\left[\Phi(1,2,1/4)-e^{-|t|/2}\Phi(e^{-2|t|},2,1/4)\right].
\end{aligned}
\]

Every piece is even.  Also `g_zeta(0)=0` by continuity and direct cancellation.

---

## 2. Near-origin source check

Suzuki derives

\[
\boxed{
g_\zeta(t)=\frac12|t|\log|t|+A|t|+g_{\rm prime}(t)+r(t),
}
\]

where

\[
A=\frac12(\log(2\pi)+\gamma-1)
\]

and `r` is even, `C^2`, with

\[
r(t)=O(t^2).
\]

For sufficiently small `|t|`, before the first prime breakpoint, `g_prime=0`.  Therefore a source calibration must satisfy

\[
\boxed{
g_\zeta(t)-\left(\frac12|t|\log|t|+A|t|\right)=O(t^2).}
\]

This is a much stronger test than merely checking continuity or evenness: it tests the delicate cancellation in the Hurwitz-Lerch term.

---

## 3. New calibration implementation

Added

`research-notes/suzuki_riemann_screw_calibration.py`.

It implements equation (1.3) directly, with the pole, prime-ramp, and archimedean terms exposed as separate functions.

The Hurwitz-Lerch expression is evaluated at elevated precision with `mpmath`, because near `t=0` the source formula contains substantial cancellation.  The exact continuous value `g(0)=0` is imposed at the origin rather than evaluating a numerically singular `z -> 1` representation.

The implementation also enumerates all Riemann prime powers satisfying

\[
\boxed{\log(p^k)\le |t|,}
\]

so there is no silent replacement of the source cutoff by a prime-only cutoff.

---

## 4. Why this control experiment is mandatory

The D12 Nyström prototype in v13.284 deliberately left the reduced archimedean screw kernel injectable.  This was the correct choice: the first numerical target should not be D12 itself, but Suzuki's exact Riemann kernel.

The control sequence is now

\[
\boxed{
\text{Suzuki (1.3)}
\to
\text{Riemann continuous kernel}
\to
\text{Section-8 Fredholm discretization}
\to
\text{finite characteristic diagnostics}
\to
\text{D12 transfer}.
}
\]

A D12 numerical result is not to be trusted until the same quadrature, parity reduction, endpoint handling, and differentiation-back diagnostics behave correctly on the Riemann control problem.

---

## 5. Exact Section-8 operator used for the control

Suzuki defines

\[
G_a=P_aGP_a
\]

on the mean-zero subspace and

\[
\boxed{S_a=G_a-\lambda K_a,}
\]

where

\[
K_a=(-\Delta_N)^{-1}
\]

has kernel

\[
\boxed{
N_a(x,y)=\frac{x^2+y^2}{4a}-\frac{|x-y|}{2}+\frac a6.
}
\]

Thus the source-faithful Riemann continuous kernel entering the control problem is

\[
\boxed{
k_{\zeta,a,\lambda}(x,y)=g_\zeta(x-y)-\lambda N_a(x,y),}
\]

with the understanding that the mean-zero projection is part of Suzuki's `G_a` construction.

The simultaneous reflection symmetry is exact:

\[
\boxed{k_{\zeta,a,\lambda}(-x,-y)=k_{\zeta,a,\lambda}(x,y).}
\]

Hence the parity-reduction machinery of v13.283–v13.284 applies to the Riemann control without modification.

---

## 6. Prime breakpoints are source-exact

Equation (1.3) shows directly that the prime-power ramp has kinks at

\[
\boxed{|t|=\log(p^k).}
\]

On the finite interval, `t=x-y`; for fixed collocation row `x`, the integration variable therefore meets breakpoints at

\[
\boxed{y=x\pm\log(p^k),}
\]

whenever these lie in the integration interval.

After half-interval parity compression, reflected terms add the corresponding `x+y` breakpoints.  Therefore the breakpoint-aware product integration proposed in v13.284 is not merely a numerical refinement: it is aligned exactly with Suzuki's source formula.

---

## 7. D12 transfer guardrail

The Riemann source formula now fixes the normalization conventions against which the D12 archimedean/conductor decomposition must be derived.

In particular, we do **not** infer the sign or coefficient of the D12 conductor contribution merely from a heuristic logarithmic-derivative argument.  The D12 screw function must be derived in the same normalization as Suzuki (1.3), preferably from the completed factorization

\[
\xi_K(s)=\xi(s)\,\Lambda(s,\chi_{12})
\]

with all normalization constants tracked through the twice-integrated explicit formula.

This guardrail is important because a linear `|t|` term becomes a scalar contribution after applying `D^* G D`, so a sign or factor error at the screw level would become a spectral shift error in the Section-8 generalized eigenvalue problem.

Accordingly, earlier project statements about the conductor becoming a scalar shift remain a structural target, but the **source-normalized coefficient is to be re-audited against equation (1.3) before the first D12 numerical run**.

---

## 8. Calibration invariants before coupling to Nyström

The Riemann kernel implementation should satisfy, to numerical precision,

\[
\boxed{g_\zeta(0)=0,}
\]

\[
\boxed{g_\zeta(t)=g_\zeta(-t),}
\]

and, before the first prime breakpoint,

\[
\boxed{
\frac{g_\zeta(t)-\frac12|t|\log|t|-A|t|}{t^2}=O(1).
}
\]

At every prime-power breakpoint `T=log(p^k)`, the function itself remains continuous while its first derivative has the expected finite jump inherited from the ramp.

These checks distinguish source-evaluation errors from Fredholm-discretization errors.

---

## 9. Next implementation step

The next step is now precise:

1. couple `g_suzuki` to the parity-reduced Nyström machinery;
2. implement row-wise splitting at all `y=x±log(p^k)` and reflected breakpoints;
3. compare global GLL quadrature against breakpoint-aware quadrature;
4. enforce the endpoint/parity constraints from v13.284;
5. differentiate the reconstructed first-kind solution back to Suzuki's original deficiency equation away from the kink set;
6. only after the Riemann control passes, derive and insert the source-normalized D12 screw kernel.

The important conceptual advance is that there is now no unknown Riemann archimedean kernel in the numerical chain: it is equation (1.3) verbatim.

---

## 10. Status

Established here:

\[
\boxed{
\text{exact Suzuki Riemann continuous kernel is now implemented as the control baseline.}
}
\]

Not established:

- convergence of the Nyström scheme;
- convergence of finite Suzuki characteristic functions;
- the source-normalized D12 conductor coefficient in the screw kernel;
- RH or GRH.

The immediate research frontier is therefore numerical/operator calibration against Suzuki's own Riemann model, followed by a normalization-audited D12 transfer.