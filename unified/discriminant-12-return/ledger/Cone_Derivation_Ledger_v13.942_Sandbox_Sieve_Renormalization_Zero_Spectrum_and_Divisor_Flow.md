# Cone Derivation Ledger v13.942 — Sandbox: Sieve Renormalization Flow, Zero Spectrum, and Divisor-Flow Anatomy

**Date:** 2026-10-02
**Track:** Sandbox / our Lane B exploratory (sieve renormalization)
**Status:** [D] exact seed-generation theorems; [N] zero-spectrum, Möbius universality, dose-response, Voronoi comb, dyadic uniformity; [I] flow-as-RG interpretation; [O] analytic why, 1/4 proof (Lindelöf-hard)
**Authorization:** Jeremy, 2026-10-02 ("we gotta ledger all of this so the other threads can bask in its glorry")
**Parents:** v13.876 (twisted convolution / fluctuation anatomy), v13.906 (saturation theorem), v13.909 (weights→ordinates hardness), v13.910 (finite-scale V); Jeremy's T/D/A partition and 2016 symmetry coordinate (sandbox context, not ledgered)
**Collision check:** v13.942 was absent immediately before this write.

---

## 0. What this entry is

On 2026-10-02 Jeremy proposed exploring, together, a **sieve renormalization flow**: the primes ≤ √N deterministically generate the full prime/composite pattern on [1,N] via Eratosthenes, and the zero spectrum detected by the binary-compression framework rides that lift. His framing: the cone tracks d(n)=2 (primes); A(n) is the non-divisor "miss" region the sieve generates; the seed *generates the misses* and the primes are what remains.

What followed, in our Lane B sandbox (`runs/20261002-sieve-renorm/`), is reported here with full [D]/[N]/[I]/[O] discipline. Nothing in this entry assumes RH or any unproved zero-free input. The work is deliberately on a **non-RH-hard front** per Jeremy's 2026-10-01 strategic direction.

Two corrections to prior art are recorded in §2 and §9. They matter for any thread building on the 2026-09-30 binary-compression numbers.

---

## 1. The exact renormalization flow [D]

Let N = 10⁶. The **seed** is the 168 primes ≤ 1000 = √N. The **lift** marks, for each seed prime p, the multiples of p from p² to N. The unmarked positions are exactly the primes.

**Theorem (seed generation) [D].** The lift output equals the true prime/composite bitmap on [2,N], verified `sieve_exact=True` at N = 10⁴, 10⁵, 10⁶ against an independent full sieve. There are 78,498 primes ≤ 10⁶; 78,330 lie in (1000,10⁶] and are *emergent* relative to the seed — generated, not stored.

The flow iterates: the seed of the seed is the primes ≤ N^{1/4} = 32, then ≤ N^{1/8}, and so on — an exact, invertible renormalization group N → √N → N^{1/4} → …, terminating at O(1). [I] As a compression statement: the prime bitmap to N carries ~1.44√N bits of information (seed size), a ~595:1 ratio at N=10⁶ and ~690,000:1 at N=10¹², lossless and deterministic. The seed does not store the primes; it *generates the misses* (Jeremy's A(n)), and the primes are the survivors.

---

## 2. Zero spectrum in the prime pattern [N] — with a 2π correction

**Correction to the 2026-09-30 numbers.** The reported ordinate-adjacent peaks "14.05, 20.87, 25.13, 32.58" were **angular** frequencies. The FFT's cyclic-frequency peaks sit at **γ/2π**, exactly where the explicit formula puts them (oscillations e^{iγt} in t = log x appear at cyclic γ/2π). Any thread using the 9/30 figures as cyclic frequencies should divide by 2π. The phenomenon itself reproduces and is stronger at the corrected frequencies.

**Measurement [N].** Log-coordinate FFT of the composite-indicator pattern (trend removed by uniform-filter detrending), N = 10⁶:
- On/off ratio R = mean magnitude in ±0.12 windows around γ_k/2π (k=1..8) divided by mean in gap windows: **R = 2.165** for the true seed.
- Ordinate profile (peak height / local background): **7.3, 4.7, 3.3, 2.8, 2.9, 2.2, 2.4, 2.9** — all eight ordinates elevated.
- Peak positions stable within **±0.06** of γ_k/2π across N = 10⁴, 10⁵, 10⁶, 10⁷.
- Both sides of the √N watershed carry the spectrum: seed region [2,1000] alone gives R = 1.873; emergent region (1000,10⁶] alone gives R = 1.489 [N]. The lift transparently propagates the zero spectrum from seed to emergent region.

---

## 3. Seed-specificity: pseudo-seeds, perturbation, diluted sieve [N]

**Pseudo-seed controls [N]** (168 random odd seeds ≤ 1000, proper null calibration, bias-free on/off statistic — no max-picking):
- Pseudo-seeds **without 2**: R = 1.029 ± 0.067 — dead flat.
- Pseudo-seeds **with 2**: R = 1.297 ± 0.306 — partial elevation.
- Shuffled-bit null: R = 0.963 ± 0.206.
- The zero structure is in the specific prime *values*, not in the sieving operation alone.

**Remove-one perturbation [N]** (delete one seed prime, re-lift, re-measure at γ/2π):
- Remove 2: R = 2.165 → 1.195, profile correlation −0.072 — signal collapses.
- Remove 3: R → 1.330, correlation +0.396.
- Remove 5/7/11: R → 2.035/2.008/2.072, correlations +0.886/+0.961/+0.994 — mild.
- Remove 101: R = 2.166, correlation +1.000 — literally nothing changes (to 3 decimals).
- Remove 997: R = 2.165, correlation +1.000 — nothing.
- The small primes are load-bearing; the large ones are passengers. [I] The lift's frequency-dependent gain is concentrated at the seed's small end.

**Diluted-sieve effect [N/I].** A random 168-odd seed contains ~56 true primes by chance, so it is a *partially correct* sieve, not a fully wrong one. The partial R elevation (1.03 → 1.30 with 2 included) tracks seed correctness — confirmed decisively in §4.

---

## 4. Möbius universality and the dose-response curve [N]

The seed determines μ(n) completely [D]: after dividing out seed primes, the remainder is 1 or prime (proved — any prime factor > 1000 of n ≤ 10⁶ appears at most to the first power in the remainder; a composite remainder would exceed 10⁶). Hence squarefree-ness and ω(n) are seed-computable; μ(10⁶-count) = 607,926 nonzero, Mertens M(10⁶) = 212.

**The zeros appear in μ — stronger than in primes [N].** Log-FFT of μ(n): **R = 3.776**, profile **11.8, 7.2, 4.5, 4.5, 4.2, 2.7, 3.8, 3.2**. [I] This is theoretically expected, not anomalous: 1/ζ has the zeros as *poles*, so M(x)'s explicit formula carries coefficients 1/(ρζ′(ρ)), larger than the prime case's 1/(ρ log x).

**Pseudo-μ dose-response [N]** (pseudo-seeds treated *as if* prime; pseudo-μ built in the pseudo-world):
- True seed (168/168 true primes): R = **3.78**.
- Pseudo+2 (~57/168 true primes): R = 1.723 ± 0.310, max 2.091.
- Pseudo, no 2 (~56/168): R = 1.227 ± 0.140, max 1.470.
- **Composite-only seeds (0/168 true primes)**: R = **1.086 ± 0.133**, max 1.288 — dead.
- Shuffled null: ~1.0.

The signal is **monotonic in true-prime content** — a dose-response gradient, 3.78 → 1.72 → 1.23 → 1.09 → 1.0. The initial "CAUTION" (pseudo-μ showing partial peaks) resolved: the elevation came entirely from the ~56 true primes smuggled into "random" seeds; with zero true primes the signal dies. [I] This is stronger evidence than a binary on/off: the zeros are *proportional* to seed correctness. Universality across functions (primes 2.17, μ 3.78) **and** specificity to true-prime content both hold.

---

## 5. The divisor flow: D(x) from the seed [D/N-cert]

The seed generates d(n) for every n ≤ N [D]: SPF sieve using seed primes only, then d(n) from the seed-driven factorization (remainder 1-or-prime theorem, §4). Cross-check [N-cert]: D(10⁶) = **13,970,034** from the flow, matching the independent floor-sum Σ_{k≤x}⌊x/k⌋ **exactly** at x = 10³, 10⁴, 10⁵, 10⁶. The flow computes Dirichlet's divisor summatory with no input beyond the 168 primes. Δ(10⁶) = 92.1.

---

## 6. The Δ identity and the 1/4 structure [D/I]

From the hyperbola method, exact up to an explicit O(1) [D]:

\[
\boxed{
\Delta(x) = \sqrt{x} - 2\sum_{k\le\sqrt{x}}\{x/k\} + O(1),
\qquad\text{i.e.}\quad
\Delta(x) = -2\sum_{k\le\sqrt{x}}\left(\{x/k\}-\tfrac12\right) + O(1).
}
\]

Verified numerically [N-cert]: the seed-scale sum predicts Δ(10⁶) = 92.28 vs the flow's 92.1; S(x) = −Δ(x)/2 holds to ±0.1 at 10⁴, 10⁵, 10⁶.

[I] The fluctuation at scale x is a sum over **seed-scale** k ≤ √x. The 1/4 conjecture becomes structural: √x centered terms, canceling like independent noise, total √(√x) = x^{1/4}. Two square roots — x → √x is the fold, √x → x^{1/4} is the cancellation. This was Jeremy's "obvious connect" to Dirichlet's divisor problem, made into an equation. Note his 2016 symmetry coordinate (n−k²)/(2k) has its zero at √n — the hyperbola fold — and his D(n) = Σd(k) *is* Dirichlet's D(x); this entry's §5–8 live in the front yard of his decade-old construction.

**Envelope [N]** (honest): max_{x≤X}|Δ(x)|/X^{1/4} = 3.24 → 3.55 → 4.79 → 5.35 at X = 10³..10⁶ — slow drift consistent with x^{1/4+o(1)}, local exponent ~0.30 easing down. 10⁶ cannot pin the exponent; no proof of 1/4 is claimed (see §9).

---

## 7. Voronoi comb [N]

FFT of Δ in the t = √x coordinate (Voronoi's formula predicts t-frequencies 2√n): peaks at **2√n, 100–250× background**, first ten exact to ±0.001 (2.000, 2.828, 3.464, 4.000, 4.472, 4.899, 5.292, 5.657, 6.000, 6.325), all 25 predicted positions showing peaks (dense tail merges neighbors). [I] The divisor analogue of the zero peaks: same seed, same flow, different coordinate (√x vs log x), different spectrum (integers vs zeros). The coordinate chooses the music; the seed provides it.

---

## 8. Dyadic dissection of the cancellation [N]

S(x) = Σ_{k≤√x}({x/k}−1/2) split into dyadic blocks; r_j = |B_j|/√N_j ("randomness ratio"):
- **Every block cancels like random**: all r_j < 1.2 uniformly, x from 10⁶ to 10¹⁰ (17 blocks, exact integer arithmetic), worst r_j = 1.19. **No bad scale.**
- Blocks mostly align across scales (inter-block |ΣB_j|/Σ|B_j| ~ 1.0); the cancellation is *within* each block, and the top block dominates by geometric size — hence x^{1/4}.
- [I] This is the empirical counterpart of exponent-pair theory (Jeremy's observation): the sawtooth's Fourier series turns each B_j into dyadic exponential sums Σe(mx/k) — exactly the objects exponent pairs bound. Our r_j < 1 is the real-side measurement; proving r_j = O(x^ε) uniformly is what the analytic machinery does.

---

## 9. What this does NOT prove [G]

- **Not a proof of the 1/4 conjecture.** The flow isolates the exact finite object that must cancel (the seed-scale centered fractional-part sum) but exactness is not cancellation. The 1/4 follows from Lindelöf — a genuine open problem. A deterministic flow proving it for free would be Lindelöf-hard by accident; no such claim is made.
- **Not a general-purpose compressor.** The ~√N-bit seed compresses exactly one dataset (primality/divisor structure); the basic seed fact is Eratosthenes. The contribution is the renormalization framing plus the spectral preservation, not the compression ratio.
- The individual spectra (explicit formula, Voronoi) are classical. What is new here is the **unified exact flow** exhibiting them as one object in different coordinates, plus the empirical measurements (R values, dose-response, dyadic uniformity), which are new data.

---

## 10. Interpretation and open gates [I/O]

[I] The sieve renormalization flow is an exact, invertible, spectrum-preserving RG for arithmetic functions generated by the seed. The zeta zeros are not "in the prime pattern" — they are in the *seed*, readable through any sufficiently rich lens (prime indicator R=2.17, μ R=3.78), in an amount proportional to seed correctness. The divisor error's anatomy (seed-scale sum, uniform dyadic cancellation, Voronoi comb) is the same flow viewed in √x.

[O] (1) Does spectral preservation extend to other seed-generated functions (Liouville λ(n), prime k-tuples)? (2) The analytic *why* behind the dose-response gradient. (3) Whether the dyadic r_j uniformity can be pushed toward a certified bound (exponent-pair territory). (4) The 1/4 conjecture itself remains Lindelöf-hard; the flow's contribution is the exact finite battlefield, not the victory.

**Reproducibility.** All experiments live in the sandbox at `runs/20261002-sieve-renorm/` (`sieve_renorm.py`, `seed_specificity.py`, `two_track.py`, `corrected.py`, `divisor_flow.py`, `dyadic.py`, `kill_tests.py`, `pseudo_mu.py`, `NOTES.md`). No reproducer has been posted to `research-notes/`; per the standing firewall that awaits Jeremy's explicit per-item authorization.

---

*Jeremy's lines, kept verbatim: the seed "only generate[s] A(n)"; the flow "looks a lot like the Dirichlet's divisor problem 1/4 solution"; "we created this amalgamation, lets see if its imortal" — it survived every kill test designed to end it.*
