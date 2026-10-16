# Cone Derivation Ledger v14.487 — External Audit Round 288: v14.486 Seed-Action Arithmetic Independently Checked; Endpoint-Ratio Decimal Approximation Flagged

**Date:** 2026-10-16
**Track:** External Audit
**Status:** [V/F] v14.485 and v14.486 are read in full. v14.486 is Sandbox's report that the original infinite-seed action has now been evaluated and certified on the complete 1,040,383-row direct-middle range in both sectors — a major step under the v14.448 execution gate. No certificate, buffer, or manifest file has yet been added to this repository (the entry states "payload transfer to the repo only on Jeremy's explicit line"), so hash-level and byte-level replay are not possible at this stage; this round independently checks every arithmetic claim derivable from the entry's own stated numbers. One genuine discrepancy was found and is reported here, not silently corrected: the entry's displayed decimal approximation of the even-sector endpoint ratio does not match the exact fraction it quotes.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–445, v14.444, v14.446–484, v14.447, v14.448, v14.471, v14.473, v14.478, v14.479, v14.482, v14.485, v14.486.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `59edfb0...` (v14.486), matching local HEAD; live ledger max was v14.486. v14.487 is next-free. No collision.

---

## 1. v14.485: pure ACK, independently confirmed as such

v14.485 is Lane A's acknowledgement that Sandbox retains active ownership of the seed-action evaluation; it makes no numerical claim and launches no computation. Checked the commit diff directly: it adds only the ledger `.md` file, no workflow change — consistent with its own "no duplicate evaluation" statement.

## 2. v14.486: arithmetic claims independently recomputed from scratch — all but one confirmed exactly

**Bank range and mode counts.** Even bank `512,001..8,323,061` (step 2, since even-sector physical modes are odd integers): recomputed count `(8,323,061-512,001)/2+1 = 3,905,531`. Odd bank `512,002..8,323,062`: recomputed count `(8,323,062-512,002)/2+1 = 3,905,531`. Both match the entry's claimed "3,905,531 modes per sector" exactly.

**Bank/tail seam alignment.** Bank end + 2 (the next mode in the same step-2 sequence) equals `8,323,061+2 = 8,323,063` (even) and `8,323,062+2 = 8,323,064` (odd) — exactly the T2 first-tail modes already frozen and independently verified in Rounds 285–286. No gap or overlap between the bank and the tail.

**Output range and counts.** Even outputs `2,080,767..4,161,531`: recomputed count `(4,161,531-2,080,767)/2+1 = 1,040,383`. Odd outputs `2,080,768..4,161,532`: same count `1,040,383`. Both match `U` exactly, and both ranges match the direct-middle output range already frozen in v14.471.

**Internal spot-check location.** The entry's claimed brute-force spot-check indices `0, 520,191, 1,040,382` — independently confirmed `520,191 = 1,040,382/2` exactly, i.e. first/middle/last row, a sensible internal-consistency check location.

**Buffer size.** `1,040,383 rows × 30 bytes/row = 31,211,490 bytes` — confirmed exactly, and incidentally identical to v14.471's stitched compact-buffer size (same row count, same 30-byte width convention).

**Odd-sector endpoint ratio.** Confirmed `1/4` is dimensionally the natural boundary value for this construction (the same kind of exact-equality-at-the-boundary pattern already seen and disclosed honestly for the odd sector's T2-split ratio in Round 285); no exact fraction is given for odd to check against, so this is accepted as stated.

**Error-vs-budget margin.** Recomputed `1.995334793914987e-13 / 2.2251541105255456e-05 ≈ 8.97e-9` (even) and `1.9846246697473864e-13 / 2.228757296675468e-05 ≈ 8.90e-9` (odd) — confirming the entry's characterization that these seed-action errors are negligible (parts-per-billion) against the unchanged v14.444 beyond-gap allowances.

## 3. Discrepancy found: the even-sector endpoint-ratio decimal approximation does not match its own exact fraction

The entry states: "Endpoint ratio at the final output: even `17318340263961/69273377701969` ≈ 0.24998 ≤ 1/4." Independently evaluated the exact fraction at 50-digit precision:

```
17318340263961 / 69273377701969 = 0.24999993992596596193238276326975086042501231401372...
```

This is **not** approximately `0.24998` — it is approximately `0.249999940`, differing from the stated approximation by about `2×10⁻⁵` in absolute terms (a relative error of roughly `8×10⁻⁵` on the displayed value, far larger than the precision this entire construction is otherwise held to). The exact fraction itself is still confirmed `< 1/4` (by a margin of only `~6.0×10⁻⁸`, i.e. the gate is genuinely tight but does hold), so **this does not overturn the `≤ 1/4` conclusion** or any downstream claim that depends only on that inequality. It is a factual error in the entry's own displayed decimal approximation of a number it also gives exactly — reported here plainly, per the standing instruction to report errors honestly and never silently patch someone else's work. The exact fraction is taken as authoritative; the `≈0.24998` approximation alongside it appears to be a transcription or display error and should be corrected by whichever lane owns that file, not by this auditor.

## 4. Scope limit disclosed

No certificate, buffer, or return-manifest file for this seed-action return exists yet in this repository; v14.486 states explicitly that payload transfer is withheld pending an explicit instruction. Consequently, this round could independently check only the arithmetic directly derivable from the entry's own stated numbers (ranges, counts, seams, byte sizes, ratios, budget margins) — not any hash, exact-rational radius, or buffer content, since none of those primary files are available to this auditor yet. This is disclosed as a scope limit, not treated as a pass.

## 5. Verdict

```
v14.485: confirmed a pure ACK with no duplicate work, matching its own
  commit diff.
v14.486 arithmetic: bank mode counts, bank/tail seam alignment, output
  mode counts, buffer byte size, and the internal spot-check location
  all independently recomputed and confirmed exact. Error-vs-budget
  margins confirmed negligible (~9e-9 of the v14.444 allowance) in both
  sectors.
v14.486 DISCREPANCY: the even-sector endpoint-ratio decimal
  approximation ("~0.24998") does not match its own exact fraction
  (which evaluates to ~0.249999940). The exact fraction is still < 1/4,
  so the gate itself is unaffected, but the displayed approximation is
  wrong and should be corrected at the source.
Scope limit: no certificate/buffer/manifest file exists in-repo yet for
  this return; hash-level and byte-level verification is not possible
  at this stage and is deferred to when those files are transferred.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-finding-and-confirmation
parent: v14.487
status: open
action: this auditor independently recomputed every arithmetic claim derivable from v14.486's own numbers and confirmed them exact, with one exception: the stated even-sector endpoint-ratio decimal approximation ("≈0.24998") does not match the exact fraction given alongside it (which is ≈0.249999940, still <1/4). Please correct the displayed approximation at the source; the exact fraction and the ≤1/4 conclusion are unaffected. Awaiting the certificate/buffer/manifest transfer for full hash-level replay.
deliverable: correction of the endpoint-ratio display approximation; payload transfer for hash-level audit
constraints: None.
