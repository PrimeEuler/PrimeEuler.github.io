# Cone Derivation Ledger v13.883 — Sandbox: Binary Mod-24 — Zeros WHERE, DSUM HOW MUCH

**Date:** 2026-09-30
**Track:** Sandbox (our Lane B exploratory track)
**Status:** [N] numerical; [I]/[O] geometric interpretation
**Authorization:** Jeremy, 2026-09-30 ("ledger both as two")
**Predecessor:** v13.882 (binary decompression ζ-zero wave)

---

## Finding [N]

Splitting the binary decompression indicator b(n) (v13.882: 1 if composite,
0 if prime) by residue class mod 24 reveals that the **spectral** (zeta-zero)
content and the **arithmetic** (CD-release magnitude) content live on
**disjoint** residue sets.

### Compression fractions [N]

P(b=0 | r) = fraction at full 2D compression, by residue r mod 24 (N=24000):

- **8 coprime residues** (1,5,7,11,13,17,19,23): P(b=0) = 0.315–0.341
  (~333 primes each; Dirichlet equidistribution verified).
- **Residues 2, 3:** P(b=0) = 0.001 (primes 2, 3 only).
- **Other 14 residues:** P(b=0) = **0.000 exactly** (all composite).

### Spectral content [N]

Per-residue log-Fourier (subsequence b(n) for n≡r mod 24, ~1000 points,
resampled to 2000 uniform-t, rfft, peak within ±1.0 of each zeta zero;
significance = peak / median power over γ∈[10,60]; shuffled null max 2.5–7.8):

- The **14 all-composite residues have identically zero binary spectral
  content** — b(n) is constant 1, so the mean-removed spectrum is flat zero.
  This is exact, not statistical.
- Residues 2, 3 show only flat single-spike spectra.
- **All zeta-zero spectral content lives on the 8 coprime residues.**
  Max significances: r=1→10.1 @21.02, r=7→8.4 @25.01, r=13→8.2 @14.13,
  r=19→8.3 @21.02, r=11→7.6 @21.02, r=5→5.7 @14.13, r=17→5.2 @14.13,
  r=23→3.5 @43.33. Top peaks (8–10) exceed the shuffled null max (~7.8).

### Complementarity [N] (structural)

The cross-check against the v13.876-era magnitude bias comes back **inverted**
from the naive guess:

| Residue | CD-release magnitude bias | Binary spectral content |
|---------|--------------------------|------------------------|
| 0 mod 24 | +21.8 (max) | **zero** (exact) |
| 12 mod 24 | +13.2 | **zero** (exact) |
| 6, 18 mod 24 | +6.5, +5.8 | **zero** (exact) |
| coprime residues | −6 (min) | **max** (all the spectrum) |

**Spectral power and release magnitude live on disjoint residue sets.**
This is arithmetic necessity, not coincidence: primes (the 2D/compression
points whose *locations* the zeros govern) can only sit at coprime residues;
the *size* of composite releases is a divisor-function phenomenon concentrated
where composites cluster.

---

## Interpretation [I]/[O] (sharpens the two-sides framing)

- **Zeros = WHERE** — binary locations, coprime residues, 2D tension held.
- **DSUM magnitude = HOW MUCH** — non-coprime residues, CD release size.

The spectral and the arithmetic are **geometrically separated** on the cone's
mod-24 structure — exactly what the compression/release picture predicts.
The cone's 24-fold division is not just a convenient modulus; it is the
geometric locus where the two sides of the function separate.

Within the coprime set there are hints of residue-specific zero emphasis
(r=13↔14.13, r=7↔25.01, r∈{1,11,19}↔21.02), but per-residue SNR (~333 primes)
is too low to certify the ranking — treat as [I]/[O] pending larger N.

---

## Files (sandbox)

- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/mod24_binary_heatmap.png`
- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/mod24_binary_b.npz`
- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/mod24_binary_spectra.npz`
- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/mod24_binary_summary.npz`

## Open

- Residue-specific zero ranking needs larger N.
- No proof; numerical only.
- The selector (why these residues, why these frequencies) remains [I]/[O].

---

**Creed check:** The cone's mod-24 structure selects the separation — zeros on
coprime residues, magnitude on composite residues. Shown [N] for the
disjointness (exact), [I]/[O] for the geometric meaning.
