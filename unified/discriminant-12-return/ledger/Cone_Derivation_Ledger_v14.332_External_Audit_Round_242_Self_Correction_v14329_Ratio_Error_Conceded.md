# Cone Derivation Ledger v14.332 — External Audit Round 242: Self-Correction — v14.329 §2(c) Ratio Error Conceded, Lane A Catch and Sandbox Resolution Independently Verified

**Date:** 2026-10-13
**Track:** External Audit
**Status:** [C] This auditor made a genuine verification error in v14.329 §2(c), caught by Lane A in v14.330 and resolved by Sandbox in v14.331. The error, the catch, and the resolution are each independently re-verified below by fresh exact-fraction arithmetic. The error is owned plainly, as the standing instruction for this thread requires ("report own errors honestly").
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–329, v14.330, v14.331.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `d3d93aa...` (v14.331), matching local HEAD; live ledger max was v14.331. v14.332 is next-free. No collision.

---

## 1. The error, stated plainly

v14.329 §2(c) computed the Region-3 window-end geometric ratios `(n/2a)²` as `0.258062...` (even) and `0.258063...` (odd), and then wrote: "Matches the stated `≤0.258` bound on both sectors, confirming the window endpoints and split point are mutually consistent as described." That is wrong on its face: `0.258062 > 0.258` and `0.258063 > 0.258` — the computed values **violate** the stated `≤0.258` bound, they do not match it. My own printed numbers already showed the discrepancy; I mischaracterized a violation as a confirmation. This was not a fabricated number — the arithmetic I actually ran was correct and is what Lane A used to catch the error — but the verdict I wrote about that arithmetic was false. Lane A's v14.330 catches exactly this.

## 2. Independent re-verification of Lane A's catch

Recomputing from scratch with exact `Fraction` arithmetic (not the floating-point check this auditor used in v14.329):

```
even: (1040384/2048006)^2 = 270599716864/1048582144009 = 0.25806248791289493...
odd:  (1040386/2048008)^2 = 270600757249/1048584192016 = 0.25806297606751544...
```

Both exact fractions match v14.330's and v14.331's stated values digit-for-digit. Both are confirmed `> 0.258` by exact rational comparison (`Fraction(258,1000)`), not floating-point rounding. Lane A's catch is correct and independently reproduced.

## 3. Independent re-verification of Sandbox's resolution (v14.331)

Two further claims in v14.331 were checked independently:

**(a) Region 2 is unaffected.** v14.331 states the Region-2 maximum ratios are `0.2499980468845367` (even) / `0.24999804688644403` (odd) — both comfortably under 0.258. Computing directly: the even-v sector uses odd-parity row indices (per v14.292 §2's "modes ≡1 mod 2"), so the last Region-2 row at or below `4R=1,024,000` is `n=1,023,999`, not `1,024,000`. `(1023999/2048006)² = 0.2499980468845367` — exact digit match. The odd-v sector uses even-parity indices, so its last row is `n=1,024,000` itself: `(1024000/2048008)² = 0.24999804688644403` — exact digit match. (This auditor's own first attempt used `n=4R` for both sectors without the parity correction and got a visibly different even-sector figure before correcting it; the parity-correct computation matches v14.331 exactly.)

**(b) The evaluator never used the rounded 0.258 constant.** v14.331 states the actual code computes, per row, an exact `Fraction` ratio `r = n²/(2a)²` and the exact geometric tail `r⁴²/(1−r)` — standard closed form for `Σ_{j≥42} r^j`, which is correct algebra (`Σ_{j≥42} r^j = r^42 · Σ_{k≥0} r^k = r^42/(1-r)` for `|r|<1`). Since each row's own exact `r` is used rather than a rounded upper bound, every row's remainder is automatically charged at that row's true ratio — which, by (a) and §2 above, tops out at the stated per-sector maxima and never actually required the false `0.258` constant for correctness. This is algebraically self-consistent and matches the established project-wide convention of exact-rational (GMP/Fraction) arithmetic for every quantity that affects a certified charge, with floating-point figures reserved for display. This auditor cannot execute `sandbox_region23_evaluator.py` directly (same byte/code-access blocker as v14.328/v14.329 §3), so this is a consistency check on the stated method, not a re-run of the code — stated as such, not glossed over.

## 4. Net effect on this audit's prior conclusions

- v14.329 §2(c)'s verdict is withdrawn and replaced by the analysis above; §2(a) and §2(b) of v14.329 (the pole-moment ratio and pre-registered-bound checks) are unaffected by this correction and stand as independently verified.
- The frozen v14.327 buffers, hashes, norms, and directed charges are **unchanged** by this correction episode — Sandbox confirms, and the algebra above is consistent with, no recomputation being required.
- The byte-transfer blocker from v14.328/v14.329 remains open and unaffected: this episode was a prose/documentation error in two ledger entries (v14.292, v14.327), not a computational one, and did not touch the still-unavailable row buffers.
- `C_S_32000` and all acceptance thresholds remain unchanged throughout.

## 5. Verdict

```
v14.329 Sec.2(c): WRONG VERDICT on correct arithmetic -- conceded.
  The computed ratios (0.258062.../0.258063...) exceed the stated
  "<=0.258" bound; this auditor incorrectly called that a match.
v14.330 (Lane A catch): independently reproduced exactly (exact fractions
  match digit-for-digit); correct.
v14.331 (Sandbox resolution): independently checked two ways --
  (a) Region-2 parity-correct maxima match exactly; (b) the exact-ratio
  tail-sum algebra is sound and renders the false 0.258 constant
  irrelevant to any actual charge. No buffer, hash, or charge changes.
Net: one prose error in two entries (v14.292, v14.327), caught by Lane A,
  resolved by Sandbox, now independently re-verified by this auditor.
  This auditor's own error in characterizing it is owned and corrected here.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-self-correction
parent: v14.332
status: closed
action: v14.330's catch and v14.331's resolution are both independently re-verified by exact-fraction recomputation; no further action needed on the ratio question. This auditor's own v14.329 §2(c) error is acknowledged and superseded by this entry. The open byte-transfer handoff from v14.328 is untouched and remains the only blocking item.
deliverable: none required; correction and re-verification only
constraints: None.
