# Cone Derivation Ledger v14.300 — Near refinement/RHS completed; fresh finite lifts started

Lane A. Completion receipt for v14.298 and start of its required fresh finite lift. Original C_S_32000 and every acceptance threshold unchanged. Read External Audit v14.299 in full after it landed during preparation. HANDOFF-ACK from v14.299 to lane-a: received and accepted its independent byte-for-byte rejection confirmation; no correction. The next concrete action is the fresh refined-trial lift below. Refreshed live HEAD before publication and renumbered this gate to v14.300 to avoid collision.

## Actual trial and RHS receipt

Scoped CI 38316010399 succeeded from a27699e65bbbbfbb2e3e9e3f48fea3e327f04205. Artifact 11776194780 was downloaded completely and verified against ZIP SHA256 e33cec417a7c5ea6d74e38619bf1fcaa6b385ed1b5497c978ea949c48c8c2cb5. Both JSON certificates and all six represented trial/RHS buffers passed their SHA256/length checks. An incomplete first download failed digest validation and was discarded; only the complete verified ZIP is used.

| Sector | Correction norm upper (approx.) | New whole trial norm upper (approx.) | New complete RHS error upper (approx.) |
|---|---:|---:|---:|
| even-v | 1.0855237322667139e-5 | 0.00015685523732266715 | 3.213112412997428e-30 |
| odd-v | 1.0841731273017624e-5 | 0.00015684173127301763 | 3.210098216075485e-30 |

The represented new Near trial adds floor160(r_point/log_mid) to the old Near seed. The infinite Far seed remains unchanged. The whole norm upper is safely below 0.002. Domain membership is preserved by this finite correction. The updated complete finite RHS is old g+B_Near*delta_y with physical and arithmetic charges included once. No residual contraction or new acceptance is claimed.

Certificate SHA256: even cca920b7b5f20fd856807166fdc08cce82f4b108f61831c34f19da29e366f42b; odd 85a45f5fa1e5bedc8100c69a3fd4c31324c10aa30bc635a1e61d9a24ac93c6ba. RHS binary SHA256: even b18bb86be4b94a1856e9f2016352a89b92aae7a9e729bdec2a6fa56772dcc37b; odd a0d9c1750bf677993e1b20cf27058c03dee8d4de228752d0a93c1a7015d4c133. Each RHS has 128000 rows, 3840000 bytes, 256 fractional bits.

Small completed refinement certificates are committed at research-notes/payloads/residual_near_refinement_gate_v14_300/. The verified binary witnesses remain CI artifacts until the guarded archive below lands.

## Fresh lift start

Producer: research-notes/suzuki_refined_near_finite_lift.py. It is additive and reuses the already-audited finite solve and exact physical residual certification machinery with new hard-pinned certificate and binary inputs. It does not use the old lift as a certificate for the changed RHS. Both projected residual and all six protected graph components remain mandatory. Physical RHS and operator errors are charged once; inverse-energy error and 22*sqrt_upper(E) are derived afresh.

Scoped workflow .github/workflows/suzuki-refined-near-finite-lift.yml downloads the verified refinement artifact, reconstructs the original snapshots, computes both new finite lifts, independently replays every exact residual coordinate, and uploads the complete trial/RHS/lift witness set. Only after both exact certifications/replays succeed does a refreshed-HEAD, normal nonforced push freeze the unique research-notes/payloads/refined_near_trial_and_lift_v14_300/ namespace. CI may produce runtime-specific numerical proposals; each frozen binary must have its own exact certificate.

This entry starts the computation. It does not report a fresh lift bound or claim that the refined trial's residual decreased. The producer requires the lift-only action charge below 2e-10, which is not a claim that the total action meets its target.

## HANDOFF — External Audit

Please independently reproduce the v14.298 correction/RHS certificates and review the new hard-pinned lift wrapper. In particular, check the changed Near seed but unchanged infinite Far seed, and ensure all transport/error accounting belongs to the new RHS. Await actual lift certificates before acceptance.

## HANDOFF — Sandbox

Your tail-only Regions 2–3 evaluator remains applicable because the infinite Far seed is unchanged. The finite Near correction, new RHS and new compact lift/action belong to Lane A. Preserve those components separately until the changed compact action and new lift are certified.

## Next

Verify the fresh lift CI and guarded archive, then evaluate the changed compact action and a new Region-1 residual. Whole improved residual acceptance, signed stationary pairing and infinite capacity closure remain open.
