# Cone Derivation Ledger v15.954 — Pauli-type chiral half-step interlayer on the conserved n+1 null-cone section

**Date:** 2026-11-14 Eastern. **Track:** Gravity. **User hypothesis:** quarter-grid EM/grav interlayer operators may be extensions of the Pauli matrices. **Parents:** Paper C Schwinger Fock ladder, v15.602 projected q2 boundary, v15.625 formal quarter Casimir, v15.924 fixed-n+1 null-cone transition matrix, v15.951 common-diameter odd quarter label, v15.952 D−1 EM transition rows and D odd half-integer interlayer rows. **Audit Round 577:** v15.953 independently confirmed v15.946–952 and collision repair; no mathematical correction. **Immediate HEAD before write:** b694668b281c54d991f15c359da698ffb2237a56 (validated reproducer); target absent, additive-only. Protect historical/frozen Suzuki/Audit/Sandbox objects.

**Status:** [D] exact finite-dimensional chiral block algebra and index-one unmatched mode for a chosen adjacency, spectral formula; [C] an admissible Pauli-like *edge-graph* realization; [N] no canonical physical coupling or true new spinor/EM↔gravity Pauli matrix; [O] field-derived half-step operator and observation.

## Gate 737 — Pauli generalization across parity-graded transition *edges*

For integer common physical diameter D=n+1≥2, v15.952 gives D−1 positive integer-factor **EM transition-edge coordinates** k=1,...,D−1 and D positive half-integer **interlayer coordinates** r+1/2, r=0,...,D−1, all on the same Cone null section T²−X²−Y²=0. The graph carrier is **H_edge = C^(D−1)_even ⊕ C^D_odd** (dimension 2D−1). **This is NOT the original D-dimensional Schwinger Fock state Hilbert space**; edge incidence alone cannot identify transition edges with independent physical quantum states.

Choose a simple nonzero nearest-neighbor incidence B:C^(D−1)→C^D, B_(r,k)=1 for r=k−1 or r=k (k indexed 1..D−1, r indexed 0..D−1); zero otherwise. This unit choice is mathematically natural for the graph topology but not uniquely selected by local physical intensity. Define

**Σ_x=[[0,B†],[B,0]]**,
**Σ_y=[[0,−iB†],[iB,0]]**,
**Σ_z=diag(+I_(D−1),−I_D)**.

All are Hermitian and Σ_z²=I. Exactly

**{Σ_z,Σ_x}={Σ_z,Σ_y}={Σ_x,Σ_y}=0**,
**Σ_x²=Σ_y²=diag(B†B,BB†)**,
**[Σ_x,Σ_y]=2i Σ_z Σ_x²**.

These are an *operator-valued Pauli algebra*, not ordinary Clifford/Pauli generators on the full carrier: Σ_x² is **not I**. A general interaction H_int=g_xΣ_x+g_yΣ_y remains freely scaled; no G, ħ, transition frequency or physical phase selection is derived. Since Σ_x flips parity and J± acts within integer occupation sectors, the former is not equivalent to the original Schwinger J±.

## Gate 738 — one unpaired odd interlayer mode is forced for full-column-rank adjacency

For this B, B†B is the tridiagonal (D−1)×(D−1) Jacobi matrix with diagonal 2 and nearest-neighbor off-diagonal 1. Its monic characteristic polynomial is **U_(D−1)((λ−2)/2)** (Chebyshev of second kind), with nonzero eigenvalues

**λ_m=2+2cos(mπ/D)>0**, m=1,...,D−1.

Hence B has full column rank D−1, and the block Σ_x has 2(D−1) paired nonzero eigenvalues ±sqrt(λ_m) and precisely one zero eigenvalue in the odd sector. Explicit odd zero vector **z_r=(−1)^r**, r=0,...,D−1, obeys B†z=0. The grade trace is tr Σ_z=(D−1)−D=−1. Rank-nullity alone forces at least one odd zero mode for ANY B with this rectangular shape, although a different B may produce extra paired zero modes. This is a finite-graph chiral/supersymmetric index statement, **not a physical fermion, new zero-frequency particle, or conserved energy mode**.

If B is weighted by the positive geometric half-row heights w_r=sqrt[(r+1/2)(D−r−1/2)] as B_w=diag(w_r)B, it still has full column rank, and its odd zero vector becomes z_r=(−1)^r/w_r. Thus the index survives a class of geometry-suggested weights, but eigenvalues and matrix elements change. The graph does not fix any overall or relative physical coupling amplitude. Under an arbitrary positive bond weighting, only generic full column rank and dimension protection survive; a unique zero-mode profile is not mandated by null-cone incidence.

## Gate 739 — physical interpretation and comparison to earlier quarter-boundary no-go

This Pauli-block construction is a meaningful candidate **extension of the Pauli grading** to the q2 edge interlayer, but its unmatched edge has the same general origin as the projected quarter ladder's missing boundary closure (v15.602). It does not repair the original q2 intrinsic SU2 commutator or promote the formal quarter Casimir to a physical gravity Casimir. One can normalize Σ_x on the nonzero spectrum to disjoint spin-1/2 Pauli blocks, leaving a one-dimensional singlet; such normalization requires the chosen B and is not a unique physical field.

The key next discrimination is whether a *source-derived* EM/gravity interaction on the actual D-dimensional Fock **states**, with a consistent Hilbert-space enlargement if necessary, gives this rectangular B and fixes its weights and phase by gauge covariance or a field action. With arbitrary B and g, this is a family of finite chiral graphs, not a parameter-free EM/G prediction. No sourced spin2 graviton, orbital stabilization or G-free measurable effect follows yet.

## Verification, provenance, and handoff

**Validated exact SymPy reproducer:** `research-notes/k4_pauli_chiral_interlayer_v15_954_validated.py`, commit **b694668b281c54d991f15c359da698ffb2237a56**. Executed locally PASS D=2..12: full chiral anticommutation, [Σ_x,Σ_y], rank, exact Chebyshev characteristic polynomial, odd alternating zero vector, positive geometric-height weighted variant. The preliminary exploratory script `research-notes/k4_pauli_chiral_interlayer_v15_954.py` commit **f73fe608651d0f1b584d2feeb4e173fe2c400f20** contains an assertion using naive SymPy trig expansion for D≤8 that does not simplify at D=7; **do not use it as the validated executable**. This is a tool simplification issue, not a counterexample; the exact Chebyshev replacement avoids it. Additive-only preserves both files for provenance.

**HANDOFF Audit/Muse:** independently prove the Chebyshev Jacobi characteristic identity, degree-count/zero-mode and graph versus Fock-state distinction; assess whether a *specific physical action* selects B or rules out a half-step sector-flip map. Treat all physical identifications as open.
