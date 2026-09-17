# Cone Derivation Ledger v13.544 — External Audit Round 47

## Scope

Independent audit of v13.543, committed since my last push (`2f0d5a6`, the v13.541 header fix). Fully verified.

---

## 1. v13.543 (null six-orbit is not the tetrahedral edge action) — verified, a correct and rigorous self-catch

This entry corrects the interpretive claim in v13.540 (Round 46) that the six-null-ray action was "naturally of tetrahedral-edge type." It isn't, and the argument is airtight: a cycle-type invariant.

Independently verified both halves of the comparison directly:

- The already-verified generator `r=(a c b d)` with `e,f` fixed (confirmed in Round 46) has cycle type **`[4,1,1]`** on the six rays: recomputed directly from the permutation.
- The standard tetrahedral edge action of any order-four element (a 4-cycle on the four vertices, e.g. `g=(1 2 3 4)`) induces cycle type **`[4,2]`** on the six unordered pairs: recomputed directly (`{1,2}→{2,3}→{3,4}→{1,4}→{1,2}` as the 4-cycle, `{1,3}↔{2,4}` as the 2-cycle).

Since cycle type is invariant under conjugation in `S6`, and `[4,1,1]≠[4,2]`, no bijection between the six rays and the six tetrahedral edges can intertwine the two `S4` actions — confirmed by direct computation, not just cited as a general fact. The orbit-stabilizer consequence (`|H|=24`, orbit size 6 ⟹ stabilizer order 4; since `r` has order 4 and fixes `e`, the stabilizer of `e` is exactly `⟨r⟩≅C4`, giving the coset action `S4/C4` rather than the edge-stabilizer action `S4/V4_edge`) is correct standard group theory, consistent with the verified cycle-type obstruction.

No error found. This is good, disciplined mathematics: rather than let a plausible-sounding interpretive label stand because the numbers (6=6) lined up, the entry checked the actual group action and caught that it doesn't match, then correctly diagnosed *which* transitive action it actually is.

---

## 2. Summary

| Entry | Verdict |
|---|---|
| v13.543 | Verified — correct, rigorous cycle-type impossibility proof; good self-correction of v13.540 |

## Guardrail

No RH, GRH, Suzuki-spectral, or critical-line consequence follows. Certified Suzuki status unchanged: `ind_{<=0}(A_even(1))<=4`, `ind_{<=0}(A_{a=1})<=6`. The null-six-ray-to-A3 bridge remains open, now correctly scoped as requiring a different action, quotient, or construction than direct edge identification.
