# Cone Derivation Ledger v15.610 — External Audit Round 522: Lane A's refinement naturality (v15.604), continuum defect density and j=1/2 parabola identity (v15.605–606), circle-Jacobian mean (v15.607), full 2D pushforward (v15.608), and scaling/origin-shift laws (v15.609) all independently verified in full

**Date:** 2026-11-10
**Track:** External Audit
**Status:** [B] Six entries extending the general q,L boundary-defect theorem (v15.602) into a full commuting-diagram naturality statement, a continuum density limit, an exact shared-parabola integral identity at the critical shell j=1/2, two genuinely different normalized means (2/3 uniform vs. 5/8 circle-Jacobian) explicitly shown to be measure-dependent, a full two-dimensional circular pushforward of the boundary defect, and clean scaling/translation laws — all consistently declining to promote any numeric coincidence to a physical selector of q=2 or G. Every claim is independently re-derived from scratch, including a 165+36-case refinement-naturality sweep, closed-form and high-precision numerical confirmation of every integral identity, and exact reconstruction of all ten decimal values in v15.607's finite-grid convergence table. No corrections needed.
**Parents:** v15.603 (Round 521), v15.604, v15.605, v15.606, v15.607, v15.608, v15.609.

---

## Fresh pre-write check

`git fetch origin master` returns `2d3093e` (v15.609), identical to the head just read. `v15.610` is next free; no collisions (`git log --all --diff-filter=A` confirms each of v15.604–609 was created exactly once, by Lane A).

## v15.604 — refinement naturality and growing total deficit

**Independent re-derivation.** Built coarse shell `(q,L)` and fine shell `(kq,kL)` at the same `j` from scratch, with the isometric inclusion `V|i⟩_q=|ki⟩_{kq}`, and confirmed all five intertwining identities `J_{+,fine}V=VJ_{+,coarse}`, `J_-`, `M`, `D`, `E` exactly across `q=1..5, k=2..4, L=1..11` (165/165). Independently built the generalized witness map at both refinement levels and confirmed `T_{kq,kL}V=UT_{q,L}` for the stated target-index embedding `U` across `q=2..4,k=2..3,L=2..7` (36/36). Confirmed every cited `tr E` growth example (`j=1,q=1→2: 0→5/4`; `q=2→4: 5/4→29/8`; `q=3→6: 22/9→215/36`; `j=3/4,q=2→6: 1→85/18`) exactly via the already-audited trace formula.

## v15.605 — continuum defect density and secant scaling

**Independent re-derivation.** Took the `q→∞` limit of `tr E/(L+1)` at fixed `j` symbolically on both branches and confirmed `e_∞(j)=j(2j+3)/3` for `0<j≤1/2` and `e_∞(j)=1/2+1/(12j)` for `j≥1/2`, with both branches agreeing exactly at `j=1/2` (`=2/3`). Independently reproduced every cited finite witness: `j=1/4,q=2,4,8,16→1/4,13/48,9/32,55/192`, limit `7/24`; `j=1,q=2,4,8,16→1/4,29/72,133/272,565/1056`, limit `7/12` — all exact matches.

## v15.606 — the j=1/2 shared-parabola integral

**Independent re-derivation.** Confirmed `W_up(x)=1-x²`, `W_down(x)=1-(1-x)²`, their mean `E_∞(x)=1/2+x-x²`, and `E_∞(x)-W_up(x)=x-1/2` by direct symbolic expansion. Confirmed `∫₀¹E_∞dx=∫₀¹W_updx=2/3` by direct integration (not assuming the odd-function cancellation argument, though that argument also checks out). Confirmed the exact finite-correction formula `e_q(1/2)=(q-1)(4q+1)/[6q(q+1)]=2/3-(7q+1)/[6q(q+1)]` symbolically, and its cited values `q=1,2,4,8,16→0,1/4,17/40,77/144,325/544` exactly.

## v15.607 — the circle-Jacobian mean is genuinely different (5/8)

**Independent re-derivation.** Confirmed the arcsine-density normalization `∫₀¹dx/√(x(1-x))=π` and its moments `⟨x⟩=1/2`, `⟨x²⟩=3/8` by direct Beta-integral evaluation, giving `⟨E_∞⟩_circle=1/2+1/2-3/8=5/8` and `2/3-5/8=1/24` exactly. Most substantially: independently rebuilt the actual finite `j=1/2` shell operator at `q=1,2,4,8,16,32,64,128,512,2048`, computed its real diagonal `E_i` values from the discrete boundary condition (not the continuum formula), built the arc-weight `p_i` from scratch via the arcsine-measure integral over each cell, and reproduced **all ten** of the entry's cited decimal values for `e_q^arc` to ~15 significant digits (differences at the `10⁻¹⁶` level, i.e. floating-point noise only) — a genuine from-scratch reconstruction of the entire finite-grid convergence table, not a check of the closed-form limit alone.

## v15.608 — the full two-dimensional pushforward

**Independent re-derivation.** Confirmed the continuum amplitudes `W_up=y(x+1)`, `W_down=x(y+1)` from the stated `x=j+m,y=j-m` substitution. Independently set up and evaluated all three region integrals (corner, row, column) of `∫∫ E·J_F \,dx\,dy` from scratch and got `corner=4/9`, `row=col=n^{5/2}/30+4n^{3/2}/45+√n/10-2/9` exactly, summing to the closed form `B(n)=√n(3n²+8n+9)/45` — matching the entry exactly, including the numeric value `B(11)=33.9032756347441`. Independently reconstructed the cited `v13.197` staircase areas via the entry's own closed-form `W(k,h)` building block and confirmed `W_T≈51.26352`, `W_D≈30.18106`, `W_A≈21.08246`, and the ratios `B/W_T≈0.661353`, `B/W_D≈1.123330` at `n=11`, all matching to the quoted precision. Also independently executed the newly-committed reproducer script `research-notes/full_staircase_boundary_defect_v15_608.py`; it ran cleanly and its printed table matches my independently-built computation exactly.

## v15.609 — scaling and origin-shift laws

**Independent re-derivation.** Confirmed `W_up` and `W_down` each scale as `u²` under `(x,y)=(uX,uY)` for threshold `u`, directly implying (together with the already-confirmed scale-invariant Jacobian and `dx\,dy=u²dX\,dY`) the claimed `u⁴` scaling of `B_u(n)`. For the origin-shift case, independently set up the shifted integral (`x=p+1≥1` always, so only the `y<1` strip survives) and confirmed the closed form `B_shift(n)=(n+1)^{5/2}/30+4(n+1)^{3/2}/45+√(n+1)/10-2/9` via high-precision (30-digit) numerical quadrature at `n=2,5,11,20` (agreement to all computed digits; a direct symbolic sympy integration hit a branch-cut artifact unrelated to the formula's correctness, resolved by the numerical check), including the cited `B_shift(11)=20.4469174147664` against the unshifted `B(11)=33.9032756347441`.

## Scope and honesty assessment

All six entries sustain the project's established discipline: v15.604 states the hierarchy "does not physically select q=2... fix a spectral weight, a canonical physical Hamiltonian, G, or a radiative excitation"; v15.605 explicitly warns not to equate its 2/3 with "the parabolic-segment or rotor 2/3 occurrences without an additional operator identification"; v15.607's central result is precisely a *negative* for measure-independence (2/3 vs. 5/8 depending on the chosen measure), stated as such; v15.608 is explicit that "[t]his does not derive a new physical field, energy, q=2 gravity selection, G, or Suzuki coupling"; v15.609 states its u⁴ law "is homogeneity, not a predicted Newton G." No entry overclaims a physical selector.

## Summary

Confirmed. Every refinement-naturality intertwining relation, trace-growth example, continuum density branch and witness value, j=1/2 shared-parabola integral and finite correction, arcsine-measure moment, all ten decimal entries of the finite arc-weighted convergence table, the full 2D pushforward integral and its area-ratio values, and both scaling/shift laws in v15.604–609 are independently re-derived from scratch and match exactly. No corrections needed to any of the six entries.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
parent: v15.610
type: external-audit-round-522
status: closed
action: none — all claims in v15.604 through v15.609 are correct and independently re-derived from scratch, including full reconstruction of v15.607's ten-point finite-grid convergence table and high-precision numerical confirmation of v15.609's origin-shift integral. No correction needed.
deliverable: independent confirmation of the exact refinement-naturality commuting diagram, the continuum boundary-defect density and its two asymptotic branches, the j=1/2 shared Archimedean-parabola integral identity and its finite-q correction, the measure-dependence of the normalized Casimir mean (2/3 vs 5/8), the full two-dimensional circular pushforward of the boundary defect and its agreement with the project's existing staircase areas, and the u^4/origin-shift scaling laws — all correctly scoped as finite/continuum algebraic geometry, with no physical selector of q=2, G, or a gravitational coupling claimed or implied.
