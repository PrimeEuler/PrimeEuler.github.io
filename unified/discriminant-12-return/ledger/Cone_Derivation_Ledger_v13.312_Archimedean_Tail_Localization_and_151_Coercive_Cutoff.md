# Cone Derivation Ledger v13.312 — Archimedean Tail Localization and 151 Coercive Cutoff

## Status

This checkpoint refines v13.311 by observing that the smooth archimedean remainder is not a permanent high-mode cost.  Its kernel is compact and, in the odd Dirichlet basis for the even-v sector, its matrix entries admit an explicit two-index decay bound.

The main result is an analytic high-mode estimate

\[
\boxed{
|(K_r)_{mn}|\le \frac{C_r}{k_mk_n},
\qquad
C_r<8.048,
}
\]

which yields

\[
\boxed{
\|P_NK_rP_N\|
\le
\frac{4C_r}{\pi^2}
\left(\frac1{N^2}+\frac1{2N}\right).
}
\]

Using this instead of the global v13.311 cost 0.459846... lowers the first sufficient odd coercive cutoff from 237 to

\[
\boxed{N=151.}
\]

No RH/GRH, kernel, or lambda_1=0 conclusion is made.

---

## 1. Setup

Let

\[
h(t)=r''(t),
\qquad
K_r(x,y)=-h(|x-y|),
\]

with

\[
r''(t)=\frac{e^{-t/2}}{1-e^{-2t}}-\frac1{2t}.
\]

From v13.311:

\[
h(t)>0,
\qquad
h'(t)<0
\quad(0<t\le2),
\]

and

\[
h(0)=\frac14,
\qquad
h'(0)=-\frac1{48}.
\]

Use the normalized even-v Dirichlet basis

\[
\psi_n(x)=(-1)^{(n-1)/2}\cos\frac{n\pi x}{2},
\qquad n\text{ odd},
\]

with

\[
k_n=\frac{n\pi}{2}.
\]

Define an antiderivative

\[
F_n(x)=(-1)^{(n-1)/2}\frac{\sin(k_nx)}{k_n}.
\]

Then

\[
F_n'=\psi_n,
\qquad
|F_n(x)|\le\frac1{k_n},
\]

and, crucially,

\[
F_n(1)=\frac1{k_n},
\qquad
F_n(-1)=-\frac1{k_n}.
\]

---

## 2. Two integrations by parts

For

\[
R_{mn}=\iint_{[-1,1]^2}\psi_m(x)K_r(x,y)\psi_n(y)\,dx\,dy,
\]

integrate once in x and once in y using the bounded antiderivatives F_m,F_n.

The corner and edge terms are controlled by h(0), h(2), and the total variation of h on [0,2].  Since h is positive decreasing,

\[
\int_0^2|h'(t)|dt=h(0)-h(2).
\]

The corner plus the four edge-variation contributions combine to

\[
2(h(0)+h(2))+4(h(0)-h(2))
=6h(0)-2h(2)
\le6h(0)=\frac32.
\]

The remaining mixed derivative is distributional because of the |x-y| cusp.  Writing t=x-y,

\[
K_{r,xy}=h''(|t|)+2h'(0)\,\delta(t).
\]

Hence its total variation on the square is bounded by

\[
4\sup_{0\le t\le2}|h''(t)|+4|h'(0)|.
\]

Since h''=r'''', the remaining task is to bound r'''' on [0,2].

---

## 3. Analytic majorant for r''''

Write

\[
r(t)=\sum_{m\ge2}a_mt^m.
\]

For k=m-1>=3, the Bernoulli Fourier estimate gives

\[
|a_{k+1}|
\le
\frac{\zeta(k)}{\pi^k k(k+1)}.
\]

Therefore, for 0<=t<=2,

\[
|r''''(t)|
\le
\frac18\sum_{k\ge3}\zeta(k)(k-1)(k-2)q^k,
\qquad
q=\frac2\pi.
\]

Using

\[
\zeta(k)\le\zeta(3)
\qquad(k\ge3),
\]

and

\[
\sum_{k\ge3}(k-1)(k-2)q^k
=\frac{2q^3}{(1-q)^3},
\]

we obtain

\[
\boxed{
\sup_{0\le t\le2}|r''''(t)|
\le
M_4
:=
\frac{\zeta(3)q^3}{4(1-q)^3}
\approx1.6159262150.
}
\]

Thus

\[
\boxed{
C_r
:=
\frac32+4M_4+\frac1{12}
=\frac{19}{12}+4M_4
\approx8.0470381934.
}
\]

and

\[
\boxed{
|R_{mn}|\le\frac{C_r}{k_mk_n}.
}
\]

This is an infinite-dimensional entrywise estimate, not a finite-section fit.

---

## 4. Hilbert-Schmidt high-tail bound

For odd n>=N,

\[
\sum\frac1{k_n^2}
=
\frac4{\pi^2}\sum\frac1{n^2}
\le
\frac4{\pi^2}
\left(\frac1{N^2}+\frac1{2N}\right).
\]

Therefore

\[
\|P_NK_rP_N\|
\le
\|P_NK_rP_N\|_{HS}
\le
C_r\sum_{n\ge N,\,n\ odd}\frac1{k_n^2}.
\]

Hence

\[
\boxed{
\|P_NK_rP_N\|
\le
\frac{4C_r}{\pi^2}
\left(\frac1{N^2}+\frac1{2N}\right).
}
\]

This decays as O(1/N), so the v13.311 global cost 0.459846... should not be retained as a permanent high-mode penalty.

At N=237 this bound is already below 0.007.

---

## 5. Updated tail inequality

Retain:

- Hilbert cost pi/2;
- v13.310 prime power-Schur bound approximately 2.044764260347282;
- cusp tail bound from the corrected v13.303/v13.304 lineage;
- pole negative cost exactly zero;
- new archimedean tail bound above.

Then

\[
\langle A_{even}c,c\rangle
\ge
\left[
\log\frac N4
-\left(
\frac\pi2
+2.044764260347282
+\|P_NK_{cusp}P_N\|
+\|P_NK_rP_N\|
\right)
\right]\|c\|^2.
\]

The only nondecaying adverse terms now are the Hilbert and prime pieces.

---

## 6. New cutoff

Using the explicit cusp-tail and arch-tail bounds, the first odd N with positive margin is

\[
\boxed{N=151.}
\]

Numerically evaluating the explicit formulas gives

\[
\|P_{151}K_rP_{151}\|
\lesssim1.09421798596\times10^{-2},
\]

\[
\|P_{151}K_{cusp}P_{151}\|
\lesssim7.48996588100\times10^{-4},
\]

and

\[
\boxed{
\log(151/4)-C_{tail}(151)
\approx3.7337121\times10^{-3}>0.
}
\]

At N=149 the same explicit lower bound remains negative, approximately -9.76e-3.

Thus this estimate improves

\[
237\to\boxed{151}.
\]

The cumulative sufficient-cutoff sequence is now

\[
5.56\times10^6
\to52363
\to3441
\to2809
\to1765
\to1433
\to1257
\to1165
\to237
\to\boxed{151}.
\]

There are only 75 odd positive integers below 151, so the explicit low/moderate-frequency window has become genuinely small.

---

## 7. Proof-status guardrail

The archimedean tail-localization derivation is analytic and infinite-dimensional.  The inherited v13.310 prime power-Schur reduction is exact as a finite breakpoint computation, but its displayed decimal constant has not yet been wrapped in formal interval arithmetic.  Therefore the numerical cutoff 151 should inherit that same finite-arithmetic qualification rather than be advertised as a machine-checked interval theorem.

No conclusion is drawn about:

- existence of a kernel at a=1;
- lambda_1(a=1)=0;
- positivity of the full operator;
- RH or GRH.

---

## 8. Strategic consequence

The finite-window problem is now much smaller than at v13.311.  A direct hard split still has noncompact prime coupling across the boundary, so a scalar Schur-complement norm estimate is likely too pessimistic.

The next high-leverage step is a core-buffer-tail audit with:

1. a small core containing the numerically stabilized near-null vector (roughly n<=19 or n<=21);
2. an explicit finite buffer from the core edge through n=149;
3. the positive infinite tail n>=151;
4. matrix-valued, rather than scalar-norm, control of the buffer-to-tail Schur correction.

That route preserves the actual geometry of the prime coupling instead of paying its full operator norm at one artificial frequency interface.
