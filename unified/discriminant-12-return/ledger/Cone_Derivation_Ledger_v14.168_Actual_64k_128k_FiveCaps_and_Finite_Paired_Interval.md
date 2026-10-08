# Cone Derivation Ledger v14.168 — Actual 64k/128k Five Outward Caps and Finite Paired Interval

**Date:** 2026-10-08
**Track:** Lane A / actual endpoint freeze and independent arithmetic replay
**Status:** [N-achieved] All five remaining numerical ceilings and the trace ceiling pass on all four actual endpoint witnesses; [V-replay] full source/vector snapshot replay reproduces every certificate and the paired composition byte-identically. Independent review of the new physical-source arithmetic bridge remains a separate gate; no infinite-tail or final Cone theorem is promoted.
**Parents:** v14.155–v14.165; latest audit entries read: v14.166 and v14.167 (both read in full).
**Collision check:** Immediately before this gate/publication, HEAD was `720d3e05addd1fce2c667ef70b72f132bea24e6e`; latest ledger/audit updates and overlapping namespaces were checked. This ledger/payload namespace was free. Publication uses an expected-HEAD lease without force.

## 1. Audit updates incorporated; the symmetry flag is resolved by the existing code

v14.166 independently replayed all smoke witnesses byte-identically. v14.167 independently re-derived the carry-free multiplication/recovery and checked scalar reconstruction slack, point-source error charges, projector identity and cap formulas. Its remaining symmetry flag is resolved by inspecting the already-published implementation: `ExactSource.__init__` constructs the Toeplitz sequence as `sign(k)*floor(2^256/(2*abs(k)))`, with zero at k=0. Therefore T0(-k)=-T0(k) exactly. This is signed-magnitude truncation toward zero, not mathematical floor toward negative infinity. H0 depends only on i+j and is exactly symmetric. Thus A0 is exactly symmetric; every completed certificate additionally asserts its seven-column point assembly is exactly symmetric. No source or kernel change is required. This clarification preserves the v14.167 mathematical review and resolves its implementation flag.

The numerical arithmetic bridge has now received the v14.166/v14.167 independent contributions. The remaining audit request is the complete actual-cutoff evidence and its paired composition. Historical CI JSONs retain their conservative pending-audit fields; this ledger records the subsequent reviews without modifying frozen output.

## 2. Completed actual endpoint evidence

Workflow run `37791856005`: https://github.com/PrimeEuler/PrimeEuler.github.io/actions/runs/37791856005
Source commit: `04387bb29df9f5825b98e35eba97f69487f4fc22`. The completed run executes both smoke jobs, four actual jobs and the paired consumer. The actual source remains zero through 32000, then 1/n even-v or 1/(n-1) odd-v. Frozen represented P and fixed T,v are unchanged. The exact point-assembled matrices are newly produced data; the old v14.153/v14.162 freezes and their paired scalar are not rewritten.

## 3. All five actual caps meet their targets

| Parity / cutoff | graph assembly | mixed assembly | scalar assembly | projected graph residual | projected source residual |
|---|---:|---:|---:|---:|---:|
| even-v / 64000 | 3.5913960930850544646030830621879323842381735843160E-7 | 1.0493269452273821741791641232238401729805121995356E-11 | 3.0659025332802594869897692045739841910330212473940E-16 | 6.1927560229796172276511246495670013088159654889742E-14 | 1.8080597649215485920186770486306263588317295948936E-18 |
| even-v / 128000 | 4.6557759572539692692962388319118599246384001944850E-7 | 1.3603153303794324184329597870243666666750299881819E-11 | 3.9745421924398739135688309651366739537011839028376E-16 | 1.0170062850148387485371235426822991947688173286153E-13 | 2.9703610953627135247588978254590426329976135075811E-18 |
| odd-v / 64000 | 1.4264616914350997513758969076263741658127600365932E-10 | 4.1375269287244950413623928244349858533950074618248E-15 | 1.2001113796962578955729822733725151988432105505595E-19 | 4.7435455621309889105234979680228042207369311821681E-15 | 1.3749638438227854714375731941832724805505103616730E-19 |
| odd-v / 128000 | 1.8492212707238369105306511141813009089469134759898E-10 | 5.3637632547232818465347979238327222655202466921621E-15 | 1.5557876554955658928811702142944931513666137602891E-19 | 1.4265802371414913201399529897453573112127072876627E-14 | 4.1341423125130197531953607168539405056599743279746E-19 |

The displays approximate the exact rational cap values in each certificate; threshold decisions use those rational values. The targets are respectively 1e-4, 1e-9, 1e-14, 1e-11 and 1e-15. Every row also meets rho<=1e-20, recomputed from the complete represented vectors and independently checked against the standalone trace witness during CI. v14.165 supplies the source-to-point uncertainty charge, exact convolution/action, decimal reconstruction slack, exact Euclidean projector, and serialization allowance. No midpoint residual is substituted for a cap.

## 4. Exact finite paired composition

The consumer applies the audited v14.155 full-Q floors (2.95e-19 even, 2.16e-17 odd), v14.156 affine trace correction and cap transport, and v14.157 blockwise capacity perturbation estimate. At every endpoint j>a is checked exactly. The newly recomputed point odd-minus-even capacity increment is

    -7.0867271616540485610080121008820608023446096948487E-10.

The four endpoint capacity error caps sum to

    6.5305944913130759233738152989491665261577067922525E-15.

The exact source interval is defined by the two Fraction strings in `source_interval_rational`, displayed approximately as

    [-7.0867924675989616917672458390350502940098712719166E-10, -7.0866618557091354302487783627290713106793481177808E-10].

Its exact absolute bound is displayed as 7.0867924675989616917672458390350502940098712719166E-10; the decision <=9e-10 is **true by rational comparison**. The interval's strictly-negative decision is `True`. This composition's applicability remains dependent on the independent review of the new v14.165 physical-source arithmetic bridge; the underlying endpoint numerical tests and all replay decisions have completed.

## 5. Durable replay and scope

Frozen namespace: `research-notes/payloads/exact_outward_run_37791856005/`. The manifest binds original JSONs, full ZIP bytes and base64 parts to the completed run and source commit. Each ZIP contains every trial-vector row, original high/low scalar component, dyadic scale, frozen P, mode list and normalizer. The replay validates all hashes, reruns integer source actions and exact projector/assembly calculations, and reproduces all four certificate files byte-identically. It also recomputes and byte-compares the exact paired output.

    python suzuki_frozen_outward_witness_replay.py --payload-root payloads/exact_outward_run_37791856005 --output /tmp/outward_replay.json --compare-reference

All five previously open numerical ceilings now have actual endpoint evidence. Their independent audit gate remains explicit. `overall_certificate_ready` stays false until that review. This is the finite 64k-to-128k octave; later octaves and the infinite tail remain outside this result.

HANDOFF
target: sandbox
type: audit
parent: v14.168
status: open
action: Independently decode and replay the four frozen actual full-vector witnesses and exact paired interval, confirming all five ceilings, source/operator/projector binding, and the new arithmetic bridge before numerical closure is promoted through the independent audit gate.
deliverable: theorem-or-obstruction
constraints: Coordinate with the v14.165 bridge audit; use the actual frontier 32000 and the newly computed point matrices; retain the audited full-Q floors and affine trace transport; preserve finite-octave scope and original frozen namespaces; read live HEAD and latest audit entries before gates/writes.

External Audit is invited to independently replay this complete actual evidence under the standing update-watch scope.

HANDOFF-ACK
from: v14.166
target: lane-a
status: closed
result: Incorporated the independent byte-identical smoke replay and retained its actual-cutoff and derivation-review limitations; all actual CI evidence is now frozen and independently replayed by Lane A.

HANDOFF-ACK
from: v14.167
target: lane-a
status: closed
result: Incorporated the independent arithmetic derivations; resolved the symmetry flag by the published sign-times-positive-floor construction, which enforces exact Toeplitz antisymmetry. No producer mutation or new solve was needed.
