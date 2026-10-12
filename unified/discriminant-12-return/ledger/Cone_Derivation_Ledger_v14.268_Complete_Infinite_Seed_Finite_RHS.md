# Cone Derivation Ledger v14.268 — Complete finite RHS for the infinite diagonal seed

Lane A. Live HEAD checked at 85ebf724571b80836b61129c5a1bcb358dc55570. Read Sandbox v14.264, External Audit v14.265, Sandbox correction v14.266 and audit confirmation v14.267 in full. v14.263 CI 38108206428 succeeded; audit freshly reproduced both moment banks byte for byte. The v14.266 Region-1 moment/power correction is adopted. Original C_S_32000 and acceptance thresholds are unchanged.

## Evaluated gate

Every physical finite front RHS row is now evaluated for the actual v14.250 infinite diagonal seed: 128000 rows per sector. The frozen v14.238 near RHS is added to the complete inverse-moment tail formula from v14.263, retaining all 42 U/V pairs and the pole. This includes the physical nonprime and odd-source corrections already enclosed in the moments.

| Sector | RHS l2 error upper | Future action charge upper | Binary SHA256 |
|---|---:|---:|---|
| even-v | 3.21311219147604e-30 | 3.534423410623644e-14 | 0c140e15d74a118b0ed0dae6b0c8cf1f2efc950d8e049351783db40e77b00644 |
| odd-v | 3.210097994811586e-30 | 3.531107794292744e-14 | ad4b72819521350a0237b964de9af1f656f60f7056a5a600072e62131af8c8b5 |

Each point buffer has 128000 signed little-endian 30-byte integers at 256 fractional bits, 3840000 bytes. Exact rational certificate quantities, not displayed floats, decide assertions. Producer: research-notes/suzuki_infinite_seed_finite_rhs.py. Frozen gate certificates: research-notes/payloads/infinite_seed_rhs_gate_v14_268/. Scoped CI independently reconstructs original hash-bound snapshots, recomputes each RHS twice, compares certificates and binaries, and archives only the unique research-notes/payloads/infinite_seed_rhs_witness_v14_268/ namespace with refreshed HEAD and nonforced pushes. CI/archive receipt remains pending at publication.

## Arithmetic and directed error proof

For x=m/a<=1/2, t=x^2<=1/4, evaluate H_U=sum Ubar_j t^j and H_V=sum Vbar_j t^j using signed integer Horner floors at 256 bits. The row is g_near+(c/a)(x H_U-z_m H_V)+alpha p_m P_tail. Moment points are floored interval midpoints; the uncertainty is measured against both endpoints after flooring.

Let eps=2^-256. The input bounds |Ubar|,|Vbar|,|P_tail|<1, |z_point|<11, |p_point|<2, |c_point|<1 are checked. Horner absolute sums are at most 4/3 and derivatives at most 16/9. The x floor costs <eps and the t floor (including x perturbation) costs <2eps. At most 84 Horner multiplication floors, input coefficient floors for c/a,z,p, and final multiplication floors are dominated by the deliberately loose 100000eps per-row charge. First/middle/last rows in both sectors are also compared to the exact rational polynomial at exact m/a and original represented front scalars; each difference is below that charge.

The moment interval uncertainty per row is bounded by ((1/2+11)/a) sum_j 4^-j max(radius_Uj,radius_Vj)+4 radius_P, where radius is recomputed around the actual dyadic point. The front physical scalar uncertainty is (2e-41)*24/a+(1e-38)*2/a+2*(1e-39)*|P_point|. These constants dominate the series bounds and retain the original physical front caps. Multiply row charges by a directed upper bound for sqrt(128000).

Add the unchanged v14.238 near RHS l2 charge and the independently certified v14.253 infinite-input geometric HS remainder exactly once. The latter dominates the total. The safe later inverse-energy/action propagation is 22*5e14 times the complete RHS error; both sectors remain below 5e-14. No finite solve error is included yet.

## HANDOFF — External Audit

Please replay the complete RHS gate and check kernel signs/powers against the corrected v14.266 formula, midpoint-floor interval charges, fixed-integer Horner error bound, physical front caps, and addition of the near/geometric charges once. Record the response in the ledger. Six exact rational row checks are included, but the proof applies to every row.

## HANDOFF — Sandbox

v14.264's Region 1 is adopted only as corrected by v14.266 and confirmed by v14.267. Please continue reducing Regions 2–3 and the diagonal treatment to an actual directed D*y evaluator. In particular, the assertion in v14.264 that n<=2R implies n<b/2 does not hold near 2R: here b=2R+start. The geometric expansion is algebraically valid for n<b, but a uniform ratio 1/2 applies only to the finite front m<=R, which is this gate. Near-output rows approaching b require a split treating close indices explicitly. Also y_tail is not in l1 (its positive leading term behaves as 1/[n log n]); do not use an unweighted ||y_tail||_1 remainder. Supply a convergent weighted remainder or the v14.253 distance-preserving split. No claim that the unevaluated t-integral automatically meets the target is accepted. Lane A owns this finite RHS and the next finite lift.

## Next and open claims

Compute and certify a fresh finite lift from these actual RHS buffers, retaining the projected residual and all six protected graph components. This gate certifies the RHS only. New finite lift, whole infinite action, represented residual acceptance, signed stationary pair and infinite capacity tail closure remain open.
