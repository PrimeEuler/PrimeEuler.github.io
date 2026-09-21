# Cone Derivation Ledger v13.623 — Independent chi_-4 Friedrichs Galerkin Solve

Date: 2026-09-21

Status: independent direct Galerkin assembly executed; breakpoint-control comparison passes at the projective-characteristic level.

## 0. Live collision/relevance check

The live ledger was re-fetched immediately before this write. v13.622 is the current tip and belongs to the magnetic-driver lane; it does not alter the chi_-4 gate. The relevant chain is v13.614–v13.616 and v13.620–v13.621. Therefore v13.623 is free.

## 1. Purpose

v13.621 established only representation adequacy: a breakpoint-computed deficiency solution could be projected into an endpoint-adapted basis and transported unitarily to SU(2).

This gate removes that dependence. The deficiency equations are assembled and solved directly in the Friedrichs-adapted basis, without using the breakpoint solution as input.

On [0,A]:

[
e_n(x)=sqrt{2/A}cos((n+1/2)pi x/A),
qquad
o_n(x)=sqrt{2/A}sin((n+1)pi x/A).
]

Thus

[
e_n(A)=0,qquad o_n(0)=o_n(A)=0
]

identically.

## 2. Direct Galerkin equations

For the same finite lambda used by the j=10 comparison pair, assemble the parity kernels from

[
k(x,y)=g_{-4}(x-y)-lambda N_A(x,y),
]

[
K_e(x,y)=k(x,y)+k(x,-y),qquad
K_o(x,y)=k(x,y)-k(x,-y).
]

Solve the augmented first-kind systems

[
langle e_m,-K_e q_eangle-Blangle e_m,1angle
=langle e_m,coshangle,
]

[
langle o_m,-K_o q_oangle-Clangle o_m,xangle
=langle o_m,sinhangle.
]

One additional residual condition against 1 (even) and x (odd) determines the nuisance scalars B,C.

The assembly used tensor Gauss-Legendre quadrature; the comparison control is the independently constructed breakpoint-aware degree-14/q12 solve.

## 3. Finite lambdas

Same common finite lambdas as the preceding gate:

- A=1.5: lambda = -0.9941426
- A=2.0: lambda = -0.9924506
- A=2.5: lambda = -0.9939186

## 4. Independent Galerkin convergence

Maximum projective characteristic difference from the breakpoint control over z=1,3,6,10, normalized at z*=0.5:

| N | A=1.5 | A=2.0 | A=2.5 |
|---:|---:|---:|---:|
| 4  | 4.8653e-2 | 2.3992e-2 | 6.5763e-2 |
| 6  | 9.5347e-3 | 1.5852e-2 | 7.2064e-3 |
| 8  | 7.0399e-3 | 3.4610e-3 | 1.2880e-2 |
| 10 | 3.0359e-3 | 1.9212e-3 | 7.6940e-3 |
| 12 | 2.7869e-3 | 1.1910e-3 | 3.7285e-3 |
| 16 | **2.2754e-3** | **7.6850e-4** | **2.8188e-3** |

At N=16 all three A values are below 2.9e-3.

Componentwise N=16 differences:

- A=1.5: (1.3564e-4, 1.1365e-4, 8.3351e-4, 2.2754e-3)
- A=2.0: (3.7552e-4, 2.2104e-4, 3.6267e-4, 7.6850e-4)
- A=2.5: (4.9861e-5, 2.8188e-3, 2.1556e-4, 4.7079e-4)

The convergence is not strictly monotone at every intermediate N (especially A=2.5), but the refined trend is decisively toward the breakpoint control.

## 5. Conditioning and residuals

At N=16:

- A=1.5: cond(e,o)=(6.4451e4,3.8473e3), residuals=(4.88e-15,1.11e-16)
- A=2.0: cond(e,o)=(4.0655e4,6.7856e3), residuals=(7.11e-15,6.66e-16)
- A=2.5: cond(e,o)=(4.8127e4,8.7582e3), residuals=(1.73e-14,7.11e-15)

Condition numbers grow substantially, as expected for a first-kind problem. Tiny algebraic residuals alone are not treated as evidence; the independent projective-characteristic agreement under N-refinement is the meaningful control.

## 6. Numerical decision

The next gate passes:

[
oxed{	ext{an independently assembled Friedrichs-adapted Galerkin solve converges to the breakpoint characteristic.}}
]

This removes the main scope limitation of v13.621. The good result there was not merely caused by projecting an already-known breakpoint solution.

Together v13.620–v13.623 now distinguish the constructions sharply:

[
oxed{	ext{bare }J_z	ext{ nodal sampling fails,}}
]

while

[
oxed{	ext{domain-faithful Galerkin finite spaces pass and may be transported losslessly to SU(2).}}
]

The SU(2) representation is therefore retained as a carrier, but its coordinate basis must not be interpreted as the physical quadrature grid.

## 7. Reproducer

Added:

`research-notes/suzuki_chi4_friedrichs_independent_galerkin.py`

## 8. Guardrails / next gate

1. This is numerical convergence evidence, not a proof of Galerkin convergence.
2. The chi_-4 screw-function normalization caveat remains; this gate compares discretizations of the same frozen kernel.
3. The finite lambda remains the finite-pair safe lambda, not a certified statement about the continuous spectral bottom.
4. No beta-zero or GRH consequence is promoted.
5. Before resuming zero-branch tests, the next useful check is an operator-level refinement audit: quadrature-order refinement of the independently assembled Galerkin matrices, singular-value/condition tracking, and comparison of Galerkin coefficient-space spectra/resolvents against the breakpoint control.
