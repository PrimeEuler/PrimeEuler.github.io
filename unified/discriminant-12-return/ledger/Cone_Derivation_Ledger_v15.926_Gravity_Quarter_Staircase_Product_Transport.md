# Cone Derivation Ledger v15.926 — Exact product transport on the audited unbounded quarter staircase

**Date:** 2026-11-13 US Eastern. **Track:** Gravity/EM geometric comparison. **Parents:** Sandbox v15.140, v15.180; Lane A v15.572–573, v15.602, v15.626–627; Gravity v15.922–925. **Immediately prewrite live HEAD:** 7898a553795bd74c0d2139999e04f280792a653c; this target path confirmed absent. Additive only: no protected Suzuki, Audit, Sandbox, or historical script edits.

**Goal:** Track the hyperbola product `P=ab` through the **already existing** q=2 quarter-grid boundary witness and two natural parity-changing quarter-rung injections. Distinguish source transition weight from target transition weight and do not reinterpret these chosen geometric maps as physical EM/gravity or E1 dynamics.

**Status:** [D] exact product-change formulas, q=2 shell grading, null geometry, boundary destination; [N] exact rational 80-shell test; [O] Hamiltonian, physical phase, radiation operator, selection between candidate quarter shifts.

## Gate 660 — careful transition-centered coordinates

The original step-one upward transition on refined shell `j=L/4` at state `m=-j+i/2` has

**a=j−m=(L−i)/2; b=j+m+1=(i+2)/2; P=ab=(L−i)(i+2)/4; X=(b−a)/2; R=(a+b)/2=j+1/2**.

Thus `P=R²−X²`. It is a **transition-centered** product, not an intrinsic state energy or an automatically conserved particle mass. For a *downward* transition, use the different oriented factorization `P_−=(j+m)(j−m+1)`. At the upper and lower open ends, these respective source outgoing products both equal **c=j+1/4=(L+1)/4**.

## Gate 661 — existing L→L+2 boundary witness sends open product c to outward product zero

The audited v15.602 q=2 witness chooses an upward leg from `m=j−1/2` to upper endpoint `m'=j+1/2` of shell `j'=j+1/2`, and a downward mirror leg to its lower endpoint `m'=-j−1/2`, both with amplitude sqrt(c). Their source *outgoing oriented* transition products are **P_source,up=P_source,down=c**, while the corresponding outgoing weights on the target shell are **P_target,up=P_target,down=0**, since each target sits at the zero-factor end in the corresponding outward direction.

Hence the exact oriented weight change is **ΔP_out=-c** on both legs. This does **not** imply that the witness's matrix-element magnitude changes from sqrt(c) to zero: its amplitude is fixed at sqrt(c); the zero describes the **subsequent outward ladder transition** at the target state. Nor is `P` a conserved scalar along the witness: the original outgoing source link and the target's outward link are distinct operators.

This is a restatement/refinement of the audited v15.143/v15.180 “escape climbs to next cone” geometry; not a new cross-shell physical operator. The witness changes shell integer `L'=L+2` and preserves **χ=(-1)^L** (v15.627).

## Gate 662 — the two simple null L→L+1 sector-changing embeddings

At each source node `|L,i>`, shell `j=L/4`, consider the two *chosen geometric index injections* into the neighboring quarter shell `L'=L+1`:

**A. |L,i> → |L+1,i>**: `m'=m−1/4`, `a'=a+1/2`, `b'=b`. Hence **ΔR=+1/4, ΔX=−1/4, ΔP=+b/2**.

**B. |L,i> → |L+1,i+1>**: `m'=m+1/4`, `a'=a`, `b'=b+1/2`. Hence **ΔR=+1/4, ΔX=+1/4, ΔP=+a/2**.

Both are null on the (X,R) kinematic diagram because **(ΔR)²−(ΔX)²=0**. Both flip the q=2 shell parity `χ=(-1)^L`, so **{χ,U}=0** on the direct-sum shell tower for either inter-sector shift U. These exact endpoint-supporting injections are a more explicit factor-coordinate realization of the *separately chosen* odd-rung shifts discussed in v15.626–627. They are not the v15.602 witness and not automatically physical motions; `J_+` still retains its defective step-one rule.

Crucial endpoint caveat: a or b can vanish. Thus ΔP≥0, with equality on the appropriate factor-zero endpoint; do **not** claim ΔP is strictly positive everywhere.

At the upward open-end source i=L−1 (a=1/2, b=(L+1)/2), shift A gives **ΔP=c**, while shift B gives **ΔP=1/4**. This pair of distinct values at the same source expresses the non-uniqueness of a geometrical odd-rung transport: a physical rule must choose a direction/amplitude from independent dynamics.

## Gate 663 — proof and physical result

All formulas follow by exact rational arithmetic, `(a+h)b−ab=hb` and `a(b+h)−ab=ha` at h=1/2. Exact Python/SymPy sweep of **L=1..80**, all i=0..L, validates simultaneous AM–GM identity, both null embeddings, the characteristic χ flip, boundary witness's c→0 outward product and χ preservation, and boundary special values. Source and target definitions are kept explicit, preventing a mistaken “product is conserved along a hyperbola” inference.

**Physical verdict:** static hyperbolic intersections encode the transition weight P but do not imply that any operator moving between shells preserves P. The established cross-shell witness and the chosen null quarter-rung shift act differently on P and on sector parity. No unique SI coupling, field action, electron velocity, radiation lifetime, gravity strength or EM↔gravity conversion emerges. The two distinct ΔP values at a single boundary node are a controlled demonstration that geometric compatibility alone doesn't choose dynamics.

**Reproducer:** `unified/discriminant-12-return/research-notes/k4_quarter_staircase_product_transport_v15_926.py`, commit **7898a553795bd74c0d2139999e04f280792a653c**. Independent external Audit pending.

**Next genuinely discriminating gate:** test whether either null injection admits a natural *adjoint-compatible* sum of both directions that intertwines with the existing defective step-one J and preserves an independently specified physical charge or energy law. Compare explicitly to the physical hydrogen SO(4,2) cross-principal dipole, not the static divisor geometry. A failure of these intertwining or selection constraints should be reported before proposing a new coupling.
