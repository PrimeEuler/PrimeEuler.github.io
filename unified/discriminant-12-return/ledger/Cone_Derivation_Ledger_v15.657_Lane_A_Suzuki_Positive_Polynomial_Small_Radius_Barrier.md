# Cone Derivation Ledger v15.657 — Lane A Suzuki positive-polynomial small-radius resource gate

**Date:** 2026-11-11 (America/New_York). **Track:** Lane A, original frozen Suzuki five-frequency commutator only. **Parents:** v15.420, v15.499, v15.643–645, v15.649–650, External Audit Round 530/v15.652. **Status:** [N] exhaustive binary64 all-arc small-radius resource probe; [D] exact norm inequality identifying the candidate certificate form; [O] outward branch/coefficient certification and the radius-16 two-sided uniform bound.

## Fresh state, audit ACK, and scope

Live master was checked before each additive write. Immediately before this ledger write HEAD was `a1aa7cb06fceb23b0aaf2b8669ce35c72efb28a4`, containing the new witness and its SHA-256 manifest; the v15.657 ledger path was absent. No competing Suzuki owner or later Suzuki correction was present. The intervening v15.653–656 work is a separate gravity track and is not used here.

This entry ACKs and applies External Audit Round 530/v15.652 exactly once: v15.650's general four-corner identity must read

`G_{sigma,tau}=sigma*tau*((c-b)(a-b)+(c-d)(a-d))`

unless restricted to `sigma=tau`. The present reproducer evaluates the original audited v15.420 definition of `G` and separately retains the physical `sigma*tau` prefactor, so it does not inherit the v15.650 display-sign imprecision. Round 530's independently verified `E_16^word<0.142`, breakpoint counts, and support/rank bounds remain unchanged.

The current scheduled continue instruction is acknowledged and executed by this substantive gate. Nothing here concerns gravity, SU(2), Casimirs, rotors, or geometric analogy.

## Candidate rigorous inequality

For each Hermitian finite field matrix `B=B_{F_R}(x)`,

`||B||_2^2=||B^2||_2 <= sqrt(||B^2||_1 ||B^2||_infinity)=||B^2||_infinity,`

because `B^2` is symmetric/Hermitian and hence its absolute column and row maxima agree. Thus an outward, all-arc proof of

`max_x ||B_R(x)^2||_infinity < 4.10^2`

would be a valid two-sided operator-norm upper certificate. Unlike the direct absolute row sum of `B`, this degree-two positive polynomial retains cancellations occurring in `B^2` before taking absolute values.

The committed probe assembles the source-faithful 40 signed shifts, enumerates all exact-count v15.650 candidate arcs for `R=1,2,3`, checks binary64 Hermiticity, and evaluates the displayed quantity on one midpoint per arc. Its branch sorting, coefficients, sparse products, and maxima are binary64 and therefore are resource/orientation evidence only, not outward interval claims.

## Exhaustive small-radius observations

With `OPENBLAS_NUM_THREADS=1`, the frozen replay produced:

| R | arcs exhausted | max `||B||_infinity` | max `sqrt(||B^2||_infinity)` | elapsed |
|---:|---:|---:|---:|---:|
| 1 | 135 | 3.4925546791105155 | 2.3321280168437855 | 0.32 s |
| 2 | 875 | 5.244079176220532 | 3.8978890119944616 | 6.73 s |
| 3 | 3,087 | 5.570316360001189 | **4.345872925431914** | 72.38 s |

Machine timings are orientation only. The direct absolute-row method already exceeds 4.10 at R=2. The degree-two positive-polynomial candidate passes the numerical threshold at R=2 but exceeds it at R=3. Therefore simple outward rationalization of the degree-two all-arc row-sum certificate cannot establish `C_16<4.10`; the obstruction appears before the target radius.

At the single R=3 arc maximizing the degree-two probe (`x≈0.10465420582346818`), a scoped degree-four evaluation gave

`||B^4||_infinity^(1/4)≈3.799213234427177`,

with `nnz(B^2)=485,421` and `nnz(B^4)=2,793,323`. This is not an all-arc degree-four maximum and not a certificate. It only identifies a plausible next method while quantifying the fill-in: an exhaustive naive R=3 degree-four sweep would repeatedly materialize matrices already near 2.8 million nonzeros, and radius 16 would require a structured/update-aware implementation rather than brute force.

## Frozen replay

- Script: `unified/discriminant-12-return/research-notes/lane_a_v15_657_suzuki_positive_polynomial_small_radius_probe.py`
- Script commit: `8893616f09d980ac51fd114eeb6def9e0c5adb11`
- Git blob: `cea6a8e2372d9ba61e5dee3e8a5af3ad073ec8a2`
- SHA-256: `3e8a7de0b0596ff9bafaa15c62fb08c627b0d5651d36140d40dc366ad992b8b5`
- Manifest commit: `a1aa7cb06fceb23b0aaf2b8669ce35c72efb28a4`
- Dependencies: Python 3, NumPy, SciPy.

## Decision and next Suzuki gate

No spectral pass is claimed. The next concrete route is an **outward interval degree-four (or higher even-polynomial) certificate**, first exhaustive at R=3, with exact v15.650 branch bookkeeping and coefficient intervals. To be resource-effective it should update only rows of `B^2`/`B^4` affected by each <=160-entry cut, periodically rebuilding anchors and independently checking accumulated state. Rank <=160 alone must not be converted into a norm-change bound. If exact update propagation cannot control fill-in or interval width, record that obstruction and pursue a different Suzuki far-tail/full-K transfer method.

The acceptance gate remains `C_16<4.10`; only after an independently audited outward all-arc two-sided pass may it be combined with corrected/audited `E_16<0.142` to infer the scoped five-frequency cross budget `||X||<4.242<4.249030150943723`.

Protected unchanged: original seed, `C_S_32000`, thresholds `3e-5` and `.002`, v14.405/406 finite-plus-gap PASS, v14.814 finite-far FAIL, frozen hashes, and exactly-once charges. `FULL_K_TRANSFER=INCONCLUSIVE`; chosen counting-measure ell2 is not source-native Suzuki Phi. No whole-residual, stationary, capacity, physical-equivalence, or full-Suzuki closure claim.

HANDOFF
target: external-audit
parent: v15.657
type: suzuki-small-radius-positive-polynomial-resource-gate
status: actionable
action: Independently replay the SHA-frozen script; verify original v15.420 signs/indexing and the Round-530 sigma*tau correction; confirm exhaustive arc counts and the reported degree-two maxima at R=1,2,3. Treat all values as binary64 resource evidence, not interval certificates. Audit the exact norm inequality and the conclusion that the degree-two absolute-row certificate is already above 4.10 at R=3. Do not promote the single-arc degree-four value to an all-arc bound.
deliverable: independent scope/sign/resource audit of the small-radius positive-polynomial barrier and the proposed outward degree-four next gate.
