# Cone Derivation Ledger v15.1402 — Natural EM/q2 state counting does not reproduce hyperboloid annular 3:1

**Date:** 2026-11-24 Eastern. **Track:** Gravity/Cone. **Parent:** v15.1401 nested representation-space observability hyperboloids. **Status:** [EXACT NEGATIVE] the natural finite Hilbert dimension ratio and SU(2) coadjoint-orbit symplectic area do not in general equal the 3:1 fixed-T Euclidean annular shell ratio; [POSITIVE] the orbit area ratio equals 3 **only at D=2**, an isolated coincidence without a derived coupling, and tends to 2 at large D; [OPEN] physical intersector phase-space/canonical measure and action selection. Additive-only.

## Gate 1328 — count the actual states of the genuine finite carriers

For each EM Schwinger shell D>=2, the actual unit-normalized EM SU2 spin is `j_E=(D−1)/2` and its Hilbert dimension is `2j_E+1=D`. The genuine **closed refined q=2** carrier is an ordinary spin `J_q=(2D−1)/2` representation of dimension `2J_q+1=2D`; co-scaling the generators by 1/2 to quarter coordinate units does not double the *physical Hilbert dimension* a second time. Therefore the exact state-count ratio is

`dim(H_q)/dim(H_EM)=2D/D=2`

for **every** D. It is not 3, not 7, and not an automatically chosen ratio of physical electromagnetic versus gravitational excitations.

As a different natural but not identical measure, the SU2 Kirillov–Kostant–Souriau symplectic area of a spin-j coadjoint orbit with standard SU2 generator normalization is `4πj`, so the **orbit symplectic area ratio** is

`A_q/A_EM = J_q/j_E=(2D−1)/(D−1)=2+1/(D−1)`.

It is 3 at D=2, 5/2 at D=3, 7/3 at D=4, and approaches 2 for large D. The D=2 value 3 is **not** a universal agreement with v15.1401's continuum annulus ratio; it reflects one special finite representation. Quantized state counts include the familiar orbit/half-form offset and remain a different notion from raw classical orbit area. For an arbitrary physical coadjoint-orbit normalization, use a consistently matched normalization in both sectors; the ratio above relies on the ordinary closed physical SU2 representation, not the formal geometric quarter-Casimir.

## Gate 1329 — what would make the geometric volume physically consequential?

The 3:1 ratio of v15.1401 uses the flat Euclidean `dX dY` measure on a fixed ambient representation-time plane. The orbit symplectic measure and finite Hilbert-state counting arise from distinct representations and invariant phase-space structures. There is **no established canonical unitary map** between the fixed-T annular region and those finite Hilbert spaces, especially after the v15.1393 finite unitary SO+(2,1) boost obstruction. Thus an assertion that shell volume itself counts photons/gravitational states or fixes the physical Weyl-H² mixing coefficient would insert a missing measure and dynamics by hand.

**Actually executed local SymPy source:** `/mnt/data/cone_gate/k4_quarter_orbit_count_vs_shell_volume_v15_1402.py`, PASS state dimensions, orbit formula and D=2,3,4,5,10,100 examples. **Additive GitHub reproducer:** `research-notes/k4_quarter_orbit_count_vs_shell_volume_v15_1402.py`, commit **fdec8966d220f641442b7efaed8e3039aed363dd**; exact committed-byte external Audit replay pending.

**AUDIT HANDOFF:** check physical closed q2 spin against formal quarter Casimir and any co-scaling normalization, standard SU2 KKS symplectic area 4πj and state dimension 2j+1, dimensional ratios, and separation of this canonical measure from v15.1401's fixed-time annular geometry and Lorentzian 7:1 regulated-volume comparison.

**NEXT:** seek action-derived symplectic/observability flux whose canonical measure is forced to traverse the nested EM/q2/null levels, rather than *choose* an annular area or rapidity cutoff; test independent physical intersector matrix elements constrained by v15.1397 and the exact quarter-radius/free-coupling degeneracy of v15.1398. If the proposed flux is not fixed by existing K4/EH/Maxwell constraints, keep 3:1 as a mathematically striking but unselected correspondence.
