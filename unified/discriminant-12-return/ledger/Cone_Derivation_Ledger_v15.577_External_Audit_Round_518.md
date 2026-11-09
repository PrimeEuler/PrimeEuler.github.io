# Cone Derivation Ledger v15.577 — External Audit Round 518: Lane A's Zeeman-style open-quarter-shell transition network (v15.576) independently verified in full

**Date:** 2026-11-09
**Track:** External Audit
**Status:** [B] Lane A's v15.576 builds candidate Hermitian Hamiltonians (original `J` ladder, alternative half-step `B` ladder, and their combination) on the odd-quarter open shells characterized in v15.572–575, and derives exact finite-dimensional transition-strength, spectrum, and short-time leakage-probability predictions — while explicitly declining to call any of it a physical interaction, emission, or chirality selection. Every numeric claim in the entry — edge weights for both `J` and `B` ladders at `j=3/4` and `j=5/4`, the mirror-symmetric "excluded outgoing" escape weights at both ends of the `j=3/4` shell, the `-gJ_x` and `-hB_x` spectra, and the short-time opposite-parity transition probability — is independently re-derived from scratch and confirmed exactly.
**Parents:** v15.575 (Round 517), v15.576.

---

## Fresh pre-write check

`git fetch origin master` returns `1eaf506` (v15.576), identical to the head just read. `v15.577` is next free; no collisions.

## v15.576 — the Zeeman-style transition network

**What this builds.** On the odd-quarter open shell (basis `m_i=-j+i/2`), the entry defines a Hermitian candidate Hamiltonian `H=\omega M-g(J_++J_-)/2-h(B_++B_-)/2`, combining the original defective ladder `J` with the alternative half-step ladder `B` from v15.574, and derives exact predictions for edge couplings, spectra, and short-time cross-parity leakage — all explicitly as finite-matrix mathematics, with the entry itself repeatedly flagging that none of it is a physical emission, coupling strength, or selection rule without additional, unsupplied physical input.

**Independent re-derivation of every numeric claim, built from scratch (no committed witness script exists for this entry; the reproducer is referenced only as an external, non-committed artifact).**
- *`j=3/4` edge weights.* Rebuilt the `4×4` `J_+` matrix directly from the AM–GM weight formula: both within-chain edges (`i=0\to2`, `i=1\to3`) have squared weight `3/2`, matching exactly.
- *The mirror-symmetric "excluded outgoing" weights.* Verified that chain 0's excluded upward (`J_+`) escape from its top node (`i=2`, `m=1/4`) has squared weight `(j-m)(j+m+1)=1`, and — the subtler point, requiring care to locate correctly — that chain 1's excluded *downward* (`J_-`) escape from its bottom node (`i=1`, `m=-1/4`), using the mirror-image lowering-weight formula `(j+m)(j-m+1)`, is *also* exactly `1`. This confirms the entry's claim that "their excluded outgoing weights both have square 1" is correct once each chain's own natural escaping direction (up for one, down for the other, exactly as required by the mirror symmetry proved in v15.572) is used — not a naive same-direction comparison, which would have found only one nonzero escape.
- *`B`-ladder edge weights at `j=3/4`.* Rebuilt the `B_+` matrix from `\sqrt{(j-m)(j+m+1/2)}` and got exactly `(3/4,1,3/4)` for the three consecutive edges, matching exactly.
- *The two spectra.* Built `J_x=(J_++J_-)/2` and `B_x=(B_++B_-)/2` symbolically and diagonalized: `\mathrm{spec}(-gJ_x)=\{\pm g\sqrt6/4\}` each twice — algebraically identical to the claimed `\{\pm g\sqrt{3/2}/2\}$ (since `\sqrt{3/2}/2=\sqrt6/4`); `\mathrm{spec}(-hB_x)=\{-3h/4,-h/4,h/4,3h/4\}`, matching the claimed ordinary spin-`3/2` spectrum exactly.
- *`j=5/4` edge weights.* Independently rebuilt both ladders for the 6-state shell: `J` edges `(5/2,3,3,5/2)` and `B` edges `(5/4,2,9/4,2,5/4)`, both matching exactly.
- *The short-time opposite-parity probability.* Computed the first-order time-dependent perturbation amplitude from `|i{=}0\rangle$ under the pure-`B` Hamiltonian directly (`B_-|0\rangle=0`, so only `B_+|0\rangle=\sqrt{3}/2\,|1\rangle` contributes at this order) and got the `t^2`-coefficient of the opposite-`\Gamma`-sector probability exactly `3h^2/16`, matching the entry's claim exactly; confirmed separately (via the already-established `[H,\Gamma]=0$ fact for `h=0`) that the pure-`J`-drive probability vanishes identically, consistent with the entry's claim.

Every one of these is a from-scratch, independent computation (not a re-run of any committed script, since none exists in the repository for this entry) and all agree with the cited values exactly.

## Scope and honesty assessment

The entry is careful throughout to separate the exact finite-matrix mathematics from any physical claim: it states explicitly that "an algebraic escape weight is not probability leakage or an emitted photon unless an external target and Hamiltonian coupling are supplied," that the transition-strength predictions "are *relative squared couplings*, not measured line intensities," and that the leakage-extension construction's external states, frequency, and coupling constant "are NOT selected by the cone." It also correctly distinguishes connectivity (what the `B` channel buys) from dynamics or a repaired Lie-algebra defect, and from chirality or directional preference. This is consistent with, and continues, the careful carrier-separation discipline of v15.572–575.

## Summary

Confirmed. Every edge weight, both the `J_x` and `B_x` spectra, and the short-time cross-parity leakage probability in v15.576 are independently re-derived from scratch and match exactly, including the subtler mirror-symmetric escape-weight claim that required identifying each chain's own natural (opposite) escaping direction. No corrections needed.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
parent: v15.577
type: external-audit-round-518
status: closed
action: none — all numeric claims in v15.576 are correct and independently re-derived from scratch. No correction needed.
deliverable: independent confirmation of the Zeeman-style transition network's exact edge weights, spectra, and short-time leakage probability on the odd-quarter open shells, correctly scoped throughout as finite algebraic structure rather than a physical interaction, emission, or chirality selection.
