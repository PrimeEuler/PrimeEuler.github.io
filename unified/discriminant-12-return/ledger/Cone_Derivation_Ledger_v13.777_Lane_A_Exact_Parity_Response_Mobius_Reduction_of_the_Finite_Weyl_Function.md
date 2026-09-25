# Cone Derivation Ledger v13.777 — Lane A Exact Parity-Response Möbius Reduction of the Finite Weyl Function

Date: 2026-09-24

Lane: A.

Status: [D] exact parity reduction of source-faithful continuous-kernel transforms; [D] finite Weyl function reduced to one meromorphic parity-response ratio; [D] exact infinite target for that ratio; [D] primitive affine constants absent; [C] asymptotic parity-response gate.

Parents: v13.667, v13.685, v13.756, v13.773–776.

## 0. Synchronization

Live ledger checked before derivation and immediately before write: v13.776 remains head; no collision. This entry uses only the source-faithful continuous-kernel route retained after the v13.773 retraction.

## 1. Exact even/odd deficiency responses [D]

Let
\[
f_+(x):=\bar D e_{+i}(x),
\qquad
f_-(x):=\bar D e_{-i}(x).
\]

Fix the derivative convention by a common nonzero scalar \(\kappa\) so that
\[
f_+=\kappa e^x,
\qquad
f_-=\sigma\kappa e^{-x},
\qquad \sigma\in\{\pm1\},
\]
where \(\sigma\) records the reflection/derivative sign convention. It will be kept explicit.

Define even/odd source components
\[
f_e:=\frac12(f_++\sigma f_-)=\kappa\cosh x,
\]
\[
f_o:=\frac12(f_+-\sigma f_-)=\kappa\sinh x.
\]

Since \(S_A\) commutes with reflection, its inverse preserves parity. Define
\[
u_e:=(S_A^{(+)})^{-1}f_e,
\qquad
u_o:=(S_A^{(-)})^{-1}f_o.
\]

Then
\[
\boxed{
u_+=u_e+u_o,
\qquad
u_-=\sigma(u_e-u_o).
}
\]

Thus one even and one odd response determine both deficiency vectors exactly.

## 2. Parity response transforms [D]

For general spectral parameter \(z\), let
\[
\phi_z:=\bar D e_{\bar z}.
\]

Define the two scalar parity transforms
\[
\boxed{
E_A(z):=
\overline{\langle\phi_z,u_e\rangle},
\qquad
O_A(z):=
\overline{\langle\phi_z,u_o\rangle}.
}
\]

The exact source-faithful deficiency transforms become
\[
\boxed{
F_{A,+}=E_A+O_A,
}
\]
\[
\boxed{
F_{A,-}=\sigma(E_A-O_A).
}
\]

No primitive sources \(1,x\), no Schur ratios, and no affine constants enter.

## 3. Exact Weyl Möbius formula [D]

The finite Weyl function is
\[
m_A
=
-i
\frac{(z-i)F_{A,+}+(z+i)F_{A,-}}
{(z-i)F_{A,+}-(z+i)F_{A,-}}.
\]

Substituting the parity transforms gives the convention-explicit formula
\[
\boxed{
m_A(z)
=
-i\,
\frac{
[(z-i)+\sigma(z+i)]E_A
+
[(z-i)-\sigma(z+i)]O_A
}{
[(z-i)-\sigma(z+i)]E_A
+
[(z-i)+\sigma(z+i)]O_A
}.
}
\]

For the reflection convention \(\sigma=+1\),
\[
\boxed{
m_A(z)
=
-i\,
\frac{
zE_A(z)-iO_A(z)
}{
-iE_A(z)+zO_A(z)
}.
}
\tag{1}
\]

For \(\sigma=-1\), the same formula is obtained with the even/odd roles interchanged according to the fixed derivative convention. The invariant content is the Möbius dependence on one parity ratio.

## 4. One meromorphic scalar is sufficient [D]

Where \(E_A\ne0\), define
\[
\boxed{
\eta_A(z):=\frac{O_A(z)}{E_A(z)}.
}
\]

Under \(\sigma=+1\), (1) becomes
\[
\boxed{
m_A(z)
=
-i\frac{z-i\eta_A(z)}{-i+z\eta_A(z)}.
}
\tag{2}
\]

Thus all finite Weyl data are determined by one meromorphic parity-response ratio.

Solving (2) for \(\eta_A\), set \(M_A:=i\,m_A\). Then
\[
M_A=\frac{z-i\eta_A}{-i+z\eta_A},
\]
so
\[
\boxed{
\eta_A(z)
=
\frac{z+iM_A(z)}
{zM_A(z)+i}
=
-i\,\frac{z-m_A(z)}{1+z\,m_A(z)}.
}
\tag{3}
\]

Equations (2)–(3) are inverse Möbius transformations away from their divisors.

## 5. Exact infinite target [D]

The audited infinite Weyl function is
\[
\boxed{
m_\infty(z)
=
-i\,c\,\frac{D_\xi(z)}{\Xi(z)},
\qquad
c:=\frac{a}{b}
=
\frac{\xi(3/2)}{\xi'(3/2)}.
}
\]

Let
\[
R_\xi(z):=c\,\frac{D_\xi(z)}{\Xi(z)}.
\]
Then
\[
m_\infty=-iR_\xi.
\]

Substitution into (3) gives the exact target parity ratio
\[
\boxed{
\eta_\infty(z)
=
-i\,
\frac{z+iR_\xi(z)}
{1-i zR_\xi(z)}.
}
\tag{4}
\]

Equivalently,
\[
\boxed{
\eta_\infty(z)
=
-i
\frac{
z+i(a/b)\,\xi'(1/2-iz)/\xi(1/2-iz)
}{
1-i z(a/b)\,\xi'(1/2-iz)/\xi(1/2-iz)
}.
}
\]

This is the precise scalar target for the finite even/odd response ratio.

## 6. Local-uniform equivalence [D]

On a compact domain avoiding the Möbius divisors and zeros of the relevant even response,
\[
\boxed{
\eta_A\to\eta_\infty
\quad\Longleftrightarrow\quad
m_A\to m_\infty
}
\]
locally uniformly.

Therefore v13.756 immediately implies
\[
\eta_A\to\eta_\infty
\Longrightarrow
\Delta_{{\rm HB},A/\pi}
\to
\Delta_{{\rm HB},\infty/\pi}
\]
locally uniformly away from the limiting divisor.

The finite-to-infinite Weyl/HB problem is now reduced to one meromorphic scalar ratio of an odd response transform to an even response transform.

## 7. Characteristic channels in parity form [D]

For \(\sigma=+1\),
\[
W_0=(z-i)F_++(z+i)F_-,
\]
\[
W_\pi=(z-i)F_+-(z+i)F_-.
\]

Hence
\[
\boxed{
W_0=2(zE_A-iO_A),
}
\]
\[
\boxed{
W_\pi=2(-iE_A+zO_A).
}
\]

Therefore
\[
\boxed{
\frac{W_0}{W_\pi}
=
\frac{z-i\eta_A}{-i+z\eta_A}
=
i\,m_A.
}
\]

This makes the parity meaning of the two boundary characteristics explicit: each is a different linear combination of the same even and odd scalar responses.

## 8. Primitive boundary constants are absent [D/G]

Neither
\[
I_0/C,\quad I_1/C
\]
nor
\[
\alpha_A,\quad\beta_A
\]
appears anywhere in (1)–(4).

They remain relevant only to reconstructing the primitive first-kind profile from the derivative-space response.

Thus the post-retraction dependency graph is now fully scalar:
\[
\boxed{
(S_A^{(+)})^{-1}f_e,\ (S_A^{(-)})^{-1}f_o
\to
E_A,O_A
\to
\eta_A
\to
m_A
\to
\Delta_A.
}
\]

## 9. New asymptotic gate [C]

The next nonredundant question is no longer a boundary-constant estimate. It is to understand the relative finite-\(A\) asymptotics of
\[
E_A(z)
=
\overline{\langle\bar D e_{\bar z},(S_A^{(+)})^{-1}\bar D\cosh\rangle},
\]
\[
O_A(z)
=
\overline{\langle\bar D e_{\bar z},(S_A^{(-)})^{-1}\bar D\sinh\rangle}.
\]

Absolute normalization is irrelevant. It suffices to prove
\[
\boxed{
\frac{O_A(z)}{E_A(z)}
\longrightarrow
-i\,
\frac{z+iR_\xi(z)}
{1-i zR_\xi(z)}
}
\]
locally uniformly on zero-free compacta.

This is the smallest source-faithful scalar asymptotic target currently available in Lane A.

## 10. Relation to the screw/helix carrier [I/C]

Because the derivative transport and screw–Weil form isometry preserve the Weyl function, \(\eta_A\) may be sought in the parity decomposition of the basepointed helix/screw carrier.

The next useful analytic test is whether the even and odd response transforms admit a common regularized denominator so that
\[
\eta_A=O_A/E_A
\]
is determined only by two regularized numerators. If so, the distributional screw-symbol obstruction can cancel projectively even when neither channel admits an ordinary scalar Wiener–Hopf factorization separately.

This is a new possible simplification enabled by taking the parity ratio before attempting raw symbol factorization.

## Result

The exact finite Weyl function has been reduced to one source-faithful meromorphic parity-response ratio:
\[
\boxed{
\eta_A(z)=\frac{O_A(z)}{E_A(z)}.
}
\]

For the canonical reflection convention,
\[
\boxed{
m_A(z)
=
-i\frac{z-i\eta_A(z)}{-i+z\eta_A(z)}.
}
\]

Its exact infinite target is
\[
\boxed{
\eta_\infty(z)
=
-i\frac{z+i(a/b)\xi'(1/2-iz)/\xi(1/2-iz)}
{1-i z(a/b)\xi'(1/2-iz)/\xi(1/2-iz)}.
}
\]

Thus Lane A's spectral convergence problem is reduced to proving one scalar ratio limit. No primitive affine constants and no retracted Schur quantities are required.
