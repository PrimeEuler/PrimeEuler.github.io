# Cone Derivation Ledger v13.286 — Breakpoint-Aware Riemann Control and Projective Characteristic Stability

Date: 2026-09-07

Status: SOURCE-FAITHFUL BREAKPOINT PRODUCT INTEGRATION + EXPLORATORY RIEMANN CONTROL DATA + NORMALIZATION GUARDRAIL — GRH NOT PROVED

## 0. Synchronization

Immediately before this write, the authoritative project README and current `master` tip were re-fetched. The tip was

`f9961de293f0f46b9dafc699ab08a7b31623cb3c`,

containing the new file

`research-notes/suzuki_riemann_breakpoint_control.py`,

with no newer external-audit checkpoint present.

The primary source remains Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v2. The control uses source equations (1.3), (2.2), (8.4), and (8.5).

---

## 1. Exact numerical target used here

Suzuki defines the Riemann screw function by equation (1.3),

\[
\begin{aligned}
g_\zeta(t)=&-4(e^{|t|/2}+e^{-|t|/2}-2)
+\sum_{n\le e^{|t|}}\frac{\Lambda(n)}{\sqrt n}(|t|-\log n)\\
&-\frac{|t|}{2}(\psi(1/4)-\log\pi)
-\frac14\left[\Phi(1,2,1/4)-e^{-|t|/2}\Phi(e^{-2|t|},2,1/4)\right].
\end{aligned}
\]

For Section 8,

\[
\boxed{k_{a,\lambda}(x,y)=g_\zeta(x-y)-\lambda N_a(x,y)}
\]

with

\[
\boxed{N_a(x,y)=\frac{x^2+y^2}{4a}-\frac{|x-y|}{2}+\frac a6.}
\]

The twice-integrated deficiency equations are

\[
\int_{-a}^{a}k(x,y)(-v_\pm(y))\,dy
=C_\pm e^{\pm x}+A_\pm x+B_\pm.
\]

This is exactly the formal first-kind Fredholm equation Suzuki proposes for numerical experimentation. As Suzuki emphasizes, it is not literally the same operator equation as the transferred equation in `H(S_a)` because the twice-integration argument suppresses domain issues.

---

## 2. Breakpoint-aware product integration

The global Gauss–Lobatto Nyström rule of v13.284 does not align with the exact nonsmooth set of the kernel. The new control instead represents `q_e,q_o` in the barycentric Lagrange basis on a common Legendre-Gauss-Lobatto node set, but computes each collocation row by separate Gauss-Legendre integrations on subintervals split at every exact row-wise nonsmooth point.

For fixed `x`, the split set contains

\[
\boxed{y=x}
\]

from the `|x-y|\log|x-y|` cusp and Neumann absolute value, together with all prime-power ramp crossings

\[
\boxed{y=x\pm\log(p^k)}
\]

that fall in `[0,a]`, plus the reflected parity-kernel crossings

\[
\boxed{y=\log(p^k)-x.}
\]

This is a product-integration scheme: on each smooth segment the kernel is evaluated directly and multiplied by the barycentric Lagrange basis before quadrature.

The implementation is

`research-notes/suzuki_riemann_breakpoint_control.py`.

---

## 3. Half-interval parity equations retained exactly

With the canonical real reflected basis and

\[
q_+=q_e+q_o,
\]

we retain

\[
\boxed{-\int_0^a K_e(x,y)q_e(y)\,dy=\cosh x+B_a,}
\]

\[
\boxed{-\int_0^a K_o(x,y)q_o(y)\,dy=\sinh x+A_ax,}
\]

where

\[
K_e(x,y)=k(x,y)+k(x,-y),
\qquad
K_o(x,y)=k(x,y)-k(x,-y).
\]

The exact trace constraints are imposed as before:

\[
q_e(a)=0,
\qquad
q_o(0)=q_o(a)=0.
\]

The odd `x=0` Fredholm row remains the exact identity `0=0` and is omitted.

---

## 4. Source-level kernel calibration passed

Independent local evaluation of the exact equation-(1.3) implementation gives, before the first prime breakpoint,

\[
g_\zeta(t)-\left(\frac12|t|\log|t|+A|t|\right)
\sim -0.875\,t^2,
\]

with

\[
A=\frac12(\log(2\pi)+\gamma-1).
\]

For example, the ratio of the remainder to `t^2` was approximately

\[
-0.87500043,\ -0.87500350,\ -0.87503707
\]

at `t=10^{-4},10^{-3},10^{-2}` respectively.

This numerically confirms Suzuki's source expansion

\[
\boxed{g_\zeta(t)=\frac12|t|\log|t|+A|t|+O(t^2)}
\]

in the no-prime neighborhood of the origin, including the delicate cancellation in the Hurwitz-Lerch term.

This is an exploratory numerical check, not a certified interval-arithmetic statement.

---

## 5. First breakpoint-aware Fredholm smoke study

A local execution of the same breakpoint-aware formulas was performed with

\[
a=1,
\qquad
\lambda=-5,
\qquad
\theta=\pi,
\]

using 6-point Gauss-Legendre integration on every exact row segment and 25-digit evaluation of the Hurwitz-Lerch term.

**Important qualification:** this smoke study does not independently certify

\[
\lambda=-5<\lambda_a.
\]

Therefore these numbers are diagnostics of the formal Fredholm discretization only; they are not yet claimed as a rigorously valid finite Suzuki self-adjoint-extension computation.

The observed data were:

| degree | cond even | cond odd | residual even | residual odd | A_a | B_a | W(1)/W(0.5) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 2.3071e2 | 5.5327e1 | 2.22e-15 | 3.33e-16 | -1.4867065 | -0.7317363 | 0.879098681 |
| 6 | 8.2337e2 | 1.6018e2 | 1.78e-15 | 1.33e-15 | -1.5147458 | -0.4917490 | 0.878016208 |
| 8 | 2.5529e3 | 3.5641e2 | 1.33e-15 | 2.66e-15 | -1.5242552 | -0.2224746 | 0.877724694 |
| 10 | 6.3508e3 | 7.7933e2 | comparable machine precision | comparable machine precision | -1.5278387 | 0.0679684 | 0.877652800 |

---

## 6. Main numerical finding: raw first-kind data are unstable, projective characteristic shape is much more stable

The condition numbers grow rapidly with degree, exactly as expected for a first-kind Fredholm discretization:

\[
\kappa_e: 2.3\times10^2\to6.35\times10^3,
\qquad
\kappa_o: 5.5\times10^1\to7.8\times10^2.
\]

At the same time, the affine constant `B_a` drifts substantially and the raw characteristic amplitude grows with degree. Thus a tiny collocation residual is not evidence that the reconstructed deficiency vector itself has converged strongly.

However, the normalization-free projective characteristic ratio

\[
\boxed{\frac{W_a(1)}{W_a(0.5)}}
\]

shows markedly better stability:

\[
0.879098681,
\quad
0.878016208,
\quad
0.877724694,
\quad
0.877652800.
\]

The degree-8 to degree-10 change is only about

\[
\boxed{7.2\times10^{-5}.}
\]

This does not prove convergence, but it supports the architectural choice made in v13.283–v13.284: the characteristic should be studied projectively, after eliminating the arbitrary overall deficiency normalization, rather than by demanding pointwise stability of the raw first-kind solution.

---

## 7. Exact real-axis phase constraint in the canonical reflected basis

There is also a new exact structural observation.

For real `z`, real `q_e,q_o`, and the canonical reflection convention,

\[
F_-(z)=\overline{F_+(z)}.
\]

At effective phase `Theta=pi`,

\[
W_a(z)
=(z-i)F_+(z)-(z+i)\overline{F_+(z)}.
\]

Writing `F_+(z)=u(z)+iv(z)` gives

\[
\boxed{W_a(z)=2i\bigl(zv(z)-u(z)\bigr),\qquad z\in\mathbb R.}
\]

Hence

\[
\boxed{W_a(z)\in i\mathbb R\quad\text{for real }z}
\]

and every same-phase normalized ratio

\[
\boxed{W_a(z)/W_a(z_*)\in\mathbb R}
\]

for real nonzero reference values.

This explains why the numerical ratios above are real to machine precision.

---

## 8. Consequence for the finite-to-infinite normalization problem

The current Suzuki-v2 target used in this branch is

\[
R_\zeta(z)
=
\frac{\xi(1/2-iz)}{\xi(1/2-iz)+\xi'(1/2-iz)}.
\]

On the real axis this target is generically not confined to one fixed complex line. For example, direct high-precision evaluation gives

\[
\frac{R_\zeta(1)}{R_\zeta(0.5)}
\approx
0.9989298628+0.0231207949i.
\]

Therefore, **if** the finite characteristic is expressed in the canonical real reflected basis with effective phase `Theta=pi`, a purely `z`-independent multiplicative constant cannot by itself transform its real projective ratios into the projective ratios of the Suzuki target.

The safe conclusion is

\[
\boxed{\text{finite phase convention and/or the }z\text{-dependence of }\phi(a,z)\text{ must be tracked explicitly.}}
\]

This weakens the earlier interpretation in v13.280 that Section 7 suggests only a scalar normalization should matter. The Section-7 infinite identity may indeed have only a fixed constant in its own canonical de Branges normalization, but that does **not** yet establish that the finite real Fredholm basis used here approaches that normalization without a `z`-dependent correction or a nontrivial phase conversion.

This is a normalization/phase guardrail, not a contradiction of Suzuki's conjecture.

---

## 9. What is exact, numerical, and open

Exact/source-established:

1. Suzuki equation (1.3) and local expansion (2.2).
2. The formal Fredholm equations (8.4)–(8.5).
3. Exact prime-power breakpoint locations.
4. Exact parity reduction.
5. Exact statement that the `Theta=pi` canonical real reflected characteristic is purely imaginary on the real axis.

Exploratory numerical:

1. Local `O(t^2)` calibration coefficient near `-0.875`.
2. The degree-4/6/8/10 smoke table at `a=1, lambda=-5`.
3. Apparent projective stabilization of `W(1)/W(0.5)` near `0.87765` for that formal control setup.

Open:

1. Certify an admissible `lambda<lambda_a` for each control interval.
2. Add differentiation-back residuals against Suzuki equation (8.4).
3. Study quadrature-order and precision convergence separately from interpolation-degree convergence.
4. Identify the finite deficiency phase convention corresponding to Suzuki's Section-7 de Branges normalization.
5. Determine the actual behavior of `phi(a,z)`.
6. Only after the Riemann control passes these tests, derive and run the source-normalized D12 kernel.
7. GRH/RH is not proved.

---

## 10. Next target

The highest-value next step is now to remove the remaining ambiguity in the formal smoke parameter by solving the compact generalized eigenvalue control problem

\[
\boxed{G_a u=\lambda K_a u}
\]

from Suzuki equation (8.7) with the **same breakpoint-aware product integration**.

That will give a numerical estimate of the finite lowest eigenvalue `lambda_a`, allowing us to choose and document a genuinely admissible `lambda<lambda_a` before repeating the deficiency-vector convergence study.

After that, differentiation back to equation (8.4) becomes the decisive internal consistency check.