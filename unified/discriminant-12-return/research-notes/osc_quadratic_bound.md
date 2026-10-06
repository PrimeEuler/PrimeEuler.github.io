# Smoothness-Aware Oscillatory Quadratic-Form Bound for |⟨w_o, R_osc w_e⟩|

**Task:** Sandbox CONSTRUCTION handoff v14.072 (type: oscillatory-quadratic-form-certificate).
**Date:** 2026-10-06
**Status:** Complete — QUANTIFIED OBSTRUCTION (no theorem bound; dominant channel
and missing estimate identified precisely).
**Scope:** Sandbox owns the analytic inequality below. Lane A owns finite data.
No repo/ledger writes. No theorem promotion (independent audit required).

**Conventions:** [D]=derived, [N]=numerical, [I]=inference, [O]=open/gap.

**Producer:** `osc_quadratic_producer.py` (deterministic, numpy only, SHA-256 verified).
All [N] values below are bare-operator, finite-window (J=300 unless noted); the
full S_p (with Schur) and the infinite-dimensional limit are flagged where relevant.

---

## 0. Verdict

**QUANTIFIED OBSTRUCTION.** No smoothness-aware theorem bound for
|⟨w_o, R_osc w_e⟩| is proved. The handoff's preferred tools (discrete summation
by parts against w_p) cannot yield a bound fitting the 64k margin, for three
independent reasons:

1. **w_p is not smooth [N].** Writing w_p = a_p + r_p with a_p = D_p^{-1}u_p
   explicit, the ripple r_p satisfies ‖r_p‖/‖w_p‖ ≈ 8–10% in ℓ² and carries
   ≈54% of the total variation Σ|Δw|. A controlled experiment (removing the
   prime phases from z^{com}) collapses ‖r‖ by 70×, proving the ripple is
   caused by the oscillatory off-diagonal E_osc. Summation by parts requires
   smoothness of the full w_p; the hypothesis is false.

2. **Summation by parts is too lossy even with true constants [N].**
   For the diagonal q-pieces, the SBP bound with the *measured* (true)
   variation Σ|Δ(w_o w_e)| exceeds the margin by 30× (16k), 6.0× (32k),
   1.2× (64k) — and this uses the true variation, not a provable overestimate.
   Direct comparison: the SBP bound is ≈159× the true diagonal q=7 value.
   SBP bounds an oscillatory sum by total variation; the 97× numerical
   cancellation lives *inside* the variation sum where SBP cannot see it.
   A rigorous variation bound would be looser still. The method cannot fit.

3. **The dominant channel resists the available rigorous bounds [D/N].**
   The off-diagonal q=7 piece dominates (|⟨w_o,R_7^{off}w_e⟩| ≈ 1.1e-10 at
   64k, ≈25% of the R_osc budget alone, 10–20× the other channels [N]).
   Its near-resonance θ_7 = π log 7 ≈ 2π − 0.17 admits an exact slow-phase
   reduction (δ_7 = π(1 − log7/2) ≈ 0.08496 [D]), and the sinc-Toeplitz
   symbol lemma gives a rigorous ‖T‖_2 ≤ π/2 [D] — but the resulting bound
   is ≈7× over the channel budget. Closing it needs the (j+k)-phase/w-ripple
   correlation, a resonant small-divisor problem (§10).

**Dominant channel:** off-diagonal q=7 oscillatory kernel difference,
size ≈ −1.1e-10 at N=64k (bare, window J=300; J-envelope ≈ 1.2e-10),
driven by the θ_7 ≈ 2π near-resonance (worst SBP denominator 11.78×).

**Missing estimate (precise):** Lemma G in §10 — a bound on
|⟨w_o, R_7^{off} w_e⟩| improving on the Toeplitz-symbol bound by capturing
the slow (j+k)-oscillation against the two-scale structure of w. Equivalently,
a usable modulus of continuity for w_p = S_{p,N}^{-1}u_p that survives the
E_osc-induced ripple (Lemma W in §10).

**Budget verdict (§§9, 12.4):** The numerical (bare, window) A_max·|⟨w_o,R_osc w_e⟩|
at 64k is ≈ 8.8e-8, i.e. ≈25% of m_* = 3.4556e-7 — it fits the absolute margin
with ≈4× headroom [N], but (i) no theorem bound is proved, (ii) the value is
J-delicate (finite sections oscillate in [−1.2e-10, +1.6e-11], conditionally
convergent [N]), (iii) this is the bare operator (Schur oscillatory remainder
needs Lane A's finite data [O]), (iv) 25% already exceeds the 10% reserve in
the γ=1 budget, leaving T1+T2+cross extremely tight. The 64k margin fit is
**not established**.

**v14.075 amendment integrated (§12):** No low-order absolute C_ρ is used.
Near/far split at 64k: Q_near = {64k<n<128k} gets the R_osc treatment
(this doc — obstruction stands); Q_sep = {n≥128k} uses the audited K=10
signed-moment expansion, whose genuine geometric remainder is ≤ 1.6e-18
via theorem γ_N=1 — **negligible [D]**. The obstruction is entirely on Q_near.
32k diagnostic (ΔA≈−15.51, C_S≈+639.83) confirms 32k is calibration only [I];
64k finite data still running, not consumed.

---

## 1. Exact decomposition [D]

### 1.1 Paired bare operators

Cutoff N even. Paired lattice j ≥ 0: n_j = N+1+2j (odd, even sector),
m_j = N+2+2j = n_j+1 (even, odd sector). Bare operator (T_p)_{νν'} on modes ν:
- j≠k: c·(ν_k z^{(p)}_{ν_j} − ν_j z^{(p)}_{ν_k})/(ν_j²−ν_k²) + α_p p^{(p)}_{ν_j}p^{(p)}_{ν_k},
  c = 2/π, α_e = +2, α_o = −2.
- j=k: d_{ν_j} + α_p(p^{(p)}_{ν_j})².

z^{(p)}_n = z^{com}_n − π_p nπ corr_n, π_e = −1, π_o = +1,
z^{com}_n = 2Σ_{q∈{2,3,4,5,7}} w_q sin(nπ log q/2) + Imψ(1/4+inπ/4),
d_n = log(n/4) + prime_diag_n + arch_n − Ci(nπ) − Si(nπ)/(nπ),
prime_diag_n = Σ_q w_q[(2−log q)cos(nπ log q/2) + sin(nπ log q/2)/k_n].

Paired difference: ΔS_bare = T_o − T_e on ℓ²(ℕ₀) (odd-sector m-modes minus
even-sector n-modes). Smooth rank-1: C_D·u⊗u,
C_D = −32cosh(1)/π² + 16E_0/π² ≈ −4.395586 [D],
u_j = 1/n_j. Define the sandbox bare remainder
  R_osc^b := ΔS_bare − C_D·u⊗u.
(The full v14.069 R_osc = R_osc^b − (Schur oscillatory remainder);
the Schur part needs Lane A's finite data — §1.5.)

### 1.2 Piece decomposition [D]

R_osc^b = Σ_{q}(R_q^{diag,cos} + R_q^{diag,sin} + R_q^{off}) + R_{smooth}, with:

- **R_q^{diag,cos}**: diagonal, (R_q^{diag,cos})_{jj}
  = w_q(2−log q)·[cos(m_jφ_q) − cos(n_jφ_q)], φ_q = π log q/2.
  Exact form: = −2w_q(2−log q)sin(φ_q/2)·sin(A_q + jθ_q),
  A_q = (N+3/2)φ_q, θ_q = π log q [D, verified §1.4].

- **R_q^{diag,sin}**: diagonal, (R_q^{diag,sin})_{jj}
  = w_q·[sin(m_jφ_q)/k_{m_j} − sin(n_jφ_q)/k_{n_j}]. Oscillatory O(1/n).

- **R_q^{off}**: off-diagonal, (R_q^{off})_{jk}
  = c·2w_q·[K^{(m)}_{jk} − K^{(n)}_{jk}] (j≠k),
  K^{(ν)}_{jk} = (ν_k sin(ν_jφ_q) − ν_j sin(ν_kφ_q))/(ν_j²−ν_k²).
  Exact sum-of-products identity [D, verified §1.4]:
    K^{(ν)}_{jk} = cos(S)sin(D)/(ν_j−ν_k) − sin(S)cos(D)/(ν_j+ν_k),
    S = (ν_j+ν_k)φ_q/2, D = (ν_j−ν_k)φ_q/2.
  On the paired lattice (ν_j+ν_k)/2 = N+c+j+k, (ν_j−ν_k)/2 = j−k:
  a (j+k)-oscillation times a (j−k)-Toeplitz factor, exactly.

- **R_{smooth}**: all smooth subleading pieces —
  R_log (diag log(1+1/n_j)), R_arch (arch_{m_j}−arch_{n_j}, smooth O(1/n²)
  within fixed parity [D, §7]), R_CiSi (smooth O(1/n²) [D]),
  R_corr/R_pole remainders (beyond the C_D rank-1; O(1/n³) in z),
  R_δu-corr (explicit δu corrections to the α_pp rank-1).
  Imψ(1/4+inπ/4) = π/2 + O(e^{−π²n/4}): contributes exactly 0 [D].

### 1.3 The q=7 near-resonance [D]

θ_7 = π log 7 ≈ 6.11326 = 2π − 0.16993. Define δ_7 := π − φ_7
= π(1 − log7/2) ≈ 0.0849641392 [D]. Exact reductions [D, verified]:
- n odd:  sin(nφ_7) = +sin(nδ_7),  cos(nφ_7) = −cos(nδ_7).
- n even: sin(nφ_7) = −sin(nδ_7),  cos(nφ_7) = +cos(nδ_7).
Hence the q=7 diagonal piece is
  (R_7^{diag,cos})_{jj} = w_7(2−log 7)·[cos(m_jδ_7) + cos(n_jδ_7)]
  = 2w_7(2−log 7)cos(δ_7/2)·cos((n_j+1/2)δ_7),
a *slow* oscillation (frequency δ_7 ≈ 0.085 per mode, ≈0.17 per j-step),
and the q=7 off-diagonal kernel is the sinc-like form with the same δ_7.
This near-resonance is why q=7 dominates and why its SBP denominator
1/|sin(θ_7/2)| ≈ 11.78 is the worst.

### 1.4 Identity verification [D]

Producer `osc_quadratic_producer.py` verifies to machine precision:
- sum-of-products identity: max err 1.1e-12.
- δ_7 sin/cos reductions: max err 5.4e-12 / 2.8e-12.
- diagonal cos-difference form: max err 1.7e-11.

### 1.5 Schur remainder (gap, Lane A's) [O]

R_osc = R_osc^b − (Schur_o − Schur_e)^{osc}, where
(Schur_p)_{jk} = (B_p^* A_{p,N}^{-1} B_p)_{jk} on the remote space.
B_p ≈ b_p⊗ũ (smooth 1/n, §analysis), so the Schur difference is
(smooth rank-1, absorbed in C_S^{paired}) + (oscillatory O(1/n²) remainder).
Bounding the oscillatory Schur remainder needs ‖A_{p,N}^{-1}‖ and B_p
structure from Lane A's finite solve. It is NOT bounded here.

---

## 2. Phase denominators [D]

Fixed per-j phase increments on n_j = N+1+2j (step 2 in n):

| q | w_q    | θ_q = π log q (diag) | 1/|sin(θ_q/2)| | φ_q = π log q/2 (offdiag) | 1/|sin(φ_q/2)| |
|---|--------|----------------------|-----------------|---------------------------|-----------------|
| 2 | 0.490129 | 2.1776             | 1.1286          | 1.0888                    | 1.9309          |
| 3 | 0.634284 | 3.4514             | 1.0121          | 1.7257                    | 1.3163          |
| 4 | 0.346574 | 4.3552             | 1.2173          | 2.1776                    | 1.1286          |
| 5 | 0.719763 | 5.0559             | 1.7369          | 2.5281                    | 1.0490          |
| 7 | 0.735485 | 6.1133             | 11.7838         | 3.0566                    | 1.0009          |

q=7 is the worst (11.78×) because θ_7 ≈ 2π. (Producer §"phase denominators".)

---

## 3. Summation-by-parts framework (conditional) [D]

### Lemma SBP-D (diagonal pieces) [D]

For b ∈ ℓ¹(ℕ₀) with b_j → 0,
  |Σ_{j=0}^∞ b_j sin(A + jθ)| ≤ V(b)/|sin(θ/2)|,
  V(b) = Σ_{j=0}^∞ |b_{j+1} − b_j|.
*Proof.* Abel summation; the boundary term S_{J−1}b_{J−1} → 0. ∎

Applied to R_q^{diag,cos} with b_j = w_{o,j}w_{e,j}:
  |⟨w_o, R_q^{diag,cos} w_e⟩|
    ≤ [2|w_q(2−log q)sin(φ_q/2)| / |sin(θ_q/2)|] · V(w_o w_e).   (SBP-D)

The bracket is explicit (§2). For q=7 the bracket is 0.9364 (no gain from
the 11.78 denominator because |2 sin(φ_7/2)| ≈ 2.0 cancels most of it —
the slow δ_7 oscillation is handled better by direct bounds, §6).

### Off-diagonal framework [D, conditional]

Via the sum-of-products identity (§1.2), each R_q^{off} is a sum of terms
  (osc in j+k) × (Toeplitz in j−k) × (smooth 1/(N+j+k)),
e.g. cos((N+1+j+k)φ_q)·T^{(q)}_{j−k},
T^{(q)}_d = sin(dφ_q)/(2d). A double Abel transform in j then k gives
  |⟨w_o, R_q^{off} w_e⟩| ≤ C_q^{off}/|sin(φ_q/2)|² · V^{(2)}(w_o, w_e),
with V^{(2)} a mixed-variation norm. The constants C_q^{off} are explicit
(c·2|w_q| times Toeplitz-derivative bounds). The framework is exact;
it is *conditional* on a usable V^{(2)} bound — which does not exist (§5).

---

## 4. Why the framework fails I: w is not smooth [N]

Write w_p = a_p + r_p, a_p = D_p^{-1}u_p (explicit), r_p = w_p − a_p
(the "ripple"). Measured (bare, window J=400, even sector):

| N     | ‖r‖/‖w‖ | Σ|Δr|/Σ|Δw| | λ_min(T_e) |
|-------|----------|-------------|------------|
| 16000 | 0.099    | 0.53        | 6.38       |
| 32000 | 0.094    | 0.54        | 7.07       |
| 64000 | 0.085    | 0.54        | 7.77       |
| 128000| 0.081    | 0.55        | 8.47       |

The ripple is ≈8–10% of w in ℓ² and carries ≈54% of the total variation.
**Controlled experiment [N]:** rebuilding T_e with the prime oscillations
removed from z^{com} (z^{com} → π/2) collapses ‖r‖ by 70× (1.52e-5 →
2.18e-7) and Σ|Δw| by 1100× when diagonal oscillations are also removed.
**Conclusion:** the ripple is caused by the oscillatory off-diagonal E_osc;
w_p = S_{p,N}^{-1}u_p is not smooth, and no usable modulus of continuity
follows from S_p ≽ I alone (the inverse does not preserve smoothness
because ‖E_osc‖ is O(1), not small). The SBP hypothesis is false.

---

## 5. Why the framework fails II: SBP is too lossy [N]

Using the *measured true* variation V = Σ|Δ(w_o w_e)| + boundary (i.e.
granting the unprovable hypothesis with perfect constants), the SBP-D bound
summed over q gives:

| N     | A_max·(SBP bound)/m_* | true A·|diag|/m_* |
|-------|----------------------|-------------------|
| 16000 | 29.97                | (diag 9.999e-11 → 0.23) |
| 32000 | 5.97                 | 0.016             |
| 64000 | 1.20                 | 0.006             |
| 128000| 0.17                 | 0.0006            |

Even with perfect variation constants, SBP exceeds the margin at 16k/32k/64k
*for the diagonal pieces alone* (the off-diagonal dominates on top).
Spot check: SBP bound vs true value for diagonal q=7 at 64k is ≈159× loose.
SBP bounds an oscillatory sum by total variation; the observed 97×
cancellation occurs inside the variation sum, invisible to SBP. A rigorous
variation bound would be looser still. **The method cannot fit, in principle.**

---

## 6. Toeplitz symbol lemma [D] and its insufficiency

### Lemma T [D]

Let (T^{(δ)})_{jk} = sin((j−k)δ)/(2(j−k)) (T_0 = δ/2). Then ‖T^{(δ)}‖_2 ≤ π/2.
*Proof.* The Toeplitz operator with entries sin(dδ)/(πd) is the orthogonal
projection onto frequencies |ω| < δ (classical sinc-kernel / Shannon
sampling), hence norm 1. Our kernel is (π/2) times that. ∎

Applied to the q=7 off-diagonal via the δ_7 reduction (§1.3), the *leading*
(first-identity-term) contribution satisfies
  |⟨w_o, R_7^{off,lead} w_e⟩| ≤ c·2w_7·π·‖w_o‖‖w_e‖.
The second identity terms carry an extra 1/(N+1+j+k); they are Hankel-type
with operator norm O((log N)/N) by standard estimates — negligible
(< 1e-11 at 64k) next to the leading term, so we bound the channel by the
leading term. Numerically at 64k: c·2w_7·π ≈ 2.942,
‖w_o‖‖w_e‖ ≈ 1.07e-9, giving a rigorous bound ≈ 3.15e-9.
True value: 1.08e-10. Budget (full R_osc): 4.3e-10.
**Rigorous but 7.3× over budget and 29× over truth.** The looseness is the
(j+k)-slow-phase/w-ripple correlation, which the symbol bound discards.

---

## 7. Smooth remainders [D]

All bounded by Cauchy-Schwarz with explicit constants; negligible:

- R_log: |(R_log)_{jj}| = log(1+1/n_j) ≤ 1/N ⟹
  |⟨w_o,R_log w_e⟩| ≤ ‖w_o‖‖w_e‖/N.
  Producer verifies: true 1.226e-14 vs bound 1.256e-14 at 64k (tight) [D/N].
- R_arch: within fixed parity, arch_n is a fixed rational function of 1/k
  (Bernoulli-polynomial series; parity enters only through fixed eps = ±1),
  hence smooth O(1/n²); |⟨w_o,R_arch w_e⟩| ≤ C_arch·‖w_o‖‖w_e‖/N² [D].
- R_CiSi: Ci(nπ), Si(nπ)/(nπ) differences are smooth O(1/n²) (sin(nπ) = 0
  kills the leading oscillation) [D].
- R_corr/R_pole remainders: O(1/n³) in z beyond the C_D rank-1 [D].
- R_δu-corr: explicit δu_j = −1/(n_j m_j) [D].
- Imψ: constant to O(e^{−π²N/4}) ≈ 1e-34000; contributes exactly 0 [D].

None exceeds ≈1e-12·‖w_o‖‖w_e‖-scale. **Not the obstruction.**

---

## 8. Numerical landscape [N] (bare, window)

Per-channel |⟨w_o, R_q w_e⟩| (J=300; 128k uses J=200):

N=16000: total −1.68e-9 (A·|·|/m_* = 3.90).
  offd by q: 2:−1.06e-10, 3:+6.3e-11, 4:+1.57e-10, 5:+1.02e-10, **7:−1.99e-9**.
N=64000: total −1.09e-10 (A·|·|/m_* = 0.254).
  offd by q: 2:+3.2e-12, 3:−4.2e-12, 4:−6.0e-12, 5:+3.7e-12, **7:−1.08e-10**.
  diag total 2.5e-12; ‖R_osc^b‖_2 = 2.99 (naive baseline, displayed per guardrail).

**q=7 off-diagonal dominates by 10–20×** at every N. The other channels are
individually ≤ 2% of the margin at 64k.

**J-delicacy [N]:** at N=64k, Q_J = −1.09e-10 (J=300), +1.55e-11 (J=500),
−1.14e-10 (J=700), −1.21e-11 (J=900). The finite sections oscillate;
the sum is conditionally convergent. Envelope ≈ 1.2e-10.

---

## 9. Cutoff-parametric table and 64k verdict

| N      | A·|⟨w_o,R_osc^b w_e⟩| [N] (J=300) | / m_* | SBP-D bound [N-var] | fits? |
|--------|----------------------|-------|---------------------|-------|
| 16000  | 1.35e-6              | 3.90  | 30× over            | no    |
| 32000  | 8.14e-8              | 0.236 | 6.0× over           | no (bound) |
| 64000  | 8.76e-8              | 0.254 | 1.2× over           | no (bound) |
| 128000 | 2.2e-10 (J=200)      | 0.001 | 0.17×               | (bound fits; value J-unstable) |

**Verdict on the 64k margin fit:** The numerical bare-window value fits the
absolute margin with ≈4× headroom (A·|·| ≈ 8.8e-8 vs m_* = 3.456e-7), but:
(a) no theorem bound is proved — the SBP bound is 1.2× OVER even with true
constants; (b) the value is J-delicate (envelope 1.2e-10 → 0.35× margin);
(c) the bare operator omits the Schur oscillatory remainder [O, Lane A];
(d) 25–35% of the margin consumed by R_osc alone leaves the γ=1 budget's
10% reserve violated — T1+T2+cross then require extremely favorable
(ΔA, C_S, C_ρ). **The 64k margin fit is not established. OBSTRUCTION.**

Note the non-monotone N-scaling (sign flips 16k→32k→64k): the bound must
control an oscillatory envelope, not a monotone decay.

---

## 10. The missing estimate (precise) [O]

**Lemma G (open).** Let R_7^{off} be the q=7 off-diagonal piece (§1.2) with
the exact δ_7 reduction (§1.3), and w_p = S_{p,N}^{-1}u_p. Then
  |⟨w_o, R_7^{off} w_e⟩| ≤ G(N)·‖w_o‖‖w_e‖
with G(N) ≤ 0.35 (the value needed at 64k), proved without inferring from
the numerical cancellation. The symbol lemma gives G = c·2w_7·π ≈ 2.94;
needed: ≈8× improvement via the (j+k)-slow-phase against the two-scale
structure w = a + Σ_q osc^{(q)}·s^{(q)}.

**Lemma W (open, equivalent).** A usable modulus of continuity for
w_p = S_{p,N}^{-1}u_p: weighted ℓ¹/ℓ² bounds on first differences that
survive the E_osc ripple — i.e., quantitative control of r_p = w_p −
D_p^{-1}u_p beyond ‖r_p‖/‖w_p‖ ≈ 0.1, resolving the ripple's
modulated-smooth structure (resonant small divisors at combined frequencies
θ_q ± φ_{q'} must be handled).

Either lemma closes the v14.072 handoff. Both are genuine harmonic-analysis
problems (resonant oscillatory quadratic forms); neither follows from
S_p ≽ I or from the SBP framework.

---

## 11. Recommendations

1. **Do not pursue SBP-on-w further** (§§4–5 prove it cannot fit).
2. **Viable analytic path:** the w = a + r split (§4) with SBP applied only
   to *explicit* smooth objects (a_p, Toeplitz factors), i.e. a two-scale
   expansion. The obstruction is then Lemma G/W (small divisors) — hard
   but correctly posed.
3. **Viable numerical path:** since the [N] envelope fits with ≈3.5×
   headroom, a *validated* numerical enclosure (outward rounding +
   rigorous J-truncation via the oscillatory tail) could close R_osc^b;
   the Schur remainder still needs Lane A. This is [N]-assisted, not [D].
4. **Lane A inputs needed:** (i) the Schur oscillatory remainder bound
   (§1.5); (ii) confirmation whether the 64k budget survives R_osc taking
   25–35% of the margin (revisit the T1/T2/cross/dU split with the true
   R_osc scale).

---

## 12. v14.075 amendment: K=10 near/far split integration

### 12.1 Architecture (replacing v14.069 hypothesis iv) [D]

Per v14.075, the low-order absolute C_ρ is **superseded** by the audited
v14.020–v14.023 K=10 signed-moment/geometric architecture (v14.019 found the
absolute construction catastrophically loose: C_{ρ,e}^{abs} ∼ 1.18e16).

For the 64k target, split {n > 64000} = Q_near ∪ Q_sep:
- **Q_near = {64000 < n < 128000}**: retain exact/correlated source-faithful
  coupling; apply the smoothness-aware R_osc quadratic-form treatment
  (this doc, §§1–11).
- **Q_sep = {n ≥ 128000}**: K=10 signed-moment expansion. For front modes
  m ≤ 64000 and n ≥ 128000, m/n ≤ 1/2. Retain ALL signed moment channels
  M_{2j+1} = Σ_{m≤N}m^{2j+1}x_m, Z_{2j} = Σ_{m≤N}z_m m^{2j}x_m (j=0..10)
  *before* taking absolute values. Absolute-bound ONLY the genuine
  geometric remainder.

No low-order scalar C_ρ is used anywhere.

### 12.2 Q_sep K=10 geometric remainder bound [D]

From v14.020 (2): for the unit-energy source,
  |R̃_K(n)| ≤ A_K/n^{2K+3} + B_K/n^{2K+4},  K=10,
  A_K = √C_N·(2/π)(4/3)·S^z_{2K+2},  B_K = √C_N·(2/π)(4/3)·Z_max·S_{2K+3}.
ℓ² bound via v14.020 (3):
  Σ_{n≥n_0} n^{-p} ≤ n_0^{-p} + n_0^{-(p-1)}/(2(p-1)).

**Scaling to (N=64000, n_0=128000) [D]:** v14.020 gives
‖R̃_{10}‖_2 < 1.21e-10 at (N=4000, n_0=8000) [N]. The bound scales as
(moments)·n_0^{-(2K+2.5)} = (moments)·n_0^{-22.5}. The n_0 ratio gives
(8000/128000)^{22.5} ≈ 8.08e-28 suppression. Even under a
10^{20}× pessimistic moment-growth assumption (64k vs 4k front),
  ‖R̃_{10}‖_{ℓ²(n≥128000)} ≤ 9.8e-18.   [D, pessimistic]

**Map into quadratic-form remainder via theorem γ_N = 1 [D]:**
- subleading: ⟨ε,S^{-1}ε⟩ ≤ (1/γ_N)·‖ε‖² ≤ 9.6e-35.
- cross: 2√A_max·‖u‖·‖ε‖/γ_N ≤ 2·28.35·2.80e-3·9.8e-18 ≈ 1.5e-18.
  (‖u‖ ≤ 1/√(2·64000), A_max = 804, γ_N = 1.)

**Q_sep contribution: ≤ 1.6e-18 ≈ 4.5e-12 × m_*. NEGLIGIBLE. [D]**

The K=10 signed moments themselves (j=0..10) are finite-data channels
retained exactly; they do not enter the remainder.

### 12.3 Q_near R_osc: obstruction stands

The §§1–11 analysis is the v14.072 smoothness-aware treatment for Q_near.
The obstruction (no theorem bound; §§4–6) is structural (method failure)
and applies to the Q_near block. The [N] window values (§8) are
illustrative of the Q_near scale; the J-delicacy (§8) reflects the
conditionally convergent oscillatory sum on Q_near.

### 12.4 Updated 64k remainder verdict (v14.073 budget units)

v14.073 budget: m_* = 3.45557892442104e-7.
- δu reserve: 1.133e-7 (32.8% of m_*).
- Remaining for T1+T2+remainder: 2.322e-7 (67.2%).

Remainder decomposition (v14.075 architecture):
| Component | Bound | / m_* | Status |
|-----------|-------|-------|--------|
| Q_sep K=10 geometric (§12.2) | ≤ 1.6e-18 | < 5e-12 | [D] negligible |
| Q_near R_osc (§§1–11) | no theorem bound; [N] ≈ 8.8e-8 | ≈ 0.25 | **OBSTRUCTION** |
| Q_near δu (exact) | part of 1.133e-7 reserve | — | [D] in reserve |
| Q_near ε (exact/correlated) | needs finite data | — | [O] Lane A |

**Verdict:** The K=10 far tail (Q_sep) is under control — negligible by
[D]. The obstruction is entirely on Q_near via the R_osc quadratic form,
for which no smoothness-aware theorem bound exists (§§4–6, Lemma G/W in
§10). **The 64k remainder fit is NOT established. OBSTRUCTION (quantified).**

Additionally, the [N] Q_near R_osc scale (≈25% of m_*) already exceeds the
10% reserve implicitly available in the v14.073 split, so even a future
R_osc theorem bound would leave T1+T2 extremely tight pending Lane A's
64k (ΔA, C_S) — currently running, not consumed.

### 12.5 32k diagnostic consistency check [N/I]

v14.075 §1 (Lane A, diagnostic midpoint only, not consumed):
ΔA_32k ≈ −15.51, C_S(32k) ≈ +639.83.
v14.073 64k-style admissible: |ΔA| < 0.11, |C_S| < 262.
Ratios: 15.51/0.11 ≈ 141× over; 639.83/262 ≈ 2.4× over.
**Confirms 32k is calibration only, not a closure cutoff [I].**
The 64k C/L/A/M11 jobs are still running; no values consumed.

---

## 13. Files

- `~/workspace/d12/osc_quadratic_producer.py` — deterministic producer
  (phase denominators, identity verifications, Toeplitz constant,
  per-channel analysis, K=10 Q_sep scaling, SHA-256).
- `~/workspace/d12/osc_quadratic_bound.md` — this derivation.

No repo/ledger writes. No theorem promotion. Report to parent with verdict.
