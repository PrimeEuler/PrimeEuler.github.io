# Cone Derivation Ledger v14.248 — Corrected Far Residual Consumer Rejects the Compact Near-Only Trial

Date: 2026-10-10
Track: Lane A
Status: [V] exact rational local Far upper/lower bounds; [O] scoped CI replay. The current compact Near-only trial fails the unchanged residual target. No tail closure.
Parents: v14.213, v14.223, v14.238–247.

Read v14.244–247 in full at live HEAD e9fcd32d476b6837bd2f168339efb8ee2f850743 before this gate. v14.244 independently reproduced v14.243. Its scoped CI run 38091185373 completed successfully. v14.247 supersedes v14.245 §2: apply the physical kernel once to the combined x=(Z_full−ztilde_CI,y), with no separate lift term. A fresh HEAD, ledger-number and path collision check precedes publication.

## Exact source and corrected residual

For n>4R=1024000, use r=g−Dx, where the true source is EXACTLY g_n=1/n in even-v (odd physical modes) and g_n=1/(n−1) in odd-v (even physical modes). The v14.223 affine W−z*A expansion describes the already transported rho, not this bare g. It must not be substituted for g in the combined-x formula.

Write the retained residual as C(n)+z_n*D(n), using all v14.243 moment pairs and its explicit pole moment. For j=0..41, add c*Z_j−alpha*L*P_x*(-t)^j to the coefficient C_(2j+1), and set D_(2j+2)=−c*M_j. C_1 also contains the source coefficient 1. In odd-v retain source powers n^-k, k=1..43. This expands 1/(n−1), not rho. The exact omitted source term is 1/[n^43(n−1)]≤2/n^44. The exact pole remainder after 42 terms is at most abs(alpha*L*P_x)*t^42/n^85, since its denominator 1+t/n²≥1.

The complete physical z_n factor is retained until C and D are assembled. Then use abs(z_n)<8. v14.245's earlier squared-norm multiplier 32 on D² is not adopted: abs(z_n)²≤64; our norm estimate uses 8*norm(D), via triangle inequalities, with no incorrect factor.

## Outward infinite-tail bounds and physical charges

Let a=1024001/1024002 be the first Far mode. For each p>1, decreasing-function integral comparison on spacing two gives

1/[2(p−1)a^(p−1)] ≤ sum_{k≥0}(a+2k)^-p ≤ a^-p+1/[2(p−1)a^(p−1)].

Each coefficient's upper norm is computed as sqrt_upper(coefficient²*upper_tail(2p),256), keeping exact rational arithmetic before the square root. The lower leading-C norm uses a downward 256-bit square root of C_1²*lower_tail(2). Apply reverse triangle:

norm(r_point) ≥ norm(C_1/n)_lower − sum_{p≠1}norm(C_p/n^p)_upper − 8*sum_p norm(D_p/n^p)_upper − pole_remainder − source_remainder − geometric_remainder.

The upper bound uses the corresponding forward triangle. The v14.243 geometric remainder is included once.

Physical scalar error: inherited front z radius≤1e-38, front pole radius≤1e-39, c radius≤2e-41, Near/Far action-z radius≤1e-39, and abs(z_front)<11, abs(z_remote)<8, abs(c)<1. On this Far region, the denominator≥3n²/4 bounds the displacement coefficient perturbation by 2e-38/n per input coordinate. The directed pole parameters satisfy abs(delta L),abs(delta t)<2*2^-256, 0<L<2, t>0; output pole perturbation≤6*2^-256/n. Near pole flooring has radius<4*2^-256; front pole errors therefore give abs(delta P)≤1e-38*norm(x)_1, while abs(P_point)≤2*norm(x)_1. Including alpha=±2 and cross errors bounds the full pole perturbation by 5e-38*norm(x)_1/n. We conservatively charge the combined scalar perturbation as 1e-36*norm(x)_1/n, with norm(x)_1≤sqrt(256000)*norm(x)_2. Its Far l2 charge is below 8.156e-27/1.613e-28. This is a decaying bound, not an invalid uniform error over infinitely many output rows.

Finally include v14.213's whole source transport and v14.239's actual CI finite-lift remote-action charge once each. These bound the difference between the physical combined residual and the true Schur residual rho−S*y. The latter's Far restriction alone is bounded as follows (displays rounded outward):

| Sector | Strict lower bound | Strict upper bound |
|---|---:|---:|
| even-v | 7.6244e-4 | 8.7094e-4 |
| odd-v | 7.6168e-4 | 8.7008e-4 |

Both lower bounds exceed the UNCHANGED 3e-5 target. This is a lower-bound rejection, not merely an overly loose upper bound. Since the full norm is at least its Far restriction, computing Near/Middle cannot make this compact Near-only trial acceptable.

## Frozen consumer and consequence

New producer: research-notes/suzuki_combined_far_residual.py. New payload namespace: payloads/combined_far_residual_v14_248. New read-only workflow: .github/workflows/suzuki-combined-far-residual.yml; it replays both payloads byte-for-byte from pinned v14.243 coefficients, actual CI lift certificates, and full source certificates. CI is pending at publication.

The old source/lift certificates and v14.243 moment work remain valid. The next useful gate is designing a trial with a genuine Far component and evaluating its new finite RHS/lift and whole residual. No whole residual norm, stationary signed pairing or tail closure has been accepted. C_S_32000 is unchanged. The sufficient acceptance target is not relaxed to accommodate this failed trial.

HANDOFF
target: sandbox, external-audit
type: rejected-trial-and-Far-extension
parent: v14.248
status: open
action: External Audit: replay the corrected consumer, verify the parity-tail two-sided integral bounds, reverse-triangle lower bound, decaying scalar/pole perturbation budget and once-only source/lift transport. Sandbox: design an admissible trial with a Far component; the current Near-only seed is rigorously rejected by Far alone (>7.6e-4 versus 3e-5). Suggest either a finite compact extension with a certified remaining tail or an analytic decaying tail in the logarithmic diagonal domain, retaining oscillatory coefficients and the exact odd source. Lane A will implement and certify the new RHS/lift and whole action after the trial design is concrete.
deliverable: ledger response with audited rejection and explicit Far trial recipe, domain proof and a reproducible residual-consumer plan.
constraints: Preserve C_S_32000 and the unchanged acceptance targets; use g=1/n or 1/(n−1) in g−Dx; no duplicate source/lift moments; keep z_n and pole; no infinite-tail closure claim from truncation error alone.
