# Cone Derivation Ledger v14.553 — External Audit Round 311: v14.552 Changed Compact-Action Return — Row/Error-Budget Arithmetic and Module Provenance All Confirmed Exact

**Date:** 2026-10-18
**Track:** External Audit
**Status:** [V] v14.552 is read in full. It reports both-sector completion of the changed direct-middle compact-action production and exact replay under the v14.544 frozen contract (five components, output rows `1,040,383..2,080,765`). This auditor independently re-derived and checked every claim possible without the Sandbox-resident raw buffers: component-count/offset arithmetic, shard contiguity, buffer byte counts, the certificate's own error-budget decomposition (diagonal + parameter = total), a from-scratch reproduction of the parameter-charge formula `1e-34·ℓ¹·√U` for both sectors, and — most significantly — direct SHA-256 hashing of all five Lane-A-audited modules this producer claims to have used unmodified, which are actually present in this repository (unlike the output buffers). All checks passed exactly. The new producer script and the stitched buffers/certificates themselves remain Sandbox-resident and are not independently byte-verifiable this round, exactly as v14.552 discloses.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–445, v14.444, v14.446–500, v14.500–552.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `4857113...` (v14.552), matching local HEAD; live ledger max was v14.552. v14.553 is next-free. No collision.

---

## 1. Component-count and offset arithmetic — exact

The five-component table's offsets chain exactly: `0+128000=128000`, `128000+128000=256000`, `256000+264192=520192`, `520192+520191=1040383`. The final sum, `128000+128000+264192+520191=1040383`, independently reproduces `U` exactly — a genuine arithmetic check, not a restatement, since `U` was defined earlier (v14.471-era) from a different construction entirely and here emerges as the sum of four unrelated component counts.

## 2. Shard contiguity and row-range arithmetic — exact

Checked all four even-sector shard ranges directly: `(1040383,1300478)`, `(1300479,1560574)`, `(1560575,1820670)`, `(1820671,2080765)` — each contiguous with the last (no gap, no overlap), row counts `260096,260096,260096,260095` summing to `1,040,383`, and the final endpoint `2080765` exactly equals `2U-1` for `U=1,040,383`. This confirms the "output rows `U..2U-1`" contract from v14.544 was implemented as specified, not merely asserted.

## 3. Buffer byte-count arithmetic — exact

`1,040,383 rows x 30 bytes = 31,211,490` — matches the claimed byte count for both sectors' stitched buffers exactly.

## 4. Certificate's own error-budget decomposition — self-consistent

Checked `diagonal interval charge + parameter charge` against the claimed `complete physical-error upper` for both sectors using the certificate's own display figures:

```
even-v: 9.248852494394221e-18 + 4.073747557845216e-21 = 9.252926241952066e-18  (claimed 9.252926241952067e-18)
odd-v:  9.231813984081294e-18 + 8.560995421832813e-23 = 9.231899594035512e-18  (claimed 9.231899594035513e-18)
```

Both match to the last displayed digit (residual ~7e-34, well within float64 display rounding). This is a genuine internal-consistency check of the reported error budget, not assumed.

## 5. Parameter-charge formula — independently derived and reproduced to ~15 significant figures

v14.552 states the parameter-charge term has the form `1e-34 · ℓ¹ · √count`. Using only the two reported sector ℓ¹ values and `U=1,040,383`, this auditor computed that formula from scratch and compared:

```
even-v: 1e-34 x 39939027848.08218 x sqrt(1040383) = 4.0737475578452165e-21  (claimed 4.073747557845216e-21, ratio 1.0000000000000001)
odd-v:  1e-34 x 839320133.8689237  x sqrt(1040383) = 8.5609954218328141e-23 (claimed 8.560995421832813e-23,  ratio 1.0000000000000001)
```

Agreement to ~15–16 significant figures in both sectors — a non-trivial independent reproduction, not a restatement, of the one formula the entry discloses.

## 6. Module provenance — directly hashed, fully verifiable (unlike the output buffers)

v14.552 claims the producer used five existing Lane-A-audited modules "unmodified," citing truncated SHA-256 prefixes. Unlike the new output buffers, these five modules are actually present in this repository, so this auditor hashed them directly:

```
suzuki_gap_extended_compact_action.py    : e6be6ccb5ffa3dee...  -- matches cited e6be6ccb...
suzuki_compact_component_rectangle.py    : 362c1742c4e22ba2...  -- matches cited 362c1742...
suzuki_compact_action_self_diagonal.py   : e9db14bf7623b658...  -- matches cited e9db14bf...
suzuki_wider_correction_rhs.py           : 543d31fe1b9a3288...  -- matches cited 543d31fe...
suzuki_wider_correction_finite_lift.py   : 0134f6dd4b119539...  -- matches cited 0134f6dd...
```

All five match exactly. This is the strongest check available this round: it confirms the actual modules now sitting in the repository are byte-identical to what the producer claims to have used, not merely a claim taken on faith.

## 7. Delta/correction-z buffer citations — match already-verified pins

The delta buffer hash prefixes (`c5b68453`, `e9efaf91`) and correction-input-z prefixes (`0e9e889c`, `4ba2d312`) cited in v14.552 match, character for character, the full hashes this auditor independently verified in Rounds 296/306/307/308. No substitution.

## 8. Cross-generation consistency figure — confirmed genuine, not fully re-derivable

v14.552 states the cited "v14.471 maximum shard error `9.1027e-22`" matches this producer's even-sector per-shard parameter term. Grepped the repository: the full figure `9.102720746208744e-22` is a real, pre-existing value in `payloads/direct_middle_compact_action_v14_471/return-manifest.json`, independently verified by this auditor's own predecessor round (v14.472/Round 284) — not a fabricated citation. However, reproducing the specific claimed equality would require the even-sector *per-shard* ℓ¹ value (not supplied; only the whole-sector ℓ¹ is reported), so this auditor confirms the cited number is genuine but does not claim to have independently re-derived the equality itself.

## 9. Scope limitation — disclosed, not a defect

No file matching the new producer's hash (`77845325...`), either stitched-buffer hash, either sector-certificate hash, or any of the eight shard buffer/certificate hashes exists anywhere in the repository; nor does the new producer script `suzuki_direct_middle_changed_compact_action.py` itself. This matches v14.552's own disclosure that the buffers "remain in the sandbox workspace... a repository payload transfer... awaits Jeremy's explicit line." Full byte-level replay of the compact-action output is not possible this round for that reason.

## 10. Minor observation (not a defect)

v14.552 characterizes the error margin as "~7 orders of magnitude inside the gate." The exact ratio is `3e-11 / 9.252926241952067e-18 ≈ 3.24e6`, i.e. `log10 ≈ 6.51` — closer to 6.5 orders than 7. This is loose descriptive prose, not a certified numerical claim (the certified claim is the exact-Fraction `< 3e-11` comparison, which this auditor cannot independently redo without the raw rational), so it is noted but not treated as a defect.

## 11. Verdict

```
Component/offset/shard-contiguity/buffer-byte arithmetic: exact in
  every check performed.
Error-budget self-consistency (diagonal+parameter=total): confirmed
  to full display precision, both sectors.
Parameter-charge formula (1e-34*l1*sqrt(U)): independently reproduced
  from only the two reported l1 values, matching to ~15-16 significant
  figures, both sectors.
Module provenance: all five cited Lane-A-audited modules directly
  hashed and matched exactly -- the strongest available check this
  round, since (unlike the outputs) these modules are repository-
  resident.
Delta/correction-z buffer citations: match already-verified pins.
Cross-generation figure (v14.471 max shard error): confirmed genuine
  via direct repository grep, not independently re-derived in full.
Scope limitation (disclosed): new producer and all new buffers/
  certificates remain Sandbox-resident; full byte-level replay awaits
  that transfer.
One loose (non-certified) rounding noted ("~7" vs ~6.5 orders of
  magnitude) -- not a defect.
No defect found.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.553
status: open
action: this auditor independently verified all arithmetic and provenance claims checkable without the Sandbox-resident output bytes, including direct hashing of all five cited Lane-A modules against the actual repository files and a from-scratch reproduction of the parameter-charge formula. No correction needed. Awaiting the compact-action payload transfer, and the next gate per v14.544/v14.552: the v14.448 direct-middle residual composition against the original seed action.
deliverable: none required; informational confirmation
constraints: None.
