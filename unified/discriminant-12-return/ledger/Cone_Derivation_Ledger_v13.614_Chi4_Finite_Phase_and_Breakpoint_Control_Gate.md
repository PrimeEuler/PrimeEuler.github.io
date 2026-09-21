# Cone Derivation Ledger v13.614 — chi_-4 Finite Phase Derivation and Breakpoint-Control Gate

Date: 2026-09-21

Status: exact phase-identifiability correction + implemented source-faithful comparison. Numerical comparison awaits independent execution/audit.

## 0. Mandatory collision/relevance check

Immediately before this entry the live ledger was re-fetched. The magnetic-driver lane has advanced through v13.613, so v13.614 is the first free number.

The most relevant older entries were re-read before writing: v13.279, v13.280, v13.283, v13.284, v13.286, v13.610, and v13.611.

A crucial correction emerges from v13.283: in the explicit real resolvent normalization, the deficiency vectors themselves canonically fix the **relative reflection phase**, but they do not determine the self-adjoint extension parameter by themselves.

## 1. What can actually be derived from finite deficiency vectors

Let R be reflection and suppose the finite deficiency vectors satisfy

[
v_-=e^{ialpha_{A,j}}Rv_+.
]

The phase measurable from the computed vectors is

[
oxed{
alpha_{A,j}
=
arglangle Rv_+,v_-angle.
}
]

A scale-independent residual is

[
epsilon_R
=
rac{|v_--e^{ialpha_{A,j}}Rv_+|}
{|v_-|}.
]

The characteristic depends only on the invariant combination

[
oxed{Theta_{A,j}=	heta_{A,j}+alpha_{A,j}pmod{2pi}.}
]

Therefore, after selecting a target invariant boundary line Theta_*,

[
oxed{
	heta(A,j)=Theta_*-alpha_{A,j}pmod{2pi}.
}
]

This is the correct meaning of “derive theta from the actual deficiency vectors.”

The deficiency vectors alone determine alpha, **not** Theta_*. Theta_* is self-adjoint-extension data. Claiming otherwise would confuse a basis gauge with a boundary condition.

## 2. Consequence for the current Zeeman implementation

The v13.610 construction uses the canonical real resolvent basis

[
q_+=S_j^{-1}f_+,qquad q_-=S_j^{-1}f_-.
]

Because the matrix pair and sources are real and reflection covariant,

[
oxed{q_-=Rq_+}
]

in exact arithmetic. Thus

[
oxed{alpha_{A,j}=0pmod{2pi}}
]

for this canonical normalization.

The external audit v13.609 already measured the corresponding numerical reflection residual at about (1.29	imes10^{-15}) for (j=6,A=2).

Consequently, if the Section-7 canonical invariant boundary line is chosen as

[
Theta_*=pi,
]

then

[
oxed{	heta(A,j)=pi}
]

for every A,j in this canonical real basis, up to numerical roundoff.

This is decisive for v13.611: the observed (1/A) root drift cannot be repaired by discovering a hidden finite deficiency-vector phase. The present implementation had already fixed that phase canonically.

## 3. Why this is not circular

There are two logically separate quantities:

1. (alpha_{A,j}): basis/reflection phase, measured from the actual finite vectors;
2. (Theta_*): physical/self-adjoint boundary line selected for comparison with the infinite model.

Only their difference is the bare coordinate theta.

Thus the computation should always report all three:

[
oxed{(alpha_{A,j},Theta_*,	heta_{A,j}).}
]

This makes future rephasings harmless.

## 4. Parallel source-faithful comparison

Added

`research-notes/suzuki_chi4_phase_and_breakpoint_comparison.py`.

The script performs two tasks in one reproducible gate.

First, for each Zeeman finite pair it measures

[
alpha_{A,j}
=
arglangle Rv_+,v_-angle
]

and the reflection residual, then derives theta from a supplied invariant Theta.

Second, it builds a **breakpoint-aware first-kind Fredholm discretization of exactly the same chi_-4 kernel**, following the architecture frozen in v13.286 rather than the direct Jz-node quadrature.

For each row x, the y integration is split at:
- (y=x);
- (y=xpmlog(p^k));
- (y=log(p^k)-x);

whenever the point lies in the half interval.

The parity equations are

[
-int_0^A K_e(x,y)q_e(y),dy=cosh x+B_A,
]

[
-int_0^A K_o(x,y)q_o(y),dy=sinh x+A_Ax,
]

with

[
q_e(A)=0,qquad q_o(0)=q_o(A)=0.
]

The implementation uses Legendre-Gauss-Lobatto interpolation nodes and row-wise Gauss-Legendre product integration on every smooth panel.

## 5. Controlled comparison observable

To isolate discretization/carrier effects, the breakpoint solve is run at the **same finite lambda** chosen by the Zeeman pair.

The raw amplitudes are not compared because the deficiency normalization is arbitrary. Instead, at a fixed nonzero reference point z_* compare

[
oxed{
mathcal W_Z(z)
=
rac{W_Z(A,j,	heta;z)}
{W_Z(A,j,	heta;z_*)}
}
]

against

[
oxed{
mathcal W_{BP}(z)
=
rac{W_{BP}(A,	heta;z)}
{W_{BP}(A,	heta;z_*)}.
}
]

The script reports

[
|mathcal W_Z(z)-mathcal W_{BP}(z)|
]

together with breakpoint-system condition numbers and collocation residuals.

This directly tests whether the Zeeman nodal carrier is approximating the source-faithful finite Fredholm characteristic shape at the same A and lambda.

## 6. Status discipline

Exact/derived now:
- deficiency vectors determine alpha through reflection overlap;
- only Theta=theta+alpha is basis invariant;
- in the canonical real resolvent basis alpha=0 exactly;
- therefore choosing canonical invariant Theta=pi gives theta=pi, so phase extraction alone cannot cure v13.611's box drift.

Implemented but not yet promoted numerically:
- chi_-4 breakpoint-aware Fredholm comparison;
- projective Zeeman-versus-breakpoint characteristic errors at A=1.5,2,2.5.

No numerical comparison values are recorded here because this connector session cannot independently execute repository Python. They must be produced by a genuine run or external audit before promotion.

## 7. Next decision gate

Run the new comparison at increasing:
- Zeeman spin j;
- breakpoint interpolation degree;
- panel quadrature order;
- precision where needed.

Two outcomes are sharply distinguishable.

If
[
mathcal W_Z-mathcal W_{BP}	o0
]
at fixed A while both retain the same (1/A) zero drift, then the box modes belong to the finite Suzuki boundary problem rather than to the Zeeman carrier.

If the breakpoint characteristic stabilizes while the Zeeman characteristic does not approach it, then the direct Jz nodal compression is the failing approximation and should be replaced by a Galerkin/carrier map that preserves the Section-8 domain and endpoint structure.

Either outcome is more informative than tuning theta, because the finite reflection phase has now been removed as an ambiguity.
