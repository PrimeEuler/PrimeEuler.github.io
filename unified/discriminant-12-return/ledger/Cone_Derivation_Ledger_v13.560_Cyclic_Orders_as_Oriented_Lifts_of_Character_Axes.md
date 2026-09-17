# Cone Derivation Ledger v13.560 — Cyclic Orders as Oriented Lifts of Character Axes

**Renumbering note:** originally filed as v13.555, which collided with the already-pushed `Cone_Derivation_Ledger_v13.555_M16001_Remaining_Outward_Certification_DAG.md`. Renumbered to v13.560 during External Audit Round 49. Mathematical content is unchanged.

## Status
Exact combinatorial/representation-theoretic continuation of v13.545 and v13.554. No new arithmetic dynamical claim is promoted.

## 1. Three perfect matchings from the six cyclic orders
For an oriented cyclic ordering `[u,v,w,x]` of `{1,5,7,11}`, define its opposite-pair matching

`M([u,v,w,x]) = {{u,w},{v,x}}`.

Orientation reversal preserves this matching. Using the v13.545 ray/cyclic-order table gives exactly

- `{a,b}` -> `{{1,11},{5,7}}` -> chi_12,
- `{c,d}` -> `{{1,5},{7,11}}` -> chi_-4,
- `{e,f}` -> `{{1,7},{5,11}}` -> chi_-3.

Thus the six-ray set is a two-sheet/orientation lift of the three character matchings:

`N_6 -> {chi_12, chi_-4, chi_-3}`,

with deck involution

`rho=(a b)(c d)(e f)`.

Equivalently, as S4-sets,

`S4/C4 -> S4/D8`,

whose fiber is `D8/C4 ~= C2`.

## 2. Character-axis geometry
In the A3 character space

`W = span_R(chi_-4, chi_-3, chi_12)`,

the three matchings correspond to the three coordinate axes. With ordered basis

`(chi_-4, chi_-3, chi_12)`,

the transverse complex plane of v13.554 is

`W_perp = span(chi_-4,chi_-3)`,

and the remaining axis is

`R chi_12`.

Therefore, relative to the chosen v13.554 intertwiner, chi_12 is exactly the coordinate axis normal to the transported cone complex plane.

This is a statement about the chosen character-coordinate realization; it is not a claim that chi_12 is canonically a geometric cone normal before the intertwiner is chosen.

## 3. Transported complex structure
v13.554 gave

`(u,v)^T = P (X,Y)^T`,

with

`P=[[1,-1],[1,1]]`,

so

`u=X-Y`, `v=X+Y`, and

`w=u+i v=(1+i)(X+iY)=(1+i)z`.

Multiplication by i is therefore

`J_chi=[[0,-1],[1,0]]`,

hence

`chi_-4 -> chi_-3`,

`chi_-3 -> -chi_-4`.

The chi_12 axis is fixed as the normal axis in the natural 3D extension

`J_hat = [[0,-1,0],[1,0,0],[0,0,1]]`.

This 3D extension has order four and acts as a quarter-turn about the chi_12 axis.

## 4. Exact relation to the six oriented lifts
The six rays do not become six A3 root/edge directions. Instead they organize as three reversal pairs lying over the three character axes:

`{a,b} -> chi_12 axis`,

`{c,d} -> chi_-4 axis`,

`{e,f} -> chi_-3 axis`.

The two members of each pair are the two cyclic orientations of the same opposite-pair matching. Thus the correct exact statement is

`null ray = oriented lift of a character matching`,

not

`null ray = A3 edge/root direction`.

The reversal involution rho forgets the orientation while preserving the underlying character axis.

## 5. Is the fiber canonically +/- i?
No, not from the presently verified structure alone.

The fibers are canonically C2-torsors once the cyclic-order model is chosen: each matching has two opposite cyclic orientations exchanged by rho. Calling these two sheets `+i` and `-i` requires an additional choice of orientation/phase convention. The transported complex structure supplies a natural quarter-turn on the chi_-4/chi_-3 plane, but it does not by itself canonically label both lifts over all three axes by +/-i.

So the exact conclusion is:

`S4/C4 -> S4/D8`

is the orientation double cover of the three character matchings, while a global identification of each two-point fiber with `{+i,-i}` remains convention-dependent unless an additional equivariant phase structure is proved.

## 6. Structural summary
The verified chain is now

`6 null rays`

`~= S4/C4`

`= six oriented cyclic orders`

`-- quotient by rho -->`

`3 perfect matchings`

`~= S4/D8`

`= {chi_12,chi_-4,chi_-3} character axes`.

Under the v13.554 coordinate choice,

`span(chi_-4,chi_-3)` is the transported cone complex plane,

`chi_12` is its normal axis,

and multiplication by i is the exact quarter-turn

`[[0,-1],[1,0]]`.

## Guardrails
1. The six rays are not the six A3 edges/root directions; v13.543 forbids that S4-set identification.
2. The ray-to-cyclic-order identification depends on the chosen generator correspondence/basepoint from v13.545.
3. The chi_12-normal statement is relative to the chosen A3 coordinate basis and v13.554 intertwiner.
4. The two lifts over each character axis are exactly orientation-reversal partners, but a canonical global `+i/-i` labeling has not been proved.
5. No Pell, Suzuki, QR dynamical, or phase-law consequence is asserted here.
