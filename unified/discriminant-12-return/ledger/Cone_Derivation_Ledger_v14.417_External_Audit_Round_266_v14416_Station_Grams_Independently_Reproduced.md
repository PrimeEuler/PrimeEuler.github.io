# Cone Derivation Ledger v14.417 — External Audit Round 266: v14.416 Station Grams Independently Reproduced; D12 Audit Partially Verified

**Date:** 2026-10-15
**Track:** External Audit
**Status:** [V] v14.416 (Sandbox's exploratory Suzuki-screw station-Gram computation and D12 normalization guardrail discharge) is read in full. All files in the deposited payload are hash-verified exactly. The two heaviest, most load-bearing numerical sections (§2 ζ station Gram and scaling; §4 χ₁₂/Dedekind station Grams) are **fully independently reproduced from scratch** by copying the deposited producer scripts into a clean sandbox and re-running them — every eigenvalue, PSD verdict, and piece-wise negative-eigenvalue count matches to float precision. The D12 normalization audit (§3) is independently confirmed on its two most mathematically central claims (the χ₁₂ character table's validity and the L(1,χ₁₂) class-number value) via entirely separate classical derivations, not dependent on the sandbox's script; the remaining diagnostic checks in §3 (the Laplace-identity integral and knot-jump finite differences, which require slow uncached high-precision mpmath evaluation) were attempted but did not complete in reasonable time and are not claimed as independently verified.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–415, v13.258, v13.285, v13.753, v14.366, v14.367, v14.414, v14.416.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `0e9dcbe...` (v14.416), matching local HEAD; live ledger max was v14.416. v14.417 is next-free. No collision.

---

## 1. Deposit integrity

All 11 payload files (`EXPLORATION.md`, `arch_cache.json`, both D12 result/script pairs, `results.json`, `scaling_results.json`, both station-Gram scripts, the calibration-script copy, and `manifest.json` itself) were hash-checked directly against the manifest's declared SHA-256/byte-length values: **all 11 match exactly**. Separately confirmed `suzuki_riemann_screw_calibration.py` in the payload is byte-identical (`diff` reports no difference) to the repo's own copy at `research-notes/suzuki_riemann_screw_calibration.py`, exactly as the manifest's provenance note claims.

## 2. Full independent reproduction: ζ station Gram and scaling (§§1–2)

Copied `station_gram.py` and its calibration-script dependency into a clean directory and ran it fresh (no reuse of any deposited result). The script's own JSON output matched the deposited `results.json` in every field to float-precision (differences only at the ~1e-13 to 1e-15 relative level, consistent with floating-point summation-order noise across runs, not a real discrepancy):

- Full `g_ζ` Gram, N=32: `λ_min=0.0` (the structural basepoint zero), `λ₂=0.0074040117...` — reproduced exactly, matching the ledger's `0.007404`.
- Piece Grams: pole-only `λ_min=-7.79598...` (1 negative direction), prime-ramp-only `λ_min=-325.8436...` (12 negative directions), archimedean-only `λ_min=-235.5025...` (6), pole+archimedean `λ_min=-15.5206...` (5) — every one of these matches the ledger's table and negative-direction counts exactly.
- Zero-mass identity and knot-jump checks reproduced at the same precision.

Then copied `station_gram_scaling.py` together with the deposited `arch_cache.json` (itself hash-verified in §1, so reusing it is not trusting an unverified intermediate) and ran the full N=32/48/64/96/128 scaling sweep fresh. All five `λ₂` values reproduced exactly, and the derived `λ₂·N` products (computed independently from the reproduced `λ₂`, not copied from the ledger) match the ledger's displayed `0.237, 0.236, 0.235, 0.242, 0.245` column exactly at every N. No PSD violation at any N, matching the claim.

## 3. Full independent reproduction: χ₁₂ and Dedekind station Grams (§4)

Ran the deposited `d12_station_gram.py` fresh (using the same hash-verified `arch_cache.json`). Every reported number matches the ledger's §4 table exactly: `g_χ` N=32 `λ₂=0.047723...`/`λ_max=10.1147...`; `g_χ` N=64 `λ₂=0.026056...`/`λ_max=26.3217...`; `g_K` N=32 `λ₂=0.074993...`/`λ_max=11.6635...`; `g_K` N=64 `λ₂=0.041876...`/`λ_max=29.0638...`; all PSD with zero violations. The piece-wise non-PSD claims also match exactly: pole-only 1 negative direction, ramp-only `λ_min=-263.283...` (14 negative), doubled-archimedean-only `λ_min=-290.073...` (2 negative).

Independently recomputed (not copied) the two derived claims in the ledger prose from these reproduced numbers:
- **λ₂/λ_max ratios at N=32:** `0.07499.../11.6635...=0.00643` (K), `0.04772.../10.1147...=0.00472` (χ), `0.007404/1.7813=0.00416` (ζ) — matching the ledger's `0.0064, 0.0047, 0.0042` exactly.
- **Ordering** `λ₂(g_K) > λ₂(g_χ) > λ₂(g_ζ)`: `0.07499 > 0.04772 > 0.00740` — confirmed.

## 4. D12 normalization audit (§3): two central claims independently re-derived by separate classical methods

Rather than re-running the sandbox's own `d12_screw_audit.py` (which depends on uncached, high-precision `mpmath` evaluations and did not complete within a reasonable background-process window — the same class of cost already documented in this thread's Rounds 247/261 for other heavy mpmath/exact-arithmetic pipelines), this auditor independently re-derived the two mathematically central claims by entirely different routes:

- **The χ₁₂ character table.** Checked directly that `χ₁₂ = {1:+1, 5:-1, 7:-1, 11:+1}` is multiplicative on `(Z/12)*` (all 16 products `χ(a)χ(b)` vs `χ(ab mod 12)` checked, all consistent), and cross-checked it against the Legendre symbol `(3/p)` for `p=5,7,11` via direct computation (`pow(3,(p-1)/2,p)`) — exact match in all three cases. This independently confirms the table is the genuine real character of conductor 12 (the Kronecker symbol for discriminant 12), not merely self-consistent.
- **`L(1,χ₁₂) = log(2+√3)/√3`.** Verified via two separate classical closed forms, neither using the sandbox's `mpmath.dirichlet` call: (i) the textbook Dirichlet class-number formula for a real quadratic field, `L(1,χ) = 2h·log(ε)/√D` with `h=1`, fundamental unit `ε=2+√3`, discriminant `D=12` for `Q(√3)`, giving `log(2+√3)/√3` directly; (ii) the classical log-sine/Gauss-sum formula for an even primitive real character, `L(1,χ) = -(1/√q)Σ_{a=1}^{q-1} χ(a)·log(2 sin(πa/q))`. Both evaluate to `0.7603459963009463` / `...462` — matching the ledger's claimed value (and each other) to the last printed digit.

The remaining §3 checks (the two-way `A₁₂(t)` agreement, the `R₁₂`/knot-jump finite-difference checks, the small-`t` sign test, and the Laplace identity at `z=3`) are not independently re-verified this round; the attempted fresh run of the deposited script for these checks was still executing well past a reasonable wait and is not claimed as completed. This is a scope limit on this round, not a finding against the entry.

## 5. Verdict

```
v14.416: Sandbox exploratory deposit (Jeremy's track; no Lane A/B item
  affected), independently reviewed.
Deposit integrity: all 11 files hash-verified exactly; calibration
  script confirmed byte-identical to the repo copy.
Sections 1-2 and 4 (station Grams, scaling, D12/Dedekind Grams):
  FULLY independently reproduced by running the deposited scripts
  fresh in a clean directory -- every eigenvalue, PSD verdict, piece-
  wise negative-eigenvalue count, ratio, and ordering claim matches
  exactly.
Section 3 (D12 normalization audit): the two mathematically central
  claims (character table validity, L(1,chi_12) class-number value)
  independently re-derived via separate classical methods -- exact
  match. The remaining diagnostic sub-checks were not independently
  completed this round (slow uncached high-precision computation);
  scope limit, not a finding.
No defect found anywhere checked. This remains Sandbox's exploratory
  track; no Lane A/B item, threshold, or C_S_32000 is touched.
```

---

HANDOFF
target: sandbox
type: audit-confirmation
parent: v14.417
status: open
action: v14.416's two heaviest numerical sections (station Grams and scaling, D12/Dedekind Grams) are fully independently reproduced with exact agreement. The D12 audit's two central claims are confirmed by separate classical derivations. The remaining A12/knot-jump/Laplace sub-checks in the normalization audit were not independently re-run this round due to computation time; no defect is implied by that gap.
deliverable: none required; informational confirmation
constraints: None.
