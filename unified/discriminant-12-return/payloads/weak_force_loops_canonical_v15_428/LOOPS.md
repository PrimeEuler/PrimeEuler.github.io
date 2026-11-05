# The loop program — running notes (sandbox)

Direction set in DIRECTION.md (ledgered v15.391): build one-loop
machinery in the exponentiated variable. This file tracks the
steps as they are actually run. Steps 1–4 below were LEDGERED at
v15.394 (2026-11-04, Jeremy's direction; payload
`payloads/weak_force_loops_v15_394/` holds the snapshot as
deposited); anything added after that deposit is sandbox-only
until a later deposit says so.

## Step 1 — determinants in the exponentiated variable (2026-11-04)

`exp_variable_determinants.py`, on the diagonal seed spectrum
d_n = log(n/4) (D only; the bounded perturbation B of K = D + B is
not included — see Next).

- **The obstruction, numerically.** Σ_{n≤N} (log(n/4))^{−2} =
  94.4, 278.2, 1313.6, 7958.3 at N = 10³, 10⁴, 10⁵, 10⁶ — growing
  like N/log²N, no ζ-function in the λ variable, as the scout's
  [analysis] said. The same sum in the exponentiated variable
  converges at once: Σ (n/4)^{−2} → 16ζ(2) = 26.318945.
- **Heat traces with certified tails.** Tr e^{−βD} = 4^β ζ(β):
  β=2: partial sum (N=10⁵) 26.31878507 with integral-test tail
  ≤ 1.6×10⁻⁴, exact value inside the certified interval; β=3:
  partial 76.93164180, tail ≤ 3.2×10⁻⁹, exact inside. The
  certified-tail discipline of the ledger work (v15.130/v15.141
  lineage) does here what renormalization does elsewhere.
- **ζ-determinant.** For A = e^D (eigenvalues n/4):
  ζ_A(s) = 4^s ζ(s), ζ_A′(0) = −log 2 − ½ log(2π),
  det A = √(8π) = 5.01325655 (ζ prescription, μ=1 in A's units).
- **A ratio, and the Krein gate made concrete.** For A_{1/2}
  (eigenvalues (n+½)/4): ζ(0, 3/2) = −1 ≠ ζ(0) = −½. The
  ζ-prescription determinant ratio is 4/√π = 2.25675833, while
  partial products with the canonical cutoff-power subtraction
  converge to 1/Γ(3/2) = 2/√π = 1.12837917. The two finite parts
  differ by exactly log 2 = −Δζ(0)·log 4. Lesson, on our own
  spectrum: when a pair's ζ(0)s differ, the determinant ratio is
  scale-sensitive — determinant comparability has to be earned
  (equal ζ(0), or an explicit scale choice), which is the Krein
  trace-class gate wearing ζ clothes.

## Step 2 — the perturbed operator, on a model B (2026-11-04)

`perturbed_determinants.py`. K = D + B with B the Hilbert-like
model B_mn = 0.3/(m+n−1) — bounded (norm ≤ 0.3π), noncompact,
borderline summability: the same operator-theoretic class as the
ledger's B, but NOT Lane A's canonical B (provenance discipline;
conclusions are about the machinery on this class).

- **Raw determinant drifts; renormalized settles.** At z = −3.5,
  log det[(K_N − z)(D_N − z)⁻¹] grows steadily with section size
  (0.2664 → 0.3204 over N = 50 → 800, increments ~0.012–0.015 per
  doubling), tracking Tr(B R_D) — the expected log log N drift,
  since Tr(B R_D) ~ Σ 1/(n log n) diverges. Subtracting the trace
  (the det₂ renormalization) leaves increments 25× smaller and
  shrinking steadily (−0.00091 → −0.00050 per doubling), limit
  ≈ −0.027 ± 0.001 (extrapolated estimate): B R_D is
  Hilbert–Schmidt (Σ 1/(n log² n) converges) though not trace
  class. The Krein gate of Step 1, now quantitative for
  perturbations.
- **Birman–Krein verified, independently.** On an N = 120 section,
  with ξ(λ) the eigenvalue counting difference
  N_D(λ) − N_K(λ): Tr[R_K − R_D] = −0.0929621596 equals
  ∫ f′(λ) ξ(λ) dλ computed by exact interval integration of the
  step function (no eigenvalue-sum rearrangement — agreement to
  1e-8), and d/dz log D(z) = Tr[(D−z)⁻¹ − (K−z)⁻¹] agrees to 1e-6.
  The spectral-shift formalism works verbatim on finite sections
  of the log spectrum.

## Step 3 — the Krein pair test proper (2026-11-04)

`krein_pair_test.py`. Protocol: diagnostics FIRST, then quote only
the determinant the diagnostics license. Reference D against two
perturbations, per parity channel (even/odd mode index — the model
analog of the ledger's odd/even sectors). z = −3.5 throughout.

- **Pair A (diagonal, summable δₙ = 0.5/(n log²(n+3))): trace
  class, as designed.** The trace-side diagnostic T1 converges
  (odd 0.1612 → 0.1628; even 0.0621 → 0.0637, N = 200 → 1600), so
  the RAW determinant is licensed: values at N=1600 are
  +0.15568 (odd) and +0.06310 (even), with increments still
  shrinking slowly (+7.0e-4 → +3.9e-4 per doubling — the tail is
  of 1/log type, so read those as values-with-a-slow-tail, not
  polished limits).
- **Pair B (channel-preserving Hilbert-like): Hilbert–Schmidt
  only, as designed.** T1 grows (odd 0.285 → 0.311, log log-like)
  while the HS norm of B R_D settles (0.2242 → 0.2299). Raw
  determinant increments +0.0128/+0.0118 per doubling in both
  channels — NOT licensed. The det₂-renormalized determinants
  settle (increments −0.0006/−0.0005): −0.02196 (odd), −0.01624
  (even) at N=800.
- **Birman–Krein per channel:** all four (pair × channel) checks
  agree to 1e-8 by independent interval integration.

Verdict: the protocol discriminated the two classes exactly, per
channel, and no ratio was quoted beyond its licence. This is the
comparability discipline the canonical application will need.

## Step 4 — insertions: amplitudes as eigen-sums (2026-11-04)

`insertion_sums.py`. Determinants (steps 1–3) are functions of
eigenvalues alone; amplitudes are traces with insertions,
Tr[R V], Tr[(R V)²], … — matrix elements joined by resolvents.

- **The insertion trace works as an eigen-sum.** For a rank-1
  vertex V = |v⟩⟨v| (vₙ = 2^{−n/2}) on the step-2 model:
  Tr[R_K(z) V] computed directly and as
  Σⱼ ⟨ψⱼ|V|ψⱼ⟩/(μⱼ − z) agree to <1e-9 at every section size, and
  the value settles with N (0.332098 → 0.332122 → 0.332133,
  N = 100 → 400). Reference: Tr[R_D V] = 0.3985262 in closed form.
- **Eigenvalues insufficient — demonstrated, not just cited.**
  Twisting K by a rotation in the (3,5) mode plane gives K′ with
  eigenvalues identical to 8e-15 — hence identical ξ and identical
  every determinant from steps 1–3 — but Tr[R_K′ V] = 0.336773
  vs Tr[R_K V] = 0.332122, a plainly nonzero difference (0.0047).
  Insertions see eigenvectors; no spectral-shift-only formula
  can produce an amplitude. The survey's cross-cutting point,
  exhibited on our own spectrum class.
- **GIM template as an insertion sum over the generation
  direction.** A = Σ_g λ_g Y(x_g) over the three replicas
  (CKM-like weights with Σλ_g = 0 to 1e-18 — completeness over
  the generation direction, imported; Inami–Lim Y; physical
  masses, imported): the mass-difference form is identical,
  degenerate masses give A = 0 to 1e-26 (cancellation exact), and
  the term shares (u 4e-8 / c 3e-3 / t 1.00) show top dominance
  is a mass fact. Frame reading: the sum runs over the frame's
  c → c+3g replicas at fixed (n₂, τ, Y mod 2); the cancellation
  is completeness over that direction. Weights and masses remain
  imported — the generation door, in loop clothes.

## Step 5 — the canonical operator (2026-11-04)

`canonical_krein.py`. The protocol of steps 1–4 applied to finite
sections of Lane A's frozen K_full kernel (DERIVATION.md §0:
K_{N,m} = c(m z_N − N z_m)/(N²−m²) + 2σ p_N p_m, K_{N,N} = d_N +
2σ p_N²; B = the ledger's hollow off-diagonal part, D = diag(K)),
per sector, in two regimes (head: first S lattice modes; remote:
S modes from b = 512001/512002). Float stack copied verbatim from
the ledger's own v15.310 scoping payload (z_float, p_float,
d_float) — probe-grade [N] standing per that SPEC: scales, not
certified values. Finite sections only; NO full-K transfer claim
(the ledger's Schur route is the certificate path).

- **Validation.** d_float matches the certified diagonal
  evaluator's midpoints to 1.2e-6 (odd) / 1.4e-6 (even) on 24
  sampled remote modes per sector (the evaluator's regime is
  n > 256000; head diagonals are float-model only). Census:
  max |d_float − log(n/4)| = 1.7431 / 1.7452 vs the certified
  1.74586 bound. Section ‖B‖ = 1.71–1.86, the v15.310 window
  estimates' scale (1.89–1.97, different compressions).
- **The canonical pair FAILS the determinant gate — harder than
  the model.** ‖B R_D(z)‖²_HS grows with section size in both
  regimes (≈ S/log²S at the head: 2.63 → 4.42 → 7.43; ≈ linear
  in S remotely: 5.11 → 10.31 → 20.66, S = 200 → 800): the
  kernel's O(1) z-oscillations give every column non-decaying HS
  content, so B R_D is not Hilbert–Schmidt on the infinite
  operator and det₂ does not exist for the pair. (B hollow ⇒
  Tr(B R_D) = 0 on sections, so the raw section determinant is
  already its det₂ form.) Section log-determinants drift
  accordingly — remotely they are EXTENSIVE: logdet/S is stable
  at ≈ −0.0131 per mode (z = 7, both sectors, S = 800), i.e. a
  determinant density exists where no determinant does.
- **What survives is exactly what the ledger uses.** Birman–
  Krein holds on every canonical section checked (S=400, both
  sectors/regimes, interval integration): ξ is a real counting
  difference (max|ξ| = 38 head / 66, 61 remote; small at mid-
  range: −4, +3, −8, +3 at the median diagonal), and eigenvalue
  displacement from the sorted diagonal stays ≤ 0.72 (Weyl),
  well under ‖B‖ ≈ 1.8. Inertia counting and resolvent bounds —
  the ledger's tools — are the level at which this pair is
  well-posed; determinants are not, without a density or a
  higher det_p renormalization (unmeasured; the natural next
  refinement).
- **Canonical insertion.** The kernel's own pole vertex
  2σ⟨p, R p⟩: head S=800 — odd +1.1591 (K) vs +1.2362 (D),
  difference −0.0771; even −0.1167 vs −0.1080, difference
  −0.0088 (the insertion sees B, finitely). Remotely the pole
  vertex is nil (~1e-9): p ∈ ℓ² lives at the head of the lattice.

## Step 6 — no det_p at any order; the density is the object (2026-11-05)

`detp_density.py` (builders imported from `canonical_krein.py`;
same probe-grade standing). Question from step 5: does some
finite-order det_p exist for the canonical pair — i.e. is
X = B R_D(z) in a Schatten class S_p?

- **No — at every order measured, and the mechanism is visible.**
  Per-mode Schatten ratios stabilize at positive constants
  (remote, S = 200 → 800, both sectors): ‖X‖₂²/S = 0.0258,
  ‖X‖₃³/S = 0.0064, ‖X‖₄⁴/S = 0.0017. The singular-value
  quantiles are S-independent to three decimals remotely
  (median s ≈ 0.10, 99th percentile ≈ 0.36, S=400 vs 800):
  X has a limiting singular-value distribution — a local band
  operator carrying ~S singular values of typical size — so
  Σⱼ sⱼ^p ≈ c_p·S diverges for every finite p. Head ratios
  decay slowly (the log weights) but the sums still grow.
  Verdict: X ∉ S_p for any finite p; NO det_p exists for the
  canonical pair. The determinant level for this pair is a
  density, at every order of renormalization.
- **The renormalized density is small and nearly universal.**
  (1/S) log det_p densities, remote (z = 7): p=2: −0.01315
  (odd) / −0.01309 (even) — step 5's number; p=3: −0.00056 /
  −0.00054; p=4: −0.00044 / −0.00044. The p=2 bulk was almost
  exactly the trace term: Tr X²/S = +0.0252, and −½·0.0252
  ≈ −0.0126 accounts for nearly all of −0.0131; Tr X³/S
  ≈ −0.0003 ≈ 0 (the per-mode eigenvalue distribution of X is
  nearly odd-symmetric). After the X² subtraction the residual
  determinant content is ≈ −4.4×10⁻⁴ per mode, S-stable from
  S=200 and sector-independent at probe precision. Head
  densities drift slowly toward the same small residual (the
  per-head-mode normalization is the awkward one there, as the
  log weights grow).

Classification of the canonical pair, complete at probe level:
spectral shift / inertia — finite, ledger-native (step 5);
insertions — finite (steps 4–5); determinants — no det_p at any
finite order, density only, with renormalized density
≈ −4.4×10⁻⁴ per mode (remote, z = 7).

## Status

The three steps proposed in `DIRECTION.md` are executed
(steps 1–4), and the protocol has now been run on the canonical
operator's finite sections (steps 5–6, probe-grade): the
canonical pair fails the determinant gate in the strongest form
(no det_p at any finite order; a stable determinant density
instead), while the spectral-shift/inertia level — the ledger's
native level — verifies cleanly throughout, and insertions are
finite. A certified (interval-arithmetic) version of steps 5–6
would ride on the ledger's Schur-route machinery and remains
untouched. Loop weights (the three g's, CKM/PMNS, masses)
remain imported throughout; the standing doors are unchanged.
