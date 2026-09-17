# Cone Derivation Ledger v13.558 — Transported Kernel V4 vs Character Translations

## Status
Exact matrix comparison continuing v13.554 and v13.557.

## 1. Full 3D transport
Extend the v13.554 transverse intertwiner by fixing the chi_12 axis:

P3 = [[1,-1,0],[1,1,0],[0,0,1]].

The determinant-one kernel extracted in v13.557 is

K = {I, -R_X, R_X R_Y, -R_Y},

with

-R_X = diag(1,-1,-1),
R_X R_Y = diag(-1,-1,1),
-R_Y = diag(-1,1,-1).

Conjugating by P3 gives

P3(-R_X)P3^{-1} = [[0,1,0],[1,0,0],[0,0,-1]],

P3(R_XR_Y)P3^{-1} = diag(-1,-1,1),

P3(-R_Y)P3^{-1} = [[0,-1,0],[-1,0,0],[0,0,-1]].

## 2. Character-translation matrices
In ordered character basis (chi_-4, chi_-3, chi_12), multiplication/translation by r in U(12) is diagonal:

D_5 = diag(1,-1,-1),
D_7 = diag(-1,1,-1),
D_11 = diag(-1,-1,1).

The v13.557 ray/cyclic-order identification was

T_5 <-> -R_X,
T_7 <-> R_XR_Y,
T_11 <-> -R_Y

before transport.

## 3. One-by-one literal/projective comparison after transport
For T_5:

K_5^P := P3(-R_X)P3^{-1} = [[0,1,0],[1,0,0],[0,0,-1]].

This is neither D_5 nor -D_5. Therefore the T_5 match is NOT literal and NOT projective after this P3 transport.

For T_7:

K_7^P := P3(R_XR_Y)P3^{-1} = diag(-1,-1,1) = D_11.

Thus it is literally equal to D_11, but not to the corresponding D_7. Relative to the mod-12 generator label T_7, the match is therefore not generator-preserving. The equality to D_11 is a relabeling coincidence induced by the chosen intertwiner.

For T_11:

K_11^P := P3(-R_Y)P3^{-1} = [[0,-1,0],[-1,0,0],[0,0,-1]].

This is neither D_11 nor -D_11. Therefore the T_11 match is NOT literal and NOT projective after this P3 transport.

## 4. Representation equivalence
Although the matrices do not agree generator by generator with D_5,D_7,D_11, both triples are faithful real 3D representations of V4 with the same character: identity has trace 3 and each nonidentity element has trace -1.

Hence they are equivalent as V4 representations after an automorphism/relabeling of the abstract V4 and an additional change of basis. What fails is the stronger marked-generator equality under the specific P3 chosen to intertwine the cone complex D8 with the A3 transverse D8.

In particular, P3 was chosen to transport the complex structure and reflection geometry, not to diagonalize the mod-12 translation V4.

## 5. Exact classification
Under the specific v13.554 transport P3:

- T_5 / -R_X versus D_5: only abstract representation equivalence; neither literal nor projective.
- T_7 / R_XR_Y versus D_7: only abstract representation equivalence as the same labeled generator; its transported matrix happens literally to equal D_11, showing a nontrivial generator relabeling.
- T_11 / -R_Y versus D_11: only abstract representation equivalence; neither literal nor projective.

Therefore the v13.557 projective generator-level identification between the ray-action mod-12 translations and native cone reflections does NOT become a literal generator-level identification with the diagonal character-translation representation after conjugation by P3.

The two structures are equivalent V4 representations, but the v13.554 complex-coordinate intertwiner and the arithmetic character-diagonal basis encode different markings.

## Guardrails
1. Do not infer from K_7^P=D_11 that arithmetic element 7 equals arithmetic element 11; it is a representation/basis relabeling phenomenon.
2. Projective equality here means equality up to one scalar for the whole 3x3 matrix. The off-diagonal transported matrices cannot be scalar multiples of the diagonal D_r.
3. v13.557 remains exact: before P3, the six-ray permutation action identifies T_5,T_7,T_11 projectively with R_X,R_XR_Y,R_Y under the chosen cyclic-order labeling.
4. v13.558 shows that this marked identification is incompatible with simultaneously using P3 as the cone-complex-to-A3 intertwiner and D_r as the diagonal character-translation matrices.
