# Cone Derivation Ledger v13.745 — Closed Scalar Moment System for the Corrected Suzuki Deficiency Equation

Date: 2026-09-23

Status: derivation gate requested after v13.742–743. The affine terms in Suzuki's corrected Section-8 deficiency equation are retained explicitly. This entry derives the exact finite-dimensional closure obtained by applying the two boundary moment functionals to the one-channel deficiency equation. It also states precisely what is and is not closed without the inverse/resolvent of Suzuki's integral operator.

Synchronization: live head before write was v13.744, commit \`949ab493b2ead5e204baac3659214e0dd8a6fc25\`. v13.744 is a full-line Suzuki–Weil current correction and explicitly leaves the corrected finite-edge lane v13.742–743 open; no collision.

## 1. One-channel corrected deficiency equation

By reflection it suffices to use the \(+\) channel. Write Suzuki's actual equation (8.5) in the form
\[
\boxed{
\mathcal L_A v_A
=
C_A e^x+A_Ax+B_A,
}
\]
where
\[
\boxed{
A_A=-I_{1,A}-C_A,
\qquad
B_A=-I_{0,A}-C_A,
}
\]
and
\[
I_{0,A}:=\ell_{0,A}(v_A)
=
\int_{-A}^{A}k(0,y)v_A(y)\,dy,
\]
\[
I_{1,A}:=\ell_{1,A}(v_A)
=
\int_{-A}^{A}k_x(0,y)v_A(y)\,dy.
\]

Thus the equation with the affine terms displayed entirely in terms of the three scalar unknowns is
\[
\boxed{
\mathcal L_A v_A
=
C_A(e^x-1-x)-I_{1,A}x-I_{0,A}.
}
\tag{1}
\]

No affine term has been dropped.

## 2. Resolve the functional unknown once

Assume \(\mathcal L_A\) is invertible on the corrected deficiency-function space after Suzuki's domain/normalization conditions are imposed. Denote
\[
R_A:=\mathcal L_A^{-1}.
\]

Introduce the three response functions
\[
\boxed{
u_{e,A}:=R_A(e^x-1-x),
\qquad
u_{1,A}:=R_A1,
\qquad
u_{x,A}:=R_Ax.
}
\]

Then (1) is equivalent to
\[
\boxed{
v_A
=
C_Au_{e,A}
-I_{0,A}u_{1,A}
-I_{1,A}u_{x,A}.
}
\tag{2}
\]

This is the key finite-rank reduction: the full deficiency vector lies in the span of three fixed responses once the three scalar coefficients are known.

## 3. Apply the two exact boundary moment functionals

Define the \(2\times3\) response moments
\[
M_{0e}:=\ell_{0,A}(u_{e,A}),\qquad
M_{00}:=\ell_{0,A}(u_{1,A}),\qquad
M_{0x}:=\ell_{0,A}(u_{x,A}),
\]
\[
M_{1e}:=\ell_{1,A}(u_{e,A}),\qquad
M_{10}:=\ell_{1,A}(u_{1,A}),\qquad
M_{1x}:=\ell_{1,A}(u_{x,A}).
\]

Applying \(\ell_{0,A}\) and \(\ell_{1,A}\) to (2) gives
\[
I_{0,A}
=
C_AM_{0e}
-I_{0,A}M_{00}
-I_{1,A}M_{0x},
\]
\[
I_{1,A}
=
C_AM_{1e}
-I_{0,A}M_{10}
-I_{1,A}M_{1x}.
\]

Therefore
\[
\boxed{
(1+M_{00})I_{0,A}
+
M_{0x}I_{1,A}
=
M_{0e}C_A,
}
\tag{3}
\]
\[
\boxed{
M_{10}I_{0,A}
+
(1+M_{1x})I_{1,A}
=
M_{1e}C_A.
}
\tag{4}
\]

These are the two exact closed scalar moment equations forced by Suzuki's corrected deficiency equation.

## 4. Explicit solution for \(I_0/C\) and \(I_1/C\)

Define
\[
\boxed{
D_A
:=
(1+M_{00})(1+M_{1x})-M_{0x}M_{10}.
}
\]

If \(D_A\ne0\), Cramer's rule gives
\[
\boxed{
\frac{I_{0,A}}{C_A}
=
\frac{
M_{0e}(1+M_{1x})-M_{0x}M_{1e}
}{
D_A
},
}
\tag{5}
\]
\[
\boxed{
\frac{I_{1,A}}{C_A}
=
\frac{
(1+M_{00})M_{1e}-M_{10}M_{0e}
}{
D_A
}.
}
\tag{6}
\]

Thus the two affine coefficients relative to the deficiency normalization are already determined by the six resolvent moments.

Specifically,
\[
\boxed{
\frac{A_A}{C_A}
=
-1-\frac{I_{1,A}}{C_A},
}
\]
\[
\boxed{
\frac{B_A}{C_A}
=
-1-\frac{I_{0,A}}{C_A}.
}
\]

## 5. Edge-contamination coefficients in closed form

Recall
\[
\alpha_A=\frac{A_A}{C_Ae^A},
\qquad
\beta_A=\frac{AA_A+B_A}{C_Ae^A}.
\]

Using (5)–(6),
\[
\boxed{
\alpha_A
=
-e^{-A}
\left[
1+
\frac{
(1+M_{00})M_{1e}-M_{10}M_{0e}
}{D_A}
\right].
}
\tag{7}
\]

And
\[
\boxed{
\beta_A
=
-e^{-A}
\left[
A\left(
1+
\frac{
(1+M_{00})M_{1e}-M_{10}M_{0e}
}{D_A}
\right)
+
1+
\frac{
M_{0e}(1+M_{1x})-M_{0x}M_{1e}
}{D_A}
\right].
}
\tag{8}
\]

These are the exact scalar formulas to test numerically or asymptotically. They retain every affine contribution.

## 6. Where the equation for \(C_A\) comes from

Equations (3)–(4) are homogeneous in the common deficiency normalization:
\[
(C_A,I_{0,A},I_{1,A})
\mapsto
c(C_A,I_{0,A},I_{1,A}).
\]

This is unavoidable: a deficiency vector is defined only up to a nonzero scalar until Suzuki's chosen normalization is imposed.

Therefore the corrected deficiency equation **alone cannot determine the absolute value of \(C_A\)**.

Let Suzuki's normalization be represented by a linear functional
\[
\mathcal N_A(v_A)=\nu_A.
\]

Define
\[
N_e:=\mathcal N_A(u_{e,A}),
\qquad
N_0:=\mathcal N_A(u_{1,A}),
\qquad
N_x:=\mathcal N_A(u_{x,A}).
\]

Applying \(\mathcal N_A\) to (2) gives the third scalar equation
\[
\boxed{
N_eC_A-N_0I_{0,A}-N_xI_{1,A}
=
\nu_A.
}
\tag{9}
\]

Together, (3), (4), and (9) form the closed \(3\times3\) scalar system
\[
\boxed{
\begin{pmatrix}
M_{0e} & -(1+M_{00}) & -M_{0x}\\
M_{1e} & -M_{10} & -(1+M_{1x})\\
N_e & -N_0 & -N_x
\end{pmatrix}
\begin{pmatrix}
C_A\\ I_{0,A}\\ I_{1,A}
\end{pmatrix}
=
\begin{pmatrix}
0\\0\\\nu_A
\end{pmatrix}.
}
\tag{10}
\]

Equivalently, with the first two rows moved to the more conventional sign,
\[
\boxed{
\begin{pmatrix}
-M_{0e} & 1+M_{00} & M_{0x}\\
-M_{1e} & M_{10} & 1+M_{1x}\\
N_e & -N_0 & -N_x
\end{pmatrix}
\begin{pmatrix}
C_A\\ I_{0,A}\\ I_{1,A}
\end{pmatrix}
=
\begin{pmatrix}
0\\0\\\nu_A
\end{pmatrix}.
}
\]

The exact numerical \(C_A\) depends on Suzuki's actual normalization convention. The ratios \(I_0/C\), \(I_1/C\), and hence \(\alpha_A,\beta_A\), do not.

## 7. If the normalization is a point or boundary condition

For a common normalization
\[
v_A(x_*)=\nu_A,
\]
equation (9) becomes
\[
\boxed{
u_{e,A}(x_*)C_A
-u_{1,A}(x_*)I_{0,A}
-u_{x,A}(x_*)I_{1,A}
=
\nu_A.
}
\]

If instead Suzuki fixes an \(H(T_A)\)-norm, the scale equation is quadratic rather than linear:
\[
\|v_A\|_{T_A}^2=\nu_A^2.
\]
After inserting (2), this becomes one explicit quadratic equation in \((C_A,I_0,I_1)\); the projective ratios from (5)–(6) remain unchanged.

## 8. Symmetry simplifications available before computation

The interval is symmetric. If \(\mathcal L_A\) commutes with reflection, then
\[
u_{1,A}\ \text{is even},\qquad
u_{x,A}\ \text{is odd}.
\]

The moment kernels have parity
\[
k(0,y)\ \text{even},\qquad
k_x(0,y)\ \text{odd}.
\]

Consequently
\[
\boxed{
M_{0x}=0,
\qquad
M_{10}=0.
}
\tag{11}
\]

This diagonalizes the two moment equations:
\[
\boxed{
(1+M_{00})I_{0,A}=M_{0e}C_A,
}
\tag{12}
\]
\[
\boxed{
(1+M_{1x})I_{1,A}=M_{1e}C_A.
}
\tag{13}
\]

Hence, provided the denominators are nonzero,
\[
\boxed{
\frac{I_{0,A}}{C_A}
=
\frac{M_{0e}}{1+M_{00}},
}
\tag{14}
\]
\[
\boxed{
\frac{I_{1,A}}{C_A}
=
\frac{M_{1e}}{1+M_{1x}}.
}
\tag{15}
\]

This is the strongest closed scalar reduction available from reflection symmetry alone.

Note that \(u_{e,A}=R_A(e^x-1-x)\) is neither even nor odd, so \(M_{0e}\) and \(M_{1e}\) are both generally nonzero.

## 9. Simplified edge criteria

With (14)–(15),
\[
\boxed{
\alpha_A
=
-e^{-A}
\left[
1+\frac{M_{1e}}{1+M_{1x}}
\right],
}
\tag{16}
\]
and
\[
\boxed{
\beta_A
=
-e^{-A}
\left[
A\left(1+\frac{M_{1e}}{1+M_{1x}}\right)
+
1+\frac{M_{0e}}{1+M_{00}}
\right].
}
\tag{17}
\]

Therefore the corrected pure-compensated edge limit follows if
\[
\boxed{
\frac{M_{1e}}{1+M_{1x}}=o(e^A),
}
\]
and
\[
\boxed{
A\frac{M_{1e}}{1+M_{1x}}
+
\frac{M_{0e}}{1+M_{00}}
=
o(e^A).
}
\]

These are now resolvent-moment estimates, not estimates of the unknown deficiency vector itself.

## 10. Singular cases and their meaning

If
\[
1+M_{00}=0
\]
or
\[
1+M_{1x}=0,
\]
the corresponding scalar Schur complement becomes singular.

This is not a harmless algebraic inconvenience. It means the affine feedback through the boundary moment functional has generated a finite-\(A\) solvability/resonance condition.

In the unsimplified system the corresponding condition is
\[
D_A=0.
\]

Such values of \(A\) must be treated separately; division by the scalar denominator is not allowed.

## Result

The corrected Suzuki deficiency equation closes projectively on three scalars:
\[
\boxed{C_A,\ I_{0,A},\ I_{1,A}.}
\]

The exact moment equations are
\[
\boxed{
(1+M_{00})I_{0,A}+M_{0x}I_{1,A}=M_{0e}C_A,
}
\]
\[
\boxed{
M_{10}I_{0,A}+(1+M_{1x})I_{1,A}=M_{1e}C_A.
}
\]

Reflection reduces them to
\[
\boxed{
\frac{I_{0,A}}{C_A}=\frac{M_{0e}}{1+M_{00}},
\qquad
\frac{I_{1,A}}{C_A}=\frac{M_{1e}}{1+M_{1x}}.
}
\]

An absolute equation for \(C_A\) requires Suzuki's chosen deficiency normalization; the integral equation itself is scale-homogeneous.

The affine edge contamination is therefore exactly
\[
\boxed{
\alpha_A=-e^{-A}\left(1+\frac{M_{1e}}{1+M_{1x}}\right),
}
\]
\[
\boxed{
\beta_A=-e^{-A}
\left[
A\left(1+\frac{M_{1e}}{1+M_{1x}}\right)
+
1+\frac{M_{0e}}{1+M_{00}}
\right].
}
\]

## Next gate

Extract Suzuki's exact normalization for \(v_{A,+}\) and the precise operator \(\mathcal L_A\) from (8.5), then compute the six response moments (four after parity) without solving a new deficiency equation for each normalization. This gives a direct finite-\(A\) diagnostic of \(\alpha_A,\beta_A\).
