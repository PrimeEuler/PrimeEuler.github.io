# Cone Derivation Ledger v13.626 — Exact Fifth-Order Phase and Sixth-Order Inversion Coefficients

Date: 2026-09-21

## 0. Collision/relevance check

The live ledger advanced to v13.625 (chi_-4 Galerkin operator certification), so the magnetic entry moved to v13.626. The live head was checked again immediately before this commit. No magnetic result superseded v13.622.

## 1. Safe-route Floquet derivation

Rather than infer higher coefficients from the v13.622 residuals, expand the exact one-fast-period spin-1/2 propagator by the Dyson recursion
[
U(t)=I+sum_{nge1}g^n U_n(t),qquad
U_n(t)=int_0^t A(s)U_{n-1}(s),ds,
]
where A(t)=-iH(t)/g and T_f=pi/omega. Then form the formal matrix logarithm
[
H_F={iover T_f}log U(T_f)
]
coefficient-by-coefficient through g^6. This is exact symbolic algebra; no floating-point fit enters.

For omega=1 the nonzero stroboscopic coefficients are
[
h_x=-{gover2}+{g^3over128}+{3g^5over4096}+O(g^7),
]
[
h_z=-{g^2over16}-{g^4over256}-{61g^6over393216}+O(g^8).
]
Restoring omega,
[
oxed{h_x=-{gover2}+{g^3over128omega^2}+{3g^5over4096omega^4}+O(g^7/omega^6)}
]
and
[
oxed{h_z=-{g^2over16omega}-{g^4over256omega^3}-{61g^6over393216omega^5}+O(g^8/omega^7)}.
]

Thus, with H_F=-(g/2)(A J_x+Z J_z) up to the common sign convention,
[
A=1-{epsilon^2over64}-{3epsilon^4over2048}+O(epsilon^6),
]
[
Z={epsilonover8}+{epsilon^3over128}+{61epsilon^5over196608}+O(epsilon^7).
]
These are the previously missing
[
oxed{a_4=-3/2048,qquad z_5=61/196608}.
]

## 2. Half-pulse phase through fifth order

At T_pi/2=pi/g,
[
deltaphi_{1/2}=
arctanleft[{Zover F}	anleft({pi Fover4}ight)ight],
qquad F=sqrt{A^2+Z^2}.
]
The spin-j full component phase range is 2j delta-phi. Exact series expansion gives
[
oxed{
Deltaphi_j=
{jover4}epsilon+
{j(50-3pi)over3072}epsilon^3+
{j(4676-810pi+15pi^2)over7864320}epsilon^5+
O(epsilon^7).
}
]
Therefore
[
oxed{c_{phi,5}(j)={j(4676-810pi+15pi^2)over7864320}}.
]
For j=1/2,
[
c_{phi,5}=1.44917425575804	imes10^{-4},
]
matching the independent v13.622 normalized residual (~1.45e-4).

## 3. Inversion through sixth order

At T_pi=2pi/g,
[
P_{1/2}={A^2over F^2}sin^2left({pi Fover2}ight),
qquad P_j=P_{1/2}^{2j}.
]
Expansion gives
[
oxed{
1-P_j=
{jover32}epsilon^2+
{j(pi^2+152-16j)over32768}epsilon^4+
{jleft(64j^2-(1824+12pi^2)j+5536+39pi^2ight)over12582912}epsilon^6+
O(epsilon^8).
}
]
Thus
[
oxed{
c_{P,6}(j)=
{jleft(64j^2-(1824+12pi^2)j+5536+39pi^2ight)over12582912}.
}
]
For j=1/2,
[
c_{P,6}=1.97319068322021	imes10^{-4},
]
matching the independent v13.622 residual 1.977e-4 before its binary64 floor.

## 4. Independent-target logic

The v13.622 residual coefficients were produced before the exact g^5/g^6 Floquet coefficients were derived. They therefore function as an independent numerical target rather than input. The analytic values land on those targets.

## 5. Reproducers

- `research-notes/magnetic_driver_exact_dyson_log_v13_626.py`: exact Dyson recursion and formal matrix logarithm through sixth order.
- `research-notes/magnetic_driver_fifth_sixth_coefficients_v13_625.py`: exact symbolic endpoint reduction after substitution of a4,z5.

## 6. Promotion and guardrails

Promoted for the same bare-resonance stroboscopic protocol:
[
Deltaphi_j={jover4}epsilon+{j(50-3pi)over3072}epsilon^3+
{j(4676-810pi+15pi^2)over7864320}epsilon^5+O(epsilon^7),
]
[
1-P_j={jover32}epsilon^2+{j(pi^2+152-16j)over32768}epsilon^4+
{j(64j^2-(1824+12pi^2)j+5536+39pi^2)over12582912}epsilon^6+O(epsilon^8).
]

Guardrails: fixed-j asymptotics; stroboscopic bare resonance; no uniform large-j remainder bound; no seventh/eighth-order coefficient claimed.
