# Cone Derivation Ledger v13.526 — M16001 Frobenius Outward Replay

Date: 2026-09-16

Status: **[Audit] / [N-cert arithmetic-stage]**. No theorem promotion.

## Synchronization
Live head checked immediately before this write. Latest numbered ledger entry is v13.525; intervening commits are unnumbered arithmetic helpers/workflow. v13.526 is free.

## Executed replay
GitHub Actions run 35160274786 executed the integrated 7991x10 residual/Frobenius replay successfully on Ubuntu 24.04, Python 3.12, NumPy 2.5.3, SciPy 1.18.1. Integrated helper merged as commit `9d9311539e112e2eea1996b51269b6f1f96221ec`.

Observed transcript:

- point Frobenius residual = `7.8288856433727728125e-15`;
- legacy uncharged envelope = `9.582335208983376775e-15`;
- `u = 5.42101086242752217e-20`;
- `gamma_79910 = 4.3319297801658517316e-15`;
- formed squared-term sum = `9.182114805732249508e-29`;
- absolute formed-term sum = same (all nonnegative);
- 79910-term accumulation charge = `3.977627657185331599e-43`;
- charged squared-norm endpoint = `9.182114805732289284e-29`;
- sqrt point = `9.5823352089833975314e-15`;
- outward sqrt endpoint = `9.582335208983397532e-15`.

Thus, conditional on the R,E entrywise transcript supplied to this stage,

\[
\boxed{\|R_F\|_2\le\|R_F\|_F<9.582335208983397532\times10^{-15}}.
\]

No empirical safety multiplier is used in the Frobenius accumulation or sqrt stage.

## Important scope
This closes the previously missing 79,910-term accumulation and final square-root arithmetic. It does **not by itself** close all primitive residual provenance identified in v13.520. In particular, the integrated R,E producer is still the v13.514-style payload-level residual producer and does not yet inject the separately derived v13.521 primitive displacement-entry formation radii, the new pole-FC primitive radii, or all source-payload conversion radii into E. Therefore the boxed number is accepted as an outward bound for the arithmetic stage *conditional on its supplied R,E*, not yet as the final primitive theorem-consumable residual radius.

Certified inertia status remains
\[
\operatorname{ind}_{\le0}(A_{\rm even}(1))\le4,\qquad
\operatorname{ind}_{\le0}(A_{a=1})\le6.
\]

Next: inject primitive FF displacement errors through the actual columnwise `sum_j |X_jr|`, add FC displacement + pole-formation + payload-conversion radii entrywise, rerun this now-certified Frobenius endpoint, then propagate through the seven-plane Schur calculation.