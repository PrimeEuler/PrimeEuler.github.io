# Cone Derivation Ledger v13.521 — M16001 Primitive Displacement Entry Bounds

Date: 2026-09-16

Status: **[N] / [Audit]** primitive nominal-arithmetic transcript; no theorem promotion.

## 0. Synchronization

Live head checked at start and immediately before this numbered write. v13.520 is latest numbered entry; helper commit `1139a5e7...` is newer but unnumbered. v13.521 is free.

## 1. Formula and arithmetic propagation

For every off-diagonal displacement entry

\[
a_{mn}=-\frac{2}{\pi}\frac{nZ_m-mZ_n}{n^2-m^2},
\]

new helper

`research-notes/suzuki_M16001_displacement_primitive_outward_transcript.py`

(commit `1139a5e796c57984cb3da6a2abf80aaa5ecab39b`) propagates long-double `u=2^-64` roundoff through, separately:

1. products `n Z_m`, `m Z_n`;
2. numerator subtraction;
3. squares `n*n`, `m*m` and denominator subtraction (charged even though integer modes are exactly representable here);
4. quotient division, including numerator/denominator input radii;
5. nominal `2/pi` division charge;
6. final multiplication by `2/pi`.

The scan visits every ordered off-diagonal `A0_FF` entry and every `A0_FC` entry. Diagonal `A0_FF` entries are deliberately excluded because they come from the separate diagonal source payload.

## 2. Replay maxima

For `A0_FF` (7991 x 7991, ordered off-diagonal entries):

- max `|numerator|` = `1.6092302110693138e5`;
- max numerator arithmetic radius = `2.2439408064377951e-14`;
- max `|denominator|` = `2.56031560e8`;
- max denominator arithmetic radius = `5.5511151448098262e-11`;
- max `|quotient|` = `1.8022379215604576`;
- max quotient arithmetic radius = `1.4171314499758582e-15`;
- `|2/pi|` = `0.63661977236758137`;
- nominal `2/pi` division charge = `3.4511227012407951e-20`;
- resulting maximum primitive entry radius:

\[
\boxed{\rho_{FF}^{\rm disp}\le 9.022982959826541\times10^{-16}}.
\]

For `A0_FC` (7991 x 10 entries):

- max `|numerator|` = `9.6053916217033985e4`;
- max numerator arithmetic radius = `1.0414506711651075e-14`;
- max `|denominator|` = `2.56032000e8`;
- max denominator arithmetic radius = `2.7759084310699511e-11`;
- max `|quotient|` = `0.47867396036424180`;
- max quotient arithmetic radius = `7.096315233660021e-19`;
- same `2/pi` value and charge;
- resulting maximum primitive entry radius:

\[
\boxed{\rho_{FC}^{\rm disp}\le 4.848047102922417\times10^{-19}}.
\]

These are maxima over the actual entrywise propagated radii, not a post-hoc observed double/long-double discrepancy.

## 3. Scope / fail-closed remainder

These radii are conditional on the stored nominal `Z` and `pi` payload values. Source-function uncertainty remains covered separately by the global shifted-nominal source bound and is not double-counted here. Still open from v13.520: diagonal-payload representation/provenance, `Z/c/pi` nominal payload conversion radii if required separately from the source certificate interface, `X` payload provenance, the `2 c_F c_C^T` outer-product formation, and the final 79910-term Frobenius sum/square-root outward endpoint.

Certified inertia therefore remains

\[
\boxed{\operatorname{ind}_{\le0}(A_{\rm even}(1))\le4},\qquad
\boxed{\operatorname{ind}_{\le0}(A_{a=1})\le6}.
\]
