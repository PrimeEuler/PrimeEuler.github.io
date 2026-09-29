# Cone Derivation Ledger v13.868 — Refinement Note: Suzuki's One-Way Implication RH ⟹ λ_a > 0, and Lane A's One-Sided RH Test

Date: 2026-09-29

Type: **citation refinement + strategic note** (not a derivation, not an audit of other entries). Contributed by the external audit thread; written up for the ledger at the project owner's request.

Parents: v13.867, v13.860 (Lane A λ_a > 0 target proposal), v13.794 (Lane A λ_a guardrail; source-faithful form-core Galerkin route), v13.848 (Bucket 2's standing hypothesis λ_a > 0).

Synchronization: live ledger head checked immediately before this write is v13.867. No collision on the present version number. **This entry does not audit v13.867 or earlier.**

## 0. The citation [D]

While checking the v13.860 proposal's sourcing, the audit thread found the following in Suzuki's text (already recorded source-faithfully in this ledger at v13.794): Section 7 explicitly assumes RH and then takes \(\lambda = 0\), \(T_{a,0} = A_a\), **because under RH \(A_a > 0\) for all \(a\)**. That is a **one-way implication**:

\[
\mathrm{RH} \;\Longrightarrow\; \lambda_a > 0 \quad \text{for every } a,
\]

where \(\lambda_a\) is the bottom eigenvalue of \(A_a\). It is **not** an equivalence, and Suzuki does not claim the converse.

## 1. What this refines (and what it doesn't)

**Refines v13.860:** \(\lambda_a > 0\) at one fixed finite \(a\) still isn't RH-equivalent and remains the tractable Lane A target — a certified-numerics objective with a clear success criterion, independent of RH's truth. That stands.

**Adds a pressure-test angle Lane A didn't have:** the contrapositive. A certified \(\lambda_a \le 0\) at *any* finite \(a\) would disprove RH. So every certified-numerics run on the bottom eigenvalue is simultaneously a **one-sided RH test**: success (certified \(\lambda_a > 0\)) is merely consistent-with-RH — a necessary condition checked, nothing proved; failure (certified \(\lambda_a \le 0\) with real margin) is catastrophic-for-RH. The program's information content is entirely in the failure direction.

## 2. Caveats [I]

- **The certification bar is asymmetric too.** A floating-point non-positive number is a signal to look harder, not a disproof. Only a rigorous enclosure with the inequality genuinely pointing the wrong way would count against RH, and the scrutiny such a claim would face (replication, independent codes, interval arithmetic end-to-end) should be understood *before* anyone runs the experiment, not after.
- **The quantifier matters.** RH gives \(\lambda_a > 0\) for *all* \(a\); each \(a\) tested is an independent one-sided check. There is no reason to stop at one.
- **No converse strategy is licensed.** Nothing here suggests proving \(\lambda_a > 0\) at finitely many (or even many) \(a\) constitutes progress toward RH. The implication points one way.

## 3. Consequence for the sandbox chain [I]

The sandbox Bucket 2 chain's single standing hypothesis is \(\lambda_a > 0\) (v13.848, v13.860). This note makes its failure mode explicit: if Lane A ever certified \(\lambda_a \le 0\) at some finite \(a\), our hypothesis fails — but so does RH, and the latter is the news. The chain's hypothesis is exactly the thing whose certified failure would falsify RH. Readers of the sandbox track should understand the hypothesis in both directions.
