# Ledger v15.281 — Sandbox addendum to v15.277: second test round — gravity apex pair, Wigner holonomy channel, rest-gap census

**Kind:** Sandbox addendum; tests of v15.277/v15.280, all
confirmed (one after a recorded extraction fix).
**Origin:** Jeremy (2026-11-01): "can we test this structure
some more?"
**Producer:** `structure_tests.py` (clean exit).
**Payload:** `payloads/structure_tests_v15_281/` —
STRUCTURE_TESTS.md, structure_tests.py, structure_tests_output.txt.

## Results
**Test A — sector generality of the apex pair.** The triple
balance of v15.280 (vertex midpoint, crossing offset, curvature
sum vanishing together on the diagonal) holds on the gravity
refined mesh at the quarter scale: innermost vertices ±1/4,
innermost crossing (0, 1/2), curvatures ∓2/+2 cancelling,
vertex midpoint = X_cross/2 throughout.

**Test D — the Wigner holonomy sits in the odd channel.** The
Pair-Split placement of the v15.271 transport gauge was tested
where it could fail: composing boosts in both orders, the
resulting γ_w is exchange-EVEN and the Wigner rotation angle
θ_W exchange-ODD, each exact to 6 digits on four random pairs,
with the residual verified a pure rotation. (Recorded method
note: a first extraction with the wrong decomposition order
gave only approximate antisymmetry and a non-pure residual; it
was rejected and the producer corrected to the B·R form before
the pass was accepted.)

**Test G — rest gaps quantified** (closes the v15.278 list item).
ψ_min(N), the least rapidity at which the lattice samples
uv = N, is zero iff N is a perfect square and strictly positive
otherwise; primes are extremal with ψ_min(p) = ½ ln p exactly
(p = 499: 3.1063), and near-square shells N = m² − 1 have
ψ_min = ½ ln((m+1)/(m−1)) (m = 3, 5, 10), decaying ~1/√N. The
lattice holds exact rest only on square shells — the v15.274
seam as a computed function.

## Scope
Addendum to v15.277 (with Test G closing a v15.278 list item and
Test A extending v15.280). No gate, classification, or selector
statement changes; the standing Pair-Split failure condition is
unchanged and remains unmet by any test so far.
