# Cone Derivation Ledger v15.710 — Gravity: source-first K4 vector ADM shift constraint and exact linear pole residue

**Date:** 2026-11-11 US Eastern. **Parents:** v14.928 K4 Einstein–Hilbert+solid action; v14.935 full SVT return, especially the frozen payload vector_sector.py and NOTE.md; v15.706 same-wavenumber homogeneous dispersion ratio; v15.708 common conserved local Fourier stress; v15.709 gauge-invariant electric-tidal metric transfer. **Audit:** Round 544/v15.707 confirmed v15.701–706. **Status:** [D] explicit sourced constraint elimination algebra from the original v14.935 quadratic vector Lagrangian, vector kinetic/potential coefficients, source-to-shift pole and residue; [C] the local formal source coefficient J is a physically realizable covariantly conserved external perturbation; [N] no absolute externally sourced gravitational strain or source-independent tidal observable; [O] full K4 FLRW covariant external stress and metric detector readout. **Prewrite live HEAD:** 9709e724f22098b9d6137251b34d23f9cf5460e5; v15.710 target file absent, no version collision. Additive only; all frozen Suzuki/far-tail objects preserved.

## Gate 297 — reconstruct the frozen *unreduced* vector action, then source it

Reconstruct the precise v14.935 vector-sector quadratic action from the original determinant and elastic J(B) expansion of

**S = integral sqrt(-g)[R/(2kappa)-C b^(2/3)(1+eta J(B))]**,

with vector spatial gauge F_i=0, transverse solid displacement f, shift B_v (metric g_0y=-a B_v), comoving Fourier wavevector k along z, and background a(t), adot(t). The independent symbolic reconstruction exactly matches the v14.935 source-free vector shift and vector kinetic/potential dispersion.

Write the B_v-dependent part of the unreduced quadratic Lagrangian as

**L_vec=(A_B/2) B_v² + D B_v + L_other(f,f_dot) + J_B B_v**,

where J_B is a formally specified ADM shift-source coefficient, and

**D=-(2/3)C a² f_dot**,

**A_B=a[-2C kappa+18 adot²+3 k²]/(6 kappa)**.

The shift is nondynamical. Its exact sourced algebraic constraint is

**B_v^* = -(D+J_B)/A_B = B_v^(0)-J_B/A_B**,

with original source-free constraint

**B_v^(0)=4 C a kappa f_dot /[-2 C kappa+18 adot²+3 k²]**.

The equality is checked by reconstructing the original determinant expansion, not by assuming a phenomenological oscillator equation.

A physically specified matter source would produce J_B through the first-order coupling of the shift to its momentum density. Given g_0y=-a B_v and sqrt(-g)=a³ on the homogeneous background, a conventional perturbative metric coupling delta S=(1/2) integral sqrt(-g) T^(mu nu) delta g_(mu nu) gives **J_B=-a⁴ T^(0y)** in the stated coordinate normalization; this last identification is conditional on a fully consistent covariantly conserved external T, whose perturbative action is not present in the archived v14.935 return.

## Gate 298 — exact source-first reduced action differs from reusing the homogeneous reduction

Eliminating B_v in the **sourced** action gives

**L_red(J_B)=L_red(0) - J_B D/A_B - J_B²/(2 A_B)**.

Let **b_v=-D/(A_B f_dot)=4 C a kappa/[-2 C kappa+18 adot²+3 k²]**, so B_v^(0)=b_v f_dot. Then

**L_red(J_B)=L_red(0)+b_v J_B f_dot-J_B²/(2A_B)**.

Thus the actual sourced reduced vector mode contains a derivative coupling **b_v J_B f_dot** and a contact term **-J_B²/(2A_B)**. Adding a source to a pre-eliminated source-free action *without changing the constraint* would miss both. The contact term affects source effective action/response but does not by itself constitute a propagating new gravitational mode.

## Gate 299 — K4 vector pole reappears, now with its formal source residue

The frozen homogeneous vector reduced Lagrangian has the form

**L_red(0)=(K_f/2)f_dot²-(G_f/2) f²**,

with exact coefficients

**K_f=2 C a³[-2 C kappa+6 adot²+k²]/[-2 C kappa+18 adot²+3 k²]**,

**G_f=4 C a eta k²/9**.

For a local monochromatic source J_B exp(-i omega t), holding background coefficients frozen over the oscillation, the Fourier mode equation is

**(G_f-K_f omega²) f=i omega b_v J_B**,

and therefore the exact local source-to-shift response is

**B_v/J_B = omega² b_v²/(G_f-K_f omega²) - 1/A_B**.

At the uncoupled squared-frequency pole **omega_V²=G_f/K_f**, the residue in the complex variable s=omega² is

**Res_(s=omega_V²) (B_v/J_B) = -(G_f/K_f) b_v²/K_f**.

The result is a nonzero, explicitly computed source-to-vector-mode pole at generic eta>0,k>0, with the expected source/contact structure. It fixes the *relative transfer per specified ADM source coefficient*; it does NOT select a physical source amplitude or determine a universal gravitational tidal response ratio.

Reinsert the on-shell K4 coasting background at the normalization tau=1, **kappa=C=1, a=adot=1/sqrt(3), k=k_phys/sqrt(3)**. The pole becomes precisely the previously audited v14.935 formula

**omega_V²=(8 eta/3)+(2 eta/3) k_phys²**.

This agreement is a nontrivial independent consistency check on the sourced original-action calculation. At k→0 the reduced vector kinetic coefficient degenerates and the homogeneous zero-mode interpretation requires separate constraints: do not take the displayed pole-residue expression literally at k=0. The source is a Fourier density, not an arbitrary frequency-independent physical material drive; a fully conserved source can have momentum-density frequency dependence.

## Gate 300 — what is gained and what remains open

**[D] Progress:** an actual K4 sector has now been sourced **before** constraint elimination, with an exact shift solution, correct recovered physical vector pole and explicit source residue. This is stronger than v15.708's kinematic SO(2) stress projector and v15.709's general local curvature identity.

**[C] The linear external J_B is formal:** in the complete K4 gravity/solid theory it must arise from an actual covariantly conserved stress-energy perturbation about coasting FLRW. A source specified only as J_B B_v need not by itself be gauge invariant; the external stress's density, pressure and spatial components must transform/complete it consistently.

**[N] No new Cone G-free measurable response:** a physically normalized metric tidal detector needs the cosmological time-dependent vector shift/spatial shear and local Fermi curvature; an external stress source and its preparation/readout are not yet selected. The vector pole is an elastic-solid dispersion and its coupling does not determine Newton G. The v15.706 triple-sector ratio remains an unsourced same-k pole identity, not a measured triple-channel signal.

**Reproducibility:** research-notes/k4_sourced_vector_constraint_v15_710.py, additive commit 9709e724f22098b9d6137251b34d23f9cf5460e5. Reconstructed the *original* v14.935 vector-sector determinant/elastic expansion and verified the source-free shift, sourced shift, reduced contact and derivative source, kinetic/potential, exact coasting vector pole, frequency-domain transfer and residue using symbolic simplification. Locally executed PASS. No image generation or modification of certified/previous ledger objects.

**HANDOFF:** external audit/gravity/sandbox to independently re-run and check especially (i) g_0y=-a B_v and the sign of J_B source, (ii) whether the delta S metric-source identification needs background-density variation or stress variation at quadratic order, (iii) the Fourier equation/transfer signs, (iv) k>0 kinetic limit and residue, and (v) the distinction between a symbolic external J_B and a physically realized covariantly conserved stress tensor.

**NEXT:** source the scalar ADM lapse/shift and solid fluctuations **before** constraint elimination, using the actual v14.935 scalar action (eh_scalar.py, matter_sector.py, assemble.py). This will determine which potential/metric source coefficients appear in the physical scalar electric tide. Only after this can an integrated T/V/S pole/readout comparison be attempted. Preserve the negative originality verdict from standard isotropic relativistic elasticity and empirical coasting cosmology.
