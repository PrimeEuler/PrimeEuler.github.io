# Cone Derivation Ledger v13.563 — V4 Automorphisms and J-Compatible Relabelings

## Status
Exact finite classification continuing v13.562. All six automorphisms of the three nonidentity elements of V4 are tested. No arithmetic dynamical claim is asserted.

## 1. Data
Use the extracted cone-kernel matrices

K5 = diag(1,-1,-1),
K7 = diag(-1,-1,1),
K11 = diag(-1,1,-1),

and the arithmetic character matrices

D5 = diag(1,-1,-1),
D7 = diag(-1,1,-1),
D11 = diag(-1,-1,1).

The complex structure is

J = [[0,-1,0],[1,0,0],[0,0,1]].

For sigma in Aut(V4) ~= S3, seek invertible Q such that, for r=5,7,11,

Q K_{sigma(r)} Q^{-1} = D_r

and

Q J Q^{-1} = J.

Equivalently,

Q K_{sigma(r)} = D_r Q,
QJ=JQ.

## 2. Exhaustive six-case result
Solving the simultaneous linear equations exactly for each permutation sigma gives:

1. sigma=(5)(7)(11): no nonzero solution compatible with J.
2. sigma=(5)(7 11): solutions exist and are invertible.
3. sigma=(5 7)(11): no nonzero solution compatible with J.
4. sigma=(5 7 11), i.e. 5->7, 7->11, 11->5: no nonzero solution compatible with J.
5. sigma=(5 11 7), i.e. 5->11, 7->5, 11->7: solutions exist and are invertible.
6. sigma=(5 11)(7): no nonzero solution compatible with J.

Thus exactly two of the six V4 automorphisms are J-compatible.

## 3. First compatible relabeling
For

sigma_A: 5->5, 7->11, 11->7,

the complete solution family is

Q_A(a,c) = diag(a,a,c),

with a*c != 0.

Indeed Q_A commutes with J because its first two diagonal entries agree, and direct conjugation gives

Q_A K5 Q_A^{-1}=K5=D5,
Q_A K11 Q_A^{-1}=K11=D7,
Q_A K7 Q_A^{-1}=K7=D11.

The simplest representative is Q_A=I. Therefore, after swapping the arithmetic labels 7 and 11 on the cone-kernel side, the two representations literally coincide in the current basis and J is literally preserved.

## 4. Second compatible relabeling
For

sigma_B: 5->11, 7->5, 11->7,

the complete solution family is

Q_B(a,c) = [[0,-a,0],[a,0,0],[0,0,c]],

with a*c != 0.

Equivalently,

Q_B(a,c) = diag(a,a,c) J,

because J=[[0,-1,0],[1,0,0],[0,0,1]].

Since diag(a,a,c) commutes with J, Q_B also commutes with J. Directly,

Q_B K11 Q_B^{-1}=D5,
Q_B K5 Q_B^{-1}=D7,
Q_B K7 Q_B^{-1}=D11.

The simplest representative is Q_B=J.

## 5. Conceptual classification
The J-fixed line is L0=<e3>, while J rotates the transverse plane L1+L2=<e1,e2>. A J-compatible intertwiner must preserve L0 and act complex-linearly on the transverse plane.

Among the three nontrivial K-elements, K7 is distinguished by fixing e3:

K7 e3 = +e3,

whereas K5 and K11 negate e3. Among the D-elements, D11 is distinguished by fixing e3:

D11 e3 = +e3,

whereas D5 and D7 negate e3.

Therefore J-compatibility forces

sigma(11)=7,

because the target D11 must be supplied by K7. Once this is imposed, sigma may send 5 and 7 to the remaining K-labels 5 and 11 in either order. Hence exactly 2!=2 automorphisms survive.

They are precisely

sigma_A=(7 11)

and

sigma_B=(5 11 7)

in cycle notation on the labels {5,7,11}.

## 6. J-compatible relabeling set
The two compatible relabelings are not a subgroup of Aut(V4): sigma_A has order 2 and sigma_B has order 3, while their set has only two elements and does not contain the identity.

Rather, they form the fiber/coset-like set of automorphisms satisfying the single structural condition

sigma(11)=7.

Equivalently, it is a two-element torsor for the stabilizer of the remaining two labels after the distinguished normal-axis correspondence is fixed.

## 7. Exact conclusion
The v13.562 no-go is specific to the original marked labeling. It disappears under exactly two of the six V4 automorphisms.

The strongest result is:

There exists Q with

Q K_{sigma(r)} Q^{-1}=D_r for all r in {5,7,11}

and

QJQ^{-1}=J

if and only if

sigma(11)=7.

For sigma_A=(7 11), all such Q are diag(a,a,c), ac != 0.

For sigma_B=(5 11 7), all such Q are [[0,-a,0],[a,0,0],[0,0,c]], ac != 0.

Thus the complex structure selects the correspondence

K7 <-> D11

between the unique nontrivial V4 elements fixing the J-normal line. The residual ambiguity is only the interchange of the two transverse V4 labels.

## Guardrails
1. This classification concerns automorphisms/relabelings of the abstract V4 and exact 3D real/complex linear representations.
2. The surviving relabeling sigma is not asserted to be canonically arithmetic without an additional argument selecting one of the two transverse orientations.
3. The two surviving automorphisms do not themselves form a subgroup.
4. No Pell, QR dynamical, Suzuki, or phase-law consequence follows from this finite representation-theoretic result alone.
