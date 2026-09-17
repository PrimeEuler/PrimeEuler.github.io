# Cone Derivation Ledger v13.562 — No-go for simultaneous marked V4 and complex-structure intertwining

## Status
Exact linear-algebra theorem continuing v13.557–v13.558 and the audited transported complex structure (renumbered by External Audit Round 49). This proves the incompatibility is not an artifact of the particular intertwiner P3.

## 1. Marked V4 data
Use the cone-kernel representatives

K5 = diag(1,-1,-1),
K7 = diag(-1,-1,1),
K11 = diag(-1,1,-1),

and the character-translation matrices

D5 = diag(1,-1,-1),
D7 = diag(-1,1,-1),
D11 = diag(-1,-1,1).

We seek all invertible real (indeed complex) 3x3 matrices Q satisfying, with labels fixed,

Q K5 Q^{-1}=D5,
Q K7 Q^{-1}=D7,
Q K11 Q^{-1}=D11.

Equivalently Q Kr = Dr Q for r=5,7,11.

## 2. Joint eigenspace signatures
For the domain basis e1,e2,e3, the joint (K5,K7,K11) signatures are

e1: (+,-,-),
e2: (-,-,+),
e3: (-,+,-).

For the codomain basis e1,e2,e3, the joint (D5,D7,D11) signatures are

e1: (+,-,-),
e2: (-,+,-),
e3: (-,-,+).

All three characters are distinct and one-dimensional. Therefore every marked intertwiner must map the corresponding joint eigenspaces as

Q e1 in span(e1),
Q e2 in span(e3),
Q e3 in span(e2).

Hence the complete family is

Q(a,b,c) = [[a,0,0],[0,0,c],[0,b,0]],

with a,b,c nonzero.

This classification holds over R or C.

## 3. Complex structure
Use the 3D extension of the transported cone complex structure

J = [[0,-1,0],[1,0,0],[0,0,1]].

Thus J is the quarter-turn on span(e1,e2) and fixes the normal axis span(e3).

The condition

Q J Q^{-1}=J

is equivalent to QJ=JQ.

For the full marked-intertwiner family,

QJ = [[0,-a,0],[0,0,c],[b,0,0]],

while

JQ = [[0,0,-c],[a,0,0],[0,b,0]].

Equality forces, already from the first column,

(0,0,b)^T=(0,a,0)^T,

so a=b=0, contradicting invertibility. Therefore no invertible Q in the marked V4 intertwiner family commutes with J.

Thus

NO invertible Q satisfies simultaneously

QKrQ^{-1}=Dr for r=5,7,11

and

QJQ^{-1}=J.

## 4. Coordinate-free proof
The obstruction can be seen without entries.

The marked V4 intertwining conditions force

Q(span(e2)) = span(e3),
Q(span(e3)) = span(e2).

But J has a distinguished real fixed line

Fix(J)=span(e3).

Any Q satisfying QJQ^{-1}=J must preserve Fix(J):

Q(Fix(J))=Fix(J).

Hence it must send span(e3) to itself. The marked V4 intertwining instead sends span(e3) to span(e2). Since these are distinct lines, contradiction.

This proves the no-go invariantly relative to the fixed marked representations.

## 5. Conclusion
The incompatibility observed for P3 in v13.558 is structural, not a poor choice of intertwiner.

There is a full 3-parameter family of marked V4 intertwiners,

Q(a,b,c) = [[a,0,0],[0,0,c],[0,b,0]], a b c != 0,

but none preserves the chosen complex structure J.

Therefore one cannot simultaneously make

T5 <-> D5,
T7 <-> D7,
T11 <-> D11

at generator level and preserve the cone/A3 complex quarter-turn J under a single linear change of basis.

The two exact bridges remain individually valid:

1. the six-ray/cyclic-order bridge gives a projective generator-level identification of mod-12 translations with native cone V4 reflections;
2. the transported-complex bridge identifies the cone complex structure with the A3 transverse complex structure.

They cannot be fused into one marked linear intertwiner preserving J.

## Guardrails
- This is a no-go for the fixed marked labels r=5,7,11 and the fixed J above. It does not forbid an automorphic relabeling of V4 generators, nor a conjugated/modified complex structure.
- The theorem holds over C as well as R because the joint eigenspace argument is unchanged.
- No Pell, Suzuki, QR dynamical, or phase-law consequence is asserted.
