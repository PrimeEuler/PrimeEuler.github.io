# Cone Derivation Ledger v13.669 — Corollary Target as an Exact Quotient of Two Boundary Characteristics

Date: 2026-09-22

Status: exact algebraic consequence of the audited v13.661 boundary-triple identity plus the RH-dependent infinite de Branges Weyl function of v13.668. This removes the need for an ad hoc finite c_a calibration at the present gate.

## 0. Live collision/relevance check

Immediately before this write the ledger ends at v13.668. No collision or newer relevant entry.

## 1. Infinite Weyl target

From v13.668, in the v13.661 boundary convention,
\[
m_\infty(z)=-
\frac{\xi(3/2)}{\xi'(3/2)}
\frac{\xi'(1/2-iz)}{\xi(1/2-iz)}.
\]
Set
\[
c_\infty:=\frac{\xi'(3/2)}{\xi(3/2)}.
\]
Then Suzuki's Corollary-1.6 target is
\[
R_\infty(z):=
\frac{\Xi(z)}{\Xi(z)+\xi'(1/2-iz)}
=
\frac1{1-c_\infty m_\infty(z)}.
\]

## 2. Select the unique boundary extension carrying the denominator

The exact finite boundary identity from v13.661 is
\[
\frac{W(a,\theta;z)}{W(a,\pi;z)}
=
A_\theta[\tau_\theta-m_a(z)],
\]
where
\[
A_\theta=-i e^{i\theta/2}\cos(\theta/2),
\qquad
\tau_\theta=\tan(\theta/2).
\]

Choose theta_* by
\[
\boxed{
\tau_*:=\tan(\theta_*/2)=\frac1{c_\infty}
=\frac{\xi(3/2)}{\xi'(3/2)}.
}
\]
Equivalently,
\[
\boxed{
\theta_*=2\arctan\!\left(\frac{\xi(3/2)}{\xi'(3/2)}\right)
\pmod{2\pi}.
}
\]

Then
\[
1-c_\infty m_\infty
=
c_\infty(\tau_*-m_\infty).
\]

Therefore
\[
\boxed{
R_\infty(z)
=
\frac{A_{\theta_*}}{c_\infty}
\frac{W_\infty(\pi;z)}{W_\infty(\theta_*;z)}.
}
\]

Thus the Corollary target is EXACTLY, up to a z-independent scalar, a quotient of the theta=pi characteristic by one distinguished second self-adjoint-extension characteristic.

## 3. Direct de Branges verification

Suzuki Section 7.8 gives
\[
W_\infty(\theta;z)\propto
C_\theta E(z)-\overline{C_\theta}E^\sharp(z),
\]
with
\[
C_\theta=\xi(3/2)\cos(\theta/2)
+i\xi'(3/2)\sin(\theta/2).
\]

At theta=pi, the boundary form is proportional to
\[
\Xi(z)=\xi(1/2-iz).
\]

For theta=theta_* with tan(theta_*/2)=xi(3/2)/xi'(3/2), the coefficients are chosen so that the corresponding real-linear combination is proportional to
\[
E(z)=\Xi(z)+\xi'(1/2-iz).
\]

Hence the quotient W_pi/W_theta* is proportional to Xi/E, independently confirming the Weyl-function derivation.

## 4. Canonical finite approximant

This suggests the finite-a object
\[
\boxed{
R_a^{BT}(z)
:=
\frac{A_{\theta_*}}{c_\infty}
\frac{W(a,\pi;z)}{W(a,\theta_*;z)}.
}
\]
Using the exact finite Weyl identity,
\[
\boxed{
R_a^{BT}(z)
=
\frac1{1-c_\infty m_a(z)}.
}
\]

No finite c_a needs to be guessed: the same distinguished extension parameter theta_* is fixed once and for all by the infinite de Branges normalization.

This object is invariant under multiplication of all W(a,theta;z) by a common nonzero scalar depending on a and z, provided that factor is theta-independent. It therefore removes the common characteristic normalization automatically.

## 5. What this does and does not remove

It DOES remove:
- arbitrary common scalar normalization of the deficiency vectors;
- any theta-independent multiplicative characteristic factor;
- the need to compare raw amplitudes of W_pi across a.

It does NOT prove:
- that m_a(z) converges to m_infty(z);
- that Suzuki's e^{phi(a,z)} is theta-independent in precisely the way needed to recover raw W_pi from the quotient;
- strong resolvent convergence of the finite extensions;
- RH.

The finite quotient has poles at the theta_* extension spectrum and zeros at the theta=pi extension spectrum.

## 6. New convergence gate

The asymptotic problem can now be split cleanly:

A. Relative boundary convergence:
\[
\boxed{
m_a(z)\to m_\infty(z)
}
\]
locally off the limiting reference spectrum, equivalently
\[
R_a^{BT}(z)\to \Xi(z)/E(z).
\]

B. Absolute characteristic normalization:
recovering Suzuki's raw statement
\[
e^{\phi(a,z)}W(a,\pi;z)\to\Xi/E
\]
requires control of W(a,theta_*;z) itself. The quotient alone cannot determine that common factor.

Thus the mysterious phi(a,z) has not vanished, but its role is sharply isolated: it belongs to the absolute normalization of one reference characteristic, not to the extension-relative spectral data.

## 7. Next gate

Investigate convergence of m_a through the canonical embeddings H(A_a)->H(A_infty) described in Suzuki Section 7.6. In deficiency-index one, local uniform Weyl-function convergence should follow from suitable generalized/strong resolvent convergence of the reference extensions plus convergence of the normalized defect vectors. Determine exactly which convergence statement Suzuki conjectures and which additional normalization is required to turn it into m_a->m_infty.
