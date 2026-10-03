# Cone Derivation Ledger v13.979 — Sandbox: Numerical-Complement Gap and One-Step Graph-Refinement Theorem

**Date:** 2026-10-03  
**Track:** Sandbox / no-twist Suzuki Xi scalar certification lane  
**Status:** [D] exact lower singular-value bound for the numerical-carrier complement from the exact P4 moat and projector angle; [D] exact graph-correction identity; [D] rigorous a-priori residual contraction bounds for one KKT graph step; [O] compare with the sandbox's four residual-KKT solves and re-Ritz replay  
**Authorization:** Jeremy, 2026-10-03 ("awesome continue")  
**Parents:** v13.823–836, v13.974, v13.978  
**Collision check:** v13.979 was absent immediately before this write.

---

## 0. Purpose

v13.978 corrects the arbitrary-carrier Feshbach reduction by restoring the Ritz-residual cross block

\[
K=\widehat QJY.
\]

The sandbox is now computing the four constrained solves required to eliminate that cross block.

Before those payloads land, the exact spectral moat and the certified projector angle already prove two useful facts:

1. the numerical-carrier complement
   \[
   \widehat D=\widehat QJ\widehat Q
   \]
   is invertible with an explicit inverse bound;

2. one exact graph correction
   \[
   Y\mapsto Y-X,\qquad X=\widehat D^{-1}K,
   \]
   contracts the Ritz residual by orders of magnitude.

---

## 1. Exact spectral data [D]

Let

\[
P=P_4=\mathbf1_{(-0.02,0.02)}(J),
\qquad
Q=I-P.
\]

Then

\[
\boxed{
\|J_P\|<a,
\qquad
a=0.02,
}
\tag{1}
\]

and the complementary spectrum satisfies

\[
\boxed{
|J_Q|\succeq bI,
\qquad
b=0.10.
}
\tag{2}
\]

Let

\[
\widehat P
\]

be any equal-rank orthogonal projector with

\[
\boxed{
\|P-\widehat P\|\le\varepsilon<1,
}
\tag{3}
\]

and set

\[
\widehat Q=I-\widehat P.
\]

---

## 2. Geometry of an approximate-complement vector [D]

Take

\[
x\in\operatorname{Ran}\widehat Q.
\]

Write

\[
x=p+q,
\qquad
p=Px,
\qquad
q=Qx.
\]

Because

\[
\widehat Px=0,
\]

\[
p
=
(P-\widehat P)x,
\]

so

\[
\boxed{
\|p\|\le\varepsilon\|x\|.
}
\tag{4}
\]

Orthogonality of \(p,q\) gives

\[
\boxed{
\|q\|
\ge
\sqrt{1-\varepsilon^2}\,\|x\|.
}
\tag{5}
\]

For every

\[
v\in\operatorname{Ran}Q,
\]

one likewise has

\[
\|\widehat Pv\|
\le
\varepsilon\|v\|,
\]

hence

\[
\boxed{
\|\widehat Qv\|
\ge
\sqrt{1-\varepsilon^2}\,\|v\|.
}
\tag{6}
\]

---

## 3. Numerical-complement lower singular value [D]

Define

\[
\widehat D
=
\widehat QJ\widehat Q
\]

on \(\operatorname{Ran}\widehat Q\).

For \(x\in\operatorname{Ran}\widehat Q\),

\[
\widehat Dx
=
\widehat QJ_Pp
+
\widehat QJ_Qq.
\]

The exact \(Q\)-term obeys

\[
\begin{aligned}
\|\widehat QJ_Qq\|
&\ge
\sqrt{1-\varepsilon^2}
\|J_Qq\|\\
&\ge
b\sqrt{1-\varepsilon^2}\|q\|\\
&\ge
b(1-\varepsilon^2)\|x\|.
\end{aligned}
\]

The exact \(P\)-term satisfies

\[
\|\widehat QJ_Pp\|
\le
a\|p\|
\le
a\varepsilon\|x\|.
\]

Therefore

\[
\boxed{
\|\widehat Dx\|
\ge
d(\varepsilon)\|x\|,
}
\tag{7}
\]

where

\[
\boxed{
d(\varepsilon)
=
b(1-\varepsilon^2)-a\varepsilon.
}
\tag{8}
\]

Whenever

\[
d(\varepsilon)>0,
\]

\[
\boxed{
\|\widehat D^{-1}\|
\le
\frac1{d(\varepsilon)}.
}
\tag{9}
\]

No sign-definiteness of \(J_Q\) is required; only the absolute spectral moat enters.

---

## 4. Apply to the unchanged frozen P4 carrier [D]

The later block-energy refinement applies to the same v13.974 carrier and gives the public angle caps

\[
\varepsilon_e<0.0582,
\]

\[
\varepsilon_o<0.0984.
\]

Thus

### even-v

\[
d_e
>
0.10(1-0.0582^2)-0.02(0.0582)
=
0.098497276.
\]

Hence

\[
\boxed{
\|\widehat D_e^{-1}\|
<
10.152566.
}
\tag{10}
\]

### odd-v

\[
d_o
>
0.10(1-0.0984^2)-0.02(0.0984)
=
0.097063744.
\]

Hence

\[
\boxed{
\|\widehat D_o^{-1}\|
<
10.302509.
}
\tag{11}
\]

Therefore the constrained-complement KKT operator used in v13.975/v13.978 is analytically separated from singularity in both sectors.

---

## 5. Exact graph correction [D]

Let

\[
Y
\]

be an orthonormal numerical carrier,

\[
Y^*Y=I,
\]

with Ritz matrix

\[
\Theta=Y^*JY
\]

and transformed residual

\[
\boxed{
K=JY-Y\Theta.
}
\tag{12}
\]

Galerkin orthogonality gives

\[
Y^*K=0,
\]

so

\[
K\subset\operatorname{Ran}\widehat Q.
\]

Define the exact numerical-complement graph correction

\[
\boxed{
X=\widehat D^{-1}K.
}
\tag{13}
\]

Then

\[
\widehat DX=K.
\]

Since the carrier/complement cross block is \(K\),

\[
JX
=
YK^*X+\widehat DX
=
YK^*X+K.
\]

Also

\[
JY=Y\Theta+K.
\]

Subtract:

\[
\boxed{
J(Y-X)
=
Y\left(
\Theta-K^*X
\right).
}
\tag{14}
\]

Define

\[
\boxed{
S
=
\Theta-K^*X.
}
\tag{15}
\]

Then

\[
J(Y-X)=YS.
\]

---

## 6. Residual of the graph-corrected carrier [D]

Let

\[
\widetilde Y=Y-X.
\]

Because

\[
Y^*X=0,
\]

\[
\widetilde Y^*\widetilde Y
=
I+X^*X
\succeq I.
\]

Using the candidate coefficient matrix \(S\),

\[
\begin{aligned}
J\widetilde Y-\widetilde YS
&=
YS-(Y-X)S\\
&=
XS.
\end{aligned}
\]

Therefore

\[
\boxed{
\|J\widetilde Y-\widetilde YS\|
\le
\|X\|\,\|S\|.
}
\tag{16}
\]

After orthonormalizing

\[
\widetilde Y
\mapsto
\widetilde Y
(I+X^*X)^{-1/2},
\]

the residual norm cannot increase because

\[
\left\|
(I+X^*X)^{-1/2}
\right\|
\le1.
\]

A subsequent Rayleigh-Ritz step in this corrected span has orthogonal residual no larger than the residual obtained from the candidate coefficient matrix.

Hence (16) is a rigorous a-priori upper bound for the re-Ritz residual of the graph-corrected carrier.

---

## 7. A-priori contraction bound [D]

Let

\[
\rho=\|K\|.
\]

From (9) and (13),

\[
\boxed{
\|X\|
\le
M\rho,
\qquad
M:=\|\widehat D^{-1}\|.
}
\tag{17}
\]

Also

\[
\|S\|
\le
\|\Theta\|
+
\|K\|\,\|X\|
\le
\|\Theta\|+M\rho^2.
\]

Therefore

\[
\boxed{
\rho_{\rm new}
\le
M\rho
\left(
\|\Theta\|+M\rho^2
\right).
}
\tag{18}
\]

This bound requires no numerical information beyond the existing carrier caps.

---

## 8. Even-v quantitative target [D]

Use

\[
M_e<10.152566,
\]

\[
\rho_e<0.00580,
\]

and

\[
\|\Theta_e\|<0.00030.
\]

Then

\[
\boxed{
\|X_e\|<0.0588849,
}
\tag{19}
\]

\[
\boxed{
\|S_e\|<0.000641533,
}
\tag{20}
\]

and

\[
\boxed{
\rho_{e,\rm new}
<
3.778\times10^{-5}.
}
\tag{21}
\]

Using the conservative \(0.08\) exact moat,

\[
\boxed{
\|\sin\Theta_{\rm new,e}\|
<
4.73\times10^{-4}.
}
\tag{22}
\]

This is an a-priori bound.  The sandbox re-Ritz replay should report the actual certified value.

---

## 9. Odd-v quantitative target [D]

Use

\[
M_o<10.302509,
\]

\[
\rho_o<0.00880,
\]

and

\[
\|\Theta_o\|<0.01050.
\]

Then

\[
\boxed{
\|X_o\|<0.0906621,
}
\tag{23}
\]

\[
\boxed{
\|S_o\|<0.0112979,
}
\tag{24}
\]

and

\[
\boxed{
\rho_{o,\rm new}
<
1.025\times10^{-3}.
}
\tag{25}
\]

Using the conservative \(0.08\) moat,

\[
\boxed{
\|\sin\Theta_{\rm new,o}\|
<
1.281\times10^{-2}.
}
\tag{26}
\]

Again this is an a-priori certified target; direct residual replay may sharpen it.

---

## 10. Consequence for the residual-cross payload [D/I]

The four additional v13.978 KKT solves compute precisely the graph matrix

\[
X=\widehat D^{-1}K.
\]

Thus the correction payload simultaneously serves two purposes:

1. it repairs the arbitrary-carrier \(6\times6\) Feshbach matrix exactly;
2. it constructs a substantially improved approximate \(P_4\) carrier
   \[
   \widetilde Y=Y-X.
   \]

The even-sector subspace error is predicted to improve by roughly two orders of magnitude, while the odd sector improves by approximately one order of magnitude.

This should sharply reduce the dominant exact-\(P_4\) uncertainty in the grouped residues and source coordinates.

---

## 11. Guardrails

This entry does not claim:

- the graph-corrected carrier is exact \(P_4\);
- the sandbox residual replay has already passed;
- the corrected finite-a scalar has any particular value;
- convergence to the Xi target;
- RH or GRH.

The numerical \(\kappa\approx0.792\) values from the incomplete v13.977 model remain reopened under v13.978.

---

## 12. Result

The frozen numerical complement is rigorously invertible:

\[
\boxed{
\|\widehat D_e^{-1}\|<10.153,
\qquad
\|\widehat D_o^{-1}\|<10.303.
}
\]

One exact graph correction

\[
X=\widehat D^{-1}K
\]

has the a-priori residual bounds

\[
\boxed{
\rho_{e,\rm new}<3.78\times10^{-5},
}
\]

\[
\boxed{
\rho_{o,\rm new}<1.03\times10^{-3}.
}
\]

Thus the v13.978 residual-cross solves are expected not only to repair the six-dimensional model but to produce a materially sharper certified \(P_4\) carrier.
