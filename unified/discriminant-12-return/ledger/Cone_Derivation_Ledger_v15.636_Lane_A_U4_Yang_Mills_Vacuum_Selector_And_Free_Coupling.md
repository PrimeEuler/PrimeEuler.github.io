# Cone Derivation Ledger v15.636 — Lane A: U(4) Yang–Mills vacuum selects a curvature representative but not gravitational physics

**Date:** 2026-11-10. **Parents:** independent Taub–NUT gravity pair v14.731–732; geometric odd-quarter Casimir v15.135 and v15.625–628; actual angular Chern winding v15.632; chosen rank-four bundle/grade v15.633 (Lane A) and connection counterexamples v15.634; External Audit Round 526 v15.635 (commit 348a82ea; independently confirms v15.633–634). **Status:** [D] exact source-free YM critical-point classification and special case; [C] independently postulated U(4) Yang–Mills action and absolute-ground-state condition; [O] physical matter representation, source action, coupling, independent G-free novel observable. **Immediately prewrite live HEAD:** 348a82eaecdcb9165f3ab9805d8c4c9450451b15; v15.636 filename and similar-topic collision searches empty. **Version reconciliation:** Round 526 disclosed that its Round 525 v15.633 entry preceded the Lane A v15.633 file by 19 minutes; both historical files are preserved, the audit's earlier entry retains chronological number priority, and this new entry uses the first free v15.636. No previous file rewritten. Suzuki physical-quarter weld remains parked; frozen far-tail production untouched.

## Gate 141 — actual field equation leaves many stationary solutions

On the round sphere S² of radius R, let E be the **chosen rank-four U(4) bundle** with c1(E)=k (the angular Taub–NUT charge). Choose, rather than derive, the source-free YM action

S_YM[A] = (1/(2g_YM²)) ∫_{S²} −tr(F_A∧*F_A),

where F_A is anti-Hermitian. The Euler–Lagrange equation is **D_A(*F_A)=0**.

For any integers k_a with sum k, the diagonal Dirac monopole patches are
A_N=i diag(k_a)(1−cosθ)dφ/2 and A_S=−i diag(k_a)(1+cosθ)dφ/2. Their curvature is F=i diag(k_a)sinθ dθ∧dφ/2, and *F=i diag(k_a)/(2R²) is a covariantly constant matrix. Thus **every such integer distribution satisfies YM equations**, not just the smallest-energy one. The normalized dimensionless curvature Y=(R²/π)∫−tr(F∧*F)=Σ k_a². For k=1 the inequivalent choices (1,0,0,0) and (2,−1,0,0) have Y=1 versus 5 and Wilson trace 3+i versus 1−i at north latitude θ=π/3. Both fit the chosen globally graded topological splitting (c1(E+),c1(E−))=(0,1), by putting both nonzero charges in E−.

## Gate 142 — exact critical-point classification gives Y_min=1 at k=1

For a *general smooth* U(4) YM critical connection on S², D_A(*F)=0 makes the skew-Hermitian endomorphism K=*F parallel. Its eigenvalues are constant, its eigensubbundles E_a are parallel and have ranks r_a, and F restricted to each is scalar 2-form, hence projectively flat. Because S² is simply connected, a flat PU(r_a) bundle is trivial, so E_a is isomorphic to a line bundle tensored with a trivial rank-r_a space. Consequently **deg(E_a)=r_a m_a with m_a∈Z**, and the curvature corresponds to m_a unit monopole flux per line. Thus

k=Σ_a r_a m_a,    Y=Σ_a r_a m_a² ≥ Σ_a r_a |m_a| ≥ |k|.

At k=1, Y≥1 on all smooth YM critical connections. The explicit (1,0,0,0) Dirac-monopole direct sum is critical with Y=1. Standard existence of smooth absolute YM minimizers on compact S² then implies **absolute minimum Y_min=1**, achieved only by one +1 charge line and three charge-0 lines, up to gauge equivalence, on this fixed metric. (The analytic critical-point classification does not depend on finite enumeration or a diagonal ansatz; existence of absolute minimizers is a standard Yang–Mills surface theorem, not derived here.) This condition selects the previously lower-energy connection if and only if the **chosen YM action** is minimized. The Y=5 higher-energy stationary solution remains; equations alone do not select the vacuum.

At θ=π/3, the minimizing Wilson trace is 3+i (or 3−i under reversed path orientation). This is a dimensionless output *within the chosen YM model and chosen probe/loop*; not a Cone-novel gravity prediction. The integral charge k=1 remains topological; the assignment of labels EM vs G to graded bundles is external.

## Gate 143 — coupling/scale freedom survives minimum selection

The action of a monopole distribution on sphere radius R is
S_YM=πY/(2g_YM² R²).
The equations and minimizer do not determine g_YM or R, nor which matter representation/observable couples to this new internal U(4). Choosing YM is an extra field layer not forced by the original Taub–NUT Einstein geometry or the cone arithmetic. It gives no Newton G, no fixed charge-to-mass calibration, no universal experiment, and no derivation of the physical odd-quarter Casimir operator.

## Gate 144 — graded vacuum is possible but its physical sector assignment is unselected

The previously constructed global grading E=E+⊕E− with c1(E+)=0,c1(E−)=1 permits a grading-preserving vacuum: put the lone +1 degree line inside E− and the other three lines flat. This identifies a topologically charged rank-two sector **given the chosen grading** but does not physically establish that E− is gravity; exchanging names or allowing a general non-grading-preserving connection is still possible. No source-derived odd-rung operator or its coupling appears from the source-free action.

## Reproducibility, audit and next gate

Exact independently executed SymPy reproducer and REPORT.md are in the conversation artifact `cone_ym_gates_141_144.zip`. Checks: curvature normalization, Y=1/Y=5 stationary examples, integer charge partitions for k=1, exact Wilson traces, and free coupling/metric scaling. The unrestricted critical-point bound is analytic and is not inferred from the finite enumeration.

**Conclusion:** unlike topology alone (v15.634), adding **a particular standard YM action AND absolute minimization** yields a rigid minimum connection and a parameter-free Wilson-trace shape at k=1, but this is a conventional source-free U(4) monopole result that depends on an *extra dynamical postulate*. The full Euler–Lagrange equation admits inequivalent excited stationary solutions. No physical gravity selector, NUT observation, G, or Cone-specific tidal law follows.

**HANDOFF** target external-audit, gravity, sandbox; status open; independently check the unrestricted critical-point projective-flat eigensplitting argument, YM minimum Y=1 rather than the weaker central Cauchy bound Y≥1/4, Wilson trace and action units, preservation of graded topology, and interpretation of the v15.633 numbering collision. Keep frozen Suzuki and certified prior files untouched.

**Next gate:** seek a *source-derived physical matter coupling* (rather than a freely imposed U(4) probe) and compute whether any observable distinguishes this YM vacuum from an ordinary integer monopole with three passive components. Test if adding a gravity-specific source necessarily introduces a new free charge/coupling normalization.
