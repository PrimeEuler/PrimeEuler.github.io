# Cone Derivation Ledger v13.481 — Affine S4 Conjugacy Classes in Character Coordinates

## Scope
This entry matches the 24 explicit affine maps from v13.476 and v13.488 (originally filed as v13.477, renumbered in External Audit Round 37 due to a version collision) to the five conjugacy classes of S4, and hence to the trace/eigenvalue data of v13.479.

No new Pell or Suzuki theorem is asserted.

## Normalization
Work on F4={0,1,w,w^2}, with w^2+w+1=0. Use the oriented affine identification

- a(1)=0,
- a(5)=1,
- a(7)=w^2,
- a(11)=w.

The character triples (chi_12,chi_-3,chi_-4) are

- 1 : (+,+,+),
- 5 : (-,-,+),
- 7 : (-,+,-),
- 11: (+,-,-).

The six linear maps are

- I(t)=t,
- A(t)=w t,
- A^2(t)=w^2 t,
- F(t)=t^2,
- AF(t)=w t^2,
- A^2F(t)=w^2 t^2.

Every affine element is Phi_{r,L}(t)=a(r)+L(t).

## Complete 24-element class assignment

| r | character triple | L | permutation on {0,1,w,w^2} | S4 class |
|---|---|---|---|---|
| 1 | (+,+,+) | I | () | 1^4 |
| 1 | (+,+,+) | A | (1 w w^2) | 3 1 |
| 1 | (+,+,+) | A^2 | (1 w^2 w) | 3 1 |
| 1 | (+,+,+) | F | (w w^2) | 2 1^2 |
| 1 | (+,+,+) | AF | (1 w) | 2 1^2 |
| 1 | (+,+,+) | A^2F | (1 w^2) | 2 1^2 |
| 5 | (-,-,+) | I | (0 1)(w w^2) | 2^2 |
| 5 | (-,-,+) | A | (0 1 w^2) | 3 1 |
| 5 | (-,-,+) | A^2 | (0 1 w) | 3 1 |
| 5 | (-,-,+) | F | (0 1) | 2 1^2 |
| 5 | (-,-,+) | AF | (0 1 w^2 w) | 4 |
| 5 | (-,-,+) | A^2F | (0 1 w w^2) | 4 |
| 7 | (-,+,-) | I | (0 w^2)(1 w) | 2^2 |
| 7 | (-,+,-) | A | (0 w^2 w) | 3 1 |
| 7 | (-,+,-) | A^2 | (0 w^2 1) | 3 1 |
| 7 | (-,+,-) | F | (0 w^2 1 w) | 4 |
| 7 | (-,+,-) | AF | (0 w^2) | 2 1^2 |
| 7 | (-,+,-) | A^2F | (0 w^2 w 1) | 4 |
| 11 | (+,-,-) | I | (0 w)(1 w^2) | 2^2 |
| 11 | (+,-,-) | A | (0 w 1) | 3 1 |
| 11 | (+,-,-) | A^2 | (0 w w^2) | 3 1 |
| 11 | (+,-,-) | F | (0 w 1 w^2) | 4 |
| 11 | (+,-,-) | AF | (0 w w^2 1) | 4 |
| 11 | (+,-,-) | A^2F | (0 w) | 2 1^2 |

## Class decomposition in affine coordinates

### Identity, size 1
{(1,I)}.

### Double transpositions, size 3
Exactly the three nonzero pure translations:
{(5,I),(7,I),(11,I)}.
Thus the normal V4 is exactly {identity} union {the 3 elements of class 2^2}.

### Three-cycles, size 8
All affine elements whose linear part is A or A^2:
{(r,A),(r,A^2): r in {1,5,7,11}}.
Hence the two order-3 linear maps each generate a four-element affine coset, and every element in those two cosets is a 3-cycle.

### Transpositions, size 6
One element in each reflection coset for each appropriate translation:
{(1,F),(1,AF),(1,A^2F),(5,F),(7,AF),(11,A^2F)}.

### Four-cycles, size 6
The complementary elements in the three reflection cosets:
{(5,AF),(5,A^2F),(7,F),(7,A^2F),(11,F),(11,AF)}.

Thus each of the three reflection-type linear directions splits its four affine lifts into two transpositions and two four-cycles.

## Hadamard traces and eigenvalues
By v13.479, the 4-dimensional Hadamard/permutation representation 1+3_std has class data:

| class | size | eigenvalues on 1+3 | trace | eigenvalues on 3_std | trace_3 |
|---|---:|---|---:|---|---:|
| 1^4 | 1 | 1,1,1,1 | 4 | 1,1,1 | 3 |
| 2 1^2 | 6 | 1,1,1,-1 | 2 | 1,1,-1 | 1 |
| 2^2 | 3 | 1,1,-1,-1 | 0 | 1,-1,-1 | -1 |
| 3 1 | 8 | 1,1,omega,omega^2 | 1 | 1,omega,omega^2 | 0 |
| 4 | 6 | 1,i,-1,-i | 0 | i,-1,-i | -1 |

Therefore the trace of every explicit Phi_{r,L} is read off immediately from the class table above.

## Structural consequences
1. Pure nonzero translations are precisely the double-transposition class. This realizes the canonical normal Klein four in S4.
2. The A/A^2 affine cosets are exactly the eight 3-cycles.
3. Reflection-type affine cosets split into the six transpositions and six 4-cycles.
4. The quotient S4/V4=S3 remembers the linear phase type, but does not by itself distinguish transpositions from 4-cycles: the translation component is essential.
5. In the Hadamard basis, the same distinction is encoded by the signed monomial matrix D_r P_L. The character triple supplies D_r; L supplies P_L.

## Guardrail
The character triple labels the chosen oriented affine translation V4. Its arithmetic components retain their distinct meanings: chi_12 is Pell-time orientation, chi_-3 is the residue-Frobenius bit, and chi_-4 is the lift/derivation bit. The abstract S3 permutation symmetry of the three nontrivial Fourier directions does not identify those arithmetic mechanisms.
