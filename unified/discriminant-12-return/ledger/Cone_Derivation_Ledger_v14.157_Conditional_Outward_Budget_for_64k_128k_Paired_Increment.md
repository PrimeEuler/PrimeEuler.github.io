# Cone Derivation Ledger v14.157 — Conditional Outward Budget for the 64k→128k Paired Increment

**Date:** 2026-10-08 UTC / 2026-10-07 EDT  
**Track:** Lane A / numerical certification target  
**Status:** [D] small-block capacity perturbation bound; [V-synthetic] exact rational tests of both perturbation signs; [N/conditional] explicit sufficient arithmetic targets evaluated on the frozen actual-cutoff matrices. **Targets are not achieved certificates.**  
**Parents:** v14.147, v14.153–v14.156.  
**Collision check:** Live HEAD and latest Sandbox/External Audit were checked before this gate and again immediately before publication. The parent HEAD was `e9db24428a57bcf149575fd961a824dba2455c35`; ledger max v14.156; v14.157 and its script/payload namespace were free. The separate v14.155/v14.156 audits remain open. Published with expected HEAD, without force.

## 1. A blockwise perturbation estimate avoids demanding a tiny global assembly error

For each cutoff and parity, write the original serialized normalized reduction as

\[
\widehat M=\begin{pmatrix}\widehat J&-\widehat\beta\\-\widehat\beta^*&-\widehat\eta\end{pmatrix},
\quad \widehat K=\widehat\eta+\widehat\beta^*\widehat J^{-1}\widehat\beta.
\]

Let the exact stationary source reduction have block differences bounded by

\[
\|J-\widehat J\|\le a,\quad
\|\beta-\widehat\beta\|\le b,\quad
|\eta-\widehat\eta|\le c.
\]

If lambda_min(Jhat)>=j>a and ||betahat||<=q, then J is positive and

\[
\boxed{|K-\widehat K|\le
\kappa=c+\frac{b(2q+b)}{j-a}
+\frac{a q^2}{j(j-a)}.}
\]

Proof: compare the two quadratic forms first using J^-1 for both vectors, charging the vector change by b(2q+b)/(j-a). The remaining inverse change is bounded by the resolvent identity

\[
\|J^{-1}-\widehat J^{-1}\|
\le a/[j(j-a)].
\]

This permits a relatively large graph-block assembly error while retaining a small capacity error, because q is small. It does not require the graph, mixed and scalar assembly errors to share the same ceiling.

## 2. Sufficient source-faithful targets to certify next

The following are **proposed upper ceilings**, at each of the four actual-cutoff/parity rows. They have not been proved by the frozen midpoint output:

| Required outward quantity, before trace repair | Target upper ceiling |
|---|---:|
| ||T^-1 D||_F | 1e-20 |
| original affine assembly graph-block error ||Mhat_J-M(V)_J|| | 1e-4 |
| original affine assembly mixed-block error ||betahat-beta(V)|| | 1e-9 |
| original affine assembly scalar-block error | 1e-14 |
| exact projected graph residual Frobenius norm ||F||_F | 1e-11 |
| exact projected source residual norm ||r|| | 1e-15 |

These caps must include the exact source, represented-vector, projector and high/low arithmetic charges appropriate to each quantity. Matching a measured norm is insufficient. The exact source g remains the v14.153 source: zero through 32000, then 1/n even or 1/(n-1) odd.

For this conditional calculation only, assume that v14.155's full-Q floors have passed independent review:

\[
\gamma_e=2.95\times10^{-19},\qquad
\gamma_o=2.16\times10^{-17}.
\]

Use v14.156's rho=1e-20, nu=rho/(1-rho), corrected f_c=f/(1-rho), s_c=s+f nu. The three original assembly targets imply a conservative whole-matrix assembly bound

\[
\alpha=\alpha_J+2\alpha_\beta+\alpha_\eta.
\]

For m>=||Mhat||, let d_tr=nu(2+nu)(m+alpha). Then the exact stationary block errors relative to the **original unchanged** serialized matrix are bounded by

\[
a=\alpha_J+d_{tr}+f_c^2/\gamma,\quad
b=\alpha_\beta+d_{tr}+f_cs_c/\gamma,\quad
c=\alpha_\eta+d_{tr}+s_c^2/\gamma.
\]

No measured defect is substituted for rho. No remote-Schur gamma=1 is used. No new large solve is needed to establish the sufficiency of these targets.

## 3. Exact decisions on the frozen small matrices

The new consumer interprets every serialized M entry as an exact rational number. It obtains j from the minimum symmetric row diagonal-dominance bound of the 6x6 graph block, q from the absolute sum of its six mixed entries, and m from the largest absolute row sum of the symmetric 7x7 matrix. Each is an actual bound for these exact serialized data; Decimal output is used only for display.

The conditional errors are:

| Parity | Cutoff | exact serialized J lower bound, displayed | conditional capacity-error upper |
|---|---:|---:|---:|
| even | 64000 | 0.99999999999986366949 | 3.40104896e-12 |
| odd | 64000 | 0.99999999999999930720 | 5.62984568e-14 |
| even | 128000 | 0.99713573414287289203 | 1.21028216e-11 |
| odd | 128000 | 0.99733409685648284419 | 9.55418924e-13 |

In every case j>a, checked with rational comparisons. Their sum is

\[
\boxed{\epsilon_{pair}\le1.65155879589147018\ldots\times10^{-11}.}
\]

Let Psi be the exact source-faithful odd-minus-even difference of the 64k→128k capacity increments. By the four endpoint perturbation bounds,

\[
|\Psi-\widehat\Psi|\le\epsilon_{pair}.
\]

The independently replayed exact serialized scalar is

\[
\widehat\Psi=-7.08672715768713812693\ldots\times10^{-10}.
\]

Consequently the **conditional** interval is approximately

\[
\Psi\in[-7.25188304,-6.92157128]\times10^{-10}.
\]

The replay also verifies abs(Psihat)<=8.675e-10 exactly. This rounded baseline lies above v14.153/v14.154's displayed midpoint paired bound. Adding the conditional endpoint errors gives

\[
8.675\times10^{-10}+\epsilon_{pair}
=8.840155879589147018\ldots\times10^{-10}
<\boxed{9\times10^{-10}}.
\]

The final strict inequality and negative-sign test are exact rational decisions. The displayed decimal interval is not supplied as an outward interval certificate; the formula using exact rational endpoints defines the conditional bound.

## 4. Completed replay and remaining implementation

Reproducer: `research-notes/suzuki_normalized_outward_budget_replay.py`, alongside its standard-library dependency `suzuki_trace_congruence_replay.py`. Frozen result: `research-notes/payloads/normalized_outward_budget_v14_157/normalized_outward_target_budget.json`.

```sh
python suzuki_normalized_outward_budget_replay.py \
  --payload-root payloads/normalized_joint_run_37697455664 \
  --output normalized_outward_target_budget.json
```

Three additional exact-rational synthetic cases, seeds 23/73/197, compare the perturbation bound against directly recomputed capacities for both signs of the matrix/vector/scalar perturbation. All pass. The four original payload hashes are recorded again and remain unchanged.

This entry establishes explicit sufficient tolerances for the next numerical gate. The implementation must now supply outward bounds for the six target quantities, rather than import the midpoint diagnostics as certificates. The normalized producer remains fail-closed; its original certificate fields remain null. The separate full-Q and trace-repair audits must be checked before their conclusions are used downstream.

The conclusion is restricted to the finite 64k→128k octave. It does not bound all later octaves, certify the infinite tail, or promote a final Cone theorem.

HANDOFF
target: sandbox
type: audit
parent: v14.157
status: open
action: Verify the blockwise capacity perturbation lemma and exact-rational sufficiency calculation for the six proposed outward ceilings, identifying any omitted arithmetic charge in the conditional composition with v14.155/v14.156.
deliverable: theorem-or-obstruction
constraints: Ceilings are targets, not measured certificates; preserve the finite-octave scope; coordinate review with the already-open floor and trace audits; do not duplicate the large source solves or rewrite other lane entries; read live HEAD, latest audit and numbering before writes.

External Audit is invited to review the conditional budget under its standing update-watch scope.
