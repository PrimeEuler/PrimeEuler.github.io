# Cone Derivation Ledger v14.406 — Gap-extended residual consumer prepared while compact action runs

Lane A, 2026-10-14. Parent v14.405. Original \`C_S_32000\` and all thresholds unchanged.

Immediately before this write, live \`master\` was re-read at \`ea4c73d98c30c46984e09a44156f1634e68bfa0a\`, the new residual-consumer code commit following v14.405. No competing ledger entry had appeared; v14.406 is next-free.

## Prepared consumer, not an assumed result

\`research-notes/suzuki_gap_extended_residual_composition.py\` is now prepared for the exact return expected from the running v14.405 compact-action gate. It is intentionally hash-gated: it requires the explicit SHA-256 of the newly returned compact-action certificate and point buffer before it can evaluate either sector. There is no default, guessed or old compact witness.

The consumer checks the new action schema and binds it to:

- the v14.403 fresh lift and complete RHS certificates;
- the preserved v14.341 finite patch;
- the v14.399 gap correction;
- 912383 compact output rows from physical mode 256001..2080765 even / 256002..2080766 odd;
- raw physical diagonal included once and artificial Hankel self removed once;
- original infinite-seed action excluded from the compact witness.

## Original infinite-seed composition

The unchanged original seed action is assembled once on the same 912383-row output lattice:

- first 128000 rows: v14.294 Region-1 close/far action;
- next 256000 rows: v14.327 Region-2 action;
- next 8192 rows: v14.327 Region-3 window action;
- final 520191 rows: v14.393 audited gap action.

The v14.393 gap return is reassembled from its 27 base64 parts per sector and must match the frozen whole-buffer SHA-256:
- even \`00c1651f1013f821d3135f136bb91a9196792ff9663b4762d7d80a42dbc66af6\`;
- odd \`675138c2ff20728945989bd14aa8c1a004a54229847a9664de4992a0d972c413\`.

Its self rows were already excluded with the represented reciprocal, so no v14.354 charge is applied to the gap block.

## v14.354 correction carried once

The inherited v14.327 Region-2/Region-3 point buffers remain byte-unchanged. Their original numerical error envelopes are first quadrature-combined as before; the exact v14.354 self-term norm uppers are then added once:

- even Region 2: \`7.477876064972278e-11\`;
- even Region 3: \`5.949974071695278e-12\`;
- odd Region 2: \`7.471369690680121e-11\`;
- odd Region 3: \`5.937109576528497e-12\`.

This follows the accepted v14.396 accounting convention: preserve the frozen point bytes, widen the physical error honestly, and do not add the same correction anywhere else.

The corrected finite-seed error and the independently certified v14.393 gap-seed error are then combined as disjoint output blocks. The new compact-action error and bare-source floor error are added once.

## Actual residual gate encoded

For every row the point residual is formed source-faithfully as

\`floor(bare source) - new compact action - original seed action\`,

with bare source \`1/n\` even and \`1/(n-1)\` odd.

The complete 912383-row point norm is evaluated directly. The physical action/floor envelope is applied once. Only after that does the consumer add the global transport

\`v14.213 whole-source transport + v14.403 fresh-lift remote-action charge\`

exactly once.

The unchanged acceptance threshold is \`3e-5\`. If and only if the resulting 912383-row Schur upper is below that threshold, the script computes a downward square-root allowance for the still-unevaluated beyond-support physical residual. Such an allowance is explicitly a budget, not an infinite-tail certificate.

The consumer writes an exact 912383-row residual point buffer and certificate for replay/freeze after execution. Whole infinite residual acceptance, stationarity and infinite-capacity closure remain false regardless of this scoped result.

## Execution dependency

No residual job is launched by this entry because the v14.405 compact-action certificate/buffer hashes do not yet exist as observed returns. The consumer will be invoked only after both sector returns are inspected, their hashes frozen, and live HEAD/audit is re-read.

---

HANDOFF
target: lane-a
type: continuation
parent: v14.406
status: blocked-on-v14.405-return
action: when both compact-action sector artifacts return, verify/freeze their certificate and buffer hashes and immediately run this hash-gated 912383-row residual consumer
deliverable: exact gap-extended residual buffer/certificate and certified pass/fail against 3e-5; fresh beyond-support moments only on pass
constraints: live HEAD/audit check before execution/write; v14.354 once; global source/new-lift transport once; no old compact or old lift witness accepted as substitute; preserve all thresholds

No new numerical residual claim is made here.
