# Cone Derivation Ledger v13.896 — Sandbox: Full-A_a FEM Joint Experiment (Positivity Route Closed)

**Date:** 2026-10-01
**Track:** Sandbox (our Lane B exploratory track)
**Status:** [N] numerics (Richardson + refinement-ratio throughout); [D] pipeline/identities; [I]/[O] interpretation
**Authorization:** Jeremy, 2026-10-01 ("lets run it and hit the ledger after" — joint experiment + prime-power ablation)
**Predecessors:** v13.894 (stability test); v13.895 (ψ = log lcm identity); deep read of Suzuki 2606.09096 v3 + Kim et al. 2607.24830 (sandbox notes, not ledgered)
**Note:** v13.893 is audit-thread; this takes the next free version.

---

## Question

v13.894 varied weight quality (Λ vs indicator vs no prime powers) in
calibration matrices and found the spring↔Suzuki positivity bridge decisively
closed. Kim et al. varied the prime sum on/off in a full-A_a FEM. Neither ran
the **joint experiment**: weight variants *inside* the full-A_a FEM. If the
v13.894 failure were a calibration artifact, the full operator could differ.

## Pipeline [D/N]

P₁ FEM on (−a,a) per Kim's recipe: dense stiffness
Q_ij = ∬ g(x−y) φ_i′(x)φ_j′(y) dxdy (Toeplitz corner assembly, G₂″=g),
standard P₁ mass M, generalized problem Qv = λMv. g(t) per Suzuki (1.3) with
the v13.894-resolved Lerch bracketing. Protocol: refinement ratio
ρ = λ₁(N)/λ₁(2N) (ρ→1 genuine, ρ→4 h² artifact) + 3-point Richardson.

**Validation [N]:**
- g(t) small-t cross-check passed: t·log t coefficient ½ to 15 digits,
  linear term = Suzuki's A = 0.707546… to 14 digits, t² term = −7/8
  (after expected O(t³) fit bias). The archimedean side is correct.
- Full-Λ baseline λ₁ > 0 at a ∈ {⅓, 0.4, 0.45, 0.5}, all ρ→1.
- Independent reproduction of Kim's R7: prime sum removed at a=2 →
  our λ₁ = −4.968 vs their −4.97 (3 s.f.). Same object, same number.

## Results [N]

Weight variants of the prime sum Σ w(n)/√n·(|t|−log n), Richardson λ₁:

| variant | a=0.4 | a=0.5 | a=1 | a=2 |
|---|---|---|---|---|
| (a) full Λ | +1.82e−4 | +9.7e−7 | — | (≥0, unresolvable ~1e−25) |
| (b) indicator 1_prime | −3.2e−3 | −0.195 | −0.578 | −4.24 |
| (c) Λ, prime powers dropped | (=a, vacuous ≤0.5) | — | −0.345 | −1.07 |
| (d) noprime control | −0.078 | −0.322 | −1.32 | −4.97 |

Hierarchy in the exact operator: **Λ ≥ 0 > nopp > indicator, noprime worst**
— the v13.894 ordering, now in A_a itself. The calibration failure was not a
setup artifact.

**Knife-edge [N/I]:** at a=0.4 the indicator differs from Λ on exactly one
term (n=2), yet flips the sign: +1.8e−4 → −3.2e−3. Descriptive lift at a=0.4:
noprime −0.0778 → indicator −0.0032 → Λ +0.00018. The indicator captures 96%
of the Λ lift yet still lands negative — positivity under Λ is a knife-edge
and only the exact weights hold it. (v13.895: those weights are the jumps of
ψ(x) = log lcm(1,…,⌊x⌋) — the canonical prime weighting, which is why the
knife-edge sits exactly at Λ.)

## Prime-power ablation anatomy at a=2 [N]

Prime powers ≤ e⁴ ≈ 54.6: {4, 8, 9, 16, 25, 27, 32, 49}. From (c) primes-only
(λ₁ = −1.0724), lift toward zero by group: **squares {4,9,16,25,49}: +0.624
(58% of the gap)**; 2-tower {4,8,16,32}: +0.336 (31%); 3-tower {9,27}: +0.331
(31%) — essentially tied; cubes {8,27}: +0.252 (23%); rest {25,49}: +0.159
(15%); k≥4 alone {16,32}: −0.035 (−3%, converged — a real near-null-space
rotation effect, basis-dependent).

Leave-one-out from full Λ (dense eigh; ARPACK stalls on the near-null
cluster): damage ranking **4 (0.490) > 9 (0.366) > 25 (0.322) > 8 (0.245) >
27 (0.211) > 16 (0.173) > 32 (0.122)**; 49 unresolved at N=3200 (do not quote).

**Exactness pattern [N], mechanism open [O]:** for prime-power removals
n ∈ {8, 9, 16, 25, 27}, |λ₁(minus_n)| = Λ(n)/√n to 3–6 digits; n=4 is exactly
√2 × Λ(4)/√4 (1.41421250, N=3200, ρ=1.000000). Prime removals (2, 3) do NOT
follow it. First-order perturbation theory is wrong-signed and naive trial
modes give positive Rayleigh quotients — the ground state rotates completely
(parity flips for n=9, preserved for n=4). A sharp numerical fact in search of
an analytic explanation.

## Interpretation [I]/[O]

1. The spring↔Suzuki **positivity** bridge is closed in the full operator:
   "compression is not a small perturbation of Λ in the positivity topology"
   (v13.894) now holds for A_a itself. The frequency mechanism
   (spring/Guinand–Weil, v13.891) needs none of this machinery — two
   mechanisms, three legs (Guinand–Weil derivation + v13.894 + this
   experiment).
2. Both the log-weighting and the prime powers are independently load-bearing:
   (c) isolates prime powers (fails milder), (b) additionally degrades the log
   weights (fails harder). The load is spread across 2's and 3's towers, led
   by squares; no single prime power closes the gap alone.
3. Three-operator disambiguation (from the deep read): A_a (positivity,
   picket-fence) ≠ D̄_{a,θ} (H–P candidate, eigenvalues = zeros of W) ≠ spring
   (frequencies). The "Suzuki bridge" target is D̄_{a,θ}, carrying two
   quantified obstructions — Suzuki v3's circularity admission and Kim's
   Paley–Wiener density constraint (no θ(a) found).
4. Protocol adopted: a ≤ 0.5, N ≥ 1600, Richardson, always quote ρ. The a→∞
   axis is numerically inaccessible (Kim's R5 scaling law; λ₁ ~ 1e−78 at a=6).

## Caveats

- All eigenvalue claims [N], not theorems. No RH claims.
- minus_49 unresolved — not quoted as converged.
- The k≥4-alone-hurts sign is converged but small and basis-dependent; do not
  over-read it.
- Kim's numbers cited except the a=2 noprime value, independently reproduced.
