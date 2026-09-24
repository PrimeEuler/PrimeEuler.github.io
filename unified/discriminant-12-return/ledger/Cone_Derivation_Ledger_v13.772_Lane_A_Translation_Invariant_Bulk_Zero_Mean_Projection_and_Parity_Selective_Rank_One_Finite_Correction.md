# Cone Derivation Ledger v13.772 — Lane A Translation-Invariant Bulk, Zero-Mean Projection, and Parity-Selective Rank-One Finite Correction

Date: 2026-09-24

Lane: A — continuation of v13.770 after External Audit Round 96 (v13.771).

Status: [D] exact kernel decomposition; [D] exact zero-mean projected rank-one correction; [D] odd-channel cancellation; [N] source-space/domain obstruction to naively replacing the corrected response by an \(L_0^2\) resolvent; [C] sharpened next gate.

Parents: v13.282, v13.742, v13.745, v13.749, v13.761, v13.766, v13.770–771.

## 0. Synchronization

External Audit Round 96 v13.771 was read first. It PASSes v13.770 and explicitly endorses carrying out the Suzuki bulk/boundary decomposition while leaving Schur nonresonance open. Live ledger was rechecked immediately before this write: v13.771 remains head; no numbering collision.

## 1. Exact algebraic kernel split [D]

Suzuki's Section-8 kernel is
\[
k_A(x,y)=g(x-y)-\lambda N_A(x,y),
\]
with
\[
N_A(x,y)=\frac{x^2+y^2}{4A}-\frac{|x-y|}{2}+\frac A6.
\]

Therefore
\[
\boxed{
k_A(x,y)
=
h(x-y)
-\lambda\left(\frac{x^2+y^2}{4A}+\frac A6\right),
}
\]
where
\[
\boxed{
h(r):=g(r)+\frac{\lambda}{2}|r|.
}
\]

Thus the finite kernel consists of a translation-invariant convolution kernel \(h(x-y)\) plus an explicit polynomial finite-volume correction.

This decomposition is exact for every finite \(A\).

## 2. Operator form of the finite correction [D]

Define
\[
(P_Av)(x)
:=
\int_{-A}^{A}
\left(\frac{x^2+y^2}{4A}+\frac A6\right)v(y)\,dy.
\]

Let
\[
m_0(v):=\int_{-A}^{A}v(y)\,dy,
\qquad
m_2(v):=\int_{-A}^{A}y^2v(y)\,dy.
\]

Then
\[
\boxed{
(P_Av)(x)
=
\left(\frac{x^2}{4A}+\frac A6\right)m_0(v)
+
\frac1{4A}m_2(v).
}
\]

Hence \(P_A\) has rank at most two on the ambient function space:
\[
\operatorname{Ran}P_A
\subset
\operatorname{span}\{1,x^2\}.
\]

## 3. Exact zero-mean reduction [D]

Suzuki's Section-8 transported space uses
\[
L_0^2(-A,A)
=
\{u\in L^2(-A,A):m_0(u)=0\}.
\]

For \(u\in L_0^2\),
\[
\boxed{
(P_Au)(x)
=
\frac1{4A}m_2(u),
}
\]
a constant function.

Thus, as an ambient map restricted to zero-mean inputs, the explicit polynomial correction has rank one.

However, the constant output is not itself in \(L_0^2\) unless \(m_2(u)=0\). Therefore the correct operator acting *within* \(L_0^2\) must include the orthogonal zero-mean projection
\[
Q_Af
=
f-\frac1{2A}\int_{-A}^{A}f.
\]

Since \(Q_A1=0\),
\[
\boxed{
Q_AP_Au=0
\qquad(u\in L_0^2).
}
\]

This is the key domain reconciliation: the explicit polynomial correction is visible in the unprojected first-kind primitive kernel, but it disappears after projection back to the transported zero-mean \(u=Dv\) space.

This does not mean the boundary data disappear; they re-enter as the affine integration constants in Suzuki's actual equation (8.5), exactly as v13.742 established.

## 4. Parity refinement [D]

For odd \(u_-\),
\[
m_0(u_-)=0,
\qquad
m_2(u_-)=0,
\]
so already before projection
\[
\boxed{P_Au_-=0.}
\]

For even zero-mean \(u_+\),
\[
P_Au_+
=
\frac1{4A}m_2(u_+)\,1,
\]
which is pure constant and hence
\[
Q_AP_Au_+=0.
\]

Therefore:

- odd channel: the explicit polynomial correction vanishes identically even in the unprojected primitive equation;
- even zero-mean channel: it survives only as a constant primitive/affine mode and is annihilated by zero-mean projection;
- the surviving physical information is consequently boundary/affine data, not a bulk \(L_0^2\) operator perturbation.

This gives an exact realization of the v13.742 principle
\[
\boxed{
\text{bulk current}+\text{two boundary constants}.
}
\]

## 5. Why the corrected response moments cannot simply use this projected operator [N]

The corrected one-channel deficiency equation from v13.745 is
\[
\mathcal L_Av_A
=
C_A(e^x-1-x)-I_{1,A}x-I_{0,A}.
\]

Its response notation
\[
u_{1,A}=R_A1,\qquad u_{x,A}=R_Ax
\]
is defined on the corrected deficiency-function/source space after Suzuki's domain/normalization conditions are imposed.

Neither source \(1\) nor, in general, the primitive affine source bookkeeping should be silently identified with an element of the transported zero-mean \(u=Dv\) space. In particular
\[
1\notin L_0^2(-A,A).
\]

Therefore it would be invalid to conclude from
\[
Q_AP_A|_{L_0^2}=0
\]
that the feedback moment \(M_{00}\) has no finite-volume correction, or to replace \(R_A\) by the inverse of the projected convolution operator without constructing the exact source/domain intertwiner.

This is the domain subtlety anticipated before this entry.

## 6. Exact bulk/boundary interpretation [D/I]

The decomposition shows that after two differentiations/projection, the finite Section-8 bulk is governed by the translation-invariant kernel
\[
\boxed{
h(x-y)=g(x-y)+\frac{\lambda}{2}|x-y|.
}
\]

The explicitly \(A\)-dependent polynomial part belongs entirely to the primitive/affine sector:
\[
\operatorname{span}\{1,x,x^2\}
\]
before the corrected deficiency constraints are imposed, and its projected \(L_0^2\) action vanishes.

This matches the already-established fact that twice differentiating Suzuki (8.5) kills the affine terms and loses boundary/domain information.

Hence the divisor-inspired renormalization principle has an exact Suzuki analogue at this level:
\[
\boxed{
\text{translation-invariant bulk current}
+
\text{finite-volume affine/boundary remainder}.
}
\]

The remainder is not a conventional bulk resolvent perturbation. It is encoded by the scalar boundary moments \(I_{0,A},I_{1,A}\).

## 7. Consequence for the two Schur denominators [D/I]

The dangerous factors remain
\[
1+M_{00},
\qquad
1+M_{1x}.
\]

The present decomposition does not prove either is nonzero.

But it sharpens where their finite-\(A\) information lives:

- the odd polynomial correction vanishes identically by parity;
- the even polynomial correction reduces to a constant primitive mode;
- after zero-mean projection neither is an interior bulk perturbation;
- therefore any nontrivial finite-\(A\) Schur feedback beyond the translation-invariant bulk must be carried by the boundary/affine reconstruction embodied in \(\ell_{0,A},\ell_{1,A}\) and the corrected source space.

Thus a standard finite-rank resolvent identity on \(L_0^2\) cannot by itself close the Schur gate.

## 8. Sharpened next gate [C]

The correct next object is not an unconstructed \(R_\infty\). It is the translation-invariant primitive operator
\[
(H_Av)(x)=\int_{-A}^{A}h(x-y)v(y)\,dy
\]
together with the exact affine reconstruction map supplied by Suzuki (8.5).

The next gate is:

1. write the corrected first-kind equation using \(H_A\) plus the explicit moment terms \(m_0,m_2\);
2. insert the definitions of \(I_{0,A},I_{1,A}\);
3. eliminate the primitive polynomial modes using parity and the corrected affine equations;
4. determine whether \(M_{00}\) and \(M_{1x}\) can be expressed as a translation-invariant response plus a finite-dimensional boundary Schur complement.

If so, the nonresonance problem becomes a scalar/matrix boundary determinant over a convolution bulk, which is the appropriate setting for Wiener-Hopf/Fourier analysis. This is a strictly more concrete target than the previously undefined finite-minus-full-line resolvent.

## Result

The divisor-inspired bulk/boundary decomposition exists exactly in Suzuki's finite kernel:
\[
\boxed{
k_A(x,y)
=
\left[g(x-y)+\frac{\lambda}{2}|x-y|\right]
-
\lambda\left(\frac{x^2+y^2}{4A}+\frac A6\right).
}
\]

The explicit finite-volume polynomial correction has rank at most two ambiently, rank one on zero-mean inputs, vanishes identically on odd inputs, and is annihilated by projection back to \(L_0^2\).

Its information is therefore not an interior \(L_0^2\) perturbation; it is precisely primitive/affine boundary data. This validates the bulk-versus-boundary strategy while also explaining why a naive projected resolvent difference would erase the very information needed for the Schur denominators.

No Schur nonresonance theorem is claimed.
