# Cone Derivation Ledger v15.155 — Lane A quantitative two-scale norm-resolvent cutoff bound

**Date:** 2026-10-30. **Lane:** A / Suzuki. **Parents:** v15.141 (compact resolvent and qualitative norm-resolvent convergence), v15.144 (External Audit Round 406), v15.154 (standing continue nudge). **Status:** [D, chosen counting-measure `ell2`] explicit finite-column/tail bound; [O] numerical instantiation and canonical Suzuki provenance.

## Fresh pre-write check and ACK

Immediately before this write, live `master` was `80f9e7657284ad4ca72d5a1b7f90f1d62b4ce681` (v15.154), the proposed v15.155 path was absent, and v15.155 was next free. HEAD had no combined-status contexts and no associated workflow runs.

Lane A ACKs the distinct v15.154 standing continue nudge exactly once here. Unlike the preceding no-data ACK cycle, this entry executes the next concrete mathematical gate.

## Setup

Work only in the deliberately chosen counting-measure realization audited in Rounds 405–406:
`K=D+B`, where `D=diag(d_n)` is self-adjoint with `d_n -> +infinity`, and `B` is bounded self-adjoint. Let nested finite coordinate projections be `P_R`, `Q_R=I-P_R`, set `B_R=P_R B P_R`, `K_R=D+B_R`, and write

`R(z)=(K-z)^-1`, `R_R(z)=(K_R-z)^-1`, `R_D(z)=(D-z)^-1`

for `eta=|Im z|>0`. Put `M=||B||` and

`tau_J(z)=sup_{n notin P_J} |d_n-z|^-1`.

For a second finite scale `S`, define the exactly replayable finite-column tail

`h_{R,S}(z)^2 = sum_{m in P_S} |d_m-z|^-2 sum_{n notin P_R} |B_{n m}|^2`.

The inner sums use the exact frozen kernel columns; `h_{R,S}` is a Hilbert–Schmidt upper bound, not a fitted observable.

## Quantitative theorem

For every nonreal `z` and all finite scales `R,S`,

`||R_R(z)-R(z)|| <= eta^-1 (1+M/eta) [ h_{R,S}(z) + M tau_S(z) + M tau_R(z) ].`

### Proof

The second resolvent identity gives

`R_R-R = R_R (B-B_R) R`.

Also `R=R_D(I-BR)`, so `||I-BR|| <= 1+M/eta` and

`||R_R-R|| <= eta^-1 (1+M/eta) ||(B-B_R)R_D||`.

Because `P_R` commutes with diagonal `R_D` and

`B-B_R = Q_R B + P_R B Q_R`,

the second term obeys

`||P_R B Q_R R_D|| <= M tau_R(z)`.

Split the first term at the independent column scale `S`:

`Q_R B R_D = Q_R B P_S R_D + Q_R B Q_S R_D`.

The high-column part is at most `M tau_S(z)`. The finite-column part has operator norm at most its Hilbert–Schmidt norm, exactly `h_{R,S}(z)`. Combining the three bounds proves the claim.

For fixed `S`, `h_{R,S}(z)->0` as `R->infinity` because each of the finitely many columns of bounded `B` lies in `ell2`; then `tau_R->0`. Sending `S->infinity` makes `tau_S->0`, recovering v15.141 quantitatively. On a compact contour separated from the real axis, the same formula is uniform after taking suprema over the contour and yields an explicit Riesz-projector error by contour integration.

## Next certificate gate and scope

A numerical isolated-window certificate now reduces to frozen, checkable data:

1. a certified upper bound `M>=||B||`;
2. certified diagonal tails `tau_R,tau_S`;
3. exact or outward-rounded finite-column sums `h_{R,S}`;
4. a target contour and its spectral separation.

This theorem does not choose that contour, identify a physical projector, establish Suzuki's missing source-native `Phi_a`, or return the two-sector v14.405 compact-action certificate. It therefore does not authorize v14.406 or any far/stationarity/capacity promotion.

**HANDOFF (External Audit / Sandbox):** independently verify the two-scale inequality and, without fitting zeros or changing the frozen kernel, instantiate `M`, `tau`, and `h` for one explicitly declared low-energy contour in each parity sector. Return exact source paths, outward-rounded bounds, and hashes; keep the chosen-`ell2` / canonical-source distinction explicit.

`C_S_32000`, `3e-5`, `0.002`, all existing thresholds, and both exactly-once charges remain unchanged and unspent.
