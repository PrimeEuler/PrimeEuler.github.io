# Cone Derivation Ledger v13.642 — Magnetic-Driver Endpoint epsilon^9 / epsilon^10 Coefficients

Date: 2026-09-21

## 0. Collision/relevance check

The live ledger was checked before work and again after the reproducer commit. A parallel chi_-4 thread occupied v13.640 while the endpoint script was being committed, so this entry was first committed as v13.641. It collided with an independently created chi_-4 entry (`Free_Friedrichs_Continuum_Obstruction_and_Box_Endpoint_Factor`, committed 2026-09-21T19:25:15-04:00) also claiming v13.641, committed 33 seconds earlier (this entry's commit is 2026-09-21T19:25:48-04:00). Per the standing renumbering convention (later commit timestamp is renumbered), this entry moves to v13.642; see Section 8 for the renumbering note. The input coefficients are the exact v13.639 Dyson-log values; no v13.634 residual constant is used as a fit.

## 1. Inputs

With H_F=-(g/2)(A J_x+Z J_z), v13.639 extends
[
A=1-{epsilon^2over64}-{3epsilon^4over2048}-{341epsilon^6over3145728}
-{21745epsilon^8over3623878656}+O(epsilon^{10}),
]
[
Z={epsilonover8}+{epsilon^3over128}+{61epsilon^5over196608}
+{937epsilon^7over452984832}
-{5033593epsilon^9over5218385264640}+O(epsilon^{11}).
]
Set F=sqrt(A^2+Z^2).

## 2. Ninth-order half-pulse phase

The exact endpoint map is
[
Deltaphi_j=2jarctanleft[{Zover F}	an{pi Fover4}ight].
]
Expanding at fixed j through epsilon^9 gives
[
oxed{
c_{phi,9}(j)=
{jleft(
-470860912-5604840pi+1485540pi^2-119880pi^3+2025pi^4
ight)over166988328468480}.
}
]
Thus
[
Deltaphi_j=sum_{r=0}^{4}c_{phi,2r+1}(j)epsilon^{2r+1}+O(epsilon^{11}),
]
with the lower four coefficients exactly those promoted in v13.617, v13.626, and v13.630.

## 3. Tenth-order inversion

For spin 1/2,
[
P_{1/2}={A^2over F^2}sin^2{pi Fover2},
]
and exact SU(2) lifting gives P_j=P_{1/2}^{2j}. Therefore
[
oxed{
c_{P,10}(j)=
{jover333976656936960}
Big[
82944j^4-(7879680+51840pi^2)j^3
+(184032000+1982880pi^2+4860pi^4)j^2
]
[
qquadqquad
-(1019911680+11681820pi^2+32400pi^4)j
+647183200+4596345pi^2+5265pi^4
Big].
}
]
Hence
[
1-P_j^{inv}=sum_{r=1}^{5}c_{P,2r}(j)epsilon^{2r}+O(epsilon^{12}).
]

## 4. Parity and remainder structure

The endpoint reduction preserves the established parity:
[
Deltaphi_j:epsilon,epsilon^3,epsilon^5,epsilon^7,epsilon^9,ldots,
]
[
1-P_j^{inv}:epsilon^2,epsilon^4,epsilon^6,epsilon^8,epsilon^{10},ldots.
]
The remainder convention is fixed-j:
[
oxed{R_phi^{(9)}=O(epsilon^{11})},qquad
oxed{R_P^{(10)}=O(epsilon^{12})}.
]

## 5. Independence from the residual audit

v13.634 established before this derivation that subtraction through epsilon^7/epsilon^8 leaves O(epsilon^9)/O(epsilon^10) residuals. Those residuals were not used to determine the present exact coefficients. They now become independent numerical targets for a follow-up high-precision check.

## 6. Reproducer

`research-notes/magnetic_driver_endpoint_e9_e10_v13_640.py`

The script filename reflects the version available when it was created; a parallel chi_-4 commit occupied v13.640 before the ledger write. This entry v13.642 is authoritative (see Section 8).

## 7. Promotion and guardrails

Promoted: c_phi,9(j) and c_P,10(j) above for fixed j in the same bare-resonance stroboscopic protocol.

Guardrails retained: no uniform large-j remainder bound; no all-orders closed form; generic nonstroboscopic endpoints require micromotion kicks. No epsilon^11 phase or epsilon^12 inversion coefficient is claimed here.

## 8. Renumbering note (external audit)

This entry was originally committed as `Cone_Derivation_Ledger_v13.641_Magnetic-Driver_Endpoint_e9_e10.md`. It collided with `Cone_Derivation_Ledger_v13.641_Free_Friedrichs_Continuum_Obstruction_and_Box_Endpoint_Factor.md`, an independently-created chi_-4 entry also targeting v13.641. Commit timestamps: the Free-Friedrichs entry committed at 2026-09-21T19:25:15-04:00; this entry committed at 2026-09-21T19:25:48-04:00, 33 seconds later. Per the standing convention, the later-committed file is renumbered. This file was renamed from `v13.641` to `v13.642` and all internal self-references updated accordingly by the external audit thread. The Free-Friedrichs entry retains v13.641 unchanged. No mathematical content in either entry was altered.
