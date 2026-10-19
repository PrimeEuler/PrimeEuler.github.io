# Paraboloids on a fiber: the cos θ coupling anatomy

*Sandbox note (little Euler), 2026-10-19. Continuation of the
selector exploration (v14.621 and the sandbox scans of
`runs/20261019-chain-selector/`). The system is Jeremy's: the
double paraboloid — dumbbell silhouette on its axis fiber — read
as a quantum rotor. Producer: `runs/20261019-rotor-coupling/rotor_coupling.py`.
Exact results are [D]; the G readout is [I]/[O] and claims no
closed item.*

## 1. The system

The double paraboloid's meridian is a dumbbell; the fiber is its
axis through the centre of mass. As a rotor it is the ladder
itself: free comb E_j ∝ j(j+1) (GM² of the consecutive split,
v14.620). Made asymmetric (unequal lobes, centre of mass offset
l from the fiber), it becomes a quantum pendulum: gravity couples
through the offset as a rank-1 perturbation ∝ cos θ — the
gravitational analogue of a dipole coupling, with dipole selection
rules. This is the one system in the program where the α-note
anatomy coexists in a single object: a spectrum (the ladder), a
coupling that selects (cos θ), and the cone's geometry as the
body. Its anatomy is computed here in full.

## 2. The coupling weights [D]

⟨j+1, 0| cos θ |j, 0⟩ = (j+1)/√((2j+1)(2j+3)), and zero unless
Δj = ±1 (Wigner–Eckart). Values: w₀ = 1/√3 = 0.5773502692,
w₁ = 0.5163977795, w₂ = 0.5070925528, w₅ = 0.5017452060,
w₁₀ = 0.5005173307, w₅₀ = 0.5000240310. Every rung's strength
tends to 1/2 from above, excess ~ 1/(8j²): the coupling is
maximally democratic — no rung is singled out.

## 3. The forced climb [D]

The product of strengths along the forced Δj = +1 climb
telescopes to a Wallis ratio,

Π_{j<J} w_j = 2^J (J!)² / ((2J)! √(2J+1)) ~ √(π/2) · 2^{−J},

verified against the direct product to 12 digits for
J = 1…300 (Π·2^J = 1.25279290 at J = 300, → √(π/2) =
1.2533141373). The chain this coupling generates is therefore a
pure per-rung halving dressed by a Wallis constant: its length J
is not selected by the strengths (and ψ_D/ln 2 = 65.37 is not an
integer, though amplitude products are not rapidities in the
first place).

## 4. The pendulum spectrum [D]

H = −∂²_θ − β cos θ on the circle, with the single dimensionless
gravity coupling **β = 2IMgl/ħ²**, Fourier-diagonalised
(|j| ≤ 45; Mathieu-equivalent). At β = 0: 0, 1, 1, 4, 4, 9 —
the comb, with ±j doublets. The coupling splits the doublets
(β = 1: 0.91806 / 1.29317, ground state −0.37849). Deep in the
well the spectrum becomes the libration comb: spacings approach
**√(2β)** from below (β = 64: 11.058, 10.794, 10.520 against
11.314; β = 256: 22.375, 22.118, 21.857 against 22.627), the
½-power warp of the bouncer appearing in a second system;
ε₀(β) ≈ −β + √(β/2) to leading order.

## 5. Readout for the G items

- Consistent with the arithmetic selector scans
  (`runs/20261019-chain-selector/RESULTS.md`: uniform ratio
  chains, α steps, prime steps, field-regulator orbits — all
  negative inside the physical window), the physical coupling
  also selects no finite chain: strengths are democratic, the
  climb is Wallis × 2^{−J}, the spectrum is governed by the one
  device parameter β.
- What the system does give item (ii) is a concrete candidate
  shape. β factorises exactly: (geometry I, l) × (mass M) ×
  (field g), over ħ². Librating this rotor over a **calibrated**
  source mass — g = GM_s/r² — makes β-spectroscopy a G-meter
  whose every non-G factor is ladder arithmetic. On Earth it
  reads g, not G: the bottom line of v14.550 §3 is unchanged,
  but the factorised observable is no longer a placeholder; it
  is a specific, buildable-shaped object — the paraboloids on
  their fiber, over a known mass.
- The hierarchy item (i) is untouched: nothing here generates
  ψ_D = 45.310004305, and §3 shows the system's own exponential
  is 2^{−J} with J free.

## Scope flags

`G_derived = false`; `hierarchy_generator_found = false`;
`factorised_G_observable_exists = false` (a candidate *form* is
identified, §5 — no such measurement exists);
`open_item_count_change = false` (still 2). [I]/[O] sandbox
note; no paper, staged draft, or certified object modified.
