# The (m, l) pair test — gravity's own dyon

Sandbox exploration, 2026-10-22. NOT ledgered. Question (Jeremy): the EM dual pair
locks α·α_m = 1/4 = (1/2)². Does gravity's own dual pair — mass m (the E_g
monopole) and NUT charge l (the H_g monopole) — close on a small rational too,
and which one: 1/4 or 1/16? Answer: **1/16**, by two independent routes that
agree exactly. Gravity's pair quantum is ħ/4, not ħ/2.

## Setup

Taub–NUT in the standard parametrisation (geometric units), coords (t, r, θ, φ):

    ds² = −f(r)·χ² + dr²/f(r) + (r² + l²)(dθ² + sin²θ dφ²),
    χ = dt + 2l cosθ dφ,   f(r) = (r² − 2mr − l²)/(r² + l²).

l is unambiguous: the same symbol sits in f and in Σ = r² + l², so no
reparametrisation freedom. The dual mass is M̃ = c²l/G (l_geo = GM̃/c²).
The pair product to test is α_G(μ)·α_G(M̃) = (μ_geo·l_geo/l_P²)² for a test
mass μ, exactly as α·α_m = (eg/ℏc)² for the EM pair.

## Route A — the Poincaré term of the geodesic angular momentum

EM template: a charge around a monopole has J = L − eg·n̂, the radial term
being the stored field angular momentum; SU(2) consistency (j half-integral,
orbital part ⊥ n̂) forces eg ∈ (ħ/2)ℤ, minimum ħ/2, product (1/2)² = 1/4.

For Taub–NUT the isometry is SU(2)×U(1). The SU(2) Killing triad was solved
from the Killing equation (f(r) left arbitrary) and verified symbolically
(`killing.py`): with c(θ,φ) the t-shift of a would-be sphere rotation, the
Killing equations force c_x = 2l cosφ/sinθ, c_y = 2l sinφ/sinθ (the opposite
sign fails), giving

    ξ_x = 2l(cosφ/sinθ) ∂_t − sinφ ∂_θ − cosφ cotθ ∂_φ
    ξ_y = 2l(sinφ/sinθ) ∂_t + cosφ ∂_θ − sinφ cotθ ∂_φ
    ξ_z = ∂_φ ,

and the triad closes: [ξ_i, ξ_j] = −ε_ijk ξ_k (checked symbolically). The
alternative z-generator ∂_φ + 2l∂_t does NOT close the algebra — the triad is
unique. Conserved charges Q_i = ξ_i·p for a unit-mass geodesic, ε := −p_t
(specific energy), satisfy two exact identities (`charges.py`, sympy;
`numeric_check.py`, 200 random phase-space points, PASS):

    J·n̂  =  −2 ε l                                            (exactly)
    J²   =  Σ²θ̇² + (p_φ + 2εl cosθ)²/sin²θ + (2εl)² .

This is the EM structure with **eg → 2εl**. The pair's radial (stored)
angular momentum per unit mass is 2εl, not εl. The "electric" member of the
gravitational pair is the particle's *energy* ε (gravitomagnetic charge
couples to energy, as the Kaluza–Klein reading says: the charge is momentum
along the t-fiber) — at rest at infinity ε = 1.

Quantisation: J·n̂ is a component of a genuine SU(2) generator triad, the
orbital remainder is ⊥ n̂, so 2μεl (total, mass μ) must be an allowed
J-component: 2μ_geo l_geo/l_P² ∈ (1/2)ℤ, i.e.

    μ_geo l_geo / l_P² ∈ (1/4)ℤ   ⇒   α_G(μ)·α_G(M̃) = (k/4)²,  min 1/16.

## Route B — Misner periodicity

χ near the poles: dt + 2l dφ (θ→0), dt − 2l dφ (θ→π). Regular time coordinates
t_N = t + 2lφ, t_S = t − 2lφ disagree by 4lφ on the overlap; after one wind
φ → φ + 2π the mismatch is 8πl, so string-freedom forces t periodic with
period T_t = 8πl/c. Single-valued phase e^{−iEt/ħ} then quantises energy in
steps E = 2πħ/T_t = ħc/(4l). Setting E = μc² (rest mass on the ladder):

    μ_geo l_geo = k·ħG/(4c³) = k·l_P²/4   ⇒   pair product (k/4)², min 1/16.

## Verdict

Both routes land on the same number, and both read it off the same place:
the **2** in χ = dt + 2l cosθ dφ. Route A sees it as the strength of the
fibration's monopole potential (pair term 2εl); Route B sees it as the
Misner period (8πl = 4π·2l). EM's potential A = g cosθ dφ carries coefficient
1, hence ħ/2 and 1/4. Gravity's carries 2, hence ħ/4 and 1/16. The factor is
the familiar spin-2 gravitomagnetic factor, here pinned in two
convention-free places (geodesic angular momentum; time periodicity) rather
than in any GEM field-definition convention.

So the pair DOES close on a small rational square — gravity's duality is as
rigid as EM's — but the square is (1/4)², one rung finer: the cone's
half-ladder, applied to gravity's own charges, quantises the pair in
quarters. Note this is a statement about (test mass, NUT) with ε general:
the pair quantum is really 2εl — energy is the electric member.

## Caveats

- NUT charge is unobserved; Taub–NUT without the periodic-time identification
  carries the Misner string, and with it, closed timelike curves. This is a
  theorem about GR's solution space + quantum single-valuedness, not about
  nature's inventory.
- It does not derive G and does not touch the selector: l is a free charge,
  nothing here counts cosmic contents.
- Files: `killing.py` (Killing triad from scratch), `charges.py` (exact
  charge identities), `numeric_check.py` (200-point numeric confirmation).
## Addendum (2026-10-22, Jeremy's line): the parabolic separation

Jeremy: "its the same lattice that our fine constant came out of. same
parabolic integration with additional power of 2 resolution." VERIFIED, with
one precise seam.

1. **MIC–Kepler separates parabolically, exactly** (`mic_sep.py`, sympy,
   residual 0). With ξ = r(1+cosθ), η = r(1−cosθ), W = U(ξ) + V(η), the HJ
   equation (including the MIC Zwanziger term +s²/r² — without it a remainder
   −s²/(ξ+η) survives and separation fails; the term is load-bearing) splits
   after the standard (ξ+η)/4 multiplier into

       ξU'² + ((k−s)/2)²/ξ − Eξ/2   +   ηV'² + ((k+s)/2)²/η − Eη/2   =   κ.

   Each parabola carries one charge: **centre k/2, offset s/2** — the two
   seats are (k/2 − s/2) and (k/2 + s/2). Hydrogen is s = 0: both seats
   (k/2)², the standard parabolic (n₁, n₂) structure the α extraction used.

2. **Taub–NUT's HJ has MIC's angular+pair sector identically, with
   s = 2εl** (`tn_sector.py`, sympy, exact):

       TN_LHS − MIC_LHS = −(2mr + l²)·p_r² − (2εl)².

   The ONLY differences are radial: a p_r² weight deformation −(2mr + l²)
   and a constant −(2εl)². Nothing angular, nothing in the pair term. The
   radial deformation is the part the standard Iwai–Katayama time
   reparametrisation absorbs (cited, not re-derived); the parabolic content —
   the part the α lattice lives in — is untouched by it.

3. **Therefore TN's parabolic seats are (k/2 − εl) and (k/2 + εl)**: centre
   k/2, offset εl. In the (n, k) diameter–secant reading: the diameter is k,
   the AM is k/2, the offset is the pair product εl itself. The twist does
   not add a new lattice — it splits each hydrogen seat symmetrically around
   its centre by exactly the pair term of Route A. Combined with the pair
   quantisation (εl-lattice in quarters, Routes A/B), the product lattice
   has denominator 4 where the state lattice has 2: one additional power of
   2 of resolution, as Jeremy said.

Seam kept honest: the identification is at the level of the HJ pair/angular
sector + MIC equivalence; the TN radial sector is Σ-deformed, so "same
parabolic integration" is exact for the angular/parabolic content and
reparametrisation-level for the radial content. Files: `mic_sep.py`,
`tn_sector.py`.
