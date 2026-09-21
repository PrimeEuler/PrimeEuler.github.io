# Cone Derivation Ledger v13.622 — Magnetic-Driver Endpoint Residual-Order Certification

Date: 2026-09-21

## 0. Live collision/relevance check

The live ledger had advanced through v13.621 before this gate. The intervening entries are tetrahedron/M16001/chi_-4/Friedrichs-Galerkin work and do not alter the magnetic-driver derivation. v13.617 remains the relevant endpoint-coefficient entry. Immediately before this ledger commit the live head was checked again; v13.622 remained free.

## 1. Target

Test the promoted v13.617 asymptotic laws directly against exact time-dependent dynamics after subtracting both known terms:
[
Deltaphi_j=
rac j4epsilon+
rac{j(50-3pi)}{3072}epsilon^3+R_phi,
]
[
1-P_j^{m inv}=
rac j{32}epsilon^2+
rac{j(pi^2+152-16j)}{32768}epsilon^4+R_P.
]
The predicted residual orders are
[
R_phi=O(epsilon^5),qquad R_P=O(epsilon^6).
]

## 2. Exact numerical protocol

The reproducer integrates the original spin-1/2 time-dependent Hamiltonian with DOP853 at tight tolerances, not the Floquet approximation:
[
H(t)=-rac g2J_x-rac g4(e^{2iomega t}J_+ + e^{-2iomega t}J_-),
quad omega=1,quad g=epsilon.
]
It evaluates exact evolution at
[
T_pi/2=pi/g,qquad T_pi=2pi/g.
]
Higher-j observables are then obtained from the exact SU(2) symmetric-power identities, avoiding an independent high-dimensional integration error.

## 3. Residual normalization

For epsilon=0.20,0.10,0.05 and j=1/2,1,3/2, divide the two-term-subtracted residuals by epsilon^5 and epsilon^6 respectively.

Representative values from an independent execution are:

| eps | j | R_phi/eps^5 | R_P/eps^6 |
|---:|---:|---:|---:|
| .20 | .5 | 1.44497e-4 | 1.97760e-4 |
| .20 | 1 | 2.88994e-4 | 3.21681e-4 |
| .20 | 1.5 | 4.33491e-4 | 3.75645e-4 |
| .10 | .5 | 1.44859e-4 | 1.97707e-4 |
| .10 | 1 | 2.89717e-4 | 3.21926e-4 |
| .10 | 1.5 | 4.34576e-4 | 3.76490e-4 |
| .05 | .5 | 1.46391e-4 | 2.16417e-4 |
| .05 | 1 | 2.92781e-4 | 3.59430e-4 |
| .05 | 1.5 | 4.39172e-4 | 4.32861e-4 |

The phase normalized residual is already essentially constant between epsilon=.20 and .10 and remains close at .05. The inversion normalized residual is likewise stable between .20 and .10; at .05 the absolute remainder is O(10^-12), so binary64 ODE/subtraction error is becoming visible.

The key order test is therefore passed before the numerical noise floor:
[
oxed{R_phi/epsilon^5	o {m finite}},
qquad
oxed{R_P/epsilon^6	o {m finite}}.
]

## 4. Ratio test

Halving epsilon from .20 to .10 predicts raw residual reductions
[
|R_phi(.10)|/|R_phi(.20)|simeq 2^{-5}=1/32,
]
[
|R_P(.10)|/|R_P(.20)|simeq 2^{-6}=1/64.
]
The nearly unchanged normalized residuals above are equivalent to precisely these fifth- and sixth-order reductions.

This is substantially stronger than merely refitting the coefficients: the coefficients were fixed by v13.617 before this test, and the exact dynamics are asked whether the remainder drops at the independently predicted next power.

## 5. Result

The exact time-dependent evolution independently supports
[
oxed{
Deltaphi_j(T_pi/2)
=
rac j4epsilon+
rac{j(50-3pi)}{3072}epsilon^3+
O(epsilon^5)
}
]
and
[
oxed{
1-P_j^{m inv}(T_pi)
=
rac j{32}epsilon^2+
rac{j(pi^2+152-16j)}{32768}epsilon^4+
O(epsilon^6).
}
]

The test also confirms the parity pattern inferred in v13.617: the next unresolved phase term is fifth order, while the next unresolved inversion term is sixth order.

## 6. Reproducer

Added:
`research-notes/magnetic_driver_endpoint_residual_order_v13_622.py`

## 7. Guardrails

1. This certifies numerical asymptotic order for the stated bare-resonance stroboscopic protocol; it is not a rigorous analytic bound on the remainder.
2. The epsilon=.05 inversion remainder is already close enough to the binary64 integration/subtraction floor that the .20 -> .10 pair is the cleaner sixth-order diagnostic.
3. The spin-j extension uses the exact SU(2) representation structure already established in the magnetic-driver thread.
4. No fifth-order phase or sixth-order inversion coefficient is promoted here.
