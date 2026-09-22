# Cone Derivation Ledger v13.657 — Exact Cyclotomic Identification of the Scalar Cone C4

Date: 2026-09-22

Status: exact representation-theoretic continuation of v13.656 priority 1. This closes the repeatedly-open question for the **scalar** cone (C_4=langle iI_3angle). It does **not** identify the arithmetic-negation lift (A) with that scalar generator.

## 0. Collision/relevance check

Immediately before this write, the live repository tip is v13.656. No later ledger entry is present, so v13.657 is free.

## 1. Two order-four operators to compare

From v13.431, on
[
K=mathbf Q(zeta_{12})=mathbf Q(i,sqrt3),
qquad mathcal Z=	imeszeta_{12},
]
one has
[
oxed{mathcal Z^3=	imes i.}
]

Using the rational character basis
[
B_chi=(1,i,isqrt3,sqrt3),
]
the action is
[
1mapsto i,quad imapsto-1,quad isqrt3mapsto-sqrt3,quad sqrt3mapsto isqrt3.
]
Hence
[
[mathcal Z^3]_{B_chi}
=
egin{pmatrix}
0&-1&0&0\
1&0&0&0\
0&0&0&1\
0&0&-1&0
end{pmatrix},
]
which is two rational copies of the irreducible (x^2+1) quarter-turn module (the second block is the same module after the harmless ordered-pair convention ((sqrt3,isqrt3))).

From v13.537/v13.548, the complexified cone group has scalar subgroup
[
mu_4={I_3,iI_3,-I_3,-iI_3}
=langle iI_3anglecong C_4.
]

## 2. Put both actions over the same scalar field

The cyclotomic field is two-dimensional over (mathbf Q(i)):
[
K=mathbf Q(i)oplus sqrt3,mathbf Q(i).
]
Therefore (mathcal Z^3=	imes i) is simply
[
oxed{mathcal Z^3=iI_2}
]
as a (mathbf Q(i))-linear operator on (Kcongmathbf Q(i)^2).

Restrict the cone carrier to the natural (mathbf Q(i))-form
[
V_{m cone}=mathbf Q(i)^3subsetmathbf C^3.
]
The scalar cone generator is
[
oxed{u=iI_3.}
]

Thus the two operators are not merely abstract order-four elements: they are the same scalar (i) acting on free (mathbf Q(i))-modules of ranks 2 and 3.

## 3. Explicit intertwiner

Write every (xin K) uniquely as
[
x=a+bsqrt3,qquad a,binmathbf Q(i).
]
Define the (mathbf Q(i))-linear embedding
[
Phi:Klongrightarrow V_{m cone},
qquad
Phi(a+bsqrt3)=(a,b,0)^T.
]
Then
[
Phi(mathcal Z^3x)
=Phi(ix)
=(ia,ib,0)^T
=iI_3(a,b,0)^T
=u,Phi(x).
]
Therefore
[
oxed{Phicircmathcal Z^3=(iI_3)circPhi.}
]

More generally, for every (kinmathbf Z),
[
oxed{Phicirc(mathcal Z^3)^k=(iI_3)^kcircPhi.}
]

Consequently the map
[
	heta:langlemathcal Z^3angle	olangle iI_3angle,
qquad
(mathcal Z^3)^kmapsto(iI_3)^k
]
is an explicit (C_4)-isomorphism realized by an operator intertwiner on the embedded cyclotomic module.

## 4. Rational representation check

If both carriers are forgotten down to (mathbf Q), multiplication by (i) has minimal polynomial
[
x^2+1.
]
Hence
[
Kcong W^{oplus2},
qquad
V_{m cone}cong W^{oplus3},
]
as rational (C_4)-modules, where (W) is the unique two-dimensional rational quarter-turn module.

This explains both facts simultaneously:

1. there is a canonical common (C_4) representation type and the explicit injection (Phi) above;
2. there cannot be an invertible intertwiner between the *entire* cyclotomic and cone carriers, because their rational dimensions are (4) and (6).

The dimension mismatch is therefore not an obstruction to identifying the scalar (C_4); it only forbids falsely identifying the two full ambient representations.

## 5. Important correction to the v13.656 handoff wording

v13.656 priority 1 says “the order-four generator (A) (equivalently the scalar (iI)...)”. The parenthetical “equivalently” is too strong.

Indeed
[
A^2=R_Y=operatorname{diag}(1,-1,1),
]
whereas
[
(iI_3)^2=-I_3.
]
Therefore
[
oxed{A
eq iI_3}
]
and the cyclic actions (langle Aangle) and (langle iI_3angle) are not the same embedded subgroup/action. This is consistent with the explicit guardrails already present in v13.534 and v13.548.

What is now identified with the cyclotomic operator is precisely the **scalar central**
[
oxed{langle iI_3angleleftrightarrowlanglemathcal Z^3angle,}
]
not the arithmetic lift (langle Aangle).

## 6. Exact conclusion

The most-repeated open question from v13.534/v13.537/v13.545 closes positively for the scalar quarter-turn:
[
oxed{
mathcal Z^3=	imes i
quadlongleftrightarrowquad
iI_3in G_{m lin}
}
]
through the explicit (mathbf Q(i))-linear intertwiner
[
oxed{Phi(a+bsqrt3)=(a,b,0)^T.}
]

So the central (C_4) of the complexified cone is not merely abstractly isomorphic to the cyclotomic cubic-step (C_4): both are restrictions of the same scalar (i)-action, and an explicit shared representation map exists.

## 7. Guardrails and next target

- This does not identify (A) with (mathcal Z^3); their squares already exclude that generator-level identification.
- This does not by itself produce a Pell, QR, Suzuki-spectral, or Moonshine consequence.
- v13.567/v13.569's orientation-versus-cyclotomic relabeling obstruction remains genuine; the present scalar identification does not erase it.
- Paper A still need not absorb this result automatically; it belongs first to the complexification/representation bridge.

With priority 1 now closed for the scalar (C_4), the next productive target from v13.656 is priority 2: identify the natural A3/U(12) six-point (S_4/C_4) object, expected representation-theoretically to be the six **oriented Hamiltonian 4-cycles modulo cyclic rotation** on the tetrahedral vertex set, rather than the six edges (S_4/V_4).
