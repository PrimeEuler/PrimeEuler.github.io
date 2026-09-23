# Cone Derivation Ledger v13.743 — Affine Boundary-Coefficient Scaling and Reflection Gate

Date: 2026-09-23

Status: source-faithful continuation after the v13.742 correction. This gate does **not** assume the affine coefficients in Suzuki (8.5) vanish. It derives the exact reflection relations and the sharp growth criterion required for the pure compensated edge source.

Synchronization: live head before write was v13.742, commit \`70ecf60e6c0c54bd391117df3116cef54f7e56af\`. No newer audit or colliding Suzuki entry was present.

## 1. Correct Section-8 deficiency equations

Write Suzuki's actual deficiency equations abstractly as
\[
\mathcal L_A[v_{A,+}](x)
=
C_{A,+}e^x+A_{A,+}x+B_{A,+},
\]
\[
\mathcal L_A[v_{A,-}](x)
=
C_{A,-}e^{-x}+A_{A,-}x+B_{A,-},
\]
with
\[
A_{A,\pm}
=
-\int_{-A}^{A}k_x(0,y)v_{A,\pm}(y)\,dy
\mp C_{A,\pm},
\]
\[
B_{A,\pm}
=
-\int_{-A}^{A}k(0,y)v_{A,\pm}(y)\,dy
-C_{A,\pm}.
\]

The affine coefficients are integration constants/boundary data and are retained.

## 2. Reflection parity of the kernel data

Suzuki's screw kernel is even in the difference variable, and the finite interval is symmetric. For the integrated kernel entering (8.5), reflection symmetry gives
\[
k(0,-y)=k(0,y),
\]
while differentiation in the first variable gives the odd relation
\[
k_x(0,-y)=-k_x(0,y).
\]

Let \(R\) denote reflection:
\[
(Rv)(x)=v(-x).
\]

The \(+\) and \(-\) deficiency equations are exchanged by \(R\). Therefore, after choosing a reflection-compatible normalization,
\[
\boxed{
v_{A,-}(x)=v_{A,+}(-x),
\qquad
C_{A,-}=C_{A,+}.
}
\]

Denote the common constant by \(C_A\).

## 3. Exact reflection relations for the affine coefficients

Using \(v_-(y)=v_+(-y)\), substitute \(u=-y\).

For the derivative coefficient,
\[
\int_{-A}^{A}k_x(0,y)v_-(y)\,dy
=
\int_{-A}^{A}k_x(0,y)v_+(-y)\,dy
=
-\int_{-A}^{A}k_x(0,u)v_+(u)\,du.
\]

Hence
\[
A_{A,-}
=
+\int k_x(0,u)v_+(u)\,du+C_A
=
-\left[-\int k_x(0,u)v_+(u)\,du-C_A\right].
\]

Therefore
\[
\boxed{A_{A,-}=-A_{A,+}.}
\]

For the constant coefficient,
\[
\int k(0,y)v_-(y)\,dy
=
\int k(0,u)v_+(u)\,du,
\]
so
\[
\boxed{B_{A,-}=B_{A,+}.}
\]

Thus the entire affine deficiency data reduce to one odd coefficient and one even coefficient:
\[
\boxed{
C_{A,-}=C_{A,+}=C_A,\qquad
A_{A,-}=-A_{A,+},\qquad
B_{A,-}=B_{A,+}.
}
\]

This reduces the two deficiency equations to one.

## 4. Right-edge scaling of the \(+\) equation

Put
\[
x=A-\xi.
\]

The source is
\[
C_Ae^x=C_Ae^Ae^{-\xi}.
\]

The affine part becomes
\[
A_{A,+}(A-\xi)+B_{A,+}
=
AA_{A,+}+B_{A,+}-A_{A,+}\xi.
\]

Divide by the natural exponential edge scale \(C_Ae^A\), assuming \(C_A\ne0\):
\[
e^{-\xi}
+
\frac{AA_{A,+}+B_{A,+}}{C_Ae^A}
-
\frac{A_{A,+}}{C_Ae^A}\xi.
\]

Define
\[
\boxed{
\alpha_A:=\frac{A_{A,+}}{C_Ae^A},
\qquad
\beta_A:=\frac{AA_{A,+}+B_{A,+}}{C_Ae^A}.
}
\]

Then the scaled right-edge source is exactly
\[
\boxed{
e^{-\xi}+\beta_A-\alpha_A\xi.
}
\]

The pure exponential edge source is recovered iff
\[
\boxed{\alpha_A\to0,\qquad\beta_A\to0.}
\]

This is sharper than separately requiring \(e^{-A}A_{A,+}\to0\) and \(e^{-A}B_{A,+}\to0\), because the physically relevant constant boundary combination is \(AA_{A,+}+B_{A,+}\), and the normalization \(C_A\) must be retained.

## 5. Left-edge scaling of the \(-\) equation

Put
\[
x=-A+\xi.
\]

Then
\[
C_Ae^{-x}=C_Ae^Ae^{-\xi}.
\]

Using
\[
A_{A,-}=-A_{A,+},
\qquad
B_{A,-}=B_{A,+},
\]
the affine term is
\[
A_{A,-}(-A+\xi)+B_{A,-}
=
AA_{A,+}+B_{A,+}-A_{A,+}\xi.
\]

Therefore the normalized left-edge source is **identical**:
\[
\boxed{
e^{-\xi}+\beta_A-\alpha_A\xi.
}
\]

Thus reflection does more than reduce the problem: both edge channels carry the same affine contamination in their own inward coordinates.

## 6. Consequence for paired cancellation

Because the right and left edge affine profiles are identical after reflection-compatible normalization, one must not assume they cancel in the paired deficiency channel.

Whether they cancel depends on the signs/phases introduced by

1. the derivative transport \(\bar D\);
2. the factors \((z-i)\) and \((z+i)\);
3. the Section-7 normalization of the two deficiency vectors.

At the pre-transport source level, the contamination is common-mode:
\[
\boxed{
b_A(\xi)=\beta_A-\alpha_A\xi.
}
\]

Therefore paired-channel cancellation is a separate theorem, not a consequence of reflection alone.

## 7. Coefficient identities in terms of one deficiency vector

Let
\[
I_{0,A}:=\int_{-A}^{A}k(0,y)v_{A,+}(y)\,dy,
\]
\[
I_{1,A}:=\int_{-A}^{A}k_x(0,y)v_{A,+}(y)\,dy.
\]

Then
\[
\boxed{
A_{A,+}=-I_{1,A}-C_A,
\qquad
B_{A,+}=-I_{0,A}-C_A.
}
\]

Hence
\[
\boxed{
\alpha_A
=
-\frac{I_{1,A}+C_A}{C_Ae^A},
}
\]
and
\[
\boxed{
\beta_A
=
-\frac{A(I_{1,A}+C_A)+I_{0,A}+C_A}{C_Ae^A}.
}
\]

The edge problem has therefore been reduced to estimating two scalar moments of a single deficiency vector.

## 8. Sharp sufficient growth conditions

Suppose
\[
|I_{1,A}|+|C_A|=o(|C_A|e^A)
\]
and
\[
A|I_{1,A}+C_A|+|I_{0,A}+C_A|
=
o(|C_A|e^A).
\]

Then
\[
\boxed{\alpha_A,\beta_A\to0}
\]
and the affine contamination disappears.

A simpler but stronger sufficient condition is: for some \(\varepsilon>0\),
\[
\frac{|I_{0,A}|+|I_{1,A}|}{|C_A|}
=
O(e^{(1-\varepsilon)A}/A).
\]

Then both scaled affine coefficients vanish exponentially up to the polynomial \(A\) factor.

No such estimate is presently established.

## 9. Corrected edge equation with explicit affine remnant

Let
\[
\alpha=\lim\alpha_A,\qquad
\beta=\lim\beta_A
\]
along any subsequence for which these limits exist.

Before derivative/core compensation, the limiting edge source is
\[
e^{-\xi}+\beta-\alpha\xi.
\]

After the core approximation/derivative transport, the exponential part produces the established bulk contribution
\[
e^{-\xi}-\delta_0.
\]

The affine part contributes a boundary/domain functional which cannot be determined by the twice-differentiated interior equation alone.

Accordingly the corrected edge equation is
\[
\boxed{
S_{\rm edge}q_\pm
=
\pm i(e^{-\xi}-\delta_0)
+
\mathcal B_{\alpha,\beta,\pm}.
}
\]

The pure compensated model is equivalent to the additional asymptotic assertion
\[
\boxed{\alpha=\beta=0.}
\]

## 10. What can be inferred without solving (8.5)

The definitions alone do **not** imply
\[
A_{A,+}=O(1),\qquad B_{A,+}=O(1).
\]

Indeed the interval grows, the kernel is nondecaying, and the deficiency vector itself may carry \(e^A\)-scale boundary mass.

Therefore no source-faithful argument currently permits setting \(\alpha_A\) or \(\beta_A\) to zero merely because the affine terms are lower degree in \(x\) than \(e^x\).

The correct comparison is amplitude, not functional type.

## 11. Next computational gate

The exact remaining quantities are
\[
I_{0,A},\qquad I_{1,A},\qquad C_A.
\]

The most direct route is to solve Suzuki's actual one-channel equation (8.5) numerically for increasing \(A\), with the same kernel and domain conditions, and measure
\[
\alpha_A
=
-\frac{I_{1,A}+C_A}{C_Ae^A},
\]
\[
\beta_A
=
-\frac{A(I_{1,A}+C_A)+I_{0,A}+C_A}{C_Ae^A}.
\]

A robust numerical gate should report
\[
A,\quad C_A,\quad I_{0,A},\quad I_{1,A},
\quad\alpha_A,\quad\beta_A
\]
and convergence ratios.

Only after that gate should the pure compensated edge source be promoted or rejected.

## Result

\[
\boxed{\textbf{PASS: reflection reduces the two deficiency equations to one.}}
\]

\[
\boxed{
C_{A,-}=C_{A,+},\quad
A_{A,-}=-A_{A,+},\quad
B_{A,-}=B_{A,+}.
}
\]

\[
\boxed{\textbf{PASS: exact scaled affine contamination isolated}}
\]
\[
\boxed{
b_A(\xi)=\beta_A-\alpha_A\xi,
}
\]
with
\[
\boxed{
\alpha_A=\frac{A_{A,+}}{C_Ae^A},
\qquad
\beta_A=\frac{AA_{A,+}+B_{A,+}}{C_Ae^A}.
}
\]

\[
\boxed{\textbf{OPEN: }\alpha_A,\beta_A\to0.}
\]

The next decisive gate is numerical or analytic estimation of the one-channel moments \(I_{0,A},I_{1,A}\) from Suzuki's actual equation (8.5).
