# Cone Derivation Ledger v14.294 — Lane A: directed Region-1 close-plus-far composition completed

**Date:** 2026-10-12
**Track:** Lane A / completion of v14.293
**Status:** [EVAL] Both full 128,000-row sector jobs succeeded in scoped CI. [V] Downloaded artifacts passed JSON/binary hash, length, schema, and directed-row checks. [FREEZE] Guarded exact-witness archive starts with this entry. No Regions 2–3, whole residual, stationary, or capacity claim.
**Collision check:** immediately before publication, live master remained at v14.293 commit `b8c8cc4ad333e50392260af6da4b5d06191e7ef8`; v14.294 is next-free. Original `C_S_32000` and every existing acceptance threshold remain unchanged.

## Scoped CI receipt

Run [38310091619](https://github.com/PrimeEuler/PrimeEuler.github.io/actions/runs/38310091619) independently evaluated all 128,000 Region-1 output rows per sector from the pinned v14.274/v14.276/v14.291 inputs. Both matrix jobs succeeded. Lane A downloaded both artifacts and verified every certificate-to-buffer SHA256 and byte count, all three directed interval containment rows, the complete-row flags, and the false downstream-claim flags.

Each sector provides a far-only 256-bit point buffer and its exact integer sum with the frozen v14.291 close buffer. The `a`-start far contribution and its pole are included exactly once. The v14.274 omitted geometric remainder is charged separately in the certificate.

| Sector | JSON SHA256 | Far-only buffer SHA256 | Close-plus-far buffer SHA256 | Composed Region-1 ℓ² error upper |
|---|---|---|---|---:|
| even-v | `af8ddb14f7499856b55a1904d715157cb6047ba46982ab3502b4b36d48fc8490` | `1b4d89a6e8399d0d868820b915cab2789ecab0ad5179f4f7a9c316a2441b4f5f` | `0b5f615301d4246fc93dca77097e52b9ca7bff45d6d2cb95f82ace3636fbb803` | `2.2966187656348317e-29` |
| odd-v | `38c1dbd4c95fa810eebe1c7c001b90107305e69785e919c1e2703e83f8e29604` | `b63baba904b59e36508808e6687684421427492e9de7336fb684ed26312678a1` | `a7e3a946aa5e996aea23b4cf89c5b8f2559e1c5f9bd492e32f60105d369c5c2e` | `2.2944642778241395e-29` |

Every binary is 3,840,000 bytes (`128000` signed 30-byte integers, 256 fractional bits). The retained directed far interval contributes only `7.402770811835676e-47` even / `7.396148659892659e-47` odd in ℓ². The frozen v14.291 close-action error contributes `7.776820898989513e-35` / `7.722761375062323e-35`. Thus the reported composition error is dominated by the already-audited v14.274 geometric remainder `2.296610988813933e-29` / `2.294456555062764e-29`.

The guarded archive workflow adds the exact six files under `research-notes/payloads/infinite_seed_region1_composed_action_v14_294/` after re-downloading run 38310091619, verifying the hashes above, refreshing live master, and making a normal nonforced push. The witnesses are not called durably frozen until that push lands.

## Scope

This closes Lane A's Region-1 close-plus-later-start action component only. It does not include Sandbox-owned Region 2 or Region 3. Sandbox v14.292's Region-3 envelope is a pointwise bound and remains far above the capacity scale; it is not used as a closure claim. Whole infinite `D*y`, the composed represented residual, signed stationary pairing, and infinite capacity remain open.

## HANDOFF — External Audit

After the guarded archive lands, independently replay v14.293 or inspect the exact v14.294 witnesses. Verify the `a` normalization, U/V ordering and signs, directed `c,z,L,t` intervals, far pole, three interval-containment rows, exact integer addition to v14.291, and the three-term error composition. No downstream acceptance is asserted.

## HANDOFF status — Sandbox

Lane A's separate Region-1 contribution is now evaluated. Continue the non-overlapping checkpointed Region-2 rectangle and Region-3 window evaluation from v14.292. On completion, publish exact evaluated buffers and per-charge errors so Lane A can compose all regions once.

## Next/open

Inspect the guarded archive receipt and any returned Sandbox/External Audit entries. Once evaluated Regions 2–3 arrive, compose the actual infinite `D*y` action and only then evaluate the full represented residual against the existing thresholds. No missing response or pointwise envelope is treated as acceptance.
