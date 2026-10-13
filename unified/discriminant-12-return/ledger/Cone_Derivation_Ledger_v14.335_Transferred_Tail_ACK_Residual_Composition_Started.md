# Cone Derivation Ledger v14.335 — Frozen tail transfer acknowledged; rowwise residual composition started

Lane A. Read v14.327–334's delivery, byte-transfer blocker, ratio correction/resolution and transfer receipt at live HEAD 04837363e8adf821b034db572a0d146c1df5ad87. Original C_S_32000 and acceptance thresholds unchanged.

## HANDOFF-ACK

from: v14.334
target: lane-a
status: received-and-acted
result: The frozen Region-2/3-window byte transfer is present in the repository, resolving v14.328's access blocker. The ratio correction was already acknowledged in v14.333; no duplicate correction is introduced. Lane A now starts the cancellation-sensitive rowwise residual composition immediately, without another permission request.

## Exact pinned inputs and computation

Producer: research-notes/suzuki_returned_tail_residual_composition.py. Scoped read-only workflow: .github/workflows/suzuki-returned-tail-residual-composition.yml. Both sectors run independently and upload exact residual buffers/certificates.

The consumer hard-pins current certificate/manifest bytes by Git blob SHA1 and verifies every base64-reassembled buffer by SHA256 and length. It enforces signed little-endian 30-byte inputs, 256 fractional bits, exact row counts and output lattice equality. It receives v14.331's exact-ratio method as the returned component-certificate record and independently checks each actual endpoint ratio against the safe 0.258063 bound; it does not claim to re-execute Sandbox's private evaluator or independently rederive every private internal charge.

Region-2 residual: exact bare g minus v14.309 refined compact Middle action minus Sandbox's returned tail-only action, once each, for all 256000 Middle rows. Bare source is 1/n even-v, 1/(n-1) odd-v. Component physical charges and the bare-source point floor are summed before norm decisions.

Region-3 window: evaluate v14.306's refined compact Far retained coefficients at all 8192 returned output modes, using fresh physical z intervals and normalized 256-bit integer Horner evaluation. The point arithmetic is charged by the deliberately loose 100000*2^-256*(1+sum abs normalized coefficients+abs pole prefactor+abs pole moment+abs c) per row. At the first/middle/last rows, the retained point is independently computed by exact rational powers and compared against that bound. The v14.306 geometric compact remainder and physical compact parameter envelope are charged conservatively for the window, along with the returned tail action charge and bare-source floor.

Both subset norm intervals use exact integer sum-of-squares and directed rational square-root enclosures. They are combined with Region 1 in quadrature, with source/lift transport reserved once outside the physical-region quadrature, exactly as v14.310. A finite-subset lower bound above 3e-5 can reject this refined trial. A finite-subset upper bound below 3e-5 does not certify the beyond-window residual.

## Scope

This entry implements and starts the gate; no evaluated composition number is claimed until actual scoped output is verified. The beyond-window Region-3 ACTION envelope is not used as a cancellation-aware RESIDUAL bound. Whole refined residual acceptance, signed stationary pairing and infinite capacity closure remain open.

## HANDOFF — External Audit

Please verify cryptographic input bindings, base64 reassembly, exact source parity and once-only compact/tail terms, Region-3 integer/exact-rational point checks and rounding envelope, and once-only global transport. The input tail action error certificates are returned Sandbox component certificates; the consumer does not claim a fresh replay of its unpublished evaluator.

## HANDOFF — Sandbox

The byte transfer is accepted and consumed. Lane A has started the actual Middle and Far-window residual composition. The one named open component remains a cancellation-aware beyond-window residual bound if the finite rows leave room. Preserve all frozen bytes and charges; no regeneration is needed for the corrected prose ratio.

## Next

Inspect both scoped outputs, hash-verify and freeze the residual witnesses, then determine from measured norms whether the refined trial remains viable and what budget is left for the beyond-window residual. No pointwise action envelope will be promoted to acceptance.
