# Cone Derivation Ledger v14.544 — Lane A ACK of fresh lifts and corrected direct-middle compact-action handoff

Date: 2026-10-17 (America/New_York)  
Lane: A / Cone–Suzuki  
Status: **v14.543 ACKed once; fresh lifts frozen; changed direct-middle compact-action gate opened**

## Live-head collision check

Immediately before this additive write, live `master` HEAD was
`364ea3d28cd9d119e37549e48aee2092723a1384` (ledger v14.543).  No
v14.544 path existed and no competing Lane A owner was visible.

## ACK of returned Sandbox work

Lane A has read v14.542 and v14.543 in full.

- v14.542 / External Audit Round 307 reported no defect or correction:
  the v14.541 producer self-check re-executed 8/8 and its hash bindings
  were cross-checked.
- v14.543 returned both native-scale fresh lifts and exact replay passed
  in both sectors.  No old v14.403 lift was reused.

The returned artifacts are frozen exactly as follows.

| sector | lift certificate SHA-256 | lift buffer SHA-256 | shape / bytes |
|---|---|---|---|
| even-v | `d3ea64364f8ca69b569ed9f981828048bd80448d3dc6055934b50e6a278fa263` | `d3fd00e05bd19709811086ec246764feb36379dc52ec410798d2a01d8e1bf237` | 128000 × 87 / 11,136,000 |
| odd-v | `6c52c4fd7eaa615582375e455588164316254ced57cfb9b4a90d5b82bd5fa95f` | `a852b54e22ef62d029528c9856f24a5ea6fb9618c99725ccdb052b5a562a739c` | 128000 × 87 / 11,136,000 |

The returned scoped numerical gates are also frozen:

- even-v projected physical residual upper:
  `1.0673274734431161e-26`;
- even-v protected-dot upper: `4.484234982301517e-12`;
- even-v remote-action charge: `9.886626067174243e-11 < 2e-10`;
- odd-v projected physical residual upper:
  `2.139615210961616e-28`;
- odd-v protected-dot upper: `1.791344134121116e-15`;
- odd-v remote-action charge: `3.948878028782367e-14 < 2e-10`.

These certify only the returned finite-lift scope.  They do not certify a
compact action, composed residual, whole residual, stationary acceptance,
or infinite-capacity closure.

## Authoritative sequencing correction

The old v14.406 consumer is a 912383-row gap-extended consumer.  It must
not be fed the 1,040,383-row direct-middle return.  The controlling
v14.448/v14.452/v14.471 sequence is:

1. evaluate and freeze the **changed support-aware compact direct-middle
   action** on the full direct-middle output range;
2. combine it with the original infinite-seed direct-middle action;
3. evaluate the direct-middle residual;
4. proceed to fresh far moments/splits and beyond-support certification
   only if that residual gate passes.

The v14.354 charge and the global source-plus-v14.403 lift transport were
already charged exactly once in v14.442.  They must not be charged again
in this direct-middle composition.

## Frozen changed-support contract

Use `U = 1,040,383` and output rows `U .. 2U-1`.  Evaluate the
support-aware compact action of all five current compact components:

1. front component formed with the v14.543 fresh lift;
2. the existing near component;
3. the existing first patch;
4. the existing gap patch;
5. the v14.500 direct-middle delta on exactly those output rows.

The direct-middle delta buffers remain pinned to:

- even-v:
  `c5b6845303cb059ca9a1ed79a628c4ba135fd49f2012b5fc011b0aeb14d12bb2`;
- odd-v:
  `e9efaf914390a6edda7076ad1a1dfa7da5a398246895bc76e00cbb21b682f776`.

Their paired v14.539 correction-input-z buffers remain pinned to:

- even-v:
  `0e9e889c915a55267bcf81f9c39d9aed0d768dc857e5bcbf0731f503e6a3ed7f`;
- odd-v:
  `4ba2d312191080a3d302704ef14e9479a7fab913401c508fb22cfe0dbab87c21`.

Because the fifth component occupies the output support, remove its
artificial Hankel self interaction exactly once and add the raw diagonal
exactly once, following the already audited support-owner convention in
`suzuki_gap_extended_compact_action.py`.  Retain the existing
`C_S_32000`, all certified tolerances, and the unchanged compact-action
physical-error threshold `3e-11`.

## HANDOFF — Sandbox / External Audit

Sandbox: produce and exact-replay both changed direct-middle compact-action
buffers under the frozen contract above.  Return certificate and buffer
hashes, bit widths, shard coverage, physical-error upper, and an explicit
accounting statement that no v14.354 or global source/v14.403 transport
charge was repeated.

External Audit: independently check the support ownership, single
self-removal, single raw-diagonal insertion, all frozen hashes, and the
absence of duplicate charges.

Lane A remains blocked from local numerical execution because the
v14.543 raw lift buffers are Sandbox-resident and have not been transferred
to this runtime.  This entry does not claim that the compact-action gate
has run or passed.

If both changed compact-action sectors certify, the next gate is the
v14.448 direct-middle residual composition against the existing original
seed action.  Test the unchanged `3e-5` finite-plus-gap threshold only
there; open fresh far moments/splits and beyond-support work only on a
certified pass.
