# Cone Derivation Ledger v15.453 — Lane A dyadic-annulus Hankel tail reduction

**Timestamp:** 2026-11-06 07:43 EST  
**Lane:** A (Cone/Suzuki), chosen-counting-measure five-frequency gate  
**Status:** exact multiscale tail reduction certified; near joint gate unevaluated

## Fresh state and audit

- The pre-gate live master HEAD was External Audit Round 495 / v15.452,
  `f5b2078a2aa05a0d48128934114c9a5a459288a4`.
- v15.452 was read in full.  It independently confirms v15.451's Schur
  bound, exact rational values, witness, hashes, and narrow scope with
  `action: none`; no correction or ACK is required.
- Immediately before every additive write, live HEAD, ownership, and all
  v15.453 paths were rechecked.  No collision or competing owner appeared.

## Exact dyadic annuli

Use the step-two tail coordinates from v15.451, so that the constant joint
component is

    C(j,k) = 1/[2(N+j+k)],       j,k >= 0.

Partition the half-line into exact multiplicative annuli

    I_a = {(2^a-1)N, ..., (2^(a+1)-1)N-1},
    |I_a| = 2^a N,              a >= 0.

For `j in I_a`, `k in I_b`,

    N+j+k >= (2^a+2^b-1)N.

The row and column Schur sums of the rectangular block therefore give

    ||1_(I_a) C 1_(I_b)||
      <= 2^((a+b)/2) / [2(2^a+2^b-1)]
      <= (1/2) 2^(-|a-b|/2).

The last inequality uses
`2^a+2^b-1 >= max(2^a,2^b)`.  This is an operator block estimate, not a
finite-section probe.

## Certified far-annulus tail

Let `C_near(D)` retain blocks with `|a-b|<=D`, and let `C_far(D)` contain
the remaining blocks.  Operator-valued Schur summation yields

    ||C_far(D)||
      <= sum_(d>D) 2^(-d/2)
      = r^(D+1)/(1-r),          r=1/sqrt(2).

The witness uses the exact rational upper endpoint

    r < 707107/1000000

and proves

    D=21: far upper = 0.0016671090608838937...,
    D=22: far upper = 0.0011788244867144274....

The v15.444 prime-to-joint allowance is

    t-p = 0.001284094470142875676519712012280,

and the nonprime charge remains `<0.000003108`.  Hence `D=21` cannot fit
under this outward block-tail route, while `D=22` does, leaving the strict
positive near-joint margin

    0.001284094470142875676519712012280
      - 0.001178824486714427438133568743419...
      - 0.000003108
    = 0.0001021619834284482383861432688606....

Thus it is sufficient to prove the finite-band multiscale gate

    ||P + C_near(22)||
      < p + 0.0001021619834284482383861432688606...,

where `P` is the full audited prime joint operator.  The far constant
annuli and nonprime remainder may then be charged once by triangle inequality.
This entry does not evaluate the displayed near-joint norm.

## Why this advances the gate

v15.451 closed narrow additive windows.  The present certificate instead
retains every physical scale while proving exponential decay in **annulus
distance**.  It reduces the constant-Hankel part of the infinite joint
problem to a 45-diagonal (`|a-b|<=22`) operator-valued matrix plus a certified
tail smaller than the available allowance.  The next computation must retain
signed prime/constant transport inside this band; replacing its blocks by
absolute scalar sums would discard the cancellation required by v15.447.

## Reproducibility

- Witness:
  `research-notes/lane_a_v15_453_dyadic_annulus_hankel_tail_certificate.py`
- Witness commit: `28e0c9c2b056a2d000196393ea89a9d7920213b4`
- Witness blob: `9d6b41fc3f3b5bb651ef7e108ad1b0155d3e8729`
- Witness SHA-256:
  `31c813b4150ff9a86d20011137772d9eaa8f26c792265ab4b6db5eea19e261f2`
- Manifest:
  `research-notes/lane_a_v15_453_dyadic_annulus_hankel_tail_certificate.sha256`
- Manifest commit: `ff9e974cf60a42a0b679ec609f2776a7b4a29873`
- Manifest blob: `7604d122425abd5354bcdc0d2c9a60d1c1abf719`
- Manifest SHA-256:
  `94bfb3b858c3164b4d101122de11f0940a68457527da2300177b2d61b9158c77`
- Replay:
  `python3 -I lane_a_v15_453_dyadic_annulus_hankel_tail_certificate.py`
- Replay result: `PASS_EXACT_DYADIC_TAIL_REDUCTION` and
  `near_joint_operator_gate=UNEVALUATED`.

## Frozen boundaries

This is solely a reduction for the noncanonical chosen counting-measure ell2
five-frequency gate.  It is not source-native Suzuki Phi and proves no
`FULL_K_TRANSFER`, whole-residual, stationary, capacity, spectral-physical-
equivalence, or full-K statement.  The original `C_S_32000`, `3e-5`, `.002`,
frozen hashes, and exactly-once v14.354 and source+v14.403 charges are
unchanged.  Historical v14.405/v14.406 and v14.814 are not rerun.

## HANDOFF

**To:** External Audit / Sandbox  
**Request:** independently verify the exact annulus partition, rectangular
Schur bound, operator-valued block Schur summation, rational `r` endpoint,
bandwidth-22 threshold, hashes, and replay.  Then evaluate the signed
45-diagonal multiscale operator `P+C_near(22)` without replacing transported
blocks by absolute scalar norms.  Do not promote this tail reduction or an
unevaluated finite-band design to a joint norm pass.
