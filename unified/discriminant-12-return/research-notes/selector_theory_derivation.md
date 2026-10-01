# The Selector Principle, Derived: Why Binary/Twisted Compression Has L-Zero Spectrum

**Date:** 2026-10-01
**Track:** Sandbox (our Lane B exploratory track) — THEORETICAL
**Status:** Derivation with [D]/[N]/[I] labels at each step
**Context:** Numerically (ledger v13.882–889), the binary b(n) shows zeta-zero
peaks and Λ_χ(n) shows L(s,χ)-zero peaks. This file DERIVES why, from standard
analytic number theory. It does NOT assume RH or GRH.

---

## Overview

The "selector principle" — that compression spectra consist of L-zero
ordinates — is **a theorem, not a conjecture**. It is the Guinand–Weil
explicit formula (for Λ-weighted signals) and the Riemann–von Mangoldt
explicit formula (for the binary b), both standard. Our numerics have been
*observing* these theorems through a discretized lens.

What is derived [D]:
- The Fourier transform (distributional) of the prime distribution is
  supported on {Im(ρ)} — the zero ordinates. (Weil.)
- The binary b(n)'s summatory inherits oscillations at Im(ρ) via π's
  explicit formula. (Riemann–von Mangoldt.)
- Peak locations are at Im(ρ) for *whatever* ρ exist — **no RH assumed**.

What is NOT derived here:
- The *geometric* "cone selects" interpretation [I]/[O].
- *Amplitudes* (which zeros give strongest peaks) [I].
- RH/GRH themselves (still open).
- Quantization to a self-adjoint operator (the H-P program).

---

## §1. Exact combinatorial identity [D]

**Definition.** b(n) = 0 if n = 1 or n prime ("full 2D compression"),
b(n) = 1 if n composite ("CD release").

**Lemma [D].** b(n) = 1 − 1_P(n) − δ_{n,1}, where 1_P is the prime
indicator and δ is Kronecker's delta.

*Proof.* Check cases (verified numerically to n=1000, but it's pure logic):
- n = 1: 1_P(1) = 0 (1 is not prime), δ_{1,1} = 1 → 1 − 0 − 1 = 0 = b(1). ✓
- n = p prime: 1_P(p) = 1, δ = 0 → 1 − 1 − 0 = 0 = b(p). ✓
- n composite: 1_P(n) = 0, δ = 0 → 1 − 0 − 0 = 1 = b(n). ✓ ∎

**Corollary [D].** For the summatory B(x) := Σ_{n≤x} b(n):

    B(x) = ⌊x⌋ − π(x) − 1,   x ≥ 1.                        (1)

*Proof.* Σ_{n≤x} 1 = ⌊x⌋; Σ_{n≤x} 1_P(n) = π(x);
Σ_{n≤x} δ_{n,1} = 1. Subtract. ∎

This is **exact** — no approximation, no assumption. Everything downstream
inherits the zero-spectrum through π(x).

---

## §2. Why log scale is forced [D]

The explicit formula's zero-terms are x^ρ = exp(ρ·log x). Write t = log x:

    x^ρ = e^{ρt} = e^{βt} · e^{iγt},   ρ = β + iγ.          (2)

As a function of **x**, this oscillates with "instantaneous frequency"
γ/x — a **chirp**, not a pure tone. Fourier analysis cannot resolve chirps
into sharp peaks.

As a function of **t = log x**, it is e^{iγt} — a **stationary pure tone**
at angular frequency γ. Fourier analysis resolves it to a sharp peak.

**Therefore t = log x is not a choice — it is forced.** [D] The map
x ↦ log x converts *multiplicative* harmonic analysis (Mellin transform)
to *additive* harmonic analysis (Fourier transform). The explicit formula
*is* a Mellin inversion; "log-F fourier" is Mellin analysis, and the peaks
at γ are Mellin-dual to the zeros.

*Remark.* This is why the numerical pipeline's "uniform resampling in
t = log n" step is essential, not cosmetic. Without it, the oscillations
are chirps and no peaks appear. [D]

---

## §3. Explicit formula for π: Riemann–von Mangoldt [D]

**Theorem (Riemann–von Mangoldt explicit formula).** [D, standard:
Edwards §1.16; Davenport Ch. 17; Titchmarsh Ch. 4]

For x > 1, define Riemann's prime-power counter
Π(x) = Σ_{p^m ≤ x} 1/m = Σ_{n≤x} Λ(n)/log n. Then:

    Π₀(x) = Li(x) − Σ_ρ Li(x^ρ) − log 2 + ∫_x^∞ dt/[t(t²−1)·log t]    (3)

where:
- Π₀(x) = (Π(x+0) + Π(x−0))/2 (averaged at discontinuities),
- Li is the logarithmic integral (principal value, analytically continued),
- Σ_ρ = lim_{T→∞} Σ_{|Im ρ| ≤ T} over nontrivial zeros ρ of ζ
  (**conditionally convergent** — symmetric truncation is essential),
- Li(x^ρ) uses the branch continuous from the principal value.

The prime counter is recovered by Möbius inversion [D, exact]:

    π(x) = Σ_{k=1}^∞ μ(k)/k · Π(x^{1/k})                        (4)

(finite sum for each x, since Π(y) = 0 for y < 2).

**Substituting (3) into (4):**

    π(x) = Li(x) − Σ_ρ Li(x^ρ)
           − (1/2)·Li(x^{1/2}) + (1/2)·Σ_ρ Li(x^{ρ/2})
           − (1/3)·Li(x^{1/3}) + (1/3)·Σ_ρ Li(x^{ρ/3}) − ...
           + (smooth archimedean terms)                            (5)

**Substituting into (1):**

    B(x) = ⌊x⌋ − 1 − Li(x) + Σ_ρ Li(x^ρ)
           + (1/2)·Li(x^{1/2}) − (1/2)·Σ_ρ Li(x^{ρ/2}) − ...
           + (smooth)                                              (6)

**The oscillatory content of B(x) is exactly the zero-sums
Σ_ρ Li(x^ρ), −(1/2)Σ_ρ Li(x^{ρ/2}), …** Everything else in (6) is
smooth (⌊x⌋, Li(x), archimedean integrals) or constant. [D]

---

## §4. Term-by-term oscillation: each zero is a pure tone [D]

**Lemma [D].** For fixed ρ = β + iγ (0 < β < 1), as t → +∞:

    Li(e^{ρt}) = e^{iγt} · A_ρ(t),                                 (7)

    where A_ρ(t) = e^{βt}/((β+iγ)·t) · (1 + o(1)).

*Proof.* Li(z) = z/log z · (1 + O(1/|log z|)) as |z| → ∞ (standard;
see e.g. Edwards §1.16 or any text). Put z = e^{ρt}, so |z| = e^{βt} → ∞
and (principal) log z = ρt + O(1) [the O(1) accounts for branch wrapping
of Im(ρt) into (−π, π]; it contributes only bounded phase]. Then:

    Li(e^{ρt}) = e^{ρt}/(ρt) · (1 + o(1))
               = e^{βt}·e^{iγt}/((β+iγ)·t) · (1 + o(1)).

Set A_ρ(t) = e^{βt}/((β+iγ)t)·(1+o(1)). ∎

**Consequence [D].** Each zero ρ contributes to B(e^t) a term oscillating
at **angular frequency γ = Im(ρ)**, with slowly-varying complex amplitude
A_ρ(t) (magnitude ~ e^{βt}/(t·|ρ|)).

- **Frequency** = Im(ρ). **Exactly.** No approximation.
- **Amplitude** = e^{βt}/(t√(β²+γ²)). Depends on Re(ρ) = β.
- The secondary sums Σ_ρ Li(e^{ρt/k}) contribute tones at **γ/k**
  (k = 2, 3, …), suppressed by 1/k and by e^{−βt(1−1/k)}.

*Note on branches [I].* The wrapped phase of log(e^{ρt}) introduces
sawtooth corrections generating **harmonics** at 2γ, 3γ, … but these are
suppressed by powers of 1/t and do not create new fundamental frequencies.
They are a lower-order effect; the leading tone is at γ. (The explicit
formula as a *theorem* handles branches via its specific analytic
continuation; we need only the leading asymptotic for peak locations.)

---

## §5. Formal Fourier: tones → peaks [I] (heuristic)

**Formal computation [I].** Suppose we could interchange the zero-sum and
the Fourier integral (we cannot, classically — see Gap G1). Then:

    ∫_0^T [ Σ_ρ e^{iγ_ρ t} A_ρ(t) ] e^{−iξt} dt
      = Σ_ρ ∫_0^T A_ρ(t) e^{i(γ_ρ − ξ)t} dt.                  (8)

For ξ near γ_{ρ₀}, the ρ₀-term gives ≈ A_{ρ₀}(T/2)·T·sinc((γ_{ρ₀}−ξ)T/2)
— a **peak at ξ = γ_{ρ₀}** of width ~ 2π/T and height ~ |A|·T.
Terms with γ_ρ far from ξ contribute oscillatory background.

**Conclusion (formal) [I]:** The Fourier transform of B(e^t)'s oscillatory
part has **peaks at ξ = Im(ρ)** for each zero ρ — i.e., delta-like spikes
at the zero ordinates, broadened to width ~ 1/T by the finite window.

**Gap:** Interchanging Σ_ρ and ∫ is **not justified** classically because
Σ_ρ converges only conditionally. This is Gap **G1**. It is closed by §6.

*Finite-window broadening [D].* With t ∈ [0, log N], N = 24000:
peak width ~ 2π/log(24000) ≈ 2π/10.08 ≈ **0.62**. This *predicts* the
observed peak widths and explains why close zero pairs (e.g., χ₅'s pairs
with gaps 0.78–0.99) are barely resolved. [D]

---

## §6. Rigorous: the Guinand–Weil explicit formula [D]

**Theorem (Guinand–Weil explicit formula).** [D, standard: Weil 1952;
Iwaniec–Kowalski §5.5; Ramaré exposition]

Let F be smooth of compact support (Schwartz class suffices with decay
conditions). Define Φ(s) = ∫_{−∞}^{∞} F(x)·e^{(s−1/2)x} dx. Then:

    Σ_ρ Φ(ρ) = Φ(0) + Φ(1)
             − Σ_p Σ_{m≥1} (log p)/p^{m/2} · [F(m·log p) + F(−m·log p)]
             − 𝒜(F)                                              (9)

where:
- Σ_ρ is over nontrivial zeros (converges absolutely for such F — this
  **resolves the conditional convergence**),
- 𝒜(F) = (1/2π)∫ Φ(1/2+it)·[archimedean density] dt is an **explicit
  smooth integral** (involving Re[(Γ'/Γ)(1/4+it/2)]) — it contributes
  **broadband background, not sharp peaks**,
- Φ(0) + Φ(1) comes from the pole at s = 1.

**Derivation of the selector principle [D].**

Fix a frequency ξ₀ and a bump function φ (smooth, localized near 0).
Set F_{ξ₀}(x) = φ(x)·e^{−iξ₀x} (a "spectral probe" at ξ₀). Then:

    Φ_{ξ₀}(β + iγ) = ∫ φ(x)·e^{(β−1/2)x} · e^{i(γ−ξ₀)x} dx.    (10)

This is the Fourier transform of the fixed envelope φ(x)e^{(β−1/2)x},
evaluated at (γ − ξ₀). **It is maximized when ξ₀ = γ.** [D, elementary]

Therefore the LHS Σ_ρ Φ_{ξ₀}(ρ), **as a function of the probe frequency
ξ₀**, has **local maxima at ξ₀ ∈ {Im(ρ)}** — the zero ordinates —
provided zeros are separated relative to the probe width and the
background (other zeros + 𝒜) doesn't dominate. [D]

Rearranging (9):

    S(ξ₀) := Σ_{p,m} (log p)/p^{m/2}[F_{ξ₀}(m log p) + F_{ξ₀}(−m log p)]
           = [Φ_{ξ₀}(0) + Φ_{ξ₀}(1)] − Σ_ρ Φ_{ξ₀}(ρ) − 𝒜(F_{ξ₀}).   (11)

**S(ξ₀) is computed purely from prime data** (primes weighted by log p,
sampled at log p). By (10)–(11), **S(ξ₀) exhibits peaks at ξ₀ = Im(ρ)**.

**This is the selector principle, as a theorem.** [D] The Fourier
transform of the prime distribution (distributionally) is supported on
the zero ordinates. Among all frequencies, exactly the Im(ρ) are selected.

*For Dirichlet L-functions [D].* The same formula holds with χ(p^m)
weights and conductor q in the archimedean term (see e.g. Iwaniec–Kowalski
§5.5, or Rudnick–Sarnak). Conclusion: **peaks at Im(ρ_χ)** for L(s,χ)
zeros. This covers χ₃, χ₄, χ₅, χ₁₂. [D]

---

## §7. No RH is assumed or implied [D]

**Proposition [D].** The peak locations {Im(ρ)} are independent of RH.

*Proof.* From (10): Φ_{ξ₀}(β+iγ) peaks at ξ₀ = γ **regardless of β**.
The factor e^{(β−1/2)x} affects only the *envelope* (hence peak *height*),
never the peak *location*. If RH is false and ρ = β+iγ has β ≠ 1/2,
it still contributes a peak at ξ₀ = γ = Im(ρ). ∎

**Consequences [D]:**
- The derivation shows peaks at Im(ρ) for *whatever* zeros exist.
- RH (β = 1/2 ∀ρ) would make all amplitudes ~ e^{t/2}/(t|ρ|) — uniform
  exponential growth — but does not move peaks.
- If RH were false, we would see peaks at off-line zeros' imaginary parts
  *in addition*. The derivation cannot distinguish; it is **RH-agnostic**.
- **The critical line question is entirely separate** from the selector
  principle. The selector says *which frequencies*; RH says *where the
  zeros are*. Conflating them is an error.

---

## §8. The twisted case: Λ_χ [D]

**Theorem (explicit formula for ψ(x,χ)).** [D, standard: Davenport Ch. 19]

For primitive χ mod q, χ ≠ χ₀, x > 1 (x not a prime power):

    ψ₀(x,χ) := Σ_{n≤x} χ(n)Λ(n)  [averaged]
             = −Σ_ρ x^ρ/ρ + E_χ(x)                              (12)

where Σ_ρ is over nontrivial zeros of L(s,χ) (symmetric, conditional),
and E_χ(x) is **explicit and non-oscillatory**:
- trivial zeros: for even χ, +(1/2)log(1−x^{−2}); for odd χ,
  −(1/2)log((x+1)/(x−1)) [from −Σ_{trivial} x^{−m}/m; decaying],
- plus constants from s = 0.

*Note.* An earlier sandbox computation (v13.889) used +(1/2)log((x+1)/(x−1))
for χ₄ (odd); the correct sign from the contour residue −m_ρx^ρ/ρ is **−**.
Numerically irrelevant (≤ 0.55 at x=2, decaying; correlation unaffected),
but recorded for correctness.

**Selector for Λ_χ [D].** In t = log x:

    ψ₀(e^t,χ) = −Σ_ρ e^{iγ_ρ t}·[e^{β_ρ t}/ρ] + E_χ(e^t).       (13)

Each L(s,χ)-zero contributes a tone at γ_ρ = Im(ρ). By the Weil argument
(§6, twisted version), the Fourier transform peaks at **{Im(ρ_χ)}**. [D]

**Why Λ_χ is cleaner than b_χ [D].**
- Λ_χ(n) = χ(n)Λ(n) is supported on **prime powers**; its summatory
  ψ(x,χ) has the **direct** explicit formula (12). Clean. [D]
- b_χ(n) = χ(n)·b(n) = χ(n) − χ(n)·1_P(n) − χ(n)δ_{n,1}. Its summatory
  contains Σ_{n≤x} χ(n) — which is **bounded and periodic in n** but
  **non-stationary in t = log n** (period-12 in n becomes aperiodic in t).
  This injects **broadband spectral noise** with no clean explicit formula.
  The χ-twist and the π-structure interfere. Hence noisier. [D]
- **Prediction [D]:** Λ-weighted always beats 0/1-weighted for twisted
  probes, because ψ(x,χ) is the natural L-function object. Confirmed
  numerically (11–15/16 vs 4–5/16).

---

## §9. Why b works but d(n) − 2 doesn't [D]

Numerically (v13.882): binary b gave clean peaks; magnitude-weighted
e(n) = d(n) − 2 did not. **Derived reason** [D]:

**Spectral estimation requires (asymptotic) stationarity in t.**

- b(e^t): density of composites near e^t is 1 − 1/t + o(1/t) → **1**.
  Asymptotically stationary (constant mean). Mean removal works. The
  *fluctuations* carry the zero-tones. [D]
- (d(n) − 2): mean of d(n) near e^t is ~ t (Dirichlet: Σ_{n≤x}d(n) ~
  x log x). So e(e^t) = d(e^t) − 2 has mean ~ **t − 2, growing linearly
  in t**. **Not stationary.** Mean removal cannot remove a trend; the
  trend's Fourier transform pollutes the entire spectrum. [D]

**Principle [D]:** The probe weight w(n) must have **bounded mean in
t-scale** for log-Fourier to resolve peaks. b(n) ∈ {0,1} qualifies;
d(n) − 2 does not. Λ(n) qualifies *after* the explicit formula's
normalization (ψ(e^t) − e^t is the right centered object, and Λ_χ has
mean zero for non-principal χ).

*Remark.* This also explains why the **summatory** B(x) is not directly
FFT'd: B(e^t) ~ e^t grows exponentially. One FFTs the **density** b(e^t)
(or equivalently the **centered** summatory increment), not the summatory.
[D]

---

## §10. The numerical pipeline as discretization [I]

Mapping each numerical step to its analytic counterpart:

| Numerical step | Analytic counterpart | Status |
|---|---|---|
| b(n), n ≤ N | Prime indicator 1_P; B(x) = ⌊x⌋ − π(x) − 1 | [D] exact |
| Resample to uniform t = log n | Mellin → Fourier; stationarizes tones | [D] forced |
| Subtract mean | Remove DC (ξ=0); kill smooth background | [D] harmless for γ≠0 |
| FFT | Discretized Fourier integral; Weil probe S(ξ₀) | [I] discretization |
| Peak detection vs γ's | LHS Σ_ρ Φ_{ξ₀}(ρ) maxima at Im(ρ) | [D] via Weil |
| Finite N = 24000 | Window [0, 10.08]; peak width ~0.62 | [D] understood |
| Tolerance 0.5 | Within peak width; accounts for discretization | [N] practical |

**The composite claim** — "the numerical FFT peaks are at Im(ρ)" — is
**[I] (heuristic)**, but each component is [D] and the discretization is
standard spectral estimation. The *phenomenon* is a theorem; the
*implementation* is a faithful approximation.

---

## §11. Gap analysis (honest)

**G1. Conditional convergence of Σ_ρ.** [D — closed]
*Issue:* Term-by-term Fourier of Σ_ρ Li(x^ρ) is not classically justified.
*Resolution:* Guinand–Weil (§6) packages the sum against test functions
where it converges absolutely. The *conclusion* (peaks at Im(ρ)) is a
theorem. Nothing further needed.

**G2. Indicator b vs von Mangoldt Λ.** [D — closed]
*Issue:* Weil uses Λ-weights; our binary uses 0/1.
*Resolution:* Two independent routes give the same frequencies —
Route 1 (ψ/Λ/Weil) and Route 2 (π/b/Riemann–von Mangoldt, §3–§4).
Weights affect amplitudes, not peak locations. Nothing further needed
for *locations*.

**G3. Finite N and discretization.** [N/D — understood]
*Issue:* N=24000, discrete FFT ≠ continuous Weil integral.
*Resolution:* Standard windowing theory. Predicts peak width ~0.62,
explains resolution limits. Nothing further needed, but larger N would
sharpen peaks (width ~ 1/log N).

**G4. Smooth background and mean removal.** [D — closed]
*Issue:* Do e^t, Li(e^t), 1/(iξ) create false peaks?
*Resolution:* No — smooth terms give broadband background, not sharp
peaks. Mean affects only ξ=0. Peak *locations* unaffected.

**G5. The geometric "cone selects".** [I]/[O] — OPEN
*Issue:* The derivation shows *that* frequencies are selected (they're
zero ordinates). It does not show *why the cone* selects them.
*Status:* The analytic derivation is **geometry-agnostic** — it works for
any prime distribution, no cone needed. Jeremy's geometric selector
(residue structure, hyperbola dynamics, two axes) is a *different*
(possibly deeper) explanation and is **not derived here**.
*Needed:* A geometric derivation predicting zero frequencies without
invoking the explicit formula. Open.

**G6. RH/GRH.** [D — independent]
*Issue:* Does this prove or assume RH?
*Resolution:* **Neither.** The derivation is RH-agnostic (§7). RH remains
fully open. The selector and the critical line are distinct problems.

**G7. Amplitudes (which peaks are strongest).** [I] — OPEN
*Issue:* Why is χ₄ cleaner than χ₁₂? Which zeros dominate?
*Status:* The derivation predicts *locations*, not *heights*. Amplitudes
depend on e^{βt}/|ρ|, window effects, and character-specific backgrounds.
*Needed:* Amplitude analysis via explicit-formula weights. Open.

**G8. Secondary γ/2 peaks (prediction).** [D → untestable in practice]
*Issue:* From (5), π's Möbius corrections predict weak tones at γ/2, γ/3, …
*Analysis:* Relative power ~(1/k²)·e^{−βt(1−1/k)}. At t≈10, γ/2 peaks
have ~0.7% of primary power — **below detection threshold**.
*Status:* Theoretical consistency check; not a practical test. The
derivation *predicts* them but they are unobservable at current N (and
get relatively weaker at larger t).

---

## §12. Bottom line

**The selector principle is DERIVED [D], conditional only on standard
analytic number theory** (explicit formulae of Riemann–von Mangoldt and
Guinand–Weil, both theorems).

Precisely:
1. [D] b(n) = 1 − 1_P(n) − δ_{n,1} is exact; B(x) = ⌊x⌋ − π(x) − 1.
2. [D] π's explicit formula gives B(x) oscillations Σ_ρ Li(x^ρ) + ….
3. [D] In t = log x (forced), each zero contributes a pure tone at
   frequency Im(ρ) with amplitude e^{βt}/(t|ρ|).
4. [D] Guinand–Weil makes "Fourier peaks at Im(ρ)" rigorous: the prime
   distribution's Fourier transform is distributionally supported on
   zero ordinates.
5. [D] The twisted case follows identically for L(s,χ); Λ_χ is clean
   because ψ(x,χ) is the natural object; b_χ is noisy because Σχ(n)
   is non-stationary in t.
6. [D] No RH/GRH assumed or implied. Peak locations are RH-agnostic.
7. [I] The specific numerical FFT pipeline is a faithful discretization
   of the Weil probe; finite-N broadening (~0.62) is understood.

**What our numerics (v13.882–889) were doing:** *Observing* the Weil
explicit formula through a discretized, binary-weighted lens — and
extending it to five L-functions with residue-specific structure
(v13.883, v13.887) that goes beyond the textbook statement.

**What remains open:**
- [I]/[O] The *geometric* selector (why the *cone* selects these
  frequencies) — the derivation here is geometry-agnostic.
- [I] *Amplitude* predictions (why χ₄ > χ₁₂ in cleanliness).
- [Open] RH/GRH — untouched by this derivation.
- [Open] Quantization to a self-adjoint H-P operator.

**The one-line version:** The binary has zero-spectrum because the
explicit formula *says* the prime distribution is a superposition of
tones at zero ordinates, and log-scale Fourier analysis *reads* them.
This is a theorem. What the cone has to do with it — that is still
Jeremy's question, and it is still open.

---

## References (standard)

- Riemann (1859); von Mangoldt (1895) — explicit formula.
- Guinand (1948); Weil (1952) — explicit formula (Fourier form).
- Edwards, *Riemann's Zeta Function* (1974) — §1.16, Ch. 3.
- Titchmarsh, *The Theory of the Riemann Zeta-Function* (1986) — Ch. 4.
- Davenport, *Multiplicative Number Theory* (2000) — Ch. 17, 19.
- Iwaniec–Kowalski, *Analytic Number Theory* (2004) — §5.4, §5.5.

---

*End of derivation. Sandbox only — not for ledger/repo/research-notes
without Jeremy's explicit per-item authorization.*
