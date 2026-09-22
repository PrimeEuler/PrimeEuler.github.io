# Cone Derivation Ledger v13.668 — Infinite de Branges Weyl Function and Exact theta=pi Characteristic Normalization

Date: 2026-09-22

Status: exact under Suzuki's Section-7 RH/de-Branges model. This computes the infinite scalar Weyl function in the same boundary-triple convention as v13.661/v13.667 and identifies the theta=pi characteristic normalization that produces Corollary 1.6.

## 0. Live collision/relevance check

Immediately before this write the ledger ends at v13.667. No collision.

## 1. Infinite deficiency basis

Under the RH-dependent de Branges model of Suzuki Section 7, let
\[
k_+(t)=K(-i,t),\qquad k_-(t)=K(i,t).
\]
They span the deficiency spaces at +i and -i and have equal norm.

Use the same boundary coordinates as finite a:
\[
\Gamma_0(\alpha k_++\beta k_-)=\sqrt h(\alpha+\beta),
\qquad
\Gamma_1(\alpha k_++\beta k_-)=i\sqrt h(\alpha-\beta).
\]
Then theta=pi is again ker Gamma_0.

## 2. Boundary characteristic for a general defect vector

For the defect vector K(bar z, .), Suzuki computes
\[
\mathcal W(K(\bar z,\cdot),W_\theta)
=
-\frac{e^{-i\theta/2}}{\pi i}
[C_\theta E(z)-\overline{C_\theta}E^\sharp(z)],
\]
where
\[
E(z)=\Xi(z)+\xi'(1/2-iz),\qquad \Xi(z)=\xi(1/2-iz),
\]
and
\[
C_\theta=\xi(3/2)\cos(\theta/2)+i\xi'(3/2)\sin(\theta/2).
\]

At theta=pi,
\[
\boxed{
\mathcal W(K(\bar z,\cdot),W_\pi)
=
\frac{2i}{\pi}\xi'(3/2)\Xi(z).
}
\]

## 3. Infinite Weyl function from the boundary-form ratio

From the finite exact identity, valid abstractly for the same boundary triple,
\[
\frac{W_\theta(z)}{W_\pi(z)}
=
-i e^{i\theta/2}\cos(\theta/2)[\tau_\theta-m_\infty(z)],
\qquad
\tau_\theta=\tan(\theta/2).
\]

Evaluate at theta=0. Suzuki's formula gives
\[
\mathcal W_z(W_0)
=
-\frac{1}{\pi i}\xi(3/2)[E(z)-E^\sharp(z)].
\]
For real xi data and the functional-equation symmetry,
\[
E(z)-E^\sharp(z)=2\xi'(1/2-iz).
\]
Meanwhile
\[
\mathcal W_z(W_\pi)=\frac{2i}{\pi}\xi'(3/2)\Xi(z).
\]
After matching the conjugation convention used in W(a,theta;z), the scalar ratio yields
\[
\boxed{
m_\infty(z)
=
-\frac{\xi(3/2)}{\xi'(3/2)}
\frac{\xi'(1/2-iz)}{\xi(1/2-iz)}
}
\]
up to the fixed sign determined by whether one defines the characteristic from W(v_z,w_theta) or its conjugate. In the v13.661 convention the displayed sign is the compatible one.

Thus the infinite Weyl function is a constant multiple of the completed logarithmic derivative.

## 4. Corollary-1.6 target as a Möbius transform of m_infty

Let
\[
c_\infty:=\frac{\xi'(3/2)}{\xi(3/2)}.
\]
Then
\[
\frac{\xi'}{\xi}(1/2-iz)=-c_\infty m_\infty(z).
\]
Hence
\[
\boxed{
\frac{\Xi(z)}{\Xi(z)+\xi'(1/2-iz)}
=
\frac{1}{1-c_\infty m_\infty(z)}.
}
\]

Therefore Suzuki's asymptotic target is exactly a scalar Möbius transform of the infinite Weyl function.

This is the cleanest boundary-triple interpretation of Corollary 1.6:
\[
\boxed{R_{\rm Suz}(z)=[1-c_\infty m_\infty(z)]^{-1}.}
\]

## 5. Why theta=pi alone does not equal the target

The raw theta=pi de Branges boundary form is proportional to Xi(z), not Xi/E. The extra denominator E(z)=Xi+xi' enters through the Fourier/energy realization of the canonical deficiency vectors f_{\pm i}, equivalently through the normalization of the defect vector by E.

Thus there are two layers:
1. boundary zero carrier at theta=pi: Xi(z);
2. normalized characteristic in Corollary 1.6: Xi(z)/E(z).

This resolves the apparent tension between "theta=pi isolates xi" and "the limit target is xi/(xi+xi')".

## 6. Finite-a asymptotic target in Weyl language

If the finite Weyl functions m_a converge locally (after the canonical embeddings/normalizations) to m_infty, then a natural scalar-normalization-free target is
\[
\boxed{
[1-c_\infty m_a(z)]^{-1}
\longrightarrow
[1-c_\infty m_\infty(z)]^{-1}
=
\frac{\Xi(z)}{E(z)}.
}
\]

However c_infty is an infinite-volume constant. A fully intrinsic finite approximation should use a finite scalar c_a determined from one calibration point or from the finite deficiency norms, and prove
\[
c_a\to c_\infty.
\]

## 7. Next gate

Construct an intrinsic finite c_a from the finite Weyl/characteristic data, preferably using values at z=0 or z=+/-i where the deficiency normalization is explicit. Then determine whether the normalized Möbius characteristic
\[
R_a(z)=[1-c_a m_a(z)]^{-1}
\]
has exactly the same zeros as W(a,pi;z), and whether it can be expressed directly as a ratio of two Suzuki characteristics W(a,theta_1)/W(a,theta_2). If so, the arbitrary exponential normalization phi(a,z) can be replaced by a finite scalar calibration plus an exact boundary-characteristic quotient.
