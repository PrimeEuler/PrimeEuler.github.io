# Cone Derivation Ledger v14.543 — Sandbox return: v14.541 direct-middle fresh finite lifts certified and exactly replayed, both sectors

**Timestamp:** 2026-10-17 (EDT, evening)
**Lane:** Sandbox (little Euler)
**Parents:** v14.542 (Audit R307, producer self-check re-executed 8/8, no defect), v14.541 (Lane A ACK + hash-gated fresh-lift producer HANDOFF), v14.540 (Audit R306, v14.539 checked, no defect), v14.539 (sandbox complete-RHS return), v14.510/v14.511 (RHS producer + ratification), v14.500/v14.502 (delta candidate + clarification), v14.403 (base RHS freeze).
**Status:** scoped production return under Jeremy's 2026-10-17 authorization. The v14.541 HANDOFF is closed for the fresh-lift phase: both sector fresh finite lifts were produced against the exact v14.539 RHS hashes and exactly replayed, byte-identically. **Lift only:** no whole action, new residual, whole-residual acceptance, stationarity, or infinite-capacity claim is made. The original C_S,32000, the 0.002 whole-trial cap, the 4e-30 RHS threshold, and the unchanged 2e-10 finite-lift remote-action cap are unchanged. No v14.403 lift was reused (`old_v14_403_lift_reused = false`, both sectors).

## Run record

Producer: `suzuki_direct_middle_delta_finite_lift.py`, delivered by Lane A at commit `20c3264ba317dc78404b65a928862e46c7e311d4` (research-notes), driven through the engine `suzuki_new_finite_lift.py` from research-notes (v14.239 era). Run supervised under systemd (`lift541.service`, workspace launcher `lift541/run_lift541.sh`, sectors sequential, per sector produce then exact replay), consuming the verified v14.539 RHS outputs in `rhs511/out/` exactly as pinned (RHS certificate SHA-256 even `d56eaf3ade699c5c85ad3ae954c5817c3e58045c6894268b3e49e6a7b2ad55ad`, odd `19c67577d032366253625a0f12ed08c217d10c0245fdd03e4bb6ce953cfb2884`; candidate point SHA-256 even `c5b6845303cb059ca9a1ed79a628c4ba135fd49f2012b5fc011b0aeb14d12bb2`, odd `e9efaf914390a6edda7076ad1a1dfa7da5a398246895bc76e00cbb21b682f776`).

- First even-v produce attempt (2026-10-17T18:49:37Z) exited 1 before any certificate was written, on `TypeError: cg() got an unexpected keyword argument 'rtol'`: the engine calls `scipy.sparse.linalg.cg(..., rtol=2e-14)`, the rtol keyword of scipy >= 1.12, while this box ships scipy 1.11.4, whose cg takes `tol`.
- The rerun (launched 2026-10-17T18:50:53Z) drove the unmodified producer through the environment shim `lift541/run_producer.py`, which translates only `rtol -> tol` when the installed cg lacks an `rtol` parameter (identical relative-residual semantics). No producer or engine file was modified. The float CG only finds the lift; certification is exact Fraction arithmetic, and replay re-derives the certificate byte-exactly from the lift buffer.
- Even-v: produce exit 0 at 2026-10-17T18:52:20Z (complement CG iterations 59, then 61); replay exit 0 at 18:52:35Z.
- Odd-v: produce exit 0 at 2026-10-17T18:53:59Z (complement CG iterations 56, then 58); replay exit 0 at 18:54:14Z. Launcher wrote `LIFT541_DONE` only after both sectors' produce+replay completed cleanly.

## Certificates and gates (independently re-verified after completion)

For each sector the sandbox monitor re-hashed the lift buffer against the certificate's `lift_buffer` spec (bytes / width / count all match: 11,136,000 bytes, width 87, count 128,000), confirmed the replay exit 0 in `run.log` (replay asserts byte-identical certificate re-serialization, so a clean replay exit is the exact-replay verdict), and re-read both certificates as exact Fractions. Certificate schema `cone.certified-direct-middle-delta-finite-lift.v1`; `finite_lift_certified = true`; all 128,000 physical residual coordinates certified; all six protected components retained; physical RHS and operator errors included once.

| sector | physical projected residual upper | physical protected dot upper | finite-lift remote-action charge upper (cap 2e-10) | lift norm (display) | inverse energy error upper (display) |
|---|---:|---:|---:|---:|---:|
| even-v | 1.0673274734431161e-26 | 4.484234982301517e-12 | 9.886626067174243e-11 | 3060713200.0968556 | 2.0195325411596953e-23 |
| odd-v | 2.139615210961616e-28 | 1.791344134121116e-15 | 3.948878028782367e-14 | 60447700.176978156 | 3.221825968223164e-30 |

Both remote-action charges are below the unchanged `2e-10` cap (`finite_lift_action_charge_below_2e_minus10 = true`, both sectors).

Exact-replay verdicts: even-v replay exit 0, certificate re-serialized byte-identically; odd-v replay exit 0, certificate re-serialized byte-identically.

## Output hashes (SHA-256)

Lift certificates (files in `lift541/out/`):

- even-v `direct-middle-finite-lift-even-v.json`: `d3ea64364f8ca69b569ed9f981828048bd80448d3dc6055934b50e6a278fa263`
- odd-v `direct-middle-finite-lift-odd-v.json`: `6c52c4fd7eaa615582375e455588164316254ced57cfb9b4a90d5b82bd5fa95f`

Lift buffers (as recorded inside the certificates and re-hashed by the monitor):

- even-v `even-v-direct-middle-finite-lift.bin`, 11,136,000 bytes, 128,000 x 87, bits 662: `d3fd00e05bd19709811086ec246764feb36379dc52ec410798d2a01d8e1bf237`
- odd-v `odd-v-direct-middle-finite-lift.bin`, 11,136,000 bytes, 128,000 x 87, bits 663: `a852b54e22ef62d029528c9856f24a5ea6fb9618c99725ccdb052b5a562a739c`

The buffers remain in the sandbox workspace (`lift541/out/`); a repository payload transfer of these bytes awaits Jeremy's explicit line, per standing practice. The hashes above freeze the bytes regardless of where they sit.

## Environment provenance

- Producer commit: `20c3264ba317dc78404b65a928862e46c7e311d4` (adds `research-notes/suzuki_direct_middle_delta_finite_lift.py`).
- Engine: `suzuki_new_finite_lift.py` from research-notes (v14.239 era), used unmodified.
- scipy 1.11.4 on this box, with the `rtol -> tol` rename shim in `lift541/run_producer.py` (sandbox-side wrapper only; it takes effect only because the installed cg lacks an `rtol` parameter). No producer or engine bytes were modified.
- Certification is exact Fraction arithmetic; the shim affects only the float CG search that finds the approximate lift, and the replay mode re-derives each certificate byte-exactly from its lift buffer.

## Scope flags (unchanged, honest)

Both certificates carry `whole_action_evaluated = false`, `new_residual_evaluated = false`, `whole_residual_acceptance_certified = false`, `stationary_acceptance_met = false`, `infinite_capacity_tail_closed = false`, and `old_v14_403_lift_reused = false`. No action, residual, whole-residual, stationary, or capacity claim is made from this lift-only gate.

## Disposition

The v14.541 HANDOFF is closed. Lane A's next action per v14.541 stands: freeze/replay the exact fresh-lift hashes above, then prepare the changed support-aware compact/original-seed action and v14.406 residual evaluation with all charges applied exactly once (v14.354 exactly once; source plus v14.403 fresh-lift transport exactly once). Whole-residual acceptance, stationarity, and infinite-capacity closure remain open.
