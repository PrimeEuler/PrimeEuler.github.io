# Cone Derivation Ledger v13.682 — Weyl-Convergence Gate: Strong Resolvent Convergence Alone Is Insufficient

Date: 2026-09-22

Status: exact abstract boundary-triple analysis. This identifies the additional datum required beyond strong resolvent convergence of the theta=pi reference extensions to obtain m_a -> m_infty.

## 0. Live collision/relevance check

Immediately before this write the ledger ends at v13.681. No collision.

## 1. Problem

The project model seeks convergence of
\[
R_a^{proj}(z)=\frac1{1-i c_\infty m_a(z)}.
\]
A natural hope is that strong resolvent convergence of the reference self-adjoint extensions
\[
H_{a,\pi}\to H_{\infty,\pi}
\]
would force
\[
m_a(z)\to m_\infty(z).
\]

It does not, by itself.

## 2. Why resolvent convergence does not determine m

For an ordinary scalar boundary triple,
\[
m(z)-m(\zeta)^*
=
(z-\bar\zeta)\gamma(\zeta)^*\gamma(z).
\]
In particular, fixing a nonreal base point z_0,
\[
\boxed{
m(z)
=
\operatorname{Re}m(z_0)
+
(z-\operatorname{Re}z_0)\times(\text{gamma-field data})
}
\]
schematically: the imaginary part and differences of m are determined by the defect-vector kernel, but an additive real boundary normalization remains.

More concretely, the boundary-triple transformation
\[
\Gamma_0'=\Gamma_0,\qquad
\Gamma_1'=\Gamma_1+r\Gamma_0,
\qquad r\in\mathbb R,
\]
leaves the reference extension
\[
\ker\Gamma_0'=\ker\Gamma_0=H_\pi
\]
UNCHANGED, while
\[
\boxed{m'(z)=m(z)+r.}
\]

Therefore even exact equality of all reference resolvents does not determine the scalar Weyl function unless the Gamma_1 normalization is also fixed.

This gives an explicit obstruction:
\[
\boxed{
H_{a,\pi}\xrightarrow{\rm s.r.}H_{\infty,\pi}
\quad\not\Rightarrow\quad
m_a\to m_\infty.
}
\]

## 3. What extra datum is sufficient

Fix a common nonreal calibration point z_0. It is sufficient to have:
1. strong/generalized resolvent convergence of H_{a,pi};
2. convergence of normalized gamma vectors
\[
J_a\gamma_a(z_0)\to\gamma_\infty(z_0)
\]
under the chosen embeddings J_a;
3. convergence of one real scalar boundary calibration
\[
\boxed{\operatorname{Re}m_a(z_0)\to\operatorname{Re}m_\infty(z_0).}
\]

Then the resolvent identity for gamma fields,
\[
\gamma_a(z)
=
\left[I+(z-z_0)(H_{a,\pi}-z)^{-1}\right]\gamma_a(z_0),
\]
gives
\[
J_a\gamma_a(z)\to\gamma_\infty(z)
\]
locally on compact subsets of the common resolvent domain.

Using
\[
m_a(z)-\overline{m_a(z_0)}
=
(z-\bar z_0)
\langle\gamma_a(z),\gamma_a(z_0)\rangle,
\]
one obtains
\[
\boxed{m_a(z)\to m_\infty(z)}
\]
locally uniformly after the one-point real calibration.

## 4. Boundary-coordinate interpretation

The missing scalar is exactly the freedom
\[
\Gamma_1\mapsto\Gamma_1+r\Gamma_0.
\]
Thus the extra hypothesis is not mysterious spectral information: it is convergence of the finite boundary-coordinate origin.

Equivalently, one may fix the normalization by requiring the theta=0 extension parameter to remain tau_0=0 in the same transported triple. If the finite embeddings preserve BOTH distinguished extensions theta=pi and theta=0, then the additive r freedom is removed.

Therefore a stronger and geometrically natural sufficient condition is:
\[
\boxed{
H_{a,\pi}\to H_{\infty,\pi}
\quad\text{and}\quad
H_{a,0}\to H_{\infty,0}
}
\]
in compatible generalized strong-resolvent sense, together with convergence of one normalized defect vector. The pair of extensions fixes the scalar boundary coordinate.

## 5. Consequence for the project model

The finite ratio
\[
R_a^{proj}=\frac{W_\pi}{W_\pi-cW_0}
\]
already uses BOTH extension characteristics. This is advantageous: it is invariant under common multiplicative characteristic gauge, but it is NOT invariant under the additive Weyl renormalization m->m+r, because that transformation changes which extension is called theta=0.

Hence convergence of R_a requires convergence of the ordered extension pair
\[
(H_{a,\pi},H_{a,0}),
\]
not merely the reference extension H_{a,pi}.

## 6. Minimal sufficient convergence package

A clean theorem target is:

Assume there are isometric embeddings J_a into a common Hilbert space such that:
(A) J_a H_{a,pi} J_a^* -> H_{infty,pi} in generalized strong resolvent sense;
(B) the theta=0 boundary condition is transported compatibly, equivalently the additive boundary shift r_a ->0;
(C) for one z_0 in C_+, J_a gamma_a(z_0)->gamma_infty(z_0).

Then
\[
m_a\to m_\infty
\]
locally uniformly on compact subsets away from the limiting reference spectrum, and therefore
\[
\boxed{
R_a^{proj}(z)
\to
\frac1{1-i c_\infty m_\infty(z)}.
}
\]

If the project-model identification of m_infty with the Section-7 heuristic is separately established, the right side is Xi/E.

## 7. Next gate

Inspect Suzuki's actual embedding/convergence conjecture in the archived PDF and determine whether it preserves only one self-adjoint extension or the full theta-family. If only one extension is controlled, formulate the smallest additional convergence statement for the theta=0 extension/deficiency vectors needed by the theorem above.

Do not attribute the resulting theorem to Suzuki unless it is explicitly present in the PDF.
