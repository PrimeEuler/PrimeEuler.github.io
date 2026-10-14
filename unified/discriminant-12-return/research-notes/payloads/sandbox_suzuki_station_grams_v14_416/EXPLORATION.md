# Suzuki Screw × Unit-Circle Dictionary — Station-Sampled Kernel Exploration

**Date:** 2026-10-14. **Track:** sandbox (Jeremy-commissioned exploration; workspace-only, nothing ledgered).
**Question (Jeremy):** explore the cone/parabolic geometry's relation to Suzuki's screw function further, given the geometry's Hilbert-space aspects.

## Grounding in the ledger record [D]

- **v13.753:** Suzuki's kernel is a Hilbert-space Gram kernel: with Ψ_u(t) = e^{itu} − 1, G_g(u,v) = g(u−v) − g(u) − g(−v) + g(0) = ⟨Ψ_u, Ψ_v⟩ in the screw increment space; the derivative map to the Weil form is an exact isometry (unitary after completion, [C] on positivity). Zero-frequency gauge: span{1, u} ↔ span{δ₀, δ₀′}, fixed by evenness and g(0) = 0.
- **v13.285:** source calibration against Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v2 eq. (1.3); guardrail: D12 transfer coefficients are re-audited against this normalization before numerics. Calibration script: repo `research-notes/suzuki_riemann_screw_calibration.py` (copy in this folder).
- **v13.258:** exact D12 screw factorization (archimedean term, character screw, Dedekind additivity over V4 channels) — formula level.
- **v14.366/v14.367 + 2026-10-14 session:** the dictionary — stations z_n, pair rapidities ψ_{n,k} = ½ ln(n/k), (n+k)/(n−k) = coth ψ_{n,k}; parabolic readout ψ = ½ ln(ξ/η).

## The formalization

Suzuki's variable t is a log variable. The dictionary discretizes the log line:

- **Stations:** u_n = log n = 2ψ_n, n = 1, …, N.
- **Kernel on pairs:** G_g(u_n, u_k) has stationary argument u_n − u_k = log(n/k) = 2ψ_{n,k} — every entry of the sampled kernel is a function of a pair rapidity.
- **Knots are prime-power stations:** g_ζ is piecewise linear-in-ramps with derivative jumps exactly at |t| = log(p^k), jump size Λ(p^k)/√(p^k) — the Λ-weighting selects prime-power stations from the full integer lattice.
- **Geometric screw:** the constant-pitch conical screw obeys dilation covariance chord(u, u+h) = e^u · chord(0, h) [D, verified §3.5] — stationary in the log coordinate u, not in raw height. Its log-unwrapping is a cylinder helix.

## Numerical results [N] (script `station_gram.py`, results `results.json`)

Calibration re-verified first: g(0) = 0 exactly; evenness exact; near-origin remainder −0.875·t² (the v13.285 §8 O(t²) invariant); derivative jumps at log 2 (0.490117 vs Λ(2)/√2 = 0.490129), log 3 (0.634251 vs 0.634284), log 4 (0.346534 vs log 2/2 = 0.346574) — all at finite-difference accuracy.

**Station Gram, N = 32 (u up to log 32 ≈ 3.47):**

| kernel piece | λ_min | # eigenvalues < −1e-9 |
|---|---|---|
| **full g_ζ (pole + prime + arch)** | **0.0** | **0** |
| pole only | −7.796 | 1 |
| prime ramp only | −325.84 | 12 |
| archimedean only | −235.50 | 6 |
| pole + arch (no primes) | −15.52 | 5 |

Findings:

1. **The full station Gram is positive semidefinite, with exactly one zero eigenvalue**, and that zero is structural: station n = 1 is the basepoint (u = 0, Ψ₀ = 0), so its Gram row vanishes identically. The next eigenvalues are 0.00740, 0.00930, 0.01136, 0.01258, … — strictly positive. This is the finite screw property of g_ζ restricted to the station lattice n ≤ 32 — the point-sample shadow of Suzuki's theorem (g_ζ is a screw function ⟺ RH). Finite and necessary only; **not** evidence toward RH beyond the finite statement itself.
2. **No proper subset of the three pieces is PSD.** Pole, prime, archimedean, and pole+arch Grams all have genuinely negative eigenvalues (not tolerance-level). The finite positivity is a three-way cancellation across the explicit-formula pieces — none of them carries it alone. The prime ramp alone is the most non-PSD (λ_min ≈ −326); the archimedean term alone is also strongly non-PSD (≈ −236).
3. **Zero-mass identity (discrete v13.753 §7):** for a zero-sum test vector f on the stations, f^T K f = f^T G f to 2.2e-16 (K = stationary kernel g(u_n − u_k)); for a nonzero-mass f the two differ by 4.43 — the affine gauge terms are exactly the mass terms, as the ledger's form-isometry predicts.
4. **Cone screw covariance:** dilation covariance of the constant-pitch conical screw verified to 1.8e-15 — the geometric screw is stationary precisely in the coordinate (log height = rapidity direction) in which Suzuki's kernel lives.

## Reading [I]/[O]

The dictionary and the screw function are native to the same coordinate: the log line, discretized by the dictionary into stations and pairs. On that lattice, Suzuki's RH-equivalent positivity is already visible as a finite, checkable, three-way cancellation — and the parabolas of the cone table are the coordinate curves of the same (ξ, η) plane whose difference coordinate is the kernel's argument. The geometric screw (cone, dilation-covariant) and the analytic screw (Hilbert-space increments) share the log coordinate as their stationarity parameter; that shared coordinate, not a shared surface, is the bridge.

## Scaling of the ζ station Gram [N] (script `station_gram_scaling.py`, `scaling_results.json`)

| N | λ₂ (smallest positive) | λ₂ · N | negatives < −1e-9 |
|---|---|---|---|
| 32 | 0.007404 | 0.237 | 0 |
| 48 | 0.004926 | 0.236 | 0 |
| 64 | 0.003678 | 0.235 | 0 |
| 96 | 0.002523 | 0.242 | 0 |
| 128 | 0.001917 | 0.245 | 0 |

PSD with the single structural basepoint zero survives to N = 128. λ₂ decays like **1/N** over this range (λ₂·N ≈ 0.24, mild upward drift) — not like 1/log N or 1/(log N)². The bottom of the finite-section spectrum accumulates at 0 at rate ~0.24/N. (One infrastructure note: the first scaling run died on a floating-point cache-key mismatch — log(n)−log(k) vs log(n/k) splitting a rounding boundary; fixed by quantizing cache keys to 1e-9 and salvaging the cache.)

## Normalization re-audit of the D12 character screw [N] (script `d12_screw_audit.py`)

The v13.285 guardrail, executed against v13.258 §§2–5. **All checks pass:**

- **Character validated end-to-end:** L(1, χ₁₂) from the table {1:1, 5:−1, 7:−1, 11:1} (mpmath Dirichlet) = 0.7603459963009463; class-number value log(2+√3)/√3 = 0.7603459963009463. Identical to all 13 printed digits.
- **Archimedean coefficient:** the direct transcription of A₁₂ and the mirror identity A₁₂(t) = −g_Γ,ζ(t) + (t/2)·log 12 agree to ≤ 2.2e-16 at t = 0.3, 1.0, 2.0, 3.5 — the conductor 12 enters the character archimedean term **only** through the linear term (t/2)·log 12, exactly as the shared Γ(s/2) parameter (¼ in both) requires.
- **Knot structure:** R₁₂ ≡ 0 below log 5; derivative jumps of Φ₁₂ at log 5, 7, 11, 25 measured 0.719753, 0.735477, −0.722999, −0.321892 vs predicted −Λ(n)χ₁₂(n)/√n = 0.719763, 0.735485, −0.722993, −0.321888.
- **Small-t sign test:** Φ₁₂(t) = −½ t log t + c t + o(t) with c ≈ 0.535 (the +½ fit converges; the −½ fit diverges) — the Φ₁₂ = −g_χ sign convention of v13.258 is the correct one.
- **Laplace identity (§5) at z = 3:** ∫₀^∞ Φ₁₂(t) e^{−3t} dt = 0.08900736666 vs (Λ₁₂′/Λ₁₂)(7/2)/9 = 0.08900726002 — agreement 1.1e-7 absolute (1.2e-6 relative), at the truncation level of the L′/L series and the kinked quadrature.

## D12 screws on the station lattice [N] (script `d12_station_gram.py`, `d12_gram_results.json`)

With g_χ = R₁₂ + arch − (t/2) log 12 (= −Φ₁₂) and the Dedekind screw g_K = g_ζ + g_χ = pole + (ramp_ζ + R₁₂) + 2·arch − (t/2) log 12:

| screw | N | λ₂ | λ_max | negatives |
|---|---|---|---|---|
| g_χ | 32 | 0.04772 | 10.11 | 0 |
| g_χ | 64 | 0.02606 | 26.32 | 0 |
| g_K | 32 | 0.07499 | 11.66 | 0 |
| g_K | 64 | 0.04188 | 29.06 | 0 |

- Both the χ₁₂ Gram and the Dedekind Gram are **PSD with exactly the structural basepoint zero** at both sizes — the finite GRH(χ₁₂) and finite GRH-for-Q(√3) echoes hold on the station lattice. [N] finite statements only.
- **No piece of g_K is PSD either:** pole-only λ_min −7.80; combined-ramp-only −263.28 (14 negative directions); doubled-archimedean-only −290.07. The three-way cancellation persists at field level.
- Zero-mass identity for g_K holds to 3.6e-15.
- Bottom-eigenvalue ordering at both N: λ₂(g_K) > λ₂(g_χ) > λ₂(g_ζ), by an order of magnitude over ζ. (Scale caveat: λ_max is also larger for the field screws; the ratios λ₂/λ_max at N = 32 are 0.0064 (K), 0.0047 (χ), 0.0042 (ζ) — same ballpark, K modestly largest. The robust content is PSD + ordering, not the ratio.)

## Next steps

1. Eigenvector structure of the λ₂ mode for the three screws (is the bottom mode a smooth "ramp" vector on the log line? does it localize near the ramified stations?).
2. χ and K scaling to N = 96/128 (archimedean cache already warm) and their λ₂ decay laws vs ζ's 0.24/N.
3. Compare the station-lattice zero-mass sector with v13.753's next gate (de Branges deficiency carrier E(z), paired characteristic T_pair) — does the discrete basepoint gauge have a boundary-triple reading?
4. The χ₁₂ archimedean screw term vs the parabolic/KS computation of the dipole kernel: same (ξ, η) machinery — is the conductor-12 archimedean term a pair-rapidity object of the same form as the 32/81 walkthrough?
