# Cone Derivation Ledger v13.507 — QR/circle pullbacks to F2^2 and signed extension

## Status
Exact finite algebra audit. This refines v13.499–v13.500 and v13.506. It does **not** promote the earlier QR coincidence to a multiplicative isomorphism.

## 1. Positive-sheet bit coordinates
Use

r(a,b)=5^a 7^b mod 24 = 1+4a+6b,  (a,b) in F2^2,

with ordering

00 -> 1, 10 -> 5, 01 -> 7, 11 -> 11.

On the cone section

X=(r-1)/2, T=(r+1)/2=X+1,

so

X: 00,10,01,11 -> 0,2,3,5,
T: 00,10,01,11 -> 1,3,4,6.

## 2. QR labels
Let Q={0,1,4,9}=QR(12), and use the proposed square labels

q_X(a,b)=X(a,b)^2 mod 12,
q_T(a,b)=T(a,b)^2 mod 12.

Explicitly,

q_X: 00->0, 10->4, 01->9, 11->1,
q_T: 00->1, 10->9, 01->4, 11->0.

Thus both are bijections F2^2 -> Q as sets.

More strongly, they are related by the affine translation

q_T(a,b)=q_X(a+1,b+1),

where additions are in F2. Equivalently the circle/QR labeling is the X/QR labeling translated by the nonzero vector (1,1).

This is an exact finite identity for these four states.

## 3. Does ordinary QR multiplication become XOR?
No.

Under ordinary multiplication mod 12, Q is not V4. For example

4*4=4, 9*9=9, 0*0=0,

so nonidentity elements are idempotent rather than order two. Also 0 has no group inverse. Hence q_X and q_T are **not** homomorphisms from (F2^2,+) to (Q,multiplication mod 12).

If one transports the V4 operation through either bijection by definition,

q_X(v) boxplus_X q_X(w) := q_X(v+w),
q_T(v) boxplus_T q_T(w) := q_T(v+w),

then each transported law is of course XOR in pulled-back coordinates. That is a valid induced V4 algebra, but it must not be confused with ordinary multiplication of quadratic residues mod 12.

Because q_T=q_X o tau_h with h=(1,1), the two transported group laws have different identity labels:

identity for boxplus_X: q_X(00)=0,
identity for boxplus_T: q_T(00)=1.

The affine shift h is not a linear group automorphism fixing the origin; it is a torsor translation between the two labelings.

## 4. Signed extension
From v13.506 write

r(a,b,c)=(-1)^c(1+4a+6b), (a,b,c) in F2^3.

The cone involution r->-r is

J(a,b,c)=(a,b,c+1),

and geometrically

J(X,T)=(-T,-X).

After squaring mod 12, signs disappear but X and T exchange. Exact formulas are

q_X(a,b,c)=q_X(a+c,b+c,0),
q_T(a,b,c)=q_X(a+c+1,b+c+1,0),

with all bit additions mod 2. Equivalently,

q_X(a,b,c+1)=q_T(a,b,c),
q_T(a,b,c+1)=q_X(a,b,c).

Therefore the signed involution extends consistently as the swap of the two QR projections:

J: (q_X,q_T) -> (q_T,q_X).

This exactly mirrors (X,T)->(-T,-X), because squaring removes the minus signs.

## 5. Interpretation
There is a genuine exact structure stronger than a bare four-set coincidence:

1. The positive cone V4 is F2^2.
2. The X-square and T-square maps are two bijective QR(12) labelings.
3. They differ by the fixed affine translation h=(1,1) in F2^2.
4. The signed C2 involution exchanges those two labelings exactly.
5. Ordinary multiplication on QR(12) does **not** realize the V4/XOR law.

Thus the correct object is an affine/torsor pair of QR labelings over the V4 carrier, with the third signed bit swapping the pair. It is not a QR multiplicative-group identification.

A compact formulation is

q_X(v,c)=q_X^+(v+c h),
q_T(v,c)=q_X^+(v+(c+1)h),  h=(1,1),

so the signed cube F2^3 projects to an ordered pair of QR labels, and c->c+1 swaps the pair.

## Guardrail
This finite cone/QR structure does not alter v13.502–v13.504: U(24) cone units remain disjoint from the Suzuki even ramified residue stratum. No Suzuki, spectral, RH, or GRH consequence is asserted here.