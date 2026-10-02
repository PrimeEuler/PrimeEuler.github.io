# Cone Derivation Ledger v13.946 — Sandbox: Fold-Semigroup Paley–Wiener Leakage Extremal and Optimized Tunneling Rate

**Date:** 2026-10-02  
**Track:** Sandbox / cross-lane cone-sieve ↔ Suzuki-Jost finite-size extremal lane  
**Status:** [D] exact convolution/fold leakage semigroup and asymptotic extremal rate; [D] RH-conditional optimized odd-gap upper-rate theorem; [D] explicit benchmark \(\sigma_*\ge\gamma_1/e\); [G] no matching lower bound and no operator RG equality; [O] solve the positive-definite Paley–Wiener Chebyshev extremal and track source residues  
**Authorization:** Jeremy, 2026-10-02 ("awesome. lets hit it")  
**Parents:** v13.942 (sieve renormalization), v13.944 (sieve/Jost scale bridge and exponential gap), v13.945 (External Audit Round 143)  
**Collision check:** v13.946 was absent immediately before this write.

---

## 0. Audit synchronization

External Audit Round 143 (v13.945) independently PASSed v13.940–944, including:

- the deficiency-overlap double-scaling law;
- the parity-pole crossover;
- the sieve-renormalization entry;
- the super-algebraic parity-gap theorem;
- the exact sieve/Jost scale matching;
- the convolution proof of an exponential odd-gap upper bound.

The present entry optimizes that convolution construction and tests whether the exact sieve fold induces a genuine recursion on the finite-size extremal.

It does — at the level of the **trial-filter leakage extremal**.

It does not yet give an exact recursion for Suzuki's eigenvalue gap itself.

---

## 1. RH-positive zero-sampling setting [D, conditional on RH]

Assume RH.

Then the Weil/Suzuki form is

\[
Q_W[f]
=
\sum_\gamma
m_\gamma
|\widehat f(\gamma)|^2,
\]

with real nonzero zero ordinates \(\gamma\).

Let

\[
\gamma_1
:=
\inf_\gamma|\gamma|
>0.
\]

For the filter extremal, let \(\mathcal P_a\) be the class of even nonnegative \(C_c^\infty\) probability densities

\[
p\ge0,
\qquad
p(x)=p(-x),
\qquad
\int p=1,
\qquad
\operatorname{supp}p\subset[-a,a].
\]

Write

\[
P(t):=\widehat p(t).
\]

Define the zero-set leakage of \(p\) by

\[
\boxed{
q(p)
:=
\sup_\gamma |P(\gamma)|.
}
\tag{1}
\]

For every nontrivial probability density in this class,

\[
q(p)<1:
\]

for each \(\gamma\ne0\), strictness follows from the equality case in the triangle inequality for a non-point-mass probability density, while \(P(t)\to0\) at infinity.

Define the optimal leakage at support radius \(a\) by

\[
\boxed{
q_*(a)
:=
\inf_{p\in\mathcal P_a}q(p)
\in[0,1).
}
\tag{2}
\]

The infimum need not be attained.

---

## 2. Exact convolution semigroup inequality [D]

Let

\[
p_1\in\mathcal P_{a_1},
\qquad
p_2\in\mathcal P_{a_2}.
\]

Then

\[
p_1*p_2
\in
\mathcal P_{a_1+a_2}.
\]

Its Fourier transform is

\[
P_{12}(t)
=
P_1(t)P_2(t).
\]

Hence

\[
q(p_1*p_2)
=
\sup_\gamma
|P_1(\gamma)P_2(\gamma)|
\le
q(p_1)q(p_2).
\]

Taking infima gives the exact variational inequality

\[
\boxed{
q_*(a_1+a_2)
\le
q_*(a_1)q_*(a_2).
}
\tag{3}
\]

In particular,

\[
\boxed{
q_*(2a)
\le
q_*(a)^2.
}
\tag{4}
\]

Thus one doubling of logarithmic support can square the optimized zero-leakage.

This is the exact trial-filter counterpart of one inverse sieve fold.

---

## 3. Sieve-fold form [D/I]

From v13.944,

\[
N=e^{2a}.
\]

Define the arithmetic-cutoff leakage

\[
\boxed{
\mathcal Q_*(N)
:=
q_*\!\left(\frac12\log N\right),
\qquad
N>1.
}
\tag{5}
\]

Then because

\[
\frac12\log(N_1N_2)
=
\frac12\log N_1
+
\frac12\log N_2,
\]

equation (3) becomes

\[
\boxed{
\mathcal Q_*(N_1N_2)
\le
\mathcal Q_*(N_1)
\mathcal Q_*(N_2).
}
\tag{6}
\]

For one complete sieve lift,

\[
N\mapsto N^2,
\]

\[
\boxed{
\mathcal Q_*(N^2)
\le
\mathcal Q_*(N)^2.
}
\tag{7}
\]

Equivalently, written in the downward sieve direction,

\[
\boxed{
\mathcal Q_*(N)
\le
\mathcal Q_*(\sqrt N)^2.
}
\tag{8}
\]

[I] One arithmetic lift can therefore square the optimally suppressible zero-leakage.

This is an exact inequality for the filter extremal.

It is not an equality or conjugacy theorem for Suzuki's operator.

---

## 4. Existence of the optimized leakage exponent [D]

Define

\[
\boxed{
S(a):=-\log q_*(a)
}
\tag{9}
\]

with the convention \(S(a)=+\infty\) if \(q_*(a)=0\).

Equation (3) gives

\[
\boxed{
S(a+b)\ge S(a)+S(b).
}
\tag{10}
\]

Also, because enlarging the support class can only lower \(q_*\),

\[
S(a)
\]

is nondecreasing.

For any fixed \(a_0>0\), write

\[
a=n a_0+r,
\qquad
0\le r<a_0.
\]

Then

\[
S(a)
\ge
S(n a_0)
\ge
nS(a_0).
\]

Thus

\[
\liminf_{a\to\infty}
\frac{S(a)}a
\ge
\frac{S(a_0)}{a_0}.
\]

Since \(a_0\) is arbitrary, while the reverse inequality against the supremum is tautological,

\[
\boxed{
\sigma_*
:=
\lim_{a\to\infty}
\frac{-\log q_*(a)}a
=
\sup_{a>0}
\frac{-\log q_*(a)}a
\in(0,\infty].
}
\tag{11}
\]

Positivity is proved explicitly in §7 below.

This is the optimized amplitude-leakage exponent.

---

## 5. Repeated-filter odd trial states [D]

Fix

\[
p\in\mathcal P_L
\]

with finite positive variance and set

\[
q:=q(p)<1.
\]

Let

\[
g_n:=p^{*n},
\qquad
f_n:=g_n'.
\]

Then:

- \(g_n\) is even;
- \(f_n\) is odd;
- \(\operatorname{supp}f_n\subset[-nL,nL]\);
- \(\widehat f_n(t)=itP(t)^n\).

Since \(P\) is Schwartz, choose \(n_0\) so that

\[
C_0
:=
\sum_\gamma
m_\gamma
\gamma^2
|P(\gamma)|^{2n_0}
<
\infty.
\]

For \(n\ge n_0\),

\[
Q_W[f_n]
\le
C_0 q^{2(n-n_0)}
\le
C_p q^{2n}.
\]

As in v13.944, the variance expansion near \(t=0\) gives

\[
\boxed{
\|f_n\|_2^2
\ge
c_p n^{-3/2}.
}
\tag{12}
\]

Therefore

\[
\boxed{
\frac{Q_W[f_n]}{\|f_n\|_2^2}
\le
C_p'
n^{3/2}q^{2n}.
}
\tag{13}
\]

---

## 6. Optimized odd-gap decay rate [D, conditional on RH + even ground]

For arbitrary large \(a\), choose

\[
n(a)=\left\lfloor\frac aL\right\rfloor-1.
\]

Then \(f_{n(a)}\) is an admissible odd trial state in \((-a,a)\).

Hence

\[
\lambda_a^{(-)}
\le
C
a^{3/2}
\exp\!\left[
-\left(
\frac{-2\log q}{L}
+o(1)
\right)a
\right].
\]

Assume additionally that the finite ground state is even for sufficiently large \(a\). Under RH,

\[
0\le
\Delta_a
=
\lambda_a^{(-)}-\lambda_a
\le
\lambda_a^{(-)}.
\]

Therefore

\[
\boxed{
\liminf_{a\to\infty}
-\frac1a\log\Delta_a
\ge
\frac{-2\log q}{L}.
}
\tag{14}
\]

Now take the supremum over all admissible base filters and support radii.

By the definition (11),

\[
\boxed{
\liminf_{a\to\infty}
-\frac1a\log\Delta_a
\ge
2\sigma_*.
}
\tag{15}
\]

If \(\Delta_a=0\) along a subsequence, the left side is interpreted as \(+\infty\) there and the inequality remains valid.

Thus \(2\sigma_*\) is a rigorous optimized **constructive tunneling-rate lower bound** for \(-a^{-1}\log\Delta_a\).

It is not yet proved to equal the true gap exponent.

---

## 7. Explicit universal benchmark from a box filter [D]

The abstract extremal already has an explicit nonzero lower rate.

Let

\[
L>\gamma_1^{-1}
\]

and consider the even probability density

\[
u_L(x)
=
\frac1{2L}\mathbf 1_{[-L,L]}(x).
\]

Its Fourier transform is

\[
U_L(t)
=
\frac{\sin(Lt)}{Lt}.
\]

For every

\[
|t|\ge\gamma_1,
\]

\[
|U_L(t)|
\le
\frac1{L\gamma_1}.
\]

Although \(u_L\notin C_c^\infty\), there exist even nonnegative smooth probability densities supported in \([-L,L]\) converging to \(u_L\) in \(L^1\).

Their Fourier transforms converge uniformly on the real axis because

\[
\|\widehat p-\widehat u_L\|_\infty
\le
\|p-u_L\|_1.
\]

Hence

\[
\boxed{
q_*(L)
\le
\frac1{L\gamma_1}.
}
\tag{16}
\]

Therefore

\[
\sigma_*
\ge
\frac{\log(L\gamma_1)}L.
\]

Optimize the right side.

Set

\[
x=L\gamma_1.
\]

Then

\[
\frac{\log(L\gamma_1)}L
=
\gamma_1\frac{\log x}{x}.
\]

The function

\[
\frac{\log x}{x}
\]

has its maximum at

\[
x=e.
\]

Thus choose

\[
\boxed{
L_*=\frac e{\gamma_1}.
}
\tag{17}
\]

Then

\[
\boxed{
\sigma_*
\ge
\frac{\gamma_1}{e}.
}
\tag{18}
\]

Consequently, under RH plus the even-ground hypothesis,

\[
\boxed{
\liminf_{a\to\infty}
-\frac1a\log\Delta_a
\ge
\frac{2\gamma_1}{e}.
}
\tag{19}
\]

Equivalently, for every \(\varepsilon>0\),

\[
\boxed{
\Delta_a
\le
C_\varepsilon
a^{3/2}
\exp\!\left[
-\left(
\frac{2\gamma_1}{e}
-\varepsilon
\right)a
\right]
}
\tag{20}
\]

for sufficiently large \(a\).

The \(\varepsilon\) absorbs the smooth approximation to the box extremal and finite-block effects.

---

## 8. Arithmetic-cutoff exponent [D]

Recall

\[
N=e^{2a}.
\]

From (15),

\[
\liminf_{N\to\infty}
-\frac{\log\Delta_{(\log N)/2}}{\log N}
\ge
\sigma_*.
\]

Thus

\[
\boxed{
\Delta_a
\le
(\log N)^{3/2+o(1)}
N^{-\sigma_*+o(1)}.
}
\tag{21}
\]

The explicit box benchmark gives

\[
\boxed{
\Delta_a
\le
(\log N)^{3/2+o(1)}
N^{-\gamma_1/e+o(1)}.
}
\tag{22}
\]

The quantity \(\sigma_*\) therefore has two simultaneous interpretations:

\[
\boxed{
\sigma_*
=
\text{optimized zero-leakage exponent per logarithmic length}
}
\]

and, through \(N=e^{2a}\),

\[
\boxed{
\sigma_*
=
\text{constructive power exponent in arithmetic cutoff for the odd-gap upper bound}.
}
\]

---

## 9. Relation to the overlap regulator [C]

Under the one-pole crossover hypotheses of v13.941,

\[
\delta_\tau(a)
\sim
x_\tau\Delta_a.
\]

Therefore any upper bound derived above transfers to the intrinsic overlap regulator:

\[
\boxed{
\liminf_{a\to\infty}
-\frac1a\log\delta_\tau(a)
\ge
2\sigma_*,
}
\tag{23}
\]

and explicitly

\[
\boxed{
\delta_\tau(a)
\le
a^{3/2+o(1)}
\exp\!\left[
-\left(
\frac{2\gamma_1}{e}
-o(1)
\right)a
\right].
}
\tag{24}
\]

In arithmetic cutoff,

\[
\boxed{
\delta_\tau(a)
\le
(\log N)^{3/2+o(1)}
N^{-\gamma_1/e+o(1)}.
}
\tag{25}
\]

This remains conditional on the one-pole crossover when transferred from \(\Delta_a\) to \(\delta_\tau\).

---

## 10. What the fold does not yet imply [G]

The exact recursion

\[
q_*(2a)\le q_*(a)^2
\]

does **not** imply:

- equality;
- an exact RG fixed point;
- an exact recursion for \(\Delta_a\);
- an exact recursion for \(\delta_\tau(a)\);
- a recursion for the source residues
  \[
  \alpha_a,\beta_a;
  \]
- a matching lower bound on the true spectral gap.

The fold acts exactly on the **admissible trial-filter semigroup**.

Promoting it to an operator-level RG requires additional structure not presently proved.

---

## 11. The remaining extremal problem [O]

The rate optimization has been reduced to

\[
\boxed{
q_*(a)
=
\inf_{\substack{
p\ge0,\ p\ {\rm even},\ \int p=1\\
\operatorname{supp}p\subset[-a,a]
}}
\sup_\gamma|\widehat p(\gamma)|.
}
\tag{26}
\]

This is a positive-definite Paley–Wiener Chebyshev problem on the Riemann-zero sampling set.

Its asymptotic rate is

\[
\boxed{
\sigma_*
=
\lim_{a\to\infty}
-\frac1a\log q_*(a).
}
\]

The next sharp questions are:

1. Is
   \[
   0<\sigma_*<\infty
   \]
   with a finite exact value?

2. Is the discrete zero-set problem asymptotically equivalent to the full-stopband minimax problem
   \[
   \sup_{|t|\ge\gamma_1}|\widehat p(t)|?
   \]

3. Can Beurling–Malliavin/sampling-density methods produce a matching lower bound?

4. Does an extremizing or asymptotically extremizing filter become self-similar under
   \[
   p\mapsto p*p,
   \]
   making the sieve lift an actual extremal RG fixed point?

5. Separately, what are the asymptotics of the physical source residues
   \[
   \alpha_a,\beta_a?
   \]

Only after items 1–3 can \(2\sigma_*\) be identified with the actual spectral-gap exponent rather than a constructive lower bound on that exponent.

---

## 12. Result

The sieve fold induces an exact semigroup inequality on the optimized zero-leakage:

\[
\boxed{
q_*(a+b)\le q_*(a)q_*(b),
\qquad
q_*(2a)\le q_*(a)^2.
}
\]

Therefore the asymptotic leakage rate exists:

\[
\boxed{
\sigma_*
=
\lim_{a\to\infty}
-\frac1a\log q_*(a)
=
\sup_{a>0}
-\frac1a\log q_*(a).
}
\]

Under RH plus the even-ground hypothesis,

\[
\boxed{
\liminf_{a\to\infty}
-\frac1a\log\Delta_a
\ge
2\sigma_*.
}
\]

A simple box-filter benchmark gives

\[
\boxed{
\sigma_*\ge\frac{\gamma_1}{e},
}
\]

hence

\[
\boxed{
\Delta_a
\le
a^{3/2+o(1)}
e^{-(2\gamma_1/e-o(1))a}.
}
\]

In arithmetic cutoff \(N=e^{2a}\),

\[
\boxed{
\Delta_a
\le
(\log N)^{3/2+o(1)}
N^{-\gamma_1/e+o(1)}.
}
\]

The remaining problem is the matching lower bound / exact extremal value.
