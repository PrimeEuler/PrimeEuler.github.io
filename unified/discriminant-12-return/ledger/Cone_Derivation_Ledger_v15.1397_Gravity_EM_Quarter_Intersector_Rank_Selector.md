# Cone Derivation Ledger v15.1397 — Conditional finite-SU2 cross-grid tensor-rank selection for half-grid EM and closed quarter carrier

**Date:** 2026-11-24 Eastern. **Track:** Gravity/Cone. **Classification:** [D/PASS conditional] exact Wigner–Eckart/triangle constraints for hypothetical common diagonal SU(2) action linking D-dimensional EM Schwinger shell to its separately defined closed 2D-dimensional refined quarter carrier; [NEGATIVE] scalar link forbidden at every D, vector link possible only at D=2, low-rank quadrupole link possible only at D=2,4, all odd-D shells have opposite SU(2) center parity obstructing ordinary integer-rank tensor operators; [OPEN] existence of common physical SU(2) gauge action, actual covariant finite-carrier intertwiner, independent dynamical coupling strength and connection to continuous SO+(2,1) sigma target. The previous v15.1393 noncompact boost obstruction and v15.1387 radius/free-coefficient degeneracy remain in effect. Strict additive.

## Gate 1319 — pair the genuine carriers, not the formal quarter Casimir

Fix the old EM D-state shell spin `j_E=(D−1)/2` and the **closed refined** quarter carrier spin `J_Q=(2D−1)/2`, dimension 2D, from the audited q2 operator dictionary v15.972/973. These are both genuine ordinary finite SU(2) irreducible representations. Do not use formal geometric spin `(2D−1)/4`, which is not the spin of the closed 2D q2 carrier. **Conditional hypothesis for this gate:** a common diagonal SU(2) symmetry acts consistently on both physical sectors and a mixing operator transforms as an irreducible spherical tensor of integer rank K=0,1,2 (respectively scalar, vector, quadrupole); the existence of this common action is not established by Cone geometry.

Wigner–Eckart imposes `|J_Q−j_E|≤K≤J_Q+j_E`, and `J_Q−j_E−K` integral. Since

`J_Q−j_E=D/2`,

the smallest allowed tensor rank is D/2, subject to a compatible parity. The SU(2) central element −1 acts on spin-j as `(−1)^(2j)`. On EM spin `(−1)^(D−1)`, on quarter spin `(−1)^(2D−1)=−1`, so **center parity matches only for even D**. For odd D, an ordinary integer-rank tensor operator has trivial center and cannot connect the sectors at all under the stated common SU(2). A spinorial half-integer-rank operator is algebraically possible, but it requires its own fermionic/spinorial physical carrier or spurion, and is not the ordinary bosonic scalar/vector/quadrupole EM or metric field assumed in this gate.

## Gate 1320 — exact finite-shell results

Executed local SymPy test `/mnt/data/cone_gate/quarter_cross_sector_rank_v15_1397.py` for D=2..12, checking every small tensor rank and parity condition:

| D | EM spin j_E | q2 spin J_Q | minimum tensor rank D/2 | permitted ranks K≤2 |
|---:|---:|---:|---:|---|
| 2 | 1/2 | 3/2 | 1 | 1, 2 |
| 3 | 1 | 5/2 | 3/2 | none |
| 4 | 3/2 | 7/2 | 2 | 2 |
| 5 | 2 | 9/2 | 5/2 | none |
| 6 | 5/2 | 11/2 | 3 | none |
| 7 | 3 | 13/2 | 7/2 | none |
| 8 | 7/2 | 15/2 | 4 | none |
| 9 | 4 | 17/2 | 9/2 | none |
| 10 | 9/2 | 19/2 | 5 | none |
| 11 | 5 | 21/2 | 11/2 | none |
| 12 | 11/2 | 23/2 | 6 | none |

Hence rank-0 scalar mixing is **never** allowed for these unequal spins; rank-1 vector mixing is allowed only for D=2; rank-2 quadrupole mixing only for D=2 or 4. These are **necessary** representation-theoretic selection rules for the conditional shared SU(2) scenario. Nonzero reduced matrix element is not guaranteed by satisfying triangle and center constraints; an actual interaction matrix element requires dynamical construction and a coefficient. Non-invariant explicit symmetry-breaking, multiple bosonic operators whose total tensor rank is high enough, or a distinct common gauge/spin structure can bypass this specific low-rank conditional no-go, and are not excluded.

**Additive GitHub reproducer:** `research-notes/k4_quarter_intersector_rank_selection_v15_1397.py`, commit **69ea38bbad9f6279c281a1b5b30e58c05526dfcd**. Locally executed mathematically identical code passed the checks. Exact GitHub-byte Audit replay pending.

## Gate 1321 — separate the possible bridge from the proposed continuous H² coupling

v15.1393 proved the original **finite** SU2 carrier has no nontrivial unitary *continuous* SO+(2,1) boost representation; this gate additionally shows a hypothetical shared SU2 **low-rank bosonic sector-mixing interaction** is severely restricted, especially for D≥5. The currently working continuous H²/Weyl–Maxwell EFT (v15.1380–1392) instead assumes two freely propagating real sigma coordinates on a **continuous** hyperboloid and a freely selected interaction coefficient. Those extra fields do not automatically carry these finite-SU2 tensor matrix elements. It would be wrong to apply the low-rank finite-SU2 selection to the continuous sigma EFT as an unconditional absence of its radiation. Conversely, nonzero sigma-EFT radiation is not evidence of a true inter-sector quarter-SU2 gauge intertwiner.

**AUDIT:** independently check SU2 spins, center parity, Wigner–Eckart triangle, ranks and even/odd D, and distinguish necessary selection rules from sufficient physical coupling. Consider possible spinorial/higher-rank spurions and physical locality. Check consistency with the no-common-finite-boost result and free-radius normalization.

**NEXT:** construct a **specific physical intersector operator** invariant under whichever common local/internal symmetry is actually established; derive its rank and reduced matrix element, enforce Hermiticity and charge/gauge conservation, and compute action-derived coupling. If no such operator can be justified, the continuous quarter-H² field remains additional chosen matter rather than derived gravity. The first fully covariant coupled σ/F/Weyl backreaction remains an independent unfinished gate.
