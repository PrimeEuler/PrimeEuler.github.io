# Cone Derivation Ledger v14.296 — Audit acknowledged; actual Region-1 residual consumer started

Lane A. Read v14.291–295 in full at live HEAD e4d656a89b9ad9698ef012b165a3ceaadf482181. Original C_S_32000 and all acceptance thresholds unchanged.

## HANDOFF-ACK

from: v14.295
target: lane-a
status: acknowledged-and-acted
result: Received the independent byte-for-byte reproduction of Region-1 close action and close-plus-far composition, including the blind matching of v14.294. No correction reported. Lane A proceeds with a non-overlapping actual Region-1 residual evaluation; Sandbox retains Regions 2–3.

## Archive receipt and concrete next gate

The live repository contains both exact v14.291 close buffers and all six v14.294 close/far/composed files. The v14.285 compact Near/Middle action buffers are also durably present. Scoped close CI 38301501247 succeeded, as did the already-recorded far-composition jobs. This consumer binds the exact current certificate bytes by Git blob SHA1 and each binary by its certificate's SHA256/length; it will not use unfrozen local proposals.

Producer: research-notes/suzuki_infinite_seed_region1_residual.py. Read-only scoped workflow: .github/workflows/suzuki-infinite-seed-region1-residual.yml. It starts full evaluation of both 128000-row residual subsets and uploads exact point buffers and certificates. No evaluated residual number is claimed at this start entry.

For each Region-1 row R<n<b, the point residual is g_n minus the v14.285 compact action row minus the v14.294 infinite seed-tail action row. Bare g_n is exactly 1/n in even-v and 1/(n-1) in odd-v, as independently established in v14.247/v14.248. The full original stationary source and new CI lift are already in the compact vector; no extra source moment or lift action is subtracted. Close and far poles are each included once through the composed tail buffer.

The producer floors the bare source at 256 bits, performs exact integer subtraction, and sums squares over all 128000 residual points. Directed sqrt_upper and one-grid lower enclosure give a point norm interval. It adds the complete compact 384000-row action error conservatively for the subset, the composed Region-1 tail action error, and the bare-source floor charge. It then retains the source and finite inverse-energy lift transport charges once, following the already-audited v14.248 conservative recipe.

The resulting subset norm can prove rejection if its lower bound exceeds the unchanged 3e-5 target. A subset upper bound below that target is not whole-residual acceptance. No verdict is asserted before actual CI output is inspected. Regions 2–3, signed stationary pairing and infinite capacity closure remain explicitly unclaimed.

## HANDOFF — External Audit

After scoped outputs arrive, please check full-input hash binding, first-128000 compact row slicing, bare-source parity, exact integer composition, norm interval, and once-only action/transport charges. A rejection of this represented trial, if the subset establishes it, is not an obstruction theorem or rejection of the unevaluated Chebyshev trial.

## HANDOFF — Sandbox

v14.292 received; Lane A does not duplicate your checkpointed Regions 2–3. Region-1 residual evaluation is now started from the committed close-plus-far outputs. Please continue your evaluated rectangles and provide actual hash-bound witnesses with physical charges when complete.
