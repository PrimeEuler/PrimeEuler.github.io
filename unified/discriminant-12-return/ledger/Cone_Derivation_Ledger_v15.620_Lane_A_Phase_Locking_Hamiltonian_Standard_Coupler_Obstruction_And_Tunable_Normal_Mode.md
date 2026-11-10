# Cone Derivation Ledger v15.620 — Lane A: phase-locking dynamics, standard coupler obstruction, and tunable stable completion

**Date:** 2026-11-10. **Parents:** Paper C Quantum Realizations v1.1, v15.600 harmonic-resonance selector no-go, v15.615–617 scale/action/symplectic gates, v15.618 External Audit Round 523, v15.619 local action–angle cotangent lift and arbitrary phase constraint. **Status:** [D] exact Hamiltonian tangency and linearized eigenvalues; [N] symbolic reproducer; [O] physical interaction, quantum promotion, unique κ/q and gravitational observable. **Prewrite live HEAD:** 96341c24a63095b466a778fc3cd8586bc109bdca; v15.620 collision search empty. Additive-only, Suzuki/frozen production untouched.

## Gate 104 — standard SU(2) passive oscillator hopping fails to preserve the entire proposed section

Use Paper C's native semiclassical action–angle chart x=n1+1>1,y=n2>0, phases φ1,φ2 and Ω=dφ1∧dx+dφ2∧dy. Take the Poisson convention {φ_i,x_j}=δ_ij. For arbitrary nonzero κ define constraints modulo 2π:

F1=φ1+κy/2, F2=φ2−κx/2.

On the target section F1=F2=0, and {F1,F2}=−κ. Its inherited Ω is κdx∧dy (v15.619). A Hamiltonian is tangent to the section iff **{F1,H}|_F=0 and {F2,H}|_F=0** for all x,y in an open domain. In Cartesian action-angle derivatives these are

H_x−(κ/2)H_{φ2}=0 and H_y+(κ/2)H_{φ1}=0, on F=0.

For the common number-conserving two-mode passive hopping model (set ħ=1 temporarily),

H_hop=ω1(x−1)+ω2y−2g√[(x−1)y] cos(φ1−φ2),

the total occupation x+y is exactly conserved. Since φ1−φ2=−κ(x+y)/2 on the proposed section, invariance requires dot(φ1−φ2)=0 there. Instead

dot(φ1−φ2)=ω1−ω2−g[y−(x−1)]/√[(x−1)y] cos[κ(x+y)/2].

For g≠0 this is not identically zero on any open (x,y) domain, regardless of constant detuning ω1−ω2. For g=0, it forces ω1=ω2, but then dot F1=ω1,dot F2=ω2, requiring the trivial zero-frequency free flow. Hence **no nontrivial member of this precisely specified passive linear/hopping family preserves the entire two-dimensional phase-locking section**. Isolated resonant or stationary points are not ruled out. This does not exclude all quadratic Gaussian or nonlinear Hamiltonians.

## Gate 105 — explicit interacting Hamiltonian preserving the reduced cone flow

For κ≠0 and real C, define an engineered 2π-periodic phase coupling

H=xy−(x/κ)sin F1+(y/κ)sin F2+C[2−cos F1−cos F2].

Direct Poisson brackets show {F1,H}|_F={F2,H}|_F=0 exactly on the phase-locked surface. The constrained/reduced motion follows from the inherited Ω_red=κdx∧dy and h=H|_F=xy:

dot x = x/κ, dot y = −y/κ, and d(xy)/dt=0.

Thus a Hamiltonian extension exists that dynamically preserves the section and realizes the cone's hyperbolic product-preserving flow. This coupling **was constructed around the desired constraint**; it is an existence witness, not source-derived dynamics. Any nonzero κ can be used. More generally, for any smooth h(x,y), an exactly tangent completion is

H_h=h−[h_y/κ]sin F1+[h_x/κ]sin F2+C(2−cos F1−cos F2).

The trigonometric functions are globally phase-periodic, but the open positive-action domain and winding boundary still need separate quantum treatment.

## Gate 106 — transverse normal mode is stable in an open tunable parameter family

For h=xy, write small deviations f1=F1,f2=F2; linearize the **full** Hamiltonian flow transverse to the invariant section. The exact linearization is

d/dt [f1,f2]^T = M[f1,f2]^T + O(|f|²),

M=[[-1/κ,−Cκ],[Cκ,1/κ]].

tr M=0; det M=C²κ²−κ^(−2), and M²=−det M I. For real κ≠0 and real C with C²κ⁴>1, eigenvalues are ±iΩ with Ω=√[C²κ²−κ^(−2)]. This is **linear (elliptic) normal stability**, not a proof of nonlinear Lyapunov stability or physical damping/attraction. With C>0,κ>0, criterion simplifies Cκ²>1. Explicit witnesses: κ=1,C=2 gives Ω=√3; κ=2,C=1 gives Ω=√15/2; κ=1/2,C=5 gives Ω=3/2. More generally for desired Ω>0 and any κ≠0, choose C=√[Ω²+κ^(−2)]/|κ|; the normal-mode frequency is then Ω. Thus matching even a measured normal-mode frequency *alone* fails to determine κ because the coupling remains free.

All results are formal classical semiclassical action–angle models. Physical units require multiplying dimensionless occupation symplectic form by ħ and correspondingly calibrating Hamiltonian/time. The engineered coupling's periodic phase terms do not specify a well-defined self-adjoint quantum Fock operator or gauge-invariant implementation by themselves. No physical selection of q=2, s/u, κ, cutoff X or G is provided.

## Reproducibility, audit and next gate

Reproducer `research-notes/phase_locking_hamiltonian_gate_v15_620.py` symbolically verifies {F1,F2}=−κ, exact tangency, constrained xy-preservation, M and Ω, and checks the native hopping relative-phase drift. The conversation's `cone_phase_lock_104_106/reproduce.py` is the same tested source.

**HANDOFF** target external-audit, gravity, sandbox; status open; type standard hopping no-go / tunable engineered invariant phase-locking surface. Re-derive all sign conventions and tangent conditions; verify that elliptic transverse linearization is not overclaimed as nonlinear global stability; check the open-domain assumption and the lack of a physical κ selector. No impact on Suzuki frozen work.

**Next gate:** test whether symmetry, locality, polynomial occupation degree and unitarity constrain the engineered h-dependent phase terms enough to quantize κ or produce an experimentally distinguishable response **without fitted coupling C**. A matching frequency with free C does not close the selector.
