# Cone Derivation Ledger v13.684 — Two-Extension Resolvent Difference Determines the Weyl Cross-Ratio

Date: 2026-09-22

Status: exact project theorem in scalar boundary-triple theory. This sharpens v13.682-v13.683: simultaneous convergence of two fixed self-adjoint extensions determines a Möbius-invariant Weyl quantity without requiring an additive calibration.

## 0. Live collision/relevance check

Immediately before this write the ledger ends at v13.683. No collision.

## 1. Scalar Krein formulas for two extensions

Let an ordinary scalar boundary triple have Weyl function m(z), gamma field gamma(z), and self-adjoint extensions H_tau given by
\[
\Gamma_1f=\tau\Gamma_0f,
\qquad \tau\in\mathbb R\cup\{\infty\}.
\]

Relative to H_infty=ker Gamma_0,
\[
(H_\tau-z)^{-1}-(H_\infty-z)^{-1}
=
\gamma(z)(\tau-m(z))^{-1}\gamma(\bar z)^*.
\]

For two finite real parameters tau_1 != tau_2, subtraction gives
\[
\boxed{
(H_{\tau_1}-z)^{-1}-(H_{\tau_2}-z)^{-1}
=
\frac{\tau_2-\tau_1}
{(\tau_1-m(z))(\tau_2-m(z))}
\gamma(z)\gamma(\bar z)^*.
}
\]

## 2. Determinant ratio and Weyl cross-ratio

The normalized perturbation determinant between the two extensions is
\[
\boxed{
\Delta_{\tau_1/\tau_2}(z;z_*)
=
\frac{\tau_1-m(z)}{\tau_2-m(z)}
\frac{\tau_2-m(z_*)}{\tau_1-m(z_*)}.
}
\]

This is invariant under a simultaneous affine change of boundary coordinates once tau_1,tau_2 are transformed with m.

Thus the intrinsic spectral datum carried by an ordered extension pair is not m alone but its Möbius cross-ratio.

## 3. Specialize to Suzuki theta=0 and theta=pi

In the project convention,
\[
\tau_0=0,\qquad
H_\pi=\ker\Gamma_0\quad(\tau_\pi=\infty).
\]
The characteristic identity gives
\[
\boxed{\frac{W_0(z)}{W_\pi(z)}=i\,m(z).}
\]

Normalize at z_*:
\[
\boxed{
\mathcal C_a(z;z_*)
:=
\frac{W_0(a,z)/W_\pi(a,z)}
{W_0(a,z_*)/W_\pi(a,z_*)}
=
\frac{m_a(z)}{m_a(z_*)}.
}
\]
This removes the common entire gauge of W and the multiplicative normalization of m, but not an additive shift. The ordered pair itself fixes the additive origin because theta=0 is part of the data.

A more robust pair-relative determinant is obtained directly from the rank-one perturbation determinant H_0 relative to H_pi:
\[
\boxed{
\Delta_{0/\pi}(z;z_*)
=
\frac{m_a(z)}{m_a(z_*)}
}
\]
up to the fixed sign convention, which cancels in the normalized ratio.

## 4. Convergence theorem for an ordered pair

Suppose J_a embeds the finite simple sectors into a common Hilbert space and:
1. H_{a,pi} -> H_{infty,pi} in generalized strong resolvent sense;
2. H_{a,0} -> H_{infty,0} in generalized strong resolvent sense;
3. the rank-one resolvent differences do not vanish degenerately and one defect normalization is fixed.

Then the normalized perturbation determinants / cross-ratios converge:
\[
\boxed{
\Delta^{(a)}_{0/\pi}(z;z_*)
\to
\Delta^{(\infty)}_{0/\pi}(z;z_*).
}
\]
Equivalently,
\[
\boxed{
\frac{m_a(z)}{m_a(z_*)}
\to
\frac{m_\infty(z)}{m_\infty(z_*)}.
}
\]

To recover m_a absolutely still requires one scalar calibration m_a(z_*) -> m_infty(z_*). But for many normalization-free observables the cross-ratio is the canonical object.

## 5. Connection with the project HB ratio

The project target
\[
R_a^{proj}(z)=\frac1{1-icm_a(z)}
\]
is not invariant under arbitrary rescaling of m, because c fixes an absolute infinite normalization.

However define a calibrated finite coefficient from one nonreal base point:
\[
\boxed{
c_a(z_*):=
\frac{\rho_*}{m_a(z_*)},
}
\]
where rho_* is any fixed target dimensionless value. Then
\[
1-i c_a m_a(z)
=
1-i\rho_*\frac{m_a(z)}{m_a(z_*)}.
\]
Therefore pair-relative convergence alone yields convergence of the calibrated HB ratio.

If the infinite target is used to set
\[
\rho_*=c_\infty m_\infty(z_*),
\]
then
\[
\boxed{
R_a^{cal}(z)
=
\left[
1-i c_\infty m_\infty(z_*)\frac{m_a(z)}{m_a(z_*)}
\right]^{-1}
\to
[1-i c_\infty m_\infty(z)]^{-1}.
}
\]

This separates the difficult absolute normalization into ONE scalar value at z_*, while all z-dependence comes from the ordered-pair perturbation determinant.

## 6. Why this matters for Suzuki's heuristic

Suzuki allows a full entire factor exp(phi(a,z)). The boundary-triple analysis shows that, for the normalization-free project model, the z-dependent extension information can in principle be reduced to a normalized rank-one perturbation determinant plus one scalar calibration.

Thus a strong finite-to-infinite theorem need not first control raw W(a,theta;z) as an entire function. It can target the much more rigid object
\[
\boxed{
\Delta^{(a)}_{0/\pi}(z;z_*).
}
\]

## 7. Next gate

Investigate whether the finite characteristic quotient
\[
\Delta^{(a)}_{0/\pi}(z;z_*)
=
\frac{W_0(a,z)W_\pi(a,z_*)}
{W_\pi(a,z)W_0(a,z_*)}
\]
can be computed directly from Suzuki's continuous-kernel defect equations without reconstructing either W_0 or W_pi absolutely.

If yes, this provides a numerically and analytically stable observable for the chi_-4 transfer lane and avoids the failed raw-zero/box-normalization strategy.
