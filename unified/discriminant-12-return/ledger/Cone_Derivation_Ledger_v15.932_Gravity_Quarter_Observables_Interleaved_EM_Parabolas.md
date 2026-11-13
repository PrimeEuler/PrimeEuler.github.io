# Cone Derivation Ledger v15.932 — The q=2 quarter observable grid interleaves the EM half-vertex transition parabolas

**Date:** 2026-11-13 US Eastern. **Track:** Gravity/EM interpretation and bicone. **User question:** Can the 1/4 grid align with observables *between* the 1/2 transition parabolas of the glued SU(2) bicone? **Parents:** legacy `webgl/index.html` and v15.921–924 AM–GM parabolas, v15.140/v15.180 boundary/parity and phase, v15.573 factor-zero theorem, v15.602 refinement, v15.625–627 grading, v15.931 two-SU2 bicone gluing. **Live HEAD immediately before ledger write:** 9c31f5a390ca3663026a552263cac66f70e5300c. Target path checked absent. Additive-only; no edits to older scripts, staged paper, Audit, Sandbox or Suzuki.

**Status:** [D] exact vertex and fixed-circle interleaving, universal 1/4 increase of squared interpolated GM height and quarter-refined factor-coset classification; [D] independent pre-existing quarter Casimir radial 1/4 depth and phase-sensitive sector-odd measurement rule; [N] equality of the two 1/4 values does *not* identify their operators; [O] independent detector/action that measures phase or gravity in this lattice.

## Gate 678 — the vertices literally interleave

At physical factor scale u=1, the old WebGL fixed-factor parabola is **P_k: Y²=k²+2kX**, vertex `X_v=−k/2`. The original EM integer rows k=1,2,... have half-offset vertices `−1/2,−1,−3/2,...`. q=2 refines factor spacing by 1/2, so new half-integer factor rows k+1/2 have vertices **X_v=−k/2−1/4**, exactly between the neighboring EM row vertices **−k/2** and **−(k+1)/2**. The k=1/2 first row has vertex −1/4, reproducing the user's gravitational/interlay offset dictionary. On the mirror parabola use +1/4, with consistent orientation. This is an *exact geometrical grid refinement*, not yet an observed physical gravitational effect.

## Gate 679 — on a fixed n+1 transition circle, the interleaved squared height has a universal +1/4 surplus

At fixed circle diameter **D=n+1**, the row intersection coordinates are

**X_k=D/2−k**, **Y_k²=k(D−k)**.

At the halfway row, `X_(k+1/2)=(X_k+X_(k+1))/2` and

**Y_(k+1/2)² = [Y_k²+Y_(k+1)²]/2 + 1/4**.

The 1/4 follows exactly from the concavity `f(k)=k(D−k)` with discrete second difference `−2`; it holds **for all D**, including noninteger D where valid positive factor rows exist. With a physical coordinate scale **u=1/t**, the surplus is **u²/4** (not a dimensionless 1/4 in physical squared units), and both X and Y must use that same scale.

This is a concrete relation between EM transition amplitudes and their interleaved geometric half rows, with no fitting. It does NOT prove these interleaved squared amplitudes are new measured EM or gravitational transition rates. The genuine fixed-D Schwinger SU(2) representation samples only the integer factor rows, while the half rows belong to the separately refined grid.

## Gate 680 — exact q=2 chain classification resolves “observable between transition parabolas”

In the audited refined shell **j=L/4**, index `i=0,...,L`, its original step-one transition pair is **a=(L−i)/2, b=(i+2)/2**, sum **D=a+b=(L+2)/2=2j+1** and squared transition weight **P=ab**. Its transition center X=(b−a)/2. The operator J+ advances index i→i+2, preserving index parity; it is not the alternative refined nearest-neighbor closed spin-L/2 ladder.

For **even L**, D is integer, even i gives integral (a,b) and the single conventional closed EM chain; odd i gives half-integral (a,b), the interleaved open fragment. This makes the user's 'observable between EM transition parabolas' picture **literally exact** for the even refined shells, subject to a chosen observable coupling to the open fragment.

For **odd L**, D is half-integer; a and b have *opposite* integer/half-integer parity at every i, so there is no ordinary integer-pair closed chain. Instead there are two one-ended mirror fragments. Thus one cannot label every odd-quarter state as “midway between two points of a fixed ordinary EM spin-j transition matrix” without crossing to a different D shell. This is the representation-type boundary of v15.140 and v15.573, not a contradiction.

The original v15.180 radius identity **(j+1/2)²−j(j+1)=1/4** is also exact, but it compares the transition-circle radius squared with the *formal* Casimir sphere radius squared. The midpoint surplus above compares the midpoint GM² with an arithmetic average of adjacent EM GM². Their numerical 1/4 agrees because both are elementary half-step quadratic identities, but **they are not yet shown to be equal as operators or physical observables**. The odd-quarter fragment is not a conventional closed SU(2) spin-j irrep, so j(j+1) is formal in that sector and not a conventional measured Casimir.

## Gate 681 — phase observable interpretation and bicones

The already-audited q=2 sector grading is χ=(-1)^L. A putative *sector-odd* detector U has **{χ,U}=0** on the direct-sum two-sector space. Any state confined to a χ eigenspace satisfies **<U>=0**. For a coherent superposition `(|even>+e^{iφ}|odd>)/sqrt2`, an idealized Hermitian unit-normalized off-diagonal probe `U=|even><odd|+|odd><even|` measures **<U>=cos φ**. This is a simple exact two-state illustration of the older v15.180 relative-phase model, NOT a derived gravitational field detector or coupling. It highlights a plausible *operational target*: a phase-sensitive measurement between conventional EM chain states and interleaved quarter-grid fragments, rather than merely another ordinary EM intensity or decay rate.

The glued two-SU(2) bicone of v15.931 supplies standard SO(4) hydrogen orbital states and auxiliary vector/scalar shell-changing operators, but **does not by itself select U**, remove the odd-quarter defective-boundary algebra, or equate the q=2 formal quarter charge with a physical EM dipole polarization. Testing whether a physical field or measurement can furnish such an off-diagonal U is the next dynamical gate.

**Reproducer:** `unified/discriminant-12-return/research-notes/k4_quarter_interleaved_parabolas_v15_932.py`, commit **9c31f5a390ca3663026a552263cac66f70e5300c**. Local SymPy run PASS for exact midpoint identities, 64 q=2 shells, coset classification, formal quarter Casimir radius identity and idealized parity-odd phase witness. External Audit pending.

**Verdict:** **YES geometrically.** The q=2 grid is precisely the interleaved set of parabola vertices and between-transition circle intersections relative to ordinary integer-factor EM rows, and their squared heights obey an exact +1/4 midpoint surplus. **POTENTIALLY** its off-diagonal sector-sensitive operators can represent new kinds of observables; **NO** measured gravitational or dipole identification follows without a physical action and properly normalized measurement operator. Keep gravitational formal Casimir and EM spin Casimir separate.

**Next gate:** Consider a candidate physical, gauge-consistent phase reference or field-dependent H_int that actually connects the bicone's ordinary dipole triplet to one quarter-sector fragment. Demand an independently specified selection rule, a detector operator and a measurable dimensionless response ratio that survives comparison with standard two-mode optical homodyne or Stark/Zeeman response; test whether the q=2 selector is unique.
