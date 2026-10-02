# Cone Derivation Ledger v13.950 — Sandbox: Exact Zero-Blind Stopband RG Exponent and Klein–Gordon/Chebyshev Extremal Family

**Date:** 2026-10-02  
**Track:** Sandbox / cross-lane cone-sieve ↔ Suzuki-Jost zero-blind RG lane  
**Status:** [D] exact asymptotic zero-blind stopband exponent; [D] explicit positive compact-support near-extremal family; [D] exact square-root arithmetic scaling at canonical normalization; [C] RH-conditional zero-blind odd-gap corollary; [O] finite-\(a\) minimax constant/uniqueness remains open  
**Authorization:** Jeremy, 2026-10-02 ("awesome. lets see if it closes")  
**Parents:** v13.942, v13.944, v13.947, v13.949 (External Audit Round 144)  
**Collision check:** v13.950 was absent immediately before this write.

---

## 0. Synchronization and result

External Audit Round 144 (v13.949) independently confirmed v13.946–948, including the diagnosis that the unrestricted zero-aware extremal is degenerate and that the correct source-faithful replacement is the zero-blind stopband problem.

For \(\Omega>0\), define

\[
\mathcal P_a
=
\left\{
p\in C_c^\infty(\mathbb R):
p\ge0,\;
p(x)=p(-x),\;
\int p=1,\;
\operatorname{supp}p\subset[-a,a]
\right\}.
\]

For \(p\in\mathcal P_a\), let

\[
P(t)=\widehat p(t).
\]

Define the zero-blind stopband leakage

\[
\boxed{
\bar q_\Omega(a)
=
\inf_{p\in\mathcal P_a}
\sup_{|t|\ge\Omega}|P(t)|.
}
\tag{1}
\]

v13.947 already proved the convolution semigroup

\[
\bar q_\Omega(a+b)
\le
\bar q_\Omega(a)\bar q_\Omega(b)
\]

and therefore existence of

\[
\bar\sigma_\Omega
=
\lim_{a\to\infty}
-\frac1a\log\bar q_\Omega(a).
\]

The present entry determines this exponent exactly:

\[
\boxed{
\bar\sigma_\Omega=\Omega.
}
\tag{2}
\]

More precisely, for every \(a>0\),

\[
\boxed{
e^{-a\Omega}
\le
\bar q_\Omega(a)
\le
\operatorname{sech}(a\Omega).
}
\tag{3}
\]

Hence

\[
-\log\bar q_\Omega(a)
=
a\Omega+O(1).
\]

At the canonical project normalization \(\Omega=1\),

\[
\boxed{
\bar\sigma_1=1.
}
\tag{4}
\]

---

## 1. Lower barrier from the slit-plane majorant [D]

Fix

\[
p\in\mathcal P_a
\]

and write

\[
P(z)
=
\int_{-a}^{a}e^{izx}p(x)\,dx.
\]

Then

\[
P(0)=1
\]

and Paley–Wiener gives, for every integer \(N\),

\[
|P(z)|
\le
C_N(1+|z|)^{-N}e^{a|\Im z|}.
\tag{5}
\]

Let

\[
D_\Omega
=
\mathbb C
\setminus
\big(
(-\infty,-\Omega]\cup[\Omega,\infty)
\big).
\]

Choose the branch

\[
s(z)
=
\sqrt{\Omega^2-z^2}
\]

on \(D_\Omega\) with

\[
s(0)=\Omega
\]

and

\[
\Re s(z)>0.
\]

Write

\[
z=x+iy.
\]

A direct calculation gives

\[
\boxed{
\Re s(z)\ge |y|.
}
\tag{6}
\]

Indeed,

\[
(\Re s)^2
=
\frac{
|\Omega^2-z^2|
+
\Omega^2-x^2+y^2
}{2},
\]

while

\[
|\Omega^2-z^2|
\ge
|x^2+y^2-\Omega^2|.
\]

For \(\varepsilon>0\), define

\[
\boxed{
G_\varepsilon(z)
=
P(z)
e^{-(a+\varepsilon)s(z)}.
}
\tag{7}
\]

Using (5)–(6),

\[
|G_\varepsilon(z)|
\le
C_N(1+|z|)^{-N}
e^{-\varepsilon\Re s(z)}.
\]

Thus \(G_\varepsilon\) is bounded on \(D_\Omega\) and tends to zero at the unbounded end of the slit domain.

On either slit,

\[
\Re s=0,
\]

so

\[
|G_\varepsilon(t)|
=
|P(t)|
\le
q,
\qquad
q:=
\sup_{|t|\ge\Omega}|P(t)|.
\]

The maximum principle/Phragmén–Lindelöf theorem on the slit domain therefore gives

\[
|G_\varepsilon(0)|
\le q.
\]

But

\[
G_\varepsilon(0)
=
e^{-(a+\varepsilon)\Omega}.
\]

Hence

\[
q
\ge
e^{-(a+\varepsilon)\Omega}.
\]

Letting

\[
\varepsilon\downarrow0
\]

gives

\[
\boxed{
q
\ge
e^{-a\Omega}.
}
\tag{8}
\]

Taking the infimum over \(p\in\mathcal P_a\),

\[
\boxed{
\bar q_\Omega(a)
\ge
e^{-a\Omega}.
}
\tag{9}
\]

Therefore

\[
\boxed{
\bar\sigma_\Omega\le\Omega.
}
\tag{10}
\]

---

## 2. A positive compact-support Chebyshev/Klein–Gordon family [D]

Define

\[
\boxed{
F_{a,\Omega}(z)
=
\frac{
\cosh\!\left(
a\sqrt{\Omega^2-z^2}
\right)
}{
\cosh(a\Omega)
}.
}
\tag{11}
\]

Because \(\cosh\) is even, the square root disappears from the power series, so \(F_{a,\Omega}\) is entire.

It has exponential type \(a\) and

\[
F_{a,\Omega}(0)=1.
\]

The key point is that it is positive definite.

Define the positive measure

\[
\boxed{
dM_{a,\Omega}(x)
=
\frac12
\left(
\delta_{-a}
+
\delta_a
\right)
+
\frac{\Omega a}{2}
\frac{
I_1\!\left(
\Omega\sqrt{a^2-x^2}
\right)
}{
\sqrt{a^2-x^2}
}
\mathbf 1_{|x|<a}\,dx.
}
\tag{12}
\]

Here \(I_1\) is the modified Bessel function.

The density in (12) is nonnegative.

The classical Bessel/Klein–Gordon identity is

\[
\boxed{
\widehat M_{a,\Omega}(z)
=
\cosh\!\left(
a\sqrt{\Omega^2-z^2}
\right).
}
\tag{13}
\]

One direct derivation starts from

\[
\int_{-a}^{a}
e^{izx}
I_0\!\left(
\Omega\sqrt{a^2-x^2}
\right)\,dx
=
\frac{
2\sinh\!\left(
a\sqrt{\Omega^2-z^2}
\right)
}{
\sqrt{\Omega^2-z^2}
}
\]

and differentiates with respect to \(a\).

The boundary terms produce

\[
2\cos(az),
\]

and the interior derivative produces the \(I_1\)-density in (12).

At \(z=0\),

\[
M_{a,\Omega}(\mathbb R)
=
\cosh(a\Omega).
\]

Therefore

\[
\boxed{
d\mu_{a,\Omega}
=
\frac{dM_{a,\Omega}}
{\cosh(a\Omega)}
}
\tag{14}
\]

is an even probability measure supported in

\[
[-a,a],
\]

and its characteristic function is exactly \(F_{a,\Omega}\).

---

## 3. Exact stopband leakage of the positive measure [D]

For real

\[
|t|\ge\Omega,
\]

write

\[
r(t)=\sqrt{t^2-\Omega^2}.
\]

Then

\[
\sqrt{\Omega^2-t^2}
=
ir(t),
\]

so

\[
F_{a,\Omega}(t)
=
\frac{\cos(ar(t))}
{\cosh(a\Omega)}.
\]

Therefore

\[
\boxed{
\sup_{|t|\ge\Omega}
|F_{a,\Omega}(t)|
=
\operatorname{sech}(a\Omega).
}
\tag{15}
\]

Equality already occurs at the stopband edge

\[
|t|=\Omega.
\]

Thus a positive compact-support measure achieves leakage

\[
\operatorname{sech}(a\Omega)
=
2e^{-a\Omega}
(1+O(e^{-2a\Omega})).
\]

---

## 4. Passage to smooth positive densities [D]

The class \(\mathcal P_a\) requires smooth densities, while \(\mu_{a,\Omega}\) contains endpoint atoms.

Fix

\[
A>a
\]

and choose an even nonnegative smooth probability density

\[
\rho_\varepsilon
\]

supported in

\[
[-\varepsilon,\varepsilon],
\qquad
\varepsilon=A-a.
\]

Then

\[
p_{A,\varepsilon}
=
\mu_{a,\Omega}*\rho_\varepsilon
\]

is an even nonnegative \(C_c^\infty\) probability density supported in

\[
[-A,A].
\]

Its Fourier transform is

\[
F_{a,\Omega}(t)R_\varepsilon(t),
\]

with

\[
|R_\varepsilon(t)|\le1.
\]

Hence

\[
\sup_{|t|\ge\Omega}
|
\widehat p_{A,\varepsilon}(t)
|
\le
\operatorname{sech}(a\Omega).
\]

Now fix \(A\) and let

\[
\varepsilon\downarrow0,
\qquad
a=A-\varepsilon.
\]

By the definition as an infimum,

\[
\boxed{
\bar q_\Omega(A)
\le
\operatorname{sech}(A\Omega).
}
\tag{16}
\]

Combined with (9),

\[
\boxed{
e^{-A\Omega}
\le
\bar q_\Omega(A)
\le
\operatorname{sech}(A\Omega).
}
\tag{17}
\]

This proves (3).

---

## 5. Exact zero-blind RG exponent [D]

From (17),

\[
\log\cosh(A\Omega)
\le
-\log\bar q_\Omega(A)
\le
A\Omega.
\]

Since

\[
\log\cosh(A\Omega)
=
A\Omega-\log2+o(1),
\]

we obtain

\[
\boxed{
-\log\bar q_\Omega(A)
=
A\Omega+O(1).
}
\tag{18}
\]

Therefore

\[
\boxed{
\bar\sigma_\Omega
=
\lim_{A\to\infty}
-\frac1A
\log\bar q_\Omega(A)
=
\Omega.
}
\tag{19}
\]

The zero-blind RG exponent is finite, positive, and exact.

No Riemann zero ordinate is used anywhere in this derivation.

---

## 6. Exact arithmetic scaling dimension [D]

From the sieve/Jost bridge,

\[
N=e^{2A}.
\]

Define

\[
\bar{\mathcal Q}_\Omega(N)
=
\bar q_\Omega\!\left(
\frac12\log N
\right).
\]

Equation (18) gives

\[
\boxed{
\log
\bar{\mathcal Q}_\Omega(N)
=
-\frac{\Omega}{2}\log N
+
O(1).
}
\tag{20}
\]

Equivalently,

\[
\boxed{
\bar{\mathcal Q}_\Omega(N)
=
N^{-\Omega/2+o(1)}.
}
\tag{21}
\]

Thus the zero-blind leakage has arithmetic scaling dimension

\[
\boxed{
\frac{\Omega}{2}.
}
\tag{22}
\]

At the canonical deficiency normalization

\[
\Omega=1,
\]

\[
\boxed{
\bar{\mathcal Q}_1(N)
=
N^{-1/2+o(1)}.
}
\tag{23}
\]

This is exactly the square-root exponent of the sieve seed scale.

The equality is an exponent identity, not a proof that the stopband filter itself is the Eratosthenes seed.

---

## 7. Fold recursion at the exponent level [D]

v13.947 gives

\[
\bar q_\Omega(2a)
\le
\bar q_\Omega(a)^2.
\]

The exact exponent theorem gives

\[
\log\bar q_\Omega(2a)
=
-2a\Omega+O(1),
\]

while

\[
2\log\bar q_\Omega(a)
=
-2a\Omega+O(1).
\]

Hence

\[
\boxed{
\log\bar q_\Omega(2a)
-
2\log\bar q_\Omega(a)
=
O(1).
}
\tag{24}
\]

After division by \(a\),

\[
\boxed{
\frac1a
\left[
\log\bar q_\Omega(2a)
-
2\log\bar q_\Omega(a)
\right]
\to0.
}
\tag{25}
\]

So the sieve fold is asymptotically an exact fixed scaling at the logarithmic-rate level.

No exact convolution fixed point is asserted.

---

## 8. Zero-blind odd-gap corollary [C]

Assume RH and choose

\[
0<\Omega\le\gamma_1.
\]

Use the smooth positive near-extremal construction of §4 with a fixed additional smoothing profile so that the Fourier transform has rapid tail decay.

Differentiate the resulting even probability density to obtain an odd trial state

\[
f_a.
\]

Its Fourier transform is

\[
\widehat f_a(t)
=
itP_a(t).
\]

On every zero ordinate,

\[
|\widehat f_a(\gamma)|
\le
|\gamma|
e^{-\Omega a+O(1)}
\times
(\text{fixed rapidly decaying factor}).
\]

Thus

\[
Q_W[f_a]
\le
C
e^{-2\Omega a}.
\]

Near \(t=0\), the Klein–Gordon/Chebyshev transform has a Gaussian-scale window of width

\[
a^{-1/2},
\]

which gives

\[
\|f_a\|_2^2
\ge
c\,a^{-3/2}.
\]

Therefore

\[
\boxed{
\lambda_a^{(-)}
\le
C
a^{3/2}
e^{-2\Omega a}.
}
\tag{26}
\]

Under the even-ground hypothesis,

\[
0\le
\Delta_a
\le
\lambda_a^{(-)},
\]

so

\[
\boxed{
\Delta_a
\le
C
a^{3/2}
e^{-2\Omega a}.
}
\tag{27}
\]

In arithmetic cutoff,

\[
N=e^{2a},
\]

\[
\boxed{
\Delta_a
\le
C
(\log N)^{3/2}
N^{-\Omega}.
}
\tag{28}
\]

At the canonical zero-blind choice

\[
\Omega=1,
\]

\[
\boxed{
\Delta_a
\le
C
(\log N)^{3/2}
N^{-1}.
}
\tag{29}
\]

This is a source-faithful zero-blind upper bound.

It is not sharp for the true RH-positive variational gap, because v13.947 shows zero-aware trial states can make that gap much smaller.

---

## 9. What closes and what remains open

### Closed [D]

The zero-blind stopband RG exponent:

\[
\boxed{
\bar\sigma_\Omega=\Omega.
}
\]

The canonical arithmetic scaling:

\[
\boxed{
\bar{\mathcal Q}_1(N)=N^{-1/2+o(1)}.
}
\]

The source-faithful zero-blind odd-gap upper exponent:

\[
\boxed{
\Delta_a
\lesssim
e^{-2\Omega a}
}
\]

up to polynomial factors, under RH + even ground.

### Still open [O]

The exact finite-\(a\) minimax value

\[
\bar q_\Omega(a).
\]

The present bounds differ only by an asymptotic factor at most \(2\):

\[
e^{-a\Omega}
\le
\bar q_\Omega(a)
\le
\operatorname{sech}(a\Omega)
\sim
2e^{-a\Omega}.
\]

It is not proved here that the positive Klein–Gordon measure is the exact finite-\(a\) minimizer within the smooth-density infimum.

Also open:

- uniqueness/asymptotic uniqueness of near-extremizers;
- an exact convolution RG fixed point;
- a direct recursion for the physical source residues \(\alpha_a,\beta_a\).

---

## 10. Result

The source-faithful zero-blind RG problem closes at the exponent level:

\[
\boxed{
e^{-a\Omega}
\le
\bar q_\Omega(a)
\le
\operatorname{sech}(a\Omega)
}
\]

and therefore

\[
\boxed{
\bar\sigma_\Omega=\Omega.
}
\]

In the arithmetic cutoff variable

\[
N=e^{2a},
\]

\[
\boxed{
\bar{\mathcal Q}_\Omega(N)
=
N^{-\Omega/2+o(1)}.
}
\]

At the canonical unit normalization,

\[
\boxed{
\bar{\mathcal Q}_1(N)
=
N^{-1/2+o(1)}.
}
\]

Thus the exact zero-blind spectral scaling dimension coincides with the square-root sieve fold.

The remaining finite-\(a\) constant problem is secondary to the RG exponent and does not affect the double-scaling exponent.
