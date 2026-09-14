# Cone Derivation Ledger v13.461 — High-Precision Small-Cutoff Even Spectrum

Date: 2026-09-14

Status labels: **[N]** high-precision numerical; **[I]** interpretation; **[Audit]** guardrail.

## 0. Synchronization [Audit]

A live-head check immediately before this write found `v13.460` as the newest numbered ledger entry, so `v13.461` was free.

This checkpoint follows the terminal-structure diagnostics v13.455-v13.459.  It does **not** strengthen the already-certified index theorem

\[
\operatorname{ind}_{\le0}(A_{a=1})\le6.
\]

Its purpose is narrower: determine whether the four machine-zero even-v finite-cutoff levels are merely binary64 cancellation artifacts or remain genuinely tiny at high precision.

## 1. Reproducible high-precision generator [N]

New artifact:

`research-notes/suzuki_even_small_cutoff_highprecision_spectrum.py`.

It rebuilds the source-faithful even-v Suzuki matrix directly in `mpmath` using:

- the canonical archimedean source formula restored by v13.387;
- the five prime-power channels q=2,3,4,5,7;
- the cusp `Si/Ci` terms;
- the full even PSD cosh pole.

No binary64 finite solve or frozen Schur basis is used in this test.

## 2. Small-cutoff spectrum [N]

At 80-digit arithmetic, the first six eigenvalues behave as follows.

### M=19

\[
\lambda_1\approx1.12\times10^{-20},\qquad
\lambda_2\approx9.42\times10^{-16},
\]
\[
\lambda_3\approx1.12\times10^{-11},\qquad
\lambda_4\approx4.77\times10^{-8}.
\]

### M=29

\[
\lambda_1\approx3.44\times10^{-25},\qquad
\lambda_2\approx1.41\times10^{-19},
\]
\[
\lambda_3\approx1.16\times10^{-14},\qquad
\lambda_4\approx1.81\times10^{-10}.
\]

### M=39

\[
\boxed{
\lambda_1\approx4.7985\times10^{-28},
\quad
\lambda_2\approx6.1126\times10^{-22},
\quad
\lambda_3\approx1.3623\times10^{-16},
\quad
\lambda_4\approx6.6123\times10^{-12}.}
\]

The next two levels are already much larger:

\[
\lambda_5\approx1.1486896\times10^{-7},
\qquad
\lambda_6\approx3.5857477\times10^{-4}.
\]

### M=49,59,69

The first four remain positive and tiny.  At M=69:

\[
\boxed{
\lambda_1\approx8.64\times10^{-30},
\quad
\lambda_2\approx3.50\times10^{-23},
\quad
\lambda_3\approx1.92\times10^{-17},
\quad
\lambda_4\approx1.95\times10^{-12}.}
\]

## 3. Precision-doubling replay [N]

The M=39 matrix was independently rebuilt at 100 decimal digits.  The first four levels are

\[
\lambda_1=
4.7984991696361970803987493788\ldots\times10^{-28},
\]

\[
\lambda_2=
6.1125866437006221822239395407\ldots\times10^{-22},
\]

\[
\lambda_3=
1.3623399856768213576450807444\ldots\times10^{-16},
\]

\[
\lambda_4=
6.6122931589980514089975598522\ldots\times10^{-12}.
\]

These agree with the 80-digit run to far beyond the displayed precision.

Therefore the four tiny finite-cutoff levels are **not** ordinary binary64 sign/rounding noise.

## 4. Relation to ordinary-double diagnostics [I]

At large cutoffs the first four finite Schur/full-matrix eigenvalues appear at roughly `10^-12` or below in binary64 and may acquire tiny negative signs.

The high-precision ladder shows that such signs must not be interpreted spectrally.  At small cutoffs where the levels can be resolved robustly, all four are positive and separated by an enormous scale hierarchy.

Thus the correct current interpretation is

\[
\boxed{
\text{extremely small positive finite-cutoff levels, not demonstrated exact zeros.}
}
\]

This reinforces the long-standing guardrail against promoting the numerical near-zero pattern to exact kernel multiplicity.

## 5. What remains open [O]

The high-precision data do **not** determine the infinite-cutoff limit of these four levels.

Several possibilities remain logically open:

1. they converge to zero in the infinite operator;
2. they remain positive but become extremely small;
3. the observed hierarchy reflects compact/smoothing spectral decay rather than an algebraic kernel;
4. some arithmetic or local-symmetry structure controls the decay rates without producing exact annihilators.

The present computation distinguishes only finite-cutoff positivity from binary64 cancellation.

## 6. Relation to v13.460 [Audit/I]

v13.460 established a canonical four-state affine `S4` carrier on the prime-2 tangent Klein four, with an `S3` stabilizer acting on three nonzero states.

The Suzuki terminal diagnostics show a superficially similar pattern of three V4-aligned directions plus one exceptional direction.  This similarity is interesting but **not yet an identification**.

In particular, the new high-precision positivity data give no representation-theoretic map from the terminal four-plane to the tangent `S4` carrier.

## 7. Next target [O]

The highest-leverage next step is no longer to search immediately for exact annihilators.  Instead:

1. compute high-precision convergence of the first four levels versus cutoff over a longer ladder;
2. fit algebraic/exponential decay models only as diagnostics;
3. inspect the associated eigenvectors for stable arithmetic character content as the cutoff increases;
4. test whether the three V4-like directions and exceptional direction remain identifiable in high precision rather than only in the frozen M3999 complement.

Only after a stable limiting pattern appears should one attempt an exact algebraic explanation.

## 8. Guardrails [Audit]

- No exact kernel is claimed.
- Tiny negative binary64 eigenvalues are treated as rounding artifacts unless independently certified otherwise.
- No sign claim for the infinite unresolved directions follows.
- No stronger inertia theorem follows.
- No RH or GRH conclusion follows.

---

**Checkpoint conclusion.**  High-precision direct assembly resolves the four machine-zero even-v finite-cutoff levels into a reproducible positive hierarchy extending over many orders of magnitude.  The M=39 values survive an 80-to-100-digit precision replay essentially unchanged.  Therefore the finite-cutoff near-zero pattern is real but is not evidence of exact zero.  The next structural problem is to understand the cutoff dependence and arithmetic organization of these tiny positive levels.