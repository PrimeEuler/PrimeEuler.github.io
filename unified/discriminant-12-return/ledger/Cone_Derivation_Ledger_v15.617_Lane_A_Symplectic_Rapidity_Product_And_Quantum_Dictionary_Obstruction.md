# Cone Derivation Ledger v15.617 — Lane A: exact symplectic factor dictionary and canonical/quantum obstruction

**Date:** 2026-11-10. **Parents:** Paper C Quantum Realizations v1.1, v14.367 pair-rapidity/Cayley dictionary, v14.767 normalized power map, v15.602 generalized boundary shell, v15.615 Fock-spectrum scale obstruction, v15.616 parabolic action quantization selector negative. **Status:** [D] exact classical Poisson identities, domain and commutator obstructions; [O] physically calibrated action/canonical quantum representation. **Prewrite live HEAD:** ed0118146dff7bacd6788934dc57ac5f596d96a9, free v15.617 collision search negative. Additive only; Suzuki and far-tail untouched.

## Gate 97: the factor-plane hyperbolic coordinates are canonically conjugate in a stated symplectic structure

For x,y>0, let ψ=1/2 log(x/y), I=xy. Equip the factor plane **by choice** with Ω=dx∧dy and the Poisson bracket {f,g}=∂_x f ∂_y g−∂_y f ∂_x g. Exact differentiation yields

**dψ∧dI=dx∧dy and {ψ,I}=1.**

The image is ψ∈R, I>0. Thus (ψ,I) is a canonical chart on the positive factor plane for this specified Ω. This is a geometric identity; it does not show that Ω is the mechanical symplectic form of gravity or that I is an observable physical action. A conversion J_phys=κI needs an independently justified κ, with action per factor-area dimensions; u alone does not fix κ.

## Gate 98: existing ladder translations are symplectic but not equal-action transitions

At fixed j=(x+y)/2, m=(x−y)/2, a unit-step ladder m→m+s (within the admissible positive domain y>s) induces x→x+s, y→y−s. This affine translation preserves dx∧dy, but

**ΔI=(x+s)(y−s)−xy=s(y−x)−s²**, generally depending on x,y.

Even if one chooses J_phys=κI, there is no uniform ΔJ quantum along the ladder. The generalized all-q chosen cross-shell witness j→j+d_q, m→m+1, d_q=1−1/q, sends (x,y)→(x+2−1/q,y−1/q), also an area-preserving translation on its admissible open domain. Its ΔI is state-dependent. The cross-shell map remains a geometrically defined **rectangular Hilbert-space witness**, not a canonical unitary identified with this classical translation; the symplectic check must not be promoted to a physical dynamics derivation.

## Gate 99: the circle and normalized power maps use different area structures

The established cone factor-to-circle projection F(x,y)=((x−y)/2,√(xy)) has

det DF=(x+y)/(4√(xy)).

Therefore F is not symplectic from (x,y,dx∧dy) to (X,Y,dX∧dY), unless restricted to special loci; it is a symplectomorphism if the **input symplectic structure is changed** to the pullback det DF dx∧dy. These are different assignments of physical area, not the same invariant.

The circle angle θ=2 arctan√(y/x) can nonetheless be completed to a canonical pair for Ω=dx∧dy using P_θ=−√(xy)(x+y)/2; explicitly {θ,P_θ}=1. This particular P_θ has dimensions of factor-area and still requires physical κ.

The normalized Paper B factor power map P_{k,u}(x,y)=(u(x/u)^k,u(y/u)^k) has determinant

**det DP_{k,u}=k²(xy/u²)^{k−1}.**

For k≠1 it is not globally symplectic under dx∧dy; in (ψ,I) it sends ψ→kψ, I→u²(I/u²)^k, whereas the simple canonical companion to ψ→kψ would be I→I/k (up to ψ-dependent translation permitted by integrability). The power map is arithmetically/geometrically valid but not a canonical action-quantum preserving map.

## Gate 100: commuting Fock occupations and positive-product Weyl obstruction

Paper C's **native** operator dictionary x=n1+1,y=n2 consists of commuting occupation-number operators. On the joint spectral domain, any functions ψ(n1,n2) and I(n1,n2) commute, [ψ,I]=0, with log singular at n2=0. This cannot realize [ψ,I]=iħ as a canonical pair by directly quantizing both as number functions. Additional phase/conjugate degrees of freedom or a different quantization prescription would be required.

Even abstractly, the classical I>0 half-plane does not permit a **global regular irreducible Weyl pair** of self-adjoint ψ and positive self-adjoint I satisfying U(t) I U(t)†=I+tħ for *all* t∈R: arbitrary translations would contradict positivity and preservation of spec(I). This is a globally scoped obstruction; local classical Darboux coordinates, affine quantization or boundary-modified operators remain possible. Do not infer that no quantization of the cone exists.

## Reproducer, audit, and next discrimination

Exact SymPy producer in conversation artifact `cone_symplectic_gates_97_100.zip` verifies Jacobian and Poisson identities, circle-angle momentum, power-map determinant, and state-dependent inter-shell product change. No extra external inputs.

**Verdict:** an exact classical canonical *candidate* pair is now identified, but it neither fixes a conversion from factor area to action nor identifies a quantum canonical pair in Paper C. The original-unit-step ladder is a symplectic translation on an open factor-domain; it is not a uniform quantum of product action. No unique q=2, ħ calibration, G, field, or measured force has been derived.

**Next gate:** examine an independently justified extended action-angle phase space for Paper C (two Fock occupation numbers plus their conjugate phases), and test whether the cone's rapidity/product can be completed as a canonical transformation there without selecting the missing κ or physical boundary law by hand.

**HANDOFF** target external-audit, gravity, sandbox; status open. Verify the sign convention and symplectic map, factor-plane vs pulled-back circle area distinction, classical ladder step calculation, exact power-map determinant, and quantum spectral/Weyl domain limitations. Frozen Suzuki untouched.
