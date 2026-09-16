# Cone Derivation Ledger v13.493 — M16001 Archimedean Source Gate

Date: 2026-09-16

Status labels: **[D]** exact derived, **[N-cert]** certified numerical bound, **[Audit]** guardrail.

## 0. Synchronization [Audit]

Live head was checked before this write. v13.492 was the newest numbered ledger entry; the unnumbered archimedean helper commit `74e3ade6d40cc9d06c9eafd18cd69cdc93d348c7` landed afterward. Thus v13.493 was free at creation time.

## 1. M16001 archimedean extension [D/N-cert]

New helper:

`research-notes/suzuki_even_arch_symbolic_rational_certificate_M16001.py`

It extends the exact-rational degree-64 polynomial evaluation architecture to the odd Fourier modes

\[
n=21,23,\ldots,16001,
\]

using `b=n*pi/2`, `sin(2b)=0`, `cos(2b)=-1`, and exact Fraction arithmetic for the Bernoulli/Euler coefficients and the rational pi enclosure.

The analytic Taylor truncation is unchanged from the audited archimedean certificate:

\[
\|h-h_{32}\|_\infty<6.1\times10^{-14},
\qquad
\boxed{\|\Delta K_{\rm arch}\|_2\le1.22\times10^{-13}}.
\]

The rational polynomial-evaluation uncertainty decreases monotonically with mode and is maximized at n=21. It is deliberately over-resolved relative to the dimension-free analytic truncation; the executable helper asserts widths below `1e-38` for H32 and `1e-39` for D32. Therefore the archimedean source budget remains governed by the already-audited `1.22e-13` operator tail, not rational evaluation rounding.

## 2. Source-gate status [Audit]

For the M16001 replay the three source branches now have dedicated certified constructions:

- prime recurrence through r=8000: v13.484;
- odd-mode cusp Si/Ci through n=16001: v13.486;
- archimedean degree-64 rational evaluation through n=16001: this entry, with the audited dimension-free analytic operator tail `<=1.22e-13`.

Thus the prior source-generation provenance gate of v13.480 is removed at the construction level.

## 3. Remaining obligation [Audit]

This entry does **not** itself promote the even-sector index bound. The next step is the full outward seven-plane replay on the shifted nominal operator, combining:

1. shifted finite Schur block;
2. normalized Q/N cross block;
3. explicit remote residual Gram from 16003 through 2,000,000;
4. blockwise analytic far tail beyond 2,000,000;
5. outward arithmetic envelopes for the structured solve and Gram accumulation.

Until that replay has a strictly positive certified lower endpoint, the theorem remains

\[
\boxed{\operatorname{ind}_{\le0}(A_{\rm even}(1))\le4}.
\]
