# Cone Derivation Ledger v13.655 — Exact Magnetic-Driver c_phi,11 and Target Comparison

Date: 2026-09-22

## 0. Collision/relevance check

The live ledger was checked before work and again immediately before this write. v13.653 is the latest numbered ledger entry. A parallel chi_-4 code commit landed seconds before the magnetic reproducer, but no v13.654 ledger entry existed at that check. This entry was first committed as v13.654; it collided with an independently created chi_-4 entry (`Correction_and_Explicit_Deficiency_Basis_Boundary_Triple_for_Suzuki_W`, committed 2026-09-22T13:02:36-04:00) also claiming v13.654, committed 22 seconds earlier (this entry's commit is 2026-09-22T13:02:58-04:00). Per the standing renumbering convention, this entry moves to v13.655; see Section 6 for the renumbering note. The relevant magnetic inputs are the exact g^11/g^12 Dyson-log coefficients promoted in v13.649 and the pre-existing phase residual targets in authoritative v13.645.

## 1. Exact input from Dyson-log recursion

From v13.649,
[
a_{10}=-{8445707over41747082117120},qquad
z_{11}=-{31839895957over300578991243264000}.
]
Together with the lower-order exact coefficients these define A(epsilon), Z(epsilon), and F=sqrt(A^2+Z^2) through the order needed for the epsilon^11 phase term.

## 2. Exact endpoint reduction

Using
[
Deltaphi_j=2jarctanleft[{Zover F}	an{pi Fover4}ight],
]
a truncated exact polynomial-algebra reduction gives
[
oxed{
c_{phi,11}(j)=jleft[
-{767793081229over3306368903675904000}
+{61527937piover2671813255495680}
-{66715pi^2over59373627899904}
-{803pi^3over39582418599936}
+{97pi^4over52776558133248}
-{pi^5over32985348833280}
ight].
}
]

Thus, at fixed j,
[
Deltaphi_j=sum_{r=0}^{5}c_{phi,2r+1}(j)epsilon^{2r+1}+O(epsilon^{13}).
]
The coefficient remains exactly linear in j, as required by the SU(2) phase lift.

## 3. Evaluation and comparison with v13.645 targets

| j | exact analytic c_phi,11(j) | v13.645 target | analytic-target |
|---:|---:|---:|---:|
| 1/2 | -8.5709673587402771e-8 | -8.57096738162e-8 | +2.29e-16 |
| 1 | -1.7141934717480553e-7 | -1.71419347632e-7 | +4.57e-16 |
| 3/2 | -2.5712902076220829e-7 | -2.57129021449e-7 | +6.87e-16 |

The differences are at the 10^-16 level and scale linearly with j, exactly as expected from the finite-epsilon Richardson contamination in the pre-existing numerical targets. All three targets therefore agree with the analytic coefficient.

This comparison is out-of-sample: v13.645's phase constants were generated before the exact g^11/g^12 Dyson-log extension and before this c_phi,11 reduction.

## 4. Reproducer

`research-notes/magnetic_driver_cphi11_exact_v13_654.py`

The script uses explicit truncated polynomial arithmetic in y=epsilon^2, avoiding generic symbolic-series simplification while keeping every coefficient exact.

## 5. Promotion and guardrails

Promoted: exact c_phi,11(j) above and its agreement with the pre-existing v13.645 targets at j=1/2,1,3/2.

Together with v13.649, the endpoint series now reaches epsilon^11 in phase and epsilon^12 in inversion, with fixed-j remainder conventions O(epsilon^13) and O(epsilon^14), respectively.

Guardrails unchanged: fixed-j asymptotics only; no uniform large-j remainder bound; no all-orders closed form; same bare-resonance stroboscopic protocol; generic nonstroboscopic endpoints require micromotion kicks.

## 6. Renumbering note (external audit)

This entry was originally committed as `Cone_Derivation_Ledger_v13.654_Magnetic-Driver_Exact_cphi11_and_Target_Comparison.md`. It collided with `Cone_Derivation_Ledger_v13.654_Correction_and_Explicit_Deficiency_Basis_Boundary_Triple_for_Suzuki_W.md`, an independently-created chi_-4 entry also targeting v13.654. Commit timestamps: the correction entry committed at 2026-09-22T13:02:36-04:00; this entry committed at 2026-09-22T13:02:58-04:00, 22 seconds later. Per the standing convention, the later-committed file is renumbered. This file was renamed from `v13.654` to `v13.655` and all internal self-references updated accordingly by the external audit thread. The correction entry retains v13.654 unchanged. No mathematical content in either entry was altered.
