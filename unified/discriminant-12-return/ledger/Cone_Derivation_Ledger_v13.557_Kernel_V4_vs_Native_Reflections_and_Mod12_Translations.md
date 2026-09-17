# Cone Derivation Ledger v13.557 — Kernel V4 vs Native Reflections and Mod-12 Translations

## Status
Exact finite-group/matrix computation continuing v13.556. This entry distinguishes linear equality from projective equality.

## 1. Extracted kernel inside the determinant-one cone S4
Use the verified generators

r = [[0,-1,0],[1,0,0],[0,0,1]],

s = [[0,0,i],[1,0,0],[0,-i,0]].

Exact closure gives H=<r,s> of order 24. The kernel of its induced action on the three reversal pairs {a,b}, {c,d}, {e,f} has exactly four matrices:

K_1 = I,

K_7 = diag(-1,-1,+1),

K_5 = diag(+1,-1,-1),

K_11 = diag(-1,+1,-1).

Their six-ray permutations are respectively

K_1: identity,

K_7: (a b)(c d),

K_5: (a b)(e f),

K_11: (c d)(e f).

Thus K={K_1,K_5,K_7,K_11} is exactly a Klein four subgroup.

## 2. Compare with native cone reflections
The native cone reflections are

R_X = diag(-1,+1,+1),

R_Y = diag(+1,-1,+1),

R_X R_Y = diag(-1,-1,+1).

Hence

K_7 = R_X R_Y,

K_5 = -R_X,

K_11 = -R_Y.

Therefore the extracted determinant-one kernel is

K = {I, -R_X, R_XR_Y, -R_Y}.

It is NOT literally the native linear fixed-T reflection group

V_geom={I,R_X,R_Y,R_XR_Y},

because R_X and R_Y have determinant -1 and are not elements of H=ker(det).

However scalar -I is projectively trivial. Therefore

[-R_X]=[R_X],

[-R_Y]=[R_Y],

and projectively

[K] = {[I],[R_X],[R_Y],[R_XR_Y]}.

So the identification with the native cone V4 is generator-level after projectivization, but not as literal linear 3x3 matrices inside H.

## 3. Compare with mod-12 translations
On Omega={1,5,7,11}, translations are

T_5=(1 5)(7 11),

T_7=(1 7)(5 11),

T_11=(1 11)(5 7).

Using the exact v13.545 cyclic-order labeling, their induced six-ray permutations are

T_5 -> (a b)(e f),

T_7 -> (a b)(c d),

T_11 -> (c d)(e f).

Comparison with the extracted kernel therefore gives the exact generator correspondence

T_5 <-> K_5 = -R_X,

T_7 <-> K_7 = R_XR_Y,

T_11 <-> K_11 = -R_Y.

Together with T_1 <-> I, this is an element-by-element identification of the abstract mod-12 translation V4 with the extracted kernel K, under the chosen v13.545 S4 equivariant labeling.

Projectively this becomes

T_5 <-> [R_X],

T_7 <-> [R_XR_Y],

T_11 <-> [R_Y].

Thus the mod-12 translation identification is generator-level on the six-ray projective action.

## 4. Important comparison with character diagonal matrices
In the character basis (chi_-4,chi_-3,chi_12), the standard translation matrices are

D_5 = diag(+1,-1,-1),

D_7 = diag(-1,+1,-1),

D_11 = diag(-1,-1,+1).

Numerically these are the same three sign matrices as the extracted K elements, but the labels are permuted relative to the cone-coordinate identification above:

D_5 has the same numeric diagonal as K_5,

D_7 has the same numeric diagonal as K_11,

D_11 has the same numeric diagonal as K_7.

This numerical coincidence must not be mistaken for equality of operators across different coordinate spaces. The exact mod-12 correspondence in Section 3 is established from the S4 action on cyclic orders, not by identifying the cone (X,Y,T) basis with the character basis.

Under the v13.554 transverse intertwiner P, the matrices transform nontrivially; therefore the coordinate-space distinction is essential.

## 5. Conclusion
There are two levels of identification:

1. Linear cone level inside H:

K = {I,-R_X,R_XR_Y,-R_Y} != {I,R_X,R_Y,R_XR_Y}.

So the extracted kernel is not literally the native reflection V4 as a subgroup of GL_3(C).

2. Projective six-ray level:

[K] = {[I],[R_X],[R_Y],[R_XR_Y]}.

With the chosen cyclic-order/mod-12 labeling,

T_5 <-> [R_X],

T_7 <-> [R_XR_Y],

T_11 <-> [R_Y].

Therefore the identification is stronger than merely abstract: it is generator-level/projective, with a precisely identified central scalar twist on the linear lift.

Equivalently, the determinant-one S4 lift chooses the representatives

R_X -> -R_X,

R_Y -> -R_Y,

R_XR_Y -> R_XR_Y

so that every kernel representative has determinant +1.

## Guardrails
- Do not state K=V_geom literally in GL_3(C); only their projective images coincide.
- The element labels T_5,T_7,T_11 depend on the chosen v13.545 equivariant cyclic-order labeling.
- Do not infer that cone coordinates (X,Y,T) are literally the character coordinates (chi_-4,chi_-3,chi_12); v13.554 supplies a nontrivial transverse intertwiner.
- This result does not identify the U(24) arithmetic sign bit, QR deck involution, or sheet reversal with these generators.
