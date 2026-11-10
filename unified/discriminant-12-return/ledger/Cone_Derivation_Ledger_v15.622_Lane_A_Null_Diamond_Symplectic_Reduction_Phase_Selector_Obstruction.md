# Cone Derivation Ledger v15.622 — Lane A: null-diamond reduction does not select the phase-locked factor action

**Date:** 2026-11-10. **Parents:** authoritative `foundations/Casimir_Null_Diamond_Standalone_v2.1.tex`, `foundations/PaperC_QuantumRealizations_v1.1.tex`, v15.600–601 null-target and additive gauge selector tests, v15.617 factor-plane symplectic dictionary, v15.618 External Audit Round 523, v15.619–621 phase-locking and finite polynomial Hamiltonian tests. **Status:** [D] geometric identity, single-mode boundary symplectic reduction and native transition leakage; [O] actual microscopic gauge/physical phase selector. **Prewrite live HEAD:** 79ad861de30517b4123cbfc033c42a5cf21e3130. v15.622 path/name collision search empty. Additive-only; no Suzuki/frozen production touched.

## Gate 110 — the null-cone identity is not a moment-map constraint

For x,y≥0, T=(x+y)/2, X=(x−y)/2, Y²=xy, identically **T²−X²−Y²=0**. On Paper C's two-mode oscillator action–angle space `(n1,n2,φ1,φ2)` with x=n1+1,y=n2 and Ω=dφ1∧dx+dφ2∧dy, the conic equation is identically zero at every point. Its differential vanishes; it does not define a new independent constraint hypersurface, Hamiltonian vector field or gauge orbit to quotient.

Casimir Null Diamond v2.1's second ingredient, primitive spinors with integer determinant ad−bc=±1, gives Lorentz midpoint norm M_F²=(ad−bc)²/4=1/4 (and spacing δ gives δ²/4). This concerns discrete **pairs of spinor points**, not continuously specified constraints on φ1,φ2 and not a first-class moment map. The null-diamond paper explicitly distinguishes Farey null edges and four-corner oscillator cells; no phase-locking dynamics are stated.

## Gate 111 — actual null-axis reduction loses the factor action I

In the native oscillator Hilbert/semiclassical geometry, the factor axis y=n2=0 is the zero-amplitude condition for the second mode, a codimension-two submanifold in smooth complex oscillator coordinates (z1,z2) with z2=0. Its pullback of the canonical oscillator 2-form is the ordinary **single-mode** form dφ1∧dn1=dφ1∧dx away from z1=0. The second oscillator phase φ2 is *undefined* at n2=0; extending action–angle coordinates there as if φ2 were independent is singular. Formal presymplectic treatment y=0 and quotienting the null φ2 direction agrees with the smooth complex-oscillator result.

On y=0, product I=xy=0 identically; ψ=(1/2)log(x/y) diverges. Thus the v15.617 rapidity–product chart and v15.619 nondegenerate form κ dx∧dy cannot be pulled back as a nontrivial two-dimensional factor-pair symplectic structure on this null axis: dy=0. The proposed phase relations φ1=−κy/2, φ2=κx/2 also fail to define a regular full two-mode phase section there, since φ2 is not defined. Any resulting condition φ1=0 further reduces the remaining single-mode symplectic plane to a one-dimensional isotropic line; it does not pick a unique κ.

The *geometric* null cone (all pairs x,y≥0) must not be confused with its *factor-axis subset* xy=0; they are distinct uses of the word null.

## Gate 112 — native Hamiltonian invariance versus target postselection

For P0 the quantum projection onto the second-mode vacuum span{|n,0⟩:n≥0}, number-diagonal H=f(N1,N2) preserves Ran P0 for **arbitrary** f. No such invariance specifies κ, step s, or the cross-shell boundary witness's normalization. Conversely, for n>0, the Schwinger lowering operator J_-=a2†a1 sends |n,0⟩ → √n |n−1,1⟩, outside Ran P0; and K_+=a1†a2† sends |n,0⟩→√(n+1)|n+1,1⟩, outside Ran P0 for all n≥0. Thus the full Jx or Kx interactions are not null-axis preserving. This is consistent with the explicit dynamical no-go of v15.600 and null-target/gauge observations of v15.601; a projector onto null *destinations* is not a derived dynamical constraint.

**Verdict:** neither the always-true Lorentz cone equation, the discrete unimodular null-edge invariant, nor the genuine oscillator-vacuum boundary supplies the two smooth phase constraints needed for the κ-dependent reduction of v15.619. The native null-axis reduction is single-mode and destroys I>0, so it cannot fix κ, the quarter mesh, a physical action calibration, or Newton G. This is a precise negative about the cited existing constraints—not a general no-go for a separately specified gauge theory or added degrees of freedom.

**Reproducer:** conversation archive `cone_null_reduction_gates_110_112.zip` with reproducible `reproduce.py` and `REPORT.md`; exact SymPy checks cover T²−X²−xy=0, phase-section form, zero product on axis, and oscillator matrix-element squared magnitudes. Independently inspect the full foundation v2.1 and Paper C v1.1 for the scope of the result.

**Next gate:** test explicit genuine moment maps from the native U(1) total-number/difference symmetries, distinguishing first-class constraints from gauge fixing, to see whether a nondegenerate two-dimensional quotient supports any meaningful factor-product action or fixes κ. Avoid engineered phase constraints or identifying a postselected projector with Gauss law without an interaction.

**HANDOFF:** target external-audit, gravity, sandbox; status open; verify complex-amplitude smooth null-axis reduction, endpoint n1=0 exception, native operator leakage, cone-identity vs xy=0 distinction, and nonexistence of an intrinsic κ selector in these *specific* structures. Frozen Suzuki lane untouched.
