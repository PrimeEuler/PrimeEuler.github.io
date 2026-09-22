# Cone Derivation Ledger v13.662 — Pell/QR Equivariance Test on the Six-Point S4/C4 Carrier

Date: 2026-09-22

Status: exact finite-algebra obstruction audit. This tests v13.656 priority 3 after v13.657-v13.659. Negative conclusions are part of the result.

## 0. Live synchronization and scope

Before writing, the live ledger was rechecked. Since v13.659, two Suzuki-thread entries have landed as v13.660 and v13.661. Therefore this thread does **not** claim v13.660; it advances to v13.662. No v13.662 entry is present at the final pre-write check.

External Audit Round 72 (v13.659) independently confirmed v13.657 and v13.658 and corrected the handoff provenance: v13.560/562/563/567/569 already contain the sharper marked-intertwiner and sigma_A/sigma_B obstruction. Those results are treated as established here.

The question is narrowly:

> Does the six-point carrier C6 = S4/C4 itself induce a new Pell or QR equivariance?

The answer is: **only at a lower-dimensional character quotient; not on the full six-point carrier.** There are several exact obstructions.

## 1. Established six-point U(12) action

From v13.658,
[
mathcal C_6={a,b,c,d,e,f}cong S_4/C_4,
]
and the arithmetic subgroup
[
U(12)={1,5,7,11}cong V_4
]
acts by
[
5=(a,b)(e,f),qquad
7=(a,b)(c,d),qquad
11=(c,d)(e,f).
]

Thus
[
mathcal C_6=
{a,b}sqcup{c,d}sqcup{e,f},
]
with stabilizers
[
H_{ab}={1,11}=kerchi_{12},
]
[
H_{cd}={1,5}=kerchi_{-4},
]
[
H_{ef}={1,7}=kerchi_{-3}.
]

Equivalently, as U(12)-sets,
[
oxed{
mathcal C_6
cong U(12)/kerchi_{12}
;sqcup;
U(12)/kerchi_{-4}
;sqcup;
U(12)/kerchi_{-3}.
}
]

This decomposition is the correct starting point for any Pell/QR equivariance claim.

## 2. What Pell actually sees

The established Pell unit is
[
lambda=2+sqrt3.
]
For (rin U(12)), the Galois action satisfies
[
oxed{sigma_r(lambda^n)=lambda^{chi_{12}(r)n}.}
]

Therefore Pell orientation factors through only
[
U(12)/kerchi_{12}cong C_2.
]

On the six-cycle carrier, precisely the orbit
[
{a,b}cong U(12)/kerchi_{12}
]
carries this same quotient.

Hence there is a genuine exact **two-state** Pell equivariance:
[
oxed{
{a,b}longleftrightarrow{lambda^{+n},lambda^{-n}},
}
]
up to choosing which of (a,b) denotes (+) orientation. Under (r),
both sides are exchanged exactly when (chi_{12}(r)=-1).

This is real structure, but it uses only one two-point orbit of C6. It does not extend Pell orientation to a faithful action on all six points.

## 3. First obstruction: Pell orientation cannot distinguish all six states

The Pell-orientation action has kernel
[
kerchi_{12}={1,11}.
]
The full U(12) action on C6 is faithful: intersecting the three orbit stabilizers gives
[
kerchi_{12}capkerchi_{-4}capkerchi_{-3}={1}.
]

So the full six-point carrier retains all three nontrivial V4 characters, while Pell orientation retains only chi12.

At representation level,
[
mathbf Q[mathcal C_6]
cong3mathbf1opluschi_{12}opluschi_{-4}opluschi_{-3},
]
whereas the two-state Pell orientation module is
[
mathbf1opluschi_{12}.
]

Therefore:
[
oxed{
	ext{Pell orientation is a quotient/submodule shadow of C6, not a full C6-equivariant dynamics.}
}
]

Any proposed Pell action that claims to canonically recover the other two cycle pairs must supply extra arithmetic data beyond the Pell unit.

## 4. QR carrier and its stabilizer mismatch

The exact QR fold from v13.507/v13.515/v13.522 has downstairs carrier
[
V=mathbf F_2^2cong U(12)
]
with the regular U(12) translation action. Thus every point of V has trivial stabilizer.

By contrast, every point of C6 has a nontrivial order-two stabilizer:
[
|operatorname{Stab}_{U(12)}(x)|=2
qquad(xinmathcal C_6).
]

Suppose there were a U(12)-equivariant map
[
F:mathcal C_6	o V.
]
For any (x), equivariance forces
[
operatorname{Stab}(x)subseteqoperatorname{Stab}(F(x)).
]
But the left side has order 2 and the right side is trivial. Impossible.

Hence
[
oxed{
operatorname{Hom}_{U(12)	ext{-sets}}(mathcal C_6,V)=arnothing.
}
]

This is a sharp obstruction: **there is no U(12)-equivariant six-cycle-to-QR-state map at all.**

## 5. The reverse direction exists, but only as three separate folds

For a transitive U(12)-set (U(12)/K), a map to (U(12)/H) exists when (Ksubseteq H).

The QR carrier V is regular, so (K={1}). Therefore V admits an equivariant two-to-one projection onto each of the three C6 orbits:
[
V	o U(12)/kerchi_{12}={a,b},
]
[
V	o U(12)/kerchi_{-4}={c,d},
]
[
V	o U(12)/kerchi_{-3}={e,f}.
]

These are exactly the three character quotients.

Thus the correct relationship is
[
oxed{
Vlongrightarrow
{a,b},{c,d},{e,f},
}
]
not
[
mathcal C_6longrightarrow V.
]

The six-point carrier packages the three inequivalent index-two quotients simultaneously; QR's regular four-state carrier lies upstream of each one separately.

## 6. QR multiplication is an additional obstruction

The square-label set
[
QR(12)={0,1,4,9}
]
is only a set-valued labeling of the four-state quotient in the established construction. Under ordinary multiplication mod 12 it is not V4:
[
4^2=4,qquad 9^2=9,qquad0^2=0.
]

Therefore the six-cycle U(12) action cannot be promoted to a multiplicative QR(12) equivariance merely by identifying cardinalities or transporting labels.

The exact structure remains the affine/torsor pullback of v13.507, not ordinary quadratic-residue multiplication.

## 7. Crucial C4 obstruction: the two C4s are not the same action

v13.657 identified the cyclotomic subgroup
[
langlemathcal Z^3angle=langle	imes iangle
]
with the **scalar central** cone subgroup
[
langle iI_3angle.
]

But the denominator C4 in
[
mathcal C_6=S_4/C_4
]
is the stabilizer of an oriented Hamiltonian 4-cycle inside S4. It is generated by a tetrahedral 4-cycle and is noncentral in S4.

These C4s are abstractly isomorphic but act in fundamentally different ways:

- scalar (iI_3) is central in the linear cone group and is projectively invisible on null rays;
- the cycle-stabilizer C4 is a noncentral subgroup of S4 whose cosets define the six-point carrier.

Therefore
[
oxed{
C_4^{m scalar}
otequiv C_4^{m stabilizer}
}
]
as acting subgroups, and v13.657 does **not** supply a cyclotomic action on S4/C4.

This blocks the most tempting route
[
mathcal Z^3stackrel?{longrightarrow} C_4subset S_4
stackrel?{longrightarrow} S_4/C_4.
]

The first C4 is central/scalar; the second is noncentral/combinatorial.

## 8. Reversal gives another cycle-type obstruction

The orientation reversal of the six cycles is
[
ho=(a,b)(c,d)(e,f),
]
which is fixed-point-free on C6.

Every nonidentity element of the arithmetic U(12)=V4 subgroup acts instead with cycle type
[
2^2,1^2,
]
fixing two points.

Therefore
[
oxed{ho
otin U(12)	ext{ acting on }mathcal C_6.}
]

In particular, one cannot identify the global cycle-orientation reversal with any of the three arithmetic unit involutions (5,7,11).

This is consistent with the semilinear extension in v13.546-v13.548: reversal is extra structure, not an element of the arithmetic V4.

## 9. Relation to the earlier Pell mod-2 swap

v13.181 established that multiplication by
[
lambda=2+sqrt3
]
on the coefficient lattice has matrix
[
M_lambda=
egin{pmatrix}2&3\1&2end{pmatrix},
qquad
M_lambdamod2=
P=
egin{pmatrix}0&1\1&0end{pmatrix},
]
and that P is GL2(F2)-conjugate to the ramified transvection.

That exact Pell/ramified bridge remains valid.

However, it does not produce a six-state action. It lives on the two-dimensional coefficient parity space, and its order-two reduction is not a canonical choice among the three two-point quotients of C6 unless one independently specifies the chi12/Pell orientation quotient.

Thus the correct composition is
[
oxed{
	ext{Pell coefficient parity}
longleftrightarrow
	ext{ramified }F_2^2	ext{ action}
longrightarrow
U(12)/kerchi_{12}
cong{a,b},
}
]
not an equivalence with all of C6.

## 10. Relation to the sigma_A/sigma_B obstruction

The present test does not resolve the v13.567/v13.569 disagreement.

Indeed it sharpens why no automatic resolution should be expected:

- cyclotomic (i=zeta_{12}^3) supplies one marking criterion;
- cyclic-order orientation supplies another;
- the scalar C4 does not equal the S4 cycle-stabilizer C4;
- Pell sees only the chi12 quotient;
- QR regular states map onto each character quotient separately but receive no equivariant map from the full C6.

Therefore the six-point carrier does not contain enough canonical arithmetic marking to force the two criteria to coincide.

The previously found disagreement remains a genuine obstruction, not a missing calculation.

## 11. Exact verdict

There **is** a genuine Pell/QR-compatible shadow:
[
oxed{
mathcal C_6
supset
{a,b}
cong
U(12)/kerchi_{12},
}
]
and this two-state quotient is exactly the character quotient governing Pell orientation.

There is **no** genuine full six-point Pell/QR equivariance currently justified. Explicit obstructions are:

1. Pell orientation factors through chi12 and therefore has nontrivial kernel, while the C6 U(12) action is faithful.
2. No U(12)-equivariant map C6 -> V_QR exists because point stabilizers are order 2 upstairs and trivial downstairs.
3. QR(12) under ordinary multiplication is not V4.
4. The scalar/cyclotomic C4 of v13.657 is not the noncentral cycle-stabilizer C4 defining S4/C4.
5. Global cycle reversal has type 2^3, whereas every nonidentity arithmetic V4 element has type 2^2 1^2.
6. The sigma_A/sigma_B marking disagreement therefore survives.

Publication-safe summary:
[
oxed{
	ext{The six-cycle carrier organizes the three quadratic-character quotients,}
atop
	ext{but only its chi12 two-state factor is canonically Pell-oriented; no full six-state Pell/QR equivariance follows.}
}
]

## 12. Next controlled question

The useful next question is no longer “does C6 itself give Pell/QR equivariance?”; the answer is now sharply delimited.

The remaining structural target is to analyze whether the three quotient maps
[
V	o U(12)/kerchi
qquad
(chi=chi_{12},chi_{-4},chi_{-3})
]
assemble naturally into a single incidence object (for example the three nonzero dual characters / three perfect matchings), and whether adding the semilinear reversal supplies a canonical marking. Any such construction must be tested against the existing sigma_A/sigma_B no-go before being promoted.
