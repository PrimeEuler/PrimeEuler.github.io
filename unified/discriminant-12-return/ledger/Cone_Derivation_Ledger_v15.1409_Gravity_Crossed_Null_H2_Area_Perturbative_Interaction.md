# Cone Derivation Ledger v15.1409 — Two noncollinear null sigma waves give nonzero Weyl–Maxwell area pullback with fifth-order nonlinear target residual

**Date:** 2026-11-24 Eastern. **Gravity/Cone.** **Status:** [EXACT POSITIVE, controlled small amplitudes] separate internal null waves traveling along x and y generate nonzero rank-two spacetime area pullback at order a*b; [EXACT NEGATIVE] unlike the rank-one chiral loop of v15.1408, this simple crossed pair is NOT an exact solution of nonlinear H² sigma equations at finite amplitudes, although its first residual begins at fifth total order a³b² or a²b³; [OPEN] explicit fifth-order correction, full Maxwell/Weyl/EH coupled energy exchange, finite packets, and an action-defined quarter-grid physical parameter. The interaction coefficient and target loop are NOT selected by 1/4. Additive only.

## Gate 1341 — rank-two spacetime area requires independent wave directions

Use H² normalized coordinates `phi=(u,v)`, target metric `G_AB=δ_AB−phi_Aphi_B/(1+u²+v²)`, and nonlinear exact sigma EOM `E_A=Box phi^A−phi^A G_BC ∂phi^B·∂phi^C=0`, as derived v15.1386. In flat (-+++) spacetime let

`u=a sin(t−x), v=b sin(t−y)`,

where a,b are arbitrary small real dimensionless amplitudes and propagation axes x,y differ. Each obeys its *isolated* free wave equation `Box u=Box v=0` exactly. Because their gradients are independent, the spacetime pullback 2-form is **nonzero** at order ab:

`(du∧dv)_tx=+ab cos(t−x)cos(t−y)`,

`(du∧dv)_ty=−ab cos(t−x)cos(t−y)`,

`(du∧dv)_xy=+ab cos(t−x)cos(t−y)`.

The normalized H² area two-form is these components divided by `sqrt(1+a²sin²(t−x)+b²sin²(t−y))`. Thus the previously proposed curvature-dependent Weyl–Maxwell interaction can be activated **if an appropriate nonzero Weyl tidal field is also present**, unlike the exact chiral but rank-one example v15.1408. Nonzero B alone is not proof that its Weyl contraction, emitted photon channel, or observed signal is nonzero in *every* gravitational geometry; phase matching and curvature tensor orientations still matter.

## Gate 1342 — exact residual and controlled leading-order consistency

The two separated null wave gradients each have zero norm, but their cross inner product is nonzero. The nonlinear target EOM residuals simplify EXACTLY to

`E_u=−2a³b² sin²(t−x)sin(t−y)cos(t−x)cos(t−y)/(1+a²sin²(t−x)+b²sin²(t−y))`,

`E_v=−2a²b³ sin(t−x)sin²(t−y)cos(t−x)cos(t−y)/(1+a²sin²(t−x)+b²sin²(t−y))`.

Therefore every Taylor coefficient of total amplitude degree <=4 vanishes, and the first nonlinear coupling error appears at **total degree five**. This is a precise perturbative justification for using two leading-order free waves when computing the earlier **order-ab** area source; it is NOT a license to call the full crossed-wave pair exactly on shell or to neglect its separate gravitational stress. An actual higher-order solution must add corrections that solve the corresponding inhomogeneous wave equation at fifth order, with specified initial/boundary conditions.

**Actually executed source:** `/mnt/data/cone_gate/k4_crossed_h2_null_waves_v15_1409.py` (SymPy exact E_u,E_v and Btx/Bty/Bxy, all derivatives through total degree four zero, PASS). Additive GitHub equivalent `research-notes/k4_crossed_h2_null_waves_v15_1409.py`, commit SHA **c888a320ad355c901327a075c8536c167fb723a5**, pending exact committed-byte independent Audit replay.

## Gate 1343 — physical interaction selection verdict and next tests

The series now distinguishes three physically different claims:

1. **Intrinsic hyperbolic holonomy:** canonical Levi-Civita transport of an auxiliary tangent vector around a specified target loop; at chosen χ=ln2, angle ±π/2 (v15.1407).
2. **Exactly-on-shell chiral internal loop:** closed target-space circle with that holonomy, but **zero** spacetime pullback B and hence **zero** Weyl–EM area interaction (v15.1408).
3. **Perturbatively-on-shell crossed sigma waves:** nonzero rank-two B and potential Weyl–EM interaction, but nonlinear EOM corrections begin at fifth order (this gate). No closed χ=ln2 loop, target holonomy selection, or measured EM output is entailed.

The geometric 3:1 null-affine spacing of the nested EM/q2/null levels and the ln2 matched-U sheet rapidity offset remain exact but do NOT furnish the physical intersector mixing action. The first-order null-Q toy transport of v15.1406 explicitly showed that conservation of total probability does not select transition probability 3:1, and its naive scalar intersector connection is forbidden by the actual finite EM/q2 common-SU2 Casimir gap `3D²/4`.

**AUDIT HANDOFF:** independently replay exact GitHub v15.1406–1409 programs and verify symplectic action, flat unitary null connection, SU2 no-intertwiner gap, intrinsic H² curvature/holonomy, rank-one chiral sigma EOM and B=0, crossed wave B component signs and precise fifth-order residuals. Record all corrections additively and flag any mismatch between the local and newly authored GitHub source bytes.

**NEXT:** calculate explicit O(a³b²) and O(a²b³) corrections to nonlinear crossed-sigma wave equations with retarded data, then integrate the Weyl area source in a known physical tidal background; derive a physical loop/transport constraint from the action rather than impose χ=ln2; finally compare any detector output against the identical enlarged EFT, noting that the q2 radius and coupling remain freely reparameterizable. No G-free new gravitational constant or quarter-grid-selected force has yet emerged.
