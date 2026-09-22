# Cone Derivation Ledger v13.644 — Dirichlet Reference Operator and Relative Fredholm Determinant for the chi_-4 Friedrichs Lane

Date: 2026-09-22

Status: exact reference construction and relative-determinant identity. This replaces the inconsistent naive g->0 first-kind control of v13.641 by a well-posed operator on the SAME Friedrichs domain.

## 0. Live collision/relevance check

The live ledger was fetched immediately before this write and is at v13.643. v13.642 is magnetic-driver work and v13.643 is the j=3/2 analog-simulation lane; neither collides. This entry takes v13.644.

## 1. Common Friedrichs domain

The finite-interval Friedrichs form domain is H_0^1(-A,A). Its canonical local reference is the Dirichlet Laplacian
[
H_{0,A}=-d^2/dx^2,qquad
D(H_{0,A})=H^2(-A,A)cap H_0^1(-A,A).
]
Thus u(-A)=u(A)=0, exactly the endpoint trace carried by the full Friedrichs realization.

Let the full operator be written at operator level as
[
H_A=H_{0,A}+V_A
]
in form/resolvent sense, where V_A denotes the nonlocal chi_-4/Weil contribution after the common local Friedrichs part has been separated. This is the proper reference split; it is NOT the formal first-kind deletion k=-lambda N_A of v13.629/v13.641.

## 2. Exact reference characteristic

Solve
[
(H_{0,A}-z^2)u=0,qquad u(-A)=0.
]
With normalization u'(-A)=1,
[
u_0(x,z)=rac{sin(z(x+A))}{z},
]
entire at z=0 by continuation. The right endpoint boundary value is
[
Delta_{0,A}(z)=u_0(A,z)=rac{sin(2Az)}{z}.
]
Normalized to one at z=0,
[
oxed{D_{0,A}(z)=rac{sin(2Az)}{2Az}.}
]
Hence the full Dirichlet box spectrum on [-A,A] is
[
oxed{z_n=pmrac{npi}{2A},quad n=1,2,ldots.}
]

Parity factorization gives
[
D_{0,A}(z)
=rac{sin(Az)}{Az}cos(Az).
]
The odd sector on [0,A] has Dirichlet-Dirichlet characteristic
[
D_{o,0}(z)=rac{sin(Az)}{Az},
quad z_n^{(o)}=pm npi/A,
]
while the even sector has Neumann-Dirichlet characteristic
[
D_{e,0}(z)=cos(Az),
quad z_n^{(e)}=pm(n+1/2)pi/A.
]
This explains why the factor B_A=sin(Az)/(Az) isolated in v13.641 is specifically the odd endpoint factor, not the complete reference characteristic.

## 3. Reference resolvent

For z not in the reference spectrum, the Dirichlet Green kernel is
[
R_{0,A}(z^2;x,y)
=
rac{sin(z(x_<+A))sin(z(A-x_>))}
{zsin(2Az)},
]
where x_<=min(x,y), x_>=max(x,y). It maps into the same Dirichlet operator domain.

## 4. Relative Fredholm determinant

Assume the perturbation is represented so that
[
K_A(z)=V_A(H_{0,A}-z^2)^{-1}
]
is trace class (or use det_2 if only Hilbert-Schmidt; then the standard exponential correction must be retained). Define
[
oxed{mathcal D_A(z)=det(I+K_A(z)).}
]
The resolvent factorization
[
H_A-z^2
=
[I+V_A(H_{0,A}-z^2)^{-1}](H_{0,A}-z^2)
]
gives
[
oxed{
mathcal D_A(z)
=
det!left((H_A-z^2)(H_{0,A}-z^2)^{-1}ight).
}
]

For finite-dimensional Galerkin compressions this identity is literal:
[
det(H_{A,N}-z^2I)
=
det(H_{0,A,N}-z^2I),
det[I+V_{A,N}(H_{0,A,N}-z^2I)^{-1}].
]

Thus the relative determinant is the mathematically correct replacement for the invalid quotient of two first-kind deficiency characteristics.

## 5. Pole-zero cancellation and normalized full characteristic

mathcal D_A is meromorphic in z because R_0 has poles at the reference box spectrum. Multiplying by the reference characteristic removes those reference poles:
[
oxed{
D_A(z)=D_{0,A}(z),mathcal D_A(z)
}
]
(up to an overall nonzero entire normalization fixed here by D_{0,A}(0)=1 and, if 0 is in the full resolvent, by dividing mathcal D_A(z) by mathcal D_A(0)).

A convenient normalized relative determinant is
[
oxed{
widehat{mathcal D}_A(z)=
rac{det(I+V_AR_{0,A}(z^2))}
{det(I+V_AR_{0,A}(0))},
qquad widehat{mathcal D}_A(0)=1.
}
]
Then
[
oxed{widehat D_A(z)=D_{0,A}(z)widehat{mathcal D}_A(z),qquad widehat D_A(0)=1.}
]

Zeros of widehat D_A are the full finite-A eigenvalues counted with multiplicity, while poles/zeros associated purely with the reference spectrum cancel in the product in the usual relative-determinant manner.

## 6. Parity-relative determinants

Because the chi_-4 kernel and the interval are reflection symmetric, H_A commutes with parity. Therefore
[
H_A=H_{A,e}oplus H_{A,o},
qquad
H_{0,A}=H_{0,A,e}oplus H_{0,A,o},
]
and
[
mathcal D_A=mathcal D_{A,e}mathcal D_{A,o}.
]
The reference factors are
[
D_{e,0}(z)=cos(Az),qquad
D_{o,0}(z)=rac{sin(Az)}{Az}.
]
Hence
[
oxed{
widehat D_A(z)
=
cos(Az)rac{sin(Az)}{Az}
,widehat{mathcal D}_{A,e}(z)
,widehat{mathcal D}_{A,o}(z).
}
]

This gives the exact endpoint factorization against a well-posed common-domain reference. The n*pi/A factor seen in v13.629/v13.641 is now identified as the odd Dirichlet sector; the half-integer cosine branch is the even Neumann-at-zero/Dirichlet-at-A sector.

## 7. Guardrail about Suzuki's W characteristic

The determinant D_A above is the spectral determinant of the common-domain Friedrichs operator pair. Suzuki's extension characteristic
[
W_A(	heta;z)=(z-i)F_+(z)+e^{i	heta}(z+i)F_-(z)
]
is built from deficiency vectors and an extension phase. Equality of W_A with D_A, or a simple entire multiple thereof, has NOT been proved here.

Therefore:
- it is legitimate to use mathcal D_A as the relative Fredholm determinant of the operator pair;
- it is NOT yet legitimate to identify W_A/W_{0,A} with mathcal D_A;
- the next gate is to derive the bridge between the extension characteristic and the perturbation determinant (a Krein/Birman-type formula), including the boundary phase and normalization.

## 8. Decision

The correct same-domain reference is the Dirichlet Laplacian on [-A,A]:
[
oxed{H_{0,A}=-d^2/dx^2,quad D=H^2cap H_0^1.}
]
Its normalized characteristic and parity factors are
[
oxed{D_{0,A}(z)=rac{sin(2Az)}{2Az}
=cos(Az)rac{sin(Az)}{Az}.}
]
The relative Fredholm determinant is
[
oxed{widehat{mathcal D}_A(z)=
rac{det(I+V_A(H_{0,A}-z^2)^{-1})}
{det(I+V_AH_{0,A}^{-1})}.}
]
This is the admissible renormalized operator object. The next gate is the exact bridge, if any, from this determinant to Suzuki's deficiency-vector characteristic W_A(theta;z).
