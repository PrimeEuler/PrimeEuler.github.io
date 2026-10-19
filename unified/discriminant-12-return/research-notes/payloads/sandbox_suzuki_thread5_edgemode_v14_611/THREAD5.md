# Thread 5 — edge-mode test: the χ/K soft mode is a far-end boundary layer

*Sandbox (little Euler), run 2026-10-15 as a Phase 2 follow-up
(post-v14.456), workspace-only until this deposit. [N] throughout:
descriptive finite statements about the saved station Grams.
Producer: `thread5_edgetest.py`; results: `thread5_edgetest_results.json`;
Grams: `gram_zeta_N128.npz`, `gram_chi_N128.npz`, `gram_K_N128.npz`.*

## Question

Phase 2 Thread 1 found that the λ₂ mode of the χ₁₂ and Dedekind-K
station Grams sits at the far edge of the station window (top stations
= last ~5 at every N), while ζ's λ₂ is pinned to small prime-power
knots {2,3,4,8,9}; Thread 2 measured λ₂ ~ N^−0.87 (χ), N^−0.84 (K)
against ζ's ~1/N. Thread 5 asks whether the χ/K edge mode is a
truncation artifact or genuine large-rapidity behaviour of the screws.

## Method

All restricted Grams are principal submatrices of the full N = 128
station Grams (entries are pair-determined: G[i,j] = g(u_i−u_j) −
g(u_i) − g(u_j)), so restrictions are exact — no kernel re-evaluation.
Tests: full Gram modes λ₂..λ₅; drop-near-edge block (stations
33..128); middle block (33..96); sliding width-64 windows starting at
1, 17, 33, 49, 65. The ζ N = 128 Gram was assembled by the producer
and saved (`gram_zeta_N128.npz`); the χ/K Grams are the Phase 2
buffers. Per-mode statistics: participation ratio, sign changes,
top-5 stations by mass, mass in first/last 1/2/4/8/16 stations and
first/last deciles.

## Findings

Full N = 128 (λ_min = 0 exactly in all three — the structural n = 1
zero of v14.416):

- ζ λ₂ = 0.0019169, top stations {2,3,4,8,9}, first-8 mass 0.433,
  last-decile mass 0.024. λ₅ top stations {5,10,15,20,30}.
- χ λ₂ = 0.0142322, top stations {125,124,126,123,122}, last-8 mass
  0.927, last-decile 0.988, first-8 mass 0.0014.
- K λ₂ = 0.0233991, top stations {124,125,123,126,122}, last-8 mass
  0.903, last-decile 0.994.

Restrictions:

- Drop-near (33..128): ζ's softest mode becomes a smooth delocalized
  mid-window hump — λ₂ = 0.0056983 (vs 0.0019169 full), participation
  ratio 42.1, 7 sign changes, top stations {59,57,58,60,56}. χ
  (λ₂ = 0.0148468) and K (λ₂ = 0.0243114) stay at the far edge
  (last-16 mass 0.992 both).
- Middle block (33..96): ζ λ₂ = 0.0073544, top {43,42,44,41,45}
  (interior). χ λ₂ = 0.0193101 and K λ₂ = 0.0313078 sit at the
  window's far end: top stations {88,87,89,86,94}.
- Sliding width-64 windows: the χ/K soft mode is NEVER at a window's
  left edge (first-8 mass 0.00 in every window) and always organizes
  at the far end, weakening as the window slides right:

  | window start | χ λ₂ | χ last-8 | χ PR | K λ₂ | K last-8 | K PR |
  |---|---|---|---|---|---|---|
  | 1 | 0.0260562 | 0.979 | 6.00 | 0.0418758 | 0.985 | 5.82 |
  | 17 | 0.0227679 | 0.560 | 8.73 | 0.0366434 | 0.537 | 8.92 |
  | 33 | 0.0193101 | 0.459 | 9.54 | 0.0313078 | 0.462 | 9.52 |
  | 49 | 0.0167647 | 0.393 | 10.01 | 0.0273453 | 0.400 | 10.00 |
  | 65 | 0.0148473 | 0.350 | 10.56 | 0.0243280 | 0.353 | 10.54 |

- λ₃/λ₄/λ₅ of the full Grams (χ and K) form a boundary-layer family
  stacked against the far edge, retreating inward as the eigenvalue
  rises (top stations ≈ 120, ≈ 116, ≈ 111; last-8 mass decreasing).

## Verdict [N/I]

The χ/K "edge mode" is a far-end boundary layer of the finite
sections — window-relative (it follows the far edge of whatever
window is used, never the near edge), not an interior mode of the
screws. The Phase 2 exponents (−0.87/−0.84) therefore describe how
this boundary layer softens as the window grows, not the decay of an
interior screw mode. ζ's pinned arithmetic mode is a genuinely softer
interior direction that out-competes the generic boundary layer
whenever the small prime-power stations are in the window.

## Verification

Re-run of `thread5_edgetest.py` from the deposited buffers on
2026-10-19 reproduced `thread5_edgetest_results.json` exactly (888
floating-point values compared, worst relative difference 0).
