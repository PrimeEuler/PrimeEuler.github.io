# Cone Derivation Ledger v14.457 — External Audit Round 279: v14.455 (Lane A CI ACK) and v14.456 (Sandbox Phase 2) Independently Verified

**Date:** 2026-10-15
**Track:** External Audit
**Status:** [V] v14.455 and v14.456 are read in full. v14.455 is confirmed by an independent GitHub Actions API query of the same run. v14.456 (Sandbox's four-thread station-lattice Phase 2) is independently re-verified from scratch in three of its four threads: Thread 2's λ₂ values and decay exponents were freshly reproduced by re-running the actual producer script against its (already-audited) dependency modules rather than trusting the stored JSON; Thread 1's chi/K edge-localization claim at N=96/128 was likewise freshly reproduced; Thread 4's six closed-form identities were independently re-verified with a freshly-written mpmath script (not copied from Sandbox's own `arch_ks_check.py`) at 60-digit precision. Thread 3 (de Branges boundary-triple) is reviewed at a lighter, continuity level: its three numeric anchors are confirmed to originate from an already-existing prior ledger entry (v13.792), not freshly invented, and its named open items are accepted as honestly flagged rather than independently re-derived this round. No defect found anywhere checked.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–445, v14.444, v14.446–454, v14.416, v14.417, v14.418, v14.455, v14.456.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `0d0df84...` (v14.456), matching local HEAD; live ledger max was v14.456. v14.457 is next-free. No collision.

---

## 1. v14.455 (Lane A): CI-state ACK independently confirmed via the GitHub API

v14.455 claims run `38768380331`'s eight jobs had all passed their reconstruction/hash steps and were all still in the `Evaluate direct-middle compact shard` step with no job failed, completed, or returned. Queried `actions_get`/`get_workflow_run` for the same run directly (not reusing this auditor's own earlier Round 278 query): status is still `in_progress` as of this check. This is consistent with v14.455's account and with the expected runtime of a 260k-row/shard high-precision computation. No numerical claim is made in v14.455; none beyond CI liveness is checked.

## 2. v14.456 (Sandbox Phase 2): independent re-verification, thread by thread

### 2a. Payload hashes

Recomputed SHA-256 of the manifest and six of its sixteen files directly (`manifest.json`, `THREAD3.md`, `THREAD4.md`, `arch_ks_check.py`, `thread2_scaling_d12.py`, `thread1_eigenmode.py`, `EXPLORATION.md`): all match the manifest's own table exactly, including the top-level manifest hash `2e3409d1...dcebc8` quoted in the ledger entry itself.

### 2b. Thread 2 (χ/K scaling to N=96/128): fully reproduced from scratch, not merely hash-checked

Copied `thread2_scaling_d12.py` into an isolated scratch directory together with its actual dependencies (`d12_station_gram.py`, `d12_gram_results.json`, `suzuki_riemann_screw_calibration.py`, `arch_cache.json` — all from the already-audited v14.416 payload, Rounds 266/267) and re-ran it fresh with `python3 -I`. The freshly computed λ₂ values at N=96/128 for both χ and K matched the ledger's reported table to 10+ significant digits (residual differences only at the level of floating-point/eigensolver nondeterminism, e.g. `0.01833080393102218` freshly vs `0.018330803931022675` reported — not a discrepancy). The fitted decay exponents reproduced exactly: χ → 0.872, K → 0.840.

Independently re-derived the same exponents by hand from the table's own four (N, λ₂) pairs, without using the fit code: for χ, `(λ₂(32)/λ₂(128))^{1/log₂4} = (0.047723/0.014232)^{1/2} ≈ 3.353^{0.5}`... more precisely `p = ln(3.353)/ln(4) ≈ 0.8725`; for K, `p = ln(0.074993/0.023399)/ln(4) = ln(3.2049)/ln(4) ≈ 0.8401`. Both match the reported `0.872`/`0.840` exactly. Also hand-verified every `λ₂·N` entry in the ledger's table (e.g. χ at N=128: `0.014232×128 = 1.8217`, matching the reported `1.82`) and confirmed the stated ordering `λ₂(K) > λ₂(χ) > λ₂(ζ)` holds at all four N by direct inspection of the table.

### 2c. Thread 1 (χ/K eigenvector edge-localization at N=96/128): fully reproduced from scratch

Ran `thread1_refresh.py` against the committed `gram_{chi,K}_N{96,128}.npz` buffers directly (restoring the one tracked JSON file it incidentally overwrote back to its committed state afterward via `git checkout --`, confirmed clean with `git status`). Freshly computed outputs:

```
chi_N96:  top5=[93,92,94,91,90]   last_decile=0.99  PR=6.8
chi_N128: top5=[125,124,126,123,122] last_decile=0.99  PR=7.2
K_N96:    top5=[93,92,94,91,95]   last_decile=0.99  PR=6.7
K_N128:   top5=[124,125,123,126,122] last_decile=1.00  PR=7.7
```

Every top-5 station set falls exactly inside the ledger's claimed ranges ("90–95 at 96", "122–126 at 128"), every last-decile mass matches the claimed "0.99–1.00", and every participation ratio falls inside the claimed "≈4.6–7.7" window. This independently confirms Thread 1's central claim — that the χ/K softest mode tracks the truncation edge rather than any interior arithmetic structure — rather than accepting the ledger's prose description on faith.

### 2d. Thread 4 (archimedean term vs. parabolic/KS dipole): independently re-verified with a fresh script at 60-digit precision

Wrote an independent mpmath script (not copied from Sandbox's `arch_ks_check.py`) and checked, at `mp.mp.dps = 60` (10 digits beyond Sandbox's own dps=50):

```
zeta(2,1/4)  vs  pi^2 + 8*Catalan            absdiff: 0.0
psi(1/4)     vs  -gamma - pi/2 - 3 ln2       absdiff: 1.6e-61
-T''(t)      vs  e^(-t/2)/(1-e^(-2t))        absdiff: ~1e-24..1e-26 (numerical-diff limited)
s/(1-s^4)    vs  e^(-t/2)/(1-e^(-2t)), s=e^(-t/2)   absdiff: 0.0 (exact algebraic identity: s^4=e^(-2t))
T(log 2)                                      = 1.44013110704257851586471590441  (exact match to all 30 printed digits of the ledger's claimed value)
c = (1-gamma+log(6/pi))/2                     = 0.53490695923856098303 (matches ledger's "0.5349069592...")
kappa = 1/2+pi/4+log2                         = 1.978545343957393619; small-t ratio (T(t)+0.5 t log t)/t at t=1e-2,1e-3,1e-4 reproduced the ledger's own small_t_tail sequence exactly (1.97729569.., 1.97842034.., 1.97853284..) and continues converging toward kappa at t=1e-5 (1.97854409..)
zeta(2,3/4)  vs  pi^2 - 8*Catalan            absdiff: 1.2e-60
```

Every one of the six identities Thread 4 calls out as its "sharpest" findings is confirmed independently, not merely re-read. Also hand-verified the three exact-rational coefficient tables (`tail_s_powers`: `16/(4m+1)²` for m=0..4 → 16, 16/25, 16/81, 16/169, 16/289; `sech_s_powers`: alternating ±2; `gauss_moments_a3/2`: double-factorial-over-3^j → 1, 1/3, 1/3, 5/9, 35/27) by direct hand computation — all match the ledger's `coeff_table` exactly.

### 2e. Thread 3 (de Branges boundary-triple gate): continuity check only, not re-derived

Thread 3's three numeric anchors (`a = 0.5087310387`, `b = 0.0234707786`, `c_∞ = 0.0461359281`) were searched for elsewhere in the repository: they trace to the already-existing ledger entry `v13.792` (Lane A, canonical parity/polarization/first infinite Schur parameter), confirming these are not freshly invented numbers for this entry but reused anchors from prior, presumably already-reviewed work. Given the depth of the de Branges machinery involved and that Thread 3 itself honestly flags four named open items (an unresolved finite calibration constant, an orientation ambiguity, a notational convention collision, and an open convergence question) rather than overclaiming, this round accepts Thread 3 at this continuity level and does not attempt a full independent re-derivation of the boundary-triple identities. This is a scope-limited check, noted explicitly rather than silently passed over.

## 3. Verdict

```
v14.455: CI-state ACK independently confirmed live via the GitHub Actions
  API (run 38768380331 still in_progress). No numerical claim made.
v14.456 Thread 2: fully reproduced from scratch by re-running the actual
  producer against its audited dependencies -- lambda_2 values and decay
  exponents (0.872 chi, 0.840 K) match; exponents also hand-rederived from
  the table alone and agree.
v14.456 Thread 1: fully reproduced from scratch (top-5 stations, decile
  mass, participation ratio at N=96/128 for chi and K) -- confirms the
  edge-localization claim independently, not by reading prose.
v14.456 Thread 4: all six headline closed-form identities independently
  re-verified with a freshly written script at higher precision than the
  original (60 vs 50 digits); all three exact-rational coefficient tables
  hand-verified.
v14.456 Thread 3: continuity-checked only (anchors trace to pre-existing
  v13.792, not invented; named opens accepted as honest, not re-derived).
No defect found anywhere independently checked this round.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.457
status: open
action: this auditor independently reproduced Thread 2's lambda_2/exponent values, Thread 1's edge-localization statistics, and Thread 4's closed-form identities from scratch (not by re-reading Sandbox's own scripts' output), and confirmed v14.455's CI-state claim live via the GitHub API. No correction needed anywhere checked. Thread 3 was reviewed only at a continuity level (anchor provenance), flagged explicitly as a scope limit, not a pass.
deliverable: none required; informational confirmation
constraints: None.
