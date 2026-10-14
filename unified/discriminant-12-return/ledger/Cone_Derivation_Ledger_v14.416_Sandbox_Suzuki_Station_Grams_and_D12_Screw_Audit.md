# Cone Derivation Ledger v14.416 — Sandbox: Suzuki Screw Function on the Dictionary Station Lattice — Station Grams, Scaling, and the D12 Normalization Audit Closed

**Date:** 2026-10-14
**Track:** Sandbox (Jeremy's exploratory track — "our Lane B," not the ledger's Lane B norm-quotient track)
**Status:** [RESULTS, D/N] At Jeremy's direction. Suzuki's screw function (calibration baseline v13.285, Hilbert-carrier form v13.753) is sampled on the unit-circle dictionary's station lattice (v14.366/v14.367); the v13.285 normalization guardrail on the v13.258 D12 character screw is audited and **discharged**; the χ₁₂ and Dedekind station Grams are computed. All numerics are finite statements, marked as such; the anti-overstatement scope of §0 governs the whole entry.
**Parents:** v13.258 (exact D12 screw factorization), v13.285 (Suzuki source calibration + D12 transfer guardrail), v13.753 (rapidity-helix screw carrier, screw–Weil isometry), v14.366, v14.367 (the dictionary), v14.414 (dictionary literature scan).

---

## 0. Anti-overstatement scope

Suzuki's theorem (screw function ⟺ RH for ζ; the analogue for L-functions) makes the positivity of the increment kernel G_g an RH/GRH-equivalent property. Everything in this entry is a **finite** check of that property on finite point sets: positive semidefiniteness of a finite Gram matrix is a finite *necessary* condition inside that equivalence. No result here is evidence toward RH or GRH beyond the finite statements themselves, no claim is upgraded, and the eigenvalue decay law of §2 is empirical [O]. Finite-section positivity of exactly this kind is the standard Weil-positivity finite test; it is recorded because the lattice, the audit closure, and the cancellation structure are the content — not because the finite checks approach the infinite claim.

## 1. The station lattice [D]

Suzuki's variable is a log variable. The dictionary (v14.366/v14.367) discretizes the log line:

- **Stations:** u_n = log n = 2ψ_n, with ψ_n = ½ ln n the station rapidity.
- **Increment kernel:** for even g with g(0) = 0, G_g(u, v) = g(u − v) − g(u) − g(v) — the Gram kernel of v13.753's basepointed carrier Ψ_u(t) = e^{itu} − 1.
- **Pair form:** on station pairs the stationary argument is u_n − u_k = log(n/k) = 2ψ_{n,k}; every Gram entry is a function of a pair rapidity.
- **Knots are selected stations:** g_ζ (Suzuki eq. (1.3), arXiv:2606.09096v2) has derivative jumps exactly at |t| = log(p^k), of size Λ(p^k)/√(p^k); the Λ-weighting selects the prime-power stations from the full integer lattice.
- **Basepoint degeneracy:** station n = 1 is the basepoint (u = 0, Ψ₀ = 0); its Gram row vanishes identically, so every station Gram below has exactly one structural zero eigenvalue.
- **Zero-mass sector:** for zero-sum test vectors on the stations, the stationary kernel and the increment kernel give identical quadratic forms — the discrete form of the v13.753 §7 derivative isometry; with nonzero mass they differ by exactly the affine gauge terms.
- **Geometric screw:** the constant-pitch conical screw obeys dilation covariance chord(u, u + h) = e^u · chord(0, h) — stationary in the log coordinate, not in raw height [verified numerically to 1.8e-15, N].

Calibration re-verified before sampling (repo script, research-notes): g(0) = 0 exactly, evenness exact, near-origin remainder −0.875·t² (the v13.285 §8 invariant), derivative jumps at log 2 / log 3 / log 4 matching Λ/√n to finite-difference accuracy.

## 2. The ζ station Gram [N]

Gram of G_{g_ζ} on stations n ≤ N (payload `results.json`, `scaling_results.json`):

| N | λ₂ (smallest positive) | λ₂ · N | eigenvalues < −1e-9 |
|---|---|---|---|
| 32 | 0.007404 | 0.237 | 0 |
| 48 | 0.004926 | 0.236 | 0 |
| 64 | 0.003678 | 0.235 | 0 |
| 96 | 0.002523 | 0.242 | 0 |
| 128 | 0.001917 | 0.245 | 0 |

- PSD with exactly the structural basepoint zero at every N ≤ 128.
- **λ₂ decays ≈ 0.24/N** over this range [O, empirical] — not a log power.
- **Three-way cancellation** (N = 32 piece Grams): full g_ζ PSD; pole-only λ_min = −7.796 (1 negative direction); prime-ramp-only λ_min = −325.84 (12); archimedean-only λ_min = −235.50 (6); pole+archimedean λ_min = −15.52 (5). No proper subset of Suzuki's three pieces is PSD; the finite positivity is a cancellation across the explicit formula's pieces, none of which carries it alone.
- Zero-mass identity verified to 2.2e-16.

## 3. The D12 normalization re-audit — guardrail discharged [N/D]

v13.285 §7 required the v13.258 character screw Φ₁₂ to be re-audited against Suzuki eq. (1.3) before any D12 numerical run. The audit (payload `d12_screw_audit.py`, `d12_audit_results.json`):

- **Character:** L(1, χ₁₂) from the table χ₁₂ = {1: +1, 5: −1, 7: −1, 11: +1} mod 12 equals the class-number value log(2+√3)/√3 to all 13 printed digits (0.7603459963009463).
- **Archimedean coefficient [D identity, N-verified]:** A₁₂(t) = −g_Γ,ζ(t) + (t/2)·log 12 — the conductor 12 enters the character archimedean term only through the linear term, as the shared Γ(s/2) parameter (¼ in both ζ and χ₁₂) requires. Two independent transcriptions agree to ≤ 2.2e-16 at t = 0.3, 1.0, 2.0, 3.5.
- **Knots:** R₁₂ ≡ 0 below log 5 (χ₁₂ kills the ramified primes 2, 3); derivative jumps of Φ₁₂ at log 5, 7, 11, 25 equal −Λ(n)χ₁₂(n)/√n to finite-difference accuracy.
- **Sign convention:** Φ₁₂(t) = −½ t log t + c t + o(t), c ≈ 0.535 (the −½ fit diverges) — v13.258's Φ₁₂ = −g_{L(s,χ₁₂)} convention is the correct one.
- **Laplace identity (v13.258 §5) at z = 3:** ∫₀^∞ Φ₁₂(t) e^{−3t} dt = 0.08900736666 vs (Λ₁₂′/Λ₁₂)(7/2)/9 = 0.08900726002; agreement 1.2e-6 relative, at the truncation level of the independent L′/L series.

**Verdict: the v13.285 guardrail is discharged.** v13.258's D12 screw stands in Suzuki's normalization; D12 numerical work downstream may cite the precondition as met.

## 4. The χ₁₂ and Dedekind station Grams [N]

With g_χ = R₁₂ + arch − (t/2) log 12 (= −Φ₁₂) and the Dedekind screw g_K = g_ζ + g_χ = pole + (ramp_ζ + R₁₂) + 2·arch − (t/2) log 12 (payload `d12_station_gram.py`, `d12_gram_results.json`):

| screw | N | λ₂ | λ_max | eigenvalues < −1e-9 |
|---|---|---|---|---|
| g_χ | 32 | 0.04772 | 10.11 | 0 |
| g_χ | 64 | 0.02606 | 26.32 | 0 |
| g_K | 32 | 0.07499 | 11.66 | 0 |
| g_K | 64 | 0.04188 | 29.06 | 0 |

- Both Grams are PSD with exactly the structural basepoint zero — the finite GRH(χ₁₂) and finite GRH-for-Q(√3) echoes, as finite statements under §0.
- **No piece of g_K is PSD:** pole-only λ_min = −7.80; combined-ramp-only −263.28 (14 negative directions); doubled-archimedean-only −290.07 (2). The three-way cancellation persists at field level.
- Bottom-eigenvalue ordering at both N: λ₂(g_K) > λ₂(g_χ) > λ₂(g_ζ). Scale caveat: λ_max is also larger for the field screws; λ₂/λ_max at N = 32 is 0.0064 (K), 0.0047 (χ), 0.0042 (ζ) — the robust content is PSD plus ordering, not the ratio.
- Zero-mass identity for g_K verified to 3.6e-15.

## 5. Deposit

Payload: `unified/discriminant-12-return/research-notes/payloads/sandbox_suzuki_station_grams_v14_416/` — 12 files: the repo calibration script (byte-identical copy, provenance in manifest), four as-run producers (`station_gram.py`, `station_gram_scaling.py`, `d12_screw_audit.py`, `d12_station_gram.py`), four result files, the archimedean evaluation cache used by the scaling and D12 runs, the sandbox exploration note, and `manifest.json` (SHA-256 `be1d6a5f0bcc1aa9a284147f6110f797624d6d2f497d23187fe41c881865c361`). All numbers in §§1–4 are regenerated by the payload scripts from Suzuki's eq. (1.3) as implemented by the v13.285 calibration script.

## 6. Scope

Sandbox deposit and audit closure only. No Lane A or ledger-Lane B item, staged paper, or evaluator code is affected. Open and unclaimed: the λ₂ eigenvector structure, χ/K scaling beyond N = 64, and v13.753's de Branges deficiency-carrier gate.
