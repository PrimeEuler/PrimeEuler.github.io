# Cone Derivation Ledger v13.981 — Sandbox: Six-Dimensional Source-Energy Interval Theorem for the Xi Scalar

**Date:** 2026-10-03  
**Track:** Sandbox / no-twist Suzuki Xi scalar certification lane  
**Status:** [D] direct source-energy enclosure from residual-certified arbitrary-carrier Feshbach data; [D] explicit propagation of the seven complement-solve errors to the 6D matrix/source/background; [D] direct interval formula for \(\kappa\); [I] source-energy route can close before the full phase sweep; [O] instantiate with the v13.978 residual-cross payload and the remote-residual certificate  
**Authorization:** Jeremy, 2026-10-03 ("awesome continue")  
**Parents:** v13.965, v13.971, v13.978–980  
**Research artifact:** research-notes/suzuki_kkt_remote_residual_certificate.py, commit 01e2f99aef44dc6c2900f6d8fa7ab677e5f24762  
**Collision check:** v13.981 was absent immediately before this write.

---

## 0. Purpose

The phase route remains exact and valuable, but the Xi scalar also satisfies

\[
\boxed{
\kappa_a^\Xi
=
\frac{E_e-E_o}{E_e+E_o},
}
\tag{1}
\]

where

\[
E_e
=
\langle f_e,A_e^{-1}f_e\rangle,
\qquad
E_o
=
\langle f_o,A_o^{-1}f_o\rangle.
\]

After v13.980, each parity source energy is an exact arbitrary-carrier \(6\times6\) Feshbach quantity plus a regular complement background.

Therefore the first rigorous scalar interval may be obtained without certifying an entire real-axis sign pattern.

---

## 1. Exact arbitrary-carrier source energy [D]

Fix one parity.

Let

\[
\mathcal M
\]

be the exact arbitrary-carrier Feshbach matrix of v13.980,

\[
f
\]

its exact reduced source, and

\[
h
\]

the exact regular complement source background.

Then

\[
\boxed{
E
=
h+f^*\mathcal M^{-1}f.
}
\tag{2}
\]

This identity is exact for the full operator whenever the chosen numerical-carrier complement is invertible.

---

## 2. Approximate complement inverse actions [D]

Let the two core-coupling complement solves have certified errors

\[
\delta_{C,1},\qquad
\delta_{C,2},
\]

the four Ritz-residual complement solves have certified errors

\[
\delta_{R,1},\ldots,\delta_{R,4},
\]

and the source complement solve have certified error

\[
\delta_f.
\]

These are errors in transformed tail norm:

\[
\|y-\widehat y\|.
\]

Define

\[
\boxed{
\Delta_C
=
\sqrt{
\delta_{C,1}^2+\delta_{C,2}^2
},
}
\tag{3}
\]

\[
\boxed{
\Delta_R
=
\sqrt{
\sum_{j=1}^4\delta_{R,j}^2
}.
}
\tag{4}
\]

Let

\[
C=B_T^{-1/2}A_{TC},
\]

and let

\[
K=\widehat QJY
\]

be the transformed Ritz-residual cross block.

Assume certified norm bounds

\[
\boxed{
\|C\|\le c,
\qquad
\|K\|\le\rho.
}
\tag{5}
\]

---

## 3. Error in the 6D matrix [D]

The exact core block is

\[
H_C
=
A_{CC}
-
C_Q^*\widehat D^{-1}C_Q.
\]

Replacing the two complement columns by certified approximations gives

\[
\boxed{
\|H_C-\widehat H_C\|
\le
c\Delta_C.
}
\tag{6}
\]

The exact core/carrier block is

\[
K_{\rm eff}
=
C_P-K^*\widehat D^{-1}C_Q.
\]

The four Ritz-residual solves give

\[
\boxed{
\|K_{\rm eff}-\widehat K_{\rm eff}\|
\le
c\Delta_R.
}
\tag{7}
\]

The exact carrier block is

\[
J_{\rm eff}
=
\Theta-K^*\widehat D^{-1}K.
\]

Hence

\[
\boxed{
\|J_{\rm eff}-\widehat J_{\rm eff}\|
\le
\rho\Delta_R.
}
\tag{8}
\]

Therefore, for the self-adjoint \(6\times6\) matrix perturbation,

\[
\mathcal M-\widehat{\mathcal M}
=
\begin{pmatrix}
\Delta H&\Delta K^*\\
\Delta K&\Delta J
\end{pmatrix},
\]

the off-diagonal block matrix has norm exactly \(\|\Delta K\|\), so

\[
\boxed{
\|\mathcal M-\widehat{\mathcal M}\|
\le
\varepsilon_M,
}
\tag{9}
\]

where a safe bound is

\[
\boxed{
\varepsilon_M
=
c\Delta_C
+
c\Delta_R
+
\rho\Delta_R.
}
\tag{10}
\]

Finite arithmetic/operator-entry radii may be added explicitly to \(\varepsilon_M\).

---

## 4. Error in the reduced source [D]

The exact upper source block is

\[
f_C-C_Q^*\widehat D^{-1}g_Q.
\]

Hence

\[
\boxed{
\|\Delta f_C\|
\le
c\delta_f.
}
\tag{11}
\]

The exact lower carrier source is

\[
g_P-K^*\widehat D^{-1}g_Q.
\]

Thus

\[
\boxed{
\|\Delta f_P\|
\le
\rho\delta_f.
}
\tag{12}
\]

Consequently

\[
\boxed{
\|f-\widehat f\|
\le
\varepsilon_f,
}
\tag{13}
\]

with

\[
\boxed{
\varepsilon_f
=
\sqrt{c^2+\rho^2}\,\delta_f.
}
\tag{14}
\]

Any source-arithmetic radius is added separately.

---

## 5. Error in the regular source background [D]

Let

\[
g=B_T^{-1/2}f_T.
\]

The exact regular term is

\[
h
=
\langle
g_Q,
\widehat D^{-1}g_Q
\rangle.
\]

Therefore

\[
\boxed{
|h-\widehat h|
\le
\|g_Q\|\delta_f
\le
\|g\|\delta_f.
}
\tag{15}
\]

Define a certified source-norm cap

\[
\|g\|\le g_*.
\]

Then

\[
\boxed{
|h-\widehat h|
\le
\varepsilon_h
:=
g_*\delta_f.
}
\tag{16}
\]

A crude fully analytic value follows from

\[
B_T\succeq\beta I
\]

and Parseval:

\[
g_*
\le
\frac{\|f_{\rm parity}\|_2}{\sqrt\beta}.
\]

At \(a=1\),

\[
\| \cosh x\|_{L^2(-1,1)}^2
=
1+\frac{\sinh2}{2},
\]

\[
\| \sinh x\|_{L^2(-1,1)}^2
=
\frac{\sinh2}{2}-1.
\]

With the public smooth-bulk floors

\[
\beta_e=0.00830,
\qquad
\beta_o=0.20500,
\]

one obtains the crude caps

\[
\boxed{
g_{*,e}<18.412,
}
\tag{17}
\]

\[
\boxed{
g_{*,o}<1.993.
}
\tag{18}
\]

---

## 6. Inverse stability of the reduced matrix [D]

Let

\[
\widehat\mu
=
\sigma_{\min}
(
\widehat{\mathcal M}
).
\]

Assume

\[
\boxed{
\varepsilon_M<\widehat\mu.
}
\tag{19}
\]

Then Weyl's inequality gives

\[
\boxed{
\sigma_{\min}(\mathcal M)
\ge
\widehat\mu-\varepsilon_M
>0.
}
\tag{20}
\]

Hence

\[
\boxed{
\|\mathcal M^{-1}\|
\le
\frac1{\widehat\mu-\varepsilon_M}.
}
\tag{21}
\]

No sign-definiteness of \(\mathcal M\) is required for this invertibility estimate.

---

## 7. Solution-vector enclosure [D]

Let

\[
\widehat w
=
\widehat{\mathcal M}^{-1}\widehat f.
\]

The exact equation is

\[
\mathcal Mw=f.
\]

At \(\widehat w\),

\[
f-\mathcal M\widehat w
=
(f-\widehat f)
-
(\mathcal M-\widehat{\mathcal M})\widehat w.
\]

Therefore

\[
\boxed{
\|f-\mathcal M\widehat w\|
\le
\varepsilon_f
+
\varepsilon_M\|\widehat w\|.
}
\tag{22}
\]

Using (21),

\[
\boxed{
\|w-\widehat w\|
\le
\delta_w,
}
\tag{23}
\]

where

\[
\boxed{
\delta_w
=
\frac{
\varepsilon_f
+
\varepsilon_M\|\widehat w\|
}{
\widehat\mu-\varepsilon_M
}.
}
\tag{24}
\]

---

## 8. Source quadratic-form interval [D]

Define

\[
\widehat q
=
\widehat f^*\widehat w.
\]

The exact reduced quadratic form is

\[
q=f^*w.
\]

Then

\[
\boxed{
|q-\widehat q|
\le
\varepsilon_f\|\widehat w\|
+
(\|\widehat f\|+\varepsilon_f)\delta_w.
}
\tag{25}
\]

Combining with the regular background,

\[
E=h+q,
\qquad
\widehat E=\widehat h+\widehat q,
\]

gives

\[
\boxed{
|E-\widehat E|
\le
\varepsilon_E,
}
\tag{26}
\]

where

\[
\boxed{
\varepsilon_E
=
\varepsilon_h
+
\varepsilon_f\|\widehat w\|
+
(\|\widehat f\|+\varepsilon_f)\delta_w.
}
\tag{27}
\]

Thus

\[
\boxed{
E
\in
[
\widehat E-\varepsilon_E,\,
\widehat E+\varepsilon_E
].
}
\tag{28}
\]

---

## 9. Direct interval for \(\kappa\) [D]

Suppose

\[
E_e\in[L_e,U_e],
\]

\[
E_o\in[L_o,U_o],
\]

with

\[
L_e>0,
\qquad
L_o>0.
\]

Since

\[
\kappa(E_e,E_o)
=
\frac{E_e-E_o}{E_e+E_o}
\]

is increasing in \(E_e\) and decreasing in \(E_o\),

\[
\boxed{
\kappa_a^\Xi
\in
\left[
\frac{L_e-U_o}{L_e+U_o},
\,
\frac{U_e-L_o}{U_e+L_o}
\right].
}
\tag{29}
\]

If either energy interval crosses zero, one instead applies ordinary interval division while separately proving that

\[
E_e+E_o
\]

does not contain zero.

---

## 10. Why this route may close first [I]

The phase certificate requires controlling

\[
F(t)
\]

over a real window.

The source-energy route requires only:

- seven complement inverse actions per parity;
- one corrected \(6\times6\) matrix;
- one corrected six-vector;
- one scalar regular background.

All are static.

Thus the proof order can be

\[
\boxed{
\text{certify }E_e,E_o
\to
\text{certify }\kappa
}
\]

first, with the phase-window certificate retained as an independent functional cross-check.

---

## 11. Remaining inputs [O]

The committed remote-residual reproducer targets exactly

\[
\delta_{C,j},
\qquad
\delta_{R,j},
\qquad
\delta_f.
\]

The v13.979 numerical-complement gap converts transformed residuals into complement-solve errors.

When the v13.978 residual-cross payload lands, this theorem can be instantiated directly.

---

## 12. Result

Certified complement-solve errors give explicit intervals for

\[
\mathcal M,\quad f,\quad h,
\]

which give explicit intervals for the parity source energies

\[
E_e,\quad E_o,
\]

and hence directly

\[
\boxed{
\kappa_a^\Xi
=
\frac{E_e-E_o}{E_e+E_o}.
}
\]

The real-axis phase theorem remains an independent verification channel rather than a necessary first step.
