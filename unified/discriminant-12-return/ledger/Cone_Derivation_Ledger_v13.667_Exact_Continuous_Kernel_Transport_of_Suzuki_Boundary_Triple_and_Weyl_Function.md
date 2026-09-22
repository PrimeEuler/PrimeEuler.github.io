# Cone Derivation Ledger v13.667 — Exact Continuous-Kernel Transport of the Suzuki Boundary Triple and Weyl Function

Date: 2026-09-22

Status: exact finite-a transport theorem, source-faithful to Suzuki Section 8. This moves the active lane from the unbounded A_a realization to the continuous-kernel S_a realization without changing the Weyl function, boundary determinant, characteristic zeros, or extension parameter.

## 0. Live collision/relevance check

Immediately before this write the ledger ends at v13.666. No collision. v13.666 corrected the asymptotic source target; the present result is finite-a and exact.

## 1. Suzuki's unitary transport

Let
\[
T_a=A_a-\lambda I,\qquad \lambda<\lambda_a,
\]
and
\[
S_a=G_a-\lambda K_a,\qquad K_a=(-\Delta_N)^{-1}.
\]
Suzuki proves
\[
\|Dv\|_{S_a}=\|v\|_{T_a}
\]
on the core, hence D extends to an isometric isomorphism
\[
\boxed{\bar D:\mathcal H(T_a)\overset{\sim}{\longrightarrow}\mathcal H(S_a).}
\]

Define
\[
\widetilde{\mathscr D}_a=\bar D\,\mathscr D_a\,\bar D^{-1}.
\]
Then
\[
\widetilde{\mathscr D}_a^*=\bar D\,\mathscr D_a^*\,\bar D^{-1}.
\]

## 2. Transported deficiency basis and boundary triple

Let v_\pm be Suzuki's equal-norm deficiency vectors and set
\[
u_\pm=\bar D v_\pm.
\]
Then
\[
\widetilde{\mathscr D}_a^*u_\pm=\pm i u_\pm,\qquad
\|u_+\|_{S_a}=\|u_-\|_{S_a}=\sqrt{h_a}.
\]

If
\[
u=u_0+\alpha u_++\beta u_-,
\]
define
\[
\boxed{
\widetilde\Gamma_0u=\sqrt{h_a}(\alpha+\beta),\qquad
\widetilde\Gamma_1u=i\sqrt{h_a}(\alpha-\beta).
}
\]
Equivalently,
\[
\boxed{
\widetilde\Gamma_j=\Gamma_j\bar D^{-1},\quad j=0,1.
}
\]
Therefore the Green identity is preserved exactly.

The theta=pi extension remains
\[
\boxed{\widetilde H_{a,\pi}=\ker\widetilde\Gamma_0.}
\]

## 3. Weyl function is invariant

Let
\[
\gamma_a(z)=(\Gamma_0|_{\ker(\mathscr D_a^*-z)})^{-1},
\qquad
m_a(z)=\Gamma_1\gamma_a(z).
\]
The transported gamma field is
\[
\boxed{\widetilde\gamma_a(z)=\bar D\,\gamma_a(z).}
\]
Hence
\[
\widetilde\Gamma_0\widetilde\gamma_a=1
\]
and
\[
\boxed{
\widetilde m_a(z)
=\widetilde\Gamma_1\widetilde\gamma_a(z)
=\Gamma_1\gamma_a(z)
=m_a(z).
}
\]

Thus the scalar Weyl function is EXACTLY representation-invariant under Suzuki's Section-8 unitary map.

## 4. Krein resolvent and determinant are invariant

For tau_theta=tan(theta/2),
\[
(\widetilde H_{a,\theta}-z)^{-1}
-(\widetilde H_{a,\pi}-z)^{-1}
=
\widetilde\gamma_a(z)[\tau_\theta-m_a(z)]^{-1}
\widetilde\gamma_a(\bar z)^*.
\]
This is the unitary conjugate of the v13.661 formula.

Therefore
\[
\boxed{
\widetilde\Delta^{bdry}_{a,\theta/\pi}(z;z_*)
=
\Delta^{bdry}_{a,\theta/\pi}(z;z_*)
=
\frac{\tau_\theta-m_a(z)}
{\tau_\theta-m_a(z_*)}.
}
\]

## 5. Characteristic is invariant

Suzuki's Section 8.3 boundary form gives
\[
W(a,\theta;z)
=
\overline{\widetilde W(u_{\bar z},\widetilde w_\theta)}
=
\overline{W(v_{\bar z},w_\theta)}.
\]
Thus W itself is unchanged by the continuous-kernel transport.

Consequently the exact v13.661 identity holds verbatim in the S_a model:
\[
\boxed{
\frac{W(a,\theta;z)/W(a,\pi;z)}
{W(a,\theta;z_*)/W(a,\pi;z_*)}
=
\frac{\tau_\theta-m_a(z)}
{\tau_\theta-m_a(z_*)}.
}
\]

## 6. The actual continuous-kernel defect equation

Suzuki gives
\[
S_a u_z=\bar D e_z,\qquad e_z(x)=e^{-izx}.
\]
This is the correct operator equation in the continuous-kernel realization.

For the deficiency points,
\[
\boxed{
S_a u_\pm=C_\pm\bar D e_{\pm i}.
}
\]
This must be distinguished from the twice-integrated first-kind equation (8.5), which Suzuki explicitly warns is only formally equivalent after differentiating twice and ignores domain issues.

Therefore the source-faithful numerical target is S_a u_z=\bar D e_z, not the projected equation obtained by simply deleting or integrating kernel terms.

## 7. Structural payoff

The finite-a spectral data can now be studied entirely in the continuous-kernel model:
\[
\boxed{
(G_a-\lambda K_a)u_z=\bar D e_z,
}
\]
while retaining exactly:
- the deficiency indices (1,1);
- the theta=pi reference extension;
- the scalar Weyl function m_a(z);
- the Krein determinant;
- the entire characteristic W(a,theta;z);
- the real-zero theorem.

This is the correct replacement for the invalid local Dirichlet bulk-factor route.

## 8. Next gate

Derive m_a(z) directly from the continuous-kernel solutions u_z and the transported boundary coordinates, then identify a scalar-normalization-free quantity suitable for a->infinity. The natural candidate is the cross ratio
\[
\mathcal R_{a,\theta}(z,z_*)
=
\frac{W(a,\theta;z)W(a,\pi;z_*)}
{W(a,\pi;z)W(a,\theta;z_*)},
\]
which equals the normalized Weyl denominator exactly and is invariant under arbitrary nonzero scalar normalization of W.

For comparison with Corollary 1.6 itself, however, theta=pi W must also be controlled, because the cross ratio compares theta to pi and becomes trivial at theta=pi. The next asymptotic gate must therefore separate (i) extension-relative data from (ii) the absolute theta=pi normalization.
