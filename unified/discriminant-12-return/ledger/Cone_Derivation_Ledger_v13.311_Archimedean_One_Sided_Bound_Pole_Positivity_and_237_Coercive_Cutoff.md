# Cone Derivation Ledger v13.311 — Archimedean One-Sided Bound, Pole Positivity, and 237 Coercive Cutoff

## Status

This checkpoint pivots away from further prime power-Schur iteration and sharpens the remaining smooth terms in Suzuki's a=1 even-v sector.

Two exact structural improvements are obtained:

1. the pole contribution is positive semidefinite in the even sector and therefore has **zero negative coercivity cost**;
2. the smooth archimedean remainder has a closed-form second derivative whose sign and monotonicity on [0,2] yield a dramatically sharper one-sided Schur bound.

No RH/GRH, kernel, or lambda_1=0 conclusion is made.

---

## 1. Smooth archimedean remainder

Recall

\[
r(t)=\frac14\sum_{m\ge2}\zeta\!\left(2-m,\frac14\right)\frac{(-2)^m}{m!}t^m.
\]

Differentiating twice and using

\[
\sum_{k\ge0}\zeta(-k,a)\frac{z^k}{k!}
=\frac1z-\frac{e^{az}}{e^z-1}
\]

gives, for a=1/4 and z=-2t,

\[
\boxed{
r''(t)=\frac{e^{-t/2}}{1-e^{-2t}}-\frac1{2t}
=\frac{e^{t/2}}{2\sinh t}-\frac1{2t}.
}
\]

With u=t/2,

\[
\boxed{
r''(t)=\frac14\left(\operatorname{csch}u+\operatorname{sech}u-\frac1u\right).
}
\]

---

## 2. Positivity and monotonicity of r'' on 0<t<=2

For 0<u<=1,

\[
\frac{\sinh u}{u}=\sum_{k\ge0}\frac{u^{2k}}{(2k+1)!}
\le\sum_{k\ge0}\left(\frac{u^2}{6}\right)^k
=\frac1{1-u^2/6},
\]

because \((2k+1)!\ge 6^k\) for k>=1.

Also, with z=u^2 in (0,1],

\[
\left(1+\frac z2\right)\left(1-\frac z6\right)^2-1
=\frac{z(z^2-10z+12)}{72}>0.
\]

Hence

\[
\frac1{(1-u^2/6)^2}<1+\frac{u^2}{2}\le\cosh u,
\]

and therefore

\[
\sinh^2u<u^2\cosh u.
\]

Equivalently,

\[
\operatorname{csch}u\,\operatorname{coth}u>\frac1{u^2}.
\]

Now

\[
\frac d{du}[4r''(2u)]
=-\operatorname{csch}u\,\operatorname{coth}u
-\operatorname{sech}u\,\tanh u
+\frac1{u^2}<0.
\]

Thus

\[
\boxed{r''(t)>0\text{ and }r''(t)\text{ is strictly decreasing on }(0,2].}
\]

The positivity also follows directly from \(t e^{t/2}>\sinh t\) on this interval, but the monotonicity proof above is the stronger result used below.

---

## 3. Exact center-row Schur bound

The smooth remainder operator has kernel

\[
K_r(x,y)=-r''(|x-y|).
\]

Because r''>0, the absolute Schur row mass is

\[
R(x)=\int_{-1}^1r''(|x-y|)\,dy
=r'(1+x)+r'(1-x).
\]

Since r'' is decreasing, r' is concave. Therefore

\[
R(x)\le 2r'(1),
\]

with equality at x=0.

Integrating the closed form gives

\[
\boxed{
r'(t)=\frac12\left[
\log\!\left(\frac{4\tanh(t/4)}{t}\right)
+\arctan(\sinh(t/2))
\right].
}
\]

Hence

\[
\boxed{
\|K_{\rm arch\,rem}\|
\le 2r'(1)
=\log(4\tanh(1/4))+\arctan(\sinh(1/2))
\approx0.4598463265063248.
}
\]

This replaces the v13.304 analytic bound

\[
2.0563386856144.
\]

So the analytic smooth-arch cost drops by more than a factor of four.

---

## 4. Pole term is positive semidefinite in the even sector

For

\[
p(t)=-8(\cosh(t/2)-1),
\]

we have

\[
-p''(x-y)=2\cosh\frac{x-y}{2}.
\]

Using

\[
2\cosh\frac{x-y}{2}
=2\cosh\frac x2\cosh\frac y2
-2\sinh\frac x2\sinh\frac y2,
\]

and evenness of v,

\[
\langle v,\sinh(x/2)\rangle=0.
\]

Therefore

\[
\boxed{
Q_{\rm pole}(v)
=2\left|\langle v,\cosh(x/2)\rangle\right|^2\ge0.
}
\]

Thus the pole contribution has

\[
\boxed{\text{negative coercivity cost }=0}
\]

in the even-v sector.

The earlier subtraction of a pole-tail norm was conservative but unnecessary.

---

## 5. Updated coercive tail inequality

Retain:

- Hilbert cost \(\pi/2\);
- v13.310 prime power-Schur bound
  \[
  \|B_{\rm prime}\|\lesssim2.044764260347282;
  \]
- new archimedean cost
  \[
  C_{\rm arch}=0.4598463265063248;
  \]
- zero pole negative cost;
- certified cusp-tail estimate from v13.304/v13.302 lineage.

Then for odd-mode vectors supported on n>=N,

\[
\boxed{
\langle A_{\rm even}c,c\rangle
\ge
\left[
\log\frac N4
-\left(
\frac\pi2
+2.044764260347282
+0.4598463265063248
+\|P_NK_{\rm cusp}P_N\|
\right)
\right]\|c\|_2^2.
}
\]

The permanent nondecaying cost is

\[
\boxed{
C_{\rm perm}
=\frac\pi2+2.044764260347282+0.4598463265063248
\approx4.075406913648504.
}
\]

---

## 6. New explicit cutoff

Using the same explicit cusp-tail formula as before, the first odd N with positive margin is

\[
\boxed{N=237.}
\]

At N=237:

\[
\|P_NK_{\rm cusp}P_N\|\lesssim4.6599297765\times10^{-4},
\]

and

\[
\boxed{
\log(237/4)-C_{\rm tail}(237)
\approx5.8928733891\times10^{-3}>0.
}
\]

Therefore

\[
\boxed{
\langle A_{\rm even}c,c\rangle>0
\quad\text{for every nonzero odd-mode tail vector supported on }n\ge237.
}
\]

This improves the v13.310 cutoff

\[
1165\to\boxed{237}.
\]

The cumulative sufficient-cutoff history is now

\[
5.56\times10^6
\to52363
\to3441
\to2809
\to1765
\to1433
\to1257
\to1165
\to\boxed{237}.
\]

---

## 7. Interpretation

This checkpoint shows that the major remaining looseness after the prime power-Schur work was the treatment of the smooth archimedean and pole terms.

The main structural lesson is:

\[
\boxed{
\text{use one-sided spectral information for coercivity, not symmetric operator norms.}
}
\]

The pole term is favorable, not adverse. The archimedean remainder has a closed-form monotone positive second derivative, so its negative contribution is controlled by a small exact Schur row mass.

This sharply localizes any possible zero/negative direction in the even-v sector to low and moderate modes below 237.

It does **not** establish:

- existence of a kernel at a=1;
- lambda_1(a=1)=0;
- positivity of the full operator;
- RH or GRH.

---

## 8. Audit continuity

The external round-15 objection to the original v13.302 off-diagonal Hilbert-Schmidt proof remains resolved by the revised v13.303 estimate, as independently confirmed by external audit round 16. The present checkpoint uses the corrected/certified cusp-tail lineage only.

---

## 9. Next target

The dominant permanent costs are now approximately

\[
\pi/2\approx1.5708,
\qquad
C_{\rm prime}\approx2.0448,
\qquad
C_{\rm arch}\approx0.45985.
\]

Further prime power-Schur work can still lower the prime constant toward the numerical Galerkin edge near 1.94, but the next strategically important problem is no longer just shrinking a global tail cutoff.

The finite window below n=237 is now small enough to motivate a rigorous low-mode / Schur-complement enclosure combining:

1. an explicit finite matrix for modes n<237;
2. the certified positive tail for n>=237;
3. rigorous control of finite-to-tail coupling.

That is the natural route toward a genuine global sign statement for the even sector without overclaiming a kernel or RH conclusion.
