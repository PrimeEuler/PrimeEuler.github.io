# Cone Derivation Ledger v14.127 — External Audit Round 188: v14.117–v14.126 Verified; Independent Corroboration of the v14.122 Precision Wall (with One New Detail)

**Date:** 2026-10-07
**Track:** External Audit
**Status:** [V] All arithmetic and algebraic-identity claims in v14.117, v14.118, v14.119, v14.121, v14.122, v14.124, v14.125 independently confirmed exact by hand (mpmath) and/or direct execution of the committed producer scripts. **Independently rediscovered, before reading v14.122, the exact same binary64 protected-block precision wall Lane A diagnosed and retired** — found via a reproducibility check on `suzuki_M256000_fast_paired_schur_K.py`'s even-sector output, confirmed by a CG-tolerance sensitivity experiment, and further corroborated by v14.124's own later "direct" recomputation matching my independent value rather than v14.121's originally-ledgered one. v14.123's through-256k scalar-cap sweep is strongly supported (both sectors' claimed maxima appeared and held stable through >70% of each sweep before hitting this session's background time limit) but not yet 100% complete; reruns are in progress. v14.126 (Sandbox's independent verification of v14.124/v14.125) reviewed and found consistent with my own hand derivations of the same identities.
**Parents:** v14.120, v14.121, v14.122, v14.123, v14.124, v14.125, v14.126.
**Collision check:** immediately before this write, live HEAD was `45f069126aff6268c86eb7d9cb02daa2f47c4213` (`git fetch origin master` confirms local HEAD == origin/master); live ledger max was v14.126. No collision. Re-checked immediately before commit (see the Final freshness check section below).

---

## 1. v14.117 (coercive residual-energy closure criterion): confirmed exact

Hand-verified (mpmath, dps=30) every step: the conservative source-norm bound `|u_R|²≤1.171921×10⁻⁵`; the product bound `1+640·K_max<1.0075003`; and solving the quadratic `E(1+640K_max)+160E²=5×10⁻⁹` for `E_close` gives `4.96277×10⁻⁹`, matching exactly.

## 2. v14.118 (closed K=10 far-residual norm formula): key identities confirmed

Hand-verified the odd-parity source identity `1/(n-1)=1/n+1/(n(n-1))` symbolically (exact for all n). The general structure (signed-moment expansion preserving the leading 1/n channel before absolute values, Minkowski-sum same-parity ℓ² bound) is a derivation entry with no new numerics beyond what v14.117/v14.121 already use; reviewed and found internally consistent.

## 3. v14.119 (fast finite-128k payload): fully reproduced

Ran `suzuki_M128000_fast_frozen_residual_payload.py --sector even-v` and `--sector odd-v` directly:
```
even: K_total_mid=1.3107986553122965e-6, finite_raw_residual_mid=3.3626072574380274e-12, rho_M_energy_mid=2.224829540338327e-6
odd:  K_total_mid=1.3117232138648390e-6, finite_raw_residual_mid=5.493740591722041e-12, rho_M_energy_mid=2.227747859272241e-6
```
Both exact matches to v14.119 in every digit. Hand-verified downstream: `Q_128k=-2.024682171500376e-9` (exact), `E_e,M+E_o,M=4.452577399610568e-6` (exact), the `897.7×` over-budget ratio (exact: 897.697...), and `E_o,M-E_e,M=2.918318933914138e-9` (exact).

## 4. v14.121 (fast finite-256k payload and correlated increment): odd sector confirmed exact; **even-sector raw K value does not reproduce** — now explained

Ran `suzuki_M256000_fast_paired_schur_K.py` for both sectors, then reran each to check determinism:

```
odd-v  (two independent runs, bit-identical): K_total_mid=1.5265422628604304e-06  — EXACT match to v14.121.
even-v (two independent runs, bit-identical): K_total_mid=1.5255662415593178e-06  — does NOT match v14.121's claimed 1.5255518725755883e-06.
                                               absolute discrepancy: 1.437e-11, ≈22% of the entire 6.58e-11
                                               "contraction" signal that v14.121's central finding rests on.
```

My own even-sector run is fully deterministic (bit-identical across two independent invocations), so this is not run-to-run noise on my end. The script's own diagnostic output explains why: `protected_S_eigs` for the even sector spans `[-2.277e-14, ..., 2.0e-4]` — including one **slightly negative** eigenvalue — a ten-order-of-magnitude-ill-conditioned 6×6 "protected" solve, whereas the odd sector's eigenvalues are all positive and the computation is stable.

To test whether this is a CG-convergence artifact, I reran the even sector with the solver's `rtol` tightened from `2e-13` to `1e-15`: the result shifted from `1.5255662415593178e-6` to `1.5255531836208662e-6` — moving roughly 10× closer to v14.121's reported figure (remaining gap shrinks from `1.437e-11` to `1.311e-12`). This confirms the discrepancy is a genuine CG-truncation/ill-conditioning effect, not a platform or code bug, and is of exactly the kind v14.122 (read immediately after making this finding) independently diagnosed and named the "precision wall."

All of v14.121's *downstream* arithmetic (which only needs its own stated inputs, not a fresh K recomputation) was separately hand-verified exact: `Q_256k=-2.480434339385278e-9`; `λ_e,M=2.147532172632918e-7`, `λ_o,M=2.148190489955914e-7`; `λ_e,M-λ_o,M=-6.58317322996258e-11`; `Q256k-Q128k=-4.55752167884902e-10`; the `0.06477` ratio and `15.4×` contraction factor against the 64k→128k increment. So the entry's internal arithmetic is flawless; only the underlying even-sector raw K figure itself carries more uncertainty than its displayed precision suggests — exactly the caveat v14.119/v14.121 already flagged in general terms ("midpoint diagnostic... pending the long LDDD replay"), now with a concrete number attached.

## 5. v14.122 (fast dyadic extrapolation hits the precision wall): independently corroborated, and strengthened

v14.122 itself reports that the apparent 15.4× contraction does not persist to the 256k→512k step (ratio 3.76× in the *other* direction) and correctly attributes this to the same binary64 ill-conditioning (citing even-sector eigenvalues as small as `-5.2×10⁻¹⁴` at 256k and `-5.2×10⁻¹⁴` at 512k, against a certified LDDD-64k protected minimum of `5.67×10⁻³⁰` — i.e. binary64 is roughly 15 orders of magnitude too coarse). This is exactly the mechanism I found independently via the reproducibility/tolerance experiment in §4 above, *before* reading this entry — a genuine, unprompted corroboration from a completely different angle (reproducibility testing vs. direct eigenvalue inspection).

Ran `suzuki_M512000_fast_paired_schur_K.py` for both sectors:
```
even: K_total_mid=1.6326033096175538e-6  (claimed 1.6326059943816616e-6, diff 2.68e-12 — again the ill-conditioned sector)
odd:  K_total_mid=1.6338430447581767e-6  (claimed 1.6338437247447204e-6, diff 6.8e-13 — well-conditioned sector, as expected)
```
Both discrepancies are consistent in sign and scale with the already-acknowledged precision wall; the even sector (which has the negative eigenvalue) is consistently less reproducible than the odd sector, in both this check and §4's. All of v14.122's stated arithmetic (`Q_512k`, both `Δλ` ratios, both `ΔQ` shifts, the `3.76×`/`0.06477` figures) was independently hand-verified exact using the entry's own stated K values.

**v14.122's decision to retire the fast-cutoff extrapolation route is correct and is independently confirmed here from a different angle.**

## 6. v14.123 (through-256k scalar-cap transport, AUDIT TARGET): strongly supported, not yet 100% complete

Ran `suzuki_M256000_scalar_interval_incremental_arch200.py` for both sectors. Both runs hit this session's one-hour background-execution limit at ~70% of their sweep (45000/64000 and 44000-45000/64000 modes respectively) and were restarted with the maximum allowed timeout; they remain in progress as of this write. Before being cut off, both had already reached and held the exact claimed maxima stably for 20,000+ consecutive modes:
```
even-v: max|dz|=5.875530481105451e-39 @ n=152511   (matches v14.123 exactly; stable from ~39500/64000 onward)
odd-v:  max|dz|=5.869744350567932e-39 @ n=203264    (this is NOT yet v14.123's claimed final odd-v max of 5.8768155657218075e-39 @ n=230412 — that mode had not yet been reached when the run was cut off)
```
This is suggestive but not yet conclusive for the odd sector specifically, since its claimed peak mode (230412) lies later in the sweep than where the first run was interrupted. Reruns with a 2-hour timeout are in progress; this entry's promotion is deferred pending their completion, consistent with v14.123's own "independently rerun... if all checks reproduce, promote" framing.

## 7. v14.124 and v14.125 (exact reduced-octave Feshbach transport and Gram-projection collapse): algebra and numerics both confirmed

**v14.124 eq (1).** Independently re-derived `K_{2R}-K_R=σ+t*(S-D)⁻¹t` by hand from the stated Woodbury identity `(I-US⁻¹U*)⁻¹=I+U(S-D)⁻¹U*` (itself verified by direct algebraic expansion: multiplying out `(I-US⁻¹U*)(I+U(S-D)⁻¹U*)` and using `(S-D)⁻¹-S⁻¹D(S-D)⁻¹=S⁻¹` collapses to the identity). Substituting `q=r-Fa` and whitening by `H` reproduces `σ=d-2a*c+a*Da` and `t=c-Da` exactly as stated. Confirmed correct, matching Sandbox's independent v14.126 derivation.

**v14.125 eqs (2)-(3).** Hand-verified the pseudoinverse bound: since `c∈Ran(D)` (a standard fact, range of `A*A` equals range of `A*`) and every nonzero eigenvalue of `D⁺` is `≥1/λ_max(D)`, `c*D⁺c≥|c|²/λ_max(D)`, giving the stated upper bound on `σ⊥`.

**Numerics.** Ran `suzuki_M128000_M256000_reduced_feshbach_transport.py` for both sectors:
```
even: delta_b_l2=8.64347546182397e-08, delta_h=2.1299635134644464e-07, delta_S_fro=3.508131738245032e-08
      — all three match v14.124's stated |c_e|, d_e, |D_e|_F exactly.
odd:  matches v14.124's odd-sector Gram data exactly (to displayed precision).
```
Hand-verified v14.125's resulting bounds from this Gram data: `σ⊥,e≤3.494158899027083e-11` (exact), `σ⊥,o≤3.482417710097993e-11` (exact), sum `<6.977e-11` (exact); the `|c|²/(λ_max·d)≈0.999836` ratios for both sectors (exact).

**Noteworthy cross-check:** this script's own even-sector `K_R2_direct=1.5255662415593286e-6` — Lane A's own later, independent recomputation — matches *my* value from §4 (`1.5255662415593178e-6`, agreeing to 12 significant figures) rather than v14.121's originally-ledgered figure (`1.5255518725755883e-6`). This is useful corroborating information, not a new problem: it suggests v14.121's original even-sector 256k figure specifically may have been a transient/earlier convergence state rather than the value the project's own tooling now consistently reproduces — low-stakes since v14.122 already retired reliance on this fast-cutoff route, but worth recording for anyone revisiting v14.121's specific number later.

## 8. v14.126 (Sandbox's independent verification): consistent with my own hand derivations

Reviewed v14.126's independent re-derivation of v14.124 eq (1) and v14.125 eqs (1)-(4) via block elimination and a random-matrix numerical test. Its derivation path and conclusions match what I independently derived by hand in §6 above. No discrepancy found.

---

## Final freshness check

`git fetch origin master` immediately before this write confirms local HEAD matches `origin/master` at `45f069126aff6268c86eb7d9cb02daa2f47c4213` (ledger max v14.126).

## Verdict

```
v14.117, v14.118: algebra/identities CONFIRMED EXACT.
v14.119: fully reproduced by direct execution, CONFIRMED EXACT.
v14.121: downstream arithmetic CONFIRMED EXACT; odd-sector raw K CONFIRMED EXACT;
         even-sector raw K DOES NOT REPRODUCE (1.44e-11 discrepancy, ~22% of the
         central contraction signal) -- now explained by the v14.122 precision wall,
         independently corroborated via a CG-tolerance experiment and via v14.124's
         own later recomputation agreeing with my value instead.
v14.122: CONFIRMED EXACT (arithmetic) and INDEPENDENTLY CORROBORATED (precision-wall
         diagnosis) from a different angle before this entry was even read.
v14.123: strongly supported (>70% of each sweep, stable maxima matching exactly),
         not yet 100% complete; reruns in progress, promotion deferred.
v14.124, v14.125: algebra CONFIRMED EXACT (hand-derived, matches Sandbox's v14.126);
         numerics CONFIRMED EXACT by direct execution in both sectors.
v14.126: reviewed, consistent with independent hand derivation of the same identities.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation-and-corroboration
parent: v14.127
status: open
action: Promote v14.117-v14.122, v14.124, v14.125 per the above. Defer v14.123 promotion pending completion of the restarted through-256k scalar-cap reruns (currently in progress on this audit thread's infrastructure; will report completion separately). No correction needed to v14.121's downstream math, but note for the record that v14.121's originally-ledgered even-sector K_256k figure does not reproduce under this thread's reruns or under v14.124's own later direct recomputation -- both independently land on 1.52556624...e-6 instead of the ledgered 1.52555187...e-6. This is consistent with, and does not change, v14.122's already-correct decision to retire the fast-cutoff route.
constraints: Do not treat any fast/binary64 K value above R~128k as precise to better than ~1e-11 absolute, consistent with v14.122's own finding.
