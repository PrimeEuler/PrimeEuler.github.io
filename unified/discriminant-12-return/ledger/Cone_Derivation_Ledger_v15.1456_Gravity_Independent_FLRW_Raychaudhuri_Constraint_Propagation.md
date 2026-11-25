# Cone Derivation Ledger v15.1456 — Independent Einstein acceleration evolution preserves the FLRW constraint with nonlinear H² sigma fields

**Date:** 2026-11-25 Eastern. **Gravity/Cone.** **Status:** [N PASS, independent evolution] Einstein homogeneous Raychaudhuri/acceleration and curved-target H² sigma Hamilton equations are evolved together **without imposing Friedmann algebraically during integration**; the independent Friedmann constraint remains preserved to ~2.5e−12 relative, confirming v15.1454's exact stiff-fluid benchmark; [NEGATIVE] no inhomogeneous fully dynamical 3+1 ADM/BSSN evolution yet, no Maxwell/Weyl interaction, no quarter-grid selection of G. Additive, parent v15.1454–1455, verified actual local reproducer and separately committed equivalent source.

## Gate 1381 — independent Einstein equation as constraint-preserving dynamics

Use spatially flat homogeneous 3+1 FLRW metric with scale factor a(t), homogeneous real curved H² sigma target `G_AB=δ_AB−φ_Aφ_B/(1+φ²)`, canonical momenta per comoving volume p_A and `C=p²+(φ·p)²`. With sigma scale f=1, density and pressure equal: `ρ=p=C/(2a^6)`. Unlike the previous v15.1454 code, which computed H from the Friedmann equation at each RHS evaluation, evolve `H=dot a/a` as an **independent state variable** using Raychaudhuri:

`dot a=aH,quad dot H=−(κ/2)(ρ+p)=−κρ`,

with `dot φ^A=(p_A+φ^A(φ·p))/a³` and `dot p_A=−(φ·p)p_A/a³`. Initial values (a(0)=1), `φ=(.15,−.08)`, `p=(.12,.07)`, and `H(0)=sqrt(κρ(0)/3)` satisfy Friedmann only **on the initial slice**. Thereafter no algebraic Friedmann enforcement occurs.

The independent constraint monitor is `F(t)=3H(t)²−κρ(t)`. Analytically `dot F=6H dot H−κ dotρ=−6κHρ+6κHρ=0`, because sigma energy obeys `dotρ+6Hρ=0`. Thus exact ODE solutions preserve F=0; numerical integration should do so approximately. Independently compare a³ with the exact closed form `a³=1+sqrt(3κC0/2)t` and C with C0.

## Actual independent numerical test

Actually executed local Python `/mnt/data/cone_gate/h2_flrw_independent_einstein_v15_1456.py`, SciPy DOP853 rtol 1e−12 atol 2e−14, 241 time samples on [0,120], two values κ:

| κ | final a | max |F|/(κρ0) | max relative a³ error | max relative sigma C drift |
|---:|---:|---:|---:|---:|
| .003 | 1.2851901226207212 | 2.44885e−12 | 9.10033e−15 | 2.78572e−12 |
| .0015 | 1.2150682167552505 | 2.11051e−12 | 3.58952e−14 | 3.18396e−12 |

The independently evolved Einstein acceleration reproduces the v15.1454 scale-factor law to near numerical rounding and **dynamically propagates the Friedmann constraint**, which was not established by a Friedmann-imposed RHS alone. This is a stronger homogeneous dynamical GR check, but still a special FLRW model, not an evolution of the inhomogeneous exact-constraint data from v15.1453. The background metric has no TT modes and the entire Weyl tensor of FLRW vanishes, so the Weyl–F–H² area operator has no active source in this benchmark. It would be wrong to extrapolate its stable energy/constraint propagation to the nonluminal full-Weyl local characteristic warning v15.1420.

**Reproducer:** additive `research-notes/k4_h2_flrw_independent_raychaudhuri_v15_1456.py`, SHA **3ac73b1751a1ff1c0a849df413c76ae1c105e198**. Equivalent to local tested script, exact committed-byte Audit replay pending. Previous v15.1454 (algebraic Friedmann) and v15.1455 (linear vacuum ADM propagation) retained.

**AUDIT:** independently derive Raychaudhuri sign, homogeneous sigma stress p=ρ and canonical H² target kinetic invariant C, differentiate F=3H²−κρ explicitly to verify constraint propagation, compare with v15.1454 exact a³ solution, and execute exact committed scripts. Do not label homogeneous GR as nonlinear **inhomogeneous** 3D Einstein-sigma simulation or a first principles derivation of G.

**NEXT:** implement a constraint-preserving 3+1 spatially inhomogeneous Einstein–H² evolution on the independently solved v15.1453 initial slice, gauge/constraint check at every time and convergence under filtering/dealiasing. Only then attempt full Weyl–F–H² interaction metric stress/EFT order reduction and all-field energy exchange. A second high-priority structural gate is whether the chosen curvature–Maxwell–area operator is redundant in the matched enlarged EFT. The quarter-grid 1/16 shell and 3:1 null-affine ratio remain geometric, not a coupling selector.
