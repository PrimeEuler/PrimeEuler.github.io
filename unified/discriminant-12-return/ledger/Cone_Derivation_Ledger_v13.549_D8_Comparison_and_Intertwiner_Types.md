# Cone Derivation Ledger v13.549 — D8 comparison and intertwiner types

## Status
Exploratory exact finite-dimensional algebra. This entry compares the D8 structures accumulated in v13.534–v13.548. It does not promote a Pell/QR dynamical identification.

## 1. Four D8 appearances must be kept distinct

### (I) Intrinsic fixed-shell complex-plane D8
On z=X+iY,

- quarter-turn J: z -> i z,
- conjugation C: z -> conjugate(z).

In the real (X,Y) basis,

J2 = [[0,-1],[1,0]],
C2 = [[1,0],[0,-1]],

with J2^4=C2^2=I and C2 J2 C2=J2^{-1}. Hence <J2,C2> ~= D8.

### (II) A3 transverse-plane D8 from v13.535
On the transverse character plane (chi_-4, chi_-3),

R_perp = [[0,-1],[1,0]] = J2,
F_perp = [[0,1],[1,0]].

The exact real intertwiner

P = [[1,-1],[1,1]]

satisfies

P J2 P^{-1} = J2,
P C2 P^{-1} = F_perp.

Therefore the intrinsic fixed-shell D8 and this A3 transverse D8 are linearly equivalent as real 2D representations. This is a genuine representation equivalence, not only an abstract group isomorphism.

### (III) Projective arithmetic-lift D8 from v13.534/v13.535
The complexified arithmetic-negation lift A satisfies A^2=R_Y. Modulo <-I_3>, its class has order four and, together with the class of R_X, gives D8.

However v13.535's obstruction remains exact: if one identifies the projective class of A with J2, then A^2=R_Y is sent to J2^2=-I, whereas the intrinsic cone identification sends R_Y to conjugation C2. Hence the generator identifications cannot simultaneously be preserved by an intertwiner.

So this D8 is abstractly D8 but is not the same marked D8 representation as (I)/(II).

### (IV) Semilinear scalar/reversal D8 from v13.548
Let q=iI_3 and let

mathcal R(X,Y,T)=(bar X, bar Y, -bar T).

Then

q^4=1,
mathcal R^2=1,
mathcal R q mathcal R^{-1}=q^{-1},

so <q,mathcal R> ~= D8.

This D8 acts very differently from (I): q is scalar and therefore projectively trivial on every ray, while mathcal R induces the nontrivial orientation-reversal permutation rho=(a b)(c d)(e f). Thus its projective image on the six-ray set is only C2, with kernel <q> ~= C4.

Consequently (IV) cannot be conjugate, as a projective six-ray action, to any faithful D8 action. It is a central-scalar extension of the reversal C2 rather than the intrinsic fixed-shell quarter-turn/reflection action.

## 2. Exact hierarchy

The comparison is therefore:

1. Intrinsic fixed-shell D8 <J,C> and A3 transverse D8 <R_perp,F_perp> are exactly linearly intertwined by P.
2. The projective arithmetic-lift D8 is abstractly D8 but has an incompatible marked-generator identification because A^2=R_Y maps to the rotation half-turn, while intrinsic R_Y is conjugation.
3. The new semilinear D8 <iI_3,mathcal R> is genuinely semilinear and has projective kernel C4; on the six null rays it collapses to the reversal C2.

In formulas:

D8_intrinsic ~=_rep D8_A3-transverse,

D8_arithmetic-lift ~= D8 abstractly, but not under the simultaneous generator marking A<->J and R_Y<->C,

1 -> C4 -> D8_semilinear -> C2_reversal -> 1.

## 3. Relation to the full semilinear group

From v13.548,

tilde G ~= S4 x D8_semilinear,
|tilde G|=192,

and projectivization on the six null rays kills precisely the scalar C4:

1 -> C4 -> S4 x D8_semilinear -> S4 x C2 -> 1.

Thus the D8 factor in the full 192-element semilinear lift should not be identified with the intrinsic fixed-shell D8 merely because both are dihedral of order eight. Their actions and kernels are different.

## 4. Guardrail

This entry establishes an exact representation equivalence only between the intrinsic fixed-shell 2D D8 and the A3 transverse-plane 2D D8. It explicitly does not erase the v13.535 arithmetic-lift obstruction and does not identify the semilinear scalar/reversal D8 with either of those marked actions.
