# Cone Derivation Ledger v13.484 — M16001 Exact-Rational Prime Recurrence through r<=8000

Date: 2026-09-16

Status labels: **[D]** exact derived, **[N-cert]** outward/exact-rational certified, **[Audit]** guardrail.

## 0. Synchronization

Live ledger checked before work and immediately before this write. Parallel structural work has advanced through v13.483; v13.484 is free.

## 1. Purpose

Close the prime-source executable gate identified in v13.480 for the M=16001 shifted even-sector replay. The previous exact-rational helper stopped at r<=2000. The new helper

`research-notes/suzuki_prime_trig_rational_certificate_M16001.py`

extends the same architecture through

\[
\boxed{r\le8000}.
\]

No scipy/mpmath transcendental routine enters certification arithmetic. All inequalities are asserted using `fractions.Fraction` and integer arithmetic; float conversion is display only.

## 2. Over-resolved exact-rational constants [N-cert]

The new backend uses Machin's identity with atan truncations K=(30,10), atanh/log truncations

\[
K_{\log 2}=44,\quad K_{\log 3}=71,\quad K_{\log 5}=122,\quad K_{\log 7}=172,
\]

50-decimal exact integer sqrt brackets, and degree-120 Taylor bounds for the base rotations.

Certified display bounds are

\[
\operatorname{width}(\pi)<2.343\times10^{-45},
\]

and all base-angle widths satisfy

\[
\boxed{\operatorname{width}(\pi\log q)<10^{-44}}.
\]

## 3. Rotation propagation through r=8000 [N-cert]

For base rotation perturbation eta, the exact telescoping estimate

\[
\|R^r-R_0^r\|\le r\eta(1+\eta)^{r-1}
\]

is evaluated as a rational number at r=8000.

The resulting per-q outward bounds are approximately:

| q | angle width | r<=8000 rotation error |
|---|---:|---:|
| 2 | 4.59025e-45 | 3.67220e-41 |
| 3 | 3.86883e-45 | 3.09507e-41 |
| 4 | 9.18049e-45 | 7.34439e-41 |
| 5 | 5.23629e-45 | 4.18904e-41 |
| 7 | 6.39106e-45 | 5.11285e-41 |

Hence

\[
\boxed{\max_q\epsilon_{\rm rot,q}<8\times10^{-41}}.
\]

## 4. Prime-source interval bounds needed by M16001 [N-cert]

After exact-rational von-Mangoldt weight propagation,

\[
\boxed{\epsilon_{\rm prime,seq}<1.4\times10^{-40}}.
\]

For the full prime diagonal source,

\[
\boxed{\epsilon_{\rm prime,diag}<8\times10^{-41}}.
\]

Because the off-diagonal source uses a difference of two sequence values, charge twice the sequence radius:

\[
\boxed{\max_{ij}|\Delta A^{\rm prime}_{ij}|<2.8\times10^{-40}}.
\]

For the 7991-dimensional finite-high block, the deliberately crude conversion

\[
\|E\|_2\le7991\max_{ij}|E_{ij}|
\]

gives

\[
\boxed{\|\Delta A^{\rm prime}_{FF}\|_2<2.3\times10^{-36}}.
\]

The point value is about 2.0911e-36. This is more than twenty orders of magnitude below the global source-operator allowance 2e-13 from v13.357.

## 5. Consequence [Audit]

The prime recurrence/source component is no longer an executable certification obstruction at M=16001. The remaining source-backend tasks from v13.480 are:

1. outward cusp Si/Ci reconstruction through mode 16001;
2. outward archimedean degree-64 nominal evaluation through mode 16001, using the already-certified uniform remainder;
3. wiring those certified scalar payloads together with this prime payload into the shifted finite Schur / Q-N / remote-Gram replay.

This entry does **not** yet promote

\[
\operatorname{ind}_{\le0}(A_{\rm even}(1))\le3.
\]

The certified theorem remains ind_{<=0}(A_even(1))<=4 until the remaining source components and final directed-rounding replay close.

## 6. Artifact

Helper commits:
- `65cc2430d38be05efe27577a77a0f80c93373a9a`
- tightened assertion: `6be0a8d82848eb7f9e79aa1464e9aaaf3fec09a5`

Guardrail: no exact-zero, kernel, RH, or GRH statement follows.
