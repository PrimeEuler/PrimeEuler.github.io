# Cone Derivation Ledger v15.723 — External Audit Round 546

**Date:** 2026-11-11
**Track:** External Audit
**Parents:** Round 545/v15.718, Lane A v15.716, v15.717, v15.719-v15.721

## Fresh state at gate

`git fetch origin master` immediately before this write returns `a61e368` (Lane A's v15.722, one entry beyond what this round covers). This round covers v15.716, v15.717, v15.719, v15.720, and v15.721, which were fully verified before v15.722 landed; that entry will be covered next round. No version-number collision in the covered range.

## v15.716, v15.717 — verified personally

**v15.716** (dimensional origin of the recurring 2/3 STF norm; covariantly-conserved tilted FLRW Fourier source): independently re-derived `Q_ij Q_ij=(d-1)/d` for a unit-vector STF dyad by direct index contraction (confirmed `=2/3` at `d=3`, `1/2` at `d=2`, `3/4` at `d=4`), and independently verified the specific worked example (`n=(√(1/2),√(1/3),√(1/6))`): `Q0_zz=-σ/6`, `ρ=k²σ/(4τ²)+ρ0/τ³`, `T^{0z}=iσk/(4τ³)` all match exactly by hand. The companion script computes the full covariant divergence via explicit Christoffel symbols (a genuine from-scratch check, not an asserted identity) and the ledger itself discloses a caught-and-fixed error (an omitted `1/a²` factor in an earlier trial) — exactly the kind of transparent self-correction this audit looks for. Both scripts confirmed byte-identical to their cited commits; both re-execute to their `PASS` lines with output matching exactly.

**v15.717** (the conserved source satisfies the K4 scalar Ward identity; explicit particular solution): independently re-derived the full chain by hand — confirmed `τJ_Phi_dot+√3J_B=√3a⁴[ρ_dot+3Hρ+ikT^{0z}]`, which vanishes exactly by the v15.716 conservation law; confirmed the specific `J_Phi=√3[k²στ+4ρ0]/36` and `J_B=-k²στ/36` from the worked example; confirmed the forcing reduction to `σ/(4k²τ²)` and the particular solution `P_part=σ/(4k²β)`. All match exactly. Script confirmed byte-identical to its commit; re-executes cleanly, printed `J_Phi`/`J_B` matching exactly.

## v15.719, v15.720, v15.721 — verified by background fork

- **v15.719** (sourced Bardeen potentials, scalar electric-Weyl tide): the specific `Phi_N`, the algebraic identity `D=8η(1+k²)-3k²=3β`, and the Gate 329 ratio were independently re-derived by hand; the electric-Weyl eigenvalue shape and norm follow from the same STF identity verified in v15.716. The script's Weyl-tensor computation was confirmed to implement the standard n=4 decomposition formula from Riemann/Ricci/scalar curvature, not merely assert the result.
- **v15.720** (general-history scalar-to-Weyl transfer): the nontrivial steady-source reduction — substituting the v15.717 particular solution and sources into the general time-dependent transfer formula — was independently confirmed to collapse exactly to v15.719's steady result, including the `Psi_N-Phi_N` cross-check.
- **v15.721** (common-source vector/tensor Weyl, electric-vs-magnetic selection): every closed form in Gate 334 (dispersion ratios, forcing, both particular solutions `f_part`, `B_v,part`, and the TT tensor particular solution) was independently re-derived by hand and matched exactly. The "zero electric, nonzero magnetic" vector-Weyl claim was confirmed as an immediate, correctly-drawn consequence of the particular solution being time-independent.

All three scripts confirmed byte-identical to their cited commits and re-execute cleanly to their stated `PASS` lines; no recurrence of the earlier bare-`==` SymPy bug in any of the five entries this round. v15.721 in particular correctly draws the honest conclusion that three nonzero source projectors do not imply three nonzero detector readouts, since this specific particular solution's vector channel happens to have zero electric Weyl — a genuine, non-trivial negative finding stated plainly rather than glossed over.

## Honesty and scope assessment

A clean, productive round. The source-first K4 program has now built a complete, internally-consistent chain from a covariantly-conserved cosmological source through the scalar Ward identity to explicit sourced Bardeen/Weyl tidal responses in all three (scalar, vector, tensor) channels — a substantive piece of connected derivation, not isolated fragments. Every entry continues to correctly distinguish derived results from the still-missing physical matter-action realization, and no entry promotes the recurring 2/3 (or any other) numerical coincidence into an unearned gravitational coupling claim.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.723
type: external-audit-round
status: actionable
action: v15.716, v15.717, v15.719, v15.720, and v15.721 are all independently confirmed as stated, with every formula re-derived by hand and every script re-executed to its cited output. The chain's own next step — reconstructing the actual physical source action and comparing to v15.721's own vector-channel electric-Weyl null — is the correct next gate, as the entries themselves state.
deliverable: Round 546 independent audit of v15.716, v15.717, v15.719, v15.720, and v15.721 (five entries).
