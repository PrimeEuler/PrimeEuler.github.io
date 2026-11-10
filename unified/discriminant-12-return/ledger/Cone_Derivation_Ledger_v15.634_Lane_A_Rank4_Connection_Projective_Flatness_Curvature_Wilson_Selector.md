# Cone Derivation Ledger v15.634 — Lane A: rank-four Taub–NUT connection, projective-flatness obstruction and nonunique gauge-invariant response

**Date:** 2026-11-10. **Parents:** independently audited Taub–NUT quarter product v14.731–732, formal EM/odd-quarter Casimir mesh v15.135 and v15.625–628, patch integer winding v15.632 (External Audit Round 525, commit 262570f7, confirms v15.630–632), and v15.633 companion rank-four clutching matrix. **Status:** [D] exact topological and connection identities; [C] illustrative diagonal gauge connections with freely chosen internal charge distribution; [O] physically selected gauge connection, gravity-specific observables, interaction normalization. **Prewrite HEAD:** 1865dac5963648c212b1c03fa26a8b8edb964a69, duplicate search for v15.634 empty, similar-topic search empty. Additive-only; all Suzuki/far-tail frozen objects untouched; Suzuki physical-quarter weld remains parked.

## Gate 137 — projectively flat connection is obstructed when k not divisible by four

Let E be rank-four Hermitian bundle over S² with Taub–NUT-derived first Chern number c1(E)=k (v15.633), including k=1. Suppose a unitary connection has curvature **F=f I4** (a scalar matrix 2-form) at each point. Its induced projective PU(4) connection has zero curvature, so is flat. As S² is simply connected, the associated flat projective bundle is trivial and E can be expressed as L⊗C⁴ for a line bundle L; hence **c1(E)=4 c1(L)**. Therefore a globally projectively flat connection on E is possible only if **4|k**. Conversely if 4|k, take E≅L_{k/4}⊕4 and the central diagonal monopole connection, so projectively flat connections exist. This is a precise if-and-only-if topological obstruction to **scalar central curvature**, not an obstruction to ordinary noncentral U(4) connections. k=1 forbids the former.

For curvature of the unitary connection, the Chern–Weil lower bound from tr(F*F) gives the formal central-connection inequality Y≥k²/4 under the unit-round-sphere normalization below; equality would demand F scalar. For k=1 equality cannot occur for a smooth U(4) connection due to the topological obstruction, but this fact alone does NOT assert an explicit globally optimal Y among all nonabelian connections (we make no such unrestricted minimization claim).

## Gate 138 — a global Z2 grading is possible, with asymmetric Chern allocation

Write z=e^{ikφ}, and let the exact v15.633 clutching matrix be

M(z)=[[0,0,0,z],[1,0,0,0],[0,1,0,0],[0,0,1,0]], M⁴=zI4, det M=−z.

Choose χ_S=diag(1,−1,1,−1), χ_N=−χ_S. Then **χ_N M=Mχ_S**, so this pair of local matrices determines a globally defined Hermitian grading χ with eigenbundles E_± of rank two, notwithstanding {χ_S,M}=0 in the chosen common matrix coordinates. Restricting the clutching map to the (+) eigenvectors sends south indices (1,3) to north indices (2,4), with transition I₂: **c1(E_+)=0**. Restriction to the (−) eigenvectors sends south (2,4) to north (1,3), with transition [[0,z],[1,0]], determinant −z: **c1(E_-)=k**. Thus the particular chosen grading assigns the topological charge to one of the two rank-two sectors.

The exchange χ→−χ swaps sector names. The bare bundle M does not choose which is EM and which is gravity, nor does it force a physical gauge connection to preserve χ. A compatible U(2)×U(2) connection preserving χ is mathematically available after this splitting. For the same graded isomorphism class with (c1(E_+),c1(E_-))=(0,1), one may realize the two comparisons below within the negatively graded rank-two subbundle, leaving the positively graded one trivial.

## Gate 139 — same bundle charge, different curvature invariant

Use the standard unit-radius sphere metric and diagonal Hermitian Dirac potentials

A_N=diag(k_a) (1−cosθ)/2 dφ,
A_S=−diag(k_a) (1+cosθ)/2 dφ,

with k_a∈Z, physical unitary connection iA. On the overlap A_N−A_S=diag(k_a)dφ, and the anti-Hermitian curvature is F=i diag(k_a) sinθ/2 dθ∧dφ. Its total first Chern number is **k=Σ_a k_a**, and the dimensionless normalized curvature functional is

**Y=(1/π)∫_{S²}−tr(F∧*F)=Σ_a k_a².**

For k=1, arrangements (1,0,0,0) and (2,−1,0,0) both have the same total Chern class and hence define topologically isomorphic rank-four complex bundles over S², but **Y=1** and **Y=5**, respectively. They also admit the *same rank-two grading class* (put the two nonzero degrees into E_- and E_+ trivial). Their gauge-invariant curvature energies differ, demonstrating that the integer NUT winding and a global EM/G-like grading do not fix the connection or its response. For k=4 the central (1,1,1,1) connection has Y=4. A rank-four connection need not be diagonal; these are sufficient exact counterexamples to uniqueness.

## Gate 140 — explicit gauge-invariant Wilson traces differ at fixed k

For a north-latitude circle θ=θ0, the diagonal connection has Wilson trace, up to the common path-orientation complex conjugation,

**tr Hol(θ0)=Σ_a exp[iπ k_a(1−cosθ0)].**

At θ0=π/3 the two k=1 connections above yield **3+i** and **1−i**, respectively. Since Wilson trace is gauge-invariant under conjugation of the holonomy matrix, this directly distinguishes the two connections in the same Chern class. The base sphere radius and path geometry are fixed for this mathematical comparison; a physical measurable Wilson observable requires a probe coupled to the chosen U(4) representation, which has **not** been supplied by the cone or Taub–NUT derivation.

## Verification, audit and next gate

Exact Python/SymPy `reproduce.py` and explanatory REPORT.md are archived in the conversation artifact `cone_connection_gates_137_140.zip`. Executed successfully: exact M⁴, determinants, χ patch compatibility, rank-two restricted transition determinants, Dirac patch potentials/curvature/flux, k=1 Y=1 versus 5, and exact Wilson traces 3+i versus 1−i. Results apply to a **chosen U(4) model**, not a physical emergent gauge field. The first Chern class is fixed by the Taub–NUT monopole construction; no physical G or new gravity response is inferred.

**Verdict:** the companion rank-four extension admits smooth U(4) connections and a global Z2 grading, but at fundamental k=1 cannot support projectively flat equal curvature. Even with fixed winding and fixed graded topological sectors, infinitely many connections and gauge-invariant responses remain available. Thus topology alone neither selects a unique G-sector interaction nor fixes a dimensionless physical response. This is a constructive nonuniqueness counterexample, not a broad no-go for all additional actions or dynamical mechanisms.

**HANDOFF:** target external-audit, gravity, sandbox; independently verify the PU(4) flatness/divisibility proof, the globally transported grading and (c1+,c1−)=(0,k) restricted clutching determinants, curvature normalization, and Wilson traces on topologically isomorphic connections. In particular confirm no claim of an unconditional Yang–Mills global minimizer or physical identification of internal subbundles. Suzuki quarter integration parked and frozen work untouched.

**Next gate:** supply a specific field action and matter representation for the rank-four carrier, including a source-normalized coupling; calculate Euler–Lagrange field equations and their possible restricted solutions, then determine whether any gauge-invariant response remains fixed without fitting parameters. Also test whether a genuine Taub–NUT-derived worldline coupling supplies the needed internal connection. Do not choose an action post hoc merely to reproduce the quarter-spectrum.
