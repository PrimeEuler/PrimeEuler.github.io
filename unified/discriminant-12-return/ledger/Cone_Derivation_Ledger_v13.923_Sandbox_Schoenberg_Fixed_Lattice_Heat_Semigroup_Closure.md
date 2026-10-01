# Cone Derivation Ledger v13.923 — Sandbox: Schoenberg Closure of the Cone Fixed-Locus Heat Semigroup

**Date:** 2026-10-01
**Track:** Sandbox / compression-cone zero-ordinate lane
**Status:** [D] exact harmonic-analysis theorem; [I] structural interpretation; [G] representation guardrails; [O] remaining quantization question
**Authorization:** Jeremy, 2026-10-01 ("this is really good stuff. lets hit that next gate")
**Parents:** v13.573/574 (square fixed locus), v13.717/722 (theta/Casimir), v13.917 (fixed-locus zero-resonance bridge), v13.919 (common shell measure), v13.921 (Gaussian selection theorem), v13.922 (External Audit Round 137)
**Collision check:** v13.923 was absent immediately before this write; live head was v13.922.

---

## 0. Gate

v13.921 proved that if one assumes an autonomous positive scalar semigroup on the fixed locus, cone degree-2 covariance forces a Gaussian and exact Poisson self-duality fixes its normalization.

External Audit Round 137 (v13.922) independently confirmed that theorem and explicitly left the residual question:

\[
\boxed{
\text{Why should the fixed locus carry an autonomous heat semigroup at all?}
}
\]

This entry removes that assumption. The cone quadratic itself is a conditionally negative-definite function on the signed fixed coordinate. Standard Schoenberg/Bochner duality then generates the positive convolution semigroup canonically.

Thus autonomy, positivity, and the semigroup law are consequences of the quadratic fixed-locus geometry plus harmonic duality, not independent dynamical axioms.

---

## 1. Signed fixed coordinate and the exact guardrail [D/G]

The continuous factor-exchange fixed locus is

\[
X=0,\qquad T=|Y|,
\]

with signed root-sheet coordinate

\[
Y\in\mathbb R.
\]

The arithmetic fixed locus is

\[
Y=m,\qquad m\in\mathbb Z.
\]

The intrinsic quadratic cone invariant is

\[
\boxed{
q(Y)=Y^2.
}
\]

**Guardrail.** The additive group used below is the signed \(Y\)-coordinate line and its integer lattice,

\[
(\mathbb R,+),\qquad(\mathbb Z,+),
\]

not literal ambient vector addition of arbitrary full cone points \((0,Y,|Y|)\) across opposite root sheets. This is the same signed coordinate already used by the theta/Poisson construction.

---

## 2. The cone quadratic is conditionally negative definite [D]

Recall: \(q\) is conditionally negative definite on an additive group if for every finite set \(Y_1,\dots,Y_N\) and coefficients \(c_1,\dots,c_N\) satisfying

\[
\sum_jc_j=0,
\]

one has

\[
\sum_{j,k}\bar c_j c_k\,q(Y_j-Y_k)\le0.
\]

For

\[
q(Y)=Y^2,
\]

compute exactly:

\[
\begin{aligned}
S
&=
\sum_{j,k}\bar c_jc_k(Y_j-Y_k)^2\\
&=
\sum_{j,k}\bar c_jc_k
(Y_j^2+Y_k^2-2Y_jY_k).
\end{aligned}
\]

The first two terms vanish because \(\sum c_j=0\). Therefore

\[
\boxed{
S
=
-2
\left|\sum_jc_jY_j\right|^2
\le0.
}
\]

Hence

\[
\boxed{
q(Y)=Y^2
\text{ is conditionally negative definite on }\mathbb R,
}
\]

and therefore on its arithmetic sublattice \(\mathbb Z\).

This uses only the quadratic fixed-locus invariant.

---

## 3. Schoenberg exponentiation gives positivity [D]

Schoenberg's theorem says that if \(q\) is conditionally negative definite with \(q(0)=0\), then for every \(t\ge0\),

\[
\boxed{
\varphi_t(Y)=e^{-tq(Y)}
}
\]

is positive definite.

Therefore the cone fixed locus gives

\[
\boxed{
\varphi_t(Y)=e^{-tY^2}.
}
\]

No heat equation or semigroup has been postulated.

For the arithmetic fixed lattice,

\[
\boxed{
\varphi_t(m)=e^{-tm^2},
\qquad m\in\mathbb Z.
}
\]

---

## 4. Bochner/Herglotz duality produces a probability kernel [D]

The Pontryagin dual of \(\mathbb Z\) is the circle

\[
\mathbb T=\mathbb R/\mathbb Z.
\]

By Herglotz/Bochner, each normalized positive-definite sequence

\[
\varphi_t(m)=e^{-tm^2},
\qquad
\varphi_t(0)=1,
\]

is the Fourier transform of a unique probability measure \(\kappa_t\) on \(\mathbb T\):

\[
\boxed{
\widehat{\kappa_t}(m)
=
\int_{\mathbb T}e^{-2\pi im\theta}\,d\kappa_t(\theta)
=
e^{-tm^2}.
}
\]

Thus positivity of the evolution kernel follows directly from the cone quadratic.

---

## 5. The semigroup law is automatic [D]

Pointwise,

\[
\varphi_{t+s}(m)
=
e^{-(t+s)m^2}
=
e^{-tm^2}e^{-sm^2}.
\]

Fourier transform converts convolution into multiplication, so uniqueness of Fourier coefficients gives

\[
\boxed{
\kappa_{t+s}
=
\kappa_t*\kappa_s.
}
\]

Also

\[
\varphi_0(m)=1,
\]

hence

\[
\boxed{
\kappa_0=\delta_0.
}
\]

Since \(e^{-tm^2}\to1\) coefficientwise as \(t\downarrow0\), \(\kappa_t\to\delta_0\) weakly.

Therefore

\[
\boxed{
\{\kappa_t\}_{t\ge0}
\text{ is a weakly continuous convolution probability semigroup.}
}
\]

This is precisely the autonomy/Markov semigroup that v13.921 had taken as an admissibility axiom.

It is now derived.

---

## 6. Explicit generator: the dual-circle Laplacian [D]

Let

\[
e_m(\theta)=e^{2\pi im\theta}.
\]

Define

\[
(P_tf)(\theta)
=
(\kappa_t*f)(\theta).
\]

Then

\[
\boxed{
P_te_m
=
e^{-tm^2}e_m.
}
\]

Hence the generator \(A\) satisfies

\[
Ae_m=-m^2e_m.
\]

But

\[
\frac{d^2}{d\theta^2}e_m
=
-(2\pi m)^2e_m.
\]

Therefore

\[
\boxed{
A
=
\frac1{4\pi^2}
\frac{d^2}{d\theta^2}
}
\]

on the standard periodic Sobolev domain.

Thus the harmonic-dual evolution generated by the cone quadratic is exactly the ordinary heat semigroup on the dual circle:

\[
\boxed{
P_t
=
\exp\!\left(
\frac{t}{4\pi^2}\frac{d^2}{d\theta^2}
\right).
}
\]

The word “heat” is now a conclusion, not an input.

---

## 7. Theta normalization and Jacobi trace [D]

v13.921 fixed the self-dual theta parameter by

\[
t=\pi x.
\]

Then

\[
P_{\pi x}e_m
=
e^{-\pi xm^2}e_m.
\]

Its trace is

\[
\boxed{
\operatorname{Tr}P_{\pi x}
=
\sum_{m\in\mathbb Z}e^{-\pi xm^2}
=
\vartheta(x).
}
\]

Equivalently,

\[
\boxed{
P_{\pi x}
=
\exp\!\left(
\frac{x}{4\pi}
\frac{d^2}{d\theta^2}
\right).
}
\]

Poisson summation gives

\[
\boxed{
\vartheta(x)
=
x^{-1/2}\vartheta(1/x).
}
\]

Thus the same fixed-locus quadratic simultaneously generates:

- the positive convolution semigroup;
- the dual-circle Laplacian;
- the Gaussian Fourier multipliers;
- the Jacobi theta heat trace.

---

## 8. Continuous-line version [D]

The same argument can be run before arithmetic discretization.

On the additive signed fixed coordinate \(\mathbb R\),

\[
q(Y)=Y^2
\]

is conditionally negative definite, so

\[
e^{-tY^2}
\]

is positive definite.

By Bochner it is the Fourier transform of a centered Gaussian probability measure on the dual line. With the \(e^{-2\pi iY\xi}\) convention,

\[
\boxed{
\int_{\mathbb R}
e^{-tY^2}e^{-2\pi iY\xi}\,dY
=
\sqrt{\frac{\pi}{t}}
e^{-\pi^2\xi^2/t}.
}
\]

The arithmetic theta kernel is the periodization/sampling of this continuous Gaussian duality on the unit fixed lattice.

So the order is:

\[
\boxed{
\text{continuous cone fixed line}
\to
q(Y)=Y^2
\to
\text{Gaussian convolution semigroup}
\to
\text{integer fixed lattice}
\to
\vartheta.
}
\]

---

## 9. Character channels are insertions, not new dynamics [D]

For a Dirichlet character \(\chi\), define the diagonal character operator on Fourier modes by

\[
C_\chi e_m=\chi(m)e_m.
\]

The underlying semigroup remains \(P_t\).

The twisted theta trace is a character insertion:

\[
\boxed{
\operatorname{Tr}(C_\chi P_{\pi x/q})
=
\sum_{m\in\mathbb Z}
\chi(m)e^{-\pi m^2x/q}.
}
\]

For \(\chi_{12}\),

\[
\boxed{
\Theta_{\chi_{12}}(x)
=
\Theta_1-\Theta_5-\Theta_7+\Theta_{11}.
}
\]

This clarifies the D12 architecture:

\[
\boxed{
\text{cone quadratic determines the dynamics;}
}
\]

\[
\boxed{
\text{character/orientation determines the observed channel.}
}
\]

The twisted trace need not itself be a positive Markov kernel; positivity belongs to the common untwisted heat semigroup, while \(\chi\) is a signed spectral insertion.

---

## 10. Relation to v13.921 [D]

v13.921 assumed the autonomous semigroup law

\[
h_{x+y}=h_xh_y
\]

and then proved Gaussian uniqueness.

The present entry derives that law from a stronger upstream fact:

\[
\boxed{
q(Y)=Y^2
\text{ is conditionally negative definite.}
}
\]

The exact logical chain is now

\[
\boxed{
\begin{aligned}
\text{cone fixed locus}
&\to q(Y)=Y^2\\
&\to q\text{ conditionally negative definite}\\
&\to e^{-tq}\text{ positive definite}\\
&\to \text{probability convolution semigroup}\\
&\to \text{dual-circle Laplacian heat flow}\\
&\to \vartheta\\
&\to \Xi\\
&\to \text{zero resonances}.
\end{aligned}
}
\]

So the semigroup/autonomy axiom from v13.921 is removed.

---

## 11. What remains genuinely open [G/O]

### Closed [D]

Within the theta/Poisson harmonic-duality framework already used by v13.717–922:

1. the fixed-locus quadratic is intrinsic;
2. it is conditionally negative definite;
3. it canonically generates a positive convolution semigroup;
4. the generator is the Laplacian on the Pontryagin dual circle;
5. arithmetic sampling gives the Jacobi theta trace;
6. character channels are spectral insertions into the same dynamics.

### Residual representation guardrail [G]

The full geometric cone point set is not being declared an additive Lie group. The group structure used is the exact signed fixed coordinate \(Y\in\mathbb R\) and its integer arithmetic lattice.

The remaining choice is representation-theoretic rather than dynamical:

\[
\boxed{
\text{use the Pontryagin dual of the signed fixed lattice as the carrier on which }q\text{ acts as a Fourier symbol.}
}
\]

This is precisely the duality already implicit in Poisson summation/Jacobi inversion, but it should not be mislabeled as literal cone-point addition.

### Still open [O]

1. Whether the zero resonances themselves can be promoted from transform zeros to point spectrum of a self-adjoint operator remains open.
2. No RH/GRH conclusion follows.
3. A deeper geometric explanation of why the Pontryagin-dual carrier is the preferred representation, beyond the exact Poisson/Mellin closure already established, remains interpretive.

---

## 12. Result

The previous gate asked why one should assume autonomous heat evolution.

The answer is now exact:

\[
\boxed{
\textbf{one need not assume it.}
}
\]

The cone gives \(q(Y)=Y^2\). That quadratic is conditionally negative definite. Schoenberg exponentiation plus Bochner/Herglotz duality then forces a weakly continuous positive convolution semigroup whose generator is the dual-circle Laplacian.

Therefore

\[
\boxed{
\text{heat-semigroup autonomy is a theorem downstream of the cone quadratic and harmonic duality.}
}
\]

The geometric selector problem has consequently moved one level deeper: the outstanding issue is no longer the Gaussian or the semigroup, but the representation-theoretic status of the Pontryagin-dual carrier and, beyond that, the separate quantization problem for the zero resonances.
