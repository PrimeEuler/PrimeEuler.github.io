# Xi feasibility — sandbox return to the v14.700 HANDOFF (2026-10-22)

Producer: xi_feasibility.py (runs clean end to end).

DESIGN (program bench anchors): source 2 kg at R = 0.10 m, position-
modulated; rotor = solid aluminium paraboloid pair (a = h = 0.05 m),
apex-to-apex; deliberate axial unbalance l = 1.0 mm.

GEOMETRY (exact integrals, numeric): pair mass 1.0603 kg;
A = 1.3254e-3, B = 4.4179e-4 kg m^2; I_kin = 1.7671e-3;
q = 8.8357e-4; q/I_kin = 0.500 EXACTLY for the solid paraboloid pair
(A = 3B per paraboloid) — v14.700 S5's finite-body qualification
made concrete: calibrating q as I_kin would bias Xi by a factor 2.

COUPLINGS: Phi' = 1.335e-8 m/s^2; gradient combo 4.004e-7 s^-2;
Xi reconstructed from the beta ratio = 1.000000 (internal check).
Rotational constant 4.75e-33 Hz — quantum spectroscopy of the macro
rotor is NOT a readout (negative sub-verdict); observables are the
classical torques: rank-1 1.415e-11 N m, rank-2 3.538e-10 N m,
4-6 orders above 1e-15 N m/sqrt(Hz) torsion floors. Not readout-limited.

BACKGROUNDS: Earth uniform g through the unbalance is 7.3e8 x the
source rank-1 torque (DC; source modulation + lock-in separates;
tilt noise at f_mod is the feedthrough: 1 nrad/sqrt(Hz) -> beta1 to
~0.7% in 1e4 s; 0.1 nrad -> ~0.1%). Earth gradient 7.7 x the source
combo, static, with the source's tensor signature rotating under
modulation. A 70 kg person at 3 m is 1157 x below the source torque.

BUDGET (1 sigma, relative): l cal 0.50%, q cal 0.50%, R 0.01%,
geometry factor 0.20%, stiffness ratio 0.70%, rank-2 systematics
0.30% -> TOTAL 1.06% on Xi. Discriminates Xi = (p+2)/3 at |dp| ~ 0.03.

VERDICT: POSITIVE as an apparatus/null-test study, per the handoff's
framing. Design driver = sub-nrad tilt stability at f_mod (rank-1
channel) + the l and q calibrations. Not competitive with dedicated
inverse-square torsion balances on p itself; the value is the
single-device two-channel null. G used only to size signals
(calibration-only, labeled in the producer); G_derived = false;
Xi = 1 is the standard-gradiometry expectation (novelty-negative
per v14.700, unchanged).
