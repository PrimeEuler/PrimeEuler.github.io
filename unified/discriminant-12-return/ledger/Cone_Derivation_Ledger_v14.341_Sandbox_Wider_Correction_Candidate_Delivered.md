# Cone Derivation Ledger v14.341 — Sandbox wider correction candidate delivered (v14.339 handoff closed)

Sandbox track (our Lane B). The evaluated wider finite correction
candidate requested by v14.339 is constructed and its frozen bytes are
in the repository at

    research-notes/payloads/sandbox_wider_correction_v14_339/

(20 files: each buffer as base64 parts of at most 800,000 bytes, both
certificates and the as-run producer as plain files, and manifest.json;
every file pushed with per-file fetch-back byte verification, and the
complete namespace then downloaded fresh and reassembled — see below.)

## Construction (exactly the v14.339 definition)

For each stored physical output mode n of the v14.337 composition,

    delta_y(n) = floor_160(r_point(n) / midpoint(log_normalized(n, 128))),

on the 256,000 Middle rows plus the 8,192 Far-window rows (264,192
rows per sector; first modes 512001/512002, final modes
1040383/1040384, same-parity step 2 — a single uniform lattice, the
Far window continuing the Middle lattice). Zero outside the support.
The patch is added to the existing trial; on this support the refined
Near trial coincides with the original infinite seed (the Near support
is disjoint and below b), and nothing outside the support changes.

Conventions mirror Lane A's own Near-trial producer
(suzuki_near_trial_lift_rhs.py) exactly: floor(q, bits) =
q.numerator·2^bits // q.denominator; midpoint(log_normalized(n, 128))
= (lo+hi)/2 with log_normalized from
suzuki_certified_remote_diagonal.py (byte-identical to the repository
copy, SHA256 08226538dffb5db42d85db5edb0f1c043a56df326ed1f51dc7391
ca7cf8a2788); buffers signed little-endian with width
(max_bit_length + 8)//8; norms via the same sqrt_upper outward
enclosure (192 bits).

Pinned inputs (all verified by SHA256 before use): the four v14.337
residual buffers and both v14.337 composition certificates, exactly
the durable witnesses of v14.337; v14.300's whole-trial norm bounds
from near-seed-refinement-{even,odd}-v.json (certificate SHA256
cca920b7b5f20fd856807166fdc08cce82f4b108f61831c34f19da29e366f42b /
85a45f5fa1e5bedc8100c69a3fd4c31324c10aa30bc635a1e61d9a24ac93c6ba).

## Delivered candidate [N-cert]

Buffers (dyadic integers at 160 fractional bits, width 18):

- even-v: 4,755,456 bytes, 264,192 values, SHA256
  fdf93112802fe28ef53efa804be760a0fc17abc404993c8b2af6c33b1b5aba05
- odd-v: 4,755,456 bytes, 264,192 values, SHA256
  b772ab850121daf0bd85afd01e26fee9f72d14b940c4145ae7643734435f8967

Exact norms (rationals in the certificates):

- Correction norm squared exact; outward norm upper
  6.583500641953496e-6 even-v / 6.5723094447733645e-6 odd-v.
- Correction ℓ¹: 0.0026870917831562087 / 0.0026822397434501074.
- Whole-trial norm upper by the triangle inequality with v14.300's
  current trial bound (1.5685523732266715e-4 / 1.5684173127301763e-4):
  **1.6343873796462063e-4 even-v / 1.63414040717791e-4 odd-v**.

Verification performed: all logpoints > 11; on 64 sampled rows per
sector (segment endpoints + seeded random rows) an independent
integer-only recomputation of floor_160 agrees exactly, and the
one-quantum bound 0 ≤ r_point − delta_y·logpoint < logpoint·2^-160
holds; the written buffers were re-parsed and their norm squares
recomputed identically; after the repository transfer, a fresh
download of the namespace reassembled both buffers to the certified
SHA256 values and the exact norm squares recomputed from the
reassembled bytes match the certificates.

## Domain justification and scope

delta_y is finitely supported with dyadic-rational values; finitely
supported sequences lie in the operator domain and in every weighted
ℓ² space of the framework, and the domain is a vector space containing
them, so the sum with the existing domain-admissible trial (v14.300)
remains domain-admissible; (D·delta_y)_n is a finite sum at every row.

Candidate construction only, as specified: no contraction claim, no
assertion that Λ⁻¹ equals the Schur inverse, no new residual
evaluated, no acceptance claim. Using the v14.337 point residuals to
choose a represented trial does not imply the points are the exact
physical residuals; Lane A's fresh RHS/lift/action certificates
decide whether the candidate works. Ownership split unchanged: Lane A
owns the new finite RHS, fresh lift, and changed compact
action/residual consumers; the wider compact support's geometric
split is theirs to recompute, as v14.339 notes.
