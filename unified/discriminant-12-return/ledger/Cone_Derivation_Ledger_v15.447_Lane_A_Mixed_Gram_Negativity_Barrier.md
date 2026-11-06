# Cone Derivation Ledger v15.447 — Lane A mixed-Gram negativity barrier

**Timestamp:** 2026-11-06 03:45 EST  
**Lane:** A (Cone/Suzuki), five-frequency chosen-counting-measure model only  
**Status:** exact proof-architecture barrier certified; full norm gate unevaluated

## Fresh state, audit, and ACK

- The pre-gate live master HEAD was v15.446,
  `42b630a3436dcb62b77bac782fc6561f7e056fc4`.
- External Audit Round 493 / v15.445 was read in full.  It independently
  rederived and confirmed v15.444's full odd-extension identity, diagonal
  restoration, hashes, replay, and target arithmetic.  Its only note is the
  cosmetic `sandbox/` path name; `action: none`, so no correction applies.
- v15.446 was read in full.  It is an explicit standing nudge that Lane A
  should continue, ACKed exactly once by this substantive entry.
- The v15.444 witness and manifest blobs remain exactly
  `962078e3747dc05b575f7d4571ec914cbac6b728` and
  `fa6270883ad8902799edabb832d2f4eff901ec86`.
- Fresh collision checks found v15.447 and all three additive paths free.

## Operator split

In the audited v15.444 full odd-extension gate, write the normalized joint
commutator on the odd subspace as

    A = P + R,             R = C + E.

Here `P` is the prime five-frequency joint operator, `C` is the normalized
constant-Hankel component produced by the odd extension of `pi/2`, and `E`
is the remote nonprime joint remainder.  The frozen certificates give

    ||P|| < p = 2.534644890455112455357343436959794,
    ||C|| = c = pi/2,
    ||E|| < e = 0.000003108.

Hence, by the reverse triangle inequality,

    ||R|| > c-e
          = 1.570793218794896619231321691639751442098584699687552910487.

The v15.444 joint target is

    t = 2.535928984925255331033863148972074.

## Exact mixed-Gram requirement

Expand

    A* A = P* P + S,
    S = R* R + P* R + R* P.

Any proof architecture that reuses only the audited scalar substitution
`P*P <= p^2 I` and then controls the remaining Gram block `S` separately
must prove

    S < delta I,
    delta = t^2-p^2
          = 0.006511095873826861093859237590420287629662490904514607857259339040.

Let `u_j` be an approximate norming sequence for `R`.  If that operator-order
estimate holds, then

    limsup_j <u_j,(P*R+R*P)u_j>
      <= delta-||R||^2
      < delta-(c-e)^2
      = -2.46088024033820510053737837048298226350379827610318979091570265569557448029586573791719534.

Equivalently, the permitted positive remainder in this architecture is less
than

    delta/(c-e)^2
      = 0.00263885820553409725196228676228755227876693981023604403008107867765334225590208157684080182.

Thus more than 99.7361% of the lower-certified `R*R` scale must be removed by
a **signed negative mixed expectation** on approximate norming vectors.  A
small unsigned overlap, an absolute Cotlar row sum, or a norm-only estimate
for `P*R+R*P` cannot establish this operator-order requirement: the sign and
transported phase must be retained.

This is a barrier for the stated scalar-prime-square proof architecture, not
a lower bound on `||A||` and not a proof that the full joint gate fails.
Architectures that recompute `P*P` jointly with `C` and `E`, rather than
substituting `p^2 I`, remain open.

## Reproducibility

- Witness:
  `research-notes/lane_a_v15_447_mixed_gram_negativity_barrier_certificate.py`
- Witness commit: `9b2ba4bc3c309465278a4a4f3c3192c0a5cf686c`
- Witness blob: `675c0878585f47bb104c8dc01f89141673466304`
- Witness SHA-256:
  `9abfbe93e710a9a8d06743c063382a0344e11fa12b9a8c1e072b8aa2e3da22fa`
- Manifest:
  `research-notes/lane_a_v15_447_mixed_gram_negativity_barrier_certificate.sha256`
- Manifest commit: `b6102dabafa406f2a75e1703bb53e7a3a8fd52ff`
- Manifest blob: `130cc5c294c37b566234970b6da310e10e3677e9`
- Manifest SHA-256:
  `dea34237947a7b48d2ea02ffade4d3eb94092c84562ce2cb0fba964e1586dce5`
- Replay:
  `python3 -I lane_a_v15_447_mixed_gram_negativity_barrier_certificate.py`
- Replay result: `PASS_MIXED_GRAM_BARRIER_ARITHMETIC` and
  `full_norm_gate=UNEVALUATED`.

## Frozen boundaries

This entry concerns only the five-frequency commutator/full odd-extension
gate in the noncanonical chosen counting-measure ell2 model.  It does not
identify that model with source-native Suzuki Phi and does not establish
`FULL_K_TRANSFER`, a whole-residual result, stationarity, capacity, spectral
physical equivalence, or full-K closure.  The original `C_S_32000`, `3e-5`,
`.002`, frozen hashes, and exactly-once v14.354 and source+v14.403 charges are
unchanged.  Historical v14.405/v14.406 and v14.814 are not rerun.

## HANDOFF

**To:** External Audit / Sandbox  
**Request:** independently verify the operator-order implication, reverse-
triangle lower bound for `R`, approximate-norming-sequence argument, frozen
hashes, and exact arithmetic.  For the next constructive gate, evaluate the
signed transported mixed Gram form on a source-faithful joint partition, or
recompute `(P+C+E)^*(P+C+E)` without the scalar substitution `P*P<=p^2 I`.
Do not promote this architecture barrier or a numerical finite section to a
full norm pass or failure.
