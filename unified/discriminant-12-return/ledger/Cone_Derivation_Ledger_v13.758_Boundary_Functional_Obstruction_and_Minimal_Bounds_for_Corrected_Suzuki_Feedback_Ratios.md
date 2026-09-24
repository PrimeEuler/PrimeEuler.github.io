# Cone Derivation Ledger v13.758 — Boundary-Functional Obstruction and Minimal Bounds for Corrected Suzuki Feedback Ratios

Date: 2026-09-24

Status: [D] exact correction/sharpening of the post-v13.757 asymptotic gate; [N] obstruction to a bulk-only helix spectral estimate; [C] sufficient norm criteria.

Parents: v13.742, v13.745, v13.753–757.

## 0. Synchronization

Live ledger rechecked immediately before commit: v13.757 is current head; no numbering collision.

This entry also records an important correction to an exploratory, unledgered step in the present thread: the response moments in v13.745 are boundary functionals \(\ell_{j,A}(R_Af)\), not automatically Hilbert pairings \(\langle f,R_Ag\rangle\). Therefore a positivity/Cauchy–Schwarz argument using invented "source energies" \(N_{\pm,A}\) is not justified without an additional Riesz-representation theorem for the boundary functionals. No such theorem is imported here.

## 1. Exact corrected moment definitions [D]

Let
\[
R_A=\mathcal L_A^{-1},
\]
and
\[
\ell_{0,A}(v)=\int_{-A}^{A}k(0,y)v(y)\,dy,
\qquad
\ell_{1,A}(v)=\int_{-A}^{A}k_x(0,y)v(y)\,dy.
\]

Then
\[
M_{00}=\ell_{0,A}(R_A1),\qquad
M_{1x}=\ell_{1,A}(R_Ax),
\]
\[
M_{0e}=\ell_{0,A}(R_A(e^x-1-x)),\qquad
M_{1e}=\ell_{1,A}(R_A(e^x-1-x)).
\]

The exact feedback ratios remain
\[
\boxed{
r_{0,A}=\frac{M_{0e}}{1+M_{00}},
\qquad
r_{1,A}=\frac{M_{1e}}{1+M_{1x}}.
}
\]

## 2. Parity reduction of the exponential source [D]

Assume the reflection symmetry already used in v13.745:
\[
R_A\mathscr R=\mathscr R R_A,
\]
with \(\ell_{0,A}\) even and \(\ell_{1,A}\) odd.

The source decomposes exactly:
\[
e^x-1-x=(\cosh x-1)+(\sinh x-x),
\]
where
\[
f_+(x):=\cosh x-1
\]
is even and
\[
f_-(x):=\sinh x-x
\]
is odd.

Therefore cross-parity contributions vanish:
\[
\boxed{
M_{0e}=\ell_{0,A}(R_A^{(+)}f_+),
}
\]
\[
\boxed{
M_{1e}=\ell_{1,A}(R_A^{(-)}f_-),
}
\]
while
\[
\boxed{
M_{00}=\ell_{0,A}(R_A^{(+)}1),
\qquad
M_{1x}=\ell_{1,A}(R_A^{(-)}x).
}
\]

Thus the corrected feedback genuinely separates into one even boundary-response ratio and one odd boundary-response ratio:
\[
\boxed{
r_{0,A}
=
\frac{\ell_{0,A}(R_A^{(+)}(\cosh x-1))}
{1+\ell_{0,A}(R_A^{(+)}1)},
}
\]
\[
\boxed{
r_{1,A}
=
\frac{\ell_{1,A}(R_A^{(-)}(\sinh x-x))}
{1+\ell_{1,A}(R_A^{(-)}x)}.
}
\]

This is exact and requires no positivity assumption.

## 3. Why the naive source-energy bound fails [N]

The quantities \(M_{0e},M_{00},M_{1e},M_{1x}\) are evaluations by \(\ell_{0,A},\ell_{1,A}\). They are not, from the presently established theory, of the form
\[
\langle 1,R_Af_+\rangle,\qquad
\langle x,R_Af_-\rangle.
\]

Therefore one may NOT infer
\[
|M_{0e}|^2\le M_{00}N_{+,A}
\]
or
\[
|M_{1e}|^2\le M_{1x}N_{-,A}
\]
by Cauchy–Schwarz without first proving that the boundary functionals have the required Riesz representatives in the same positive resolvent form.

This is a genuine boundary-vs-bulk distinction, not merely missing notation.

## 4. Minimal valid functional-norm bounds [D/C]

Choose Banach/Hilbert spaces \(X_{A,+},X_{A,-}\) on which the restricted resolvents and boundary functionals are bounded. Then the exact duality estimate gives
\[
|M_{0e}|
\le
\|\ell_{0,A}\|_{X_{A,+}^*}
\,
\|R_A^{(+)}f_+\|_{X_{A,+}},
\]
\[
|M_{1e}|
\le
\|\ell_{1,A}\|_{X_{A,-}^*}
\,
\|R_A^{(-)}f_-\|_{X_{A,-}}.
\]

Define the Schur denominators
\[
d_{0,A}:=|1+M_{00}|,
\qquad
d_{1,A}:=|1+M_{1x}|.
\]
Away from finite-A boundary resonances,
\[
\boxed{
|r_{0,A}|
\le
\frac{
\|\ell_{0,A}\|\,\|R_A^{(+)}f_+\|
}{d_{0,A}},
}
\]
\[
\boxed{
|r_{1,A}|
\le
\frac{
\|\ell_{1,A}\|\,\|R_A^{(-)}f_-\|
}{d_{1,A}}.
}
\]

These are the minimal source-faithful bounds available without a Riesz-representation theorem.

## 5. Exact sufficient asymptotic criteria for the pure compensated edge [D/C]

From v13.757,
\[
\alpha_A=-e^{-A}(1+r_{1,A}),
\]
\[
\beta_A=-e^{-A}[A(1+r_{1,A})+1+r_{0,A}].
\]

Hence it is sufficient that
\[
\boxed{
\frac{
\|\ell_{1,A}\|\,\|R_A^{(-)}f_-\|
}{d_{1,A}}
=o(e^A/A),
}
\]
and
\[
\boxed{
\frac{
\|\ell_{0,A}\|\,\|R_A^{(+)}f_+\|
}{d_{0,A}}
=o(e^A).
}
\]

Under these two estimates,
\[
\boxed{\alpha_A\to0,\qquad\beta_A\to0.}
\]

A convenient stronger condition is:
- \(d_{0,A},d_{1,A}\) bounded below subexponentially (in particular uniformly away from zero);
- the two products \(\|\ell_{0,A}\|\|R_A^{(+)}f_+\|\) and \(\|\ell_{1,A}\|\|R_A^{(-)}f_-\|\) grow polynomially or, more generally, sufficiently subexponentially.

## 6. What the helix/screw–Weil carrier does and does not control [D/N]

The compensated source functions satisfy
\[
f_+(0)=f_+'(0)=0,
\qquad
f_-(0)=f_-'(0)=f_-''(0)=0.
\]
This mirrors the basepoint compensation of
\[
e^{itu}-1.
\]

However, v13.742 already identifies the affine coefficients as boundary/domain data lost by twice differentiating the finite equation. The helix/screw–Weil carrier controls precisely that differentiated bulk current.

Therefore:
\[
\boxed{
\text{bulk helix/Weil spectral control alone cannot determine }
r_{0,A},r_{1,A}.
}
\]

It may control the response norms
\[
\|R_A^{(+)}f_+\|,\qquad
\|R_A^{(-)}f_-\|,
\]
but closing the feedback ratios additionally requires control of
\[
\boxed{
\|\ell_{0,A}\|,\quad
\|\ell_{1,A}\|,\quad
d_{0,A}^{-1},\quad
d_{1,A}^{-1}.
}
\]

These are the missing boundary trace/Schur-complement data.

This is exactly consistent with v13.742's statement:
\[
\boxed{
\text{bulk explicit-formula current}
+
\text{two boundary constants}
\text{ are both required.}
}
\]

## 7. Boundary-triple interpretation [D/I]

The denominators
\[
1+M_{00},\qquad1+M_{1x}
\]
are the two scalar Schur complements generated by feeding the affine boundary moments back through the corrected integral equation.

Their vanishing is a genuine finite-A solvability/resonance condition, as already noted in v13.745.

Thus the next asymptotic problem naturally splits into:
1. bulk response control, where the helix/screw–Weil representation can help;
2. boundary trace control of \(\ell_{0,A},\ell_{1,A}\);
3. nonresonance control of \(d_{0,A},d_{1,A}\).

This is the finite-A analogue of the v13.754 split between the helix/Weil current and the complementary boundary determinant correction.

## 8. Consequence for the Weyl/HB convergence lane [D]

v13.757 reduces Weyl convergence to the corrected deficiency shape
\[
w_A=u_{e,A}-r_{0,A}u_{1,A}-r_{1,A}u_{x,A}.
\]

The present result shows exactly what is required to stabilize that shape:
\[
\boxed{
\text{response convergence}
+
\text{boundary-functional bounds}
+
\text{Schur nonresonance}.
}
\]

If these imply locally controlled \(r_{0,A},r_{1,A}\) and convergence of the three response shapes, then v13.757 gives
\[
\rho_A\to\rho_\infty
\iff
m_A\to m_\infty,
\]
and v13.756 then gives
\[
\Delta_{{\rm HB},A/\pi}\to\Delta_{{\rm HB},\infty/\pi}.
\]

## 9. Result

The parity gate closes exactly:
\[
\boxed{
r_{0,A}
=
\frac{\ell_{0,A}(R_A^{(+)}(\cosh x-1))}
{1+\ell_{0,A}(R_A^{(+)}1)},
}
\]
\[
\boxed{
r_{1,A}
=
\frac{\ell_{1,A}(R_A^{(-)}(\sinh x-x))}
{1+\ell_{1,A}(R_A^{(-)}x)}.
}
\]

But the attempted bulk-only Cauchy–Schwarz closure is obstructed: the four moments are boundary-functional evaluations, not established positive resolvent inner products.

The minimal valid sufficient bounds are
\[
\boxed{
|r_{0,A}|
\le
\frac{\|\ell_{0,A}\|\,\|R_A^{(+)}(\cosh x-1)\|}{d_{0,A}},
}
\]
\[
\boxed{
|r_{1,A}|
\le
\frac{\|\ell_{1,A}\|\,\|R_A^{(-)}(\sinh x-x)\|}{d_{1,A}}.
}
\]

Therefore the pure compensated edge limit reduces to proving subcritical growth of these two boundary-response quotients. The helix/Weil carrier can address the response side, but the boundary traces and Schur denominators require separate boundary analysis.

## 10. Next gate

Extract \(\ell_{0,A},\ell_{1,A}\) as explicit trace/Riesz functionals in Suzuki's finite energy space, if possible, and derive their A-dependence together with lower bounds on
\[
|1+M_{00}|,\qquad |1+M_{1x}|.
\]
This is the smallest remaining boundary estimate needed before a helix/spectral bulk bound can close the affine-edge contamination and feed into the v13.757 Weyl ratio.