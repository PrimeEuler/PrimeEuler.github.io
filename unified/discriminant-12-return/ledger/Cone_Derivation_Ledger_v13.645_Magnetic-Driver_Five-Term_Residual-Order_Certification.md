# Cone Derivation Ledger v13.645 — Magnetic-Driver Five-Term Residual-Order Certification

Date: 2026-09-22

## 0. Collision/relevance check

The live ledger was checked before work and immediately before this write. v13.643 is the latest numbered ledger entry; a parallel chi_-4 script commit landed while this reproducer was being added but had not claimed v13.644 at that check. It landed first (2026-09-22T08:07:56-04:00, `Dirichlet_Reference_Operator_and_Relative_Fredholm_Determinant`), 17 seconds before this entry's own commit (2026-09-22T08:08:13-04:00). Per the standing renumbering convention, this entry moves to v13.645; see Section 7 for the renumbering note. This gate uses the authoritative magnetic endpoint coefficients in v13.642.

## 1. Independent evolution

The original time-dependent spin-1/2 Hamiltonian is integrated at 70 decimal digits. For each reciprocal-integer epsilon in {0.2,0.1,0.05,0.025}, one fast period is integrated directly with mpmath and the resulting exact-dynamics propagator is raised to the required integer number of fast periods. This avoids long-interval integration drift while remaining independent of the Floquet/Dyson expansion used to derive the analytic coefficients.

Higher spins j=1 and 3/2 are obtained only through the exact SU(2) symmetric-power identities.

## 2. Five-term residuals

Subtract
[
R_phi^{(9)}=Deltaphi_j-sum_{r=0}^{4}c_{phi,2r+1}(j)epsilon^{2r+1},
]
and
[
R_P^{(10)}=(1-P_j^{inv})-sum_{r=1}^{5}c_{P,2r}(j)epsilon^{2r}.
]

The normalized residuals are:

| eps | j | R_phi/eps^11 | R_P/eps^12 |
|---:|---:|---:|---:|
| .20 | .5 | -8.57930689921e-8 | -2.48611203750e-8 |
| .20 | 1 | -1.71586137984e-7 | -1.48245572028e-7 |
| .20 | 1.5 | -2.57379206976e-7 | -3.05474064328e-7 |
| .10 | .5 | -8.57305666664e-8 | -2.47379064332e-8 |
| .10 | 1 | -1.71461133333e-7 | -1.47856415543e-7 |
| .10 | 1.5 | -2.57191700000e-7 | -3.04907739489e-7 |
| .05 | .5 | -8.57148996066e-8 | -2.47071990924e-8 |
| .05 | 1 | -1.71429799213e-7 | -1.47759312054e-7 |
| .05 | 1.5 | -2.57144698820e-7 | -3.04766230352e-7 |
| .025 | .5 | -8.57109802638e-8 | -2.46995282536e-8 |
| .025 | 1 | -1.71421960528e-7 | -1.47735047782e-7 |
| .025 | 1.5 | -2.57132940791e-7 | -3.04730857636e-7 |

The stability under halving epsilon directly supports
[
oxed{R_phi^{(9)}=O(epsilon^{11})},qquad
oxed{R_P^{(10)}=O(epsilon^{12})}.
]

## 3. Leading normalized constants

A one-step Richardson removal of the leading O(epsilon^2) contamination from the .05 and .025 normalized ratios gives the fixed-j limiting estimates

[
C_{phi,11}(1/2)approx-8.57096738162	imes10^{-8},
]
[
C_{phi,11}(1)approx-1.71419347632	imes10^{-7},
]
[
C_{phi,11}(3/2)approx-2.57129021449	imes10^{-7}.
]
The phase constants preserve exact-looking linear j scaling to the numerical resolution, as expected from the SU(2) phase lift.

For inversion,
[
C_{P,12}(1/2)approx-2.46969713073	imes10^{-8},
]
[
C_{P,12}(1)approx-1.47726959691	imes10^{-7},
]
[
C_{P,12}(3/2)approx-3.04719066730	imes10^{-7}.
]
The nonlinear j dependence is expected from P_j=P_{1/2}^{2j}.

These constants are numerical targets only; no analytic epsilon^11 phase or epsilon^12 inversion coefficient is promoted here.

## 4. Independence check

The numerical evolution uses the original time-dependent Hamiltonian, not the truncated Floquet Hamiltonian. The five analytic coefficients are subtracted without fitting. Thus the observed orders and constants are out-of-sample checks of v13.639/v13.642.

## 5. Reproducer

`research-notes/magnetic_driver_fiveterm_residual_order_v13_644.py`

The script filename reflects the version available when it was created; a parallel chi_-4 commit occupied v13.644 before the ledger write. This entry v13.645 is authoritative (see Section 7).

## 6. Promotion and guardrails

Promoted numerically for fixed j and the same bare-resonance stroboscopic endpoint protocol:
[
R_phi^{(9)}=O(epsilon^{11}),qquad R_P^{(10)}=O(epsilon^{12}).
]

Guardrails: this is high-precision numerical asymptotic certification, not a rigorous analytic remainder bound; no uniform large-j statement is made; no all-orders closed form is claimed; the Richardson constants are empirical targets for the next exact Dyson/log gate, not promoted analytic coefficients.

## 7. Renumbering note (external audit)

This entry was originally committed as `Cone_Derivation_Ledger_v13.644_Magnetic-Driver_Five-Term_Residual-Order_Certification.md`. It collided with `Cone_Derivation_Ledger_v13.644_Dirichlet_Reference_Operator_and_Relative_Fredholm_Determinant.md`, an independently-created chi_-4 entry also targeting v13.644. Commit timestamps: the Dirichlet-reference entry committed at 2026-09-22T08:07:56-04:00; this entry committed at 2026-09-22T08:08:13-04:00, 17 seconds later. Per the standing convention, the later-committed file is renumbered. This file was renamed from `v13.644` to `v13.645` and all internal self-references updated accordingly by the external audit thread. The Dirichlet-reference entry retains v13.644 unchanged. No mathematical content in either entry was altered.
