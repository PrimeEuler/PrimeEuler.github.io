# Cone Derivation Ledger v15.1380 — First explicit quarter-hyperboloid-invariant electromagnetic interaction and no-scale selector

**Date:** 2026-11-24 US Eastern. **Track:** Gravity/Cone. **Previous thread:** v15.1183–1185 closed refined q=2 hyperboloid, v15.1178 Casimir-free tidal readout, v15.989 quarter kinetic anisotropy, v15.1353 full first-order Einstein closure and v15.1355/1377 optical probe. **Status:** [C] constructive generally covariant U(1)-gauge-invariant SO+(2,1)-target-isometry-invariant Maxwell coupling to an independent two-field map into the H² quarter hyperboloid; [D/PASS] exact target geometry, area pullback, induced conserved electromagnetic current and explicit nonzero example; [NEGATIVE] area exactness/field-redefinition obstruction, free coupling, radius normalization cancels, no original Maxwell+K4 source can activate it without new H² fields; [OPEN] independent sourced gravitational kinetic/action sector, detector and continuum, matched EFT comparator. Strict additive; historic frozen code untouched.

## Gate 1286 — specify the physical target, not only its formal Casimir

Use the positive sheet of a **candidate closed refined-step** geometric carrier, `H²_r: T²−X²−Y²=r²`, where `r=1/4` (thus **Q=r²=1/16**, not a physically established gravitational Casimir; original unit quarter-grid operator has different, possibly state-dependent levels). Let a new independent spacetime field `n(x)=(T,X,Y)=r(sqrt(1+u²+v²),u,v)`. The pullback of the induced Riemannian target metric has determinant `det G=r⁴/(1+u²+v²)`. Its normalized invariant oriented area two-form is

`B_{mu nu}=(partial_mu u partial_nu v−partial_nu u partial_mu v)/sqrt(1+u²+v²)`.

This is the pullback of the target volume form divided by r². It is antisymmetric under spacetime indices, U(1)-neutral, invariant under **orientation-preserving** SO+(2,1) target isometries, closed as a two-form, and vanishes when only one independent target coordinate moves. This construction **assumes a continuous sigma field** in addition to the frozen Einstein–Maxwell+K4 content. The archived v15.1185 proves no nontrivial common boost preserves every member of the finite quarter grid; thus finite exact quarter-lattice preservation and full continuous SO+(2,1) covariance cannot simultaneously be asserted from those frozen finite-shell nodes. This is a continuous completion hypothesis, not an established physical fourth-grid field.

## Gate 1287 — a legitimate, testable interaction exists, but its coefficient is free

Consider `S_H=−f²/2∫ sqrt(−g) G_norm,AB(u,v) ∇mu phi^A ∇^mu phi^B` where `G_norm` is the positive unit-radius H² metric, plus standard Maxwell `−F_mu nu F^mu nu/4`, plus

`L_int=−lambda F^{mu nu} B_mu nu/2`.

Here `f` is an independent scale needed for properly normalized dynamical target fields and `lambda` is an independent dimensionless EFT coefficient (since u,v are dimensionless, B has mass dimension 2). The construction is gauge invariant because it depends only on F and the target area form, and generally covariant when all spacetime indices use the physical metric. Variation of the Maxwell field gives

`nabla_mu(F^{mu nu}+lambda B^{mu nu})=J_ext^nu`,

or equivalently induced quarter-sector current `J_H^nu=−lambda nabla_mu B^{mu nu}`, which satisfies **exact conservation** because B is antisymmetric and the double covariant divergence of an antisymmetric two-form is zero. It represents a *real source term if a dynamic/prepared H² map is present*, not a new current arising automatically from existing K4 gravitational stress.

Direct example in flat local spacetime: `u=a sin(kx)`, `v=b sin(qy)`. Then `B_xy=ab kq cos(kx)cos(qy)/sqrt(1+a²sin²kx+b²sin²qy)`. This yields a nonzero conserved effective transverse current `J^x=lambda ∂y B_xy`, `J^y=−lambda ∂x B_xy`. At small amplitude, `J^x=−lambda ab k q² cos(kx)sin(qy)+O(a³b,ab³)`, `J^y=+lambda ab k²q sin(kx)cos(qy)+O(a³b,ab³)`, and `∂x Jx+∂y Jy=0`. The chosen static internal map is a **specified/externally prepared field configuration**, not yet an on-shell solution of the dynamical sigma model; generating/protecting it costs energy and requires boundary/initial data. It is a real off-shell source example only.

## Gate 1288 — exact no-go for naive uniqueness

The target `H²` is topologically an open plane and has no nontrivial compact two-cycle. Its normalized area form is **globally exact**. A regular primitive is

`C=[u dv−v du]/[1+sqrt(1+u²+v²)]`, hence `B=dC`.

So the simple Maxwell coupling obeys the exact quadratic-completion identity

`−F²/4−lambda F·B/2=−(F+lambda B)²/4+lambda² B²/4`.

In the source-free electromagnetic sector, the local gauge-potential redefinition `A_new=A+lambda C` removes the *linear mixing* but shifts the target field's higher-derivative self-action. If electrical charges couple to the original A, the redefinition transfers a physical interaction to the matter current through C, so it does not prove full physical equivalence to completely uncoupled electromagnetism. It does prove the simple mixing is not a fixed, intrinsically quarter-specific new photon channel. Neither topology nor a flux integral quantizes lambda on the **contractible** H² sheet; the chosen normalized area eliminates the explicit r=1/4 from the interaction altogether. The separate target kinetic scale f likewise remains undetermined. At constant n, the new current vanishes identically, so injecting only the frozen v15.1353 Maxwell packet into an unexcited internal target yields no new linear response. This is a **negative physical selector** even though the interaction is mathematically admissible.

**Executable exact symbolic source:** `research-notes/k4_quarter_hyperboloid_area_maxwell_v15_1380.py`, SHA **28319725c55bd6158cb9f8bb1e1a8f4cf9b446a5**; equivalent local code actually executed PASS positive metric determinant, primitive, quadratic current conservation, small-amplitude coefficients and complete square. Actual local test file `/mnt/data/cone_gate/quarter_hyperboloid_interaction_v15_1380.py`. Exact committed source replay not yet external-Audited.

**Audit:** independently check sigma area form and determinant, primitive and global contractibility, all Maxwell signs, positive-energy sigma kinetic sign under (-+++), current conservation and leading Jx/Jy, free λ and r cancellation, and no finite-grid global boost. Search whether the coupling is a known EFT operator; do not assert its novelty from algebra alone.

**Next gate:** test Weyl-curvature-sensitive `C_{mu nu rho sigma} F^{mu nu} B^{rho sigma}` with fully dynamical H² map, time-dependent source, and an actual detector difference against the identical action without this operator. Quantify whether the curvature contraction is closed or removable by A redefinition. Do not import a new f or lambda and then claim a prediction independent of them.
