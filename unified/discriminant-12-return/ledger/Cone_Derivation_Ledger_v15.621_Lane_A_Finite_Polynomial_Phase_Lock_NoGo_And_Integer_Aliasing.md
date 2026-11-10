# Cone Derivation Ledger v15.621 — Lane A: finite-polynomial exact phase-lock no-go and integer-lattice aliasing

**Date:** 2026-11-10. **Parents:** Paper C Quantum Realizations v1.1, v15.600 harmonic selector no-go, v15.617–619 symplectic/action-angle lift and phase section, v15.620 standard hopping failure and engineered tunable phase-locking. **Status:** [D] exact finite-harmonic/algebraic-amplitude no-go under stated semiclassical conditions; [D] formal integer-label alias; [O] physical quantum phase/selector. **Prewrite live HEAD:** 758c33f24a874dd9423ef6fb825b8c9a92008847; v15.621 collision search negative. All work additive-only, frozen Suzuki/far-tail production untouched.

## Gate 107 — exact global phase locking demands occupation-dependent exponential coefficients

On Paper C's open action-angle region x=n1+1>1,y=n2>0 with symplectic Ω=dφ1∧dx+dφ2∧dy, let κ∈R\{0} and the intended invariant section be F1=φ1+κy/2=0, F2=φ2−κx/2=0 modulo 2π.

Hamiltonian vector-field tangency to this section on a nonempty open set is equivalent to
H_x−(κ/2)H_{φ2}=0 and H_y+(κ/2)H_{φ1}=0 at F1=F2=0.

Consider the explicitly scoped class of **finite Fourier Hamiltonians with algebraic occupation amplitudes**,

H(x,y,φ1,φ2)=Σ_(a,b)∈finite h_ab(x,y) exp[i(aφ1+bφ2)],

a,b∈Z and each h_ab a single-valued algebraic function of x,y on a chosen simply connected occupation patch. This includes classical action-angle symbols of all finite-degree polynomial two-boson creation/annihilation Hamiltonians (with a consistent normal/semiclassical symbol prescription). Restriction to the phase section makes the (a,b) harmonic proportional to exp[iκ(bx−ay)/2]. Distinct integer pairs have distinct exponentials of linear forms, linearly independent over algebraic-function coefficients on open complex-analytic continuations of the patch. Hence the tangency equations decouple into

∂_x h_ab=(iκb/2)h_ab,  ∂_y h_ab=−(iκa/2)h_ab,

with unique local solution

**h_ab=C_ab exp[iκ(bx−ay)/2].**

When κ≠0, any nonzero (a,b) demands nonalgebraic exponential dependence (unless C_ab=0). The zero mode (a,b)=(0,0) requires ∂_x h_00=∂_y h_00=0, hence it is constant. Therefore:

**No nonconstant finite-Fourier Hamiltonian with algebraic occupation amplitudes preserves this entire phase section on an open positive-occupation domain.**

This is an **exact global open-set** obstruction for the specified Hamiltonian-symbol class, not a no-go for nonpolynomial interactions, higher-dimensional gauge extensions, approximate local locking, singular/delta constraints, isolated periodic solutions, dissipative systems, or finite single-state matching. κ=0 is excluded since it gives a degenerate reduced 2-form and the tangency problem changes.

The engineered v15.620 term sin(φ1+κy/2) has Fourier coefficients involving exp(±iκy/2), so it is **outside** this algebraic-amplitude class and does not contradict the theorem. Even within its permitted family, its normal frequency Ω²=C²κ²−κ^(−2) permits arbitrarily chosen κ with freely chosen C.

## Gate 108 — integer occupation sampling aliases κ modulo 4π

At native Paper C integer vertices x=n1+1 and y=n2 with n_i∈Z_≥0, replace κ by κ+4πm, m∈Z. Then the prescribed section phases change by

Δφ1=−2πm n2, Δφ2=2πm(n1+1),

and are consequently identical modulo 2π at every integer occupation pair. A 2πm shift gives occupation-parity-dependent signs and is generally not the same prescribed phase. Thus the sampled **prescription** for the phase section cannot distinguish κ and κ+4πm from vertex phase values alone.

Crucial limitation: exact Fock number eigenstates have no simultaneously sharp canonical phases. The 4π alias is a statement about formal sampling of the *semiclassical function*, not a physical unitary equivalence of all κ theories. Continuous surfaces and induced symplectic area forms Ω_red=κdx∧dy differ between the vertices; hence the formal alias neither selects κ nor proves a physical action quantum periodicity.

## Gate 109 — selector audit and experimental criteria

Within the exact finite-degree bosonic polynomial Hamiltonian class, the phase-locking reduction cannot be globally dynamically invariant at nonzero κ. Permitting an explicit occupation-dependent phase coupling restores existence (v15.620), but introduces a freely tunable C and κ; measuring one transverse frequency Ω cannot identify κ without an independently fixed interaction strength. No finite polynomial sector uniquely selects the proposed q=2 interlay or Newton G. A physical progress condition would be an independently sourced nonpolynomial interaction or constrained symplectic reduction with a fixed phase law, plus a calibratable and experimentally distinguishable response.

Independent SymPy reproducer and report: conversation artifact `cone_gate107_109.zip`, containing `cone_gate107_109/reproduce.py` and `REPORT.md`; checks include exact tangent differential conditions mode by mode, necessity of exponential coefficients, invariance of v15.620's engineered exception, and vertex alias formulas.

**HANDOFF** target external-audit, gravity, sandbox; status open; independently verify the exponential/algebraic linear-independence argument and assumptions (positive occupation patch, finite harmonics, analytic algebraic coefficients), the exclusion of κ=0, and that formal lattice aliasing does not assert global quantum equivalence. Retain certified artifacts and frozen Suzuki production unchanged.
