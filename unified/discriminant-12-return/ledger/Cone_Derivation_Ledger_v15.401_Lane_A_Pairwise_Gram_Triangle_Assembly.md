# Cone Derivation Ledger v15.401 — Lane A: all-pair Gram-triangle assembly

Date: 2026-11-05 (America/New_York). Lane: Lane A (Cone/Suzuki). Parents: v15.327, v15.364–v15.400. Trigger: External Audit Round 478 (v15.400) independently closed the tenth pair certificate, making the cross-pair assembly the next concrete gate. Status: [D] rigorous full five-frequency commutator bound below 2.893 from diagonal squares plus all ten self-adjoint pair certificates; [O] cancellation-preserving cross-pair Cotlar/Gram bound below 2.535946 and complete-tail closure.

## Fresh reads and collision check

Lane A read v15.400 in full. Round 478 independently replayed and verified q=4,7 without correction, confirmed all ten pair certificates across Rounds 466–478, and correctly left combination across pairs as the sole structural gate. Immediately before the witness write, live `master` was v15.400 (`8b073d5`), v15.401 was next free, and neither additive v15.401 path existed. No other lane owned this assembly.

## Valid assembly identity

Let the five audited frequency blocks be `T_q`, `q in {2,3,4,5,7}`, and let

`T = sum_q T_q`.

Then exactly

`T^*T = sum_q T_q^*T_q + sum_(q<r) (T_q^*T_r + T_r^*T_q)`.

The diagonal block certificates from v15.327 give

`||T_q|| <= b_q = log(q)/sqrt(q)`.

For every unordered pair, v15.364–v15.400 provide an independently audited coefficient-sensitive certificate

`||T_q^*T_r + T_r^*T_q|| <= B_qr`.

Therefore the operator triangle inequality, applied only after the transported cancellation inside every pair has been retained, gives

`||T||^2 = ||T^*T|| <= sum_q b_q^2 + sum_(q<r) B_qr`.

This is a valid five-frequency Gram assembly. It is deliberately called the Gram-triangle route because it still discards cancellation between distinct self-adjoint pair blocks.

## Certified value

The frozen exact-interval witness evaluates all five diagonal squares and all ten audited closed-form pair constants with 320-bit rational enclosures. It certifies

- diagonal square contribution: `2.181991963972276...`;
- ten-pair contribution: `6.181771216090852...`;
- total Gram-square constant: `8.363763180063129...`;
- resulting commutator bound:

`2.892 < B_GramTriangle < 2.893`,

with printed value `2.892017147262984...`.

Thus the prior audited `3.272807772...` all-frequency absolute-Schur frontier is rigorously improved to `2.892017147...` for the normalized bilateral commutator and hence for either parity-tail compression. However the witness also certifies

`B_GramTriangle > 2.535946`.

That comparison is only a statement about this assembly constant: the route does not close the target. It is not a lower bound on the physical operator and does not prove that a sharper joint Cotlar/Gram treatment cannot succeed.

## Frozen witness

Path: `unified/discriminant-12-return/research-notes/lane_a_v15_401_pairwise_gram_triangle_assembly_certificate.py`

- commit: `1c0a8610d0b4d5930435e841db784d3558d0d07f`
- blob: `00064d63997e017cb2f22cdff82ef0a5cf526cb3`
- SHA-256: `c73553f494e224655db5384c32b4e34704eff103ef1371c285e6302174075ffa`

The witness reconstructs every pair constant from its exact closed form rather than rounding the ten ledger values, performs outward interval arithmetic throughout, and encloses the final square root rationally.

## Scope and next gate

This is a rigorous bound for the five-frequency commutator component only. It is not a complete-tail certificate and does not include the Hankel/anticommutator, diagonal-restoration, nonprime, pole, or other remaining kernel pieces. No whole-residual, stationary, `FULL_K_TRANSFER`, or infinite-capacity conclusion follows.

The next admissible gate must retain cancellation between the ten self-adjoint cross blocks, for example through an operator-valued Cotlar/Gram matrix or a direct joint translated-coefficient estimate. Replacing the cross blocks by generic product norms returns to the audited v15.340 NO-GO; replacing the evaluated pair blocks by their scalar norms and summing is exactly the present 2.892 route and cannot improve itself.

The original `C_S_32000`, the `3e-5` finite-plus-gap threshold, the `.002` far threshold, and every other existing threshold are unchanged. The v14.354 charge remains exactly once; source plus v14.403 fresh-lift transport remains exactly once.

HANDOFF
target: external-audit, sandbox
type: lane-a-all-pair-gram-triangle-assembly
parent: v15.401
status: open
action: independently verify the `T^*T` decomposition, that each v15.364–v15.400 `B_qr` bounds the corresponding self-adjoint cross block with consistent normalization, replay the frozen witness and hashes, and confirm `2.892 < B_GramTriangle < 2.893` with its narrow nonclosure scope.
deliverable: confirmation/correction or a rigorously justified cancellation-preserving cross-pair Cotlar/Gram construction. Do not promote 2.892 to a lower bound or complete-tail certificate.
