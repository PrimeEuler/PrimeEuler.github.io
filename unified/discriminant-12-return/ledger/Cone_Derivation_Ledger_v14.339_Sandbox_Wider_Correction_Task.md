# Cone Derivation Ledger v14.339 — Sandbox wider-correction task; Lane A owns RHS/lift/action

Lane A. Read Sandbox v14.338 in full at HEAD 6481369e83d147705497a50afcff45137fceb115. HANDOFF-ACK: received its independent byte-for-byte confirmation of the v14.337 residual rejection; no correction. Jeremy asked for useful Sandbox work. Original C_S_32000 and all acceptance thresholds unchanged.

## HANDOFF — Sandbox: evaluated wider finite correction candidate

status: open
source: v14.337 frozen residual points
task: build and return an actual candidate correction over the Middle plus the evaluated Far window, in both sectors.

Use the exact durable Middle and Far-window residual buffers under research-notes/payloads/returned_tail_residual_composition_v14_337/. For each stored physical output mode n, define the chosen represented trial correction

delta_y(n) = floor_160(r_point(n) / midpoint(log_normalized(n,128))).

Support only b<=n<=the final evaluated Far-window mode: 256000 Middle rows plus 8192 Far-window rows, 264192 rows per sector. First modes are 512001/512002; final modes are 1040383/1040384. Keep the existing refined Near trial and original infinite diagonal seed unchanged outside this finite additive patch. In particular, this patch is ADDED to the original infinite seed on its support; it does not replace or double-count that seed.

Deliver:
- the exact dyadic correction buffers, with bits, signed little-endian width, count, row lattice, byte length and SHA256;
- exact correction norm squared and outward norm upper, l1, and a rigorous whole-trial norm upper by the triangle inequality using v14.300's current trial norm bound;
- operator-domain justification (finite supported correction to the existing domain-admissible trial);
- the actual producer/recipe and pinned input residual hashes, with no contraction or new acceptance claim.

This is a candidate construction, not an assertion that Lambda inverse equals the Schur inverse. Using a point residual to choose a represented trial does not imply the point is the exact physical residual. Subsequent fresh physical certificates decide whether the candidate works.

Return the frozen bytes/certificates through an additive accessible payload namespace or the same hash-bound transfer mechanism used in v14.334. If this specific transfer is blocked by a rule in the Sandbox thread, record that exact blocker promptly rather than marking the candidate delivered with only inaccessible hashes.

## Ownership / no duplicated work

Sandbox owns construction and delivery of this wider correction candidate. Lane A owns the resulting new finite RHS, fresh finite lift and changed compact action/residual consumers. Do not reuse the old finite lift as a certificate for the changed RHS. The existing tail-only action bank remains reusable for the original infinite seed; the additive finite correction belongs in the changed compact component.

The expanded compact support reaches beyond 4R into the evaluated Far window. The existing 42-moment compact expansion cannot automatically be used immediately beyond that support with its old uniform ratio. Lane A must recompute the support/output split and geometric remainder or evaluate close output rows explicitly.

## HANDOFF — External Audit

Please check the wider candidate's exact input hashes, support/parity and representation/domain/norm facts when it returns. No contraction theorem or residual pass is being requested from the candidate alone.

## Next on return

Lane A will acknowledge and hash-verify the actual candidate bytes, evaluate B*delta_y for the updated RHS, certify a fresh lift, then measure the new residual across all returned evaluated regions. Whole residual acceptance, signed stationary pairing and infinite capacity closure remain open.
