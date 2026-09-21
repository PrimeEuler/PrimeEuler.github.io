# Cone Derivation Ledger v13.617 — Magnetic-Driver Next Endpoint Coefficients

Date: 2026-09-21

## 0. Live collision and relevance check

The live ledger advanced after v13.613: v13.614 is a chi_-4 control gate, v13.615 is External Audit Round 65, and v13.616 is a chi_-4 breakpoint sweep. Round 65 independently re-derived the v13.613 commutators and executed its reproducer, confirming the cubic Floquet result. No entry derives the next magnetic endpoint coefficients. v13.617 was free before the reproducer commit and remained free immediately before this ledger commit.

## 1. A necessary refinement of the proposed gate

v13.613 supplied the cubic transverse term and quadratic longitudinal term,
[
H_{m strob}=
left(-rac g2+rac{g^3}{128omega^2}ight)J_x
-rac{g^2}{16omega}J_z+cdots.
]
Those orders determine the leading endpoint laws, but they do **not** by themselves determine the complete epsilon^3 phase coefficient or epsilon^4 inversion coefficient. The reason is that the next longitudinal Floquet term, O(g^4/omega^3) J_z, enters the tilt at O(epsilon^3), and its interference with the leading tilt enters inversion at O(epsilon^4).

Thus the next gate must include that term.

## 2. Stroboscopic Floquet recursion one order farther

Expanding the one-period spin-1/2 Floquet problem (equivalently the Fourier/Sambe recursion) through fourth order gives
[
oxed{
H_{m strob}
=
left(-rac g2+rac{g^3}{128omega^2}ight)J_x
-
left(rac{g^2}{16omega}+rac{g^4}{256omega^3}ight)J_z
+O(g^5/omega^4).
}
]
The new coefficient is therefore
[
oxed{-rac1{256}}
]
for the quartic longitudinal term.

An independent matrix-log extraction from the exact one-fast-period propagator converges to
[
rac{a_x+g/2}{g^3}	orac1{128},
qquad
rac{a_z+g^2/(16omega)}{g^4/omega^3}	o-rac1{256}.
]

## 3. Dimensionless slow axis

Set epsilon=g/omega. Factoring g/2 from the magnitude,
[
A=1-rac{epsilon^2}{64}+O(epsilon^4),
qquad
Z=rac{epsilon}{8}+rac{epsilon^3}{128}+O(epsilon^5).
]
Then
[
F=sqrt{A^2+Z^2}
=1-rac{epsilon^2}{128}+O(epsilon^4).
]

At the nominal half pulse t=T_pi/2=pi/g, the spin-1/2 relative component-phase spread is
[
deltaphi_{1/2}
=
arctan!left[rac{Z}{F}	an!left(rac{pi F}{4}ight)ight].
]
Expanding,
[
deltaphi_{1/2}
=
rac{epsilon}{8}
+
left(rac{25}{3072}-rac{pi}{2048}ight)epsilon^3
+O(epsilon^5).
]

The spin-j multiplet is the 2j-th symmetric power, so its full component-phase range is 2j times the fundamental range:
[
oxed{
Deltaphi_j(T_pi/2)
=
rac j4epsilon
+
rac{j(50-3pi)}{3072}epsilon^3
+O(epsilon^5).
}
]

Thus
[
oxed{c_phi(j)=rac{j(50-3pi)}{3072}.}
]

## 4. Inversion through epsilon^4

At T_pi=2pi/g the fundamental inversion probability is
[
P_{1/2}^{m inv}
=
rac{A^2}{F^2}
sin^2!left(rac{pi F}{2}ight).
]
Expansion gives
[
1-P_{1/2}^{m inv}
=
rac{epsilon^2}{64}
+
left(
rac{9}{4096}+rac{pi^2}{65536}
ight)epsilon^4
+O(epsilon^6).
]

Using the exact SU(2) extremal-transfer identity
[
P_j^{m inv}=(P_{1/2}^{m inv})^{2j},
]
we obtain
[
oxed{
1-P_j^{m inv}
=
rac j{32}epsilon^2
+
rac{j(pi^2+152-16j)}{32768}epsilon^4
+O(epsilon^6).
}
]

Hence
[
oxed{
c_P(j)=rac{j(pi^2+152-16j)}{32768}.
}
]

The j-dependence at quartic order contains the expected binomial/symmetric-power correction -16j^2.

## 5. Parity structure

For the stroboscopic bare-resonance protocol:
- phase spread is odd in |epsilon| as a magnitude expansion: epsilon, epsilon^3, ...;
- inversion infidelity is even: epsilon^2, epsilon^4, ....

This sharpens the v13.607 remainder statements:
[
Deltaphi_j=rac j4epsilon+O(epsilon^3)
]
to an explicit cubic coefficient, and
[
1-P_j^{m inv}=rac j{32}epsilon^2+O(epsilon^4)
]
to an explicit quartic coefficient.

## 6. Reproducer

Added:
`research-notes/magnetic_driver_next_endpoint_coefficients_v13_617.py`

It extracts the exact one-period spin-1/2 Floquet Hamiltonian by matrix logarithm and checks convergence of the transverse cubic coefficient to 1/128 and the longitudinal quartic coefficient to -1/256.

## 7. Promotion and guardrails

Promoted for the same bare-resonance, stroboscopic protocol fixed in v13.607:
[
oxed{
Deltaphi_j(T_pi/2)
=
rac j4epsilon
+
rac{j(50-3pi)}{3072}epsilon^3
+O(epsilon^5)
}
]
and
[
oxed{
1-P_j^{m inv}(T_pi)
=
rac j{32}epsilon^2
+
rac{j(pi^2+152-16j)}{32768}epsilon^4
+O(epsilon^6).
}
]

Guardrails:
1. The quartic longitudinal Floquet coefficient is essential; truncating at v13.613 gives incorrect next endpoint coefficients.
2. These are stroboscopic bare-resonance formulas. Generic epsilon/observation times require endpoint kicks.
3. Fixed-j asymptotics are intended; no uniform large-j error bound is claimed.
