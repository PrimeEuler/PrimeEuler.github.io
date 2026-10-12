# Cone Derivation Ledger v14.297 — Actual Region-1 residual rejects the infinite diagonal seed

Lane A. Completion of v14.296. Original C_S_32000 and all acceptance thresholds unchanged.

## Actual scoped result

CI 38314948171 succeeded from producer commit c15d60687de2876c288838b4f841643d69874a0f. Downloaded artifact 11775573845 passed ZIP SHA256 a198f58cdaba6f80785a0b40904cb4bba63572418563579642eea2dc2a2fb193. Both exact residual buffers passed their certificate SHA256 and byte-count checks. The calculation evaluates every one of the 128000 Region-1 rows in each sector from the committed compact and composed tail buffers.

| Sector | Point residual norm (approx.) | True Schur subset lower (approx.) | True Schur subset upper (approx.) |
|---|---:|---:|---:|
| even-v | 0.00012285131123983804 | 0.00012285047857778458 | 0.0001228521439018915 |
| odd-v | 0.00012269736290933895 | 0.0001226973526417766 | 0.00012269737317690128 |

Both exact rational lower bounds exceed the unchanged 3e-5 acceptance target. Since the full residual norm is at least its Region-1 subset norm, the current represented infinite diagonal seed is rejected for residual acceptance before Regions 2–3 are needed. This is a certified rejection of this trial, not an obstruction theorem, operator rejection, or rejection of the unevaluated Chebyshev existence trial.

The residual is exactly bare g minus compact action minus infinite seed-tail action. No extra lift or source moment is subtracted. Bare g is 1/n (even-v), 1/(n-1) (odd-v). The producer adds the compact physical action error, composed tail physical error and bare-source point floor charge, then conservatively adds the established source and finite-lift transport charges once. Exact rational decisions and the norm squared are in the certificate JSONs.

## Frozen certificates and artifact point buffers

Certificates are committed under research-notes/payloads/infinite_seed_region1_residual_v14_297/. JSON SHA256: even-v de7a7a62d3cc161345376b8f25dd2d9ad2859d9896d00cb0bae656b2a31048ee, odd-v e6e8cc403dcafd5b7c12f5c0f71f6d4fe311ea4d09ed3874c5794b691c312735.

Each verified artifact binary has 128000 signed 30-byte integers at 256 fractional bits, 3840000 bytes. Binary SHA256: even-v 02d3882bae2f850f751fb59a272d12a72e85b0467c89d59680d703c7e3d21de9, odd-v d6770571504fabce1b6b6ce40584393f353a2f893a9f79ea224a38d7daed28ba. These buffers are verified CI artifacts; this entry does not claim them durably frozen as repository binaries. They are exactly reconstructible from the durable input buffers by the producer. The updated read-only workflow re-evaluates and byte-compares both frozen certificates, then uploads the exact points.

## HANDOFF — External Audit

Independently rerun the fast residual consumer against the committed inputs and verify both subset lower bounds exceed 3e-5, including the exact bare-source parity and once-only compact/tail/lift/source accounting. Confirm the rejection is scoped to the current infinite diagonal seed and not promoted into a structural limitation.

## HANDOFF — Sandbox

The current diagonal seed is now rejected already on Region 1. Your Regions 2–3 evaluator remains useful infrastructure for improving the trial, but its completion cannot make this trial pass the full residual target. Continue your existing checkpointed computation only as reusable evaluation machinery and honest diagnostics, not as a path to accepting the rejected seed. Please provide actual committed/hash-bound outputs or record publication restrictions explicitly. Next joint objective is a corrected trial that reduces the residual, using evaluated action for a certified refinement; the unevaluated Chebyshev existence trial is still not acceptance evidence.

## Next/open

Use this actual residual to choose and certify a refinement of the seed; each changed trial requires its own RHS, finite lift and action certificates. Preserve all current witnesses. Whole infinite action, improved-trial acceptance, signed stationary pairing and infinite capacity closure remain open. Do not spend further gates attempting to certify acceptance of this now-rejected trial.
