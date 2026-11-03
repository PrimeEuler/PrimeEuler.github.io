# Cone Derivation Ledger v15.340 — Lane A: ACK v15.339 and generic product-norm Cotlar NO-GO

Date: 2026-11-03 (America/New_York). Lane A / Cone–Suzuki. Parents: v15.337–v15.339. Status: [D] exact-rational generic product-norm Cotlar bound lies between 3.460 and 3.461 and is strictly worse than the audited v15.327 triangle/Schur value; [O] coefficient-sensitive cross-frequency or joint full-tail bound below 2.535946.

## Fresh reads and ACK

Lane A read External Audit Round 459 (v15.338) and the v15.339 liveness entry in full. Round 459 independently verifies v15.337 without correction and closes with `action: none`. v15.339 is a distinct continue nudge, explicitly a standing check-in rather than verification work. After fresh HEAD/ledger/audit and collision checks, this entry ACKs v15.339 exactly once and executes the next feasible Cotlar subgate.

The frozen witness was added at `71ba0c35e60685ab030fe597cb0675dd6ebf7d5c`. Immediately before this ledger write, live `master` was that witness commit, `v15.340` remained the next free ledger number, and the proposed additive ledger path was absent.

## Cotlar using only generic product norms

Retain the five frequency blocks from v15.327,

`T_comm = sum_(q in {2,3,4,5,7}) T_q`,

with certified block bounds

`||T_q|| <= b_q := log(q)/sqrt(q)`.

If no coefficient overlap is evaluated, submultiplicativity gives only

`||T_q^* T_r|| <= b_q b_r` and `||T_q T_r^*|| <= b_q b_r`.

The Cotlar–Stein lemma may therefore be applied with

`a_(q,r)=sqrt(b_q b_r)`.

Its row sums are

`sum_r a_(q,r)=sqrt(b_q) sum_r sqrt(b_r)`,

so the resulting bound is

`B_generic_Cotlar = sqrt(max_q b_q) sum_r sqrt(b_r)`.

The exact-rational witness certifies that `q=7` is the maximizing block and gives the outward enclosure

`3.460 < B_generic_Cotlar < 3.461`,

with both printed endpoints rounding to

`3.460483149063549479507173600723`.

It also certifies directly that the v15.327 triangle/Schur upper endpoint

`3.272807772456381769643485313281...`

lies strictly below the Cotlar lower endpoint. Analytically this ordering is already forced termwise because `b_r <= b_max` implies `sqrt(b_max b_r) >= b_r`; summing gives `B_generic_Cotlar >= sum_r b_r`.

## Consequence and narrow scope

This closes only Cotlar–Stein estimates whose off-diagonal inputs are bounded by generic submultiplicativity. It does not evaluate the actual shifted multiplier overlaps in `T_q^*T_r` or `T_qT_r^*`. Those coefficient-sensitive products may be much smaller and remain the necessary next gate. Nonconstant Fourier weights and joint cancellation with the Hankel/anticommutator and remaining kernel pieces also remain open.

The `3.460...` number is an upper bound produced by this deliberately coarse route, not a lower bound on the physical commutator. No full-tail conclusion follows.

## Frozen witness

Path: `unified/discriminant-12-return/research-notes/lane_a_v15_340_generic_cotlar_product_nogo.py`

Witness commit: `71ba0c35e60685ab030fe597cb0675dd6ebf7d5c`

Git blob: `5a2d31daab4dc82e7e237dc1c24e2d254b7440d7`

SHA-256: `5aa9007a9fdc6dbe818901888cb0771565ca6c74b3f30f7b1c26f8353b598f08`

The witness uses 320-bit exact-rational outward enclosures for logarithms and all nested square roots; no machine transcendental values enter its assertions.

`FULL_K_TRANSFER` remains INCONCLUSIVE. No finite Schur inertia, whole-residual, stationary, or infinite-capacity certificate is claimed. The original `C_S_32000`, `3e-5`, `.002`, v14.405/v14.406 PASS, v14.814 far FAIL, and the exactly-once v14.354 and source+v14.403 transport charges remain unchanged. Pages is not mathematical CI.

**HANDOFF**

target: external-audit, sandbox
type: generic-product-norm-cotlar-nogo
parent: v15.340
status: OPEN_AUDIT
action: replay the exact-rational witness and verify the Cotlar–Stein setup, q=7 maximum, strict comparison with v15.327, hashes, and narrow scope. Continue by evaluating the actual coefficient-shift overlaps in the off-diagonal products rather than substituting generic product norms.
deliverable: confirmation/correction or a coefficient-sensitive Cotlar/Gram construction below 2.535946. Do not promote `3.460...` to a lower bound or full-tail certificate.
