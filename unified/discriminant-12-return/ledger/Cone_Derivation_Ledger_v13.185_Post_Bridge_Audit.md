# Cone Derivation Ledger v13.185 — Post-Bridge Audit

Status labels: [S] source-established, [D] exact derived, [N-cert] rigorous numerical/computer-assisted, [I] interpretation, [O] open, [Audit] correction/limitation.

## Scope

This audit checks the chain developed in v13.177–v13.184 linking:

- Paper A parabola/anti-diagonal tangency,
- Cone Lorentz geometry,
- the discriminant-12 return,
- Pell-unit action on the ramified ideal p_2,
- the centered operator H,
- cyclotomic multiplication by zeta_12,
- the ramified four-state quotient,
- the unramified residue field F_4.

## A. Tangent-circle geometry

[D] For fixed factor level u, the Paper A row parabola

Y^2=u^2+2uX

has Euclidean vertex (-u/2,0), while the mirror column parabola has vertex (+u/2,0).

[D] The origin-centered fixed-T circle tangent at those vertices has radius

T=u/2.

[D] Therefore the complete integer family has radii 1/2,1,3/2,2,... and tangent points X=±u/2.

[Audit] The circular text boxes around product labels in the reconstructed figure are annotations, not geometric conics. Only explicitly defined fixed-T circles count as geometry.

## B. Null-ray identification

[D] In (T,X) coordinates the tangent points

(T,X)=(u/2,±u/2)

satisfy T^2-X^2=0. They lie on the two null rays.

[D] The Lorentz form of the discriminant-12 return is

B_12=[[2,sqrt(3)],[sqrt(3),2]].

Its null eigenvalues are

lambda=2+sqrt(3), lambda^{-1}=2-sqrt(3).

[D] Hence the tangent endpoints are exactly the expanding and contracting null eigenrays of the return.

## C. Shell dynamics

[D] In Paper A null coordinates x=T+X, y=T-X,

x' = lambda x,
y' = lambda^{-1} y.

[D] Therefore xy is preserved and each divisor shell xy=n is invariant under the real return.

[D] In rapidity coordinates x=sqrt(n)e^s, y=sqrt(n)e^{-s},

s' = s + log(lambda).

[Audit] This is a real dynamical statement. It does not by itself identify the discrete integer divisor points with an invariant orbit.

## D. Mesh renormalization

[D] An isotropic mesh transported covariantly by the return becomes anisotropic:

(m_x,m_y)->(m_x/lambda, lambda m_y).

[D] The product m_x m_y is invariant.

[D] Writing m_x=m e^{-rho}, m_y=m e^{rho}, one gets

rho' = rho + log(lambda),

so s-rho is invariant.

[Audit] Naive parity of transported mesh indices is unchanged and does not produce the ramified transvection. The nontrivial mod-2 action occurs on the Pell/ideal coefficient lattice.

## E. Pell ideal realization

[D] Let p_2=(1+sqrt(3))=(2,sqrt(3)-1).

In the ramified basis f=(2,sqrt(3)-1), multiplication by lambda=2+sqrt(3) has matrix

g_12=[[3,1],[2,1]].

[D] In the principal/Pell basis e=(1+sqrt(3),3+sqrt(3)), multiplication by lambda has matrix

[[2,3],[1,2]].

[D] The integral basis-change matrix reduces mod 2 to the previously used Boolean map Phi.

[D] Thus Phi bar(g) Phi^{-1}=P is the mod-2 shadow of an actual unimodular ideal-basis change.

## F. Centered operator

[D] H=g-2I acts as multiplication by sqrt(3) on p_2.

[D] Hence H^2=3I follows from (sqrt(3))^2=3.

[D] In the Pell basis,

H=[[0,3],[1,0]].

[Audit] This identifies H with a multiplication operator on the rank-2 F-ideal module. It does not make H itself a scalar over Q; the scalar interpretation is over F=Q(sqrt(3)).

## G. Cyclotomic operator

[D] After adjoining i,

Z=(H+iI)/2

acts as multiplication by

(sqrt(3)+i)/2=zeta_12.

[D] On the integral cyclotomic ideal lattice p_2 O_K, Z is therefore multiplication by zeta_12.

[D] The earlier index-4 phenomenon comes from comparing the coarse order Z[sqrt(3),i] with the full cyclotomic ring O_K=Z[zeta_12].

[Audit] The half-integral formula for Z in the coarse basis is a lattice-coordinate artifact, not evidence that the cyclotomic operator is nonintegral on its natural carrier.

## H. Four-state quotients

[D] The ramified quotient

p_2/2p_2 ≅ O_F/2O_F ≅ F_2[epsilon]/(epsilon^2)

has four elements and additive group V_4, but is nonreduced.

[D] The cyclotomic residue quotient

O_K/P_2 ≅ F_4

has four elements and additive group V_4, but is a field.

[Audit] These are not the same quotient and are not canonically ring-isomorphic.

[D] In the natural basis (1,omega), omega^2+omega+1=0, Frobenius x->x^2 on F_4 has matrix

[[1,1],[0,1]],

exactly the ramified transvection matrix bar(g).

[D] Multiplication by omega has matrix

[[0,1],[1,1]]

of order 3.

[D] Frobenius reverses this order-3 multiplication, so the two generate GL(2,2)≅S_3.

[D] Adding translations gives AGL(2,2)≅S_4.

[Audit] The bridge between the two four-state systems is action-level/representation-level, not an equality of rings.

## I. n=11 bridge

[D] On shell n=11, (11,1) and (1,11) lie on x+y=12 and map to

(T,X,Y)=(6,±5,sqrt(11)),

with 6^2-5^2=11.

[D] Separately, 11≡-1 mod 12 gives the complex-conjugation Frobenius class in the cyclotomic extension, and the narrow-class calculation identifies the prime above 11 with the class of p_2.

[Audit] The geometric x+y=12 intersection and the arithmetic Frobenius/class-field statements are exact facts sharing the same prime 11, but no theorem here says one causes the other.

## J. Suzuki crossing

[N-cert] For theta=2 there is a certified unique t_* in the stated interval with

m_2(t_*)=2+sqrt(3).

[D] The target value 2+sqrt(3) is now identified as the Pell unit generating the return, whose centered part is sqrt(3), and whose cyclotomic completion is zeta_12.

[Audit] This does not prove that the Suzuki framework globally derives the arithmetic return or its finite quotients. The result is a certified matching at the distinguished crossing.

## K. Publication-safe synthesis

The following chain is now exact, with each arrow interpreted at its proper level:

[D]
2+sqrt(3)
 -> multiplication on p_2
 -> g_12
 -> H=g_12-2I = multiplication by sqrt(3)
 -> Z=(H+iI)/2 = multiplication by zeta_12
 -> multiplication by omega on F_4.

The ramified reduction of the Pell return gives the order-2 transvection, while Frobenius on F_4 realizes the same order-2 matrix. Together with the order-3 cyclotomic multiplication they generate the full linear symmetry GL(2,2)≅S_3, and with translations the affine symmetry S_4.

## L. Open points

[O] Establish whether there is a canonical functorial object containing both the ramified thickening O_F/2O_F and the unramified residue field F_4 without making a basis choice.

[O] Determine whether the Cone mesh phases admit a nontrivial arithmetic reduction naturally compatible with the ideal action, beyond covariant transport.

[O] Determine how much of the new operator package can be stated in Papers A/B/C without obscuring their original scope.

[O] Audit the new-paper draft section-by-section against this ledger before promoting the strongest unification statements into publication text.
