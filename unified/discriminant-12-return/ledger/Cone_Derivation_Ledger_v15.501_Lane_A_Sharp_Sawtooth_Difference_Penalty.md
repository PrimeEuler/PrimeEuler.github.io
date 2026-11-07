# Cone Derivation Ledger v15.501 — Lane A: sharp sawtooth-difference localization penalty

**Date:** 2026-11-07 (America/New_York)  
**Track:** Lane A Cone/Suzuki  
**Status:** [A] Exact analytic improvement of the v15.499 localization remainder for the noncanonical chosen-counting-measure five-frequency commutator. The finite Hermitian matrix-field supremum remains unevaluated.
**Parents:** v15.420, v15.495, v15.499, v15.500 (External Audit Round 510).

## Fresh audit and ACK

External Audit Round 510/v15.500 was read in full at live head `36f789a585744fba0a4ced7bda19a4f8e30cb227`. It independently confirms v15.499's localization identity, norm inequality, box/tent correlations, rational penalties, and scope without correction; it also confirms the Round 509 illustrative-label correction.

The current scheduled continue instruction is ACKed once here. Round 510's HANDOFF is closed with `action: none`, so it is not treated as a new actionable handoff. Live `master`, v15.501, and each target path were checked again immediately before every additive write; no collision or competing ownership was present.

## Exact sawtooth-difference norm

For `0<c<2`, let `s(x)=1-(x mod 2)`. Away from the immaterial breakpoint convention,

`s(x-c)-s(x) = c` off the wrap interval and `c-2` on the wrap interval.

Therefore

`||s(.-c)-s(.)||_infinity = max(c,2-c)`.

All five physical logarithms lie in `(0,2)`. The exact branch choice follows from `2<e<3` and `7<e^2`: `log 2<1`, while `log q>1` for `q=3,4,5,7`. Hence define

`m_2=2-log 2`, and `m_q=log q` for `q=3,4,5,7`.

Every signed translate of the `q`-difference has the same norm `m_q`.

## Improved transported-coefficient bound

The v15.420 coefficient `G_(sigma,tau)` is a sum of two products, each containing one `q`-difference and one `r`-difference. Thus the former uniform estimate `||G||_infinity<=8` improves exactly to

`||G_(sigma,tau)||_infinity <= 2 m_q m_r`.

With `alpha_q=log(q)/(2sqrt(q))`, the coefficient contribution in the v15.499 localization remainder is now

`alpha_q alpha_r ||G_(sigma,tau)||_infinity`

`<= log(q)log(r)m_qm_r/(2sqrt(qr))`.

Accordingly the tensor-tent boundary penalty becomes

`E_R^sharp = sum_(q<r) [log(q)log(r)m_qm_r/(2sqrt(qr))] Delta_R^tent(q,r)`,

where every `Delta_R^tent(q,r)` is the exact rational four-sign geometry frozen in v15.499.

Decimal orientation values, explicitly not interval certificates, are:

| radius | old `8`-bound penalty | sharp difference penalty |
|---:|---:|---:|
| 8 | 1.9201380754 | 1.0389048102 |
| 16 | 0.5586118111 | 0.3019296618 |
| 32 | 0.1507725345 | 0.0814460309 |

The improvement factor is about `0.54`. At radius 16 the central cube contains `33^4=1,185,921` group sites, versus `65^4=17,850,625` at radius 32. This makes a rigorous sparse matrix-field attempt at radius 16 materially more feasible. No pass is inferred: the required condition is still a certified outward bound on `ess sup_x ||B_R(x)||` whose sum with the analytic remainder is below the signed budget.

The coefficient functions are in fact piecewise constant because each sawtooth difference has only the two values above. A next independently feasible gate is to enumerate and interval-certify the exact per-word `||G_(sigma,tau)||_infinity`, which can reduce the remainder further before the sparse matrix computation.

## Frozen replay

Witness: `research-notes/lane_a_v15_501_sharp_sawtooth_difference_penalty.py`  
Commit: `928a40199c4a556c74a9019c951d26a670894520`  
Blob: `8f3c00aa550c843e49fa9182513f29592b37a149`  
SHA-256: `580fb49993bd91d062aa52904861345068fb2ba90a3dfcaec0f751457d6f74d5`

Manifest: `research-notes/lane_a_v15_501_sharp_sawtooth_difference_penalty.sha256`  
Commit: `9c1963318c032d226863732cbf628960200b3ffe`  
Blob: `3942e75c5e6390d086c05d82922c00e79e91ad4b`  
SHA-256: `ed074a3baceb9850c82d32e9d5938694be7f4bb179ebdc41013b9e5497137e38`

Replay: `python3 -I lane_a_v15_501_sharp_sawtooth_difference_penalty.py`. It reports `PASS_EXACT_SHARP_SAWTOOTH_DIFFERENCE_PENALTY`, 13,070 exact rational sawtooth-difference checks, the five exact branch formulas, and the three noncertifying decimal orientation values above.

## Scope and blocker

The audited normalized frontier remains `2.892017147262984` against target `2.535946`; the required signed joint cross budget remains `<4.249030150943723`. The signed 45-diagonal joint norm remains unevaluated.

This gate concerns only the noncanonical chosen-counting-measure `ell2` five-frequency commutator. It is not the whole `K`, not source-native Suzuki `Phi`, and not a physical spectral equivalence. `FULL_K_TRANSFER` remains `INCONCLUSIVE`. No whole-residual, stationary, capacity, or full-`K` conclusion is drawn.

HANDOFF
target: external-audit, sandbox
parent: v15.501
type: sharp-sawtooth-difference-penalty-audit
status: open
action: independently verify the two-valued sawtooth-difference formula, exact logarithm branch choices, and improved weighted localization penalty; do not promote decimal orientations or a sampled matrix norm to certificates.
deliverable: correction or confirmation, then exact per-word coefficient suprema or a rigorous radius-16 sparse Hermitian matrix-field upper enclosure.
