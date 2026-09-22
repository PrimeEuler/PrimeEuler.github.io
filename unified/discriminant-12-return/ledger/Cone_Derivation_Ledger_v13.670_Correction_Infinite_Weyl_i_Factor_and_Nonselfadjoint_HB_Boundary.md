# Cone Derivation Ledger v13.670 — Correction: Infinite Weyl Function Carries an i; Xi/E Is Not a Quotient of Two Self-Adjoint Boundary Characteristics

Date: 2026-09-22

Status: exact correction of v13.668 Section 3-6 and retraction of v13.669's central claim. A direct comparison with Suzuki Section 7.8 exposes a missing factor of i caused by mixing the raw boundary form with the conjugated finite characteristic.

## 0. Live collision/relevance check

Immediately before this write the ledger ends at v13.669. No collision. This correction is prompted by an internal consistency check of v13.669 against Suzuki's explicit Section-7.8 formula.

## 1. Source identities

Write
\[
\Xi(z)=\xi(1/2-iz),\qquad D(z)=\xi'(1/2-iz),
\]
so
\[
E=\Xi+D,\qquad E^\sharp=\Xi-D.
\]
Let
\[
a=\xi(3/2),\qquad b=\xi'(3/2).
\]
Suzuki gives
\[
C_\theta=a\cos(\theta/2)+ib\sin(\theta/2)
\]
and raw boundary form
\[
B_\theta(z):=
\mathcal W(K(\bar z,\cdot),W_\theta)
=
-\frac{e^{-i\theta/2}}{\pi i}
[C_\theta E-\bar C_\theta E^\sharp].
\]
Therefore
\[
\boxed{
B_\theta(z)
=
-\frac{2e^{-i\theta/2}}{\pi i}
[ib\sin(\theta/2)\Xi(z)+a\cos(\theta/2)D(z)].
}
\]
In particular
\[
\boxed{B_\pi=(2ib/\pi)\Xi,\qquad B_0=(2ia/\pi)D.}
\]
Hence
\[
\boxed{\frac{B_0}{B_\pi}=\frac{a}{b}\frac{D}{\Xi}.}
\]

## 2. Where v13.668 lost the i

The finite characteristic used in v13.661 is
\[
W(a,\theta;z)=\overline{\mathcal W(v_{\bar z},w_\theta)}.
\]
The v13.661 boundary-triple identity is
\[
\frac{W_\theta}{W_\pi}
=
-i e^{i\theta/2}\cos(\theta/2)[\tau_\theta-m(z)].
\]
At theta=0,
\[
\boxed{\frac{W_0}{W_\pi}=i\,m(z).}
\]

The raw de Branges boundary-form ratio B_0/B_pi cannot simply be substituted for W_0/W_pi without tracking the conjugation. With the compatible characteristic convention, comparison yields
\[
\boxed{
m_\infty(z)=
-i\,\frac{a}{b}\frac{D(z)}{\Xi(z)}
}
\]
(up to the globally fixed opposite sign if the entire boundary-form convention is reversed). The crucial point is the unavoidable factor i.

Thus v13.668's displayed real multiple
\[
m_\infty=-(a/b)D/\Xi
\]
is corrected to an imaginary multiple.

## 3. Correct Möbius expression for the Corollary target

Set
\[
c_\infty=b/a.
\]
Then
\[
\frac{D}{\Xi}=i c_\infty m_\infty
\]
for the displayed convention, and therefore
\[
\boxed{
\frac{\Xi}{\Xi+D}
=
\frac{1}{1+i c_\infty m_\infty}.
}
\]

This replaces v13.668's incorrect 1/(1-c m).

## 4. No real self-adjoint theta_* produces E

A self-adjoint extension has real
\[
\tau_\theta=\tan(\theta/2)\in\mathbb R\cup\{\infty\}.
\]
Its relative characteristic is proportional to
\[
\tau_\theta-m_\infty.
\]

To make
\[
1+i c_\infty m_\infty
\]
proportional to tau-m would require
\[
\boxed{\tau=i/c_\infty=i\,a/b,}
\]
which is nonreal.

The same obstruction is visible directly in Suzuki's formula:
\[
B_\theta\propto
ib\sin(\theta/2)\Xi+a\cos(\theta/2)D.
\]
For real theta, the Xi coefficient is imaginary while the D coefficient is real. They cannot be equal nonzero coefficients, so no real theta makes B_theta proportional to
\[
E=\Xi+D.
\]

Therefore v13.669's claimed real
\[
\theta_*=2\arctan(a/b)
\]
does NOT produce E and the central quotient claim of v13.669 is RETRACTED.

## 5. Correct interpretation

The Corollary target
\[
\boxed{\Xi/E}
\]
is a Möbius transform of the Weyl function evaluated at a NON-SELF-ADJOINT complex boundary parameter.

Equivalently, E is the characteristic denominator of a maximal dissipative/accumulative extension (depending on sign convention), not of a self-adjoint member of Suzuki's real theta family.

This is structurally natural in de Branges theory: E itself has no real zeros and encodes the Hermite-Biehler function, whereas the real self-adjoint extension characteristics are its real phase combinations.

## 6. What survives

v13.661: survives exactly.
v13.667: survives exactly.
v13.668: Section 1-2 source formulas survive; Sections 3-7 must use the corrected i factor.
v13.669: central claim that Xi/E is a quotient of two SELF-ADJOINT boundary characteristics is retracted.

A corrected finite candidate is still available:
\[
\boxed{
R_a^{HB}(z)=\frac{1}{1+i c_\infty m_a(z)},
}
\]
but it corresponds to a complex boundary parameter, not a second real theta extension.

## 7. Next gate

Develop the maximal dissipative boundary extension with complex parameter
\[
\tau_{HB}=i/c_\infty
\]
and show that its perturbation determinant relative to theta=pi has infinite characteristic proportional to E. Then formulate the finite-a Hermite-Biehler approximant
\[
E_a(z)\propto W_\pi(a,z)[1+i c_\infty m_a(z)]
\]
and test what can be proved about zero location / Schur contractivity from the Nevanlinna property of m_a. This is the correct boundary-triple route to Suzuki's Xi/E target.
