# Cone Derivation Ledger v13.618 — Equal-Spin Racah Recurrence and Crossed-Casimir Neighbor Coefficient

Date: 2026-09-21

Status labels: [S] standard recoupling fact, [D] exact derived, [Audit] checked against prior exact matrices/audits, [G] structural interpretation.

## 0. Mandatory live collision / relevance check

Immediately before this write the live ledger was re-fetched. The current tip is v13.617, so v13.618 is free.

Relevant intervening entries were inspected. v13.615 independently audited the recent magnetic Floquet work; v13.616 is the chi_-4 breakpoint convergence gate; v13.617 extends the magnetic-driver endpoint coefficients. None derives the equal-spin Racah recurrence or the crossed-Casimir coefficient below. The magnetic lane remains structurally relevant as a separate SU(2) weighted-path construction, but no magnetic/tetrahedral operator identification is used here.

This entry closes the final intermediate recoupling step left explicit as an open gate in v13.602.

---

## 1. [S] Two invariant recoupling bases

For four equal external spins j, define

[
|kangle_{12}=|[(j_1j_2)k,(j_3j_4)k],J=0angle,
]

and

[
|ellangle_{23}=|[(j_2j_3)ell,(j_1j_4)ell],J=0angle,
]

with

[
k,ell=0,ldots,2j.
]

The real orthogonal Racah matrix is

[
U_{kell}={}_{12}langle k|ellangle_{23},
]

and, up to the fixed recoupling phase convention,

[
U_{kell}
=
sqrt{(2k+1)(2ell+1)}
egin{Bmatrix}
j&j&k\\
j&j&ell
end{Bmatrix}.
]

Since

[
K_{23}^2|ellangle_{23}=ell(ell+1)|ellangle_{23},
]

each column (U_{ulletell}) is an eigenvector of the k-basis matrix of (K_{23}^2).

---

## 2. [S] Symmetric three-term Racah recurrence

Write the normalized Racah finite-difference equation as

[
p_+(x)U(x+1,y)+w(x)U(x,y)+p_-(x)U(x-1,y)
=
lambda(y)U(x,y),
]

with

[
p_-(x)=p_+(x-1).
]

For external labels a,b,c,d,

[
p_+(x)=
rac{
sqrt{(a+b+x+2)(a+b-x)(a-b+x+1)(-a+b+x+1)}
}{x+1}
]

[
hspace{2.5cm}	imes
rac{
sqrt{(d+c+x+2)(d+c-x)(d-c+x+1)(-d+c+x+1)}
}{
sqrt{(2x+1)(2x+3)}
},
]

[
w(x)=
rac{
[b(b+1)-a(a+1)+x(x+1)]
[d(d+1)-c(c+1)-x(x+1)]
}{
x(x+1)
},
]

and

[
lambda(y)=2[y(y+1)-b(b+1)-c(c+1)].
]

The endpoint terms are understood by finite support: coefficients outside the admissible coupling interval vanish.

---

## 3. [D] Equal-spin diagonal and eigenvalue terms

Set

[
a=b=c=d=j,qquad x=k,qquad y=ell.
]

The external-Casimir differences vanish, so

[
w(k)
=
rac{k(k+1)[-k(k+1)]}{k(k+1)}
=
-k(k+1).
]

Thus

[
oxed{w(k)=-k(k+1).}
]

Also

[
oxed{
lambda(ell)=2[ell(ell+1)-2j(j+1)].
}
]

Therefore

[
p_+(k)U_{k+1,ell}
-k(k+1)U_{kell}
+p_-(k)U_{k-1,ell}
=
2[ell(ell+1)-2j(j+1)]U_{kell}.
]

---

## 4. [D] Equal-spin neighboring recurrence coefficient

Use

[
p_-(k)=p_+(k-1).
]

At (x=k-1), the first square-root numerator becomes

[
sqrt{(2j+k+1)(2j-k+1)k^2}
=
ksqrt{(2j+1)^2-k^2}.
]

The second square root is identical because all four external spins are j. Their product is

[
k^2[(2j+1)^2-k^2].
]

The remaining denominator is

[
(x+1)sqrt{(2x+1)(2x+3)}
=
ksqrt{(2k-1)(2k+1)}
=
ksqrt{4k^2-1}.
]

Canceling one k gives

[
oxed{
p_-(k)
=
rac{k[(2j+1)^2-k^2]}
{sqrt{4k^2-1}}.
}
]

By symmetry,

[
oxed{
p_+(k)
=
rac{(k+1)[(2j+1)^2-(k+1)^2]}
{sqrt{4(k+1)^2-1}}
=p_-(k+1).
}
]

---

## 5. [D] Read the recurrence as the K_23^2 eigenvalue equation

Divide the recurrence by 2:

[
rac{p_+(k)}2U_{k+1,ell}
-rac{k(k+1)}2U_{kell}
+rac{p_-(k)}2U_{k-1,ell}
=
[ell(ell+1)-2j(j+1)]U_{kell}.
]

Add (2j(j+1)U_{kell}) to both sides:

[
ell(ell+1)U_{kell}
=
rac{p_+(k)}2U_{k+1,ell}
+
left[2j(j+1)-rac{k(k+1)}2ight]U_{kell}
+
rac{p_-(k)}2U_{k-1,ell}.
]

But the left side is exactly the eigenvalue equation

[
K_{23}^2|ellangle_{23}
=
ell(ell+1)|ellangle_{23}.
]

Therefore the k-basis matrix entries are read off directly:

[
oxed{
langle k|K_{23}^2|kangle
=
2j(j+1)-rac{k(k+1)}2,
}
]

and

[
oxed{
langle k-1|K_{23}^2|kangle
=
rac{p_-(k)}2
=
rac{k[(2j+1)^2-k^2]}
{2sqrt{4k^2-1}}.
}
]

The matrix is real symmetric, so the opposite neighboring entry is identical.

Define

[
c_k=
rac{k[(2j+1)^2-k^2]}
{2sqrt{4k^2-1}},
qquad
d_k=2j(j+1)-rac{k(k+1)}2.
]

Then

[
oxed{
K_{23}^2=
egin{pmatrix}
d_0&c_1&0&cdots&0\\
c_1&d_1&c_2&ddots&dots\\
0&c_2&d_2&ddots&0\\
dots&ddots&ddots&ddots&c_{2j}\\
0&cdots&0&c_{2j}&d_{2j}
end{pmatrix}.
}
]

Its spectrum is (ell(ell+1)), (ell=0,ldots,2j), and its normalized eigenvectors are the Racah columns (U_{ulletell}).

---

## 6. [D] Recover the volume coefficient with no remaining recoupling black box

From v13.602,

[
oxed{
Q=rac{i}{4}[K_{12}^2,K_{23}^2].
}
]

Since

[
K_{12}^2|kangle=k(k+1)|kangle,
]

[
langle k-1|Q|kangle
=
rac{i}{4}[(k-1)k-k(k+1)]
langle k-1|K_{23}^2|kangle.
]

The Casimir eigenvalue difference is

[
(k-1)k-k(k+1)=-2k.
]

Hence

[
langle k-1|Q|kangle
=
-rac{ik}{2}
rac{k[(2j+1)^2-k^2]}
{2sqrt{4k^2-1}},
]

or

[
oxed{
langle k-1|Q|kangle
=
-i
rac{k^2[(2j+1)^2-k^2]}
{4sqrt{4k^2-1}}.
}
]

Therefore

[
oxed{
a_k=
rac{k^2[(2j+1)^2-k^2]}
{4sqrt{4k^2-1}},
}
]

exactly as used in v13.599 and derived via the commutator in v13.602.

---

## 7. [G] New factorization: spectral difference times Racah edge

The two path coefficients satisfy

[
oxed{a_k=rac{k}{2}c_k.}
]

The factor (c_k) is the crossed-pair Racah coupling,

[
c_k=
rac{k[(2j+1)^2-k^2]}
{2sqrt{4k^2-1}},
]

while

[
rac{k}{2}
=
rac14left| (k-1)k-k(k+1)ight|
]

is the adjacent spectral difference of (K_{12}^2) including the commutator factor (1/4).

Thus the oriented-volume path weight factors exactly as

[
oxed{
	ext{volume edge weight}
=
	ext{pair-Casimir spectral difference}
	imes
	ext{crossed-pair Racah edge weight}.
}
]

This separates the two ingredients that had previously appeared only in the final closed coefficient.

---

## 8. [Audit] Consistency with the established chain

At j=1/2,

[
c_1=rac{sqrt3}{2},
qquad
a_1=rac{sqrt3}{4},
]

giving the v13.591 matrix.

At j=1,

[
a_1=rac{2sqrt3}{3},
qquad
a_2=rac{sqrt{15}}3,
]

giving the v13.596 matrix.

Round 63 already independently reconstructed the higher-spin tensor-space spectra at j=2 and j=5/2 from the same final (a_k) formula. Thus the now-explicit Racah route is consistent with both the low-spin exact matrices and the independent higher-spin audit.

---

## 9. Provenance chain now explicit end to end

[
6j	ext{ / Racah recoupling}
]

[
Downarrow
]

[
oxed{
p_-(k)=
rac{k[(2j+1)^2-k^2]}{sqrt{4k^2-1}}
}
]

[
Downarrow
]

[
oxed{
langle k-1|K_{23}^2|kangle
=
rac{k[(2j+1)^2-k^2]}{2sqrt{4k^2-1}}
}
]

[
Downarrowquad
Q=rac{i}{4}[K_{12}^2,K_{23}^2]
]

[
oxed{
langle k-1|Q|kangle
=
-i
rac{k^2[(2j+1)^2-k^2]}{4sqrt{4k^2-1}}
}
]

[
Downarrow
]

the nonvanishing bipartite path used in the v13.599 kernel/D8 theorem.

The coefficient-provenance gate opened in v13.599 and narrowed in v13.602 is therefore closed.

---

## 10. Guardrails

1. The recurrence is written for normalized Racah coefficients with the project's fixed recoupling phase convention. Rephasing basis states can change displayed neighboring signs but not the spectrum or physical orientation.
2. Physical orientation reversal sends Q to -Q; it is distinct from a basis rephasing.
3. (K_{23}^2) and Q are different weighted paths. Their edge coefficients are related by (a_k=(k/2)c_k), not equality.
4. The magnetic-driver weighted path remains a separate representation/dynamics problem; no operator intertwiner is asserted here.
5. Physical LQG volume normalization factors beyond the dimensionless oriented triple product Q are outside this entry.

## Promoted conclusion

The equal-spin Racah recurrence yields directly

[
oxed{
langle k-1|K_{23}^2|kangle
=
rac{k[(2j+1)^2-k^2]}
{2sqrt{4k^2-1}},
}
]

and therefore the Casimir commutator gives

[
oxed{
langle k-1|Q|kangle
=
-i
rac{k^2[(2j+1)^2-k^2]}
{4sqrt{4k^2-1}}.
}
]

No unexpanded recoupling matrix element remains between the Racah transform and the general equal-spin tetrahedron D8 theorem.

## Open next gate

With the coefficient provenance closed, the next structural question is to compare the three finite weighted paths now present in the project — the SU(2) ladder/magnetic path, the crossed-Casimir Racah path (c_k), and the tetrahedral volume path (a_k=(k/2)c_k) — and determine exactly which transformations are genuine similarities/intertwiners and which are only weight-level correspondences.
