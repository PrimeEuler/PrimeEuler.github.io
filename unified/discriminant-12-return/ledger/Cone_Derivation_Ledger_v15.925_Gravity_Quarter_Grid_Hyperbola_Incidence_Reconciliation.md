# Cone Derivation Ledger v15.925 — Hyperbola/product intersections reconciled with the existing unbounded quarter-grid staircase

**Date:** 2026-11-13 US Eastern. **Track:** Gravity/EM geometric operator reconciliation. **Parents:** v15.140, v15.180, v15.572–573, v15.602, v15.627; Gravity v15.921–924 (user's original WebGL factor-row parabolas and exact hyperbolic intersections). **Immediately before ledger write, live HEAD:** 093c7eb40ef6b5d5e9d3b298fabe7f1ec6145b74. Target path absent; additive-only, historical quarter-grid/Audit/Sandbox/Suzuki/certified objects untouched.

**User reminder:** The product-shell/sum-shell intersection network has already been developed on the **unbounded q=2, ±1/4 mesh**. Avoid rediscovery, and verify whether the hyperbola weights agree with the older staircase's Casimir boundary and cross-shell witnesses.

**Status:** [D] exact overlap with the audited old quarter-grid weight/defect identities, including all boundary cases; [N] 44 exact SymPy shell checks; [N] the existing boundary witness preserves grading rather than coupling the proposed EM and gravitational sectors; [O] physically selected cross-sector/radiative operator.

## Gate 655 — quarter-grid parabolas intersect both fixed-sum and fixed-product shells

On the original q=2 refined mesh from v15.602, set integer shell index L≥1, j=L/4, mesh m_i=−j+i/2 for i=0,...,L. Keep the **original** step-1 raising law, NOT the alternative closed half-step SU(2) ladder. For its transition centered at X_i=m_i+1/2, the *same legacy WebGL AM–GM pair form* is

**a=j−m_i=(L−i)/2**, **b=j+m_i+1=(i+2)/2**,

**R=(a+b)/2=j+1/2=(L+2)/4**,

**X=(b−a)/2=(2i+2−L)/4**,

**P=ab=(L−i)(i+2)/4=R²−X²**.

Thus for every state with a>0, the same factor-row parabola **Y²=a²+2aX** and hyperbola **T²−X²=P** meet at **X=(P−a²)/(2a)**, with **T=R** and **Y²=P**. This exactly embeds v15.922's hyperbolic intersection geometry on the already-defined refined staircase, with the essential new accounting being **half-integer a,b** rather than unrestricted integer divisor pairs. The integer-scaled factors A=2a=L−i, B=2b=i+2 have sum L+2, product AB=4P. Since the refined grid fixes L and i, no unconditional identity with d(N) for integer N should be asserted. The square-root weight is a *matrix amplitude* once the representation's step-1 operator is supplied, not by the intersection alone.

## Gate 656 — exact upper/lower escape products and boundary theorem

At the source of the upward missing edge, i=L−1 (m=j−1/2), its factors are

**a=1/2, b=j*2+1/2=(L+1)/2**,

so its absent transition has **P_escape=ab=(L+1)/4=j+1/4**. This is the **same** universal escape weight from v15.140, v15.180, v15.572 and the factor-zero theorem v15.573, without a new boundary parameter. The downward missing edge is the corresponding mirrored source i=1 with the same weight. For L=2, these two directed omissions share the same source; don't claim there are always two *distinct* defect sites.

The physical point of the missing upper-edge amplitude is at **X=j** on the boundary transition circle R=j+1/2, while the missing destination at m'=j+1/2 is the top state of adjacent j'=j+1/2 shell. The target has its *own* zero outgoing raising factor; the source's nonzero P does **not** become a conserved product carried to the target. Thus the geometric staircase describes adjacent shell incidence, not equality of product N across the shell shift.

## Gate 657 — exact defective algebra and previously chosen witness

For finite refined shell, define J+ as step i→i+2 with amplitude sqrt(P_i) when the destination is present, J−=J+†, M=diag(m_i), Jx=(J++J−)/2, Jy=(J+−J−)/(2i). Retaining the original defective unit-step ladder, one obtains

**D=[J+,J−]−2M**,

**E=j(j+1)I−(Jx²+Jy²+M²)**.

The upper missing-edge product contributes +c to D at i=L−1, and the reflected lower edge −c at i=1, where **c=j+1/4**. In matrix form **D=c(|L−1><L−1|−|1><1|)**, with coincident-source cancellation when L=2. The positive Casimir defect is **E=(c/2)(|L−1><L−1|+|1><1|)**, allowing the coincident-site contribution at L=2. Hence **tr(E)=c** and the two missing *directed* edge squares sum to 2c.

The existing v15.602 **chosen geometric cross-shell witness** T maps the omitted upper/lower edges to orthogonal endpoints of shell j'=j+1/2 (L'=L+2), with amplitude sqrt(c) per directed edge. It satisfies exactly **T†T=2E**. This is the already-audited construction; the hyperbola view is an exact coordinate/weight reconciliation, NOT a newly derived operator.

## Gate 658 — selection-rule warning

The quarter grid's formal sector grading at q=2 is **χ=(-1)^L**. Since the established boundary witness changes L→L+2, it **preserves χ**, exactly as v15.627 established. By contrast a separately chosen minimal L→L+1 shift flips χ but is not the v15.602 witness, has independently unspecified amplitudes and is not a physical EM↔gravity interaction. Neither the hyperbola formula nor its divisor-product labels upgrades the existing T into a cross-sector physical operator.

The classical AM–GM coordinate is the same algebraic parabola family on the EM integer grid and the refined quarter mesh, but their *representations* are not the same: the even refined shell has one closed standard SU(2) chain plus an open fragment; the odd-quarter refined shell has two mirror open fragments and no closed unitary spin-j SU(2). Its formal j(j+1) is not an actual closed representation Casimir. Additionally, the gravitational mesh's formal Casimir should not be conflated with the EM 1/4 spin correction.

## Gate 659 — verification / next step

**Reproducer:** `unified/discriminant-12-return/research-notes/k4_quarter_grid_hyperbola_boundary_witness_v15_925.py`, commit 093c7eb40ef6b5d5e9d3b298fabe7f1ec6145b74. Local Python/SymPy independently executed for all L=1..44: PASS intersection identities; all D, E matrices; c boundary weights; precise T†T=2E including L=2 overlap; trace E=c; unchanged parity χ under L→L+2. In particular L=3 (j=3/4) gives D=diag(0,−1,+1,0), E=diag(0,1/2,1/2,0), and upper/lower missing edge products each 1. External Audit pending.

**Verdict:** The sought fixed-product hyperbola intersections **are already encoded** in the unbounded quarter-grid staircase, including its missing-edge Casimir/commutator defects and chosen cross-shell witness. The latest work supplies an explicit geometric-coordinate and factor-product audit that connects the legacy WebGL formula to those earlier results; it does not add new physical forces, radiative lifetimes, a clock, G, or a unique EM↔gravity coupling.

**NEXT nonredundant test:** Starting from the *existing* audited q=2 graph, label all vertices by their pair product P and track the cross-shell witness T's product *change*, not assume it conserves P. Compare exactly against the previously defined null target geometry and χ parity; determine whether any geometrically natural, symmetry-respecting operator with **odd ΔL** can carry physical E1 transition labels without inserting arbitrary amplitude factors. Do not disturb Lane A/Suzuki certification or assert a physical operator absent an action.
