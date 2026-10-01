# Cone Derivation Ledger v13.890 — Sandbox: 5/5 Loops Closed + v13.885 Sign Correction

**Date:** 2026-10-01
**Track:** Sandbox (our Lane B exploratory track)
**Status:** [N] numerical; [I]/assumption for RH-per-character; [I]/[O] structural
**Authorization:** Jeremy, 2026-10-01 ("yes please")
**Predecessors:** v13.885 (χ₁₂ loop), v13.888 (universality), v13.889 (β loop)

---

## 5/5 loops closed [N]

The χ₃ and χ₅ explicit-formula loops are closed. All five probed
L-functions now track:

| L-function | zeros | block-500 | probe rate (v13.888) |
|------------|------:|----------:|---------------------:|
| ζ | 100 | 0.9995 | — |
| χ₄ (β) | 50 | 0.9976 | 15/16 |
| χ₃ | 46 | 0.9959 | 13/16 |
| χ₅ | 53 | 0.9925 | 14/16 |
| χ₁₂ | 67 | 0.9840 | 11/16 |

Details: χ₃ (odd, 46 zeros): 0.9535 pointwise → 0.9959 block-500 → 0.9996
block-1000; residual std 12.94 vs true 42.91. χ₅ (even, 53 zeros): 0.9469
pointwise → 0.9925 block-500 → 0.9990 block-1000; residual std 13.79 vs
true 42.88. Both show systematic convergence (half→full zeros improves
everywhere). No failures.

The "cleaner probe → tighter loop" pattern holds broadly (best probe χ₄ →
best loop; worst probe χ₁₂ → worst loop) but not strictly: χ₃ (13/16)
beats χ₅ (14/16) despite fewer zeros. Cause unidentified [O].

## Correction to v13.885 [D]

Re-deriving the trivial-zero contribution from the contour (reproduces the
textbook ζ formula exactly): **even** characters carry
**−(1/2)·log(1−x^{−2})**, odd characters +(1/2)·log((x+1)/(x−1)).
v13.885's χ₁₂ entry used **+**(1/2)·log(1−x^{−2}) — **wrong sign**.

Impact: numerically negligible (≤0.144 at x=2, ≤5e−5 by x=100;
correlations unaffected to 4 dp). The χ₁₂ loop result stands; only the
stated trivial-zero term's sign was wrong. The χ₅ loop in this entry used
the correct sign. v13.889 (β/χ₄, odd) is unaffected.

## Structural [I]/[O]

The compression→spectrum→explicit-formula chain is confirmed independently
in five L-worlds. It is not a ζ accident — it is the shape of the explicit
formula itself, seen through compression. The D12 instance (χ₁₂) factors
through χ₃, χ₄ (v13.888).

## Explicitly NOT claimed

- **No GRH.** RH-per-character was an *input assumption* [I] throughout.

## Files (sandbox)

- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/chi3_explicit_wave.npz`
- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/chi3_explicit_overlay.png`
- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/chi5_explicit_wave.npz`
- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/chi5_explicit_overlay.png`
- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/five_loops_summary.png`

---

**Creed check:** The cone selects L-zero spectra via twisted compression in
all five L-worlds tested, and every explicit-formula loop closes. The
v13.885 sign error is corrected on the record. Shown [N]; the *why* is now
under derivation (selector theory in progress).
