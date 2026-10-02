# Cone Derivation Ledger v13.962 — Sandbox: No-Twist Xi Branch Equals Ground Regulator and Is Sub-\(N^{-1}\) Under RH

**Date:** 2026-10-02  
**Track:** Sandbox / no-twist Suzuki Xi branch and source-RG scale lane  
**Status:** [D] exact identification \(\delta_{\Xi}(a)=\lambda_a\) of the absolute \(\lambda=0\) Xi branch in ground-recentered variables; [D] exact Xi-target overlap parameter from v13.792; [D] RH-conditional super-exponential upper bound on \(\lambda_a\) from an even zero-aware trial family; [D] RH-conditional conclusion \(N_a\lambda_a\to0\); [R] strategic correction — the \(N^{-1}\) zero-blind window is not the selected Xi regulator branch; [O] prove finite-to-Xi convergence at \(\delta=\lambda_a\) and sharpen the asymptotic of \(\lambda_a\)  
**Authorization:** Jeremy, 2026-10-02 ("lets try and get those closed!")  
**Parents:** v13.792, v13.794, v13.935, v13.947, v13.950, v13.958–961  
**Collision check:** v13.962 was absent in the live tree immediately before this write.

---

## 0. Main correction of target

The recent source-RG lane studied fixed overlap levels

\[
\kappa_a(\delta_\tau(a))
=
e^{-\tau}
\]

and asked whether the corresponding regulator might satisfy

\[
\delta_\tau(a)\asymp N_a^{-1},
\qquad
N_a=e^{2a}.
\]

That is a valid intrinsic crossover problem.

But the **specific no-twist Suzuki Xi branch** already has an exact absolute shift:

\[
\boxed{
\lambda_{\rm abs}=0.
}
\]

In the ground-recentered parametrization

\[
T_{a,\delta}^{\circ}
=
A_a-\lambda_a I+\delta I
=
A_a-(\lambda_a-\delta)I,
\]

the absolute shift is

\[
\lambda_{\rm abs}
=
\lambda_a-\delta.
\]

Therefore

\[
\boxed{
\lambda_{\rm abs}=0
\iff
\delta=\lambda_a.
}
\tag{1}
\]

Thus the finite no-twist Xi regulator is not an unknown scaling law:

\[
\boxed{
\delta_{\Xi}(a)=\lambda_a.
}
\tag{2}
\]

The remaining problem is the asymptotic behavior of \(\lambda_a\) and the Weyl data evaluated at this exact branch.

---

## 1. Source-faithful shift bookkeeping [D]

v13.794 fixes the source convention:

- Suzuki's finite Section-7 Xi target uses the **absolute shift**
  \[
  \lambda=0;
  \]
- under RH, Suzuki may use that branch because
  \[
  A_a>0;
  \]
- the finite \(F,h,m\) data depend on the shift in general.

v13.935 defines

\[
B_a=A_a-\lambda_aI
\]

and

\[
T_{a,\delta}^{\circ}
=
B_a+\delta I.
\]

Hence

\[
T_{a,\delta}^{\circ}
=
A_a-(\lambda_a-\delta)I.
\]

Equation (1) follows exactly.

No asymptotic or RH assumption is needed for this bookkeeping identity.

---

## 2. Xi target overlap level [D/C]

At the absolute \(\lambda=0\) branch, define

\[
\boxed{
\kappa_a^{\Xi}
:=
\kappa_a(\lambda_a)
=
h_{a,\lambda=0}(i).
}
\tag{3}
\]

v13.792 computes the source-fixed Xi target Schur parameter

\[
\boxed{
\kappa_\Xi
=
\frac{\xi''(3/2)}{\xi'(3/2)}
-
\frac{\xi'(3/2)}{\xi(3/2)}
}
\tag{4}
\]

with numerical value

\[
\boxed{
\kappa_\Xi
\approx
0.9968019520324009035.
}
\tag{5}
\]

Therefore, if the finite \(\lambda=0\) Suzuki Weyl data converge to the Xi target,

\[
\boxed{
\kappa_a(\lambda_a)
\longrightarrow
\kappa_\Xi.
}
\tag{6}
\]

Define the corresponding intrinsic overlap parameter

\[
\boxed{
\tau_\Xi
=
-\log\kappa_\Xi.
}
\tag{7}
\]

Numerically,

\[
\boxed{
\tau_\Xi
\approx
0.003203172651908305.
}
\tag{8}
\]

The associated parity-susceptibility ratio is

\[
\boxed{
q_\Xi
=
\tanh(\tau_\Xi/2)
=
\frac{1-\kappa_\Xi}{1+\kappa_\Xi}
\approx
0.0016015849565572,
}
\tag{9}
\]

matching the v13.792 target ratio.

Thus the Xi branch corresponds to a very small fixed overlap parameter, not to the illustrative one-e-fold choice \(\tau=1\).

---

## 3. Even zero-aware trial family [D, conditional on RH]

Assume RH.

Use the positive smooth zero-aware filters from v13.947.

Enumerate positive zero ordinates

\[
0<\gamma_1\le\gamma_2\le\cdots.
\]

Fix

\[
0<\eta<1
\]

and an even nonnegative compactly supported Gevrey probability density

\[
\rho\in C_c^\infty(-L,L)
\]

with

\[
|\widehat\rho(t)|
\le
C e^{-c|t|^\eta}.
\]

For

\[
j=1,\ldots,M,
\]

set

\[
\ell_j
=
\frac{\pi}{2\gamma_j}
\]

and

\[
\nu_j
=
\frac12
\left(
\delta_{+\ell_j}
+
\delta_{-\ell_j}
\right).
\]

Define

\[
\boxed{
p_M
=
\rho*\nu_1*\cdots *\nu_M.
}
\tag{10}
\]

Then:

- \(p_M\ge0\);
- \(p_M\) is even;
- \(p_M\in C_c^\infty\);
- \(\int p_M=1\);
- 
  \[
  \widehat p_M(\gamma_j)=0
  \qquad
  1\le j\le M.
  \]

The support radius is

\[
\boxed{
a_M
=
L+\frac{\pi}{2}
\sum_{j=1}^{M}\frac1{\gamma_j}
=
O((\log M)^2).
}
\tag{11}
\]

---

## 4. Uniform noncollapse of the even trial norm [D]

Because

\[
\sum_{j\ge1}\ell_j^2<\infty,
\]

there exists a fixed \(t_0>0\) and \(c_0>0\) such that

\[
\prod_{j=1}^{M}
|\cos(\ell_j t)|
\ge
c_0
\]

for every

\[
|t|\le t_0
\]

and every \(M\).

Also

\[
|\widehat\rho(t)|
\ge c_1>0
\]

after reducing \(t_0\) if needed.

Hence

\[
|\widehat p_M(t)|
\ge
c_0c_1
\qquad
(|t|\le t_0).
\]

By Plancherel,

\[
\boxed{
\|p_M\|_2^2
\ge
c_2>0
}
\tag{12}
\]

uniformly in \(M\).

This is the even analogue of the norm noncollapse used for the derivative trial in v13.947.

---

## 5. Super-exponentially small even Weil energy [D, conditional on RH]

Under RH,

\[
Q_W[p_M]
=
\sum_j
m_j
|\widehat p_M(\gamma_j)|^2.
\]

The first \(M\) terms vanish.

For \(j>M\),

\[
|\widehat p_M(\gamma_j)|
\le
|\widehat\rho(\gamma_j)|
\le
C e^{-c\gamma_j^\eta}.
\]

Using Riemann–von Mangoldt,

\[
\boxed{
Q_W[p_M]
\le
C'
e^{-c'\gamma_{M+1}^{\eta}}.
}
\tag{13}
\]

Also

\[
\gamma_M
\gg
\frac{M}{\log M}.
\]

Thus the Rayleigh quotient satisfies

\[
\boxed{
\frac{
Q_W[p_M]
}{
\|p_M\|_2^2
}
\le
C''
e^{-c'\gamma_{M+1}^{\eta}}.
}
\tag{14}
\]

---

## 6. Convert the \(M\)-scale to interval width \(a\) [D]

From

\[
a_M
=
O((\log M)^2),
\]

there exists \(c_3>0\) such that for every sufficiently large \(a\), one may choose

\[
M=M(a)
\]

with

\[
a_{M(a)}\le a
\]

and

\[
\boxed{
\log M(a)
\ge
c_3\sqrt a.
}
\tag{15}
\]

Therefore

\[
\gamma_{M(a)}
\gg
\frac{
e^{c_3\sqrt a}
}{
\sqrt a
}.
\]

After adjusting constants,

\[
\boxed{
\gamma_{M(a)}^\eta
\ge
c_4
e^{c_5\sqrt a}
}
\tag{16}
\]

for some \(c_4,c_5>0\).

Because

\[
p_{M(a)}
\in
C_c^\infty(-a,a),
\]

the variational principle gives

\[
\lambda_a
\le
\frac{
Q_W[p_{M(a)}]
}{
\|p_{M(a)}\|_2^2
}.
\]

Hence

\[
\boxed{
0\le
\lambda_a
\le
C
\exp\!\left[
-c_6e^{c_5\sqrt a}
\right]
}
\tag{17}
\]

under RH.

No ground-state simplicity or parity assumption is required.

---

## 7. The Xi regulator is far below the zero-blind \(N^{-1}\) window [D]

Recall

\[
N_a=e^{2a}.
\]

Equation (17) gives

\[
N_a\lambda_a
\le
C
\exp\!\left[
2a
-
c_6e^{c_5\sqrt a}
\right].
\]

Since

\[
e^{c_5\sqrt a}\gg a,
\]

\[
\boxed{
N_a\lambda_a
\longrightarrow0.
}
\tag{18}
\]

By (2),

\[
\delta_\Xi(a)=\lambda_a.
\]

Therefore

\[
\boxed{
N_a\delta_\Xi(a)
\longrightarrow0
}
\tag{19}
\]

under RH.

Equivalently,

\[
\boxed{
\delta_\Xi(a)
=
o(N_a^{-1}).
}
\tag{20}
\]

Indeed (17) is much stronger than any fixed polynomial suppression in \(N_a\).

---

## 8. Strategic relation to v13.950 and v13.959 [R/I]

v13.950 proves that the canonical zero-blind whole-stopband leakage has exact arithmetic scaling

\[
N^{-1/2}
\]

at unit stopband.

v13.959 proves that the corresponding zero-blind source-capacity balance singles out the regulator exponent

\[
\delta=N^{-1}.
\]

Those results stand.

The present theorem shows:

\[
\boxed{
\textbf{the zero-blind \(N^{-1}\) capacity window is not the actual no-twist Xi regulator branch under RH.}
}
\tag{21}
\]

The reason is exact:

- zero-blind RG asks for an intrinsic scale without using the zero set;
- the physical finite ground energy \(\lambda_a\) is a variational property of the full arithmetic operator and can exploit its complete zero structure;
- the Xi branch is fixed by the absolute shift \(\lambda=0\), hence by \(\delta=\lambda_a\).

Thus the two scales answer different questions.

---

## 9. Consequence for the source-RG \(N\)-scaled ratio [D/I]

At the Xi branch,

\[
c_a^{\Xi}
:=
N_a\delta_\Xi(a)
=
N_a\lambda_a.
\]

Under RH,

\[
\boxed{
c_a^{\Xi}\to0.
}
\tag{22}
\]

Therefore, in the \(N\)-scaled source-RG coordinate of v13.958,

\[
c=N\delta,
\]

the Xi branch approaches the **left endpoint**

\[
c=0,
\]

not an interior fixed crossing.

This means a finite nonzero source-RG fixed point

\[
C_\tau\in(0,\infty)
\]

for some fixed \(\tau\) would describe a different intrinsic crossover window, not Suzuki's absolute \(\lambda=0\) Xi branch.

---

## 10. Correct scalar Xi convergence diagnostic [C]

The finite no-twist Xi branch should now be tested by

\[
\boxed{
\kappa_a(\lambda_a)
}
\]

rather than by imposing an arbitrary fixed \(\tau\).

If finite-to-Xi convergence holds,

\[
\boxed{
\kappa_a(\lambda_a)
\to
\kappa_\Xi
}
\tag{23}
\]

with \(\kappa_\Xi\) given by (4).

Equivalently,

\[
\boxed{
\frac{
G_{a,-}(\lambda_a)
}{
G_{a,+}(\lambda_a)
}
\to
q_\Xi
\approx
0.0016015849565572.
}
\tag{24}
\]

This is the exact source-capacity scalar diagnostic for the no-twist Xi branch.

---

## 11. What is now closed [D]

Under RH:

\[
\boxed{
\delta_\Xi(a)=\lambda_a
}
\]

exactly,

\[
\boxed{
\lambda_a
\le
C
e^{-c e^{c'\sqrt a}}
}
\]

for suitable positive constants, and therefore

\[
\boxed{
N_a\delta_\Xi(a)\to0.
}
\]

So the relative scale question between the no-twist Xi branch and the cone/sieve \(N^{-1}\) window is closed:

\[
\boxed{
\textbf{the Xi branch lies asymptotically below the \(N^{-1}\) window.}
}
\]

---

## 12. Remaining Xi gate [O]

The correct next question is no longer whether

\[
N_a\delta_\Xi(a)
\]

has a finite nonzero limit.

It does not under RH.

The remaining source-faithful Xi problem is:

\[
\boxed{
\textbf{does }
\kappa_a(\lambda_a)
\longrightarrow
\kappa_\Xi
\textbf{ and, more strongly, do the full finite Weyl data at absolute }\lambda=0
\textbf{ converge to the Xi target?}
}
\]

By v13.929, identifying the full Herglotz target is RH-hard in the unconditional direction.

Under RH, the present entry supplies the correct regulator path along which that conditional convergence should be investigated.
