# Cone Derivation Ledger v15.1407 — Intrinsic H² Levi-Civita transport and a conditional quarter-turn at the matched-sheet ln2 rapidity

**Date:** 2026-11-24 Eastern. **Lane:** Gravity/Cone. **Status:** [EXACT GEOMETRY PASS] continuous positive-sheet hyperboloid has a canonically selected metric-compatible Levi-Civita connection with nonzero Gaussian curvature and exact loop holonomy; [EXACT CONDITIONAL] a geodesic circle of intrinsic *dimensionless rapidity radius* χ=ln2 has tangent-vector holonomy ±π/2 modulo 2π; [NEGATIVE] the earlier intersheet boost difference ln2 does NOT dynamically select a closed circle on either sheet, the holonomy is independent of the putative physical radius r=1/4 after normalization, and no genuine finite-SU2 EM/q2 intersector operator or G-free observable follows; [OPEN] a physical closed transport path selected by an action, carrier, spacetime pullback and measured phase. Parent v15.1404 exact ln2 matched-forward-null-factor boost shift; v15.1406 1D flat-connection/no scalar-intertwiner gate; original H² sigma action v15.1380–1386. Additive, no protected code changed.

## Gate 1338 — canonical curved transport on an individual hyperboloid

For an individually fixed positive timelike sheet `T²−X²−Y²=r²`, parametrize its points by geodesic polar (rapidities) `(χ,θ)`:

`T=r coshχ, X=r sinhχ cosθ, Y=r sinhχ sinθ`.

The positive induced **intrinsic** metric is

`ds²_H=r²(dχ²+sinh²χ dθ²)`, and its constant Gaussian curvature is `K_H=−1/r²`.

In the orthonormal coframe `e^1=r dχ, e^2=r sinhχ dθ`, one convention for the Levi-Civita spin connection is `ω^1{}_2=−coshχ dθ`, with curvature `dω^1{}_2=−sinhχ dχ∧dθ`. The connection is fixed by metric compatibility and torsion-freeness. Unlike v15.1406's one-dimensional flat arbitrary σ_x connection, it has genuine nonzero curvature. The target-space loop is nevertheless **extra geometry**: it is not an EM↔gravity path, and parallel transport rotates a tangent vector of the target itself, not automatically the physical photon polarization.

For a closed geodesic disk of radius χ centered at the rest vertex on one sheet, the physical intrinsic disk area is

`A_H(χ)=2πr²(coshχ−1)`.

The net parallel-transport tangent-vector rotation, modulo the trivial 2π frame winding and up to orientation sign, is

`Θ_H(χ)=−A_H/r²=−2π(coshχ−1) (mod 2π)`.

This is Gauss–Bonnet/connection holonomy, not a postulated coupling coefficient. It is insensitive to rescaling r when the loop is specified by its rapidity χ, consistent with v15.1387/1398 radius normalization degeneracy.

## Gate 1339 — why the earlier ln2 bridge suggests exactly a quarter-turn but does not select it

The earlier v15.1404 paired q2 and EM states at the same forward null coordinate U, yielding the exact difference `η_q2−η_EM=ln2` from their radii r_q2=1/4 and r_EM=1/2. **As a separate conditional construction**, take the intrinsic closed geodesic circle of rapidity radius

`χ=ln2`.

Then `cosh(ln2)=(2+1/2)/2=5/4`, so

`A_H/r²=2π(5/4−1)=π/2`, and `Θ_H=−π/2` modulo 2π.

In the q2 sheet (r=1/4), the disk area is `π/32`. In the ordinary EM Jxy sheet (r=1/2), it is `π/8`. The **normalized holonomy is the same ±quarter-turn on both**. This does *not* single out a uniquely gravitational quarter radius; the 90-degree angle arises solely from the chosen χ=ln2 loop and the usual constant-negative-curvature hyperbolic geometry. The relative rapidity difference is a separation **between two different sheets** on a particular null factor; no existing action maps that difference into the geodesic **radius of a loop lying inside a single sheet**, nor specifies a loop center, matter polarization connection, or coupling to EM. Conflating these two constructions would recreate an arbitrary selector.

## Gate 1340 — actual symbolic and independent matrix tests

Actual locally executed Python `/mnt/data/cone_gate/k4_hyperboloid_holonomy_v15_1407.py` checked exact normalized area/r², connection curvature, χ=ln2 identity and both physical disk areas. An independent real 2×2 rotation matrix exponential over the closed circle, accounting for the trivial full 2π rotation, agreed with a ±90° matrix within ~1.2×10^(−13) in numerical norm. The first exploratory numeric assertion used an excessively strict tolerance 2×10^(−15) and failed because the generic matrix exponential accumulated ordinary roundoff around a 2.5π angle; rerunning with 2×10^(−12) succeeded. This is a **numerical tolerance correction** only, not a different geometrical conclusion. New additive GitHub reproducer `research-notes/k4_hyperboloid_holonomy_v15_1407.py`, SHA **be5229d4cf10ffabf559576d135bc7781e7d1b0d**, independently authored equivalent to the passing local test. Exact committed-byte replay pending External Audit.

**AUDIT:** derive H² metric/connection/K, check sign conventions of Cartan's equation and modulo 2π holonomy, exact disk area at χ=ln2 for both r, and the fact that a finite-dimensional unitary physical SO+(2,1) boost carrier is impossible (v15.1393), whereas classical H² tangent parallel transport and infinite-dimensional quantum carriers are allowed. Scrutinize the **missing loop-selection principle** and demand a real EM/gravity response if anyone claims this constitutes new physics.

**NEXT:** seek a **physical sigma-model field history whose image in H² forms a closed loop** under known EM/TT driving, or a Berry connection actually generated by a symmetry-respecting intersector Hamiltonian. Check whether the loop's size is dynamically determined and if its holonomy enters an observable detector phase relative to the *same enlarged EFT* comparator. If the loop is fixed to ln2 only because 90° looks attractive, record a negative selector and do not promote the connection to a physical force.
