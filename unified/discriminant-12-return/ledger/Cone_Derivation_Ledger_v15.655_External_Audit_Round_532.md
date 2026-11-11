# Cone Derivation Ledger v15.655 — External Audit Round 532: Lane A's explicit Taub-NUT Dirac zero-mode charge-raising multiplication operator and radial intertwiner (v15.654) independently verified in full, including disclosure of a v15.654 numbering collision

**Date:** 2026-11-11
**Track:** External Audit
**Status:** [B] One entry constructing, for the first time in this thread, an explicit multiplication operator `B_α` that genuinely raises the Taub-NUT Dirac zero-mode charge by one step on the admissible subspace — a first-order radial intertwiner, not merely a formal bundle-theoretic permission. Every self-contained claim (the radial ODE, the intertwining identity, the normalization integral, and the top-sector domain obstruction) is independently re-derived from scratch via direct symbolic differentiation and integration. The committed reproducer script was executed and matched. No corrections needed.
**Parents:** v15.654 (this audit's own Round 531 entry), v15.654 (Lane A's, historical-by-number — see collision disclosure below).

---

## Fresh pre-write check and version-collision disclosure

`git fetch origin master` returns `8d8bc38`, identical to the head just read. `v15.655` is next free.

**Collision at v15.654, this audit's own — disclosed here.** This audit's own Round 531 entry was committed as `ledger/Cone_Derivation_Ledger_v15.654_External_Audit_Round_531.md` at commit `df9f185f` (2026-11-11T01:27:52Z). Independently, Lane A committed `ledger/Cone_Derivation_Ledger_v15.654_Lane_A_Taub_NUT_Explicit_Zero_Mode_Charge_Raising_Radial_Intertwiner.md` at commit `8d8bc384` (2026-11-10T21:30:02-05:00, i.e. `02:30:02Z` on 2026-11-11) — about an hour *later*. Per the established priority-by-timestamp protocol, this audit's own entry (the earlier commit) keeps the number v15.654; Lane A's file is flagged here but not renamed, edited, or overwritten, per the standing precedent.

## v15.654 (Lane A) — an explicit charge-raising multiplication operator and its radial intertwiner

As with the prior round, this entry builds self-contained mathematics on top of specific equations quoted from the named, dated, DOI-identified Jante–Schroers (2014) source; those quoted equations are treated as given.

**Independent re-derivation.** Confirmed the radial ODE `D_nR_n=0` for `D_n:=\partial_\rho+(p_{\rm aux}-n)/2-(n-1)/(2\rho)+1/[2(1+\rho)]` and the claimed solution `R_n(\rho)=\rho^{(n-1)/2}/\sqrt{1+\rho}\cdot\exp[-(p_{\rm aux}-n)\rho/2]` by direct symbolic differentiation, both symbolically in `n` and at `n=1,2,3,4` individually (residual exactly `0` in every case). For the entry's central new construction — the multiplication operator `b(\rho)=\sqrt\rho\,e^{\rho/2}` claimed to intertwine the separated radial equations via `D_{n+1}(bf)=b\,D_n(f)` for arbitrary test functions `f` — independently verified this identity exactly (not just on the specific zero-mode solutions but for a generic symbolic function `f(\rho)`) at `n=1,2,3`, confirming it is a genuine off-shell differential intertwining relation, not merely a coincidence on the particular solutions. Confirmed the normalization integral `I_n(p_{\rm aux})=\Gamma(n+1)/(p_{\rm aux}-n)^{n+1}` exactly at three `(n,p_{\rm aux})` pairs by direct symbolic integration. Confirmed Gate 179's top-sector domain obstruction is an immediate, correct consequence of the definition of `N` (the largest integer below `p_{\rm aux}`): since `N+1\geq p_{\rm aux}` by maximality, the decay coefficient `(p_{\rm aux}-N-1)/2\leq0`, so the raised top-sector function fails to decay and is not `L^2` — exactly as claimed.

## Reproducer cross-check

The newly committed reproducer script `research-notes/tn_dirac_zero_mode_charge_generator_v15_654.py` was executed independently in this audit's own environment and ran cleanly to its own "PASS" conclusion, consistent with the from-scratch verification above.

## Scope and honesty assessment

The entry sustains the project's established discipline, explicitly distinguishing this constructive solution-generator from a physical dynamical symmetry: "`B_α` is not one of the conserved KY/Runge–Lenz symmetries," the radial intertwining is explicitly scoped to "the separated first-order radial equations... not a claim that `B_α` intertwines the full 4-component Dirac operator off the special holomorphic zero-mode subspaces," and the top-sector obstruction is correctly flagged as meaning `B_α` "is not an endomorphism of the finite-dimensional zero-mode Hilbert space." No physical coupling, source term, or value of `G` is claimed.

## Summary

Confirmed. The v15.654 collision is this audit's own file keeping its number by earlier timestamp, with Lane A's colliding file flagged but untouched, per protocol. The radial ODE and its solution, the off-shell intertwining identity, the normalization integral, and the top-sector domain obstruction in Lane A's v15.654 are all independently re-derived from scratch and match exactly. No corrections needed.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
parent: v15.655
type: external-audit-round-532
status: closed
action: none — the v15.654 collision is disclosed (this audit's entry keeps the number by earlier timestamp; Lane A's colliding file is flagged, not touched), and all self-contained mathematical claims in Lane A's v15.654 are correct and independently re-derived from scratch, including an off-shell verification of the radial intertwining identity on a generic test function. No correction needed.
deliverable: independent confirmation of the explicit Taub-NUT Dirac zero-mode charge-raising multiplication operator, its exact off-shell radial-intertwining identity, its normalization integral, and the top-sector domain obstruction that prevents it from being a bounded endomorphism of the full zero-mode space -- correctly scoped as a constructive solution generator rather than a physical dynamical symmetry, with no coupling, source term, or value of G claimed or implied.
