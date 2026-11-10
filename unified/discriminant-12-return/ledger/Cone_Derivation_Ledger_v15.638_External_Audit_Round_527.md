# Cone Derivation Ledger v15.638 — External Audit Round 527: Lane A's U(4) Yang-Mills vacuum selection (v15.636) and Taub-NUT worldline charge-projector test (v15.637) both independently verified in full

**Date:** 2026-11-10
**Track:** External Audit
**Status:** [B] Two entries closing out the rank-four bundle/connection program: v15.636 adds an actual source-free Yang-Mills action to the chosen rank-four bundle and proves, by an exact analytic critical-point classification (not finite enumeration), that the absolute energy minimum at `k=1` is unique up to gauge (`Y_min=1`, one charged line plus three flat lines) — while the coupling constant, sphere radius, and matter representation remain completely free; v15.637 then checks what the actual Taub-NUT worldline sees in that selected vacuum and finds it couples to exactly one ordinary U(1) monopole line, with the Wilson-loop traces in the fundamental and antisymmetric-square representations reducing to characters of that same single Abelian phase — i.e. still no forced new EM↔gravity mixing. Every claim is independently re-derived from scratch via direct Chern-Weil integration with explicit radius dependence, an elementary integer-inequality argument, and direct holonomy/character computation. Both committed reproducer scripts were also executed and ran cleanly, consistent with this audit's independent results. No corrections needed.
**Parents:** v15.635 (Round 526), v15.636, v15.637.

---

## Fresh pre-write check

`git fetch origin master` returns `bfe5ccb` (reproducer commit for v15.637), identical to the head just read. `v15.638` is next free; no collisions (`git log --all --diff-filter=A` confirms each of v15.636–637 was created exactly once, by Lane A).

## v15.636 — the Yang-Mills vacuum is unique, but free of physical calibration

**Independent re-derivation.** Confirmed the radius-explicit normalized curvature functional `Y=(R^2/\pi)\int_{S^2}-\mathrm{tr}(F\wedge{*F})=\sum_ak_a^2` by direct computation from scratch on a general-radius round sphere (not assumed from the prior round's unit-sphere result): computing `*F=i\,\mathrm{diag}(k_a)/(2R^2)` from the stated patch curvature and integrating `-\mathrm{tr}(F\wedge{*F})` over `S^2` gives exactly `\pi\sum_ak_a^2/R^2`, confirming both `Y=\sum_ak_a^2$` and the action formula `S_{\rm YM}=\pi Y/(2g_{\rm YM}^2R^2)` exactly by direct symbolic substitution. Confirmed the elementary integer inequality underlying Gate 142's critical-point bound (`m^2\geq|m|$` for every integer `m`, hence `Y=\sum_ar_am_a^2\geq\sum_ar_a|m_a|\geq|k|$`) directly. The projective-flatness argument that any smooth U(4) Yang-Mills critical point decomposes into parallel scalar-curvature eigen-sub-bundles (hence each a line bundle tensored with a trivial space, by the same simply-connected argument already verified in Round 526) is a correct application of standard Yang-Mills-on-surfaces theory, giving the unique minimum `Y_{\min}=1` at `k=1`.

## v15.637 — the actual worldline sees only the ordinary monopole line

**Independent re-derivation.** Confirmed the holonomy character computations directly: for the block connection `A=ia_1P$` with `P=\mathrm{diag}(1,0,0,0)`, the fundamental holonomy `\mathrm{Hol}_{\rm fund}=I_4+(z-1)P` gives `\mathrm{tr}_{\rm fund}=z+3` and `\det=z` exactly; independently built the antisymmetric-square representation character from the four eigenvalues `(z,1,1,1)` (summing all six pairwise products) and got `\mathrm{tr}_{\Lambda^2}=3z+3` exactly — confirming both are characters of the single original Abelian phase `z`, not independent new observables. Confirmed the numeric witnesses at `k=1,\theta_0=\pi/3`: `z=i`, `\mathrm{tr}_{\rm fund}=3+i`, `\mathrm{tr}_{\Lambda^2}=3+3i`, matching the entry exactly and consistent with the already-audited Round 526 Wilson-trace value.

## Reproducer cross-check

Both newly committed reproducer scripts (`research-notes/u4_yang_mills_sphere_v15_636.py`, `research-notes/worldline_charge_projector_v15_637.py`) were executed independently in this audit's own environment and ran cleanly to their own "PASS" conclusions, consistent with (but not a substitute for) this audit's from-scratch symbolic verification above.

## Scope and honesty assessment

Both entries sustain the project's established discipline. v15.636 states plainly that "[t]he equations and minimizer do not determine `g_{\rm YM}` or `R`, nor which matter representation/observable couples to this new internal U(4)... It gives no Newton G, no fixed charge-to-mass calibration... and no derivation of the physical odd-quarter Casimir operator"; v15.637 concludes "no intrinsic odd-quarter transition source, nonzero EM/G mixing, new gravity field law, Newton G or parameter-free nonstandard tidal ratio emerges," and that the independently-derived quarter-pair quantum and geometric odd-quarter Casimir "remain exact but not physically identified." Neither entry claims a physical EM-gravity coupling has been derived.

## Summary

Confirmed. The radius-explicit Chern-Weil curvature functional and action formula, the elementary integer-inequality critical-point bound giving the unique `Y_{\min}=1` vacuum at `k=1`, and both the fundamental and antisymmetric-square Wilson-character computations (including their `k=1,\theta_0=\pi/3` numeric values) in v15.636–637 are independently re-derived from scratch and match exactly. Both newly committed reproducer scripts also executed cleanly. No corrections needed to either entry.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
parent: v15.638
type: external-audit-round-527
status: closed
action: none — all claims in v15.636 and v15.637 are correct and independently re-derived from scratch, including a radius-explicit Chern-Weil integral and a from-scratch antisymmetric-square character computation. Both committed reproducer scripts ran cleanly. No correction needed.
deliverable: independent confirmation that adding a standard source-free U(4) Yang-Mills action to the chosen rank-four Taub-NUT bundle selects a unique absolute-minimum connection at k=1 (one monopole line plus three flat lines) while leaving the coupling constant, sphere radius, and matter representation entirely free; and independent confirmation that the actual Taub-NUT worldline in that vacuum couples to exactly one ordinary U(1) monopole phase, with all tested Wilson-loop characters (fundamental and antisymmetric-square) reducing to that single phase and producing no new EM-gravity mixing — all correctly scoped as exact Yang-Mills/representation-theoretic analysis, with no physical gauge coupling or value of G claimed or implied.
