# Thread 4 — The χ₁₂ Archimedean Screw Term vs the Parabolic/KS Dipole Computation

**Date:** 2026-10-15. **Track:** sandbox ("our Lane B"), thread 4 of 4.
Workspace-only; nothing ledgered.
**Question:** does the archimedean term of the D12 screw admit a
parabolic-coordinate reading — as a dipole-type matrix element or a
(ξ,η)-Gaussian moment of the same kind that produced 32/81 and the
−4/3 KS bridge — or is the resemblance only notational?

**Verdict (up front): only notational — and stronger than "unproven":
the parabolic reading is structurally excluded for the Lerch tail, by
function class [D].** The archimedean term is the Mellin shadow of
Γ(s/2): a saturating-ramp sum over the Hurwitz lattice {m + 1/4}. Its
constants are γ and Catalan's G, its origin behaviour is −½ t log t,
and its density in the station variable is a meromorphic geometric
series — none of which any polynomial×Gaussian (ξ,η) moment or
parabolic bound-state matrix element can produce. Independently of
that, the term is *entirely ζ-shared* except for the single linear
conductor piece (t/2)·log 12, so even a hypothetical reading would
belong to Γ(s/2), not to conductor 12 or the cone.

Grounding: ledger v13.258 §§2–3 (Suzuki specialization), the
v14.416 audit identity A₁₂ = −g_Γ,ζ + (t/2) log 12,
`../suzuki_riemann_screw_calibration.py` (g_Γ,ζ),
`../../parabolic-dipole/bch-squeeze-derivation.md`,
`../../parabolic-dipole/ks-bridge-first-principles.md`,
`../../../Unit_Circle_Encoding_and_Hyperbolic_Cone_Form.md` (§§6–8).
All numerics: `arch_ks_check.py` in this folder (mpmath, dps = 50),
results in `arch_ks_results.json`.

Markings: [D] derived · [N] numerical · [C] conditional ·
[I] interpretation · [O] open.

---

## 1. The archimedean term, isolated

From v13.258 §3, for t ≥ 0, with Φ the Hurwitz–Lerch transcendent:

$$
\mathcal A_{12}(t)
=\frac{t}{2}\Bigl[\psi\!\left(\tfrac14\right)+\log\frac{12}{\pi}\Bigr]
+\frac14\Bigl[\zeta\!\left(2,\tfrac14\right)
-e^{-t/2}\,\Phi\!\left(e^{-2t},2,\tfrac14\right)\Bigr].
$$

### 1a. The split: one conductor piece, everything else ζ-shared [D]

The v14.416 audit identity A₁₂(t) = −g_Γ,ζ(t) + (t/2)·log 12
(re-verified here to ≤ 2.2e-16 at t = 0.3, 1.0, 2.0, 3.5 [N]) splits
the term as

| piece | form | status |
|---|---|---|
| pure conductor | $\frac{t}{2}\log 12$ | the **only** place 12 enters [D] |
| ζ-shared linear | $\frac{t}{2}\bigl[\psi(1/4) - \log\pi\bigr]$ | part of −g_Γ,ζ |
| Lerch tail | $T(t) := \frac14\bigl[\zeta(2,\frac14) - e^{-t/2}\Phi(e^{-2t},2,\frac14)\bigr]$ | part of −g_Γ,ζ, **verbatim ζ's** |

So χ₁₂ contributes *nothing* archimedean beyond the linear
(t/2)·log 12. At field level the same tail appears with coefficient
1/2 = 2 × 1/4 (v13.258 §7) — one copy per Γ(s/2) factor, by the
additivity Φ_K = Φ_ζ + Φ₁₂. The tail is a property of the single
gamma factor Γ(s/2), shared by ζ and by every even degree-1 L with
that factor. Any "reading" of the tail is a reading of Γ(s/2).

The two constants are classical [D identities, N-verified to
50 digits]:

$$
\zeta\!\left(2,\tfrac14\right) = \pi^2 + 8G = 17.197329154507110739\ldots,
\qquad
\psi\!\left(\tfrac14\right) = -\gamma - \frac{\pi}{2} - 3\ln 2
= -4.227453533376265408\ldots
$$

(G = Catalan's constant; γ = Euler–Mascheroni.) Note already: the
tail's value at infinity is T(∞) = ζ(2,1/4)/4 = (π² + 8G)/4
= 4.299332288626777685… — transcendental constants of lattice-sum
type, before any dynamics.

### 1b. The tail in the natural variable: a diagonal Laplace series [D]

With Φ(z,2,a) = Σ_{m≥0} z^m/(m+a)², at z = e^{−2t}, a = 1/4:

$$
e^{-t/2}\,\Phi\!\left(e^{-2t},2,\tfrac14\right)
=\sum_{m\ge0}\frac{e^{-2(m+1/4)\,t}}{(m+1/4)^2}
=\sum_{m\ge0}\frac{e^{-(4m+1)t/2}}{(m+1/4)^2}.
$$

(Series = Lerch value to ~1e-50 at t = 0.4, 1.0, 2.0 [N].) Terms
identified:

- **lattice:** the Hurwitz translates m + 1/4, m = 0, 1, 2, …;
- **rate:** λ_m = 2(m + 1/4) = (4m+1)/2 — the rate is *exactly twice
  the lattice point* (a "diagonal" Laplace series: point λ/2 carries
  e^{−λt}/(λ/2)²);
- **weight:** (m + 1/4)^{−2} = 16/(4m+1)².

Equivalently, as a saturating-ramp sum [D; N-verified — §5]:

$$
T(t)=\frac14\sum_{m\ge0}
\frac{1-e^{-2(m+1/4)t}}{(m+1/4)^2},
$$

the same formal shape as the prime ramp
R₁₂(t) = Σ_n c_n (t − log n)₊, but with the linear ramp kernel
(t − ·)₊ replaced by the saturating kernel (1 − e^{−λt}) and the
prime measure replaced by the Hurwitz-lattice measure
(1/4)(m+1/4)^{−2} δ(λ − 2(m+1/4)).

### 1c. The density is a bare geometric series [D — sharpest identity]

Differentiating twice, the weights conspire exactly:
λ_m² · (1/4) · (m+1/4)^{−2} = 1 for every m, so

$$
\boxed{\;-\,T''(t)=\sum_{m\ge0} e^{-(4m+1)t/2}
=\frac{e^{-t/2}}{1-e^{-2t}}=\frac{s}{1-s^{4}},\qquad s:=e^{-t/2}.\;}
$$

[N-verified: at t = 0.3, 1.0, 2.0 the values 1.907646662191906655,
0.701463408826254407, 0.374743100475801736 agree with mpmath's
numerical T″ and with the geometric sum to ≤ 2.7e-51.] So the tail
is, up to its linear term, the two-fold integral of a *geometric
series in the station variable s*, supported on the exponents
4m + 1. (The linear term is not optional bookkeeping: T′(t) → ∞
like −½ log t at the origin, §1d.) In the dictionary's Cayley variable (§8 of the
note), s is exactly the Cayley argument: on a station-Gram entry
(n, k), t = log(n/k) and s = √(k/n). The pole of s/(1−s⁴) at s = 1
is the t → 0 singularity; the other poles sit at s = −1, ±i, the
4th roots of unity — the gamma factor's pole lattice, seen in the
s-plane.

### 1d. Small-t expansion [D, N-verified]

The s = 1 Lerch degeneration Φ(e^{−μ},1,a) = −log μ − ψ(a) − γ + o(1)
(verified numerically at a = 1/4: Φ(e^{−μ},1,1/4) + log μ →
3.6502378684747325475 = π/2 + 3 ln 2 = −ψ(1/4) − γ) gives, via
z∂_z Φ(z,2,a) = Φ(z,1,a) − aΦ(z,2,a):

$$
T(t)=-\tfrac12\,t\log t+\kappa\,t+o(t),
\qquad
\kappa=\tfrac12+\tfrac{\pi}{4}+\ln 2=1.978545343957393619\ldots
$$

(the ζ(2,¼)-contributions to κ from the e^{−t/2} prefactor and from
the aΦ term cancel identically — an automatic (a, λ)-identity, not
1/4-numerology), and hence

$$
\mathcal A_{12}(t)=-\tfrac12\,t\log t+c\,t+o(t),
\qquad
c=\tfrac12\bigl[\,1-\gamma+\log(6/\pi)\bigr]=0.534906959238560983\ldots
$$

[N: (T + ½t log t)/t at t = 10^{−1..−4} reads 1.96608, 1.97730,
1.97842, 1.97853 → κ; (A₁₂ + ½t log t)/t reads 0.52244, 0.53366,
0.53478, 0.53489 → c. This upgrades the v14.416 audit's fitted
c ≈ 0.535 to a closed form.] Two facts to carry into §2: the
**log coefficient −1/2 does not involve the shift 1/4 at all**
(it is −(λ/2)·(1/λ) at λ = 1/2), and the surviving constants are
γ, π, ln 2, ln 3 — lattice/digamma constants.

---

## 2. The attempted parabolic reading

### 2a. What the KS side's generating structures actually are [D]

From the two parabolic-dipole documents, the KS computation has
exactly three kinds of analytic object:

1. **Gaussian moments.** Under e^{−a(A+B)} (A = u₁²+u₂²,
   B = u₃²+u₄²), ⟨u_i^{2j}⟩ = (2j−1)!!/(2a)^j. At the dipole's
   a = 3/2 (the pair (n,k) = (2,1), squeeze D(√2), ψ_{2,1} = ½ ln 2,
   ⟨u_i²⟩ = 1/(n+k) = 1/3): the moment sequence is
   1, 1/3, 1/3, 5/9, 35/27, … — pure rationals, double-factorial
   combinatorics.
2. **Squeeze overlaps.** d₀² = sech ψ; in the variable s = e^{−ψ},
   sech ψ = 2s/(1+s²) = 2 Σ_j (−1)^j s^{2j+1} — support on **all**
   odd powers, coefficients **±2**; per-mode overlap
   (sech ψ)^{1/2} = (2s)^{1/2}(1+s²)^{−1/2} — *algebraic* in s,
   branch points at s = ±i, analytic at s = 1.
3. **The bridge.** B = −½·(I₂/I₀) with I₂/I₀ = 8/3: a ratio of
   u²-weighted to unweighted polynomial×Gaussian integrals. Pure
   rational; π cancels identically; matrix-element dependent
   (Stark case 3/2, not 4/3). The full dipole value at its station
   is the rational skeleton 32/81 = 2⁵/3⁴ × bridge (−4/3) × node
   sign = −128/243.

Every constant on this side is a rational in the {2,3} alphabet;
γ and G occur nowhere; no logarithm of a variable occurs anywhere
(the only log is the constant ψ_{2,1} = ½ ln 2 fixing the station).

### 2b. Side-by-side in the common variable s

Both sides can be written in s = e^{−t/2} (resp. e^{−ψ}) — this is
the whole of the notational resemblance. The Lerch factor
L(s) := e^{−t/2}Φ(e^{−2t},2,1/4) = Σ_m s^{4m+1}/(m+1/4)² versus
d₀² = sech ψ:

| power of s | 1 | 3 | 5 | 7 | 9 | 11 | 13 |
|---|---|---|---|---|---|---|---|
| tail L(s) | 16 | **0** | 16/25 | **0** | 16/81 | **0** | 16/169 |
| sech ψ | 2 | −2 | 2 | −2 | 2 | −2 | 2 |
| Gaussian moments ⟨u^{2j}⟩ (index j) | 1 (j=0) | — | 1/3 (j=1) | — | 1/3 (j=2) | — | 5/9 (j=3) |

### 2c. The mismatches [D]

1. **Support.** The tail lives on exponents ≡ 1 (mod 4); sech lives
   on all odd exponents; the tail is exactly zero at s³, s⁷, s¹¹
   where the squeeze overlap is ∓2. The mod-4 support is the period
   of 1/(1−s⁴) — i.e. of z = e^{−2t} = s⁴, the Mellin variable of
   Γ(s/2) (the 2 is 1/λ, λ = 1/2). It is gamma-factor data, present
   for every Γ(s/2)-factored L, not a (ξ,η) or conductor-12 feature.
2. **Coefficient law.** Inverse-square decay 16/(4m+1)² → 0, vs
   constant-modulus ±2 (sech), vs double-factorial growth
   (2j−1)!!/3^j (moments). Consecutive-coefficient ratios are
   [(4m+1)/(4m+5)]² on one side and double-factorial/binomial
   rationals on the other; no choice of Gaussian width a or station
   (n,k) reconciles the families — they are different sequences,
   not different parametrizations of one sequence.
3. **Singularity class.** The tail's density −T″ = s/(1−s⁴) is
   *meromorphic* with poles at the 4th roots of unity; T itself has
   a t log t term at t = 0 (§1d). Every KS object is algebraic in s
   or a rational moment ratio — analytic at s = 1, no variable
   logarithm anywhere. A polynomial×Gaussian integral is analytic
   in all parameters (width, squeeze, station); it cannot produce
   a t log t term or a pole at s = 1. **This alone excludes the
   reading.**
4. **Constants.** The tail forces γ (in ψ(1/4), in κ) and Catalan's
   G (in ζ(2,1/4) = π² + 8G; G is precisely the 1/4-vs-3/4
   asymmetry of the odd lattice: ζ(2,3/4) = π² − 8G [N-verified]).
   Gaussian moments are rational in the width; the KS bridge's π
   cancels; γ and G cannot be manufactured by any (ξ,η)-Gaussian
   moment ratio.
5. **Station test [N].** At the dipole's own station (2,1),
   t = log 2: T(log 2) = 1.440131107042578516…,
   A₁₂(log 2) = 0.439477230926606039…. sympy nsimplify over
   {π, G, ln 2, γ, √2} finds no closed form — no 2^a/3^b rational
   skeleton of the kind the KS side produces at its station.

### 2d. The dipole-matrix-element candidate, specifically [D]

A parabolic bound-state dipole matrix element is a *number*
attached to discrete parabolic stations, computed from one
polynomial×Gaussian integral in (ξ,η) times a measure bridge. The
tail is a continuous function on [0,∞) with a t log t origin
singularity and transcendental values at the stations checked.
Polynomial-operator matrix elements between Gaussian×polynomial
states are algebraic functions of the state parameters (rapidity,
widths) — in particular analytic in the boost parameter at 0. The
tail is not analytic at t = 0. Hence no assignment "tail = matrix
element of a polynomial operator between parabolic states" exists:
excluded, not merely unfitted. (Scope: bound-state parabolic matrix
elements and KS-bridge Gaussian moments — the objects the project
actually uses. Continuous-spectrum Gordon-type integrals are a
different class, are not part of the KS computation, and are not
Lerch functions either.)

### 2e. What the tail is, and the two honest formal parallels

The tail *is* [D]: the Laplace/Mellin shadow of Γ(s/2) — the
saturating-ramp sum over the gamma factor's pole lattice
{2(m + 1/4)} (§1b), two-fold integral of the geometric density
s/(1−s⁴) (§1c). Its generating kernel is the geometric sum
1/(1−s⁴) — a discrete-lattice object — where the KS bridge's
kernel is the Gaussian e^{−au²}: same Laplace grammar, different
measure — discrete shifted lattice vs continuous Gaussian.

Two parallels survive scrutiny, both marked for what they are:

- **Two discrete measures [I].** Inside Suzuki's own formalism,
  Φ₁₂ is a sum over two discrete measures: the primes (linear-ramp
  kernel, Λχ₁₂(n)/√n weights, knots at the dictionary stations
  log n) and the Hurwitz lattice (saturating kernel, (m+1/4)^{−2}
  weights). This is the explicit formula's two sides; it does not
  pass through (ξ,η) coordinates.
- **Complementary coordinates [I, on D facts].** The KS bridge
  lives on the *sum* coordinate: its moments are in
  u² = (ξ+η)/2 = r (the 4u²/π measure weight; I₀ vs I₂). The screw
  term lives on the *ratio* coordinate: on Gram entries its
  argument is t = log(n/k) = log(ξ/η) under the dictionary's
  parabolic readout (ξ/η = n/k, ψ = ½ log(ξ/η)) — i.e. t = 2ψ_{n,k}.
  The KS machinery integrates the sum coordinate out at a frozen
  ratio (one station); the archimedean term is a function of the
  ratio carrying no sum-integral. They occupy complementary
  coordinates of the same (ξ,η) plane, which is the geometric
  restatement of why no moment identity transfers between them.

---

## 3. The parameter 1/4 on the two sides

**Screw side [D].** Two distinct quarters coincide because μ = 0:
the bracket prefactor λ/2 = 1/4 (Suzuki's archimedean normalization
for a Γ(λs + μ) factor) and the Hurwitz shift a = λ/2 + μ = 1/4.
The shift is the operative one: it fixes ψ(1/4) in the linear term,
ζ(2,1/4) = π² + 8G (the translates m + 1/4 are the ≡1 mod 4 class:
ζ(2,1/4) = 16 Σ_{j≡1(4)} j^{−2}), the rates 2(m+1/4), and (with λ)
the s⁴ period of the density. It does **not** fix the t log t
coefficient (−1/2, shift-independent). It is spectral data of
Γ(s/2), shared with ζ; conductor 12 never touches it.

**KS side [D provenances].** Quarters occur as (i) Jacobian
constants of the KS/parabolic change of variables —
d³x = ((ξ+η)/4) dξdηdφ, d⁴u = (1/16) dξdη dχ₁dχ₂ — fixed by the
conventions ξ = r + z, ρ² = ξ/2; (ii) hydrogenic rate arithmetic —
the dipole's combined decay (3/4)/a₀-type factors from
1/(2n₁) + 1/(2n₂) at n = 1, 2, the e^{−ξ/2} ground-state rate, the
(1 − ξ/2) node; (iii) Jeremy's 2011 ratio sequence (k−1)/(2k)
starting at 1/4 (k = 2). Meanwhile the dipole's *moment* structure
runs on thirds — ⟨u_i²⟩ = 1/(n+k) = 1/3 at (2,1), denominators
3⁴, 3⁵ in 32/81 and 128/243.

**Conclusion [D-negative].** The screw's 1/4 is a Selberg gamma
parameter (λ/2 + μ); the KS quarters are a paraboloid Jacobian and
principal-quantum-number rates. Different provenance, no map
between them; the shared numeral is a coincidence of two unrelated
normalizations. The dipole's operative alphabet is {2,3}; the
tail's is {4, π², G, γ}.

---

## 4. Verdict and markings

- **(a) Parabolic reading of the archimedean term as a (ξ,η)-Gaussian
  moment structure: excluded [D]** — coefficient law, support, and
  singularity class all mismatch (§2c, items 1–3), and the constants
  γ, G are unreachable by Gaussian moments (item 4).
- **(b) As a parabolic dipole matrix element: excluded [D]** —
  analyticity at the origin (§2d) and the station test [N] (§2c.5).
- **(c) What it is [D]:** −g_Γ,ζ's tail = the Γ(s/2) Hurwitz-lattice
  ramp sum; density s/(1−s⁴) in the Cayley variable; conductor 12's
  entire archimedean fingerprint is the linear (t/2)·log 12.
- **(d) Surviving parallels [I]:** the two-discrete-measures grammar
  inside Suzuki's formalism, and the sum-vs-ratio complementary
  coordinates in the (ξ,η) plane. Both are descriptions of where the
  objects live, not mechanisms connecting them.
- **Creed:** there is no selection principle here to exhibit, and
  the honest marking is stronger than "permitted, not selected":
  for the Lerch tail the parabolic reading is *not permitted* by
  function class. Nothing in this negative touches the prime side:
  whether the full Φ₁₂ admits parabolic structure through its ramp
  (whose knots are dictionary stations) is the station-Gram
  question, not this thread's [O].

## 5. Verification log [N] (arch_ks_check.py, dps = 50)

- ζ(2,1/4) = π² + 8G: abs diff 0.0 at 50 digits (values agree to all
  printed digits); ζ(2,3/4) = π² − 8G: diff 5.3e-51.
- ψ(1/4) = −γ − π/2 − 3 ln 2: diff 2.8e-51.
- A₁₂ direct (v13.258) vs mirror (−g_Γ,ζ + (t/2) log 12):
  ≤ 2.2e-16 at t = 0.3, 1.0, 2.0, 3.5 (mirror path is float64).
- Exponential series Σ e^{−(4m+1)t/2}/(m+1/4)² vs Lerch value:
  ≤ 6.4e-50 at t = 0.4, 1.0, 2.0.
- Ramp form: mp.nsum to ∞ vs T(t): 5.3e-51 (t = 1), 0.0 (t = 2);
  finite M = 2000 sum differs by exactly the omitted constant
  (1/4)Σ_{m≥2000}(m+1/4)^{−2} = 0.000125015624348 at all t (at
  t = 0.4, nsum extrapolation itself is only good to 5.9e-6; the
  truncation identity is the verification there).
- Density: −T″(t) numeric vs e^{−t/2}/(1−e^{−2t}) vs geometric sum:
  ≤ 2.7e-51 at t = 0.3, 1.0, 2.0.
- Small-t limits → κ and c as tabulated in §1d; the s = 1 Lerch
  constant Φ(e^{−μ},1,1/4) + log μ → −ψ(1/4) − γ verified.
- T(log 2) = 1.440131107042578516…, A₁₂(log 2) =
  0.439477230926606039…; nsimplify over {π, G, ln 2, γ, √2}: no
  closed form found.
