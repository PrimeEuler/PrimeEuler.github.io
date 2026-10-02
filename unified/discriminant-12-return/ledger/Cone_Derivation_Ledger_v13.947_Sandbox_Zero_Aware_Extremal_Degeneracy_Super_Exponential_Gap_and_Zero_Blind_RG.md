# Cone Derivation Ledger v13.947 — Sandbox: Zero-Aware Extremal Degeneracy, Super-Exponential Gap Upper Bounds, and the Zero-Blind RG Replacement

**Date:** 2026-10-02  
**Track:** Sandbox / cross-lane cone-sieve ↔ Suzuki-Jost finite-size extremal lane  
**Status:** [D] zero-aware extremal degeneracy under RH; [D] super-exponential odd-gap upper bound under RH + even-ground; [R] sharpens v13.946 by determining \(\sigma_*=\infty\); [G] explains why unrestricted zero-aware optimization is not the intrinsic cone/sieve RG; [O] solve the zero-blind stopband/seed-filter extremal  
**Authorization:** Jeremy, 2026-10-02 ("awesome. lets hit it")  
**Parents:** v13.942, v13.944–946  
**Collision check:** v13.947 was absent immediately before this write.

---

## 0. Main correction/refinement

v13.946 defined the zero-set filter extremal

\[
q_*(a)
=
\inf_{p\in\mathcal P_a}
\sup_\gamma |\widehat p(\gamma)|
\]

and showed the exact fold-semigroup inequality

\[
q_*(a+b)\le q_*(a)q_*(b),
\]

with asymptotic rate

\[
\sigma_*
=
\lim_{a\to\infty}
-\frac1a\log q_*(a)
\in(0,\infty].
\]

The present gate determines the value of that extended rate under RH:

\[
\boxed{\sigma_*=\infty.}
\]

The reason is not a new arithmetic miracle.

It is a **selection-class pathology**:

\[
\boxed{
\text{if the optimizing filter is allowed to know the individual zero ordinates, it can cancel them one by one.}
}
\]

Thus the unrestricted zero-aware extremal is mathematically legitimate but not the source-faithful cone/sieve RG observable.

---

## 1. Zero-annihilating positive filters [D, conditional on RH]

Assume RH and enumerate the positive ordinates

\[
0<\gamma_1\le\gamma_2\le\cdots
\]

with multiplicity.

For each \(j\), set

\[
\ell_j
=
\frac{\pi}{2\gamma_j}.
\]

Define the symmetric Bernoulli probability measure

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

Its Fourier transform is

\[
\widehat\nu_j(t)
=
\cos(\ell_j t).
\]

Therefore

\[
\boxed{
\widehat\nu_j(\gamma_j)=0.
}
\tag{1}
\]

Now convolve the first \(M\) factors:

\[
\boxed{
\nu^{(M)}
=
\nu_1*\cdots *\nu_M.
}
\tag{2}
\]

Then

\[
\widehat\nu^{(M)}(t)
=
\prod_{j=1}^M
\cos(\ell_j t),
\]

so

\[
\boxed{
\widehat\nu^{(M)}(\gamma_k)=0
\qquad
1\le k\le M.
}
\tag{3}
\]

The support radius is

\[
\boxed{
A_M
=
\sum_{j=1}^M\ell_j
=
\frac\pi2
\sum_{j=1}^M\frac1{\gamma_j}.
}
\tag{4}
\]

---

## 2. Support cost is only \(O((\log M)^2)\) [D]

Riemann–von Mangoldt gives

\[
\gamma_j
\asymp
\frac{j}{\log j}.
\]

For the upper-bound direction needed here, there exists \(c>0\) such that

\[
\gamma_j
\ge
c\,\frac{j}{\log(j+2)}
\]

for all sufficiently large \(j\).

Therefore

\[
\frac1{\gamma_j}
\le
C\frac{\log(j+2)}j.
\]

Hence

\[
\boxed{
A_M
=
O((\log M)^2).
}
\tag{5}
\]

By contrast,

\[
\gamma_M
\gg
\frac{M}{\log M}.
\tag{6}
\]

So killing the first \(M\) zeros costs only logarithmic-squared support radius while moving the first surviving sampled frequency to order \(M/\log M\).

---

## 3. Smooth positive completion and tail suppression [D]

Fix once and for all a nonzero even nonnegative compactly supported Gevrey probability density

\[
p\in C_c^\infty(-L,L)
\]

whose Fourier transform satisfies, for some

\[
0<\eta<1,
\]

\[
\boxed{
|P(t)|
\le
C e^{-c|t|^\eta}.
}
\tag{7}
\]

Define the smooth probability density

\[
\boxed{
p_M
=
p*\nu^{(M)}.
}
\tag{8}
\]

Then:

- \(p_M\ge0\);
- \(p_M\) is even;
- \(\int p_M=1\);
- \(p_M\in C_c^\infty\);
- 
  \[
  \operatorname{supp}p_M
  \subset
  [-(L+A_M),L+A_M].
  \]

Its Fourier transform is

\[
\boxed{
P_M(t)
=
P(t)
\prod_{j=1}^M
\cos(\ell_j t).
}
\tag{9}
\]

At the first \(M\) zero ordinates,

\[
P_M(\gamma_k)=0.
\]

For \(k>M\),

\[
|P_M(\gamma_k)|
\le
|P(\gamma_k)|
\le
C e^{-c\gamma_k^\eta}.
\]

Therefore

\[
\boxed{
q(p_M)
\le
C e^{-c\gamma_{M+1}^\eta}.
}
\tag{10}
\]

---

## 4. The zero-aware leakage exponent is infinite [D]

Let

\[
a_M=L+A_M.
\]

Then by (5),

\[
a_M
=
O((\log M)^2).
\]

But from (6) and (10),

\[
-\log q(p_M)
\gg
\gamma_{M+1}^\eta
\gg
\left(
\frac{M}{\log M}
\right)^\eta.
\]

Hence

\[
\frac{-\log q(p_M)}{a_M}
\to\infty.
\]

Since

\[
q_*(a_M)
\le
q(p_M),
\]

we obtain

\[
\boxed{
\sup_{a>0}
\frac{-\log q_*(a)}a
=
+\infty.
}
\tag{11}
\]

By the superadditive/Fekete theorem of v13.946,

\[
\boxed{
\sigma_*
=
\lim_{a\to\infty}
\frac{-\log q_*(a)}a
=
+\infty.
}
\tag{12}
\]

Thus the unrestricted zero-set Chebyshev extremal has no finite tunneling exponent.

---

## 5. Uniform lower bound on the derivative norm [D]

To transfer the construction to Suzuki's odd Rayleigh quotient, set

\[
f_M:=p_M'.
\]

Then \(f_M\) is odd and compactly supported in \((-a_M,a_M)\).

Its Fourier transform is

\[
\widehat f_M(t)
=
itP_M(t).
\]

The crucial point is that the \(L^2\) norm does not collapse with \(M\).

Indeed,

\[
\sum_{j\ge1}\ell_j^2
=
\frac{\pi^2}{4}
\sum_{j\ge1}\gamma_j^{-2}
<
\infty.
\]

Therefore for sufficiently small fixed \(|t|\le t_0\),

\[
\prod_{j=1}^M
|\cos(\ell_j t)|
\ge
c_0>0
\]

uniformly in \(M\).

Also \(P(t)\) stays bounded below near \(0\).

Hence by Plancherel,

\[
\|f_M\|_2^2
=
c_F
\int
t^2|P_M(t)|^2dt
\]

has the uniform lower bound

\[
\boxed{
\|f_M\|_2^2
\ge
c_1>0.
}
\tag{13}
\]

---

## 6. Super-exponential odd-sector upper bound [D, conditional on RH]

Under RH,

\[
Q_W[f_M]
=
\sum_k
m_k
\gamma_k^2
|P_M(\gamma_k)|^2.
\]

The first \(M\) terms vanish exactly.

For the tail,

\[
|P_M(\gamma_k)|
\le
C e^{-c\gamma_k^\eta}.
\]

Using zero counting,

\[
\sum_{k>M}
m_k
\gamma_k^2
e^{-2c\gamma_k^\eta}
\le
C'
e^{-c'\gamma_{M+1}^\eta}.
\]

Therefore

\[
\boxed{
Q_W[f_M]
\le
C'
e^{-c'\gamma_{M+1}^\eta}.
}
\tag{14}
\]

Combining with (13),

\[
\boxed{
\lambda_{a_M}^{(-)}
\le
C''
e^{-c'\gamma_{M+1}^\eta}.
}
\tag{15}
\]

Since

\[
a_M=O((\log M)^2),
\]

we may invert the relation and obtain constants \(c_2,c_3>0\) such that along the resulting support scale,

\[
\boxed{
\lambda_a^{(-)}
\le
\exp\!\left[
-c_2
\exp(c_3\sqrt a)
\right]
}
\tag{16}
\]

after harmless adjustment of constants and for sufficiently large \(a\).

By nested odd form domains, the same qualitative upper bound extends between the constructed support scales.

---

## 7. Recentered parity gap [D, conditional on RH + even ground]

Assume the finite ground state is even for sufficiently large \(a\).

Under RH,

\[
\lambda_a\ge0.
\]

Thus

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
\Delta_a
\le
\exp\!\left[
-c_2
\exp(c_3\sqrt a)
\right].
}
\tag{17}
\]

In particular,

\[
\boxed{
\forall C>0,\qquad
\Delta_a=O(e^{-Ca}).
}
\tag{18}
\]

So the RH-conditional variational upper bound is faster than every ordinary exponential in \(a\).

This is consistent with v13.946's formula

\[
\liminf
-\frac1a\log\Delta_a
\ge
2\sigma_*,
\]

because now

\[
\sigma_*=+\infty.
\]

---

## 8. Consequence for the overlap regulator [C]

Under the one-pole crossover hypotheses of v13.941,

\[
\delta_\tau(a)
\sim
x_\tau\Delta_a.
\]

Therefore

\[
\boxed{
\forall C>0,\qquad
\delta_\tau(a)=O(e^{-Ca})
}
\tag{19}
\]

and, with the explicit zero-aware construction,

\[
\boxed{
\delta_\tau(a)
\le
\exp\!\left[
-c_2
\exp(c_3\sqrt a)
\right]
}
\tag{20}
\]

up to the fixed crossover constant.

This is conditional on the same one-pole assumptions.

---

## 9. Why this is not the intrinsic cone/sieve RG [G]

The construction above explicitly uses

\[
\gamma_1,\ldots,\gamma_M
\]

to place filter zeros.

Therefore it cannot be used as a source-faithful derivation of the regulator law.

It is a **variational upper-bound construction**, not a canonical selection mechanism.

This distinction is essential:

\[
\boxed{
\text{the physical spectral gap may be bounded using zero-aware trial states;}
}
\]

but

\[
\boxed{
\text{the intrinsic cone/sieve double scaling may not be defined by fitting those zeros.}
}
\]

Thus v13.946's unrestricted zero-set extremal is too permissive to serve as the RG fixed-point observable.

---

## 10. Zero-blind replacement [D/O]

A source-faithful replacement is to optimize a continuum stopband or a pre-registered seed-filter family.

For a fixed real threshold

\[
\Omega>0
\]

chosen independently of the individual Riemann zeros, define

\[
\boxed{
\bar q_\Omega(a)
=
\inf_{p\in\mathcal P_a}
\sup_{|t|\ge\Omega}
|\widehat p(t)|.
}
\tag{21}
\]

Then convolution gives exactly

\[
\boxed{
\bar q_\Omega(a+b)
\le
\bar q_\Omega(a)
\bar q_\Omega(b).
}
\tag{22}
\]

Hence the zero-blind stopband exponent exists:

\[
\boxed{
\bar\sigma_\Omega
=
\lim_{a\to\infty}
-\frac1a\log\bar q_\Omega(a)
=
\sup_{a>0}
-\frac1a\log\bar q_\Omega(a).
}
\tag{23}
\]

If

\[
0<\Omega\le\gamma_1,
\]

then every Riemann-zero sample lies in the stopband, so

\[
q(p)
\le
\sup_{|t|\ge\Omega}|\widehat p(t)|.
\]

Thus any zero-blind stopband construction gives a valid RH-conditional odd-gap upper bound without using individual ordinates.

The box benchmark gives

\[
\boxed{
\bar\sigma_\Omega
\ge
\frac{\Omega}{e}.
}
\tag{24}
\]

The natural fully normalized project choice to test is \(\Omega=1\), because the canonical deficiency/Schur base point already fixes the unit scale through \(z=i\).

No claim is made yet that \(\bar\sigma_\Omega\) is finite, attained, or equal to the physical gap exponent.

---

## 11. Sieve-fold recursion survives the correction [D]

Define

\[
\bar{\mathcal Q}_\Omega(N)
=
\bar q_\Omega\!\left(\frac12\log N\right).
\]

Then

\[
\boxed{
\bar{\mathcal Q}_\Omega(N_1N_2)
\le
\bar{\mathcal Q}_\Omega(N_1)
\bar{\mathcal Q}_\Omega(N_2),
}
\tag{25}
\]

and in particular

\[
\boxed{
\bar{\mathcal Q}_\Omega(N)
\le
\bar{\mathcal Q}_\Omega(\sqrt N)^2.
}
\tag{26}
\]

So the exact sieve-fold semigroup remains intact after imposing zero-blindness.

This is the correct candidate RG observable.

---

## 12. Result

The unrestricted zero-aware extremal of v13.946 is degenerate in the precise sense

\[
\boxed{
\sigma_*=+\infty.
}
\]

Under RH plus the even-ground hypothesis,

\[
\boxed{
\Delta_a
\text{ is variationally bounded above faster than every }e^{-Ca}.
}
\]

That is a genuine spectral statement.

But the construction obtains this by encoding the zero ordinates in the trial filter.

Therefore the intrinsic cone/sieve RG must use a zero-blind class.

The replacement

\[
\boxed{
\bar q_\Omega(a)
=
\inf_{p\in\mathcal P_a}
\sup_{|t|\ge\Omega}
|\widehat p(t)|
}
\]

retains the exact convolution/sieve-fold semigroup while forbidding individual zero fitting.

The next sharp gate is to determine the zero-blind exponent

\[
\boxed{
\bar\sigma_\Omega
}
\]

and decide whether it is finite, whether an extremizer exists, and whether the fold admits an asymptotically self-similar optimizer.
