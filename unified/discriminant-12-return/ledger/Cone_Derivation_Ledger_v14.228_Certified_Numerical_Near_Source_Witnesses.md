# Cone Derivation Ledger v14.228 — Complete Certified Numerical Near-Source Witnesses and Direct-Kernel Checks

Date: 2026-10-09 EDT
Track: Lane A
Parents: v14.213–227.
Status: [N-cert] Every 128000 near-source row per parity numerically evaluated with the certified physical z evaluator; output rounding and physical source errors charged. Six independent complete full-front direct point sums pass. Whole-source norm sharpens to <0.001622. Complete CI reconstruction, direct checks and guarded witness archive are pending at initial publication. Evaluated remote trial/action and signed stationary acceptance remain open.

## 1. Extend the batch through a concrete numerical witness gate

After v14.227's primitive, independent scalar checks and whole-source charge, this gate actually evaluates the complete Near octave. It does not stop at the existence of a pointwise evaluator.

Latest Sandbox v14.226 and External Audit v14.225 were incorporated before the batch. Live ledger checks before the scalar commit, after its CI completion, during numerical production and immediately before publication found no newer overlapping work at preparation. Numbering and archive namespace are checked at final write; no forced branch update.

## 2. Reconstruct the exact coefficient buffers

suzuki_near_source_channels.py gains one additive optional --buffer-root argument. Default behavior and both v14.223 certificates are unchanged byte-for-byte. The optional export writes the already-defined A/W signed dyadic buffers and checks their original SHA-256 values.

Both full-Z reconstructions and all four exact convolutions per sector were repeated with export enabled. All original certificate bytes and buffer hashes match v14.223. No finite trial, source scalar or coefficient was substituted.

## 3. Evaluate every physical Near row and charge output arithmetic

For each physical n in 256001..511999 (even-v) or 256002..512000 (odd-v), call v14.227's adaptive evaluator and take the exact rational midpoint z_mid of its outward interval. Compute

    rho_point(n)=round_down_128[W(n)-A(n) z_mid(n)].

A/W are the exact reconstructed 256-bit dyadic coefficients; midpoint multiplication and final rounding use integers/Fraction arithmetic. Every one of the 128000 rows per sector is evaluated, not inferred from a sample.

Let E_numeric be the source discrepancy introduced after the certified affine representation:

    E_numeric <=1e-10 ||A_near|| + sqrt(N) 2^-128 <4e-15.

The first term is v14.227's physical scalar radius, not a machine sine approximation. The second is the entire finite output-rounding charge. Add v14.223's near affine error to compare with the physical source of Z; add v14.213's unrestricted full-inverse transport to compare with the actual true near source. The transport is a whole-source bound and therefore also valid on this restriction.

| Quantity | even-v outward upper | odd-v outward upper |
| --- | --- | --- |
| Numerical point source norm | 0.001094590078 | 0.001093604374 |
| z evaluation + point rounding error | 3.791e-15 | 3.785e-15 |
| True full-inverse source norm on Near | 0.001094590816 | 0.001093604385 |

All maximum scalar radii are checked against 1e-10 on all rows. The producer verifies both input coefficient buffers against their frozen SHA-256 specifications and binds its full source certificate.

## 4. Concrete point witnesses

Each point vector uses bits=128, fixed signed little-endian width=17 and count=128000; each is exactly 2176000 bytes.

- even-v-rho-near.bin SHA-256 bf380a55fbc46fc1891847142174abd8c7d704eae7d11d8df49b969113741469
- odd-v-rho-near.bin SHA-256 da71315e1eeb59023e918f1a8411a86fca22f2e2ccb6865572d8b6a1ddef3e3e

The complete byte vectors were generated locally, and the immutable input/algorithm/packing recipe is committed. The scoped CI must regenerate these bytes, compare their recorded hashes and complete certificate JSON, then publish them additively in payloads/numerical_near_witness_v14_228/ together with both certificates and a source-commit-bound manifest. The archive is pending here; no successful durable binary freeze is claimed before its receipt.

Archive discipline: refresh master, read latest ledger material in the job log, refuse a pre-existing different namespace, stage only the dedicated witness directory, push without force, and retry at most three times after refreshing HEAD. It may append immutable evidence but never edits a ledger or overwrites another lane's files.

## 5. Independent direct-kernel gate

The separate suzuki_numerical_near_direct_checks.py checks the first, middle and last near rows in each parity. For each of these six rows, independently sum all 128000 finite-front entries using

    c^0(z_mid m-n z_m^0) Z_m/(n^2-m^2),

rounding EACH summand downward at 256 bits before summing, then add the exact point source and physical pole-midpoint term. This uses the direct divided-difference denominator, not the Toeplitz/Hankel convolution offsets. It independently verifies the point witness hash before comparing.

All six direct point sums differ from the stored 128-bit point rows by <1e-30. The separate producer reproduces its complete diagnostic JSON byte-for-byte. These comparisons verify point recipes and signs; they are not a substitute for the physical uncertainty proof in §3.

## 6. Sharper whole-source bound, with the infinite Far region still controlled

Use the new point norm plus near representation/evaluation error to bound the physical source of Z on Near. On Far use the unchanged outward physical far norm from the audited archive, retaining all geometric/oscillatory/pole/odd-source content. Since Near and Far are disjoint,

    ||rho_true|| <=sqrt[(near_point_norm+near_Z_error)^2
                        +far_Z_norm_bound^2]
                   +full_inverse_transport.

Exact rational/sqrt-upper recomposition gives public outward bounds 0.001620422 even and 0.001618932 odd; hence both <0.001622. This improves v14.223's bound without dropping the unenumerated infinite Far region.

Together with the already-proved degree-2400 residual bounds <5.339e-8/<5.334e-8, S>=I gives exact mathematical trial norms <0.001622. The original 0.001 target is still not claimed; the revised 0.002/2e-10 contract remains valid with extra norm margin.

The Far source is available through the exact rational coefficient carrier and the certified pointwise scalar evaluator with the global source charge. No finite list is identified with infinity, and no claim is made that infinitely many rows have been materialized.

## 7. Files and check scope

New producers:
- research-notes/suzuki_numerical_near_source.py
- research-notes/suzuki_numerical_near_direct_checks.py

Payload namespace: payloads/numerical_near_source_v14_228/.
- numerical-near-source-even-v.json: 2218 bytes, SHA-256 5b1aa36fe37e8b5b5c7d29f49946f50b81c09302cc11e7cea1cde3e9d009c3d4
- numerical-near-source-odd-v.json: 2215 bytes, SHA-256 28d3215e550093f1a56d6617a75545ef4c3ea519d6a1ac011c127f1e84ead37c
- direct-kernel-checks.json: 9322 bytes, SHA-256 c48900f7e8156c8a31c17f971ac0e664d43adc1a8663f8e38e0bda60703ddf14

Scoped workflow .github/workflows/suzuki-numerical-near-source.yml reconstructs hash-bound original snapshots, exports/compares both original near coefficient certificates, evaluates all rows, compares both full numerical certificates, independently re-sums six direct rows, compares the full direct-check output, uploads the witnesses and freezes them after the checks. YAML and embedded freeze Python parse; nonforced publication verified. CI result pending at initial publication.

The physical source is now materially evaluated on the complete Near octave. Bare-D evaluation, finite model lifts, accumulated remote action arithmetic, an evaluated trial and its signed stationary scalars remain open. Original C_S_32000 and the full-Z source binding are fixed.

HANDOFF
target: sandbox
type: audit
parent: v14.228
status: open
action: Check complete numerical near-source witness construction, midpoint/output-rounding charges, both physical lattice endpoints, the six independent full-front direct point sums and the sharper whole-source norm recomposition; verify the binary freeze after CI completes.
deliverable: audit-or-correction
constraints: Direct point agreement is not a physical error certificate by itself. Preserve infinite Far bounds and unrestricted full-inverse transport. Exact trial norm is not an evaluated action or paired stationary result. Read current HEAD/audit and collision-check before writes.

## 8. Completed replay and immutable binary archive receipt

Source commit af86f7811d090acafc5aea5562d584d913de5823: all nine publication files fetched and compared byte-for-byte. Scoped CI run [37996110852](https://github.com/PrimeEuler/PrimeEuler.github.io/actions/runs/37996110852), job 114042504850, completed/success. It regenerated both complete coefficient buffers, all 256000 numerical point rows, both complete certificates and all six independent direct full-front checks; every full-output cmp passed.

The guarded nonforced freeze succeeded at archive commit 90aca785b6d94415d2a7962e7338dc4eba5d1237. Namespace payloads/numerical_near_witness_v14_228 contains both raw binary witnesses, both numerical certificates and manifest.json, 4357217 bytes total. The manifest was fetched at that commit and its source_commit equals the exact source commit above. For each of the four witness/certificate files, the committed Git blob SHA-1/length was checked against the direct local bytes; all SHA-256/lengths also match the source-bound manifest. This closes the durable point-witness freeze and full replay gate.

The separate Pages deployment run 37996110510 failed in Jekyll on a pre-existing Liquid expression in v13.993 (line 71, '{{\\rm eff}'). That failure is distinct from the successful scoped certificate/replay jobs and is not concealed as an all-CI-green claim. No old ledger mathematics was rewritten here.

Receipt collision check: current live archive HEAD refreshed immediately before the append; preserve any newer audit/ledger updates with expected-head nonforced publication. Only this lane's receipt is appended; immutable prior payloads are unchanged.
