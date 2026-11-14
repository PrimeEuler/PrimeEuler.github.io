# Cone Derivation Ledger v15.991 — Correction: open q2 quarter ladder joins two action circles through a boundary defect, unlike the closed q2 Casimir

**Date:** 2026-11-14 US Eastern. **Lane:** Gravity. **Prompt:** user corrects v15.989's closed-sector Casimir focus: existing quarter ladders have open boundaries and connect two action circles. **Status:** [D] recovered v15.602 projected original-unit-step q2 boundary theorem and cross-shell T†T=2E; [D] concrete q2 rank-two defect and shell-radius shift; [C] Hermitian coupled-shell kinetic Hamiltonian with free physical coefficient; [N] v15.989 closed-quarter Casimir no-go is correctly scoped but does not exhaust open-ladder boundary transitions; [N] existing T preserves EM/odd-quarter shell grading and does not itself drive EM-to-quarter conversion; [O] actual K4/Maxwell physical source and energy normalization.

**Redundancy and audit:** v15.602 Lane A all-q open-chain boundary theorem, independently verified Audit Round 521/v15.603, already constructs the exact boundary map. v15.628 distinguishes the actual T, which preserves q2 shell parity, from a desired odd-rung EM/quarter exchange; its independent Audit Round 524/v15.629 confirms. v15.934 preserves difference between original-unit projected ladder and closed nearest-neighbor co-scaled q2 SU2; v15.954 chooses an edge-graph rectangular B with index-one zero mode, not a native Fock state intertwiner; v15.969–973 prove central Casimir phase-only for closed carriers; v15.989 tests *only* that latter closed carrier. External Audit Round 583 took canonical v15.990 and verified v15.988–989 without mathematical corrections. **Live master immediately before ledger write:** 03f1226643237ac91c48ee041a06c35ffc2ca7ff, exact script for this gate. Target absent, additive only, no existing certified, Suzuki, Audit, Sandbox or Muse objects modified.

## Gate 809 — exact original-unit-step open q2 ladder, not the closed co-scaled q2 spin

On mesh q=2, step h=1/2, let L≥3 integer, formal quarter label **j=L/4** with refined states m_i=−j+i/2 for i=0,...,L. Retain the *original* Δm=1 raising law, so **J+|m> = sqrt[(j−m)(j+m+1)] |m+1>** when target lies on this finite refined shell, otherwise zero. This advances i→i+2, producing two residue chains mod 2, unlike the closed Δm=1/2 conventional spin-L/2 ladder.

Define M=diag(m_i) and **E=j(j+1)I−(Jx²+Jy²+M²)**. This E is nonzero at open boundary sources i=1 and L−1. For q2 **w=(L+1)/4** is the omitted squared original-step amplitude on either side, and for L≥3 (distinct sources) **E_(1,1)=E_(L−1,L−1)=w/2**, all other diagonal entries zero. Rank E=2. Original-unit projected quarter Casimir therefore differs from scalar j(j+1) by E; the v15.989 closed co-scaled K² result does NOT invalidate or replace this boundary defect.

## Gate 810 — two action-circle shells and exact boundary exchange map

The previously derived v15.602 cross-shell map is **T:H_j→H_(j+1/2)**, with upper/lower omitted legs from sources m=j−1/2 and m=−j+1/2 to targets m'=j+1/2 and m'=−j−1/2. Each carries amplitude **sqrt(w)**. The target refined shell index is **L'=L+2**. Exactly:

**T†T=2E**, with two nonzero singular values sqrt(w). The shell action-circle radii **R=j+1/2** and **R'=j'+1/2=j+1** differ by **R'−R=1/2**. Scalar formal geometric Casimir labels differ by **C(j')−C(j)=j+3/4**. Neither radius difference nor Casimir-label difference is automatically a *physical energy gap*.

Example L=3: j=3/4, j'=5/4, action radii (5/4,7/4), w=1; **E=diag(0,1/2,1/2,0)** and T has rank two. Exact source-to-target geometry therefore **permits** inter-action-circle amplitude transfer, in contrast to an isolated scalar closed-shell Casimir.

## Gate 811 — what a physically driven cross-shell exchange would mean

On the explicitly enlarged direct-sum carrier H_j⊕H_j', a conditional Hermitian interaction is **H_int=g T+g* T†** with appropriate block orientation. Units matter: geometric T is dimensionless, so g must have units of energy (or ℏ times a frequency). With an independently supplied sector energy detuning Δ and constant real g (take ℏ=1 for formula), each active singular pair reduces to the standard 2×2 Hamiltonian **H_pair=[[-Δ/2,g√w],[g√w,+Δ/2]]**. Starting on the lower leg, its transfer probability is

**P(t)=[4g²w/(Δ²+4g²w)] sin²[(t/2)√(Δ²+4g²w)]**.

This proves that the OPEN boundary operator can produce population transfer and a nontrivial time-dependent kinetic-energy exchange **if an interaction is physically activated**. It does not mean g, Δ, source amplitude, frequency, or an independently physical gravitational mode has been derived. With g=0 there is no transfer, although the entire boundary geometry and defects remain intact. A diagonal sector Casimir phase term is not a substitute for a nonzero T coupling.

## Gate 812 — critical parity / open-versus-closed distinctions

The *specific* v15.602 T shifts shell label **L→L+2**, preserving **L mod 2**. v15.628 proves its χ parity is unchanged for q=2, whereas a genuine EM↔odd-quarter exchange operator would flip χ and requires a distinct physical carrier/source (ordinary two-mode Fock occupation forbids a ΔN=1/2 jump without enlargement). Thus the existing open ladder **does connect two action circles**, but we should NOT claim it automatically converts EM to gravitational quarter-only Casimir class or that it is the missing K4 graviton/Maxwell coupling.

Also, the graph B in v15.954 connects D−1 integer *edges* and D half-integer *interlayer positions* on a fixed-D circle. It is mathematically different from v15.602's cross-shell boundary T and from the closed Schwinger K². Its index-one zero mode proves a graph fact, not a unique physical zero-energy state. These constructions cannot be conflated.

## Gate 813 — result, reproducer and next physical test

**Positive:** the user's correction is accurate. The v15.989 closed q2 central Casimir no-go does *not* close the OPEN two-action-circle quarter ladder. Its exact boundary defect E and map T are already established and nontrivial, and the required boundary amplitude is fixed **relative to the chosen original-step ladder**, not selected as a physical energy coefficient.

**Negative:** original-unit projected quarter ladder is not ordinary closed SU2, and the known boundary map preserves even/odd shell grading; the source-selected physical exchange term and unique kinetic normalization remain open. Any T-coupled time evolution with arbitrary g is an admissible toy, not a new gravitational observable.

**Exact reproducer:** `research-notes/k4_open_quarter_boundary_two_circle_v15_991.py`, additive commit **03f1226643237ac91c48ee041a06c35ffc2ca7ff**. Exact local SymPy checks PASS for L=3..15: reconstructed original-unit-step raising matrices, defect E, cross-shell T†T=2E, rank two, radius and Casimir shell shifts and parity preservation. Also symbolic 2×2 coupled-pair Rabi frequency and g=0 control. Independent Audit pending.

**NEXT/HANDOFF Audit, Muse:** independently verify L=3 E and rank-two T map, parity preservation L→L+2, and check which *physically sourced* K4 action can activate a boundary link while respecting its charge/holonomy and open-ended domain. Test whether a genuine field-operator matrix element selects g or Δ; stop rather than inferring a frequency from the length 1/2. Compare any candidate with ordinary Maxwell/GR detectors under equal kinetic-source normalization. Preserve the distinction between connected action circles, open boundaries, original projected ladder and closed q2 Schwinger completion.
