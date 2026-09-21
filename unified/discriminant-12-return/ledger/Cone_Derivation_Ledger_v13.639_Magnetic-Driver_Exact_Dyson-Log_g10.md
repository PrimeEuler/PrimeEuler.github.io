# Cone Derivation Ledger v13.639 — Exact Magnetic-Driver Dyson–Matrix-Log Coefficients through g^10

Date: 2026-09-21

## 0. Collision/relevance check

The live ledger was checked before the calculation and again immediately before this commit. The latest numbered entry is v13.638, an external-audit addendum unrelated to the perturbative coefficients. The audit checkpoint v13.635 instructs the magnetic thread to continue the expansion with the existing fixed-j/no-all-orders guardrails. v13.639 is free.

## 1. Exact recursion

For omega=1 write the spin-1/2 equation as
[
dot U=gA(t)U,qquad U(0)=I,
]
with A(t)=-iH(t)/g. Expand
[
U(t)=I+sum_{n=1}^{10}g^nU_n(t)+O(g^{11}),
qquad
U_n(t)=int_0^tA(s)U_{n-1}(s),ds.
]
At the fast period T_f=pi, set X=U(T_f)-I and form the formal logarithm
[
log U(T_f)=sum_{k=1}^{10}{(-1)^{k+1}over k}X^k+O(g^{11}),
qquad
H_F={ioverpi}log U(T_f).
]
All integrations and matrix algebra are exact SymPy expressions; no residual fitting or numerical inference enters.

## 2. New coefficients

Projection onto J_x,J_y,J_z gives, at orders 9 and 10,
[
oxed{h_x^{(9)}={21745over7247757312}g^9},
qquad
oxed{h_y^{(9)}=0},
]
[
oxed{h_z^{(10)}={5033593over10436770529280}g^{10}},
qquad
oxed{h_y^{(10)}=0}.
]
Restoring omega by dimensional homogeneity,
[
oxed{
h_x^{(9)}=
{21745g^9over7247757312,omega^8}
}
]
and
[
oxed{
h_z^{(10)}=
{5033593g^{10}over10436770529280,omega^9}.
}
]

The positive sign of h_z^(10) is a genuine sign reversal relative to the preceding longitudinal corrections; it is an exact output of the formal logarithm, not a fit.

## 3. Extended stroboscopic Hamiltonian

Combining v13.626, v13.630, and the present result,
[
egin{aligned}
h_x={}&-{gover2}
+{g^3over128omega^2}
+{3g^5over4096omega^4}
+{341g^7over6291456omega^6}\
&+{21745g^9over7247757312omega^8}
+O(g^{11}/omega^{10}),
end{aligned}
]
while
[
egin{aligned}
h_z={}&-{g^2over16omega}
-{g^4over256omega^3}
-{61g^6over393216omega^5}
-{937g^8over905969664omega^7}\
&+{5033593g^{10}over10436770529280omega^9}
+O(g^{12}/omega^{11}).
end{aligned}
]

## 4. Parity structure

Through tenth order the exact stroboscopic result retains
[
J_x: g,g^3,g^5,g^7,g^9,ldots,
]
[
J_z: g^2,g^4,g^6,g^8,g^{10},ldots,
]
and J_y=0 through the computed order. Thus the established endpoint parity remains compatible with odd phase powers and even inversion-infidelity powers.

Writing H_F=-(g/2)(AJ_x+ZJ_z), the new dimensionless coefficients are
[
oxed{a_8=-{21745over3623878656}},
qquad
oxed{z_9=-{5033593over5218385264640}}.
]

## 5. Reproducer

`research-notes/magnetic_driver_exact_dyson_log_g10_v13_639.py`

## 6. Promotion and guardrails

Promoted: the exact fixed-order coefficients h_x^(9), h_z^(10), a_8, and z_9 above for the same bare-resonance stroboscopic protocol.

Guardrails retained exactly as requested by the audit: fixed-j asymptotics only; no uniform large-j remainder bound; no all-orders closed form; generic nonstroboscopic endpoints require micromotion kicks. Endpoint c_phi,9(j) and c_P,10(j) are not promoted in this entry; they are the next analytic-reduction gate.
