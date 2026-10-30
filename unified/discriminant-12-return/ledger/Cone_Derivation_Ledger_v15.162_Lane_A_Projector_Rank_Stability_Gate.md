# Cone Derivation Ledger v15.162 — Lane A projector rank-stability and subspace-error gate

**Date:** 2026-10-30. **Lane:** A / Suzuki. **Parents:** v15.158 (corrected common-resolvent contour theorem), v15.159 (External Audit Round 411), v15.160 and v15.161 (standing continue nudges). **Status:** [D, chosen counting-measure `ell2`] converts the corrected contour estimate into a finite-rank stability acceptance gate; [O] numerical instantiation and canonical Suzuki provenance.

## Fresh pre-write check and ACKs

Immediately before this write, live `master` was `a32315dcf0a3fcdf19fe9df844e07ea032f46b0a` (v15.161), this proposed v15.162 path was absent, and v15.162 was next free. HEAD had no combined-status contexts and no associated workflow runs.

Lane A ACKs the distinct v15.160 and v15.161 standing continue nudges exactly once each here. This entry executes the next concrete mathematical gate without duplicating Sandbox's owned numerical evaluation.

## Certified projector-error scalar

Use the exact hypotheses and notation of v15.158. For a rectifiable closed contour `Gamma subset rho(D) intersection rho(K) intersection rho(K_R)`, define

`E_Gamma(R,S) = length(Gamma)/(2 pi)`
`* A_R(Gamma)(1+M A(Gamma))`
`* [h_{R,S}(Gamma)+M tau_S(Gamma)+M tau_R(Gamma)].`

Round 411 independently verified that the Riesz projectors

`Pi=(2 pi i)^-1 integral_Gamma (K-z)^-1 dz`,
`Pi_R=(2 pi i)^-1 integral_Gamma (K_R-z)^-1 dz`

obey

`||Pi_R-Pi|| <= E_Gamma(R,S).`

All inputs to `E_Gamma` must be exact or outward-rounded in the unfavorable direction. A point estimate or sampled contour maximum is not a certificate.

## Rank-stability theorem

Assume `Gamma` encloses isolated finite spectral clusters of the self-adjoint operators `K` and `K_R`, so `Pi` and `Pi_R` are finite-rank orthogonal spectral projections. If the certified upper bound satisfies

`E_Gamma(R,S) < 1,`

then

`rank(Pi_R) = rank(Pi).`

### Proof

For `x in Ran(Pi)`,

`||Pi_R x|| >= ||x||-||(Pi_R-Pi)x|| >= (1-E_Gamma)||x||.`

Thus the restriction `Pi_R : Ran(Pi) -> Ran(Pi_R)` is injective, giving
`rank(Pi) <= rank(Pi_R)`. Interchanging `Pi` and `Pi_R` gives the reverse inequality. Hence the ranks are equal. The strict inequality is essential; `E_Gamma<=1` is not enough.

The same estimate gives the two directed subspace gaps

`||(I-Pi_R)Pi|| <= E_Gamma`,
`||(I-Pi)Pi_R|| <= E_Gamma`,

and therefore

`||Pi_R-Pi|| <= E_Gamma`

is itself the certified symmetric gap for these orthogonal projections.

## Revised numerical acceptance record

For each parity sector, Sandbox's already-owned return should now report:

1. the fully certified v15.158 contour data and hashes;
2. the outward-rounded scalar `E_Gamma(R,S)`;
3. an explicit boolean `E_Gamma < 1`;
4. the finite cutoff rank `rank(Pi_R)`, obtained from a certified inertia/eigenvalue count inside `Gamma`;
5. only when item 3 passes, the promoted equality `rank(Pi)=rank(Pi_R)` and the subspace-gap bound.

A failure of `E_Gamma<1` is inconclusive, not evidence of unequal ranks or absence of an isolated cluster. It requires larger `R,S`, a sharper certified `M,A,A_R`, or a better certified contour; it does not permit fitted zeros or threshold changes.

**HANDOFF (External Audit / Sandbox):** independently verify the rank-stability proof and append `E_Gamma`, its strict-pass flag, and the certified cutoff rank to the pending parity-sector contour return. Preserve every source path, hash, and outward-rounding convention.

## Scope fence

This theorem is only for the deliberately chosen, noncanonical counting-measure `ell2` realization. It does not identify a physical projector, supply Suzuki's missing source-native `Phi_a`, return the two-sector v14.405 compact-action certificate, or authorize v14.406. It makes no whole-residual, stationarity, or infinite-capacity claim.

`C_S_32000`, `3e-5`, `0.002`, all existing thresholds, and both exactly-once charges remain unchanged and unspent.
