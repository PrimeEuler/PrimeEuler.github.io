# Cone Derivation Ledger v15.924 — The n+1 Schwinger transition matrix and hyperbola cuts are the same row parabolas

**Date:** 2026-11-13 US Eastern. **Track:** Gravity/EM geometry. **Parents:** v14.550 diameter/secant and legacy `webgl/index.html`, v15.906–909 and v15.921–923 circle, hyperbola, fixed-k parabola and exact intersections. **Owner correction:** “they are the same parabolas as the ones crossing the n+1 transition matrix.” **Live master HEAD immediately before write:** b5e37f17b6c42c5910c9be5a9435d9914d587e49; target path verified absent. Additive-only; no existing historical script, page, certified, Audit, Sandbox or Suzuki files edited.

**Status:** [D] exact identity of row parabolas on fixed-diameter circle and fixed-product hyperbola; [D] explicit geometry-first construction of every SU(2) J+ matrix entry; [N] independent SymPy D=2..18 commutator and incidence checks; [O] physical cross-principal-energy-shell dipole operator and radiative lifetime bridge.

## Gate 651 — not parallel-looking constructions: the same point

Set sector scale u=1 and outer diameter **D=n+1**. Let **k=1,…,D−1** label one fixed-factor row parabola **P_k: Y²=k²+2kX**. Let the fixed-sum circle be **C_D: X²+Y²=(D/2)²**, and positive-pair hyperbola **H_N: T²−X²=N** with Y²=N.

Intersect P_k with the physically relevant branch of C_D:

**X=D/2−k,  Y²=k(D−k),  T=D/2.**

(The other formal circle intersection at X=−D/2−k lies outside a>0, b>0: it has a<0 and therefore is not a positive factor pair.) The identical row parabola intersects H_N at

**X=(N−k²)/(2k), Y²=N, T=(N+k²)/(2k).**

At **N=k(D−k)**, these are *exactly the same coordinates*. Hence the commuting incidence diagram is

**fixed D=n+1 circle ∩ row P_k = fixed N=k(D−k) hyperbola ∩ row P_k**.

The two cuts are different descriptions of one AM–GM point. They are not two new independent physical constructions.

## Gate 652 — geometry-first matrix entries

The same point has half-chord **Y=sqrt[k(D−k)]**. On the D-dimensional Schwinger shell `|a−1,k>` with a=D−k, define J+ by the row-parabola's coordinate:

**J+ |D−k−1,k> = sqrt[k(D−k)] |D−k,k−1>**.

Thus the fixed `D=n+1` transition matrix draws its coefficients directly from the intersections, instead of a separately postulated matrix subsequently compared to geometric radii. As k runs from D−1 down to 1 the full raising ladder is generated. This is an exact faithful construction of the **standard SU(2)** Schwinger representation and the commutator **[J+,J−]=2J_z** follows with J_z eigenvalues a−(D−1)/2 in the occupation-a basis.

**Important indexing:** one fixed circle D samples many P_k row parabolas; each fixed P_k row passes across the full family of outer circles D>k. They share an incidence lattice rather than requiring one single parabola to produce all D entries. At D=5, k=1,2,3,4 gives square roots **2,√6,√6,2** (in decreasing k row order). The outer endpoint k=0 has zero outgoing J+ coefficient and is excluded from positive-k parabola intersection formula, but its state remains in the full D×D representation.

## Gate 653 — implications and limitations

This resolves a possible false separation in v15.921–923 between the v15.922 hyperbolic intersection parabola family and the v15.906/909 `n+1` transition-matrix parabola family: they are *identical* algebraic curves, sampled at different row and shell constraints. Geometric `sqrt[nk]` amplitudes are not arbitrary weighting factors; the positive-pair incidence assigns them uniquely for the chosen SU(2) ladder. However the operator action **which state is connected to which** is still a separately imposed representation/dynamical structure; equal static row intersections do not force a physical Hamiltonian or clock.

The outer diameter **D=n+1** here is the dimension/occupation shell of the oscillator comparator, not the Bohr energy spacing of the hydrogen `n→n+1` spectral transition. Within one fixed-D isotropic oscillator shell all states have equal unperturbed energy; `J+` does not generate ordinary spontaneous E1 photons. The v15.920 genuine 2p→1s and 3p→1s/2s radiative dipoles are still *cross-principal-shell*, requiring their physical SO(4,2) / KS map, angular selection, normalization and measured ω. The user's exact geometric identification is positive but does not remove that physical distinction.

With original legacy division t, substitute **u=1/t**, **X=u(D/2−k)**, **Y=u sqrt[k(D−k)]**, and hyperbolic product slice **N=u² k(D−k)** to keep coordinates consistent with the old WebGL plotting scale. This is the same normalization caveat from v15.922.

## Gate 654 — reproducibility and next step

**Validated reproducer:** `research-notes/k4_nplusone_parabola_transition_incidence_v15_924_validated.py`, additive commit **b5e37f17b6c42c5910c9be5a9435d9914d587e49**. Symbolic proof of both intersections and simultaneous substitution; exact matrix reconstruction and commutator for D=2..18; explicit D=5 coefficients. Independent local SymPy run passed. An initial exploratory script `.../k4_nplusone_parabola_transition_incidence_v15_924.py` (commit 1633bbfab130a1e481c7e42cc28f0e16ba59b94b) had used an expression as the polynomial unknown when checking the second root; its add-only validated replacement introduces an independent real x variable and confirms the two formal circle roots. The original exploratory file is left intact and must not be used as the passing verification target. Independent Audit pending.

**NEXT:** Encode the union of every fixed-D row-parabola intersection as a weighted bipartite incidence graph between sum shells D and product shells N. Test whether *a uniquely prescribed cross-D operator* comes from a natural incidence shift preserving the KS/SO(4,2) measure; compare its transition selection rules and the three measured lifetime dipole ratios to standard hydrogen. Without that additional physical operator, treat the unified parabola identity as a rigorous geometric representation of SU(2), not a standalone spectroscopic law.
