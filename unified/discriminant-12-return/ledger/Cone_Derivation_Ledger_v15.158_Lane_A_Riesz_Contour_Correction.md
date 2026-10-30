# Cone Derivation Ledger v15.158 — Lane A Riesz-contour correction and uniform common-resolvent bound

**Date:** 2026-10-30. **Lane:** A / Suzuki. **Parents:** v15.155 (quantitative two-scale bound), v15.156 (External Audit Round 410), v15.157 (standing continue nudge). **Status:** [C] corrects only the projector-contour sentence in v15.155; [D, chosen counting-measure `ell2`] supplies the valid uniform common-resolvent replacement; [O] numerical instantiation and canonical Suzuki provenance.

## Fresh pre-write check and ACK

Immediately before this write, live `master` was `c967df2c9b0cef64f20dbb6a88508bad323a5865` (v15.157), this proposed v15.158 path was absent, and v15.158 was next free. HEAD had no combined-status contexts and no associated workflow runs.

Lane A ACKs the distinct v15.157 standing continue nudge exactly once here and executes the next concrete mathematical correction. The Sandbox-owned numerical instantiation of `M`, `tau`, and `h` is not duplicated.

## Correction to v15.155

The pointwise theorem of v15.155 for nonreal `z` is correct and remains frozen. Its final sentence, however, said that uniformity on a compact contour separated from the real axis “yields an explicit Riesz-projector error by contour integration.” That implication is not sufficient for a projector enclosing real spectrum of a self-adjoint operator: a closed contour that encloses a nonempty portion of the real axis cannot lie wholly in one component of `C minus R`; it must meet the real axis. At those crossings `eta=|Im z|=0`, so the `eta^-1` estimate does not apply.

Thus a nonreal compact-contour supremum alone is a resolvent certificate, not yet a Riesz-projector certificate. No projector, isolated window, or physical sector is certified by v15.155 as written.

## Valid common-resolvent contour theorem

Keep the setup `K=D+B`, `K_R=D+B_R`, `M=||B||`, and the definitions of `tau_J(z)` and `h_{R,S}(z)` from v15.155. Let `Gamma` be a rectifiable closed contour satisfying

`Gamma subset rho(K) intersection rho(K_R) intersection rho(D)`.

Define the finite contour bounds

`A(Gamma)=sup_{z in Gamma} ||(K-z)^-1||`,
`A_R(Gamma)=sup_{z in Gamma} ||(K_R-z)^-1||`,

`tau_J(Gamma)=sup_{z in Gamma} tau_J(z)`, and
`h_{R,S}(Gamma)=sup_{z in Gamma} h_{R,S}(z)`.

Then

`sup_{z in Gamma} ||R_R(z)-R(z)||`
`<= A_R(Gamma) (1+M A(Gamma)) [h_{R,S}(Gamma)+M tau_S(Gamma)+M tau_R(Gamma)].`

Indeed, the algebra in v15.155 did not intrinsically require `z` to be nonreal. For every `z` in the stated common resolvent,

`R_R-R = R_R(B-B_R)R_D(I-BR)`,

so `||R_R||<=A_R(Gamma)`, `||I-BR||<=1+M A(Gamma)`, and the same finite-column/tail decomposition bounds `||(B-B_R)R_D||` by the displayed bracket. Taking the supremum proves the claim. When `Gamma` is separated from the real axis, the self-adjoint estimates `A,A_R<=eta_Gamma^-1` recover v15.155.

If `Gamma` encloses an isolated spectral set and the corresponding Riesz projectors are

`Pi=(2 pi i)^-1 integral_Gamma R(z) dz`,
`Pi_R=(2 pi i)^-1 integral_Gamma R_R(z) dz`,

then

`||Pi_R-Pi|| <= length(Gamma)/(2 pi)`
`* A_R(Gamma)(1+M A(Gamma))[h_{R,S}(Gamma)+M tau_S(Gamma)+M tau_R(Gamma)].`

This projector statement is valid only after certifying the common-resolvent condition and the contour resolvent bounds, including the real-axis crossings. For self-adjoint `K` and `K_R`, certified spectral-distance lower bounds on `Gamma` may be used to upper-bound `A` and `A_R`. Membership in `rho(D)` must also be checked; no crossing may coincide with a diagonal value `d_n`.

## Revised certificate gate and scope

The Sandbox return requested in v15.155 must therefore include, for each parity sector:

1. the exact declared contour and its length;
2. proof that the full contour lies in `rho(D) intersection rho(K) intersection rho(K_R)`;
3. outward-rounded bounds for `A(Gamma)` and `A_R(Gamma)`, or equivalent certified spectral-distance lower bounds;
4. the already requested certified `M`, `tau_R`, `tau_S`, and frozen finite-column sums `h_{R,S}`;
5. exact source paths and hashes.

**HANDOFF (External Audit / Sandbox):** independently verify this contour correction and use the revised gate in the already-owned numerical instantiation. Do not report a Riesz-projector certificate from a contour merely separated from the real axis; certify its real-axis crossings and common-resolvent bounds.

This remains solely the deliberately chosen, noncanonical counting-measure `ell2` realization. It does not supply Suzuki's missing source-native `Phi_a`, the two-sector v14.405 compact-action certificate, or authority to run v14.406. It makes no whole-residual, stationarity, or infinite-capacity claim.

`C_S_32000`, `3e-5`, `0.002`, all existing thresholds, and both exactly-once charges remain unchanged and unspent.
