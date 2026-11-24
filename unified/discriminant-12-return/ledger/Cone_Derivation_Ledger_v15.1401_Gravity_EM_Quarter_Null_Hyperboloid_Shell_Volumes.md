# Cone Derivation Ledger v15.1401 — Volumes between EM Jxy, closed q=2, and null observability hyperboloids

**Date:** 2026-11-24 Eastern. **Lane:** Gravity/Cone. **Classification:** [EXACT POSITIVE] nested representation-space (Q=T²-X²-Y²) sheets have constant, exactly partitioned fixed-(T) transverse areas, with a 3:1 EM–q2 shell / q2–null annular area ratio and 3/4 of the EM–null annulus lying between EM and q2; [EXACT NEGATIVE] these fractions are **not invariant under all natural choices of volume measure/regulator**: a common timelike-proper-radius/rapidity cutoff yields shell/inner ratio 7:1 instead; complete noncompact Lorentzian volume diverges; no unique dimensionless interaction or G scale follows; [OPEN] physical canonical measure/cutoff, operator-to-spacetime correspondence, state density, derived sigma/EFT coupling, detector response. The result is *representation-space geometry*, not a mass-shell prediction. Prior audited v15.1182/1183 is used to identify correctly the levels. Current external Audit Round 635, commit 902ee0e352d74f99888452da4891e90d7b8876ab, independently verified Gravity v15.1395–1398 without finding new errors. Additive only, preserve previous lanes.

## Gate 1325 — distinguish the three exact surfaces

The archived **ordinary EM** transverse observable is the standard Schwinger Jxy quadratic level (Q_{m EM}=(j+1/2)^2-m²-(j(j+1)-m²)=1/4) (v15.1182). The **closed q=2 refined nearest-step** SU2 carrier has (h=1/2), (Q_{m q2}=h²/4=1/16) (v15.1183). Its projected original-unit-step ladder does **not** generally lie on the same sheet: (Q_{m proj}=1/4+E_i), with boundary defects. The **null transition cone** has (Q_{m null}=0). These are three different representation-space constructions on the same ambient quadratic (Q=T²-X²-Y²), with positive T sheets. The physical gravity sector may have no Casimir carrier (v15.1178), so calling the q2 sheet "gravitational" is an **explicit working identification**, not already an established physical gravitational mass or force.

Write (a=sqrt{Q_{m EM}}=1/2), (b=sqrt{Q_{m q2}}=1/4). For each fixed (Tge a), the circle radii are

`R_null(T)=T`, `R_q2(T)=sqrt(T²−b²)`, `R_EM(T)=sqrt(T²−a²)`.

Thus (R_{m EM}<R_{m q2}<R_{m null}), and the annular area in the real transverse ((X,Y)) plane *between EM and q2* is

`A_EM-q2(T)=pi(R_q2²−R_EM²)=pi(a²−b²)=3pi/16`,

while the area *from q2 to the null cone* is

`A_q2-null(T)=pi(R_null²−R_q2²)=pi b²=pi/16`.

The entire EM-to-null area is (A_{m EM-null}=pi a²=pi/4). Hence **exact constant fractions** under this same-(T), Euclidean-transverse-area construction:

`A_EM-q2/A_q2-null=3`, `A_EM-q2/A_EM-null=3/4`, `A_q2-null/A_EM-null=1/4`.

The EM-q2 annular width in R shrinks as T grows, but the circumference grows and keeps area constant. For any fixed T slab (T_0le Tle T_1) with (T_0ge1/2), integrating the Minkowski coordinate-volume density (dT,dX,dY) over that **coordinate-defined slab** gives (V_{m EM-q2}=3pi(T_1-T_0)/16) and (V_{m q2-null}=pi(T_1-T_0)/16). This is geometrically exact and reproduces a 3:1 ratio, but (T_0,T_1) define a preferred Lorentz frame; boosts do not preserve these slab boundaries.

## Gate 1326 — independent Lorentzian-volume regulator changes the number

The ambient Minkowski measure (dT,dX,dY) is preserved by proper Lorentz transformations, but the **regions used for finite volume matter**. Parametrize the interior of the future cone by timelike proper radius (s=sqrt{Q}>0), hyperbolic rapidity (chige0), and polar angle (	heta):

`T=s cosh chi, X=s sinh chi cos theta, Y=s sinh chi sin theta`.

The Jacobian is **exactly (s²sinhchi)**. With a chosen *common rapidity* cutoff (0lechile H) the volume between proper radii (ble sle a) is

`V_shell(H)=(2pi/3)(a³−b³)(cosh H−1)`,

while the volume between the null boundary proper-radius limit (s=0) and the q2 sheet (s=b) is

`V_inner(H)=(2pi/3)b³(cosh H−1)`.

Their ratio is **((a³−b³)/b³=7)** for a/b=2, not the fixed-T value 3. The (chi)-cutoff selects a reference timelike axis, and as (H	oinfty) **each volume diverges**; any 7 obtained by cancelling a common regulator is still a *regulated ratio*, not a unique finite invariant volume of the unbounded regions. Moreover a fixed-(chi) cutoff approaches the null cone only at the apex as (s	o0), whereas a fixed-(T) annulus meets the null boundary at finite T; these are **different exhaustions**, not contradictory computations. Noncompact (SO^+(2,1)) has no finite-volume boost-invariant way to truncate all directions while preserving the whole symmetry.

In a genuine physical (3+1) spacetime with **three spatial dimensions**, the fixed-T spatial *ball* volumes instead give

`V^(3)_shell(T)=(4pi/3)[(T²-b²)^(3/2)−(T²-a²)^(3/2)]`,

`V^(3)_q2-null(T)=(4pi/3)[T³−(T²-b²)^(3/2)]`.

Their ratio **depends on T**, tending to 3 only at large T. For T=1/2 it is `≈1.85322214545`, for T=1 it is `≈2.79844737342`, and for T=4 it is `≈2.98823136616`. This also prevents indiscriminate import of the 2+1 representation-sheet constant annulus partition into a (3+1) physical cosmic volume, especially without a physical map from spin/Casimir coordinates to spacetime.

## Gate 1327 — interpretation, exact executable tests, and falsifiable selector

The *positive* feature is that the geometric midpoint steps h=1 and h=1/2 generate nested (Q=h²/4) sheets with **uniformly partitioned fixed-time transverse areas**: EM-to-null area decomposes exactly as (3/4+1/4), or shell/inner (3:1). This is potentially useful for constructing a **mode-counting or coupling weight** if a dynamical action independently chooses (i) the ambient representation-space (dX,dY) area, (ii) a common physical time-section variable T, (iii) a physical integration region/cutoff, and (iv) an operator or current with an actual measure over that region. None of these is yet derived from the archived K4 + Maxwell action or from a physical quantized quarter carrier. The ratio is not an independent universal coupling, a mass gap, an observed gravitational energy share, or G-free prediction merely because it equals 3:1 or 3/4:1/4.

**Actually executed reproducer:** `/mnt/data/cone_gate/k4_nested_hyperboloid_volumes_v15_1399.py` (its scratch filename reflects first chosen slot, but Audit already owns canonical v15.1399); all SymPy assertions PASS after correcting a spurious symbolic-limit assertion that had assumed (a>b) without specifying it. The actual valid assertion substitutes a=1/2,b=1/4 first. Additive GitHub source `research-notes/k4_nested_observability_hyperboloid_volumes_v15_1401.py`, commit **ab4f6eb5a51572d7e53b530ccd555ecb3d4a910c**, independently authored to reproduce the same exact area, Jacobian, regulated and 3+1 results; exact committed-byte Audit replay pending.

**AUDIT:** verify choice Q_EM=1/4 versus q2 closed Q=1/16 and projected defect (1/4+E_i), fixed-T annular area orientation, 3/1 and 3/4 fractions, Lorentzian coordinate Jacobian, regulated 7/1 volume ratio and its frame/noncompact limitations, and the physical 3+1 varying ratio. Avoid interpreting fixed-T slicing as a Lorentz-invariant finite shell measure or counting discrete SU2 states through a continuum Euclidean annulus without a state-density derivation.

**NEXT ACTION:** independently derive a **canonical spectral/state measure** on the EM and q2 ladders from their actual Hilbert inner products and/or variational phase-space symplectic form; compute whether the shell measure reproduces 3:1, 7:1, or another ratio *without choosing a cutoff*. Then test a proposed EM↔q2 transition matrix element/selection rule against v15.1397’s conditional rank obstruction and v15.1398’s exact radius/coupling cancellation. If no physically distinguished measure exists, treat these volumes as elegant but non-predictive ambient geometry.
