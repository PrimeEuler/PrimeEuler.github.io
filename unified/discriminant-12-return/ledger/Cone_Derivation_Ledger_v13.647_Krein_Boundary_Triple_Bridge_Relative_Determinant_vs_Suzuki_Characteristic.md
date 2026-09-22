# Cone Derivation Ledger v13.647 — Krein Boundary Triple Bridge: Relative Determinant versus Suzuki Extension Characteristic

Date: 2026-09-22

Status: exact abstract boundary-triple derivation, with a crucial scope correction. The common-domain perturbation determinant of v13.644 and Suzuki's theta-extension characteristic are different factors. The exact scalar boundary factor is a Cayley transform of the scalar Weyl function. Equality to the printed Fourier W requires an additional normalization identity not yet established.

## 0. Live collision/relevance check

The live ledger was fetched immediately before this write and is at v13.646 (External Audit Round 68). Round 68 explicitly leaves v13.640/v13.641/v13.644 open for a future independent audit and does not overturn them. This entry takes v13.647.

## 1. Two logically distinct comparisons

Let S_A be the closed symmetric operator underlying Suzuki's deficiency construction, with deficiency indices (1,1). Let H_{A,F} denote a fixed self-adjoint Friedrichs/reference extension of S_A. Separately, let H_{0,A} be the same-domain Dirichlet local reference introduced in v13.644.

There are TWO determinant ratios:
(i) common-domain bulk perturbation:
[
Delta_A^{bulk}(zeta)=det[(H_{A,F}-zeta)(H_{0,A}-zeta)^{-1}],
]
(ii) rank-one extension change:
[
Delta_{A,	heta}^{bdry}(zeta)
=det[(H_{A,	heta}-zeta)(H_{A,F}-zeta)^{-1}].
]
They must not be conflated.

The total relative determinant factors:
[
oxed{Delta_{A,	heta}^{tot}(zeta)
=Delta_{A,	heta}^{bdry}(zeta)Delta_A^{bulk}(zeta).}
]

## 2. Ordinary boundary triple

Choose an ordinary scalar boundary triple (C,Gamma_0,Gamma_1) for S_A^* so that
[
H_{A,F}=S_A^*|_{kerGamma_0}.
]
Let gamma_A(zeta) be the gamma field and m_A(zeta) the scalar Weyl function:
[
gamma_A(zeta)=(Gamma_0|_{ker(S_A^*-zeta)})^{-1},qquad
m_A(zeta)=Gamma_1gamma_A(zeta).
]

A self-adjoint extension with real boundary parameter tau is
[
H_{A,	au}=S_A^*|_{Gamma_1 f=	auGamma_0 f}.
]

Krein's formula is
[
oxed{
(H_{A,	au}-zeta)^{-1}-(H_{A,F}-zeta)^{-1}
=gamma_A(zeta)(	au-m_A(zeta))^{-1}gamma_A(arzeta)^*.
}
]
This is rank one.

## 3. Exact scalar perturbation determinant

For scalar deficiency, the extension perturbation determinant normalized at a reference point zeta_* in the common resolvent is
[
oxed{
widehatDelta_{A,	au}^{bdry}(zeta;zeta_*)
=
rac{	au-m_A(zeta)}{	au-m_A(zeta_*)}.
}
]
Indeed
[
-rac{d}{dzeta}log(	au-m_A(zeta))
=
operatorname{tr}[(H_{A,	au}-zeta)^{-1}-(H_{A,F}-zeta)^{-1}]
]
with the sign fixed by m_A'(zeta)=gamma_A(arzeta)^*gamma_A(zeta).

Thus the exact boundary scalar is tau-m_A.

## 4. Phase parametrization and Cayley factor

Suzuki labels extensions by a phase e^{i theta}. Introduce the Schur/Cayley transform of the Weyl function
[
s_A(zeta)=rac{m_A(zeta)-i}{m_A(zeta)+i}.
]
The standard relation between a real tau and a unitary phase is
[
e^{i	heta}=rac{	au-i}{	au+i},
qquad
	au=-cot(	heta/2)
]
for this boundary-triple convention.

A direct algebraic calculation gives
[
oxed{
	au-m_A(zeta)
=
-rac{	au+i}{2i},[m_A(zeta)+i],[1-e^{i	heta}s_A(zeta)].
}
]
Therefore, after normalization at zeta_*,
[
oxed{
widehatDelta_{A,	heta}^{bdry}(zeta;zeta_*)
=
rac{m_A(zeta)+i}{m_A(zeta_*)+i}
rac{1-e^{i	heta}s_A(zeta)}
{1-e^{i	heta}s_A(zeta_*)}.
}
]
Equivalently the zero-carrying scalar boundary factor is
[
oxed{b_{A,	heta}(zeta)=1-e^{i	heta}s_A(zeta),}
]
up to the nonzero theta-independent factor m_A+i determined by the chosen triple.

This is the exact rank-one boundary factor.

## 5. Relation to Suzuki's printed W

Suzuki's canonical reflection-basis characteristic has
[
W_A(	heta;z)
=(z-i)F_{A,+}(z)+e^{i	heta}(z+i)F_{A,-}(z).
]
Factor the first coefficient:
[
oxed{
W_A(	heta;z)
=(z-i)F_{A,+}(z)
left[
1+e^{i	heta}
rac{(z+i)F_{A,-}(z)}{(z-i)F_{A,+}(z)}
ight].
}
]
Hence define the Suzuki Schur candidate
[
oxed{
s_A^{Suz}(z)=-
rac{(z+i)F_{A,-}(z)}
{(z-i)F_{A,+}(z)}.
}
]
Then identically
[
oxed{
W_A(	heta;z)
=(z-i)F_{A,+}(z)[1-e^{i	heta}s_A^{Suz}(z)].
}
]

Therefore the printed W has EXACTLY the abstract boundary-triple phase dependence. Its exact scalar boundary factor is
[
oxed{1-e^{i	heta}s_A^{Suz}(z).}
]

What is not yet proved is the normalization/identification
[
s_A^{Suz}(z)=s_A(zeta)
]
with the Cayley transform of the Weyl function, including the spectral-variable map zeta=z^2 (or the precise Suzuki transformed variable) and any fixed unimodular convention factor. Establishing that requires computing Gamma_0,Gamma_1 on Suzuki's canonical deficiency vectors, not merely matching the algebraic theta dependence.

## 6. Combined determinant formula

Once the Weyl/Suzuki identification is established, the total determinant relative to the local Dirichlet reference factors as
[
oxed{
widehatDelta_{A,	heta}^{tot}
=
widehatDelta_A^{bulk}
widehatDelta_{A,	heta}^{bdry}.
}
]
Using v13.644,
[
widehatDelta_A^{bulk}(z)
=
rac{det[I+V_AR_{0,A}(z^2)]}
{det[I+V_AR_{0,A}(0)]}.
]
The boundary factor is the normalized Cayley scalar above.

Correspondingly the normalized full spectral characteristic is of the form
[
D_{0,A}(z),
widehatDelta_A^{bulk}(z),
widehatDelta_{A,	heta}^{bdry}(z),
qquad
D_{0,A}(z)=rac{sin(2Az)}{2Az}.
]

This separates exactly:
1. endpoint geometry: D_{0,A};
2. common-domain arithmetic/nonlocal bulk perturbation: Delta_bulk;
3. self-adjoint extension phase: Delta_bdry.

## 7. Correction to the hoped-for direct quotient

There is no basis at present for
[
W_A/W_{0,A}=Delta_A^{bulk}.
]
W_A primarily carries the extension boundary factor. The bulk relative determinant is a separate same-domain object.

The exact algebraic bridge presently proved is:
[
oxed{
W_A(	heta;z)
=(z-i)F_{A,+}(z),b_{A,	heta}^{Suz}(z),
quad
b_{A,	heta}^{Suz}=1-e^{i	heta}s_A^{Suz}.
}
]
The abstract Krein factor is
[
oxed{
b_{A,	heta}=1-e^{i	heta}rac{m_A-i}{m_A+i}.
}
]
Their equality is reduced to the concrete boundary-triple identity
[
-rac{(z+i)F_{A,-}}{(z-i)F_{A,+}}
=
rac{m_A-i}{m_A+i}
]
(up to a fixed convention phase and the precise spectral-variable map).

## 8. Next gate

Construct Gamma_0,Gamma_1 explicitly in Suzuki's canonical deficiency basis q_+=T^{-1}e^x, q_-=Rq_+, evaluate the scalar Weyl function m_A, and prove or refute the displayed Schur identity. Only after that identity is fixed should W be combined with the bulk determinant for an A->infinity renormalization experiment.
