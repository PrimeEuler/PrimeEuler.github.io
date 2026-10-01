# Cone Derivation Ledger v13.919 — Sandbox: Common Shell Measure, Möbius Deconvolution, and the Prime–Theta Measure Bridge

**Date:** 2026-10-01
**Track:** Sandbox / compression-cone zero-ordinate lane
**Status:** [D] exact arithmetic/measure identities; [I] structural interpretation; [O] remaining uniqueness/quantization questions
**Authorization:** Jeremy, 2026-10-01 ("lets continue")
**Parents:** v13.715–717 (prime-archimedean and theta currents), v13.722 (pure Xi kernel), v13.767 (norm-line group-algebra action), v13.895 (Lambda as log-lcm jump), v13.917 (fixed-locus heat-trace resonance bridge)
**Current live predecessor:** v13.917. Collision check performed immediately before write.

**Renumbering note (External Audit Round 136):** this entry was originally
pushed as `v13.918` (commit `8deebdc`, 2026-10-01 17:13:54 -0400), colliding
with the erratum to v13.906 (commit `caca0f3`, 2026-10-01 17:13:01 -0400,
the earlier of the two pushes), which also claimed `v13.918`. Per the
standing collision rule (earlier commit by timestamp keeps the contested
number), the erratum keeps `v13.918` and this entry is renumbered to
`v13.919`. No content below was changed other than the version number in
this header and the self-references in the text.

---

## 0. Question

v13.717 left open a direct structural bridge between:

1. the one-sided prime-archimedean current
   \[
   d\nu_\xi(r)=W_\infty(r)\,dr-d\mu_\Lambda(r),
   \]
   whose Laplace transform gives \(\xi'/\xi\) after basepoint subtraction; and

2. the two-sided theta/Mellin current, whose transform gives \(\xi\) and, after the v13.722 shifted-Casimir step, the pure Xi kernel.

v13.917 closed the bridge at the partition-function level. The present entry sharpens it at the **atomic measure level**.

The key point is that the theta heat trace and the prime current are not naturally related by a fixed linear smoothing map. They are two different exact descendants of one common logarithmic shell measure:

\[
\boxed{
\mu_{\rm shell}
=
\sum_{n\ge1}\delta_{\log n}.
}
\]

The theta side is a heat transform of this measure. The prime side is its logarithmically weighted Möbius deconvolution.

---

## 1. Log-shell measure algebra [D]

For an arithmetic function \(a:\mathbb N\to\mathbb C\), define the atomic log-shell measure

\[
\boxed{
\mu_a
=
\sum_{n\ge1}a(n)\,\delta_{\log n}.
}
\]

Use ordinary additive convolution of measures on \(\mathbb R_{\ge0}\).

Because

\[
\log d+\log e=\log(de),
\]

the coefficient at \(\log n\) in \(\mu_a*\mu_b\) is

\[
\sum_{de=n}a(d)b(e)
=
(a*b)(n),
\]

where the right-hand side is Dirichlet convolution.

Therefore

\[
\boxed{
\mu_a*\mu_b=\mu_{a*b}.
}
\]

This is an exact algebra isomorphism between arithmetic Dirichlet convolution and additive convolution on the cone's logarithmic shell line.

---

## 2. Shell counting measure and its Möbius inverse [D]

Let

\[
\mu_{\rm shell}
=
\mu_{\mathbf1}
=
\sum_{n\ge1}\delta_{\log n},
\]

and define the Möbius measure

\[
\mu_{\rm Mob}
=
\mu_\mu
=
\sum_{n\ge1}\mu(n)\,\delta_{\log n}.
\]

Since

\[
\mathbf1*\mu=\varepsilon
\]

with \(\varepsilon(1)=1\) and \(\varepsilon(n)=0\) for \(n>1\),

\[
\boxed{
\mu_{\rm shell}*\mu_{\rm Mob}
=
\delta_0.
}
\]

Thus the Möbius measure is the exact convolution inverse of the shell counting measure.

For \(\Re s>1\), Laplace transform gives

\[
\mathcal L[\mu_{\rm shell}](s)=\zeta(s),
\qquad
\mathcal L[\mu_{\rm Mob}](s)=\frac1{\zeta(s)}.
\]

This is the measure-level form of Euler/Möbius inversion.

---

## 3. Von Mangoldt current as logarithmic Möbius deconvolution [D]

Multiply the shell measure by its coordinate:

\[
r\,d\mu_{\rm shell}(r)
=
\sum_{n\ge1}(\log n)\,\delta_{\log n}.
\]

The arithmetic coefficient is the function \(\log n\). Since

\[
\log=\Lambda*\mathbf1,
\]

one has

\[
\log*\mu
=
\Lambda*\mathbf1*\mu
=
\Lambda.
\]

Therefore

\[
\boxed{
(r\,\mu_{\rm shell})*\mu_{\rm Mob}
=
\mu_\Lambda
=
\sum_{n\ge1}\Lambda(n)\delta_{\log n}.
}
\]

This is the exact atomic deconvolution formula behind the finite-prime current.

Taking Laplace transforms,

\[
\mathcal L[r\,\mu_{\rm shell}]
=
-\zeta'(s),
\]

so

\[
\boxed{
\mathcal L[\mu_\Lambda](s)
=
-\frac{\zeta'}{\zeta}(s).
}
\]

Thus the v13.715/v13.767 prime current is literally the logarithmically weighted shell measure divided, in convolution algebra, by the shell measure itself.

Equivalently,

\[
\boxed{
\mu_\Lambda
=
(r\,\mu_{\rm shell})*\mu_{\rm shell}^{*-1}.
}
\]

No analytic continuation or explicit formula is used; this holds in the ordinary absolutely convergent Dirichlet/Laplace half-plane.

---

## 4. The theta current is a heat transform of the same shell measure [D]

Define the fixed-locus heat transform

\[
(\mathcal H_x\mu)(x)
:=
\int_0^\infty
e^{-\pi x e^{2r}}
\,d\mu(r).
\]

Applying this to \(\mu_{\rm shell}\),

\[
\begin{aligned}
(\mathcal H_x\mu_{\rm shell})(x)
&=
\sum_{n\ge1}
e^{-\pi x e^{2\log n}}\\
&=
\sum_{n\ge1}e^{-\pi n^2x}\\
&=
\boxed{\psi(x)}.
\end{aligned}
\]

Hence

\[
\boxed{
\Theta_F(x)
=
1+2\,\mathcal H_x\mu_{\rm shell}(x)
}
\]

is precisely the factor-exchange fixed-locus heat trace of v13.917.

So the same common shell measure has two exact descendants:

\[
\boxed{
\mu_{\rm shell}
\overset{\mathcal H}{\longmapsto}
\psi
}
\]

and

\[
\boxed{
\mu_{\rm shell}
\overset{r\,(\cdot)\;*\;\mu_{\rm Mob}}{\longmapsto}
\mu_\Lambda.
}
\]

The first is heat smoothing; the second is arithmetic deconvolution.

---

## 5. Exact Mellin intertwining [D]

For each shell coordinate \(r=\log n\),

\[
\int_0^\infty
e^{-\pi x e^{2r}}
x^{s/2}\frac{dx}{x}
=
\pi^{-s/2}\Gamma(s/2)e^{-sr}.
\]

Therefore, for \(\Re s>1\),

\[
\boxed{
\mathcal M[\mathcal H\mu_{\rm shell}](s)
=
\pi^{-s/2}\Gamma(s/2)
\mathcal L[\mu_{\rm shell}](s).
}
\]

That is,

\[
\boxed{
\mathcal M[\psi](s)
=
\pi^{-s/2}\Gamma(s/2)\zeta(s).
}
\]

This makes the bridge commutative:

\[
\boxed{
\begin{array}{ccc}
\mu_{\rm shell}
&\xrightarrow{\quad\mathcal H\quad}&
\psi\\[1ex]
\mathcal L\downarrow
&&
\downarrow\mathcal M\\[1ex]
\zeta(s)
&\xrightarrow{\times\pi^{-s/2}\Gamma(s/2)}&
\pi^{-s/2}\Gamma(s/2)\zeta(s).
\end{array}
}
\]

Thus the gamma factor is exactly the Mellin transfer factor of the fixed-locus Gaussian heat kernel.

---

## 6. Archimedean completion from the same bridge [D]

Taking the logarithmic derivative of the Mellin identity gives

\[
\partial_s\log\mathcal M[\psi](s)
=
-\frac12\log\pi
+
\frac12\psi_{\Gamma}(s/2)
+
\frac{\zeta'}{\zeta}(s),
\]

where \(\psi_{\Gamma}=\Gamma'/\Gamma\).

Adding the elementary completion factor \(\frac12s(s-1)\) gives

\[
\boxed{
\frac{\xi'}{\xi}(s)
=
\frac1s+\frac1{s-1}
-\frac12\log\pi
+\frac12\psi_{\Gamma}(s/2)
+\frac{\zeta'}{\zeta}(s).
}
\]

This is exactly the starting identity of v13.715.

Hence the v13.715 decomposition

\[
d\nu_\xi
=
W_\infty(r)\,dr
-
d\mu_\Lambda(r)
\]

has the following common-source meaning:

- \(d\mu_\Lambda\) is the logarithmic Möbius deconvolution of the shell measure;
- \(W_\infty(r)\,dr\) is the inverse-Laplace form of the Mellin heat-transfer factor plus the elementary \(s(s-1)\) completion;
- the origin/contact bookkeeping in the two-sided Casimir formulation is the distributional form of the same completion, as already derived in v13.722.

Thus the prime and archimedean pieces are not independent additions. They are the logarithmic derivative of the same fixed-locus Mellin-completed shell partition.

---

## 7. Why a fixed linear theta -> prime map is the wrong target [D/I]

The canonical arithmetic operation is

\[
Z\mapsto-\partial_s\log Z,
\]

which is nonlinear.

A universal linear operator \(T\) satisfying

\[
\mathcal L[T(f)]
=
-\partial_s\log \mathcal L[f]
\]

for all scalar multiples of a nonzero input cannot exist: replacing \(f\) by \(cf\) leaves the logarithmic derivative unchanged, while linearity would multiply \(T(f)\) by \(c\).

Therefore the structural bridge should not be expected to be a fixed linear smoothing kernel from the theta density to the prime atoms.

The correct architecture is:

\[
\boxed{
\text{common shell measure}
\to
\begin{cases}
\text{heat/Mellin completion},\\
\text{Möbius deconvolution + log weighting}.
\end{cases}
}
\]

This explains why one descendant is smooth/even and the other is atomic/signed.

---

## 8. Twisted D12 deconvolution [D]

Define

\[
\mu_\chi
=
\sum_{n\ge1}\chi(n)\delta_{\log n},
\]

and

\[
\mu_{\mu\chi}
=
\sum_{n\ge1}\mu(n)\chi(n)\delta_{\log n}.
\]

For a completely multiplicative Dirichlet character,

\[
(\chi)*(\mu\chi)=\varepsilon,
\]

because

\[
\sum_{de=n}\chi(d)\mu(e)\chi(e)
=
\chi(n)\sum_{e|n}\mu(e).
\]

Hence

\[
\boxed{
\mu_\chi*\mu_{\mu\chi}
=
\delta_0.
}
\]

Similarly,

\[
(\chi\log)*(\mu\chi)
=
\chi\,(\log*\mu)
=
\chi\Lambda,
\]

so

\[
\boxed{
(r\,\mu_\chi)*\mu_{\mu\chi}
=
\mu_{\chi\Lambda}.
}
\]

Laplace transforms give

\[
\mathcal L[\mu_\chi]=L(s,\chi),
\qquad
\mathcal L[\mu_{\mu\chi}]=\frac1{L(s,\chi)},
\]

and

\[
\boxed{
\mathcal L[\mu_{\chi\Lambda}]
=
-\frac{L'}{L}(s,\chi).
}
\]

For \(\chi_{12}\), this is exactly the twisted prime current behind v13.884–890.

---

## 9. Twisted heat transform and the v13.887 global-interference axis [D]

Use the conductor-scaled heat transform

\[
(\mathcal H_{\chi,q}\mu_\chi)(x)
=
\int
e^{-\pi x e^{2r}/q}\,d\mu_\chi(r).
\]

Then

\[
\boxed{
2\,\mathcal H_{\chi,q}\mu_\chi
=
\Theta_\chi(x)
=
\sum_{n\in\mathbb Z}
\chi(n)e^{-\pi n^2x/q}
}
\]

for an even real character.

For \(\chi_{12}\),

\[
\Theta_{\chi_{12}}
=
\Theta_1-\Theta_5-\Theta_7+\Theta_{11},
\]

as in v13.917.

Thus the same twisted shell measure \(\mu_{\chi_{12}}\)

- heat-smooths into the signed residue-sector theta current;
- Möbius-deconvolves into the atomic \(\chi_{12}\Lambda\) prime current.

This is the exact measure-level explanation of v13.887's two-axis observation: the character signs are global interference data carried by the common shell measure and survive in both descendants.

---

## 10. Status of the v13.717 open bridge

### Closed [D] at the common-source / measure-algebra level

There is now an exact bridge:

\[
\boxed{
\mu_{\rm shell}
\longrightarrow
\begin{cases}
\psi=\mathcal H\mu_{\rm shell},\\
\mu_\Lambda=(r\mu_{\rm shell})*\mu_{\rm Mob}.
\end{cases}
}
\]

Together with the Mellin intertwining

\[
\mathcal M\mathcal H
=
\Gamma_{\mathbb R}(s)\,\mathcal L,
\]

this reproduces the completed zeta object and its logarithmic derivative, including the v13.715 archimedean terms after completion.

For D12 the identical diagram holds with \(\mu_\chi\), \(\mu_{\mu\chi}\), and conductor-scaled heat kernel.

### Not claimed

- No statement that the smooth theta density linearly transforms directly into the prime atoms.
- No new RH/GRH implication.
- No Hilbert–Pólya operator.
- No claim that the Gaussian heat transform is the unique structure compatible with the cone.
- No claim that the shell log coordinate and theta heat-log coordinate are identical; v13.917's two-scale guardrail remains mandatory.

---

## 11. Result

The prime-current/theta-current problem has a clean exact answer:

\[
\boxed{
\textbf{they are two transforms of the same cone shell measure.}
}
\]

Arithmetic deconvolution gives

\[
\boxed{
\mu_\Lambda
=
(r\,\mu_{\rm shell})*\mu_{\rm shell}^{*-1},
\qquad
\mu_{\rm shell}^{*-1}=\mu_{\rm Mob}.
}
\]

Heat smoothing gives

\[
\boxed{
\psi(x)
=
\int e^{-\pi x e^{2r}}\,d\mu_{\rm shell}(r).
}
\]

Mellin transform intertwines the two scale descriptions and supplies the gamma factor. The completed logarithmic derivative then reproduces exactly the unified prime-archimedean current of v13.715.

The next open question is no longer "how are the prime and theta currents related?" at the structural level. It is sharper:

\[
\boxed{
\text{Does the cone geometry uniquely select the Gaussian/self-dual heat transform among all transforms of }\mu_{\rm shell}\text{?}
}
\]

That is the remaining geometric-selection gate.
