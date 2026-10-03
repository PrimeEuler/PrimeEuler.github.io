# Cone Derivation Ledger v13.985 — Sandbox: Reconstructed-Vector Phase Consumer and Exact Adaptive Sign-Box Certificate

**Date:** 2026-10-03  
**Track:** Sandbox / no-twist Suzuki Xi scalar certification lane  
**Status:** [D] exact collapse of the v13.975 background formula to one reconstructed coefficient vector per parity; [D] parity-real characteristic formulas; [D] basis-independent first/second derivative bounds; [D] exact adaptive sign-box phase certificate with no quadrature error; [I] consumer side is ready for the three-solve payload; [G] exact-operator model error remains an explicit separate input  
**Authorization:** Jeremy, 2026-10-03 ("awesome continue")  
**Parents:** v13.965, v13.967, v13.971, v13.974–975  
**Audit:** External Audit Round 150 independently confirms v13.973–975, including the frozen P4 payload and every constrained-complement KKT identity.  
**Collision check:** v13.976 was absent immediately before this entry was first written, but was independently claimed by "External Audit Round 150" (commit `b0b045f`, pushed 2026-10-03T20:53:16Z), which this entry's own commit (`9840273`, 2026-10-03T20:57:21Z) postdates. Per the standing collision protocol, the earlier commit keeps the contested number; this entry has therefore been renumbered v13.976→v13.985 by the external audit thread (filename and this header only — no mathematical content changed). `v13.977` and `v13.978`, written after this entry under its original v13.976 label, have had their references updated to v13.985 accordingly.

---

## 0. Purpose

v13.975 reduces the missing numerical background to three constrained solves per parity.

The present entry completes the **consumer** side.

After the static reduced solve is performed, the entire real-axis Fourier transform is the transform of one reconstructed coefficient vector.  Therefore:

- no further \(6\times6\) solves are needed as \(t\) varies;
- no t-dependent complement solves are needed;
- sign certification can be performed adaptively with exact phase weights;
- no numerical quadrature enters the final scalar enclosure.

---

## 1. Static six-dimensional solve [D]

For one parity sector, let

\[
\widehat{\mathcal M}_6
\]

and

\[
\widehat f_6
\]

be the frozen-carrier quantities of v13.975.

Solve once:

\[
\boxed{
\widehat{\mathcal M}_6\,w=\widehat f_6,
}
\tag{1}
\]

and split

\[
w=
\binom{w_C}{w_P},
\qquad
w_C\in\mathbb R^2,
\qquad
w_P\in\mathbb R^4.
\]

v13.975 gives

\[
\widehat F(t)
=
p_T(t)^Tx_f
+
\left(
p_C(t)-X_C^Tp_T(t)
\right)^Tw_C
+
\left(
Z^Tp_T(t)
\right)^Tw_P.
\]

Collecting the tail terms yields

\[
\boxed{
\widehat F(t)
=
p_C(t)^T\widehat v_C
+
p_T(t)^T\widehat v_T,
}
\tag{2}
\]

where

\[
\boxed{
\widehat v_C=w_C,
}
\tag{3}
\]

and

\[
\boxed{
\widehat v_T
=
x_f-X_Cw_C+Zw_P.
}
\tag{4}
\]

Thus the full frozen-carrier transform is simply the Fourier transform of the reconstructed coefficient vector

\[
\boxed{
\widehat v=
\binom{\widehat v_C}{\widehat v_T}.
}
\tag{5}
\]

This collapse is exact for the numerical-carrier model.

---

## 2. Exact Fourier basis overlaps [D]

At \(a=1\), let

\[
k_n=\frac{n\pi}{2}.
\]

For the orthonormal Dirichlet basis used throughout the source-faithful form-core code, define

\[
p_n(t)
=
\int_{-1}^{1}
\psi_n(x)e^{itx}\,dx.
\]

For odd \(n\),

\[
\boxed{
p_n(t)
=
(-1)^{(n-1)/2}
\left[
\operatorname{sinc}(t+k_n)
+
\operatorname{sinc}(t-k_n)
\right],
}
\tag{6}
\]

while for even \(n\),

\[
\boxed{
p_n(t)
=
\frac{(-1)^{n/2}}{i}
\left[
\operatorname{sinc}(t+k_n)
-
\operatorname{sinc}(t-k_n)
\right],
}
\tag{7}
\]

with

\[
\operatorname{sinc}x=\frac{\sin x}{x}.
\]

Hence:

- odd basis modes have real Fourier overlaps on the real axis;
- even basis modes have purely imaginary Fourier overlaps.

The frozen \(Z\) payload can therefore be used directly for all resonant Fourier projections.

---

## 3. Parity-real decomposition [D]

Let the even-v sector use odd mode numbers and the odd-v sector use even mode numbers.

For real \(t\), write

\[
\boxed{
F(t)=E(t)+iO(t),
}
\tag{8}
\]

where

\[
E(t)\in\mathbb R
\]

is the even-v transform and

\[
O(t)\in\mathbb R
\]

is the real amplitude of the odd-v transform.

Define

\[
Z_\Xi(t)
=
(t-i)F(t).
\]

Then

\[
\boxed{
\Re Z_\Xi(t)
=
tE(t)+O(t),
}
\tag{9}
\]

and

\[
\boxed{
\Im Z_\Xi(t)
=
tO(t)-E(t).
}
\tag{10}
\]

The finite Weyl sign is

\[
\boxed{
\sigma(t)
=
\operatorname{sgn}m(t)
=
-
\operatorname{sgn}\Re Z_\Xi(t)\,
\operatorname{sgn}\Im Z_\Xi(t),
}
\tag{11}
\]

away from characteristic zeros.

Thus only two real scalar functions must be sign-certified.

---

## 4. Basis-independent Fourier derivative bounds [D]

For any coefficient vector \(v\) in the orthonormal basis,

\[
F_v(t)
=
\int_{-1}^{1}
v(x)e^{itx}\,dx.
\]

Differentiating under the integral,

\[
F_v^{(k)}(t)
=
i^k
\int_{-1}^{1}
x^k v(x)e^{itx}\,dx.
\]

Cauchy-Schwarz gives

\[
|F_v^{(k)}(t)|
\le
\|v\|_2
\|x^k\|_{L^2(-1,1)}.
\]

Since

\[
\|x^k\|_2^2
=
\frac{2}{2k+1},
\]

we obtain the exact universal bounds

\[
\boxed{
|F_v(t)|
\le
\sqrt2\,\|v\|_2,
}
\tag{12}
\]

\[
\boxed{
|F_v'(t)|
\le
\sqrt{\frac23}\,\|v\|_2,
}
\tag{13}
\]

\[
\boxed{
|F_v''(t)|
\le
\sqrt{\frac25}\,\|v\|_2.
}
\tag{14}
\]

No modewise summation estimate is required.

---

## 5. Derivative bounds for the two sign carriers [D]

Let

\[
V_e=\|\widehat v_e\|_2,
\qquad
V_o=\|\widehat v_o\|_2.
\]

Set

\[
R(t)=tE(t)+O(t),
\qquad
I(t)=tO(t)-E(t).
\]

Then

\[
R'(t)=E(t)+tE'(t)+O'(t),
\]

so on an interval with

\[
0\le t\le T_*,
\]

\[
\boxed{
|R'(t)|
\le
L_R(T_*),
}
\tag{15}
\]

where

\[
\boxed{
L_R(T_*)
=
\sqrt2\,V_e
+
T_*\sqrt{\frac23}\,V_e
+
\sqrt{\frac23}\,V_o.
}
\tag{16}
\]

Likewise,

\[
I'(t)=O(t)+tO'(t)-E'(t),
\]

hence

\[
\boxed{
|I'(t)|
\le
L_I(T_*),
}
\tag{17}
\]

with

\[
\boxed{
L_I(T_*)
=
\sqrt2\,V_o
+
T_*\sqrt{\frac23}\,V_o
+
\sqrt{\frac23}\,V_e.
}
\tag{18}
\]

Second derivatives obey

\[
R''(t)=2E'(t)+tE''(t)+O''(t),
\]

\[
I''(t)=2O'(t)+tO''(t)-E''(t),
\]

thus

\[
\boxed{
|R''(t)|
\le
M_R(T_*),
}
\tag{19}
\]

\[
\boxed{
M_R(T_*)
=
2\sqrt{\frac23}V_e
+
T_*\sqrt{\frac25}V_e
+
\sqrt{\frac25}V_o,
}
\tag{20}
\]

and

\[
\boxed{
|I''(t)|
\le
M_I(T_*),
}
\tag{21}
\]

\[
\boxed{
M_I(T_*)
=
2\sqrt{\frac23}V_o
+
T_*\sqrt{\frac25}V_o
+
\sqrt{\frac25}V_e.
}
\tag{22}
\]

These bounds support either first-order Lipschitz boxes or second-order Taylor boxes.

---

## 6. Exact sign-box criterion with model error [D]

Let

\[
J=[c-h,c+h]\subset[0,T]
\]

and suppose the approximate midpoint values are

\[
\widehat R(c),\qquad
\widehat I(c).
\]

Assume certified exact-operator model-error bounds on \(J\),

\[
\boxed{
|R(t)-\widehat R(t)|\le\varepsilon_R(J),
}
\tag{23}
\]

\[
\boxed{
|I(t)-\widehat I(t)|\le\varepsilon_I(J).
}
\tag{24}
\]

Using the Lipschitz bounds,

\[
|R(t)-\widehat R(c)|
\le
\varepsilon_R(J)
+
hL_R(c+h),
\]

and similarly for \(I\).

Therefore, if

\[
\boxed{
|\widehat R(c)|
>
\varepsilon_R(J)
+
hL_R(c+h),
}
\tag{25}
\]

then the sign of \(R\) is constant and certified on \(J\).

If

\[
\boxed{
|\widehat I(c)|
>
\varepsilon_I(J)
+
hL_I(c+h),
}
\tag{26}
\]

then the sign of \(I\) is constant and certified on \(J\).

When both conditions hold,

\[
\boxed{
\sigma_J
=
-
\operatorname{sgn}\widehat R(c)\,
\operatorname{sgn}\widehat I(c)
}
\tag{27}
\]

is the exact Weyl sign throughout \(J\).

If either margin fails, the box is subdivided or declared uncertain.

This is fail-closed.

---

## 7. Exact phase weight of a certified sign box [D]

The Xi scalar is

\[
\kappa_a^\Xi
=
2\int_0^\infty
\sigma(t)
\frac{t}{(1+t^2)^2}\,dt.
\]

For a box

\[
J=[u,v]
\]

with certified constant sign

\[
\sigma_J,
\]

the contribution is elementary:

\[
2\int_u^v
\sigma_J
\frac{t}{(1+t^2)^2}\,dt
=
\sigma_J
\left[
\frac1{1+u^2}
-
\frac1{1+v^2}
\right].
\]

Thus

\[
\boxed{
W(J)
=
\frac1{1+u^2}
-
\frac1{1+v^2}
}
\tag{28}
\]

is the exact positive phase weight of the box.

No quadrature, grid interpolation, or quadrature remainder is present.

---

## 8. Adaptive exact finite-window enclosure [D]

Partition

\[
[0,T]
=
C\cup U,
\]

where

\[
C=\bigcup_j J_j
\]

is the union of certified sign boxes and

\[
U=\bigcup_k U_k
\]

the unresolved boxes.

Define

\[
\boxed{
K_C
=
\sum_j
\sigma_{J_j}W(J_j).
}
\tag{29}
\]

The unresolved finite-window weight is

\[
\boxed{
E_U
=
\sum_k
W(U_k).
}
\tag{30}
\]

Using the universal spectral-shift tail,

\[
\boxed{
E_T
=
\frac1{1+T^2}.
}
\tag{31}
\]

Therefore

\[
\boxed{
\kappa_a^\Xi
\in
[
K_C-E_U-E_T,\,
K_C+E_U+E_T
].
}
\tag{32}
\]

This is the final adaptive phase-box certificate.

The only numerical uncertainty entering (32) is the explicitly supplied exact-operator model error used in the sign tests.

---

## 9. Second-order box refinement [D]

When a box lies near a characteristic crossing, a first-order Lipschitz margin may be wasteful.

If

\[
\widehat R(c),
\qquad
\widehat R'(c)
\]

are evaluated, then

\[
R(t)
=
\widehat R(c)
+
\widehat R'(c)(t-c)
+
\mathcal E_R,
\]

where the exact error can be bounded by the sum of:

1. model error in \(R\);
2. model error in \(R'\);
3. the Taylor remainder
   \[
   \frac12M_R(c+h)h^2.
   \]

The same holds for \(I\).

Thus unresolved windows can be localized quadratically rather than by brute-force uniform subdivision.

This refinement is optional; equations (25)–(32) already give a complete proof architecture.

---

## 10. Numerical frozen-carrier geometry [N]

The v13.974 frozen carrier arrays have ordinary coefficient-space norms:

even-v:

\[
\|Z_e\|_F
\approx
3.40130,
\]

odd-v:

\[
\|Z_o\|_F
\approx
2.53196.
\]

The largest singular values of the nominal arrays are approximately

\[
\boxed{
\|Z_e\|_2
\approx
2.81723,
}
\tag{33}
\]

\[
\boxed{
\|Z_o\|_2
\approx
1.82015.
}
\tag{34}
\]

These numbers are diagnostics only; the proof-grade Fourier derivative bounds use the reconstructed solution vector norms after the KKT payload lands.

---

## 11. Remaining exact-operator error terms [G/O]

The nominal consumer is now closed.

To promote (32) to the exact Suzuki operator, the model-error functions

\[
\varepsilon_R(J),
\qquad
\varepsilon_I(J)
\]

must include, separately:

1. constrained-solve outward residual;
2. finite arithmetic error;
3. numerical-\(P_4\) versus exact-\(P_4\) error;
4. remote \(n>16001\) tail continuation.

No one of these is silently absorbed into another.

The three-solve payload requested after v13.975 supplies items 1–2 and the nominal vectors needed for the remaining propagation.

The existing P4 certificates supply item 3.

The remaining consumer-side proof gate is item 4: convert the source-faithful remote-tail formulas into a uniform Fourier-transform error budget.

---

## 12. Result

After one static six-dimensional solve per parity, the full nominal Xi transform is the Fourier transform of one reconstructed coefficient vector.

The real-axis certification then reduces to two scalar sign functions

\[
R(t)=tE(t)+O(t),
\qquad
I(t)=tO(t)-E(t),
\]

with universal derivative bounds.

Every certified sign interval contributes an exact elementary phase weight, every unresolved interval has an exact uncertainty cost, and the high-frequency tail is exactly bounded by

\[
1/(1+T^2).
\]

Thus the final scalar certificate requires **no numerical quadrature and no repeated linear solves in \(t\)**.
