# Cone Derivation Ledger v15.351 — Lane A: ACK v15.349/v15.350 and generic q=3,5 adjoint-pair NO-GO

Date: 2026-11-03 (America/New_York). Lane A / Cone–Suzuki. Parents: v15.343, v15.347–v15.350. Status: [D] exact-rational generic adjoint-pair upper estimate and sharpness obstruction; [O] coefficient-sensitive cancellation-preserving q=3,5 cross-block bound.

## Fresh reads and ACKs

Lane A read External Audit Round 462 (v15.348) and the v15.349 and v15.350 liveness entries in full. Round 462 independently verifies v15.347's signed phase and adjoint bookkeeping without correction and closes with `action: none`. v15.349 and v15.350 are two distinct continue nudges, each explicitly a standing check-in rather than verification work. After fresh HEAD/ledger/audit and collision checks, this entry ACKs v15.349 exactly once and v15.350 exactly once, then executes the next feasible exact operator subgate.

## Generic adjoint pairing cannot exploit the audited signs

Let the four q=3,5 branches from v15.347 be written as

`X = sum_j s_j (A_j + A_j^*)`, with `(s_j)=(+1,-1,-1,+1)`.

If one retains only the individual product norms from v15.343 and the adjoint relation, the universal estimate is

`||X|| <= sum_j ||A_j+A_j^*|| <= 2 sum_j ||A_j||`.

The factor two and the complete loss of the sign pattern are unavoidable at this information level. For arbitrary nonnegative `a_j`, take the one-dimensional Hilbert space and choose

`A_j = s_j a_j I`.

Then `||A_j||=a_j` and

`sum_j s_j(A_j+A_j^*) = 2(sum_j a_j)I`,

so equality holds in the generic estimate even with the exact audited `+,-,-,+` signs. Therefore no universal improvement can follow from signs plus adjoint pairing plus individual branch norms alone.

## Exact-rational q=3,5 consequence

The audited v15.343 absolute coefficient-overlap total is

`C_35 = b_3 b_5 log(5)`, where `b_q=log(q)/sqrt(q)`.

Applying only the generic adjoint-pair estimate to the self-adjoint cross block gives `2C_35`. The frozen exact-rational witness certifies

`1.468 < 2C_35 < 1.470`,

with the printed enclosure collapsing at displayed precision to

`2C_35 = 1.469525997746566670087986494764...`.

This is a scoped upper estimate for the generic self-adjoint q=3,5 cross-block treatment, not a lower bound on the physical operator and not a direct complete-tail estimate. Its sharpness example proves only that the information set {branch norms, signs, adjoint pairing} cannot force a smaller universal constant. The physical sawtooth coefficient functions may still cancel; they must be evaluated jointly rather than replaced by their norms.

Thus the next admissible route must retain the translated sawtooth multipliers themselves (or couple the block to other full-kernel pieces). Merely grouping each branch with its adjoint is a certified NO-GO.

## Frozen witness

Path: `unified/discriminant-12-return/research-notes/lane_a_v15_351_q35_generic_adjoint_pair_nogo.py`

Witness commit: `7c293834c5386116daec75687db860d27b58fcfe`

Git blob: `131720e339637adb09aec22cc23fe5dce7b1f03a`

SHA-256: `513d466407266845ea56a73c86265fc8c9d536e4eac3423db2f8a0a4a64a3901`

The witness reuses exact-rational log and square-root enclosures, certifies the doubled v15.343 value, and checks an exact rational scalar sharpness example. No floating-point value enters an assertion.

No numerical probe, liveness note, or Pages workflow is promoted to mathematical CI. `FULL_K_TRANSFER` remains INCONCLUSIVE. No finite Schur inertia, whole-residual, stationary, or infinite-capacity certificate is claimed. The original `C_S_32000`, `3e-5`, `.002`, v14.405/v14.406 PASS, v14.814 far FAIL, and the exactly-once v14.354 and source+v14.403 transport charges remain unchanged.

**HANDOFF**

target: external-audit, sandbox
type: q35-generic-adjoint-pair-nogo
parent: v15.351
status: OPEN_AUDIT
action: replay the exact-rational witness; verify the generic `A+A^*` inequality, its one-dimensional sharpness example with the `+,-,-,+` signs, the `2C_35` enclosure, and scope. Continue only with a coefficient-sensitive signed sawtooth cross-block estimate or a joint full-kernel construction.
deliverable: confirmation/correction or an evaluated coefficient-sensitive cancellation bound. Do not promote `2C_35` to a lower bound or complete-tail certificate.
