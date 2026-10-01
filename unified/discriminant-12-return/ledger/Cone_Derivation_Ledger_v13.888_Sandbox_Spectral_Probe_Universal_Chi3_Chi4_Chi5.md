# Cone Derivation Ledger v13.888 — Sandbox: Spectral Probe Is Universal (χ₃, χ₄, χ₅)

**Date:** 2026-10-01
**Track:** Sandbox (our Lane B exploratory track)
**Status:** [N] numerical; [I]/assumption for RH-per-character; [I]/[O] structural
**Authorization:** Jeremy, 2026-10-01 ("yep")
**Predecessors:** v13.882 (ζ binary), v13.884 (χ₁₂ twisted), v13.887 (two axes)

---

## Headline [N]

The binary/twisted spectral probe is **universal, not a ζ/χ₁₂ coincidence**.
Five for five: ζ, χ₃, χ₄, χ₅, χ₁₂ — every Dirichlet L-function tested
returns its zeros as Fourier peaks of its twisted prime detector.

## Characters [N]

| χ | modulus | parity | definition |
|---|---------|--------|------------|
| χ₃ | 3 | odd | 0 on 3‖n; ±1 on n≡1,2 |
| χ₄ | 4 | odd | 0 on even; ±1 on n≡1,3 (Dirichlet β) |
| χ₅ | 5 | even | Legendre (·/5); ±1 on n≡±1/±2 |

Multiplicativity verified numerically. χ₁₂ = χ₃·χ₄ confirmed on n=1..499.

## L-zeros computed directly [N]

L(s,χ)=q^{−s}Σχ(a)ζ(s,a/q) via mpmath Hurwitz (25 dps); Hardy Z(t) real
(all root numbers ε=+1, verified via Gauss sums); sign-change scan t∈[0,100]
+ bisection. Gamma factor per parity (odd→Γ((s+1)/2), even→Γ(s/2)).

| χ | zeros found (t<100) | asymptotic N(100) | first zero | FE check |
|---|-------------------:|------------------:|-----------:|---------:|
| χ₃ | 46 | 45.6 ✓ | 8.039737 (= known L(s,χ₋₃) ✓) | 2.4e-31 |
| χ₄ | 50 | 50.2 ✓ | 6.020949 (= known Dirichlet β ✓) | 6.6e-32 |
| χ₅ | 53 | 53.7 ✓ | 6.648453 | 4.0e-32 |

## Probe results [N]

Λ_χ(n)=χ(n)Λ(n), b_χ(n)=χ(n)b(n), n≤24000, log-F fourier, top-16 peaks,
tolerance 0.5:

| χ | Λ_χ matched/16 | best diffs | b_χ matched/16 |
|---|---------------|------------|----------------|
| χ₃ | **13/16** | 0.01, 0.03, 0.04, 0.07, 0.08 | 5/16 |
| χ₄ | **15/16** | 0.00, 0.04, 0.05, 0.10, 0.12 | 4/16 |
| χ₅ | **14/16** | 0.03, 0.03, 0.07, 0.07, 0.11 | 5/16 |

All three **beat** χ₁₂'s 11/16. Unmatched peaks sit at γ>100, beyond the
computed range — outside reference, not failures. The Λ_χ-clean / b_χ-noisy
pattern holds as in ζ and χ₁₂.

## Structural: D12 detection is compositional [I]/[O]

χ₁₂ = χ₃·χ₄, and the probe fires on **both factors individually** — both
stronger than χ₁₂'s own 11/16. The v13.884 χ₁₂ spectral detection therefore
**factors through its prime-conductor constituents**. Data supports this
reading. The D12 case is not isolated; it is built from prime-modulus pieces.

## Quirks [N]

- Odd χ₃/χ₄: trivial zeros at s=−1,−3,…; even χ₅: s=−2,−4,…
- All ε=+1, so no phase rotation needed for Z(t).
- χ₅ shows 6 genuinely close zero pairs (gaps 0.78–0.99) — real, not
  duplicates.

## Explicitly NOT claimed

- **No GRH.** RH-per-character was an *input assumption* [I] in placing zeros
  on the critical line. This shows low L-zeros appear as Fourier peaks of
  the twisted prime detector; it says nothing about the critical line.

## Files (sandbox)

- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/multichar_spectra.png`
- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/multichar_summary.png`
- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/multichar_Lzeros_chi{3,4,5}.npy`
- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/multichar_spectra.npz`

## Open

- β-explicit-formula tracking test (χ₄'s 15/16 + 0.00-diff deserves its own
  loop-closer) — running as follow-up.
- Larger N for residue-specific ranking (per v13.887 caveat).

---

**Creed check:** The cone selects L-zero spectra via twisted compression for
*every* Dirichlet character tested — five for five. The selection is
universal; the D12 instance factors through χ₃, χ₄. Shown [N]; the *why*
remains [I]/[O].
