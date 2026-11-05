# The loop program — running notes (sandbox)

Direction set in DIRECTION.md (ledgered v15.391): build one-loop
machinery in the exponentiated variable. This file tracks the
steps as they are actually run. Nothing here is ledgered unless a
later deposit says so.

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

## Status

The three steps proposed in `DIRECTION.md` are now all executed
in sandbox: exponentiated-variable determinants (steps 1–2), the
Krein pair comparability protocol (step 3), eigen-sum insertions
with the GIM template (step 4). The machinery the literature
pointed to exists and behaves on this spectrum's perturbation
class. What has NOT been touched: applying any of it to Lane A's
canonical K (its actual B matrix elements) — a separate step,
with its own provenance care, not a silent substitution of the
model B. Loop weights (the three g's, CKM/PMNS, masses) remain
imported throughout; the standing doors are unchanged.
