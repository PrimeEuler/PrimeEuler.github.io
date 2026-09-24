# Cone Derivation Ledger v13.773 — Lane A Correction: Basepoint Compatibility Identities Collapse the Artificial Schur-Nonresonance Gate

Date: 2026-09-24

Lane: A.

Status: **[Audit/D] correction of v13.745, v13.758, v13.761, v13.765–766 and checkpoint v13.769 insofar as they treat \(R_A1\), \(R_Ax\), and the resulting Schur denominators as ordinary independent inverse-source responses.** The source-faithful finite deficiency equation itself (v13.742–743) is retained. v13.770–772 remain valid as structural kernel/rapidity observations, with the present correction sharpening their consequence.

Parents: v13.282, v13.742–743, v13.745, v13.758, v13.761, v13.765–766, v13.769–772.

## 0. Synchronization and trigger

External Audit Round 96 v13.771 PASSed the divisor-shell test v13.770. v13.772 then decomposed Suzuki's primitive kernel into a translation-invariant bulk plus polynomial/affine sector and warned that the corrected source space cannot be identified with an unconstrained \(L_0^2\) resolvent.

Re-reading the source-faithful equation recorded in v13.742–743 and the exact Section-8 first-kind equation recorded already in v13.282 reveals a stronger compatibility identity that invalidates the later artificial Schur gate.

Live ledger rechecked immediately before this write: v13.772 is head; no collision.

## 1. Source-faithful primitive operator [D]

Suzuki's Section-8 first-kind equation is recorded in v13.282 as
\[
\boxed{
\int_{-A}^{A}k_A(x,y)(-v(y))\,dy
=
C e^x+A_1x+B_1.
}
\]

Let
\[
(K_Av)(x)=\int_{-A}^{A}k_A(x,y)v(y)\,dy.
\]
Then the actual primitive left-hand operator is
\[
\boxed{\mathcal L_A=-K_A}
\]
on its admissible deficiency domain/range.

The boundary moments are
\[
I_0=\ell_{0,A}(v)=(K_Av)(0),
\qquad
I_1=\ell_{1,A}(v)=(K_Av)'(0).
\]

The source-faithful affine coefficients are
\[
A_1=-I_1-C,\qquad B_1=-I_0-C.
\]

Therefore
\[
\boxed{
-K_Av
=
C(e^x-1-x)-I_1x-I_0.
}
\tag{1}
\]

## 2. Basepoint evaluation is an identity, not an independent scalar equation [D]

Evaluate (1) at \(x=0\). The left side is
\[
-(K_Av)(0)=-I_0.
\]
The right side is
\[
C(1-1-0)-0-I_0=-I_0.
\]

Thus
\[
\boxed{-I_0=-I_0.}
\]

Differentiate (1) and evaluate at \(x=0\). The left side is
\[
-(K_Av)'(0)=-I_1.
\]
The right side is
\[
C(e^0-1)-I_1=-I_1.
\]

Thus
\[
\boxed{-I_1=-I_1.}
\]

Consequently the two “moment closure equations” obtained in v13.745 by applying \(\ell_0,\ell_1\) after introducing an unconstrained inverse are not additional equations. At the source-faithful operator level they are the two basepoint compatibility identities built into the affine integration constants.

## 3. Exact range constraints for any formal inverse [D/N]

Suppose, only formally, that \(R_A=\mathcal L_A^{-1}=(-K_A)^{-1}\) exists on a source \(f\) sufficiently regular at the basepoint. Then
\[
-K_A R_A f=f.
\]
Taking value and derivative traces at \(0\) gives
\[
\boxed{
\ell_{0,A}(R_Af)=-f(0),
}
\]
\[
\boxed{
\ell_{1,A}(R_Af)=-f'(0).
}
\tag{2}
\]

Apply (2) to the sources used in v13.745:

For \(f=1\),
\[
\boxed{M_{00}=\ell_0(R_A1)=-1.}
\]

For \(f=x\),
\[
\boxed{M_{1x}=\ell_1(R_Ax)=-1.}
\]

For
\[
f_e=e^x-1-x,
\]
we have
\[
f_e(0)=f_e'(0)=0,
\]
so
\[
\boxed{M_{0e}=M_{1e}=0.}
\]

Parity also gives the cross terms \(M_{0x}=M_{10}=0\).

Hence the formal response matrix necessarily gives
\[
\boxed{
1+M_{00}=1+M_{1x}=0,
\qquad
M_{0e}=M_{1e}=0.
}
\]

The v13.745 ratios
\[
\frac{M_{0e}}{1+M_{00}},
\qquad
\frac{M_{1e}}{1+M_{1x}}
\]
therefore become \(0/0\), not finite Schur feedback ratios.

This is not a physical resonance theorem. It proves that the decomposition into independent inverse responses to \(1,x,e^x-1-x\) is incompatible with treating the primitive first-kind operator as an ordinary unconstrained invertible map.

## 4. Correction to the previous Schur-nonresonance program [Audit/N]

The following load-bearing program is retracted:

\[
M_{00}>-1,\qquad M_{1x}>-1,
\]
or
\[
|M_{00}|<1,\qquad |M_{1x}|<1,
\]
as a required nonresonance theorem for the source-faithful Suzuki deficiency equation.

Under the formal inverse notation these quantities are forced to \(-1\) by the defining trace identities. Therefore their apparent “dangerous denominators” were artifacts of splitting a compatibility-constrained first-kind equation into source components that are not independently admissible.

Accordingly, the following earlier interpretations require correction:

- v13.745: the \(2\times2\) moment system is not an independent closure system when \(\mathcal L_A=-K_A\) is used source-faithfully.
- v13.758/761: lower-bounding \(1+M_{00}\), \(1+M_{1x}\) is not the correct remaining boundary gate.
- v13.765: the associated rank-one Fredholm determinants encode the artificial split, not an established physical boundary resonance.
- v13.766: the coupling-homotopy analysis of those artificial determinants is algebraically correct conditional on their definitions but not a source-faithful nonresonance route.
- v13.769: its Lane-A “load-bearing open item” is superseded by this correction.

No claim is made that the actual Suzuki finite deficiency problem is singular.

## 5. What remains genuinely unknown [D/O]

Equation (1) shows that \(I_0\) and \(I_1\) are integration/boundary constants. Their values are not determined by evaluating the primitive equation at the basepoint because those evaluations are tautologies.

The genuine finite problem must determine them from Suzuki's admissible domain/deficiency normalization and global solution conditions.

Thus the correct unknown ratios remain
\[
\boxed{
r_{0,A}:=\frac{I_{0,A}}{C_A},
\qquad
r_{1,A}:=\frac{I_{1,A}}{C_A},
}
\]
but **not** through the retracted formulas
\[
r_{0,A}=\frac{M_{0e}}{1+M_{00}},
\qquad
r_{1,A}=\frac{M_{1e}}{1+M_{1x}}.
\]

The exact affine edge coefficients from v13.743 remain valid:
\[
\boxed{
\alpha_A=-e^{-A}(1+r_{1,A}),
}
\]
\[
\boxed{
\beta_A=-e^{-A}\left[A(1+r_{1,A})+1+r_{0,A}\right].
}
\]

Therefore the true asymptotic gate is direct control of \(I_0/C\) and \(I_1/C\) from the admissible global deficiency solution.

## 6. Relation to v13.772 [D/I]

v13.772 found
\[
k_A(x,y)
=
h(x-y)
-\lambda\left(\frac{x^2+y^2}{4A}+\frac A6\right),
\qquad
h(r)=g(r)+\frac{\lambda}{2}|r|,
\]
and showed that the explicit polynomial sector becomes primitive/affine boundary data after zero-mean projection.

The present correction explains exactly why that boundary information cannot be recovered by separately inverting the bulk operator on \(1\) and \(x\): those affine modes are compatibility data of the twice-integrated equation, not free bulk sources.

Thus v13.772's warning is strengthened to:
\[
\boxed{
\text{translation-invariant bulk solve}
+
\text{independent boundary/domain conditions},
}
\]
not
\[
\text{bulk inverse}+\text{rank-one Schur feedback on }1,x.
\]

## 7. Correct next gate [C]

The next Lane-A problem is now cleaner:

1. retain the translation-invariant primitive kernel
\[
h(x-y)=g(x-y)+\frac{\lambda}{2}|x-y|;
\]
2. solve/analyze the homogeneous or compensated bulk equation only on the compatibility subspace;
3. treat \(I_0,I_1\) as boundary integration constants;
4. use Suzuki's actual deficiency-domain normalization/global endpoint conditions to determine the two ratios
\[
I_0/C,\qquad I_1/C;
\]
5. only then test
\[
r_{1,A}=o(e^A/A),\qquad r_{0,A}=o(e^A)
\]
or the sharper combined v13.743 edge criterion.

The natural analytic machinery is therefore a Wiener–Hopf/boundary-value problem with two integration constants, not a Schur-complement nonresonance problem.

## Result

The supposed Lane-A Schur denominators collapse identically under the source-faithful primitive operator:
\[
\boxed{
M_{00}=M_{1x}=-1,\qquad M_{0e}=M_{1e}=0
}
\]
whenever the formal inverse responses are meaningful.

This does **not** show physical resonance. It shows that the inverse-source decomposition introduced in v13.745 was not compatible with the range constraints of Suzuki's first-kind equation.

The source-faithful open problem is restored to the direct boundary constants:
\[
\boxed{
I_{0,A}/C_A,\qquad I_{1,A}/C_A.
}
\]

No RH/Hilbert–Pólya/nonresonance theorem is claimed.
