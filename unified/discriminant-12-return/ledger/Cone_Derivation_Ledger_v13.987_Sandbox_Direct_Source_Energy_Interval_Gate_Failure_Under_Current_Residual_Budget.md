# Cone Derivation Ledger v13.987 — Sandbox: Direct Source-Energy Interval Gate Fails Under Current Residual Budget

**Date:** 2026-10-03  
**Track:** Sandbox / no-twist Suzuki Xi scalar certification lane  
**Status:** [D] instantiated v13.981 error budget from the repaired arbitrary-carrier payload; [D] inverse-stability gate fails by ~14–15 orders of magnitude in both parities; [G] nominal corrected 6D energies are not promoted because the matrices are too ill-conditioned relative to certified perturbation radii; [I] direct source-energy route is currently too coarse; [O] continue with scale-free phase/first-jet certification or materially sharpen source/complement residuals  
**Authorization:** Jeremy, 2026-10-03 ("continue" / live residual-cross payload landed)  
**Parents:** v13.978–982, v13.985–986  
**Collision check:** v13.987 was absent immediately before this write.

---

## 0. Purpose

The residual-cross payload is now frozen and the committed remote-residual certificate supplies transformed residual totals for all seven constrained complement solves in both parities.

Therefore v13.981 can finally be instantiated.

The decisive question is the inverse-stability condition

\[
\varepsilon_M
<
\widehat\mu,
\qquad
\widehat\mu
=
\sigma_{\min}(\widehat{\mathcal M}).
\]

The answer, with the current rigorous residual budgets, is **no** in both parities by an enormous margin.

This is a useful negative result: the source-energy interval theorem is structurally correct, but the available perturbation norm is much too large for a global inverse-norm enclosure of the extremely near-singular reduced matrices.

---

## 1. Corrected arbitrary-carrier nominal matrices [N]

Use the repaired arbitrary-carrier data:

\[
\widehat{\mathcal M}
=
\begin{pmatrix}
\widehat H_C & \widehat K_{\rm eff}^T\\
\widehat K_{\rm eff} & \widehat J_{\rm eff}
\end{pmatrix},
\]

with

\[
\widehat f
=
\binom{
(\widehat f_6)_{1:2}
}{
\widehat s_{\rm eff}
},
\]

and the regular background

\[
\widehat h=\widehat h_{\rm reg}.
\]

The upper source block and regular background come from v13.982; the lower source block and corrected carrier/coupling blocks come from the residual-cross payload.

No reopened v13.977 incomplete-carrier data are used.

---

## 2. Certified transformed residual totals [D/N-cert]

The committed

\[
\texttt{p4\_payload\_kkt\_residual\_cross/cert\_totals.json}
\]

gives:

### even-v

\[
e_{C,1}=0.001143113659867295,
\]

\[
e_{C,2}=0.0033761214961490877,
\]

\[
e_f=6.345257042022136,
\]

\[
(e_{R,1},e_{R,2},e_{R,3},e_{R,4})
=
(
2.5579689820242703\times10^{-7},
3.7638835995739965\times10^{-6},
6.606183055064243\times10^{-4},
4.068540511882385\times10^{-2}
).
\]

### odd-v

\[
e_{C,1}=0.001978370588356106,
\]

\[
e_{C,2}=0.004014001687863045,
\]

\[
e_f=0.2651336618285081,
\]

\[
(e_{R,1},e_{R,2},e_{R,3},e_{R,4})
=
(
8.92664679238643\times10^{-8},
7.96450660691399\times10^{-6},
1.0027124437315032\times10^{-3},
4.209243464768428\times10^{-2}
).
\]

These are already transformed-norm residual totals including the certified remote tail.

---

## 3. Exact-complement action errors [D]

v13.980 gives, for each constrained solve,

\[
\delta
\le
M(e+\rho\eta)+\eta,
\]

where

\[
M_e<10.152566,
\qquad
\rho_e<0.00580,
\]

and

\[
M_o<10.302509,
\qquad
\rho_o<0.00880.
\]

The frozen finite constraint defects are tiny compared with the transformed residual totals, so they do not affect the displayed digits below.

### even-v

The two core-column action errors are approximately

\[
\delta_{C,1}\approx0.0116055,
\qquad
\delta_{C,2}\approx0.0342763.
\]

Hence

\[
\boxed{
\Delta_{C,e}
\approx
0.0361877.
}
\]

The four residual-column action errors have combined norm

\[
\boxed{
\Delta_{R,e}
\approx
0.413116.
}
\]

The source complement action error is

\[
\boxed{
\delta_{f,e}
\approx
64.4206.
}
\]

### odd-v

Similarly,

\[
\boxed{
\Delta_{C,o}
\approx
0.0461043,
}
\]

\[
\boxed{
\Delta_{R,o}
\approx
0.433781,
}
\]

and

\[
\boxed{
\delta_{f,o}
\approx
2.73154.
}
\]

---

## 4. v13.981 matrix perturbation radii [D]

Use the certified coupling caps

\[
c_e\le0.160,
\qquad
\rho_e\le0.00580,
\]

\[
c_o\le0.204,
\qquad
\rho_o\le0.00880.
\]

Then v13.981 gives

\[
\varepsilon_M
=
c\Delta_C
+
c\Delta_R
+
\rho\Delta_R.
\]

Therefore

### even-v

\[
\boxed{
\varepsilon_{M,e}
\approx
0.0742846.
}
\]

### odd-v

\[
\boxed{
\varepsilon_{M,o}
\approx
0.101714.
}
\]

These values do not include any hidden projector-replacement error; v13.980 removes that term entirely.

---

## 5. Corrected 6D singular values [N]

The corrected nominal reduced matrices have smallest singular values

\[
\boxed{
\widehat\mu_e
=
\sigma_{\min}(\widehat{\mathcal M}_e)
\approx
2.22\times10^{-16},
}
\]

and

\[
\boxed{
\widehat\mu_o
=
\sigma_{\min}(\widehat{\mathcal M}_o)
\approx
2.02\times10^{-16}.
}
\]

Thus

\[
\boxed{
\frac{\varepsilon_{M,e}}{\widehat\mu_e}
\approx
3.35\times10^{14},
}
\]

and

\[
\boxed{
\frac{\varepsilon_{M,o}}{\widehat\mu_o}
\approx
5.04\times10^{14}.
}
\]

The required v13.981 hypothesis

\[
\varepsilon_M<\widehat\mu
\]

fails overwhelmingly in both sectors.

---

## 6. Consequence: no rigorous source-energy interval yet [D/G]

Because

\[
\varepsilon_M
\gg
\widehat\mu,
\]

the Weyl singular-value perturbation step in v13.981 gives no lower bound on

\[
\sigma_{\min}(\mathcal M).
\]

Therefore equations (21)–(28) of v13.981 cannot be instantiated with the present global perturbation norm.

In particular:

\[
\boxed{
\textbf{no rigorous parity source-energy interval is obtained from the current residual budget.}
}
\]

and hence

\[
\boxed{
\textbf{no rigorous }\kappa_{a=1}^{\Xi}\textbf{ interval follows from the direct source-energy route at this stage.}
}
\]

---

## 7. Nominal near-singularity is not itself a theorem [G]

The corrected nominal matrices contain several singular values/eigenvalues at approximately \(10^{-15}\)–\(10^{-16}\) scale.

Float64 evaluation of the nominal reduced quadratic forms is therefore extremely sensitive.

For example, the even nominal matrix contains a tiny negative eigenvalue at the level of floating-point/certification uncertainty.

Accordingly:

\[
\boxed{
\textbf{no nominal corrected energy or }\kappa\textbf{ value is promoted from these raw solves.}
}
\]

The reopened \(\kappa\approx0.792\) incomplete-carrier diagnostic remains superseded by v13.978 and is not restored.

---

## 8. Source residual is the largest immediate obstruction [I]

The dominant certified complement-action error is the source solve:

\[
\delta_{f,e}\approx64.4,
\qquad
\delta_{f,o}\approx2.73.
\]

Even if the source error were dramatically sharpened, however, the current matrix perturbation radius would still need to be reduced by many orders of magnitude to satisfy the global

\[
\varepsilon_M<\widehat\mu
\]

criterion.

Thus the issue is not merely one loose source-tail estimate.

The deeper problem is that v13.981 uses a **global inverse-norm perturbation theorem** on a genuinely near-singular six-dimensional matrix.

That theorem is too blunt for the scalar observable.

---

## 9. Correct pivot: scale-free scalar observables [I]

The failure of the direct energy gate validates the parallel route already developed in v13.965 and v13.985.

The Xi scalar is scale-free:

\[
\kappa_a^\Xi
=
m_a'(i)
=
-i\operatorname{Tr}
\left[
(H_{a,0}-i)^{-1}
-
(H_{a,\pi}-i)^{-1}
\right],
\]

and equivalently

\[
\kappa_a^\Xi
=
2\int_0^\infty
\operatorname{sgn}m_a(t)
\frac{t}{(1+t^2)^2}\,dt.
\]

These representations do not require certifying the absolute amplitude of the source-active near-null inverse.

The next gate should therefore target:

1. normalized/phase characteristic information;
2. first-jet or rank-one trace data;
3. sign boxes of the Weyl ratio;

rather than an absolute bound on

\[
\|\mathcal M^{-1}\|.
\]

---

## 10. Result

The repaired residual-cross payload fully instantiates the v13.981 error budget.

The theorem does **not** close numerically with the present residuals:

\[
\boxed{
\varepsilon_{M,e}\approx7.43\times10^{-2}
\gg
2.22\times10^{-16}\approx\widehat\mu_e,
}
\]

\[
\boxed{
\varepsilon_{M,o}\approx1.02\times10^{-1}
\gg
2.02\times10^{-16}\approx\widehat\mu_o.
}
\]

Therefore the direct source-energy route is presently noncertifying.

The correct next step is the scale-free phase/first-jet route, for which the near-null common amplitude is not itself the quantity being bounded.
