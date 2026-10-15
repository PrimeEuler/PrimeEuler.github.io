# Cone Derivation Ledger v14.456 — Sandbox Suzuki station-lattice Phase 2: λ₂ eigenmodes, χ/K scaling to 128, de Branges boundary-triple gate, archimedean–KS exclusion

**Timestamp:** 2026-10-15 (EDT)
**Lane:** Sandbox (our Lane B) — exploratory, deposited at Jeremy's direction
**Parent:** v14.416 (station Grams + D12 screw audit; fully audit-verified R266/R267, v14.417/v14.418)
**Commission:** Jeremy, 2026-10-15 — all four open threads of v14.416 §6 run in parallel.

## Scope and markings

Phase 2 of the station-lattice exploration: Suzuki screw functions sampled at the dictionary stations u_n = log n. [N] = finite numerical statement, [D] = derived, [C] = conditional, [O] = open, [I] = interpretation. Finite PSD/eigenvalue statements are finite *necessary* conditions inside Suzuki's screw ⟺ RH / GRH equivalences; nothing here is evidence toward RH/GRH beyond the finite statements themselves. Payload: `research-notes/payloads/sandbox_suzuki_phase2_v14_456/` (16 files; manifest SHA-256 `2e3409d1ffcab94393834d0ae509b3b3cb7392f58ab0f7dc0a55736383dcebc8`).

## §1 Thread 2 — χ and K scaling to N = 96/128 [N]

Station Grams for g_χ (L(s,χ₁₂) screw) and g_K (Dedekind ζ of ℚ(√3)) extended from N=64 to N=96/128 with the v14.416 machinery (D12 normalization audited in v14.416 §3). PSD holds at both new sizes for both screws (single structural zero at the n=1 basepoint, no negative eigenvalues).

| N | λ₂(χ) | λ₂(K) | λ₂(ζ) (v14.416) |
|---|---|---|---|
| 32 | 0.047723 | 0.074993 | 0.007404 |
| 64 | 0.026056 | 0.041876 | 0.003678 |
| 96 | 0.018331 | 0.029758 | 0.002523 |
| 128 | 0.014232 | 0.023399 | 0.001917 |

λ₂·N *rises* over the window (χ: 1.53→1.67→1.76→1.82; K: 2.40→2.68→2.86→3.00), so the effective decay is λ₂ ~ N^−0.87 (χ) and N^−0.84 (K), against ζ's ~0.24/N (λ₂·N ≈ const). Ordering λ₂(K) > λ₂(χ) > λ₂(ζ) at every N. Section caveat: per §2, the χ/K λ₂ over these windows is governed by a truncation-edge mode, so these exponents are partly statements about the finite section, not only about the screws.

## §2 Thread 1 — structure of the λ₂ eigenvector [N]

- **ζ:** the softest nonzero mode is *pinned to small prime-power knots*: top-|v| stations {2, 3, 4, 8, 9} at every N = 32…128; prime-power stations carry 0.58–0.79 of the mass; participation ratio grows 10.9 → 19.6; sign changes ≈ N (maximally oscillatory); overlaps with smooth shapes (constant, linear-in-u, 1/√n) all ≤ 0.15. The mode does not drift as the window grows.
- **χ and K:** the mode *follows the far edge of the window*: top stations are the last ~5 at every N (28–32 at N=32; 59–63 at 64; 90–95 at 96; 122–126 at 128), with 0.99–1.00 of the mass in the last decile at N=96/128 and participation ratio ≈ 4.6–7.7. It is an edge-localized oscillatory mode of the truncation, not an interior structure — the exact opposite behavior from ζ's arithmetically pinned mode.

## §3 Thread 3 — v13.753's de Branges gate [D, with named opens]

The boundary-triple interpretation of the basepointed helix carrier **exists and is exact at finite A**: the derivative transport D̄ is a unitary conjugation of Suzuki's realizations, so the triple itself transports (Γ̃_j = Γ_j D̄⁻¹, γ̃_a = D̄ γ_a) and the Weyl function is *identical* on the helix side (m̃_a = m_a). The screw–Weil unitary intertwines the triple-determined part of the paired characteristic T_pair, not merely its quadratic form; E_a's de Branges kernel is exactly the transported γ-field Gram dressed by the W_π gauge, and the helix current sees T_pair at log-derivative level via −iL = T_pair′/T_pair + E′/E. Checks: three sympy identities exact; mpmath at 30 digits confirms Ξ/E = [1 + i·c_∞·m_∞]⁻¹ to ~1e-31 and E·T_pair = C_ξ·Ξ to ~1e-34 (anchors a = 0.5087310387, b = 0.0234707786, c_∞ = 0.0461359281).

The **basepoint quotient is provably NOT a boundary condition**: it is the pre-triple quotient by ker D = span{1}, corresponding on the de Branges side to the entire-gauge freedom of E at fixed m (all characteristics see only −g″, annihilating the same span{δ₀, δ₀′}); the station n=1 structural zero is its finite shadow — the station Gram is built from increments and cannot represent the gauge at all.

Named opens/catches: (i) an intrinsic finite c_a → c_∞ does not exist yet [O, v13.668 §7] — "the helix determines E_a" holds modulo one imported scalar plus orientation; (ii) orientation soft spot: v13.670 §7's candidate differs from v13.677's E_a by the deficiency reflection (E vs E♯); the sign is fixed only by Suzuki's §7.8 anchor, not by the triple alone; (iii) a silent Ξ convention collision exists between v13.737 (Ξ(w) = ξ(1/2+w)) and v13.668/670 (Ξ(z) = ξ(1/2−iz)); (iv) finite-to-infinite convergence of T_pair remains [O]/[C] on screw positivity. Full text: payload `THREAD3.md`.

## §4 Thread 4 — χ₁₂ archimedean term vs the parabolic/KS dipole [D, negative]

The parabolic reading is **excluded by function class**, not merely unfound. The audit identity A₁₂(t) = (t/2)·log 12 − g_Γ,ζ(t) says conductor 12's entire archimedean fingerprint is the linear term; the whole Lerch tail is ζ's own Γ(s/2) term verbatim. The tail carries a −½·t·log t origin singularity and the lattice constants γ and Catalan's G (ζ(2,1/4) = π² + 8G; ψ(1/4) = −γ − π/2 − 3 ln 2), while (ξ,η)-Gaussian moment structures and parabolic dipole matrix elements are algebraic in the station variable with purely rational constants (the KS bridge's skeleton is 32/81). In the common Cayley variable s = e^{−t/2} (= √(k/n) on a Gram entry): the tail is supported on exponents ≡ 1 (mod 4) with coefficients 16/(4m+1)² — exactly zero at s³, s⁷, s¹¹ where the KS squeeze overlap sech ψ = 2s/(1+s²) carries ∓2 on all odd powers. At the dipole's own station t = log 2, T = 1.440131107042578516… admits no closed form over {π, G, ln 2, γ, √2} [N]. For the Lerch tail the parabolic reading is not "permitted, not selected" — it is excluded.

Sharpest identity found [D, verified to ≤2.7e-51]: the tail's density is a bare geometric series in the Cayley variable, **−T″(t) = Σ_{m≥0} e^{−(4m+1)t/2} = s/(1−s⁴)**, poles at the 4th roots of unity (the weights conspire exactly: λ_m²·¼·(m+¼)⁻² = 1). Closed small-t forms upgrade the v14.416 audit's numerical fit to its exact limit: **A₁₂(t) = −½·t·log t + ½[1 − γ + log(6/π)]·t + o(t)**, linear coefficient 0.5349069592… (the fit was converging to it: 0.5337 at t=0.01). Surviving parallels are locational only [I]: Φ₁₂ is a sum over two discrete measures (primes + Hurwitz lattice), and in the (ξ,η) plane the KS bridge lives on the sum coordinate while the screw term lives on the ratio coordinate t = log(ξ/η) — complementary coordinates, which is why no moment identity transfers. Full text: payload `THREAD4.md` + `arch_ks_check.py` (mpmath, dps=50).

## §5 Open items carried forward [O]

1. Intrinsic finite c_a → c_∞ (the de Branges finite-calibration gate, v13.668 §7) — now the lane's most concrete finite problem.
2. Edge-mode test: restrict the χ/K Grams away from the truncation edge and re-measure λ₂ — artifact vs large-rapidity behavior.
3. λ₃ and higher modes of the three screws.
4. T_pair,A → T_pair convergence (resolvent/γ-field level; stays [C] on positivity).

## §6 Provenance

Scripts and results in the payload: `thread1_eigenmode.py`, `thread1_refresh.py`, `thread1_results.json`, `thread1_refresh_96128.json`, `thread2_scaling_d12.py`, `thread2_results.json`, Gram matrices `gram_chi_N96.npz`, `gram_chi_N128.npz`, `gram_K_N96.npz`, `gram_K_N128.npz`, `THREAD3.md`, `THREAD4.md`, `arch_ks_check.py`, `arch_ks_results.json`, consolidated note `EXPLORATION.md`. All computations were run in the sandbox workspace on 2026-10-15; the consolidation section of `EXPLORATION.md` is Phase 2 of that file.
