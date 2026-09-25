# Cone Derivation Ledger v13.799 — Lane A Pole-Parity Sign Correction, Legacy Odd-Certificate Hold, and Corrected Fast-Assembly Compatibility

Date: 2026-09-25

Lane: A.

Status: [R] correction to the older odd-sector pole convention; [D] source/form derivation; [N] corrected finite diagnostics; [G] legacy odd certificates on HOLD pending replay.

Formatting note: re-rendered after External Audit Round 102 (v13.802) to restore corrupted LaTeX backslashes. Mathematical content is unchanged.

Parents: v13.291, v13.403, v13.417, v13.451–453, v13.796–798.

Research artifact: suzuki_form_core_parity_pole_sign_regression.py, commit e908f7f1cf742e537cf50695e4d8de49f4037d68.

## 1. Exact source-level pole identity

Suzuki's pole term is
\[
g_{\rm pole}(t)
=
-4\left(e^{|t|/2}+e^{-|t|/2}-2\right)
=
-8\left(\cosh(|t|/2)-1\right).
\]

For \(\psi,\phi\in H_0^1(-1,1)\),
\[
Q_{\rm pole}[\psi,\phi]
=
\iint g_{\rm pole}(x-y)\psi'(x)\phi'(y)\,dx\,dy.
\]

The constant term vanishes because the test functions have zero boundary trace. Using
\[
\cosh\frac{x-y}{2}
=
\cosh\frac x2\cosh\frac y2
-
\sinh\frac x2\sinh\frac y2
\]
and integrating by parts gives
\[
\boxed{
Q_{\rm pole}[\psi,\phi]
=
2\langle\psi,\cosh(x/2)\rangle
 \langle\phi,\cosh(x/2)\rangle
-
2\langle\psi,\sinh(x/2)\rangle
 \langle\phi,\sinh(x/2)\rangle.
}
\]

With
\[
c_n=\langle\psi_n,\cosh(x/2)\rangle,
\qquad
d_n=\langle\psi_n,\sinh(x/2)\rangle,
\]
the full pole matrix is
\[
\boxed{
A_{\rm pole}=2cc^T-2dd^T.
}
\]

Parity therefore gives
\[
\boxed{
A_{\rm pole}^{(+)}=+2cc^T,
\qquad
A_{\rm pole}^{(-)}=-2dd^T.
}
\]

The older odd-sector \(+2dd^T\) convention is incorrect.

## 2. Numerical regression

Representative checks from the source-faithful direct form are
\[
A_{{\rm pole},11}
=
+3.3990095309706886781456965\ldots
=
2c_1^2,
\]
\[
A_{{\rm pole},22}
=
-0.2093615780898617975648995\ldots
=
-2d_2^2,
\]
and
\[
A_{{\rm pole},24}
=
-0.1066569712469395458530105\ldots
=
-2d_2d_4.
\]

The old and corrected odd matrices differ by
\[
4dd^T.
\]
On the \(n=2\) diagonal,
\[
4d_2^2
=
0.4187231561797235951297968\ldots.
\]

External Audit Round 102 independently re-derived the sign and reproduced these checks.

## 3. Consequence for historical odd certificates

The following older claims cannot be inherited without replay:

- v13.403's positive odd pole formula;
- v13.417's Loewner reduction using \(+2dd^T\);
- the downstream odd frozen-Schur/cross/residual certificate underlying v13.451;
- therefore the promoted odd index bound and the dependent full-parity index bound are on HOLD.

This does not prove those bounds false. It means the existing certificate is not source-faithful under the corrected odd pole sign.

The independently certified even-v lineage is unaffected.

## 4. Current Lane A work survives

The current direct form-core assembly integrates the actual pole screw term and already realizes
\[
2cc^T-2dd^T.
\]

Therefore the v13.795/v13.798 protected-resolvent diagnostics remain valid apart from the separate precision-figure correction recorded by v13.802 and the corrected v13.798 file.

## 5. Corrected fast-builder compatibility

Changing only
\[
+2dd^T\longrightarrow-2dd^T
\]
in the archived odd fast builder makes it agree with the current direct odd-v block through \(N=16\) to approximately
\[
\boxed{
8.7\times10^{-23}
}
\]
entrywise at the tested high precision.

The analogous even-v fast builder agrees to approximately
\[
8\times10^{-23}.
\]

Thus the closed-form/Feshbach infrastructure remains usable for larger cutoffs if the odd pole sign is corrected.

## 6. Corrected finite-high midpoint

On
\[
F=\{22,24,\ldots,4000\},
\]
the archived pole-free midpoint minimum was
\[
\lambda_{\min}(A_{FF}^{(0)})
\approx0.5328423837861.
\]

The old incorrectly positive-pole matrix gives
\[
\lambda_{\min}(A_{FF}^{\rm old})
\approx0.53374499902694.
\]

The corrected matrix
\[
A_{FF}^{\rm corr}
=
A_{FF}^{(0)}-2d_Fd_F^T
\]
gives
\[
\boxed{
\lambda_{\min}(A_{FF}^{\rm corr})
\approx0.53191549510157.
}
\]

The midpoint remains above \(0.53\), but the old Loewner shortcut is unavailable because
\[
2\|d_F\|_2^2
\approx0.0208331092258
\]
is much larger than the pole-free excess above \(0.53\).

A fresh source-faithful outward replay is therefore required before any historical odd/full-parity index theorem is restored.

## 7. Compatibility map

Reusable without change:

- direct form-core matrix assembly;
- analytic source overlaps;
- generic Feshbach/Schur algebra;
- generic residual-to-Schur error bounds;
- even-v fast formulas.

Reusable after correction:

- odd-v fast formulas with \(-2dd^T\).

Not reusable as current certificates:

- the old odd frozen theorem payload;
- the old odd normalized cross/residual replay;
- the v13.451 odd index promotion;
- the dependent v13.452/v13.453 full-parity promotion.

## Result

\[
\boxed{
A_{\rm pole}=2cc^T-2dd^T.
}
\]

\[
\boxed{
A_{\rm pole}^{(+)}=+2cc^T,
\qquad
A_{\rm pole}^{(-)}=-2dd^T.
}
\]

\[
\boxed{
\textbf{The old odd }+2dd^T\textbf{ certificate convention is corrected and remains on HOLD pending replay.}
}
