# Cone Derivation Ledger v13.662 — Correction: Dirichlet-Laplacian Bulk Determinant Is Not Yet a Suzuki Same-Domain Determinant

Date: 2026-09-22

Status: exact source/domain correction to v13.644. The Dirichlet Laplacian characteristic derived there is mathematically correct as a standalone reference problem, but the claimed decomposition H_A=H_0,A+V_A on a common operator domain was not established for Suzuki's Friedrichs operator A_A and is generally incompatible with the source domain structure.

## 0. Live collision/relevance check

Immediately before this write the live ledger ends at v13.661. No collision. This correction is forced by re-reading the live Suzuki v2 source while completing the boundary-triple gate.

## 1. Suzuki's actual finite operator domains

The live source defines
\[
B_A=D^*G_AD,\qquad D(B_A)=H_0^1(-A,A),
\]
and proves that the self-adjoint Weil operator A_A is the Friedrichs extension of B_A.

Crucially Suzuki states explicitly that
\[
\boxed{D(A_A)\supsetneq D(B_A)=H_0^1(-A,A)}
\]
and that D(A_A) contains functions such as constants.

Thus A_A is not presented as a Dirichlet second-order differential operator with
\[
D(A_A)=H^2\cap H_0^1.
\]

## 2. What v13.644 got right

The standalone local Dirichlet reference
\[
H_{0,A}=-d^2/dx^2,\qquad D(H_{0,A})=H^2\cap H_0^1
\]
has normalized characteristic
\[
D_{0,A}(z)=\frac{\sin(2Az)}{2Az}
\]
and parity factors
\[
\cos(Az),\qquad \frac{\sin(Az)}{Az}.
\]
Those ODE facts remain exact.

## 3. What v13.644 did not establish

v13.644 wrote schematically
\[
H_A=H_{0,A}+V_A
\]
and then formed
\[
\det[I+V_A(H_{0,A}-z^2)^{-1}].
\]
For Suzuki's A_A this decomposition was never derived. The source instead gives the nonlocal form/operator architecture
\[
A_A=\operatorname{Friedrichs}(D^*G_AD).
\]
Because the domains and operator orders differ, one cannot identify A_A-H_{0,A} with a trace-class operator V_A merely from the common interval or the H_0^1 core.

Therefore the quantity called the common-domain bulk determinant in v13.644 is presently only a formal/hypothetical determinant for an unproved additive decomposition, not an established Suzuki relative determinant.

## 4. Correct reference architecture supplied by Suzuki

Suzuki Section 8 gives an exact isometric transfer:
\[
\bar D:\mathcal H(T_A)\overset{\sim}{\longrightarrow}\mathcal H(S_A),
\]
where
\[
T_A=A_A-\lambda I,
\qquad
S_A=G_A-\lambda(-\Delta_N)^{-1}.
\]
The first-order operators on these two energy spaces are unitarily equivalent.

This is the correct finite-A comparison structure supplied by the source. It does NOT identify either space with the local Dirichlet-Laplacian spectral problem of v13.644.

## 5. Consequence for determinant factorization

The exact boundary determinant obtained in v13.661 is intrinsic to the pair of self-adjoint extensions of the SAME symmetric first-order operator:
\[
\Delta^{bdry}_{A,\theta/\pi}.
\]
It is valid.

By contrast, a bulk determinant against -d^2/dx^2 would require a separately proved operator/form determinant theorem. Until such a theorem is supplied,
\[
\boxed{\Delta^{tot}=\Delta^{bulk}\Delta^{bdry}}
\]
with the v13.644 Dirichlet bulk factor is NOT established for Suzuki's construction.

The safe exact finite characteristic is Suzuki's W itself and its relative extension quotient:
\[
\boxed{
\frac{W(A,\theta;z)/W(A,\pi;z)}
{W(A,\theta;z_*)/W(A,\pi;z_*)}
=
\Delta^{bdry}_{A,\theta/\pi}(z;z_*).
}
\]

## 6. Reinterpretation of the n*pi/A box branch

The factor sin(Az)/(Az) found in the projected free control remains a useful endpoint diagnostic, but after this domain correction it cannot be promoted to an exact multiplicative factor of Suzuki's A_A characteristic through the v13.644 additive-determinant argument.

Its status returns to:
\[
\boxed{\text{finite-box / projected endpoint diagnostic, not a proved Suzuki bulk factor}.}
\]

## 7. Next gate

The clean path is now to stop trying to multiply a local Dirichlet bulk determinant into W. Instead:
1. use the exact Suzuki energy-space boundary determinant of v13.661;
2. exploit the exact unitary map \bar D between H(T_A) and H(S_A);
3. formulate any renormalization directly in terms of W(A,pi;z), its Weyl function m_A, or the continuous-kernel S_A problem;
4. compare that object to the corrected infinite target z^2 xi/xi' without inserting an unproved local-Laplacian determinant.

A separate local-reference determinant can be revisited only if a genuine form-resolvent comparison theorem is derived.
