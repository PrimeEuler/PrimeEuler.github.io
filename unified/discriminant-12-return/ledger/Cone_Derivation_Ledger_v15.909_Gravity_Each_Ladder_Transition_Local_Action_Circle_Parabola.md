# Cone Derivation Ledger v15.909 — Every fixed-sum ladder station has a distinct product-shell action circle and local parabola

**Date:** 2026-11-13 US Eastern. **Gravity lane.** Parents: v14.550 diameter–secant machine, v15.895–897 two-circle and parabola analysis, v15.906–908 Schwinger ladder and physical EM/tidal comparator. **Live master HEAD checked immediately before ledger write:** eaebe9965927fc2a5b6b47dd2e6b541f66a51e6e. Target path checked absent; additive-only, no certified, Suzuki, Sandbox or Audit edits.

**Owner correction:** Every transition on the shared outer action circle is itself associated with a distinct action circle and acceleration parabola. Do not keep only one sqrt(n) inner circle for an entire n+k ladder.

**Status:** [D] exact fixed-sum/varying-product circle bundle; exact per-product rest-circle/hyperbola contact and row-parabola crossing; [N] no field-derived acceleration/frequency from these local geometric parabolas.

## Gate 605 — fixed sum, changing product: a circle at each transition

For any factor pair n,k>=1 and sector factor u>0, original Cone coordinates are X=u(n−k)/2, Y=u sqrt(nk), T=u(n+k)/2. A fixed Schwinger shell conserves D=n+k, so the **outer** action circle has common radius R_o=uD/2 and the ladder step J_+ maps (n,k)→(n+1,k−1), preserving D. However each visited state has a different product P_k=nk and hence a **distinct associated rest action-circle scale**

**R_k=u sqrt(nk)**.

Every positive-product P_k has an auxiliary hyperbolic shell T²−X²=u² P_k and its own rest circle X²+T²=u² P_k in the (X,T) projection, tangent at X=0, T=R_k. The rest circle at each rung is NOT the same geometrical circle as the outer fixed-T circle in (X,Y), even though the factors and amplitude map one station to the other.

For k>=1, a separate **factor-row parabola** is Y²=u² k²+2u k X, and it crosses the common outer circle at X=u(n−k)/2,Y=u sqrt(nk). Different k means different factor-row parabola; the specific k=1 row from v15.895–897 is only the terminal positive-product row.

## Gate 606 — distinct osculating quadratics and curvature

Near each rest station X=0 in (X,T), the local hyperbola and local rest circle expand:

T_shell(X)=R_k+X²/(2R_k)−X⁴/(8R_k³)+...,

T_local_circle(X)=R_k−X²/(2R_k)−X⁴/(8R_k³)+...,

so their separation is **X²/R_k+O(X^6)**. Their local parabola coefficients depend on k through 1/R_k=1/[u sqrt(nk)]. For comparison the fixed outer circle's curvature is **1/R_o=2/(uD)**, independent of k; its osculating parabola in a tangent/normal frame has the same curvature at all rungs. The per-station curvature ratio is **R_o/R_k=D/(2sqrt(nk))**. Treat these separate projections and tangent-frame expansions distinctly; don't mistake the local-circle osculating parabola for the outer circle's own curvature or for the physical radial-time acceleration parabola of v15.900.

At each discrete J_+ transition the product changes by **P_next−P=k−n−1**, and the radius changes nonlinearly from u sqrt(nk) to u sqrt[(n+1)(k−1)]. On the n>=k branch this decreases as the ladder approaches the right endpoint. The endpoint k=0 has R_k=0; a nondegenerate local rest circle/hyperbola and curvature 1/R_k no longer exist there. At the central n=k seat, R_k=R_o and the associated circle radii agree numerically, but their coordinate projections remain distinct.

Example D=5: (3,2)→(4,1)→(5,0) has local radii u sqrt6, 2u, 0 respectively, all with the same outer radius (5/2)u. The J_+ amplitudes on the first two arrows equal sqrt6 and 2 respectively. In fact **R_k/u** equals the normalized matrix element <n,k−1|J_+|n−1,k>, so every transition has an exactly matched local-circle amplitude.

## Gate 607 — force/clock selector remains open

The stationary point in each different hyperbolic product shell is a *geometrical* rest station, not a separately derived mechanically stationary turning point. Even knowing all local curvatures, standard Hamiltonians H=f(J_z,J_-J_+) are diagonal and cannot generate J_+ transitions. The explicit EM and tidal controls v15.908 provide transverse J_y or J_x couplings only once their physical field coefficients and oscillator-coordinate mapping are specified. Thus the cascade of local action-circle/parabola objects fixes a relative geometric/operator pattern, not a new physical acceleration a(t), force, frequency, or Newton G.

One could hypothesize a local oscillator law omega_k²=C/R_k or omega_k²=C/R_k², but both require independent kinetic stiffness C; neither follows from tangency or Schwinger algebra. Distinguish ladder operator *amplitude* sqrt(nk) from a temporal step rate and from the outer ratio D/(n−k).

**Reproducer:** research-notes/k4_nested_transition_action_circles_v15_909.py, commit eaebe9965927fc2a5b6b47dd2e6b541f66a51e6e. Exact SymPy checks: fixed-D boundary, product-shell tangency curvature, row parabola station, discrete product shift and variable local/outer curvature; explicit D=2..9 ladder tables. Independent Audit pending.

**Next:** test a physically motivated network of linked local circle responses under a single externally normalized EM/tidal interaction, with complete two-neighbor J_± structure, and ask whether measured phase/transition ratios depend on product-shell curvature after standard SU(2) effects are divided out. If not, record a negative Cone-specific selector. Audit/Muse: independently verify distinct coordinate planes, local semicircle vs outer station arc, endpoint degeneration, and whether the proposed 'own acceleration parabola' has any actual time parameter in the field equations.
