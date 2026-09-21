# Cone Derivation Ledger v13.608 — chi_-4 Zeeman Finite Deficiency and Suzuki Characteristic

Date: 2026-09-21

Status: finite-characteristic construction/prototype; zero-convergence test remains open. No GRH claim.

## 0. Mandatory collision/relevance check

Immediately before committing this entry the live ledger was re-fetched.

A collision was found: two distinct entries currently carry number v13.607:
- `v13.607_Chi4_Suzuki_Kernel_Zeeman_SU2_Compression`;
- `v13.607_Magnetic-Driver_Floquet-Magnus_Re-Audit`.

Therefore this lane does **not** reuse v13.607. The present checkpoint advances to v13.608.

New relevance was also found in the concurrently landed magnetic-driver v13.607: it sharpens the distinction between van-Vleck and stroboscopic Floquet gauges but does not alter the exact static Zeeman (J_z/J_x) carrier used here. No mathematical collision with the chi_-4 compression was found.

The older Suzuki ledger was also rechecked. Two guardrails are directly relevant:
- v13.280: the canonical Section-7 boundary choice is theta=pi and the characteristic target is Xi/E, not a raw kernel eigenvalue.
- v13.288 supersedes the numerical generalized-eigenvalue scale reported in v13.287. In particular, no inherited claim such as lambda=-5<lambda_a may be treated as certified.

## 1. Input from v13.607 chi_-4 lane

The previous checkpoint constructed

[
g_{-4}(t)
]

with the chi_-4 prime-power twist and the odd-character (a=3/4,q=4) archimedean factor, then compressed it to the exact spin-j Zeeman carrier,

[
(G_j^{(-4)})_{mn}=sqrt{w_mw_n},g_{-4}(x_m-x_n).
]

The present checkpoint adds the finite Suzuki deficiency/characteristic layer.

## 2. Neumann inverse on the same carrier

On ([-A,A]), Suzuki's Section-8 inverse Neumann kernel is

[
N_A(x,y)=rac{x^2+y^2}{4A}-rac{|x-y|}{2}+rac A6.
]

Compress it on the same Zeeman nodes and quadrature weights:

[
(K_j)_{mn}=sqrt{w_mw_n},N_A(x_m,x_n).
]

Let (P_j) be the exact finite weighted mean-zero projector. The working pair is

[
widehat G_j=P_jG_jP_j,qquad
widehat K_j=P_jK_jP_j.
]

The finite generalized spectrum is computed on an orthonormal basis (B_j) for the mean-zero subspace:

[
B_j^*widehat G_jB_j,c
=mu,B_j^*widehat K_jB_j,c.
]

## 3. Lambda guardrail corrected before use

Because v13.288 invalidated the earlier numerical scale, this construction does not inherit a fixed lambda from v13.287.

Instead, for each finite compressed pair it computes its actual finite generalized spectral bottom (mu_{0,j}) and chooses

[
oxed{lambda_j=mu_{0,j}-delta,qquad delta>0.}
]

This guarantees invertibility/positivity relative to the **finite matrix pair**. It is not promoted to a theorem that (lambda_j) lies below the true continuous (lambda_A).

Define

[
S_j=widehat G_j-lambda_jwidehat K_j.
]

## 4. Finite deficiency vectors

Use projected weighted source vectors corresponding to (e^{pm x}):

[
f_{pm,j}=P_j{sqrt{w_m}e^{pm x_m}}_m.
]

The finite deficiency proxies are the solutions

[
oxed{S_jv_{pm,j}=f_{pm,j}}
]

on the mean-zero carrier.

Reflection symmetry supplies an immediate diagnostic: after a consistent real normalization,

[
v_{-,j}stackrel{?}{=}R,v_{+,j}.
]

The implementation reports the relative residual of this relation.

## 5. Finite characteristic

Define the quadrature Fourier transforms

[
F_{pm,j}(z)
=
sum_msqrt{w_m},v_{pm,j,m}e^{izx_m}.
]

Following the Section-7.8 combination frozen in v13.280, define

[
oxed{
W_j^{(-4)}(	heta;z)
=
(z-i)F_{+,j}(z)
+
e^{i	heta}(z+i)F_{-,j}(z).
}
]

At the canonical boundary phase,

[
oxed{
W_j^{(-4)}(pi;z)
=
(z-i)F_{+,j}(z)
-
(z+i)F_{-,j}(z).
}
]

This is now the finite characteristic object to compare, after scalar normalization, with the primitive-character analogue

[
R_{-4}(z)
=
rac{Xi_{-4}(z)}
{E_{-4}(z)},
qquad
E_{-4}(z)=Xi_{-4}(z)+iXi_{-4}'(z).
]

The relevant zeros of the target numerator are the critical-line ordinates of (L(s,chi_{-4})).

## 6. Implementation

Added

`research-notes/suzuki_chi4_zeeman_finite_characteristic.py`.

It imports the v13.607 chi_-4 kernel implementation and adds:
- sampled Neumann inverse (K_j);
- exact finite weighted mean-zero projection;
- generalized finite spectrum;
- finite-pair-safe lambda selection;
- (e^{pm x}) deficiency solves;
- reflection diagnostic;
- Fourier transforms;
- (W_j^{(-4)}(	heta;z)), with theta=pi as the default.

## 7. What is and is not established

Established as a finite construction:
[
oxed{
chi_{-4}	o g_{-4}	o(G_j,K_j)	o v_{pm,j}	o W_j^{(-4)}(pi;z).
}
]

Not established:
- that this particular Zeeman nodal compression converges to Suzuki's continuous finite-volume deficiency problem;
- that its finite characteristic zeros converge with (j);
- that (A	oinfty) and (j	oinfty) limits commute;
- that the characteristic zeros equal beta-zero ordinates at finite j;
- GRH for (L(s,chi_{-4})).

## 8. Next gate

The next experiment must be quantitative and falsifiable:

1. independently compute the first several positive zeros (gamma_n^{(-4)}) of (Xi_{-4});
2. locate real zeros of (W_j^{(-4)}(pi;z)) for a grid of increasing spins j;
3. repeat for more than one interval scale A;
4. track zero branches rather than nearest-neighbour rematching at every j;
5. report signed errors and convergence ratios;
6. fail closed if branches drift, disappear, or depend strongly on A.

Only after that comparison may any statement of zero indexing/convergence be considered.
