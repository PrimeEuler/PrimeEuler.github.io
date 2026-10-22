# Lobes from Larmor orbits + Coulomb wrap-up — exploration report

**Prompts (Jeremy, 2026-10-21):** (1) "the cone projects the Larmor vector
orbits onto the sphere and those vector orbits create the orbital lobes
through integration"; (2) "wrap up the Coulomb" — close the open items of
`explorations/hydrogen-radial/REPORT.md` §10.

**Status:** sandbox exploration, workspace only. Nothing ledgered.
Machine-checked where stated. Axis correction from hydrogen-radial §7 is
respected throughout: lab-frame Larmor is about **X** (latitude circles
X = const on the shell S²_T); the Y-motion is the Rabi drive on the meridian.

---

## Part 1 — Coulomb: CLOSED up to the single coupling

The one remaining energetics input was the ω² = |E|/2μ link (§10 of the
hydrogen-radial report). It is not an input; it is an identity of the
regularization map.

**Derivation.** Sundman/Poincaré fictitious Hamiltonian Γ = r(H − E) for
H = p²/2μ − κ/r. Under the Levi-Civita map (2D shadow of KS:
x = u₁² − u₂², y = 2u₁u₂, P₁ = 2(u₁p_x + u₂p_y), P₂ = 2(−u₂p_x + u₁p_y))
the momentum identity

    P² = 4r p²        [verified symbolically, sympy: residual exactly 0]

gives Γ = P²/(8μ) − E|u|² − κ. On the physical shell Γ = 0:

    H_osc := P²/(2M) + (Mω²/2)|u|² = κ,   M = 4μ,   Mω²/2 = |E|
    ⟹  ω² = |E|/(2μ).        [verified symbolically]

So the "link" is the potential coefficient of the fictitious oscillator —
a definition of the map, not a physical assumption. The KS identity
p² = P²/(4r) is the same algebra in 4D; the KS constraint is the bicone
gluing (hydrogen-radial §10, already closed).

**Quantization on the glued bicone sector** (machine-checked, truncated
Fock space, n = 1..5): N_a = N_b = n−1 per Schwinger pair, sector
dimension n², and H_osc/(ħω) = N_tot + 2 = **2n uniformly on every state**.

**Closure.** κ = H_osc = 2nħω ⟹ ω_n = κ/(2ħn), and

    |E_n| = 2μω_n² = μκ²/(2ħ²n²).

The full Rydberg spectrum — 1/n² form *and* prefactor — is forced by the
chain. Numeric (κ = e²/4πε₀, μ = reduced mass): E₁ = −13.5983 eV,
E₂ = −3.3996, E₃ = −1.5109, E₄ = −0.8499 (the 13.5983, not 13.6057,
is the reduced-mass hydrogen value; the chain carries μ explicitly).

**Honest remainder.** κ enters exactly once, as the oscillator's
eigenvalue on the shell — this *is* §10's "U(1) charge (Gauss source)"
item, now identified rather than open: the charge is the shell's
conserved value, and its size is nature's input, in the same position
as α_G in the gravity arc (ingredients assembled, one constant
external). What the cone does not do: fix κ's value. Stark effect and
Rydberg revivals remain future, unclaimed.

Checks: `coulomb_check.py` (all pass).

---

## Part 2 — Lobes from integrated Larmor orbits: three readings, three negatives

Anchors (all from the record): shell S²_T; Larmor = latitude circles
X = const; multiplet ring T = j+½ with X_m = m+½ (2026-10-06 orbital
map); vector length GM = √(j(j+1)) (v14.620). Target: the θ-marginals
of |Y_jm|², θ measured from the X (quantization) axis; L1 distance
between normalized profiles (0 = identical, 2 = disjoint).

**Test A — per-state Larmor ring.** The orbit projects to a ring at
cos α = (m+½)/(j+½). Ring positions vs |Y_jm|² maxima:

| j | m | ring α | \|Y_jm\|² max |
|---|---|--------|---------------|
| 1 | +1 | 0.00° | 90.0° |
| 1 | 0 | 70.53° | 0.0° |
| 1 | −1 | 109.47° | 90.0° |
| 2 | +2 | 0.00° | 90.0° |
| 2 | +1 | 53.13° | 135.0° |
| 2 | 0 | 78.46° | 0.0° |
| 2 | −1 | 101.54° | 135.0° |
| 2 | −2 | 126.87° | 90.0° |

No per-state correspondence: a ring is not a lobe, and the ring
latitudes do not track the lobe maxima. **Negative.**

**Test B — vector model (Kepler plane sweep + Larmor precession of L).**
r̂ uniform on the plane ⊥ L (circular orbit), L precessing on its cone
at α, both phases integrated exactly (720×720 grid). Profiles are bands
with caustic peaks at the band edges. L1 vs |Y_jm|² marginals:
0.62–0.78 across j = 1, 2 (textbook angle cos α = m/√(j(j+1)) marginally
better than the cone angle, neither close). Degenerate case: cone
m = ±j gives α = 0, r̂ confined to the equatorial plane — a spike,
L1 ≈ 1.99. **Negative.**

**Test C — composed shell motion (§7's two motions).**
r(t) = R_x(ω_L t) R_y(Ω_R t) r₀, time-averaged on the shell. Since
Larmor about X preserves X, the θ-profile is exactly the X-dwell of the
meridian (Rabi) motion — an arcsine family, set by the turning points.
Pole start (m = +1 cone point): profile peaks at the poles, L1 = 0.521
vs |Y_10|² — the closest any candidate came, but arcsine ≠ polynomial
(Rabi-only gives the same 0.521; Larmor does not enter the θ-profile).
Mid-latitude starts (m = 0, −1 cone points): density stays banded near
the starting latitude (peaks 70.7° / 109.3° ≈ the starting rings),
L1 ≥ 1.04 against every target. **Negative.**

**What the three negatives jointly localize.** Orbit integration on the
*density* side generically produces deltas, band caustics, and arcsine
dwells — classical accumulation profiles. The lobes |Y_jm|² are
polynomials in cos θ: they live on the *amplitude* side, |amplitude|².
No density-side integration of the orbits, in any of the three natural
readings, manufactures them.

**Test D — phase-angle integration (Jeremy's correction, 2026-10-21):
EXACT.** "Integration of the phase angle is what gives you the scatter
needed" — i.e. the shape the edge of a precessing top traces out over
time, accumulated with its phase. Take the Larmor vector as the complex
null vector in the shell's own coordinates (X, Y, W),

    w(χ) = (1, i cos χ, i sin χ),

precessing about X with phase angle χ (= ω_L t — the phase integral
*is* the time accumulation of the trace). The phase-weighted orbit
integral (the Schläfli / Laplace–Heine construction),

    I_jm(θ) = (1/2π) ∫₀^{2π} e^{−imχ} (cos θ + i sin θ cos χ)^j dχ,

satisfies, for every (j, m) with j ≤ 3 (all 16 states, trapezoid
integration at 4096 phases):

    |I_jm(θ)| = [ j! / (j+|m|)! ] · |P_j^{|m|}(cos θ)|

with the ratio constant in θ to a worst relative deviation of
3.1×10⁻¹⁵, and the |I_jm|² θ-marginals equal the |Y_jm|² θ-marginals
to L1 ≈ 5×10⁻¹⁶ — machine precision, no free parameters. The constants
come out in closed form down the table (1, 1/2, 1/3, 1/12, 1/20,
1/120, … = j!/(j+|m|)!).

So Jeremy's statement is confirmed in its phase-weighted form: the
cone's Larmor orbit, projected to the sphere and integrated over its
phase angle against the m-th character, *is* the orbital lobe
amplitude; |I_jm|² is the lobe. The density-side negatives above are
the same integral with the phase weight dropped — which is exactly
what destroys the harmonics and leaves rings/caustics. Note the
orbit itself is null (X² + (iY)² + (iW)² = 0): it lies on the cone,
and the j-th power of its projection is the harmonic polynomial —
the cone projects, the phase integrates, the sphere receives the lobe.

Code: `lobe_test.py` (A, B), `lobe_test3.py` (C), `lobe_test4.py` (D).
Figure: `fig_lobes.png` / `.pdf` (shell with canonical mesh + Larmor
latitudes; j = 1 profile comparison).

---

## Calibration

- Coulomb: the closure is a derivation chain on standard KS/LC
  machinery plus the program's own bicone counting — the spectrum's
  form and prefactor are outputs; κ's value is the one external
  constant, stated plainly.
- Lobes: Jeremy's mechanism is confirmed in its phase-weighted form
  (Test D, exact at machine precision, Jeremy's phase-angle anchor
  supplied after Tests A–C). The density-side readings fail with
  numbers — the phase weight e^{−imχ} is not decoration, it is the
  ingredient that manufactures the harmonics. Calibration honesty:
  the integral itself is the classical Schläfli/Laplace–Heine
  representation of P_j^m; what is the program's is the orbit —
  the null Larmor vector in the shell's (X, Y, W) coordinates,
  precessing about the cone's quantization axis.

## Closures appended 2026-10-22 (post-v14.680)
REPHASING CAVEAT: CLOSED. Exact (Fraction) evaluation of the
Test D integral gives I_jm = i^m * R_jm with R_jm real for all
j <= 4 (parity of the binomial moments), and
R_jm = c_jm P_j^m(cos th) to 4e-15 with the closed form
c_jm = (-1)^m j!/(j+m)!. Hence I_jm = (-i)^m [j!/(j+m)!] P_j^m:
the phase is exactly (-i)^m, theta-independent — the cone
harmonics ARE Y_jm under a fixed azimuth-origin rephasing.
(rephasing_test.py)
STARK: the first-order shift dE = (3/2) n (n1-n2) F is
3 n F * offset, where offset = (n1-n2)/2 is the diameter-secant
offset of the (n,k) machine on the parabolic pair (the cone's
two parabola families). The (n1,n2,m) enumeration reproduces the
textbook tables exactly: n=2 {+3:1, 0:2, -3:1}, n=3 {+9:1,
+4.5:2, 0:3, -4.5:2, -9:1}, totals n^2. (stark_test.py)
RYDBERG REVIVALS: VERIFIED [N] on the cone spectrum
E_n = -1/(2n^2). Classical recurrences at T_cl = 2 pi nbar^3
(|A|^2 = 0.90 at T_cl for nbar=40, sigma=1.0, decaying envelope),
mirror enhancement at T_rev/2 (0.53), full-revival peak 0.80 /
0.88 / 0.95 at sigma = 1.2 / 1.0 / 0.8, located at
t = (1.009-1.010) T_rev with T_rev = (4 pi/3) nbar^4. The ~1%
offset from the E'' time is the exact ladder's higher-order
terms (residual cubic phase 8 pi/(3 nbar) per delta^3 at T_rev);
the discrete second-difference time does NOT locate the peak —
the exact revival position is a Diophantine phase alignment on
the ladder, not a local derivative. (revival_test.py)
