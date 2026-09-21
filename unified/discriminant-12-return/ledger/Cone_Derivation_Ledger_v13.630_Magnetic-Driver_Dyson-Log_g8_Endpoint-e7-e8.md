# Cone Derivation Ledger v13.630 — Magnetic-Driver Dyson–Log through g^8 and Endpoint epsilon^7/epsilon^8 Terms

Date: 2026-09-21

## 0. Live collision/relevance check

The live ledger had advanced through v13.629. External Audit Round 66 (v13.628) independently reproduced the v13.626 fifth/sixth magnetic coefficients at high precision, providing relevant independent support. v13.629 is unrelated chi_-4 work. The head was checked again after the reproducer commit; v13.630 remained free.

## 1. Exact Dyson–matrix-log extension

Continue the exact spin-1/2 Dyson recursion for one fast period through n=8 and form the formal matrix logarithm coefficient-by-coefficient. No floating-point fitting is used.

The new nonzero stroboscopic Floquet coefficients are
[
oxed{h_x^{(7)}={341g^7over6291456,omega^6}},
qquad
oxed{h_z^{(8)}=-{937g^8over905969664,omega^7}}.
]

Together with v13.626,
[
h_x=-{gover2}+{g^3over128omega^2}+{3g^5over4096omega^4}
+{341g^7over6291456omega^6}+O(g^9/omega^8),
]
[
h_z=-{g^2over16omega}-{g^4over256omega^3}
-{61g^6over393216omega^5}
-{937g^8over905969664omega^7}+O(g^{10}/omega^9).
]

Hence the dimensionless slow-axis series acquire
[
oxed{a_6=-{341over3145728}},
qquad
oxed{z_7={937over452984832}},
]
where
[
A=1-{epsilon^2over64}-{3epsilon^4over2048}
-{341epsilon^6over3145728}+O(epsilon^8),
]
[
Z={epsilonover8}+{epsilon^3over128}
+{61epsilon^5over196608}
+{937epsilon^7over452984832}+O(epsilon^9).
]

## 2. Endpoint phase through epsilon^7

Using
[
deltaphi_{1/2}=arctan!left[{Zover F}	an{pi Fover4}ight],
quad F=sqrt{A^2+Z^2},
]
and Delta-phi_j=2j delta-phi_1/2, exact symbolic reduction gives the next term
[
oxed{
c_{phi,7}(j)=
-{jleft(75004+69678pi-3024pi^2+63pi^3ight)over12683575296}.
}
]

Thus
[
Deltaphi_j=
{jover4}epsilon+
{j(50-3pi)over3072}epsilon^3+
{j(4676-810pi+15pi^2)over7864320}epsilon^5
+c_{phi,7}(j)epsilon^7+O(epsilon^9).
]

For j=1/2,
[
c_{phi,7}=-1.04864597887745	imes10^{-5}.
]

## 3. Endpoint inversion through epsilon^8

Using
[
P_{1/2}={A^2over F^2}sin^2{pi Fover2},
qquad P_j=P_{1/2}^{2j},
]
the next exact coefficient is
[
oxed{
c_{P,8}(j)=
-{jover115964116992}
left[
4608j^3-(262656+1728pi^2)j^2
+(2841984+27648pi^2+54pi^4)j
-3759104-26622pi^2-9pi^4
ight].
}
]

Therefore the v13.626 inversion series extends by
[
1-P_j^{inv}=cdots+c_{P,8}(j)epsilon^8+O(epsilon^{10}).
]

Numerically,
[
c_{P,8}(1/2)=1.09172628924621	imes10^{-5},
]
[
c_{P,8}(1)=1.01558403042407	imes10^{-5},
]
[
c_{P,8}(3/2)=-5.64640931153744	imes10^{-7}.
]
The sign change with j is allowed: this is a subleading coefficient, while the full infidelity remains nonnegative.

## 4. Structural pattern

Through this order the exact stroboscopic Floquet Hamiltonian retains the alternating parity pattern:
- J_x contains odd powers g,g^3,g^5,g^7,...;
- J_z contains even powers g^2,g^4,g^6,g^8,...;
- no J_y term appears.

Correspondingly the endpoint phase remains odd in epsilon and inversion infidelity even in epsilon.

## 5. Reproducer

`research-notes/magnetic_driver_dyson_log_g8_endpoint_v13_630.py` performs the exact Dyson recursion through n=8, formal matrix logarithm, and symbolic endpoint reduction.

## 6. Promotion and guardrails

Promoted for fixed j in the same bare-resonance stroboscopic protocol:
[
h_x^{(7)}={341g^7over6291456omega^6},quad
h_z^{(8)}=-{937g^8over905969664omega^7},
]
and the endpoint coefficients c_phi,7(j), c_P,8(j) above.

Guardrails: no uniform large-j remainder claim; no epsilon^9/epsilon^10 endpoint coefficient claimed; generic nonstroboscopic times still require endpoint kicks.
