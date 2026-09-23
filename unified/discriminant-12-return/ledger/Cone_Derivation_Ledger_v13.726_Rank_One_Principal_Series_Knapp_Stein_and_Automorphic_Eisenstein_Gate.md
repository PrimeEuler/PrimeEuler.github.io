# Cone Derivation Ledger v13.726 — Rank-One Principal Series, Knapp–Stein, and Automorphic Eisenstein Gate

**Date:** 2026-09-23  
**Status:** exact structural derivation with normalization caveats explicitly separated  
**Parent:** v13.722 (shifted Casimir theta kernel / pure Xi current)  
**Cross-thread check:** v13.723 external audit passed v13.717–722; v13.724–725 are Suzuki edge-operator work and do not collide with this analytic-number-theory / rank-one representation lane.

## 1. Purpose

This checkpoint records the gates after v13.722: the rank-one radial and A-Casimir identification; the unflattened theta vector and contact term; the full line-model principal-series test; canonical spherical/Harish–Chandra normalization; Knapp–Stein comparison; and the global SL(2,Z) Eisenstein-series gate.

The main conclusion is that the common Casimir/Weyl structure is exact, while the zeta-specific gamma/Euler normalization is not supplied by the bare symmetric space. It appears only in the global automorphic scattering matrix.

## 2. Standard rank-one radial Casimir

For
\[
G/K=SL(2,\mathbb R)/SO(2)\simeq\mathbb H^2
\]
with geodesic radius \(t\),
\[
\Delta_{\rm rad}
=
\partial_t^2+\coth t\,\partial_t
=
\frac1{\sinh t}\partial_t(\sinh t\,\partial_t).
\]
Flattening \(L^2(\sinh t\,dt)\) by
\[
(Uf)(t)=\sqrt{\sinh t}\,f(t)
\]
gives
\[
\boxed{
U\Delta_{\rm rad}U^{-1}
=
\partial_t^2-\frac14+\frac1{4\sinh^2 t}.
}
\]
Thus the geodesic radial operator does NOT globally equal \(\partial_t^2-\frac14\); a Pöschl–Teller term remains.

For the Iwasawa A-coordinate \(r\), the restricted-root multiplicity is one and
\[
\rho=\frac12.
\]
The unflattened A-Casimir is
\[
\boxed{\mathcal C_A=\partial_r^2+\partial_r.}
\]
The rho-shift gives the exact identity
\[
\boxed{
e^{r/2}\mathcal C_Ae^{-r/2}
=
\partial_r^2-\frac14.
}
\]
Hence v13.722's shifted operator is exactly the rho-shifted A-constant-term Casimir.

For \(e^{(w-1/2)r}\),
\[
\mathcal C_Ae^{(w-1/2)r}
=
(w^2-\tfrac14)e^{(w-1/2)r}.
\]
This unifies
\[
w=j+\tfrac12\Rightarrow w^2-\tfrac14=j(j+1),
\]
\[
w=k-\tfrac12\Rightarrow w^2-\tfrac14=k(k-1),
\]
and
\[
w=s-\tfrac12\Rightarrow w^2-\tfrac14=s(s-1).
\]

## 3. Unflattened theta vector and contact term

Recall
\[
K_\theta(r)=e^{|r|/2}\psi(e^{2|r|}),
\qquad
\psi(x)=\sum_{n\ge1}e^{-\pi n^2x}.
\]
Define
\[
\boxed{F_\theta(r)=e^{-r/2}K_\theta(r).}
\]
Then
\[
F_\theta(r)=
\begin{cases}
\psi(e^{2r}),&r>0,\\
e^{-r}\psi(e^{-2r}),&r<0.
\end{cases}
\]
It is continuous at zero:
\[
[F_\theta]_0=0.
\]
Using Jacobi inversion at the fixed point gives
\[
\boxed{[F_\theta']_0=-\frac12.}
\]
Therefore
\[
\boxed{
\mathcal C_AF_\theta
=
e^{-r/2}\Phi(r)-\frac12\delta_0.
}
\]
This is exactly the unflattened form of
\[
(\partial_r^2-\tfrac14)K_\theta
=
\Phi-\frac12\delta_0.
\]

The vector is rapidly decreasing at both ends, so
\[
F_\theta\in L^1(\mathbb R)\cap L^2(\mathbb R)
\]
and defines a regular distribution.

Its exact Weyl law is
\[
\boxed{F_\theta(-r)=e^rF_\theta(r).}
\]
Thus with
\[
(\mathcal W_AF)(r)=e^{-r}F(-r),
\]
\[
\mathcal W_A^2=1,\qquad
\mathcal W_AF_\theta=F_\theta,\qquad
[\mathcal W_A,\mathcal C_A]=0.
\]
Hence \(F_\theta\) is a genuine \(A\rtimes W\) distribution vector, but not a fixed-Casimir eigenvector: it is a Casimir wave packet.

## 4. Explicit line-model sl2 action

Take
\[
[H,E]=2E,\qquad [H,F]=-2F,\qquad [E,F]=H
\]
and
\[
E_a=\partial_x,\qquad
H_a=-2x\partial_x+a,\qquad
F_a=-x^2\partial_x+ax.
\]
Direct calculation verifies all three commutators.

For
\[
\Omega=\frac14H^2+\frac12(EF+FE),
\]
the differential terms cancel:
\[
\boxed{\Omega_a=\frac{a(a+2)}4I.}
\]
Setting \(a=2w-1\),
\[
\boxed{\Omega_w=(w^2-\tfrac14)I.}
\]

If \(F_\theta\) were the A-constant term of a vector in one fixed-w principal series, centrality would force
\[
\mathcal C_AF_\theta=(w^2-\tfrac14)F_\theta.
\]
But
\[
\mathcal C_AF_\theta=e^{-r/2}\Phi-\frac12\delta_0
\]
is not proportional to \(F_\theta\). Therefore
\[
\boxed{
F_\theta\text{ cannot come from a single fixed-infinitesimal-character principal-series vector.}
}
\]
The appropriate full-group object must be a principal-series wave packet/direct integral.

## 5. Canonical spherical transform

For unitary parameter \(w=it\), the Harish–Chandra c-function has, up to the fixed normalization constant and elementary \(2^{\pm it}\) phase,
\[
\boxed{
c(t)\propto\frac{\Gamma(it)}{\Gamma(\frac12+it)}.
}
\]
Thus
\[
\boxed{|c(t)|^{-2}\propto t\tanh(\pi t)}
\]
and
\[
d\mu_{\rm Pl}(t)=C_{\rm Pl}|c(t)|^{-2}dt.
\]

For the normalized spherical eigenfunction,
\[
\boxed{
CT_A[\varphi_t](r)
=
c(t)e^{(it-1/2)r}
+
c(-t)e^{(-it-1/2)r}.
}
\]
After the rho-shift,
\[
e^{r/2}CT_A[\varphi_t]
=
c(t)e^{itr}+c(-t)e^{-itr}.
\]

Let
\[
I_\theta(it)=\int_{\mathbb R}K_\theta(r)e^{itr}\,dr.
\]
For a spherical wave packet
\[
V_\theta=\int A_\theta(t)\varphi_t\,d\mu_{\rm Pl}(t),
\]
the coefficient required to recover \(CT_A[V_\theta]=F_\theta\) is, modulo the chosen full-line/half-line inversion constant,
\[
\boxed{
A_\theta(t)\propto c(-t)I_\theta(it).
}
\]
The invariant content is one c-factor dressing the flat theta amplitude, followed by the Plancherel factor \(|c|^{-2}\), so that the A-constant term reduces to ordinary Fourier synthesis.

The Casimir acts fiberwise by
\[
-(t^2+\tfrac14),
\]
hence the coefficient of \(\Omega V_\theta\) is proportional to
\[
c(-t)[\Xi(it)-\tfrac12].
\]
The origin contact term survives canonical spherical normalization.

## 6. Knapp–Stein operator

Parameterize the spherical principal series by
\[
s=\frac12+it.
\]
The standard unnormalized intertwiner
\[
M(s):I(s)\to I(1-s)
\]
acts on the spherical vector by a scalar whose spectral dependence is
\[
\boxed{
m(s)\propto
\frac{\Gamma(s-\frac12)}{\Gamma(s)}
=
\frac{\Gamma(it)}{\Gamma(\frac12+it)}.
}
\]
Thus
\[
\boxed{m(\tfrac12+it)\propto c(t).}
\]

Normalize
\[
R(s)=m(s)^{-1}M(s).
\]
Then
\[
R(s)v_s^0=v_{1-s}^0,
\qquad
R(1-s)R(s)=I
\]
under the standard normalization.

The local Harish–Chandra scattering phase is
\[
\boxed{S_{\rm HC}(t)=\frac{c(-t)}{c(t)}}
\]
up to the elementary convention phase, and \(|S_{\rm HC}(t)|=1\) for real \(t\).

## 7. Compare with the zeta archimedean factor

Let
\[
L_\infty(s)=\pi^{-s/2}\Gamma(s/2).
\]
Its reflection ratio is
\[
\boxed{
S_\zeta(s)
=
\frac{L_\infty(1-s)}{L_\infty(s)}
=
\pi^{s-1/2}
\frac{\Gamma((1-s)/2)}{\Gamma(s/2)}.
}
\]
At \(s=1/2+it\),
\[
\boxed{
S_\zeta(t)
=
\pi^{it}
\frac{\Gamma(\frac14-\frac{it}{2})}
{\Gamma(\frac14+\frac{it}{2})}.
}
\]

This is not the same meromorphic function as \(S_{\rm HC}(t)\). The mismatch is not removable by a constant normalization: the gamma arguments and pole lattices differ.

Therefore
\[
\boxed{S_{\rm HC}\neq S_\zeta.}
\]
What agrees exactly is the Weyl reflection \(s\leftrightarrow1-s\) and the invariant quadratic Casimir.

## 8. Global Eisenstein gate

Take the standard nonholomorphic Eisenstein series
\[
E(z,s)
=
\sum_{\gamma\in\Gamma_\infty\backslash SL(2,\mathbb Z)}
\Im(\gamma z)^s.
\]
Its constant Fourier term is
\[
\boxed{
E_0(y,s)=y^s+\phi(s)y^{1-s},
}
\]
where
\[
\boxed{
\phi(s)
=
\sqrt\pi\,
\frac{\Gamma(s-\frac12)}{\Gamma(s)}
\frac{\zeta(2s-1)}{\zeta(2s)}.
}
\]
With
\[
\Lambda(u)=\pi^{-u/2}\Gamma(u/2)\zeta(u),
\]
this is
\[
\boxed{
\phi(s)=\frac{\Lambda(2s-1)}{\Lambda(2s)}.
}
\]

Thus the global scattering coefficient factors conceptually into the local real Knapp–Stein gamma normalization and the finite-prime Euler ratio. The arithmetic lattice supplies exactly the ingredient absent from the bare symmetric space.

The functional equation gives
\[
\boxed{\phi(s)\phi(1-s)=1.}
\]

## 9. Completed Eisenstein series

Define
\[
\boxed{E^*(z,s)=\Lambda(2s)E(z,s).}
\]
Then
\[
\boxed{
E_0^*(y,s)
=
\Lambda(2s)y^s+\Lambda(2s-1)y^{1-s}.
}
\]
Center \(s=1/2+w\):
\[
\boxed{
E_0^*(y,\tfrac12+w)
=
\Lambda(1+2w)y^{1/2+w}
+
\Lambda(2w)y^{1/2-w}.
}
\]
Under \(w\mapsto-w\), the functional equation \(\Lambda(u)=\Lambda(1-u)\) exchanges the two coefficients exactly:
\[
\Lambda(1-2w)=\Lambda(2w),
\qquad
\Lambda(-2w)=\Lambda(1+2w).
\]
So the completed global Eisenstein constant term realizes the same Weyl geometry internally.

## 10. Compare global Eisenstein with theta/Xi

The theta lane has
\[
\Xi(w)=\xi(\tfrac12+w)
=
\int_{\mathbb R}\Phi(r)e^{wr}\,dr.
\]
The completed Eisenstein constant term instead carries
\[
\Lambda(1+2w),\qquad \Lambda(2w).
\]

These are not \(\Lambda(\tfrac12+w)\), and no constant reparameterization simultaneously turns both Eisenstein channels into the centered Xi argument while preserving the same Weyl reflection.

Forcing \(2s=\tfrac12+w\) makes the companion reflected argument \(\tfrac32-w\), not \(\tfrac12-w\). Forcing \(2s-1=\tfrac12+w\) makes the other channel \(\tfrac32+w\).

There is also an asymptotic obstruction: a single Eisenstein constant term is a sum of two power/exponential A-modes, whereas \(F_\theta\) decays superexponentially at both ends.

Therefore
\[
\boxed{
\text{the standard }SL(2,\mathbb Z)\text{ Eisenstein constant term is not the theta/Xi bilateral current.}
}
\]

The two exact mechanisms are distinct:

1. Jacobi theta + Mellin transform gives the completed Riemann zeta and the positive bilateral kernel \(\Phi\).
2. Global SL2 Eisenstein scattering gives the ratio \(\Lambda(2s-1)/\Lambda(2s)\).

They share the rank-one Weyl involution, centered quadratic Casimir, archimedean gamma normalization, and global Euler factors, but not the same spectral vector or zeta argument.

## 11. Exact chain now established

\[
\boxed{
\mathcal C_A=\partial_r^2+\partial_r
\xrightarrow{\rho\text{-shift}}
\partial_r^2-\frac14
}
\]
and
\[
\boxed{
F_\theta
\to K_\theta
\to \Phi-\frac12\delta_0
\xrightarrow{\mathcal B}
\Xi(w)-\frac12.
}
\]

Full principal-series fibers realize
\[
\boxed{\Omega=w^2-\frac14.}
\]
Canonical spherical synthesis dresses the theta Fourier amplitude by one Harish–Chandra c-factor.

Globally,
\[
\boxed{\phi(s)=\Lambda(2s-1)/\Lambda(2s)}
\]
shows exactly how local gamma and finite-prime Euler factors combine.

## 12. Status

- Geodesic radial Casimir -> exactly \(\partial^2-\frac14\): **FAIL**, residual \(1/(4\sinh^2t)\).
- A-constant-term Casimir -> \(\partial^2-\frac14\): **EXACT**.
- \(F_\theta\) is an \(A\rtimes W\) distribution vector: **EXACT**.
- Contact term \(-\frac12\delta_0\): **EXACT**.
- Single principal-series fiber realizes \(F_\theta\): **FAIL**, central-character obstruction.
- Direct-integral principal-series wave packet: **STRUCTURALLY VALID**, convention constants require a fixed Haar normalization.
- Line-model H,E,F and Casimir \(w^2-\frac14\): **EXACT**.
- Spherical Plancherel density proportional to \(|c|^{-2}\): **EXACT**.
- Unnormalized Knapp–Stein spherical scalar proportional to c: **EXACT**.
- Bare local scattering equals zeta archimedean reflection factor: **FAIL**.
- Global Eisenstein scattering \(\phi(s)=\Lambda(2s-1)/\Lambda(2s)\): **EXACT**.
- Completed Eisenstein Weyl exchange: **EXACT**.
- Standard Eisenstein constant term equals \(F_\theta\)/Xi current: **FAIL**.
- Xi as spectral determinant / Hilbert–Pólya operator: **NOT ESTABLISHED**.

## 13. Next discriminating gates

1. Put the theta/Xi wave packet into the canonical automorphic continuous-spectrum decomposition of \(SL(2,\mathbb Z)\backslash\mathbb H\) and test whether its incoming/outgoing coefficients satisfy the global scattering relation \(\phi(1/2+it)\).
2. Compare that scattering relation with exact evenness of \(K_\theta\); incompatibility would give a clean automorphic obstruction.
3. In parallel, formulate the theta/Mellin construction in its natural Tate/GL1 local-global setting, where \(\pi^{-s/2}\Gamma(s/2)\zeta(s)\) is native, and compare that mechanism with the SL2 Casimir lane.

**Guardrail:** shared Casimir/Weyl geometry is exact, but bare local SL2 scattering and standard global Eisenstein scattering are not themselves the theta/Xi current. No RH, Hilbert–Pólya, or spectral-determinant claim is promoted.
