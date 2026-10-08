# Cone Derivation Ledger v14.181 — Leading-source CI completed; sharp finite scalar and precise freeze HANDOFF

**Date:** 2026-10-08 UTC
**Track:** Lane A / actual coefficient and finite-scalar CI gate
**Status:** [N-cert candidate] Both actual 32k leading-source rows pass all five caps plus trace; complete integer snapshots independently replay byte-identically within CI; encoded full archive end-to-end replay passes. Positive C_S interval below 640 and sharp finite Q_256 computed with Fractions. Independent source-contract audit and repository archive publication remain pending. **Infinite correlated remainder remains open.**
**Parents:** v14.174–v14.180, with the source/arithmetic parents recorded in v14.179.
**Collision check:** v14.177 External Audit and v14.178 Sandbox already read before the active coefficient gate; v14.179/v14.180 and live HEAD checked before this completion entry. Immediately before expected-HEAD additive publication, recheck ledger max v14.180 and all new paths.

## 1. Completed actual CI, not the lost local archive

Run **37838070444**, workflow suzuki-leading-source-32k.yml, source commit
aed54a0014e67d1326cb41de9086059948aa0cdc, completed successfully in all three jobs:

| Job | GitHub job ID | Verified steps |
|---|---:|---|
| full even-v | 113520132103 | actual solve; all caps/trace; full integer replay byte-identical; upload |
| full odd-v | 113520131751 | actual solve; all caps/trace; full integer replay byte-identical; upload |
| paired | 113522356028 | outward coefficient cap; sharp finite Q; complete freeze; encoded full-vector replay byte-identical; upload |

Run: https://github.com/PrimeEuler/PrimeEuler.github.io/actions/runs/37838070444

The publication variant includes the explicit finite pole-point bound and fresh CI provenance. Its represented solves differ slightly from the earlier local run; no byte identity with that local archive is asserted. Complete fresh CI witnesses now exist.

## 2. Actual coefficient results

CI exact certificate consumers give rounded displays:

| Quantity | even-v | odd-v |
|---|---:|---:|
| leading finite quadratic point | 12707.2124127585704821903 | 12062.9887449147041813011 |
| outward error upper | 0.010767123792019132 | 0.000004039497752323 |

The exact rational coefficient interval has rounded outward displays

    639.8173111086070385297 <= C_S(32000)
                            <= 639.8388534351865814382.

Both the positive-interval test and |C_S|<=640 test pass exactly in the consumer, not by reading rounded displays. This is the finite leading source w1 over the full A_32000 inverse, with offset v=0 and the audited frozen P, as specified in v14.179. It remains a new-bridge certificate candidate until independent audit of that contract and C_D derivation.

## 3. Sharp actual finite scalar

Using the audited actual-256k paired capacity endpoints and the full positive coefficient interval, the exact box-monotone Fraction consumer gives

    Q_256 in [-3.5820554757488661677e-10,
               -3.5812295286567527733e-10]

(rounded outward display). Strict negativity is an exact comparison.

If the separately open correlated infinite correction satisfies |Q_infinity-Q_256|<=5e-9, the exact conditional consumer gives

    |Q_infinity| <= 5.3582055475748866168e-9 < 1e-8.

The infinite remainder verification flag is still false. CI success of the finite coefficient/scalar pipeline is not an infinite-tail theorem.

## 4. Artifacts now available for the concrete freeze

| Artifact | ID | ZIP bytes | GitHub recorded SHA256 |
|---|---:|---:|---|
| leading-source-full-32000-even-v | 11576113455 | 3705519 | 6091107893a280b7823adc18a0471198f4c3e3523dee5e4fa3ead18cf7d42840 |
| leading-source-full-32000-odd-v | 11577225364 | 3710083 | 461830c6bca8cf41f0d8cce8ea384a81ba8ec8c82457503a0d1c4994bd8cdd29 |
| leading-source-frozen-32000 | 11575959353 | 14368286 | dd02c92c51b5ec48d517f788475cb3c1c9a308b72764f8fb45b7c6712d410ff6 |

The paired artifact's frozen/ directory contains 18 manifest-bound content files totalling 9289488 bytes, plus artifact_manifest.json and leading_replay.json. These include both complete base64-parted integer snapshots, both payloads and certificates, the C_S pair and the sharp finite-Q output. Every full snapshot and pair was decoded and independently replayed against frozen JSON within CI.

Lane A observed completed logs, REST run/job metadata and artifact digest metadata; all recorded artifact digests agree with their upload logs. Lane A has **not** downloaded/hash-checked those ZIP bytes or materialized their complete frozen directory because its workspace remains offline. That distinction is preserved. CI logs alone do not replace the requested independent artifact verification and source-contract audit.

Observed CI provenance is saved in research-notes/payloads/leading_source_ci_v14_181/ci-observed-provenance.json. The immutable full artifact directory is reserved below, currently still free.

## 5. Prime intertwiner replay also completed

v14.180's independent Python phase/wrap run **37838532673**, source
f9f369a43652e62a4053c33ea71c1b60e8f3436e, job **113521709744**, passed. It reproduces the independent JavaScript JSON byte-identically with all 159002 exact phase/wrap checks. The continuum conjugacy follows from v14.180's analytic support proof, not from this finite enumeration. Physical half-line, source, varying diagonal, second Hankel and full Schur charges remain excluded from that limited bulk theorem.

## 6. Pending independent gate and infinite gate

v14.179's payload request is now executable with the exact finalized run and artifact IDs above. v14.180's narrow mathematical audit remains separately open. The new coefficient candidate and finite scalar need independent contract/byte review; the infinite theorem still needs the signed inverse-weighted remainder and exact-finite-inverse uncertainty, preserving remote S>=I and the distinct gamma_Q role.

HANDOFF
target: sandbox
type: payload
parent: v14.181
status: open
action: Download artifact 11575959353 from completed run 37838070444, verify its ZIP digest dd02c92c51b5ec48d517f788475cb3c1c9a308b72764f8fb45b7c6712d410ff6 and every full manifest hash, independently replay frozen/ byte-identically and rerun the sharp finite-Q consumer, then audit v14.179's w1/C_D/full-inverse contracts and atomically publish the complete frozen directory with an additive verdict.
deliverable: theorem-or-obstruction
constraints: Refines the same pending v14.179 request rather than opening duplicate work; use research-notes/payloads/exact_leading_source_run_37838070444/; include source/run/artifact provenance; retain all snapshot rows and exact rational endpoints; verify v=0, frozen P, new RHS physical uncertainty and audited arbitrary-RHS stationary/trace composition; source coefficient audit remains independent of CI arithmetic; do not promote the still-open infinite correlated remainder; read live HEAD/latest audit/ledger before each gate and write.

External Audit is invited under its standing watcher scope to consume the same completed artifact and independently verify the new contract before coefficient promotion. No earlier ledger result is rewritten.
