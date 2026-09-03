# Cone Derivation Ledger v13.184 — Ramified vs. Unramified Four-State Bridge

Status labels: [D] exact derived, [I] interpretation, [Audit] limitation.

## 1. Two different four-element quotients

Let F=Q(sqrt(3)), O_F=Z[sqrt(3)], and p_2=(1+sqrt(3)). Since p_2^2=(2), multiplication by (1+sqrt(3))^{-1} identifies

p_2 / 2 p_2  ≅  O_F / 2 O_F.

Because sqrt(3) ≡ 1 mod 2 and (sqrt(3)-1)^2 ≡ 0 mod 2, this ring is the nonreduced dual-number ring

[D]  O_F/2O_F ≅ F_2[epsilon]/(epsilon^2).

Its additive group is V_4.

By contrast, for K=Q(zeta_12)=F(i) and P_2=p_2 O_K, the residue quotient is

[D]  O_K/P_2 ≅ F_4.

This is a field, also with additive group V_4.

Therefore the two four-state objects are not the same quotient and are not canonically isomorphic as rings:

[D]  p_2/2p_2 is ramified/nonreduced,
[D]  O_K/P_2 is unramified/reduced.

They only share the abstract additive group F_2^2.

## 2. Ramified transvection

In the ramified basis used previously, the discriminant-12 return reduces to

bar(g) = [[1,1],[0,1]].

This is the nontrivial unipotent transvection of order 2 over F_2.

Equivalently, after the integral ideal-basis change Phi, it is conjugate to the swap

P=[[0,1],[1,0]].

## 3. The same transvection appears canonically as Frobenius on F_4

Choose omega in F_4 satisfying

omega^2+omega+1=0,

so omega^2=omega+1.

Use the F_2-basis (1,omega). The Frobenius automorphism Fr(x)=x^2 satisfies

Fr(1)=1,
Fr(omega)=omega^2=1+omega.

Hence

[D] [Fr]_(1,omega) = [[1,1],[0,1]] = bar(g).

Thus the ramified mod-2 return matrix is exactly the Frobenius matrix on the unramified residue field in the natural basis (1,omega).

This is an action-level bridge, not a canonical identification of the two quotient rings.

## 4. Cyclotomic multiplication gives the order-3 generator

Multiplication by omega on F_4 is

omega*1=omega,
omega*omega=1+omega.

Therefore

[D] M_omega = [[0,1],[1,1]].

It has order 3.

Frobenius has order 2 and reverses multiplication:

[D] Fr M_omega Fr^{-1} = M_omega^{-1}.

Hence

[D] <M_omega, Fr> = GL(2,2) ≅ S_3.

## 5. Affine completion

The additive translations of F_4 form

F_4^+ ≅ V_4.

The order-3 multiplicative subgroup gives

[D] AGL(1,4)=F_4 ⋊ F_4^× ≅ A_4.

Adding Frobenius enlarges the linear part from C_3 to S_3 and gives

[D] AΓL(1,4)=F_4 ⋊ S_3 ≅ S_4.

Thus the finite symmetry ladder is

V_4  ->  A_4  ->  S_4,

with the final extension supplied by Frobenius.

## 6. Exact synthesis

The same 2x2 transvection appears in two arithmetically distinct ways:

[D] ramified side:
    multiplication by 2+sqrt(3) on p_2, reduced mod 2;

[D] unramified/cyclotomic side:
    Frobenius x->x^2 on F_4=O_K/P_2.

Meanwhile multiplication by zeta_12 reduces to multiplication by omega of order 3 on F_4.

Therefore the finite operator package can be written as

    Pell return  ->  transvection/Frobenius (order 2)
    cyclotomic operator -> multiplication by omega (order 3)

and these generate the full linear group

[D] GL(2,2) ≅ S_3.

After adjoining translations of the four states, the full affine group is

[D] AGL(2,2) ≅ S_4.

## 7. Audit guardrail

[Audit] Do not claim p_2/2p_2 and O_K/P_2 are canonically identical four-state systems. One is the ramified dual-number quotient F_2[epsilon]/(epsilon^2); the other is the field F_4. The exact bridge is that the same transvection matrix acts as the reduced Pell return on the first and as Frobenius on the second, once the stated natural bases are chosen.

[I] This gives a strong representation-theoretic unification of the two four-state pictures without collapsing their distinct arithmetic origins.
