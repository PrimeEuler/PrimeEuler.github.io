# Cone Derivation Ledger v13.799 — Lane A Pole-Parity Sign Correction, Legacy Odd-Certificate Hold, and Corrected Fast-Assembly Compatibility

Date: 2026-09-25

Lane: A.

Status: [R] correction to the older odd-sector pole convention; [D] source/form derivation; [N] corrected finite diagnostics; [G] legacy odd certificates placed on HOLD pending replay; [C] corrected fast-builder route opened.

Parents: v13.291, v13.403, v13.417, v13.451–453, v13.796–798.

Research artifact:

- research-notes/suzuki_form_core_parity_pole_sign_regression.py
- commit e908f7f1cf742e537cf50695e4d8de49f4037d68

## 0. Why this entry exists

v13.797 explicitly required checking the existing protected-subspace/Feshbach machinery for compatibility before reusing it.

The even-v machinery was found compatible with the current source-faithful form realization.

The older odd-v machinery was not. The mismatch was traced exactly to the pole channel: the older odd-sector lineage beginning at v13.403 uses +2 d d^T for the sinh pole channel, whereas the current direct form, already used by v13.291, v13.795, and v13.798, gives -2 d d^T.

This is a source/form sign issue, not a floating-point issue.

No v13.800+ entry existed at the collision check preceding this write.

## 1. Exact source-level pole identity [D]

Suzuki's pole term in the screw function is

[
g_{\rm pole}(t)
=
-4\left(e^{|t|/2}+e^{-|t|/2}-2\right)
=
-8\left(\cosh(|t|/2)-1\right).
]

On the Dirichlet form core, with test functions \(\psi,\phi\in H_0^1(-1,1)\),

[
Q_{\rm pole}[\psi,\phi]
=
\iint
g_{\rm pole}(x-y)
\psi'(x)\phi'(y)\,dx\,dy.
]

The constant term drops because

[
\int_{-1}^1\psi'(x)\,dx
=
\psi(1)-\psi(-1)
=
0.
]

Using

[
\cosh\frac{x-y}{2}
=
\cosh\frac x2\cosh\frac y2
-
\sinh\frac x2\sinh\frac y2
]

and integration by parts,

[
\int\psi'(x)\cosh(x/2)\,dx
=
-\frac12\int\psi(x)\sinh(x/2)\,dx,
]

[
\int\psi'(x)\sinh(x/2)\,dx
=
-\frac12\int\psi(x)\cosh(x/2)\,dx.
]

Therefore

[
\boxed{
Q_{\rm pole}[\psi,\phi]
=
2\langle\psi,\cosh(x/2)\rangle
 \langle\phi,\cosh(x/2)\rangle
-
2\langle\psi,\sinh(x/2)\rangle
 \langle\phi,\sinh(x/2)\rangle.
}
]

Define

[
c_n=\langle\psi_n,\cosh(x/2)\rangle,
\qquad
d_n=\langle\psi_n,\sinh(x/2)\rangle.
]

Then the full pole matrix is

[
\boxed{
A_{\rm pole}=2cc^T-2dd^T.
}
]

Parity fixes the channels:

- odd Dirichlet mode number \(n\) means even-v; \(d_n=0\), hence
  [
  \boxed{A_{\rm pole}^{(+)}=+2cc^T;}
  ]
- even Dirichlet mode number \(n\) means odd-v; \(c_n=0\), hence
  [
  \boxed{A_{\rm pole}^{(-)}=-2dd^T.}
  ]

Thus the older v13.403 formula \(P_{\rm pole}^{\rm odd}=+2dd^T\) has the wrong sign.

## 2. Independent numerical regression [N]

The new regression script compares the exact closed identity above with the pole component independently assembled by research-notes/suzuki_componentwise_high_precision_audit.py.

At high precision the identity agrees entrywise to the working precision.

Representative diagonal checks:

For \(n=1\), even-v,

[
A_{{\rm pole},11}
=
+3.3990095309706886781456965\ldots
=
2c_1^2.
]

For \(n=2\), odd-v,

[
\boxed{
A_{{\rm pole},22}
=
-0.2093615780898617975648995\ldots
=
-2d_2^2.
}
]

The off-diagonal odd-v example \(m=2,n=4\) likewise gives

[
A_{{\rm pole},24}
=
-0.1066569712469395458530105\ldots
=
-2d_2d_4.
]

The older \(+2dd^T\) and corrected \(-2dd^T\) odd matrices differ by

[
\boxed{
4dd^T.
}
]

On the \(n=2\) diagonal,

[
4d_2^2
=
0.4187231561797235951297968\ldots,
]

exactly the discrepancy observed when the archived odd builder was compared against the current source-faithful form matrix.

## 3. Why the old audit did not catch this [Audit]

External Audit Round 26 checked the closed magnitude formula

[
d_n
=
\frac{2k_n\sinh(1/2)}
{k_n^2+1/4},
\qquad
k_n=\frac{n\pi}{2},
]

against direct quadrature.

That magnitude formula is correct.

However, verifying the overlap magnitude does not determine the sign with which the sinh rank-one term enters the quadratic form. The load-bearing sign comes from the difference in the hyperbolic addition law combined with the overall negative coefficient in \(g_{\rm pole}\).

Therefore the earlier magnitude check did not validate the \(+2dd^T\) Loewner claim.

## 4. Consequence for the older odd-sector certificate lineage [R/G]

The following older statements cannot be inherited as currently justified:

- v13.403's positive odd pole formula;
- v13.417's Loewner reduction \(A_{FF}=A_{FF}^{(0)}+2dd^T\succeq A_{FF}^{(0)}\);
- downstream odd-sector certificate calculations that assemble the full odd matrix with \(+2dd^T\), including the frozen-Schur/cross/residual pipeline used for v13.451;
- therefore the promoted conclusion \(\operatorname{ind}_{\le0}(A_{\rm odd}(1))\le2\) and the dependent full-parity \(\operatorname{ind}_{\le0}(A_{a=1})\le6\) must be placed on HOLD pending corrected odd-sector replay.

This does not prove either index bound false. It means the existing certificate is not source-faithful under the corrected pole sign and cannot presently support those theorem statements.

The independently certified even-v index bound is not touched by this correction because its pole channel is indeed \(+2cc^T\).

## 5. Current Lane A protected-resolvent work survives [G]

v13.795 and v13.798 use component_matrices_mp from the direct source decomposition

[
A=A_{\rm pole}+A_{\rm prime}+A_{\rm arch}.
]

That implementation integrates the actual pole screw term and therefore already carries the parity-signed identity \(2cc^T-2dd^T\).

Hence the v13.798 protected-subspace conclusions remain valid:

- both parity source-resolvent blocks at \(N=16\) show a four-level near-null ladder;
- four protected directions leave a stiff complement;
- the protected/Feshbach and full spectral quadratic forms agree at the reported high precision;
- the current \(\kappa_{0,N}\) sequence is unaffected by this correction.

No recomputation of v13.798 is required solely because of the legacy odd sign error.

## 6. Corrected fast odd builder is compatible with the current direct form [N]

The archived odd fast builder's non-pole scalar formulas were compared with the current source-faithful odd block.

With the archived \(+2dd^T\) pole sign, the mismatch is order one at the lowest mode, as expected.

Changing only

[
+2dd^T
\quad\longrightarrow\quad
-2dd^T
]

gives agreement with the current odd-v \(N=16\) block to

[
\boxed{
\max_{i,j}
|A^{(-)}_{\rm direct}-A^{(-)}_{\rm fast,corrected}|
\approx
8.7\times10^{-23}
}
]

at the tested high precision.

For comparison, the analogous archived even-v fast builder already agrees with the current direct even-v block at approximately \(8\times10^{-23}\) entrywise on the same overlap.

Therefore the old closed-form/Feshbach infrastructure can be reused for larger Lane A cutoffs provided the odd sinh pole sign is corrected.

## 7. Corrected M=4000 finite-high midpoint diagnostic [N]

The old odd finite-high block is

[
F=\{22,24,\ldots,4000\}.
]

The archived pole-free midpoint value was

[
\lambda_{\min}(A_{FF}^{(0)})
\approx
0.5328423837861.
]

The old, incorrectly positive-pole full matrix gives

[
\lambda_{\min}(A_{FF}^{\rm old})
\approx
0.53374499902694.
]

Replaying the same fast source formulas with the corrected negative pole,

[
A_{FF}^{\rm corr}
=
A_{FF}^{(0)}-2d_Fd_F^T,
]

gives the midpoint diagnostic

[
\boxed{
\lambda_{\min}(A_{FF}^{\rm corr})
\approx
0.53191549510157.
}
]

Thus the corrected midpoint still lies above \(0.53\), with margin

[
\boxed{
0.00191549510157\ldots.
}
]

However, the old Loewner shortcut is unavailable. On this finite-high block,

[
\|2d_Fd_F^T\|_2
=
2\|d_F\|_2^2
\approx
0.0208331092258,
]

which is much larger than the pole-free \(0.002842\) excess above \(0.53\). Therefore one cannot recover the \(0.53\) lower bound merely by subtracting an operator-norm bound from the pole-free certificate.

A new source-faithful corrected finite-high factorization/replay is required.

## 8. Updated compatibility map

Reusable without change:

- current direct form-core matrix assembly;
- current analytic source overlaps;
- v13.798 protected/Feshbach algebra;
- generic Schur residual identities;
- even-v closed-form/Feshbach matrix formulas.

Reusable only after correction:

- odd-v closed-form matrix formulas, with \(+2dd^T\to-2dd^T\).

Not presently reusable as certificates:

- old odd frozen \(Q_8,L_0\) theorem payload as a positivity certificate;
- old odd normalized \(C/H\) replay;
- v13.451 odd index-\(\le2\) promotion;
- v13.452/v13.453 dependent full-parity index-\(\le6\) promotion.

The frozen dyadic data may remain useful as historical starting vectors, but they must be tested against the corrected matrix rather than assumed valid.

## 9. Next Lane A gate

The protected source-resolvent program should now proceed with the corrected fast parity builders:

1. freeze a common low protected basis under the current direct form;
2. use the audited even fast builder unchanged;
3. use the corrected odd fast builder with \(-2dd^T\);
4. prove overlap agreement against the current direct form on progressively larger finite prefixes;
5. eliminate the stiff complement by Feshbach while carrying the analytic source vector;
6. track the protected eigenvalues, complement gaps, source coordinates, \(E_e,E_o\), and \(\kappa_0\) as the cutoff grows;
7. do not promote \(\kappa_1\) until \(\kappa_0\) stabilizes under that corrected cutoff enlargement.

Separately, restoration of the historical odd/full-parity inertia theorems requires a dedicated corrected-certificate replay rather than silent reuse inside the Lane A source-resolvent calculation.

## Result

[
\boxed{
A_{\rm pole}=2cc^T-2dd^T.
}
]

[
\boxed{
A_{\rm pole}^{(+)}=+2cc^T,
\qquad
A_{\rm pole}^{(-)}=-2dd^T.
}
]

[
\boxed{
\textbf{The old odd +2dd^T certificate convention is corrected and placed on HOLD.}
}
]

[
\boxed{
\textbf{The corrected odd fast builder matches the current source-faithful form and can now support the next Lane A Feshbach enlargement.}
]
