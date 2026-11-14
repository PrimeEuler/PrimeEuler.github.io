# Cone Derivation Ledger v15.994 — External Audit Round 584

**Date:** 2026-11-14
**Track:** External Audit
**Parents:** Round 583/v15.990, Gravity v15.991 through v15.993

## Fresh state at gate

`git fetch origin master` immediately before this write returns `e461d86` (Gravity's v15.993 ledger text, which landed mid-round after its reproducer script `6bd6346`), identical to the head checked throughout the remainder of this round's work. No version-number collision (`v15.994` confirmed free).

## v15.991 — reopening the original-step quarter boundary, verified personally

This entry correctly scopes v15.989's closed-sector Casimir no-go: the project's *open* original-unit-step quarter ladder (from the already-audited v15.602) is a genuinely different object that does connect two distinct action circles via a nontrivial boundary map, unlike the closed co-scaled Casimir v15.989 tested. Independently rebuilt the `L=3` open-ladder defect operator from scratch (not the committed script): confirmed `E=diag(0,1/2,1/2,0)` and the boundary weight `w=(L+1)/4=1` exactly, matching the ledger's worked example.

## v15.992 — quadratic Maxwell/tidal terms cannot activate the boundary; quartic needs an L-dependent coefficient, verified personally

This entry tests whether the already-sourced leading-order Maxwell/tidal operators can realize the v15.991 boundary map in a canonical two-mode oscillator embedding, and finds a clean selection-rule no-go: the boundary requires `Δm_phys=±2` at `ΔN=+2`, but the leading quadratic tidal creation operators only produce `Δm_phys=+1,0,-1` at that occupation change — an exact degree mismatch, not a numerical smallness. The minimal oscillator operator that *could* match is quartic, `(a_1^†)^3a_2`, with amplitude `A_4(L)=\sqrt{L(L+1)(L+2)}`, requiring a coefficient `c_L=A_T/A_4=1/(2\sqrt{L(L+2)})` that depends on the shell index `L` — ruling out a single universal physical coupling constant for this monomial.

Independently re-derived both formulas symbolically from scratch and confirmed the `L=3` worked example exactly (`A_T=1`, `A_4=\sqrt{60}=2\sqrt{15}`, `c_3=1/\sqrt{60}`, matching the equivalent form `\sqrt{15}/30` the script prints).

**Re-executed both scripts.** Both ran to completion with `PASS`; v15.992's script additionally printed sample values at `L=4,6,10` (`c_4=\sqrt6/24`, `c_6=\sqrt3/24`, `c_{10}=\sqrt{30}/120`), all confirmed to follow directly from the verified closed-form `c_L` formula.

## v15.993 — source-first audit of the quartic candidate, verified personally

This entry extends v15.992 by checking the project's actual frozen physical actions (Maxwell at prescribed metric, the K4 solid action) for whether they could generate the needed quartic vertex, rather than simply positing one. It correctly observes that `S_EM=-(1/4)∫F²` stays exactly quadratic in the gauge potential at any fixed metric order, so no bare four-photon term appears from a metric expansion alone — confirmed by inspecting the already-audited v15.695 reduced Lagrangian form, which the script checks explicitly through `b²` order. It restates the v15.992 ratio `|T_L|/|\langle O_4\rangle_L|=1/[2\sqrt{L(L+2)}]` (re-verified, matching exactly) and adds the trivial-but-correct commutator fact `[H_0,O_4]=2\hbarω_0O_4` for the quartic monomial under the free Hamiltonian, establishing the `2\hbarω_0` energy detuning any resonant realization would need to overcome.

**Re-executed the script.** Ran to completion with `PASS`, printing the same ratio formula I had already verified in v15.992.

## Honesty and scope assessment

v15.991 is a model self-correction: rather than defending v15.989's scope, it explicitly accepts the user's correction and precisely delineates which prior no-go applies to which carrier (closed co-scaled Casimir vs. open original-step boundary). v15.992 then runs the natural next test with the project's own already-sourced physical operators and reports a clean, representation-theoretic negative (an exact occupation-change selection rule, not a numerical coincidence) rather than overclaiming the admissible quartic monomial as a discovered coupling. v15.993 takes this one step further by actually checking the project's own frozen field actions rather than assuming the quartic candidate could be sourced, correctly concluding the question remains genuinely open rather than resolved either way. No mathematical corrections needed in this round.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.994
type: external-audit-round
status: actionable
action: v15.991-993 all independently confirmed correct. No corrections needed. No open items from this round.
deliverable: Round 584 independent audit of v15.991-993 (3 entries, 3 scripts); all confirmed correct.
