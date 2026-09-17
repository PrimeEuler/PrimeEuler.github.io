# Cone Derivation Ledger v13.556 — Three-Pair Quotient S4 -> S3

## Status
Exact permutation calculation from the verified six-ray generators. This identifies the standard S4/V4 ~= S3 quotient on the three reversal pairs / character matchings.

## 1. Input
On the six rays `{a,b,c,d,e,f}`, the verified generators are

`r=(a c b d)` with e,f fixed,

`s=(a f d)(b e c)`.

The reversal fibers from v13.560 are

`P_12={a,b}` corresponding to chi_12,

`P_-4={c,d}` corresponding to chi_-4,

`P_-3={e,f}` corresponding to chi_-3.

## 2. Induced action of r
Since

`r(a)=c`, `r(b)=d`,

we have `r(P_12)=P_-4`.

Also

`r(c)=b`, `r(d)=a`,

so `r(P_-4)=P_12`, while e,f are fixed, so `r(P_-3)=P_-3`.

Therefore

`bar r = (P_12 P_-4)`.

Equivalently on character-axis labels,

`bar r = (chi_12 chi_-4)`, with chi_-3 fixed.

## 3. Induced action of s
From `s=(a f d)(b e c)`:

- a,b map to f,e, hence `P_12 -> P_-3`;
- e,f map to c,d, hence `P_-3 -> P_-4`;
- c,d map to b,a, hence `P_-4 -> P_12`.

Therefore

`bar s = (P_12 P_-3 P_-4)`.

Equivalently

`bar s = (chi_12 chi_-3 chi_-4)`.

## 4. Quotient homomorphism
The induced permutations generate all S3 because `bar r` is a transposition and `bar s` is a 3-cycle. Thus the pair action defines a surjective homomorphism

`pi:S4 -> S3`,

with

`pi(r)=(chi_12 chi_-4)`,

`pi(s)=(chi_12 chi_-3 chi_-4)`.

Since |S4|=24 and |S3|=6,

`|ker pi|=4`.

The unique normal subgroup of S4 of order 4 is the Klein four subgroup

`V4={1,(12)(34),(13)(24),(14)(23)}`

in an abstract four-letter realization. Hence

`ker pi ~= V4`.

Therefore

`S4/V4 ~= S3`.

## 5. Exact sequence
The three-pair action gives the standard exact sequence

`1 -> V4 -> S4 -> S3 -> 1`.

Here S3 acts faithfully by permuting the three perfect matchings / nonprincipal character axes

`{chi_12,chi_-4,chi_-3}`.

This is precisely the standard action of S4 on the three partitions of four labels into two unordered pairs.

## 6. Relation to the six-ray orientation cover
The six-ray S4-set is `S4/C4`; quotienting each reversal pair gives `S4/D8`. The induced three-point action factors through `S4/V4 ~= S3`:

`S4 -> S3 -> Sym({P_12,P_-4,P_-3})`.

The reversal rho is external to this S4 and acts trivially on all three pairs. In the extended 48-element group `S4 x C2`, the pair-action kernel is therefore `V4 x C2`, of order 8.

## 7. Connection to the mod-12 V4 structure
This computation recovers an exact Klein-four kernel inside the verified S4 cone symmetry. It matches the abstract `V4 normal S4` structure used elsewhere in the mod-12 character geometry. However, this statement alone does not identify each of these four S4-kernel elements with a particular native cone reflection or with a particular arithmetic U(12)/U(24) carrier element. Such a generator-level intertwiner must be computed separately.

## Guardrails
1. `ker pi ~= V4` is exact as a subgroup of the verified S4 action.
2. Do not automatically identify this kernel element-by-element with the native geometric V4 `{1,R_X,R_Y,R_XR_Y}` or with arithmetic U(12); only the abstract/representation-theoretic V4 structure is established here.
3. The three points are perfect matchings / character axes, not six A3 root directions.
4. Reversal rho lies in the separately adjoined C2 and is not an element of this S4 kernel.
