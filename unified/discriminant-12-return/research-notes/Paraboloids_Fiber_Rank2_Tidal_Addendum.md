# Paraboloids on a fiber, addendum: the rank-2 (tidal) channel

*Sandbox note (little Euler), 2026-10-19. Addendum to the
rotor anatomy of v14.626 (which treated the rank-1 cos θ
channel). Prompted by Jeremy's question about the Cavendish
torsion balance — a balanced dumbbell on a fiber, attracted
by a placed mass: that experiment is this channel. Producer:
`rotor_rank2.py`. All formulas [D], machine-verified as
stated.*

## 1. The coupling

A placed source mass M_s at distance R acts on a balanced
dumbbell through the n = 2 Legendre term of the two-lobe
potential:

U_tidal = −(GM_s I/R³) · P₂(cos θ),

with I the dumbbell's moment of inertia. In rotor units the
strength is **β₂ = 2GM_sI²/(ħ²R³)**. This is Cavendish's
channel, and the gravity-gradient coupling of satellites.

## 2. Weights and selection rules [D]

The P₂ matrix in the |j, 0⟩ basis has support only on
Δj ∈ {0, ±2} (max off-support entry exactly 0 in a J = 60
build): the tidal coupling **splits the ladder into two
independent chains**, even j and odd j — parity is conserved,
unlike the rank-1 channel, which mixes everything.

- Up-weights: v_j = ⟨j+2,0|P₂|j,0⟩ = (3/2)·w_j·w_{j+1}
  = (3/2)(j+1)(j+2) / ((2j+3)√((2j+1)(2j+5))), built from the
  rank-1 weights of v14.626. v₀ = 1/√5 = 0.4472135955,
  v₁ = 0.3927922024, v₅ = 0.3772725652; v_j → **3/8** from
  above. Verified against the explicit (3cos²θ − 1)/2 matrix
  to 1.7×10⁻¹⁶.
- Diagonal: d_j = (3(w_j² + w²_{j−1}) − 1)/2; d₀ = 0,
  d₁ = 2/5, d_j → 1/4. Verified to 2.2×10⁻¹⁶ on interior rows
  (a single 0.375 raw discrepancy was identified exactly as
  the finite-matrix truncation edge, (3/2)w²₅₉).

## 3. Climbs [D]

Products over N steps of Δj = 2 (log-sum extrapolation to
N = 4000 steps, constants stable to six digits):

- even chain: Π v ~ **√(π/2)** · (3/8)^N — the rank-1 climb's
  Wallis constant, again;
- odd chain: Π v ~ **√(3π/8)** · (3/8)^N, √(3π/8) = 1.085402.

Per unit j, the tidal climb decays as (3/8)^{1/2} ≈ 0.612,
against the rank-1 climb's 1/2.

## 4. Budgets [D]

- **Nano dumbbell (I = 1.92×10⁻³¹), 1 mg at 1 mm:** β₂ =
  4.4×10² (deep well), libration 1.8 mHz; Earth's own tidal
  well is 4.6% of the signal.
- **Bench rotor (I = 10⁻⁴), 10 kg at 10 cm:** β₂ = 1.2×10⁵⁴
  (classical regime); Earth's tidal well is 4.6× the signal —
  static, known, removable by source modulation.

## 5. The structural point

Rank-2 is the only channel in the anatomy with **no uniform-g
Earth carrier**: a balanced dumbbell in uniform g feels no
torque, so rank-1 Earth leakage is symmetry-forbidden and
enters only through a CM offset l (DC tolerance l << U/(Mg):
7×10⁻¹¹ m bench, 2×10⁻¹⁹ m nano — modulation converts the
requirement from absolute balance to balance stability, the
Cavendish art). The anatomy is now two chapters: rank-1 =
the g channel (β = 2IMgl/ħ², Δj = ±1, Wallis 2^{−J});
rank-2 = the G channel (β₂ ∝ I²M_s/R³, Δj = ±2,
parity-split, (3/8)^N climbs). Item (ii)'s factorised
observable has a concrete spectral form in each chapter;
neither is a measurement. `G_derived = false`.
