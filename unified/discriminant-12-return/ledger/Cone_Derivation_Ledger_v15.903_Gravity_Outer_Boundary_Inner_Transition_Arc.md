# Cone Derivation Ledger v15.903 — Outer n+1 boundary versus inner sqrt(n) first-transition arc

**Date:** 2026-11-13 US Eastern. **Gravity lane.** Parents: v13.177 diameter/parabola circle, v15.867/869 nodes and transition parabola, Gravity v15.895–902 two-circle shell geometry and phase-station proposal. **Master HEAD checked immediately before ledger write:** 6e4dcc651da54df0be53c83a2b4b4aab882d110f. Target checked absent. Additive only; no changes to prior certified/Audit/Sandbox/Suzuki artifacts.

**Owner clarification:** Read **n+1 as the outer action circle's geometric diameter/boundary**, *not* as an independently justified number of uniformly spaced phase stations. Read **pi sqrt(n)** as the arc used to identify the first sign-changing half-cycle transition along nodes. Earlier v15.901/902 N=n+1 node assumptions are therefore hypothetical alternatives, not faithful statements of this latest clarified claim.

## Gate 584 — distinguish the three candidate arcs

At factor-grid unit u>0 and n>=1, the outer circle in the (X,Y) section has radius R_o=u(n+1)/2 and its chord half-height is R_i=u sqrt(n), at X=u(n−1)/2. The *inner* circle's half-circumference is **S_inner_half=pi u sqrt(n)**, with angular phase pi for a one-winding mode on that inner circle.

The minor OUTER circle arc between its two chord endpoints, passing through its rightmost point, has exact length

**S_outer_chord = 2 R_o asin(R_i/R_o) = u(n+1) asin[2sqrt(n)/(n+1)] = 2u(n+1) atan(1/sqrt(n))**.

For n=1, both are pi u. For n>1, the inner semicircular arc is strictly larger than the minor outer chord arc: since the inner radius is the chord half-height, the outer circular path is flatter. Do not substitute S_inner_half for this geometric outer-boundary arc. For n=4, S_outer_chord/u≈4.63647609 versus S_inner_half/u=2pi≈6.28318531.

If the proposal instead means **a prescribed outer-boundary arc having LENGTH pi u sqrt(n)**, its central angle must be **Delta theta_outer = S_inner_half/R_o = 2pi sqrt(n)/(n+1) = pi/gamma_n**, where gamma_n=(n+1)/(2sqrt(n)). That angle differs from both the inner half-turn pi and the geometric chord-endpoint angle **2 asin[2sqrt(n)/(n+1)]**. Such an arc length can be selected on the outer boundary, but its endpoints are not forced to coincide with the chord endpoints. This clarifies all three interpretations without assuming any outer node count.

## Gate 585 — simple periodic standing-wave closure gives an exact negative test

If a one-dimensional, uniformly propagated real standing wave sin(m theta) on the OUTER circle is assigned adjacent zero-node arc spacing S_inner_half, the allowed integer azimuthal wave number must satisfy

**m = circumference_outer/(2 S_inner_half) = (n+1)/(2sqrt(n))=gamma_n**.

For positive integer n, m can be an integer **only when n=1**: an integer m requires sqrt(n) rational, hence sqrt(n)=k integer; k²+1=2mk implies k divides 1, so k=1. Thus for n=2,4,9,16, the candidate outer modes are noninteger gamma=1.06066,1.25,1.66667,2.125. The proposed pi sqrt(n) spacing therefore **cannot be the uniform spacing between consecutive zeros of a single-valued standard sine eigenmode wrapping the entire outer circle**, except n=1. This negative statement holds ONLY for that explicit uniform periodic mode model; it does not rule out a nonuniform phase map, only a half-boundary traversal, coupled sheets/coverings, nodes on the separate inner circle, or more general field boundary conditions.

## Gate 586 — action/phase and dimensional scope

A half turn is pi *radians* on a normalized circular phase coordinate; pi sqrt(n) is an arc length in factor-grid units, not an angular phase unless the arc-coordinate normalization is separately defined. The n+1 diameter geometrically fixes R_o but does not specify N=n+1 nodes. Similarly the sqrt(n) circle and n+1 circle live originally in different Cone sections; mapping their arcs physically requires a justified correspondence. Geometry alone selects neither wave propagation speed nor a temporal frequency in Hz, acceleration, orbital force, Newton's G or a Compton clock.

**Reproducer:** `unified/discriminant-12-return/research-notes/k4_outer_boundary_inner_arc_v15_903.py`, commit 6e4dcc651da54df0be53c83a2b4b4aab882d110f. Exact symbolic checks and numerical n-samples confirm circle/chord, arcs, assigned outer angle and integer-wave-mode obstruction. Independent Audit pending.

**Next:** recover from the Cone's actual boundary and action operator the physical meaning of the owner's n+1 boundary and pi sqrt(n) transition arc; test nonuniform phase transport or a two-section boundary condition rather than importing an N=n+1 count. Keep the outer acceleration parabola explicitly present, and require dynamics for any transition rate. Audit/Muse: examine the arc distinction, single-valuedness proof, and competing phase conventions.
