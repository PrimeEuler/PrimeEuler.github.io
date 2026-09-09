# Cone Derivation Ledger v13.381

## Centered corrected-rank-4 long-double roundoff certificate

This checkpoint closes the **arithmetic** part of the renewed finite-high-block
certificate after External Audit Rounds 20-21.

The corrected displacement form is the sum of two skew generator pairs.  The
arch pair is used in the exact centered gauge of v13.377, so its fourth
generator is

\[
q_n^{\rm arch}=n\bigl(nH_n-c_\infty\bigr),
\qquad
c_\infty=\frac2\pi\frac{e^{-1}}{1-e^{-4}}.
\]

This changes no matrix entry and removes the large artificial `O(n)` generator
cancellation.

### Arithmetic model

The full 7991-step factorization was replayed in `numpy.longdouble` on a runtime
reporting a 63-bit stored mantissa and unit roundoff

\[
u=2^{-64}.
\]

At each step, the current stored state is regarded as exact input to the local
checker.  The exact Schur step represented by that state is compared with the
stored next state.  Therefore no interval state is propagated through all 7991
steps.

For column reconstruction, a deliberately conservative `gamma_12` absolute
error charge is used.  The multiplier division uses `gamma_3`, and the scalar
Schur/generator updates use `gamma_4`.  The resulting elementwise error bounds
are inserted into the exact corrected rank-4 local Frobenius-defect inequality
from v13.375.

### Transcript

The corrected centered replay gives

\[
\boxed{d_{\min}\approx0.2554790845853607}
\]

at mode `n=29`, together with

\[
\boxed{\|||L|\|_1\approx43.02616786684},
\]

\[
\boxed{\|||L|\|_\infty\approx3.72623077509},
\]

and streamed inverse majorant

\[
\boxed{y_{\max}\approx18.13687509296}.
\]

The accumulated local-defect budget is

\[
\boxed{
\sum_k\delta_k<8.86\times10^{-11}
}
\]

and hence

\[
\boxed{
\|E_{\rm arith}\|_2<1.43\times10^{-8}.
}
\]

From the crude but rigorous inverse-factor architecture

\[
\|L^{-1}\|_2\le \sqrt{7991}\,y_{\max},
\]

the corrected a-posteriori residual allowance is approximately

\[
\frac{d_{\min}}{7991\,y_{\max}^2}
\approx9.72\times10^{-8}.
\]

Thus the arithmetic residual is below the positivity threshold by almost a
factor of seven.

### Scalar/matrix uncertainty remains a separate line item

This checkpoint does **not** silently reuse the old v13.362 theorem.  The
roundoff budget is now repaired for the intended rank-4 matrix.  The final
finite-block certificate must additionally bind the exact target operator to
the nominal scalar state used by the factorization.

The previously developed high-precision prime/cusp scalar constructions remain
applicable.  The arch polynomial approximation error is controlled directly at
kernel/operator level,

\[
\|\Delta K_{\rm arch}\|<1.2181\times10^{-13},
\]

which does not depend on the superseded legacy off-diagonal formula.

The remaining finite-block task is therefore a provenance-clean replay using
the high-precision scalar provider and the rounded acceptance guards

- `min pivot > 0.2554`,
- `|||L|||_1 < 43.1`,
- `|||L|||_inf < 3.73`,
- `y_max < 18.14`,
- `sum local defects < 9e-11`,
- `arithmetic residual < 1.43e-8`.

Those guards have substantial margin relative to the total corrected allowance
`>9.7e-8`.

## Status

The arithmetic obstruction is closed.  The finite high block itself is not yet
re-promoted to theorem status until the scalar-provenance replay is run.  The
corrected cross is separately targeting `<0.995` from v13.379-380.  No
high-complement, exact-zero, RH, or GRH conclusion follows yet.
