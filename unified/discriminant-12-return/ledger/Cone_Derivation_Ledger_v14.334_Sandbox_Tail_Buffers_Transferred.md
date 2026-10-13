# Cone Derivation Ledger v14.334 — Sandbox frozen tail buffers transferred to the repository (v14.328/v14.330 handoff closed)

Sandbox track (our Lane B). Byte transfer executed on Jeremy's explicit
approval (2026-10-13), closing the transfer half of the v14.328 and
v14.330 handoffs. The four v14.327 frozen buffers and their exact
directed-charge certificates are now in the additive repository payload
namespace

    research-notes/payloads/sandbox_tail_regions23_v14_327/

No bytes were regenerated or altered. The evaluator code is not part of
this transfer (not required by the handoff; its as-run SHA256 remains
recorded in v14.327/v14.331).

## Contents (35 files, each pushed with per-file fetch-back byte verification)

- The two 7,680,000-byte Region-2 buffers and the two 245,760-byte
  Region-3-window buffers, each stored as base64 parts of at most
  800,000 bytes following the repository's existing snapshot convention
  (`<name>.bin.b64.partNNN`, 13 + 13 + 1 + 1 = 28 parts).
- The four action certificates (`region2-action-{even,odd}-v.json`,
  `region3-action-{even,odd}-v.json`) and the two Region-3 envelope
  certificates (`envelope-{even,odd}-v.json`) as plain JSON.
- `manifest.json`: schema (signed little-endian 30-byte integers, 256
  fractional bits, same-parity row order), byte lengths, SHA256 values,
  part lists, and reassembly instructions (concatenate parts in numeric
  order, base64-decode).

## End-to-end verification [N-cert]

After the pushes, the complete namespace was downloaded fresh and every
buffer reassembled from the repository parts alone:

- even-v Region 2: 7,680,000 bytes, SHA256
  01049b9491c91ff49a640964cb878da6fdcacd08542eddc5d345944cb8edf390 ✓
- odd-v Region 2: 7,680,000 bytes, SHA256
  e0dfb52f4255d8f13a1f312b6ae772d6e57d077810d620e4e4bd44eab21621a9 ✓
- even-v Region 3 window: 245,760 bytes, SHA256
  4705c6a0cf10b35d3050ba21c4a347ebe0c7ba393734225112da7eeafec992d2 ✓
- odd-v Region 3 window: 245,760 bytes, SHA256
  29f39fd719d45690fb5240d0dc31e4c3241a482591a715501e04dbfbd1c1bfc7 ✓

All four hashes equal the v14.327 frozen values exactly, and all six
certificates are byte-identical to the sandbox originals. Combined with
v14.331 (the evaluator used exact rowwise geometric ratios; the false
"≤ 0.258" prose bound is corrected and no charge changed), the
v14.328/v14.330 requirements are fully satisfied: Lane A can now
hash-verify and perform the rowwise remaining-residual composition
(v14.309 compact Middle + these tail rows − bare g, against the
v14.310 budgets) in its own runtime.

Scope unchanged: no whole-residual, stationary-pairing, or
infinite-capacity claim is made here; the cancellation-aware ℓ² bound
on the beyond-window Region-3 residual remains the named open piece
(v14.327).
