# Cone Derivation Ledger v13.599 — General Equal-Spin Tetrahedron Kernel Parity and D8 Decomposition Theorem

Date: 2026-09-19

Status labels: [S] standard representation fact, [D] exact derived, [Audit] algebraic proof, [G] structural interpretation, [O] open.

## Coordination / collision and relevance check

Immediately before this write, the live ledger contained v13.598 entries and v13.599 was free. The live directory currently contains two separately named v13.598 files, so this entry deliberately advances to v13.599 rather than attempting to alter either parallel checkpoint.

The active magnetic-driver lane was also checked. v13.600 (renumbered from v13.598 during External Audit Round 63) establishes the exact off-resonant magnetic Hamiltonian

[
H_r=-Delta J_z-gamma B_1J_x
]

and retains the SU(2) weighted path

[
Y_q=sqrt{(j-q)(j+q+1)}.
]

That lane is structurally relevant because it supplies another finite SU(2) weighted path, but its path matrix is symmetric/Hermitian and its dynamics are a spin rotation. The tetrahedral volume matrix below is imaginary antisymmetric/Hermitian and acts on the recoupling/intertwiner label k. No operator equality between these paths is claimed.

This checkpoint generalizes the tetrahedron results of v13.591, v13.593, and v13.596.

---

## 1. [S] Equal-spin four-valent intertwiner space

For four equal spins j, with (2jinmathbb Z_{ge1}),

[
mathcal H_j=operatorname{Inv}_{SU(2)}(V_j^{otimes4})
]

has the recoupling basis

[
|kangle,qquad k=0,1,ldots,2j,
]

so

[
oxed{dimmathcal H_j=2j+1.}
]

Use the oriented triple product

[
Q_j=mathbf J_1cdot(mathbf J_2	imesmathbf J_3)
]

with the orientation convention already used in the preceding tetrahedron checkpoints.

---

## 2. [D] Exact weighted-path form

In the ordered k basis, the equal-spin volume operator has the tridiagonal form

[
oxed{
Q_j=i
egin{pmatrix}
0&-a_1&0&cdots&0\\
a_1&0&-a_2&ddots&dots\\
0&a_2&0&ddots&0\\
dots&ddots&ddots&ddots&-a_{2j}\\
0&cdots&0&a_{2j}&0
end{pmatrix},
}
]

with

[
oxed{
a_k=
rac{k^2ig[(2j+1)^2-k^2ig]}
{4sqrt{4k^2-1}},
qquad
k=1,ldots,2j.
}
]

For every allowed k,

[
k>0,qquad k<2j+1,qquad 4k^2-1>0,
]

hence

[
oxed{a_k>0.}
]

Therefore every edge of the path

[
0-1-2-cdots-2j
]

is present.

The low-spin matrices previously computed are recovered by this formula.

---

## 3. [D][Audit] Bipartite parity form

Define k-parity

[
oxed{H|kangle=(-1)^k|kangle.}
]

Then

[
H^2=I
]

and, because Q_j connects only neighboring k,

[
oxed{HQ_jH=-Q_j.}
]

Separate the basis into even and odd k. In that reordered basis,

[
oxed{
Q_j=i
egin{pmatrix}
0&-B\\
B^T&0
end{pmatrix},
}
]

where B is a real bidiagonal matrix built from the positive (a_k).

Thus Q_j is a bipartite weighted-path operator, with H equal to +1 on the even part and -1 on the odd part.

---

## 4. [D][Audit] Kernel theorem: half-integer j

Let

[
j=n+rac12,qquad ninmathbb Z_{ge0}.
]

Then

[
2j+1=2n+2.
]

There are exactly (n+1) even k values and (n+1) odd k values. Hence B is square.

With the natural parity ordering, B is bidiagonal and its diagonal entries are alternating path weights, all strictly positive. Therefore

[
det B
eq0.
]

Consequently

[
oxed{ker Q_j={0}qquad (jinmathbb Z+	frac12).}
]

Equivalently,

[
oxed{operatorname{rank}Q_j=2j+1}
]

for half-integer j.

So the entire intertwiner space is the nonzero-volume sector.

---

## 5. [D][Audit] Kernel theorem: integer j

Let

[
j=n,qquad ninmathbb Z_{ge1}.
]

Then

[
2j+1=2n+1.
]

There are

[
n+1
]

even k states and

[
n
]

odd k states. Therefore B has size

[
(n+1)	imes n.
]

Because its n diagonal/pivot weights are nonzero, B has full column rank n. Hence

[
operatorname{rank}Q_j=2n
]

and

[
oxed{dimker Q_j=1.}
]

Moreover the kernel lies entirely in the larger parity sector, namely even k:

[
oxed{
ker Q_jsubsetmathcal H_{m even}.
}
]

Thus

[
oxed{
dimker Q_j=
egin{cases}
1,&jinmathbb Z,\\
0,&jinmathbb Z+rac12.
end{cases}
}
]

This proves the integer/half-integer kernel pattern observed at j=1/2,1,3/2,2,5/2.

---

## 6. [D] Explicit integer-j kernel recurrence

For integer j, write

[
|Z_jangle=sum_{r=0}^{j}z_{2r}|2rangle.
]

The odd-k rows of (Q_j|Z_jangle=0) give

[
a_{2r+1}z_{2r}-a_{2r+2}z_{2r+2}=0,
qquad r=0,ldots,j-1.
]

Hence

[
oxed{
z_{2r+2}
=
rac{a_{2r+1}}{a_{2r+2}}z_{2r}.
}
]

Therefore, up to normalization,

[
oxed{
z_{2r}
=
z_0prod_{s=0}^{r-1}
rac{a_{2s+1}}{a_{2s+2}}.
}
]

All coefficients are nonzero and have one common sign if (z_0) is chosen positive.

Since the state contains only even k,

[
oxed{H|Z_jangle=|Z_jangle.}
]

The previously computed j=1 and j=2 zero modes are special cases of this recurrence.

---

## 7. [D][Audit] Spectral pairing

From

[
HQ_jH=-Q_j,
]

if

[
Q_j|psi_lambdaangle=lambda|psi_lambdaangle,
]

then

[
Q_j(H|psi_lambdaangle)
=
-lambda(H|psi_lambdaangle).
]

Therefore every nonzero eigenvalue occurs in an orientation pair

[
oxed{+lambdaleftrightarrow-lambda.}
]

Also

[
HQ_j^2H=Q_j^2,
]

so H preserves every eigenspace of the metric-magnitude operator (Q_j^2).

Let

[
mathcal H_{m nz}=(ker Q_j)^perp.
]

Its dimension is always even:

[
oxed{
dimmathcal H_{m nz}
=
egin{cases}
2j,&jinmathbb Z,\\
2j+1,&jinmathbb Z+rac12.
end{cases}
}
]

---

## 8. [D][Audit] Spectral flattening theorem

On (mathcal H_{m nz}), Q_j is invertible. Define

[
oxed{
R_j=-i,operatorname{sgn}(Q_j)
=-iQ_j(Q_j^2)^{-1/2}.
}
]

Because (operatorname{sgn}(Q_j)^2=I) on the nonzero sector,

[
oxed{R_j^2=-I_{m nz}}
]

and therefore

[
oxed{R_j^4=I_{m nz}.}
]

Since H anticommutes with Q_j but commutes with (Q_j^2),

[
H,operatorname{sgn}(Q_j),H
=
-operatorname{sgn}(Q_j).
]

Thus

[
HR_jH=-R_j.
]

From (R_j^2=-I),

[
R_j^{-1}=-R_j,
]

so

[
oxed{
HR_jH=R_j^{-1}.
}
]

Together with (H^2=I),

[
oxed{
R_j^4=I,qquad
H^2=I,qquad
HR_jH=R_j^{-1}
}
]

on (mathcal H_{m nz}).

Therefore the nonzero oriented-volume sector carries an exact real representation of the project's order-8 dihedral group D8 for every equal spin j.

---

## 9. [D][Audit] Direct-sum decomposition into standard 2D D8 planes

The preceding result can be sharpened without assuming distinct volume magnitudes.

The real operator R_j is orthogonal and satisfies

[
R_j^2=-I.
]

Hence it defines an orthogonal complex structure on (mathcal H_{m nz}).

The reflection H satisfies

[
HR_j=-R_jH.
]

Let (E_+) denote the +1 eigenspace of H inside (mathcal H_{m nz}). For any unit vector (ein E_+), define

[
o=R_je.
]

Then

[
Ho=HR_je=-R_jHe=-R_je=-o,
]

so (o) lies in the -1 parity sector. Also

[
R_jo=R_j^2e=-e.
]

Thus the plane

[
Pi_e=operatorname{span}{e,o}
]

is invariant under both R_j and H, and in the ordered basis ((e,o)),

[
oxed{
R_j|_{Pi_e}
=
egin{pmatrix}
0&-1\\
1&0
end{pmatrix},
qquad
H|_{Pi_e}
=
egin{pmatrix}
1&0\\
0&-1
end{pmatrix}.
}
]

Choosing an orthonormal basis of (E_+) therefore decomposes the entire nonzero sector into mutually orthogonal standard D8 planes.

Let (ho) denote this standard real 2D representation. Then

[
oxed{
mathcal H_{m nz}
cong
ho^{oplus N_j},
}
]

where

[
oxed{
N_j=
egin{cases}
j,&jinmathbb Z,\\
j+rac12,&jinmathbb Z+rac12.
end{cases}
}
]

Equivalently,

[
oxed{N_j=leftlfloor j+rac12ightfloor.}
]

No nondegeneracy assumption on the positive volume magnitudes is needed for this representation-theoretic decomposition.

---

## 10. [D] Full equal-spin decomposition theorem

For integer j,

[
oxed{
mathcal H_j
=
mathbf1_{m zero}
oplus
ho^{oplus j},
}
]

where (mathbf1_{m zero}) is the one-dimensional even-parity kernel of Q_j.

For half-integer j,

[
oxed{
mathcal H_j
=
ho^{oplus(j+1/2)}.
}
]

Thus the low-spin sequence is not accidental:

[
egin{array}{c|c}
j&	ext{decomposition}\\
hline
1/2&ho\\
1&mathbf1_{m zero}oplusho\\
3/2&hooplusho\\
2&mathbf1_{m zero}oplushooplusho\\
5/2&hooplushooplusho
end{array}
]

and the pattern now follows from the bipartite path structure itself.

---

## 11. [G] What the theorem says geometrically

There are three distinct layers:

1. The physical oriented-volume operator Q_j is a local nearest-neighbor path in recoupling k.
2. Its kernel parity is fixed by the imbalance between even and odd vertices of that path.
3. Spectral flattening discards metric volume magnitude while retaining orientation, producing the orthogonal complex structure R_j on the nonzero sector.

The D8 action is therefore carried by oriented-volume planes. Each plane contains one even-parity direction and its R_j-rotated odd-parity partner.

This makes the natural carrier statement exact:

[
oxed{
	ext{For every equal four-spin tetrahedron, the nonzero oriented-volume sector is a direct sum of standard }D_8	ext{ planes.}
}
]

For integer j there is one unpaired, reflection-even, zero-volume line. For half-integer j there is no unpaired line.

---

## 12. [G] Coordination with the magnetic-driver path

The magnetic checkpoints v13.595 and v13.600 establish another family of connected SU(2) weighted paths, now in the magnetic (J_z) basis. The tetrahedral theorem proves that its own recoupling-k path has a parity/kernel structure whose spectral sign produces D8 planes.

The relevance is now precise enough to state as a future audit question:

[
oxed{
	ext{Which properties follow from generic weighted-path bipartiteness, and which require the specific SU(2)/tetrahedral weights?}
}
]

The kernel parity argument above uses only:
- path bipartiteness,
- nonzero edge weights,
- parity-sector dimensions.

By contrast, the actual volume spectrum and the physical meaning of Q_j use the tetrahedral coefficients (a_k).

No magnetic/tetrahedral operator equality is claimed.

---

## 13. Guardrails

1. The D8 quarter-turn is (R_j=-i,operatorname{sgn}(Q_j)), not the raw physical volume Q_j except in special single-magnitude cases after scalar normalization.
2. For integer j, R_j is defined as a quarter-turn only on (mathcal H_{m nz}). If sign(0)=0 is extended to the full space, then (R_j^2=-P_{m nz}), not (-I).
3. The direct-sum D8 decomposition does not require distinct positive volume eigenvalues.
4. The one-dimensional integer-j kernel is even under k-parity.
5. Similar weighted-path appearances in the magnetic driver do not establish an intertwiner or physical equivalence.

## Promoted theorem

[
oxed{
dimker Q_j=
egin{cases}
1,&jinmathbb Z,\\
0,&jinmathbb Z+rac12,
end{cases}
}
]

and, on the nonzero-volume sector,

[
oxed{
R_j=-i,operatorname{sgn}(Q_j),qquad
R_j^2=-I,qquad
H^2=I,qquad
HR_jH=R_j^{-1}.
}
]

Consequently,

[
oxed{
mathcal H_jcong
egin{cases}
mathbf1_{m zero}oplusho^{oplus j},&jinmathbb Z,\\
ho^{oplus(j+1/2)},&jinmathbb Z+rac12.
end{cases}
}
]

## Open next gate

Derive the exact coefficient formula (a_k) directly from the recoupling/Casimir commutator representation of the oriented triple product, including every convention-dependent factor and sign, rather than treating the already low-spin-validated tridiagonal coefficient formula as the input to this theorem. This would close the remaining representation-theoretic provenance gate behind the general proof.
