# Cone Derivation Ledger v14.403 — Gap-correction complete RHS and fresh finite lifts certified, replayed and frozen

Lane A, 2026-10-14. Parents v14.398–402. Original C_S_32000 and every threshold unchanged. Local and actual scoped CI receipts are distinguished below.

## Completed complete-RHS gate

Both complete local v14.402 runs succeeded on the actual v14.399 correction bytes. They freshly evaluated all520191 correction-input z values, computed every128000 updated finite-front RHS coordinate and passed three full-input direct checks per sector.

Scoped CI run38607293592 independently succeeded, source dcb10d14ba3a54eacccbfe7a8c79b3eaefdae976. Both downloaded artifact ZIP digests match GitHub's declared frozen values; every complete RHS buffer, input-z cache and certificate byte equals local output.
- even artifact11917311498, ZIP14755839 bytes, SHA256 e62040be08299e40cf22203d8400e9eff109f820c2b1e3c63f0ade96aa4f9a96
- odd artifact11917077294, ZIP14755793 bytes, SHA256 c2d4386a39267cbf00522a04c3bdd01f74b97a69b89ba30e2b0b59978693c6db

| Sector | New whole-trial norm upper | Complete physical RHS error upper |
| --- | ---: | ---: |
| even-v | 1.6828077719441745e-4 | 3.2131128292548455e-30 |
| odd-v | 1.682472020770804e-4 | 3.2100986315445134e-30 |

Both norms remain below0.002 and both RHS errors below4e-30, decided by exact rationals. The whole-trial cap margin is about11.9-fold; the roughly400-fold figure in candidate discussion pertains to the correction alone, not the whole trial.

RHS certificate SHA256:
- even: 42c71d7e017eadc08a6ebe20045f6d6e83bbe3523e17ba282903eccf08edc075
- odd: 1309bec0a4568684f3631a2d88a278ba711c8496960491e5a81428a8fb5b30b3

Complete RHS buffer SHA256:
- even: 2007a804cb269ea1c5018d5305e772930be018ba1236985c2f845ffbc98be21c
- odd: bd3077e6903e1c63d4a1f60b1e2916fc212105c03700469e6550c597065db109

The preserved old full RHS plus gap-only update includes all prior trial components once. The candidate's chosen point error is not a contraction certificate.

## Completed fresh-lift gate

New lifts were actually produced against those exact new RHS pins, not inherited from v14.345. ExactSource.action certifies all128000 finite residual coordinates, all six protected components, physical operator/RHS uncertainty and inverse-energy estimate. Both saved new dyadic witnesses were then loaded and exactly replayed; each complete serialized certificate matches its original bytes.

| Sector | Inverse-energy error upper | New lift remote-action charge upper |
| --- | ---: | ---: |
| even-v | 1.9963208986550784e-23 | 9.829645542689003e-11 |
| odd-v | 3.185382848347673e-30 | 3.926480992695971e-14 |

Both lift charges pass unchanged2e-10. Local produce/replay is complete; a separate CI replay of the frozen chunks/new lifts is launched by this publication and remains pending observation.

Lift certificate SHA256:
- even: 4d49b475c4a6b97de137258d7b53415b914aec8fa1a0fb52f8b6400ba214bfb3
- odd: f2f2a9e3c018902198a8a9b7df5e91bba42a81de4bd1334cffaa1e2fb0cf0daf

All complete buffer hashes, scales and lengths are in their exact certificates and the manifest. No new action/residual acceptance is claimed by these RHS/lift gates.

## Frozen accessible witnesses and transport safeguards

research-notes/payloads/gap_correction_rhs_and_lift_v14_403/ contains all four certificate files and76 raw chunks reconstructing six whole buffers: both complete RHS buffers, both freshly evaluated gap-z caches and both new finite lifts.

Every raw chunk is at most700000 bytes, keeping its encoded transport below the previously observed cap. All76 returned Git blob identities were checked against the exact local raw-chunk hash BEFORE tree publication. The manifest binds per-chunk SHA256/length/Git SHA1 and each complete buffer's SHA256/length. The scoped CI reconstructs every chunk and complete buffer independently before exact lift replay. Large unchecked transport is not reused.

## Next action preparation

research-notes/suzuki_compact_component_rectangle.py supports arbitrary global input offsets and separate dyadic scales. It passed486 independent original physical-kernel rows in both parities (outputs before/inside/after support, with same-reciprocal self removal), and234 additional exact mixed-scale split/recombination rows locally. This prepares chunked/component action evaluation without padding every remote patch to the high-bit front-lift scale. It is an interface/algebra result, not full action evaluation.

The next full compact input is:
- Front: original whole source Z_full minus this NEW lift;
- Near: preserved refined Near trial;
- first patch: v14.341 Middle/window correction;
- second patch: v14.399 gap correction.

Each component is included once. Evaluate the actual912383 remote rows through2080765/2080766 with raw diagonal and represented self removal; compose original infinite-seed actions v14.294/v14.327/v14.393, carrying v14.354 correction once. Old compact action buffers and far coefficients do not certify the changed lift/trial. Fresh support-aware far moments/splits are still required.

HANDOFF-ACK
from: v14.399, v14.400, v14.401, v14.402
target: lane-a
status: closed
result: Complete new RHS locally and in scoped CI agrees byte-for-byte; fresh lifts produced and exactly replayed; accessible exact witnesses frozen here

HANDOFF
target: external-audit
type: audit
parent: v14.403
status: open
action: Reconstruct the small-chunk new RHS/lift archive, independently replay both new finite lifts and review the complete-RHS update and component rectangle offsets/scales.
deliverable: Ledger verification or concrete correction
constraints: Source unchanged, prior components preserved once; local replay and RHS CI completed, new lift CI receipt pending; no changed whole-residual acceptance claimed

HANDOFF
target: lane-a
type: task
parent: v14.403
status: open
action: Consume the frozen-lift CI/audit receipts, implement and run the component/chunk-aware enlarged compact action, then evaluate the actual912383-row changed residual from the pinned original infinite-seed components.
deliverable: Actual new compact-action and residual certificates with accessible buffers, followed by beyond-support work if the finite gate passes
constraints: Do not reuse v14.345 lift or old compact output as proof; apply raw self-diagonal exclusion and v14.354 correction once; preserve C_S_32000 and every threshold; read live HEAD/audit before each gate and mutation; continue on returned results without waiting for Jeremy

Whole infinite residual acceptance, stationarity and capacity closure remain open. No assumption that finite extensions alone close the infinite tail is made.
