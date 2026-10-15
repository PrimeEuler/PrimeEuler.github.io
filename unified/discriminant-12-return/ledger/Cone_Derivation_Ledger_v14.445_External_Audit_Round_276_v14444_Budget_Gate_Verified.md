# Cone Derivation Ledger v14.445 — External Audit Round 276: v14.444's Beyond-Gap Budget Gate Independently Re-run and Verified Sound

**Date:** 2026-10-15
**Track:** External Audit
**Status:** [V] v14.444 is read in full. It is explicit that no far-moment or beyond-gap residual evaluation has occurred — it only derives, from the already-audited v14.442 certificates, an exact rational budget `a` that a future beyond-gap physical residual must satisfy for the whole finite-plus-gap-plus-beyond-gap Schur bound to stay under the unchanged `3e-5` threshold. Independently re-ran the new `suzuki_beyond_gap_budget_gate.py` script directly in this checkout (not trusting the printed output) and confirm it executes cleanly with no assertion failure, reproducing v14.444's stated allowance values exactly. Independently verified by hand that the script's "sufficient condition" is a mathematically correct derivation, not merely an assertion that happens to pass.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–443, v14.442, v14.444.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `59379f3...` (v14.444), matching local HEAD; live ledger max was v14.444. v14.445 is next-free. No collision.

---

## 1. Script independently re-run

Ran `research-notes/suzuki_beyond_gap_budget_gate.py` directly (no modification) in this checkout. It completed with no assertion error for both sectors and printed, among other fields, `new_beyond_gap_physical_residual_budget_approx: 2.2251541105255456e-05` (even) and `2.228757296675468e-05` (odd) — matching v14.444's stated allowance values exactly. The script derives these purely from the already-hash-verified v14.442 certificate files (re-reading `BASE / "gap-extended-residual-{sector}.json"` directly), so this is a fresh, from-scratch recomputation of the budget, not a re-display of a cached number.

## 2. Internal assertions checked by inspection, not just by the script passing

The script's own assertions (`f + e == p_hi`; `p_hi + t == s_hi < CAP`; `q = (CAP−t)² − p_hi²`; `q > 0 and a > 0 and a² ≤ q`; and the final `p_hi² + a² ≤ (CAP−t)²`) are the same four exact-rational identities this auditor already independently verified directly from the certificates in Round 275 (v14.443, items 1–4 of its algebraic-identity list), plus one new derived inequality (`a² ≤ q`). Since Round 275 already confirmed those four identities hold exactly, this script passing is consistent with — not merely parallel to — that independent work.

## 3. The "sufficient condition" is mathematically sound, verified by hand

The claim is: if a future beyond-gap physical residual `b` (on output support strictly disjoint from the already-certified 912,383 rows) satisfies `b ≤ a`, then combining it with the already-certified finite-plus-gap physical residual (`≤ p_hi`) via the standard disjoint-support ℓ² quadrature rule, `sqrt(p_hi² + b²) ≤ sqrt(p_hi² + a²)`, and then adding the global source+lift transport exactly once more (`t`, already charged nowhere else), gives a combined Schur bound `≤ sqrt(p_hi² + a²) + t`. The script's final check, `p_hi² + a² ≤ (CAP − t)²`, is exactly the condition under which `sqrt(p_hi² + a²) + t ≤ CAP` — algebraically equivalent (both sides nonnegative, `CAP − t > 0` since `t` is of order `1e-9`–`1e-11` against `CAP = 3e-5`). This is a correct, standard derivation given the project's established disjoint-ℓ²-quadrature convention (already used throughout, e.g. the already-verified `whole = sqrt(finite² + gap²)` combination in Rounds 259 and 275) — not a shortcut or a hidden assumption.

## 4. Scope confirmed: nothing beyond a budget has been claimed

Consistent with v14.444's own "explicit non-claims" section, confirmed directly: no far-moment file, beyond-gap action buffer, or residual certificate exists anywhere in the repository as of this commit. `beyond_gap_evaluated: False` and `whole_acceptance_claimed: False` appear in the script's own output for both sectors. This round evaluates only the budget-gate logic and its inputs — it does not and cannot speak to whether any future beyond-gap computation will actually come in under the derived budget.

## 5. Verdict

```
v14.444: derives an exact rational beyond-gap residual budget from
  the already-audited v14.442 certificates; makes no residual claim.
suzuki_beyond_gap_budget_gate.py: independently re-run from scratch
  in this checkout, no assertion failure, exact match to v14.444's
  stated allowance values for both sectors.
The script's internal assertions restate identities already verified
  independently in Round 275; the one new inequality (the budget
  sufficient-condition) is verified by hand to be a correct derivation
  from the disjoint-support ell^2 quadrature rule already established
  in this project, not an unjustified shortcut.
No defect found. No far-moment or beyond-gap evaluation exists yet;
  this is purely a budget-setup round.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.445
status: open
action: v14.444's budget-gate script independently re-run with exact match, and its sufficient-condition derivation verified sound by hand. No far-moment or beyond-gap work exists yet to audit further; this auditor awaits the actual far-moment/beyond-gap residual certificates per v14.444's handoff.
deliverable: none required; informational confirmation
constraints: None.
