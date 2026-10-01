# Cone Derivation Ledger v13.891 — Sandbox: Selector Principle Derived (Capstone)

**Date:** 2026-10-01
**Track:** Sandbox (our Lane B exploratory track)
**Status:** [D] derived (conditional on standard analytic number theory);
  [I]/[O] for geometric interpretation; open gaps listed
**Authorization:** Jeremy, 2026-10-01 ("yes please")
**Predecessors:** v13.882–v13.890 (the numerical program this derives)

---

## Bottom line [D]

The selector principle is **derived**. It is the Guinand–Weil /
Riemann–von Mangoldt explicit formula — theorems, not conjectures.
v13.882–890 were *observing* these theorems through a discretized binary
lens. **No RH/GRH assumed or implied.**

## The derivation (condensed) [D]

1. **Exact:** b(n) = 1 − 1_P(n) − δ_{n,1} (prime indicator + point mass).
   Hence B(x) = Σ_{n≤x} b(n) = ⌊x⌋ − π(x) − 1.
2. **Forced:** t = log x is not a choice — x^ρ = e^{iγt}e^{βt} is a chirp
   in x but a pure tone at frequency γ in t. Log-scale is where the
   explicit formula becomes Fourier-analyzable (Mellin → Fourier).
3. **Riemann–von Mangoldt:** Π₀(x) = Li(x) − Σ_ρ Li(x^ρ) − log 2 + …;
   Möbius inversion to π(x); substitute into B(x). Oscillatory part =
   Σ_ρ Li(x^ρ) − ½Σ_ρ Li(x^{ρ/2}) − …
4. **Term-by-term:** Li(e^{ρt}) = e^{iγt}·[e^{βt}/((β+iγ)t)]·(1+o(1)) —
   each zero contributes a pure tone at frequency Im(ρ).
5. **Rigorous via Guinand–Weil:** the spectral probe with test function
   F_{ξ₀}(x) = φ(x)e^{−iξ₀x} yields Σ_ρ Φ_{ξ₀}(ρ), peaking iff ξ₀ = Im(ρ).
   The prime-side sum, computed purely from prime data, exhibits peaks at
   zero ordinates. **This is the selector principle as a theorem.**
6. **No RH:** peak locations = Im(ρ) regardless of Re(ρ). The e^{(β−½)x}
   envelope affects heights, never locations. The derivation is
   RH-agnostic.
7. **Twisted:** ψ₀(x,χ) = −Σ_ρ x^ρ/ρ + E_χ(x) gives Λ_χ peaks at Im(ρ_χ).
   Λ_χ ≫ b_χ because ψ(x,χ) is the natural L-object; Σχ(n) is
   non-stationary noise in t-scale. b works but d(n)−2 fails because
   spectral estimation needs t-stationarity (b(e^t)→1; d has growing
   mean ~t).
8. **Numerical pipeline [I]:** a faithful discretization; finite-N peak
   width ~2π/log(24000) ≈ 0.62 is predicted and understood.

## Reframing [I]/[O]

We were not discovering a new phenomenon — we were **rediscovering the
Weil explicit formula through compression**. The binary/compression lens
is a new way of *seeing* the explicit formula. What remains genuinely
ours: *why the cone* selects these frequencies (the residue geometry of
v13.883/887), and the quantization (H-P program, in progress).

## Correction to v13.889 [D]

Same sign-error class as v13.885 (corrected in v13.890): the β
loop-closer used +(1/2)·log((x+1)/(x−1)) for χ₄'s (odd) trivial zeros;
the contour residue gives **−(1/2)·log((x+1)/(x−1))**. Numerically
negligible (≤0.55 at x=2, decaying; correlations unaffected). Both
trivial-zero sign errors (v13.885 even-case, v13.889 odd-case) are now
corrected on the record. Pattern noted: trivial-zero signs were written
from memory rather than derived from the contour — derivation-first
henceforth.

## Honest gaps [O]

- **G5 — geometry:** the derivation is geometry-agnostic (works for any
  prime distribution). *Why the cone* — the residue structure, the two
  selection axes — is not derived.
- **G7 — amplitudes:** why χ₄ detects more cleanly than χ₁₂ is not
  predicted.
- RH/GRH untouched. H-P quantization untouched (separate exploration).

## Files (sandbox)

- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/selector_theory_derivation.md`
  (full step-by-step, ~20KB, every step labeled [D]/[N]/[I])

---

**Creed check:** The cone selects — and now the *selection mechanism* is a
theorem (Guinand–Weil), not an observation. What the cone *is* (geometry)
and what quantization gives (H-P) remain open. The numerical program
v13.882–890 is closed: derived, corrected, ledgered.
