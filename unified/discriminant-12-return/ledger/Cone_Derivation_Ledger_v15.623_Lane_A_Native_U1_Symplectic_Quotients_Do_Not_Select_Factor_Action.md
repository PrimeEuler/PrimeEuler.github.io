# Cone Derivation Ledger v15.623 — Lane A: native U(1) charge reductions and the factor-product action obstruction

**Date:** 2026-11-10. **Parents:** Paper C Quantum Realizations v1.1; Casimir Null Diamond v2.1; v15.617 factor-plane symplectic chart, v15.619 local cotangent lift, v15.620–621 phase-lock dynamics, v15.622 null-axis symplectic reduction. **Status:** [D] ordinary U(1) moment-map reductions on regular strata; [O] physical constrained Hamiltonian, phase/action calibration and sector selection. **Immediately prewrite live HEAD:** 5a74993328a9f45069ae226fa87ff2120f24208e; v15.623 collision search empty. Additive only; frozen Suzuki and certified objects unchanged.

## Gate 113 — Schwinger total-number charge gives a genuine two-dimensional quotient but not {ψ,I}=1

On the local two-oscillator action–angle manifold (n1,n2>0, φ1,φ2 mod 2π) with Ω=dφ1∧dn1+dφ2∧dn2, the common U(1) phase rotation has moment map N=n1+n2. Fix N=c>0. Then n2=c−n1 and the pullback Ω=d(φ1−φ2)∧dn1. Quotienting the common phase leaves (n1,δ=φ1−φ2) with the same nondegenerate two-form, on the regular interior 0<n1<c. The global reduced space is a CP¹/S²-type symplectic quotient with phase-circle collapse at the two endpoints; action–angle coordinates are not globally regular there.

In Paper C's shifted factor dictionary x=n1+1, y=n2, the fixed-N condition gives x+y=c+1. Both cone quantities ψ=(1/2)log(x/y) and I=xy depend only on n1 on the quotient. Their reduced Poisson bracket is **{ψ,I}_red,N=0**, not 1. They therefore cannot form canonical conjugates on this quotient. No extra free symplectic parameter κ is selected by the U(1) charge reduction.

## Gate 114 — squeezing number-difference U(1) gives the same obstruction

Paper C's two-mode SU(1,1) squeezing conserves D=n1−n2, which generates opposite phase rotations in the classical action–angle space. Fix D=d and choose z=n2>max(0,−d). Then n1=z+d, x=z+d+1, y=z, and Ω=(dφ1+dφ2)∧dz on the fixed charge surface. Quotient the relative/opposite phase, retaining η=φ1+φ2 and z as the canonical pair on each regular sector. Once again ψ=(1/2)log[(z+d+1)/z] and I=z(z+d+1) depend only on z, hence **{ψ,I}_red,D=0**.

More generally, for an ordinary nontrivial linear U(1) moment map Q=a n1+b n2 with fixed Q, the two occupations lie on a one-dimensional curve; any two functions of occupations alone have vanishing reduced Poisson bracket after the corresponding phase quotient, wherever the reduction is regular. This obstruction is intrinsic to the chosen functions of occupations, not merely to the special N or D charges. A phase-dependent observable could be conjugate to the remaining action, but neither ψ nor I is such an observable.

In quantum Fock space N and D are indeed integer spectrum labels, but integer charge eigenvalues do **not** identify a unique κ or q=2: those require a further physically justified condition relating the geometric factor unit to action/interaction. The arithmetic null-edge determinant condition is not this charge moment map.

**Verdict:** the existing null-axis, Schwinger and SU(1,1) U(1) reductions are mathematically legitimate but do not recover κ dψ∧dI with ψ,I conjugate. No physical step, phase-locking interaction, G or gravitational observable follows. This is a scoped no-go for these native charge reductions, not for all gauge theories or added phase-dependent variables.

**Independent verification:** exact symbolic substitutions of N=c and D=d into Ω and analytic derivative checks confirm bracket zero; the structural one-dimensional-action argument covers all fixed regular linear U(1) moment maps. Complementary executable reproducer for null-axis Gate 110–112 is `research-notes/null_diamond_symplectic_reduction_gate_v15_622.py`; conversation artifact `cone_null_reduction_gates_110_112.zip` stores that report/script. All checks are mathematical, not numerical G fits.

**HANDOFF:** target external-audit, gravity, sandbox; status open. Verify global quotient boundary description, moment-map sign conventions, the zero bracket for ψ,I on both N/D reductions, and the exact distinction between a phase-space quotient and an imposed phase section. **Next gate:** search for a concrete source-derived first-class Gauss/moment-map constraint that couples phases to occupations, or formulate an experimentally operational cutoff/energy observable independently of any fitted parameter. Preserve frozen Suzuki.
