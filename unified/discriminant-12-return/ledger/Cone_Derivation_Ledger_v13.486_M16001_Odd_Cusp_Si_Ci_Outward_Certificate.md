# Cone Derivation Ledger v13.486 — M16001 Odd Cusp Si/Ci Outward Certificate

Date: 2026-09-16

Status: **[N-cert]** exact-rational source enclosure; **[Audit]** no theorem promotion by this entry alone.

## Synchronization

The live ledger was checked immediately before this write. Two parallel threads have both used `v13.485`; this entry therefore takes `v13.486` and records the collision rather than overwriting either file.

## Certified range and formulas

For the M16001 even-sector finite-high band

\[
n=21,23,\ldots,16001,
\]

set `x=n*pi`. Since `n` is odd,

\[
\operatorname{Si}(x)=\pi/2+F(x),\qquad \operatorname{Ci}(x)=G(x),
\]

with the standard Laplace auxiliary functions. The new helper

`research-notes/suzuki_odd_cusp_rational_certificate_M16001.py`

uses exact `Fraction` arithmetic, Machin rational intervals for pi, range-reduced atanh intervals for `log(n/4)`, and 12-term inverse-power expansions for F and G with first-omitted Laplace-moment remainders. No SciPy/mpmath special function enters the certificate.

The worst asymptotic widths occur at the first finite-high mode `n=21`; the logarithmic width remains negligible throughout the full range.

## Outward bounds

The exact-rational replay gives the following safe rounded enclosures:

\[
\boxed{\operatorname{width}(\operatorname{Si}(n\pi))<5\times10^{-22}},
\]

\[
\boxed{\operatorname{width}(\operatorname{Ci}(n\pi))<2\times10^{-22}},
\]

and for

\[
c_n=\log(n/4)-\operatorname{Ci}(n\pi)-\frac{\operatorname{Si}(n\pi)}{n\pi},
\]

\[
\boxed{\operatorname{width}(c_n)<2\times10^{-22}}.
\]

More specifically at `n=21`, independently replayed exact-rational widths are approximately

- `Si`: `4.06918e-22`,
- `Ci`: `1.54197e-22`,
- cusp diagonal: `1.60365e-22`.

Hence the cusp source-sequence radius is below `2.5e-22`, and the cusp diagonal radius is below `1e-22`.

Even the deliberately crude finite-high conversion

\[
\|E_{\rm cusp}\|_2\le 7991\,(2\epsilon_{\rm entry})
\]

gives

\[
\boxed{\|E_{\rm cusp}\|_2<4\times10^{-18}},
\]

with the replayed value about `3.252e-18`.

This is five orders of magnitude below the existing global exact-vs-high-precision-nominal source budget `2e-13` from v13.357.

## Consequence

The odd-mode cusp `Si/Ci` reconstruction is no longer an executable source-generation obstruction for the M16001 replay. Together with v13.484, both the prime and cusp finite-high source channels now have exact-rational outward enclosures at the required range.

The remaining source-generation gate is the degree-64 archimedean nominal reconstruction through mode 16001 and its wiring into the shifted structured replay. This entry does **not** by itself promote the even-sector index bound.
