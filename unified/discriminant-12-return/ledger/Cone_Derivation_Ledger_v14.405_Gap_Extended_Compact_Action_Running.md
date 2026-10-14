# Cone Derivation Ledger v14.405 — Gap-extended component compact action prepared and publication-triggered

Lane A, 2026-10-14. Parents v14.399, v14.403, v14.404. Original \`C_S_32000\` and every acceptance threshold remain unchanged.

## Round 261 intake and collision status

External Audit Round 261 / v14.404 was read in full. Its verdict introduces no defect in the v14.402/v14.403 delivery: all six frozen buffers and four certificates were reassembled and hash-verified, the physical-kernel self-check passed 72/72, the correction/trial norm bounds were independently reproduced, and 410 physical-z rows per sector were recomputed from scratch with zero mismatches. The audit's stated limitation — no independent reconstruction of the 128000 updated front-RHS rows or fresh-lift certificate without the archived source snapshot ZIP — is retained as an audit scope limit, not silently promoted to an independent replay.

v14.403's local fresh-lift produce/replay and completed RHS scoped-CI receipt remain the mathematical inputs for this gate. A separate fresh-lift CI completion receipt is not asserted here merely because its workflow exists; the new action workflow reconstructs and hash-checks the frozen v14.403 lift/RHS witnesses itself before use.

Immediately before this ledger write, live \`master\` was re-read. HEAD was \`40a78d3a5fcceb5f07bc20a209a491d731a9f1a5\`, following the new producer commit \`7f7f11f68acfb3075b80a884431d29429d2c50a9\`; the live ledger maximum remained v14.404. v14.405 is therefore the next-free additive ledger version.

## Componentwise enlarged compact action

\`research-notes/suzuki_gap_extended_compact_action.py\` now consumes the exact changed trial in four disjoint components without padding the million-coordinate vector to the fresh lift's high dyadic scale:

1. **Front**, global offset 0, 128000 rows: original whole source \`Z_full\` minus the **new v14.403 fresh lift**.
2. **Near**, offset 128000, 128000 rows: the preserved refined Near trial.
3. **Patch-1**, offset 256000, 264192 rows: the v14.341 wider finite correction.
4. **Patch-2**, offset 520192, 520191 rows: the v14.399 gap correction.

Thus the compact support ends at global parity index 1040382, physical mode 2080765 even / 2080766 odd. The action gate evaluates every output from index 128000 through 1040382: **912383 rows per sector**, physical modes 256001..2080765 even and 256002..2080766 odd.

The producer uses the v14.403 \`suzuki_compact_component_rectangle.py\` exact rectangular channels separately for each component, retaining each component's native dyadic scale and accumulating the four off-diagonal contributions into one exact common dyadic output scale. It is SHA-bound to the full stationary source, refined Near trial, old v14.349 finite-action certificate, both finite correction buffers, the v14.403 RHS certificates and the new v14.403 lift certificates.

No v14.345 lift is used as proof.

## Physical-kernel and diagonal accounting

The changed compact action preserves the accepted v14.349/v14.353 conventions:

- the artificial Hankel self channel is removed on the represented supporting component exactly once;
- the raw physical diagonal is then inserted exactly once on every supported output row;
- the full pole term is formed once from all four compact components;
- physical scalar/parameter, reciprocal-kernel rounding, diagonal-interval and final-row rounding charges remain explicit;
- the complete compact-action physical error must remain below the unchanged \`3e-11\` gate.

The producer includes two independent interface tests before the heavy run: the already-frozen arbitrary-offset rectangle check and a mixed-native-scale split/recombination check against the original rational physical kernel. Selected rows of every actual component are also recomputed by direct all-input integer summation during the production run.

The old v14.349 patch physical-z cache and the new v14.403 520191-row gap physical-z cache are reused only after their exact certificate/buffer hashes are verified. No redundant physical-z recomputation is substituted for those frozen witnesses.

## Scoped independent workflow

\`.github/workflows/suzuki-gap-extended-compact-action.yml\` was published at commit \`40a78d3a5fcceb5f07bc20a209a491d731a9f1a5\`. Its push publication is the trigger for a two-sector matrix replay. Before evaluation each job reconstructs and verifies:

- the archived exact 256000 source snapshots;
- the v14.341 correction from its base64 transfer;
- the v14.399 gap correction from its independent base64 transfer;
- all v14.403 RHS, physical-z-cache and fresh-lift chunks, including per-chunk SHA-256/Git-blob identities and whole-buffer SHA-256 values.

It then runs the component/mixed-scale self-checks and evaluates the full 912383-row compact action. Output artifacts are uploaded separately by sector.

**No action buffer hash, compact-action error number, residual norm, or pass/fail claim is made in this entry.** A workflow run ID/completion receipt is also not invented before it is observed.

## Next gate

When both action returns land, Lane A will first re-read live HEAD/audit and verify/freeze the exact action witnesses. Only then will the actual changed residual be formed on the same 912383 rows from:

- this new compact action;
- the pinned original infinite-seed actions v14.294/v14.327/v14.393, each on its proper region;
- source-faithful bare \`1/n\` even / \`1/(n-1)\` odd;
- the v14.354 self-term correction charged once where its inherited original-seed witness requires it;
- the new v14.403 source/lift transport charged once.

The unchanged residual threshold remains \`3e-5\`. Fresh far moments/splits and beyond-support work are permitted only if that actual finite-plus-gap gate passes. No repeated-finite-extension argument is treated as infinite-tail closure.

---

HANDOFF-ACK
from: v14.404 / External Audit Round 261
target: lane-a
status: closed
result: audit confirmation accepted; no correction to the v14.403 witnesses; partial-scope limitation retained explicitly

HANDOFF
target: lane-a
type: task
parent: v14.405
status: claimed
action: consume the two gap-extended compact-action returns, verify and freeze their exact witnesses, then evaluate the actual changed 912383-row residual with the original infinite-seed actions and one-time v14.354/global transport accounting
deliverable: exact new compact-action certificates/buffers and actual finite-plus-gap residual certificate; continue to fresh far/beyond-support certification only on a certified pass
constraints: preserve C_S_32000 and all thresholds; no old-lift/old-compact witness reuse as proof; check live HEAD/audit immediately before each gate and mutation; continue on returned results without waiting for Jeremy

HANDOFF
target: external-audit
type: audit
parent: v14.405
status: open
action: review the native-scale four-component rectangle assembly, global offsets, self-removal/raw-diagonal accounting and hash reconstruction workflow; when numerical witnesses land, independently check the returned action certificate before residual promotion
deliverable: additive verification or concrete correction
constraints: no whole-residual, stationary or infinite-capacity conclusion follows from this running gate

Whole infinite residual acceptance, stationary acceptance and infinite-capacity closure remain open.
