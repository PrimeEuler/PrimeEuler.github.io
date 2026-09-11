# Cone Derivation Ledger v13.390 — Six-Positive-Direction Quadratic Tail Target

## Status

**New terminal reduction; diagnostic / target-setting checkpoint.**

This checkpoint follows the restoration of the source-faithful rank-two
Suzuki matrix after External Audit Round 20.  It deliberately does **not**
reinstate the earlier v13.365/v13.366 full-cross / full-Schur closure claims.

## 1. Why the old terminal target was unnecessarily strong

The previous terminal formulation aimed to solve all ten high-block equations

\[
A_{DD}X=A_{DC}
\]

with a uniform residual small enough to certify the entire \(10\times10\)
Schur complement entrywise.  Because the fifth finite-Schur eigenvalue is only
of order \(4\times10^{-8}\), that route drove the nominal full-operator solve
residual target down toward the \(10^{-11}\) scale.

The residual is not isotropic.  Numerical source-faithful finite-section tests
show that the remote-tail residual is dominated by one channel and becomes
increasingly low rank as the cutoff grows.  Therefore a uniform ten-column
bound throws away the geometry that protects the fifth direction.

## 2. Quadratic tail correction

Let

\[
C=\{1,3,\ldots,19\}
\]

be the ten-dimensional low core, and let

\[
F_M=\{21,23,\ldots,M\}
\]

be a finite high block.  Eliminating \(F_M\) gives a finite Schur complement
\(S_F\).  Let \(W\) denote the six-dimensional span of the finite-Schur
eigenvectors corresponding to eigenvalue indices \(5,\ldots,10\).

If the remaining effective tail satisfies

\[
T_{\rm eff}\succeq \delta I
\]

and \(R_W\) is the residual coupling from \(W\) into that tail, then

\[
S_\infty|_W
\succeq
S_F|_W-\delta^{-1}R_W^*R_W.
\]

Thus it is enough to prove

\[
\delta>
\lambda_{\max}\!\left(
S_W^{-1/2}R_W^*R_WS_W^{-1/2}
\right).
\]

Call the right-hand side \(\delta_{\rm crit}\).

This is the correct anisotropic terminal quantity.  It only penalizes a large
residual strongly when that residual lands in a Schur direction whose positive
margin is itself small.

## 3. Finite diagnostics

Using an equal-width next tail band solely as a floating-point diagnostic gives

| cutoff \(M\) | \(\delta_{\rm crit}\) |
|---:|---:|
| 199 | 0.4702 |
| 399 | 0.3978 |
| 799 | 0.2713 |
| 1199 | 0.2108 |

The same residual matrices become rapidly low rank.  The ratios
\(\sigma_2/\sigma_1\) are approximately

| cutoff \(M\) | \(\sigma_2/\sigma_1\) |
|---:|---:|
| 199 | \(5.0\times10^{-3}\) |
| 399 | \(2.1\times10^{-3}\) |
| 799 | \(9.1\times10^{-4}\) |
| 1199 | \(5.5\times10^{-4}\) |

At \(M=1199\),

\[
\sigma_4\approx8.5\times10^{-10},\qquad
\sigma_5\approx1.7\times10^{-11}.
\]

The dominant channel couples mainly into a large positive Schur direction,
not into the tiny fifth direction.  That is precisely the geometry hidden by a
uniform residual norm.

These numbers are midpoint diagnostics, not certificates.

## 4. Comparison with the old tail-coercivity target

The earlier architecture used the three targets

\[
A_{0,[21,16001]}\succeq0.22I,
\qquad
\|G\|<0.994,
\qquad
\alpha_{16003}>4.6732.
\]

If all three were independently revalidated, the corresponding effective-tail
lower bound would be

\[
\delta
>
4.6732-\frac{0.994^2}{0.22}
=
\boxed{0.1821272727\ldots}.
\]

This number is now used only as a **comparison target**.  The old v13.365
full-cross certificate was placed under audit, so v13.390 does not claim that
\(\delta>0.1821\) is presently certified.

The diagnostic sequence

\[
0.4702,\ 0.3978,\ 0.2713,\ 0.2108
\]

is nevertheless important: it is decreasing toward the scale required by the
source-faithful \(16001\) split, suggesting that the correct terminal proof is
not a \(10^{-11}\) uniform solve certificate but a six-dimensional residual-Gram
certificate.

## 5. Exact next target

The terminal task is now split cleanly into two independently auditable pieces:

1. **Revalidate tail coercivity** for the source-faithful split at 16001 without
   relying on any superseded v13.365 projection claim.
2. **Certify the six-dimensional residual Gram**
   \(R_W^*R_W\) for the full tail \(n\ge16003\), using the restored rank-two
   Cauchy generator and analytic remote-tail expansion.

If the resulting certified values satisfy

\[
\delta_{\rm certified}>
\delta_{{\rm crit},\,\rm certified},
\]

then the six candidate-positive Schur directions are globally positive.  The
remaining four tiny directions can then be isolated without ever asserting
that they are exact kernels.

## 6. New code checkpoint

Added:

`research-notes/suzuki_six_positive_direction_quadratic_tail_target.py`

The script records the finite diagnostic sequence, the low-rank residual
ratios, and the provisional comparison value

\[
4.6732-0.994^2/0.22=0.1821272727\ldots.
\]

It explicitly labels that last number provisional and refuses to reinterpret
it as a restored v13.365 certificate.

## 7. Guardrails

- No exact-zero statement.
- No claim that the first four numerical near-zero Schur directions are exact
  kernels.
- No final inertia theorem yet.
- No RH or GRH claim.
- v13.365/v13.366 remain non-authoritative until their relevant ingredients are
  separately revalidated.

## Conclusion

The terminal proof target has become materially smaller and better conditioned:
**certify one six-dimensional quadratic residual Gram against a positive tail
lower bound**, rather than certify ten independent infinite solves to a uniform
\(10^{-11}\) residual scale.
