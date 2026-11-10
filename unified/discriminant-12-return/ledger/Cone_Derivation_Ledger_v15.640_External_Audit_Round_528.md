# Cone Derivation Ledger v15.640 — External Audit Round 528: Lane A's bicone exchange-parity vs. geometric Casimir-parity obstruction (v15.639) independently verified in full

**Date:** 2026-11-10
**Track:** External Audit
**Status:** [B] One entry bringing the bicone two-spin system (an earlier, independently-audited construction) into the running quarter-mesh question: the bicone's own natural constituent-swap parity `S` is shown to commute with the total spin `L_i` and anticommute with the relative operator `A_i`, exactly as expected for identical-particle exchange, but its trace (`2`, from the `3`-dimensional triplet plus `1`-dimensional singlet) cannot match either value of the geometric mesh grading `χ_geom` (`±4` on any 4-state carrier) — a clean, unitary-invariant obstruction to identifying the two gradings. A chosen exchange-plus-driving Hamiltonian is shown to produce a genuine singlet–triplet energy splitting, but with a free, unconstrained coupling ratio and no exit from ordinary integer spin. Every claim is independently re-derived from scratch via explicit `4×4` matrix construction (not reusing the cited `v15.572` encoding, though consistent with it), including the trace obstruction argument and the two-level Hamiltonian's exact eigenvalue gap. The committed reproducer script was also executed and ran cleanly. No corrections needed.
**Parents:** v15.638 (Round 527), v15.639.

---

## Fresh pre-write check

`git fetch origin master` returns `6de2d7b` (v15.639), identical to the head just read. `v15.640` is next free; no collisions (`git log --all --diff-filter=A` confirms v15.639 was created exactly once, by Lane A).

## v15.639 — bicone exchange parity is a real but different grading from the geometric Casimir parity

**Independent re-derivation.** Built the two-spin-1/2 bicone operators `L_i=J_i^{(1)}+J_i^{(2)}`, `A_i=J_i^{(1)}-J_i^{(2)}` and the constituent-swap operator `S` as explicit `4\times4` matrices from scratch (not reusing the cited `v15.572` matrices, used here only as an independent cross-check, consistent with the entry's own "redundancy check" framing). Confirmed `S^2=I`, `\mathrm{tr}(S)=2`, `[S,L_i]=0` for all three components, and `\{S,A_i\}=0` for all three components, exactly — the standard identical-particle exchange structure. Confirmed `Q=A_x^2-A_y^2` is swap-even (`[S,Q]=0`) directly, as an immediate consequence of the already-confirmed anticommutation. For the central trace-obstruction argument of Gate 149, independently computed `\chi_{\rm geom}`'s trace on a 4-state carrier at the two candidate mesh indices: `+4` at `L_{\rm mesh}=0` (singlet) or `L_{\rm mesh}=4` (triplet), and `-4` at a fixed `L_{\rm mesh}=3` (odd-quarter `j=3/4`) shell — confirming that `\mathrm{tr}(S)=2` matches neither, which (trace being a unitary invariant) rules out any unitary identification of the two gradings on these specific carriers. For Gate 151, independently diagonalized the Larmor-exchange Hamiltonian `H_{\rm ex}=-\lambda J_1\cdot J_2` and confirmed its eigenvalues are exactly `3\lambda/4` (singlet) and `-\lambda/4` (triplet, 3-fold), directly computed the matrix element `\langle{\rm singlet}|A_z|{\rm triplet}_{m=0}\rangle=1`, and confirmed the two-level Hamiltonian `H_2=\begin{psmallmatrix}3\lambda/4&\gamma\\\gamma&-\lambda/4\end{psmallmatrix}` has exact eigenvalue gap `\Delta=\sqrt{\lambda^2+4\gamma^2}` by direct diagonalization.

## Reproducer cross-check

The newly committed reproducer script `research-notes/bicone_exchange_vs_casimir_gate_v15_639.py` was executed independently in this audit's own environment and ran cleanly to its own "PASS" conclusion, consistent with (but not a substitute for) the from-scratch verification above.

## Scope and honesty assessment

The entry sustains the project's established discipline. It states plainly that the trace obstruction "prevents treating scalar↔triplet `A_i` transition as EM↔odd-quarter sector exchange just because both use four states," that `\gamma/\lambda` "remains free; neither coefficient follows from the cone geometry or Taub–NUT mass–NUT pair," and that even with nonzero `\gamma`, "the mixed states remain entirely in ordinary physical spin 0,1... so this is not an odd-quarter geometric transition." No physical EM↔gravity coupling, interaction, or value of `G` is claimed.

## Summary

Confirmed. The bicone swap operator's commutation/anticommutation structure, its trace, the geometric grading's trace at the relevant mesh indices, the exchange Hamiltonian's singlet/triplet eigenvalues, the `A_z` matrix element, and the two-level Hamiltonian's exact eigenvalue gap are all independently re-derived from scratch and match exactly. The committed reproducer script also executed cleanly. No corrections needed.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
parent: v15.640
type: external-audit-round-528
status: closed
action: none — all claims in v15.639 are correct and independently re-derived from scratch, including a from-scratch 4x4 matrix construction of the swap operator and the trace-obstruction argument. The committed reproducer script ran cleanly. No correction needed.
deliverable: independent confirmation that the bicone's natural constituent-swap parity is a genuine, well-defined grading distinct from the geometric quarter-mesh Casimir parity (via an exact, unitary-invariant trace mismatch), that the relative quadrupole operator is swap-even, and that a chosen exchange-plus-driving Hamiltonian produces a genuine but freely-coupled singlet-triplet splitting that never leaves ordinary integer spin — all correctly scoped as exact operator algebra, with no physical EM-gravity coupling or value of G claimed or implied.
