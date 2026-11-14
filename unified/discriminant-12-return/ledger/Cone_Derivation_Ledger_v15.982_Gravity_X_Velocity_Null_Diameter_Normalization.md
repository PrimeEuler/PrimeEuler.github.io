# Cone Derivation Ledger v15.982 — Is the X velocity-axis half-step map forced by the n+1 null circle?

**Date:** 2026-11-14 US Eastern. **Gravity lane.** **User:** continue v15.981's exact 9/5 rapidity/CG coincidence by testing a genuine velocity-coordinate map derived from the X-axis null-cone and action-circle structure. **Prior work:** v15.860 ±c dimensional tags, v15.884 the owner's X-axis in m/s correction, v15.885 constant-proper-acceleration node conditionality, v15.888 rapidity node comparison, v15.905–906 Schwinger D=n+1 mapping, v15.932/955 (canonical repair v15.968) midpoint and transition-edge locations, v15.981 candidate β=(|m|+1/2)/D and special D=4 9/5. v15.617/623 physical symplectic/source caveats; v15.916 clock selector negative. **Latest Audit:** Round 580 at canonical v15.980, commit 93ce5785e8b20317a062eeefdd26e3552a3093dc, confirmed v15.978/979; v15.981 awaiting audit.

**Status:** [D] exact distinction between native null-coordinate ratio X/T, boundary-normalized edge ratio and previously chosen half-diameter edge ratio; [C] any interpretation as physical relativistic β=v/c; [N] neither 1/2,1/4 as physical speed nodes nor the 9/5 rapidity/CG bridge is forced by the cone identity; [O] dynamical metric/clock law and physical observable.

**Immediately prewrite live HEAD:** 00fae493b2ec76ed2da3cec4d765f385ea0d81c3 (validated reproducer). Target absent, additive-only; frozen Suzuki, Audit, Muse and Sandbox untouched.

## Gate 782 — separate null-cone coordinate normalization from physical speed

On the fixed EM Schwinger diameter D=n+1, set **T=D/2**, **X=m**, **Y²=T²−X²**. The algebraic identity **T²−X²−Y²=0** holds. A dimensionless directional coordinate naturally produced by that homogeneous equation is **b=X/T=2m/D** (with |b|≤1). For classical edges instead of state centers, the relevant outward positive coordinate is X_out=|m|+1/2 and the **boundary-normalized edge** is **b_edge=X_out/T=(2|m|+1)/D**. At an outermost state |m|=(D−1)/2, this reaches the null boundary b_edge=1.

The previously chosen velocity-node map v15.981 used **b_halfedge=X_out/D=(|m|+1/2)/D=b_edge/2**. It is an exact dimensionless arithmetic map, but it divides by the **full diameter D=2T**, not the distinguished scale T of the fixed null section. This extra factor of 1/2 is not selected by the null equation, and exactly explains how v15.981 obtained β=1/4,1/2 instead of the full-edge β=1/2,1.

Even for the native b=X/T, identifying b with a massive test particle's physical relativistic velocity β=v/c is **conditional**. A null vector with T²−X²−Y²=0 and dimensionless homogeneous coordinates is not automatically an on-shell particle four-velocity. Rescaling with a physical c can provide SI units, but it requires assigning the physically correct metric, parameter and motion law. The user's X-axis m/s interpretation is a proposed physical dictionary, not contradicted by this algebra; the test only shows what the cone identities do and do not determine.

## Gate 783 — D=4: three consistent geometric locations yield three distinct rapidity results

The D=4 ordinary EM carrier has j=3/2 and positive |m|=1/2,3/2. For the *same two state labels*:

| Map | inner b | outer b | ratio Cayley(outer)/Cayley(inner) |
| --- | --- | --- | --- |
| State centers: |m|/T | 1/4 | 3/4 | **21/5** |
| Boundary-normalized outward edges: (|m|+1/2)/T | 1/2 | 1 | **diverges** (atanh 1) |
| v15.981 half-diameter outward edge: (|m|+1/2)/D | 1/4 | 1/2 | **9/5** |

Here Cayley(b)=(1+b)/(1−b)=exp(2 atanh(b)). The 9/5 match to the D=4 axial and equal-weight TT-summed rank-2 CG ratio remains arithmetically exact, but **not invariant under these natural choices of center/edge and radius/diameter normalization**. In the edge-normalized model the last location is the zero-amplitude outward transition boundary; its infinite *assumed rapidity* is a reason **not** to equate every edge coordinate with a massive particle speed.

## Gate 784 — continuous physical scaling freedom remains even if state centers are accepted

Choose physical speed dictionary β=λ X/T with a positive speed-calibration factor λ≤1, so every state center remains subluminal. It preserves all original factor-grid locations and null-geometry identities while changing physical rapidity. For D=4, positive center coordinates are b_i=1/4, b_o=3/4. With λ=1 the Cayley ratio is 21/5; λ=1/2 yields 77/45; λ=2/3 yields 15/7; λ=3/4 yields 325/133. Thus geometry has **no unique SR rapidity difference** without independently specifying λ and which geometric points correspond to physical speeds.

This is complementary to the v15.885 scale covariance of acceleration: even after choosing β, a phase or frequency requires a physical trajectory, clock and action. The 1/4 and 1/2 mesh offsets are not themselves a derived physical massless/light speed. Similarly the exact factor-diameter ratio 9/5 at (7,2) in v15.906 is another independent arithmetic equality; no shared spacetime operator is supplied.

## Gate 785 — normalized geometry and the remaining physical lever

The best current *internal* normalization is b=X/T (or edges b=X_edge/T), because it is intrinsic to the homogeneous null equation and sends the boundary X=±T to ±1. The proposed half-diameter version can only be preferred if an independent physical reason selects a **half-speed velocity range** or a dynamical map with v=(c/2)(X/T) for those edge coordinates. The action-circle quantization of v15.973 does not select that map; v15.885 shows the action quantization and tangency alone do not determine a clock or acceleration.

Therefore **the v15.981 9/5 correspondence is a validated low-shell coincidence under a chosen half-scale speed dictionary**, not a derived universal Lorentz/SU2/TT-tidal observable. It is not ruled out that a future sourced field action supplies this map; it simply cannot be claimed from the available geometry. A legitimate positive result would derive the physical velocity map from a covariant Hamiltonian and show that its normalized polarization-resolved detector response differs from ordinary GR/Maxwell controls without postselecting the D=4 values.

**Validated exact reproducer:** `research-notes/k4_X_velocity_null_normalization_v15_982_validated.py`, additive commit **00fae493b2ec76ed2da3cec4d765f385ea0d81c3**, exact local SymPy check PASS for all three D=4 coordinate profiles, Cayley ratios, positive speed-rescaling controls and D=2..24 boundary normalization. The first script `k4_X_velocity_null_normalization_v15_982.py`, commit 0a7a645b32db8a4a653121c643f80fda7ce4fa42, contains an *assertion-only SymPy infinity representation error* (it tests denominator zero of zoo and fails). That original exploratory file is retained unchanged; **only the validated additive replacement is endorsed**. This is an explicit reproducibility disclosure, not a physics correction. Independent external Audit pending.

**NEXT / HANDOFF Audit/Muse:** verify center 21/5, edge divergence and half-edge 9/5, check the physical null-axis normalization and the precise distinction of m/s speed vs dimensionless X/T, and challenge whether any genuine source can fix λ=1/2 rather than any other value. If no sourced mapping exists, close the special 9/5 branch as unselected and return to actual tidal action/detector susceptibility.
