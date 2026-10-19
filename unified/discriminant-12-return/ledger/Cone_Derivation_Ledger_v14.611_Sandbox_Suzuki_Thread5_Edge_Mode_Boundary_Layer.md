# Cone Derivation Ledger v14.611 — Sandbox deposit: Suzuki Thread 5 edge-mode test — the χ/K soft mode is a far-end boundary layer

**Timestamp:** 2026-10-19 (EDT)
**Lane:** Sandbox (little Euler)
**Parents:** v14.416 (station-sampled Suzuki screw Grams for ζ, χ₁₂, g_K; PSD with exactly one structural zero), v14.456 (Phase 2: Thread 1 λ₂ eigenvector structure, Thread 2 λ₂ scaling exponents), v14.457 (Audit R279 verification of Phase 2 Threads 1/2/4), v14.610 also being live HEAD at allocation (collision-checked immediately before — next-free was v14.611).
**Status:** deposit entry under Jeremy's explicit 2026-10-19 authorization ("Deposit Thread 5 + the channel table, then draft both notes"). Answers **no Lane A HANDOFF**; changes no paper, no staged draft, and no certified object. Thread 5 ran 2026-10-15 as a Phase 2 follow-up and has been workspace-only since; this entry deposits it unchanged. All statements are **[N]** (descriptive finite statements about the saved Grams); the verdict reading is [N/I].

## The question

Phase 2 Thread 1 (v14.456) found the λ₂ modes of the χ₁₂ and Dedekind-K station Grams sitting at the far edge of the station window (top stations = last ~5 at every N = 32..128), while ζ's λ₂ is pinned to the small prime-power knots {2,3,4,8,9}; Thread 2 measured λ₂ ~ N^−0.87 (χ), N^−0.84 (K) against ζ's ~1/N. Thread 5 asks the question Thread 1's caveat left open: is the χ/K edge mode a truncation artifact, or genuine large-rapidity behaviour of the screws?

## Method

Every restricted Gram is a principal submatrix of the full N = 128 station Gram (entries are pair-determined, G[i,j] = g(u_i−u_j) − g(u_i) − g(u_j)), so restrictions are exact — no kernel re-evaluation. Tests: full-Gram modes λ₂..λ₅; drop-near-edge block (stations 33..128); middle block (33..96); sliding width-64 windows starting at 1, 17, 33, 49, 65. Per-mode statistics: participation ratio, sign changes, top-5 stations by mass, mass in first/last 1/2/4/8/16 stations and first/last deciles. The ζ N = 128 Gram was assembled by the producer and saved with the payload; the χ/K Grams are the Phase 2 buffers.

Deposit: payload `research-notes/payloads/sandbox_suzuki_thread5_edgemode_v14_611/` (note `THREAD5.md`, producer `thread5_edgetest.py`, results `thread5_edgetest_results.json`, the three N = 128 Gram buffers; manifest with SHA-256 per file in the payload). Workspace originals in `explorations/screw-stations/`.

## Results

Full N = 128 (λ_min = 0 exactly in all three — the structural n = 1 zero of v14.416):

- ζ λ₂ = 0.0019169, top stations {2,3,4,8,9}, first-8 mass 0.433, last-decile mass 0.024; λ₅ top stations {5,10,15,20,30} (multiples of 5).
- χ λ₂ = 0.0142322, top stations {125,124,126,123,122}, last-8 mass 0.927, last-decile 0.988, first-8 mass 0.0014.
- K λ₂ = 0.0233991, top stations {124,125,123,126,122}, last-8 mass 0.903, last-decile 0.994.

Restrictions:

- **Drop-near (33..128):** ζ's softest mode becomes a smooth delocalized mid-window hump (λ₂ = 0.0056983 vs 0.0019169 full; participation ratio 42.1; 7 sign changes; top {59,57,58,60,56}). χ (λ₂ = 0.0148468) and K (λ₂ = 0.0243114) stay at the far edge (last-16 mass 0.992 both).
- **Middle block (33..96):** ζ λ₂ = 0.0073544 stays interior (top {43,42,44,41,45}); χ λ₂ = 0.0193101 and K λ₂ = 0.0313078 sit at the window's far end (top {88,87,89,86,94}).
- **Sliding width-64 windows:** the χ/K soft mode is never at a window's left edge (first-8 mass 0.00 in every window) and always organizes at the far end, weakening as the window slides right — χ: λ₂ 0.0260562 → 0.0148473, last-8 mass 0.979 → 0.350, participation ratio 6.00 → 10.56 (starts 1 → 65); K: λ₂ 0.0418758 → 0.0243280, last-8 mass 0.985 → 0.353, participation ratio 5.82 → 10.54.
- **λ₃/λ₄/λ₅ (full Grams, χ and K)** form a boundary-layer family stacked against the far edge, retreating inward as the eigenvalue rises (top stations ≈ 120, ≈ 116, ≈ 111; last-8 mass decreasing).

## Verdict [N/I]

The χ/K "edge mode" is a far-end boundary layer of the finite sections — window-relative (it follows the far edge of whatever window is used, never the near edge), not an interior mode of the screws. The Phase 2 exponents (−0.87 χ, −0.84 K) therefore describe how this boundary layer softens as the window grows, not the decay of an interior screw mode. ζ's pinned arithmetic mode is a genuinely softer interior direction that out-competes the generic boundary layer whenever the small prime-power stations are in the window. This refines — does not retract — the v14.456 Thread 1/2 records: the exponents stand as measurements, their interpretation is corrected to the boundary layer.

## Verification

Re-run of `thread5_edgetest.py` from the deposited buffers on 2026-10-19 (deposit day) reproduced `thread5_edgetest_results.json` exactly: 888 floating-point values compared, worst relative difference 0.

## Scope flags (honest)

`answers_lane_a_handoff = false`; `papers_modified = false`; `certified_objects_modified = false`; `claim_class = NUMERICAL_FINITE_SECTIONS_ONLY` (no statement about the infinite sections or the continuum operators); `phase2_thread1_2_records = REFINED_NOT_RETRACTED` (interpretation only); `boundary_layer_is_truncation_phenomenon = YES_BY_CONSTRUCTION_OF_TEST` (window-relative following is the evidence); `G_derived = false`.

## Disposition

The Suzuki×dictionary lane's Phase 2 follow-up is now fully deposited (Threads 1–4 at v14.456, Thread 5 here). The finite-section boundary-layer reading is the standing interpretation of the χ/K λ₂ scaling for any downstream use, including external correspondence.
