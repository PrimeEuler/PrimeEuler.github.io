# Cone Derivation Ledger v15.1189 — Scalar kinetic-Hessian weight diagnostic: conditions for sigma = -H/2, not yet a certified scalar reduction

**Date:** 2026-11-18 Eastern. **Lane:** Gravity/Cone. **Status:** [D] generic exact constrained quadratic-action Schur-complement scaling identity; [D] exact treatment of a mixed q qdot term and the dependence of canonical frequency on an additional kinetic scaling power r; [C] expected a³ scalar kinetic scaling if the archived ADM constrained coefficients obey the necessary powers; [O] full symbolic extraction of scalar reduced K_PP(a,k,eta) and the auxiliary scalar ψ(t,k) from archived v14.935 source; [N] no demonstrated independent scalar -H/2 physical squeeze and no q2-specific gravitational boost/EM coupling.

**Live HEAD immediately prewrite:** 2a1962c03ab8b3f21b9404821febdaa9a0a932d7. Target v15.1189 absent. Additive-only; all older and certified files protected.

## Scope and redundancy
Owner authorizes next scalar canonical-normalization gate after exact vector reduction v15.1188. We retrieved and examined the original published v14.935 full SVT files `matter_sector.py`, `eh_scalar.py`, `assemble.py`, `scalar_statespace.py`, `vector_sector.py`, `final_checks.py`, and `NOTE.md`. They establish the *frozen-background* scalar propagating count (one scalar, ψ auxiliary), positivity of scalar kinetic A22 for k>0, and numerical frozen-time friction 3H. They **do not publish a closed formula for the full time-dependent constrained scalar kinetic prefactor in the ledger summary**; their reproducer produces a large expression `scalar_reduced.pkl` after assembling and constraint reduction and only afterward freezes coefficients. Do not infer a globally valid scalar canonical field normalization from a local frozen-spectrum check.

## Gate 1121 — exact Schur-complement weight theorem (conditional on ADM coefficient weights)
Take physical scalar velocity v and auxiliary lapse/shift variables z=(z1,z2). Assume a homogeneous constrained quadratic kinetic block
**L_kin=(a³/2)k0 v² + a² v C^T z +(a/2) z^T H z**,
with k0,C,H time-independent and H invertible on the chosen k>0 mode. Solve the algebraic auxiliaries **z_star=−a H^(-1) C v**. Substitution yields the exact reduced Hessian
**K_eff(a)=a³[k0−C^T H^(-1) C]**.
This proves that eliminating such auxiliaries does not spoil the a³ dependence: their Schur complement has the same scaling. **It does not prove the actual archived scalar ADM coefficients have these homogeneous weights after gauge fixing and solving the metric scalar ψ constraint.** That last claim requires direct coefficient extraction from the source file, not intuition from the vector reduction or the reported 3H eigenvalue.

## Gate 1122 — exact effect of mixed q qdot terms
For any single real reduced scalar q with action **L=(K(t)/2)qdot²+M(t)q qdot−(V(t)/2)q²**, direct Euler–Lagrange variation gives
**K qddot+Kdot qdot+[V+Mdot]q=0**.
Therefore **friction = Kdot/K**, while the mixed term shifts the restoring coefficient by **+Mdot**. The mixed term cannot be discarded from the global frequency merely because it drops out of the friction. This is essential to a faithful sourced scalar action check: the auxiliary scalar ψ(t,k) can induce such a time-dependent mixing when substituted.

## Gate 1123 — exact canonical diagnostic for a dressing exponent
Write **K(t)∝a(t)^(3+r)** locally with constant r (not an assertion that K4 actually does so), and set a(tau)∝tau. Then the reduced friction is **(3+r)/tau**. For the canonical coordinate u=sqrt(K)q, ignoring the independent Mdot restoring correction only for the displayed `omega²=V/K` toy, the effective oscillator frequency is
**Omega²=omega²−(3+r)(1+r)/(4tau²)**.
At r=0 this matches the vector shift −3/(4tau²). For r≠0 the coefficient differs. If the resulting Omega(tau)=constant/tau>0, its instantaneous normalization sigma=Omegadot/(2Omega)=−H/2 regardless of r; so a shared sigma alone does **not** prove equal underlying scalar and vector kinetic geometry. The physically meaningful discriminants are the complete canonical Omega, its log-time effective index, initial/final state matching, and observable metric/EM transfer.

## Verdict and Audit handoff
**Positive exact result:** a clear necessary computational diagnostic, general Schur-scaling theorem and correct mixed-term sign. **No full scalar closure yet**: the archival `scalar_reduced.pkl` coefficients and the time-dependent ψ algebraic constraint still must be run through actual symbolic elimination before claiming the K4 scalar has K_PP∝a³ or sigma=−H/2. This is an explicit open gate rather than a false certification. The prior vector-sector result v15.1188 stands independently and does not extend to scalar by analogy. Since the underlying action is Einstein gravity plus the same relativistic solid, even a confirmed scalar squeeze would be a conventional matched comparator unless a quarter-specific sourced operator yields a different dimensionless observable.

**Reproducer:** `research-notes/k4_scalar_canonical_hessian_weight_diagnostic_v15_1189.py`, additive commit **2a1962c03ab8b3f21b9404821febdaa9a0a932d7**. Local SymPy checks PASS Schur scaling, exact Euler–Lagrange mixed-term sign, arbitrary-exponent canonical frequency. A first local sign check used V−Mdot and failed; corrected to the actual **V+Mdot** before publishing. **AUDIT:** independently verify weight assumptions, mixed-term sign, distinction between frozen-state-space damping and genuine global scalar kinetic prefactor, possibility of scalar ψ-induced mixed term, and no extrapolation of the vector result. **NEXT:** execute the original archived source scripts and extract exact scalar K_PP(a,k,eta), ψ-slaving law, mixed coefficient and globally normalized scalar mode. Treat source-dependent coefficients, not abstract Hessian scaling, as the pass condition.
