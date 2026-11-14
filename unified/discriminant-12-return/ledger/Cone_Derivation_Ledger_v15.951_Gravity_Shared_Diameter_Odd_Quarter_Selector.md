# Cone Derivation Ledger v15.951 — Shared n+1 outer circle forces an odd-quarter interleaved shell

**Date:** 2026-11-13 Eastern. **Gravity lane.** **Parents/redundancy:** v14.767 scale-covariant diameter; v15.624–625 separate physical EM Casimir versus formal odd-quarter spectral classes; v15.866 Sandbox distinct tangency circles; v15.932 fixed-diameter half-row interleave and +1/4 GM² surplus; v15.943 formal quarter-Casimir midpoint −1/16; v15.947 original n+1 halfdisk and T/D/A counts; v15.949 co-scaled quarter parabola; v15.950 equal-product scale comparator. Latest Audit Round 576 v15.945 verified gravity v15.940–944, and its collision was repaired in v15.946. **Live prewrite HEAD:** 7b0c90f571a77c7b89187f92fa7273e9b9ddb2c4. Checked v15.951 target absent. Additive only, no certified/other lane/Suzuki changes.

**Question:** Instead of equal physical product (v15.950), demand that the EM 1/2-vertex and candidate G 1/4-vertex grids lie on the **same geometric outer circle of diameter D=n+1**. Does this condition naturally produce the *odd* formal quarter Casimir shell, not merely a different unit?

**Status:** [D] exact shared-diameter parity alignment and geometric gap; [C] common physical outer-diameter boundary choice; [N] no field-derived source, physical gravity operator or unique experimental response.

## Gate 730 — one global D=n+1 forces odd q=2 shell index

The general normalized factor endpoint pair is **(uL,u)** with diameter **D=u(L+1)** and factor product **P=u²L**. EM grid u_EM=1 has pair **(n,1)**, diameter D=n+1, normalized shell L_EM=n. The proposed quarter-vertex grid has u_q=1/2. Demand the *same* numerical physical diameter D=n+1. Then

**(L_q+1)/2=n+1 ⇒ L_q=2n+1**,

and the quarter endpoint pair is **(n+1/2,1/2)**. **L_q is necessarily odd** for every integer n≥1. In the geometric q=2 shell assignment **j_q=L_q/4=n/2+1/4**, exactly between the neighboring ordinary half-grid labels **j_EM=n/2** and **j_EM+1/2**. The fixed-diameter rule geometrically *selects the odd residue class* of the already-known formal q2 mesh without inserting parity by hand after the diameter match. It does **not** derive the separate physical G Casimir, because that requires independent rotational/dynamical generators per v15.624–625 and v15.942. Nor is D matching forced by known gravity/EM dynamics.

## Gate 731 — geometric radius offset versus *formal* Casimir midpoint

For any endpoint factor pair (D−u,u), the exact outer circle radius is **R_o=D/2**, product-defined squared inner chord **R_i²=u(D−u)**, and geometric Casimir-circle quantity from v15.934 is

**R_C²=(D²−u²)/4**.

At equal D for u=1 vs 1/2,

**R_C,q²−R_C,EM²=[1−(1/2)²]/4=3/16**,

a constant independent of n, while the physical factor products differ: **P_EM=n**, **P_q=(n+1/2)/2=n/2+1/4**, hence **P_EM−P_q=n/2−1/4** for n≥1. Thus these are **NOT equal-product sections** and cannot be treated as the same physical hyperbola; they share an outer circle because the arithmetic means match.

On the *formal* quarter-shell polynomial **C(j)=j(j+1)**,

**C(n/2+1/4)−(C(n/2)+C((n+1)/2))/2=−1/16**,

the exact midpoint defect already in v15.943. The formal quarter Casimir at L_q=2n+1 is **C_formal=L_q(L_q+4)/16**, whereas the **scaled geometric** radius on this circle is **R_C,q²=L_q(L_q+2)/16**. Their difference is **C_formal−R_C,q²=L_q/8**, nonconstant. Therefore the new geometric constant **+3/16** and old formal Casimir midpoint **−1/16** describe DIFFERENT comparisons and cannot be identified as one physical Casimir shift. As v15.866 already warns, h²/4 geometric gap and formal quarter Casimir residues are different objects.

Examples (n,D,L_q,P_EM,P_q,C_EM,C_q_formal,R_Cq²): n=1 => (1,2,3,1,3/4,3/4,21/16,15/16); n=2 => (2,3,5,2,5/4,2,45/16,35/16); n=3 => (3,4,7,3,7/4,15/4,77/16,63/16). The geometric RC² difference at every row is 3/16.

## Gate 732 — same-D versus same-P compatibility obstruction

For general positive grid units u≠v, the endpoint-pair diameter at the same physical product P is **D_u(P)=P/u+u**. The condition D_u(P)=D_v(P) forces **P=uv** (since D_u−D_v=(u−v)(1−P/(uv))). For u=1,v=1/2, this is **P=1/2**. However the EM grid's positive integer-factor contact shells have **P∈{1,2,3,...}**, so no positive EM integer endpoint shell shares **both physical product and outer diameter** with the half-scale grid. The shared-D alignment above therefore compares distinct product shells; this is an exact scoped incompatibility for primitive endpoint pairs.

## Verification / physical frontier

**Reproducer:** `research-notes/k4_fixed_diameter_odd_quarter_selector_v15_951.py`, additive commit **7b0c90f571a77c7b89187f92fa7273e9b9ddb2c4**. Executed a local SymPy version PASS before deposition: all symbolic relations, 200 consecutive shared-diameter integer shells, formal midpoint and both geometric radii, and same-P equality theorem. **Independent Audit pending.**

**Positive result:** A chosen shared global n+1 diameter gives an exact, *non-arbitrary parity mapping* n→2n+1, landing exclusively on odd-quarter q2 classes, alongside fixed +3/16 geometric squared-radius contrast. This is a new *matching-condition consequence* within the existing v15.932/943 geometry; it is not a new topological bundle or independent spin representation.

**Negative/next gate:** No reason from the current dynamical action selects common outer diameter over common P, common frequency, or common proper time; the selection is contingent. Test whether the physically sourced action-circle, boundary/matching condition, or Taub–NUT U1 periodicity independently selects D equality, and whether any predicted rank1/rank2 observable survives field rescaling. Otherwise record conditional geometry only.

**HANDOFF Audit/Muse:** verify odd L=2n+1 and ΔR_C²=3/16; scrutinize different products at common D and ensure the +3/16 is not mistakenly equated with the formal −1/16 midpoint or a physical G operator Casimir. Check the scope of P=uv for primitive endpoints.
