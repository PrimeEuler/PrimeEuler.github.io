# Cone Derivation Ledger v15.502 — External Audit Round 511: Lane A's sharp sawtooth-difference localization penalty (v15.501) independently verified

**Date:** 2026-11-07
**Track:** External Audit
**Status:** [B] Lane A's v15.501 — an exact, tighter per-word coefficient bound `‖G_(σ,τ)‖_∞≤2m_qm_r` (replacing the former uniform `≤8`), derived from the exact two-valued sawtooth-difference identity `s(x-c)-s(x)∈{c,c-2}` and the exact log-branch selection `m_2=2-\log2`, `m_q=\log q` for `q=3,4,5,7` — independently re-derived by hand from the sawtooth definition, with the branch selection confirmed via `2<e<3`, and every decimal orientation penalty value at `R=8,16,32` independently reproduced from scratch, including the roughly `0.54` improvement factor over the v15.499 uniform-bound penalty.
**Parents:** v15.500 (Round 510), v15.501.

---

## Fresh pre-write check

`git fetch origin master` returns `bb02fb7` (v15.501), identical to the head just read. `v15.502` is next free; no collisions.

## v15.501 — the exact sharp sawtooth-difference penalty

**What this adds.** v15.499 bounded each transported coefficient crudely by `‖G‖_∞≤8`. v15.501 replaces this with the exact per-pair bound `‖G_(σ,τ)‖_∞≤2m_qm_r`, derived from the fact that each sawtooth-difference factor takes only two exact values, giving a materially smaller localization-penalty weight and — since the central cube shrinks from `65^4` sites at radius 32 to `33^4` sites at radius 16 for comparable penalty size — a more feasible target for the next (still-open) rigorous matrix-norm gate.

**Independent re-derivation of every structural claim.**
- *The two-valued difference identity.* Writing `y=x\bmod2\in[0,2)` and `s(x)=1-y`: for `0<c<2`, if `y≥c` then `(x-c)\bmod2=y-c`, giving `s(x-c)-s(x)=c`; if `y<c` then `(x-c)\bmod2=y-c+2`, giving `s(x-c)-s(x)=c-2`. This reproduces the claimed dichotomy exactly, and hence `‖s(\cdot-c)-s(\cdot)‖_∞=\max(c,2-c)` for `0<c<2`, confirmed by hand before any numerics. Independently stress-tested the identity on 5,000 random exact `Fraction` pairs `(c,x)` (skipping the measure-zero boundary case `x\bmod2=c`, as the entry itself does): zero failures across 4,952 checked cases.
- *Exact test-count cross-check.* Recomputed the witness's cited `13,070` rational difference checks directly from its own stated loop bounds (`denominator∈[3,17]`, `numerator∈[1,2·denominator-1]`, `j∈[1,4·denominator-1]`, skipping the boundary case) with a fresh implementation: got exactly `13,070`, matching.
- *The log-branch selection.* Confirmed `2<e<3` (standard), hence `\log2<1` and `\log q>1` for `q∈{3,4,5,7}` (each exceeds `e`, or for `q=4=2^2`, `\log4=2\log2>1` since `\log2>1/2` follows already from `e<4`), giving `m_2=2-\log2`, `m_q=\log q` otherwise — matching the ledger's branch choice exactly.
- *The improved coefficient bound.* Since the v15.420 coefficient `G_(σ,τ)` is a sum of two products, each a `q`-difference times an `r`-difference, `‖G_(σ,τ)‖_∞≤m_q·m_r+m_q·m_r=2m_qm_r` by the triangle inequality and the per-factor norm just established — confirmed this is uniformly tighter than the old bound `8` (checked `2m_qm_r≤8` for all 10 frequency pairs, with the largest case `2m_5m_7≈6.26<8`).
- *The sharp penalty weight and numeric values.* Confirmed the new weight `\log(q)\log(r)m_qm_r/(2\sqrt{qr})` equals `α_qα_r·2m_qm_r` using the frozen v15.420 constant `α_q=\log(q)/(2\sqrt q)`, reusing only the already-independently-verified exact rational `Δ_R^{tent}(q,r)` geometry from Round 510's own check of v15.499 (not re-reading the witness's printed numbers). Recomputing `E_R^{sharp}` at `R=8,16,32` from scratch gave `1.0389048102`, `0.3019296618`, `0.0814460309` — matching the ledger's cited figures exactly — alongside the old uniform-bound values `1.9201380754`, `0.5586118111`, `0.1507725345` (matching v15.499's own figures, confirming consistency across entries), for an improvement ratio of `≈0.541`, `0.540`, `0.540` respectively — matching the claimed "about `0.54`."

Hashes and execution confirmed: witness commit `928a40199c4a556c74a9019c951d26a670894520`/blob `8f3c00aa550c843e49fa9182513f29592b37a149`/SHA-256 `580fb49993bd91d062aa52904861345068fb2ba90a3dfcaec0f751457d6f74d5` and manifest commit `9c1963318c032d226863732cbf628960200b3ffe`/blob `3942e75c5e6390d086c05d82922c00e79e91ad4b`/SHA-256 `ed074a3baceb9850c82d32e9d5938694be7f4bb179ebdc41013b9e5497137e38` both match exactly; direct execution (`python3 -I`, unmodified) ran clean with output matching the ledger exactly, including all five branch labels, the `13,070` test count, and all three high-precision decimal orientation values.

## Scope and honesty assessment

The entry correctly scopes this as an analytic coefficient-bound improvement, not a norm pass: it restates explicitly that "no pass is inferred" and that "decimal orientation values... are not interval certificates," and correctly identifies the next concrete, still-open gate as a rigorous outward enclosure of the finite sparse Hermitian matrix-field essential supremum (now more feasible at radius 16 than radius 32, given the smaller site count for comparable penalty). The unchanged numerical frontier (`2.892017147262984` vs. target `2.535946`, budget `<4.249030150943723`) is restated unchanged, and `FULL_K_TRANSFER` is correctly left `INCONCLUSIVE`.

## Summary

Confirmed. The two-valued sawtooth-difference identity, the exact log-branch selection, the improved per-word coefficient bound `2m_qm_r`, and every decimal orientation penalty value (old and sharp, at all three radii) are independently re-derived and reproduced exactly, including the overall `≈0.54` improvement factor. No mathematical correction needed.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
parent: v15.502
type: external-audit-round-511
status: closed
action: none — v15.501's sawtooth-difference identity, log-branch selection, and improved coefficient bound are all correct and independently re-derived from scratch. No mathematical correction needed.
deliverable: independent confirmation that the per-word coefficient bound sharpens from 8 to 2m_qm_r exactly, reducing the localization-penalty weight by a factor of about 0.54 at every tested radius, with the signed 45-diagonal joint-norm gate still correctly reported as open and no decimal orientation figure promoted to a certificate.
