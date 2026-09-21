# Cone Derivation Ledger v13.638 — External Audit Addendum: Suggested Next Question for the LQG/Tetrahedron Thread

Date: 2026-09-21

Status: advisory addendum from the external audit thread, at the project owner's explicit request. Not a derivation, not a claim, and not a request to prove anything below before proceeding — a scoping note for a possible future gate.

## 0. Live collision/relevance check

The live ledger was fetched immediately before this write. Tip is v13.637 (chi_-4 closed-avenues consolidation). v13.636 (the LQG/tetrahedron synthesis note requested in v13.635) landed first and closes that sub-result cleanly, with its own Section 11 guardrail list matching the checkpoint's requirements exactly. v13.638 is free and does not touch either v13.636 or v13.637's content.

## 1. Why this addendum exists

The project owner asked the external audit thread, after v13.636 closed the weighted-path/flattened-D8 synthesis, whether it is theoretically possible to connect the magnetic-driver thread and the LQG/tetrahedron thread beyond what v13.624/v13.631/v13.636 already establish. The audit's answer, reproduced here for the LQG thread's own record: **not as a claim that the two systems share dynamics or a spectrum** — v13.624 already rules that out generically from j=3/2 onward, and v13.636 Section 11 correctly keeps that door shut. What may be worth exploring, as a distinct and clearly-labeled next question, is a narrower and more modest idea: **whether the driven-spin (magnetic) platform could serve as an engineered analog/digital simulator of the tetrahedral volume operator's orientation/kernel structure**, using the explicit intertwiner already constructed in v13.631/v13.636 as the basis-mapping tool.

## 2. What would make this well-posed, if pursued

This is explicitly not proposed as ready to derive. If a future round takes it up, it should first establish, not assume:

1. **A precise notion of "simulate."** The shared object is the flattened D8 skeleton `(R,H)` — orientation and kernel-dimension parity — not the raw spectrum. Any simulation claim must state up front that it targets this combinatorial/topological structure (does `Q_a` have a zero mode at this j; what is the D8 orbit structure) and not the volume operator's actual eigenvalues, which v13.624 already shows the magnetic-drive operator does not share.
2. **An explicit protocol**, not an analogy: given the magnetic-driver's Floquet quasi-energy structure (v13.626/v13.630, now confirmed through 8th order) at some j, what engineered choice of drive parameters realizes `R_Y` on that j-dimensional space, and what does the v13.631 intertwiner `U_{a<-Y}` then say about reading off `Q_a`'s orientation data from the drive's own basis?
3. **A fidelity/error metric.** Since the flattening operation `R=H\,\mathrm{sgn}(L)` is itself nonlinear and the intertwiner has `O(N_j)` gauge freedom (v13.636 Section 8), any concrete proposal needs to state what "the simulation succeeded" would even mean numerically.
4. **A literature check before new derivation.** Analog/digital simulation of small loop-quantum-gravity spin-network Hamiltonians on engineered quantum platforms is an existing research direction (e.g. proposals for simulating spin-network dynamics on quantum hardware). Before deriving anything here, locate and cite what is already known, so any new result is measured against it rather than independently reinvented.

## 3. Explicit non-goals

To avoid this addendum being over-read the way v13.636 was careful the synthesis note itself not be over-read:

- This is not a claim that such a simulation exists, works, or is easy.
- This is not a request to weaken or revisit the spectral-inequivalence result (v13.624) in any way; the inequivalence is precisely what makes "simulate the skeleton, not the spectrum" the only honest framing.
- This is not connected to the chi_-4/L-function thread (v13.637) or to any GRH-relevant claim; nothing here bears on that lane.
- The Coldea et al. E8 golden-ratio spin-chain resonance that motivated this question remains, as v13.636 Section 11 already states, an outside physical observation by the project owner, not a result derived in this ledger, and this addendum does not change that status.

## 4. Recommendation

If the LQG/tetrahedron thread wants a next gate after v13.636, this is a reasonable candidate — but it should be opened as its own clearly-scoped entry (state the protocol, the fidelity metric, and the literature context before any derivation), not treated as a continuation of the now-closed synthesis. If it is not pursued, v13.636 stands complete on its own and needs nothing further.
