# v14.880 sandbox handoff — finite-Larmor retarded Maxwell pole: derivation

Date 2026-10-25. Parent handoff: v14.880 (target sandbox, type
finite-larmor-retarded-Maxwell-pole). Jeremy's go: main chat 2026-10-25 21:05 EDT
("Take it up now") — supersedes the freeze for this item only.

## Source model (from v14.871/872, exact)

Equal-width Gaussian blobs ±q at reflected positions
r_±(t) = c(t) ± R ξ x̂, ξ = δ/u, c(t) = R√(1−ξ²)(0, cos Ωt, sin Ωt).
Exact Fourier source obeys ∂tρ + ik·J = 0. First order in δ (g = 2qR/u,
f_a = exp(−a²k²/2)):

rho1(k,t) = −i g k_x f_a e^{−ik·c(t)} δ(t)
J1(k,t)  = g f_a e^{−ik·c(t)} [ δdot x̂ − i k_x v(t) δ(t) ],   v = dc/dt.

## Effective action and the pole function

Coulomb gauge. Coulomb part instantaneous: U_C gives k_C = g²/(24π^{3/2} ε0 a³),
unchanged by common rotation (v14.878). Transverse part: on-shell field action
for prescribed sources S_T = +(μ0/2) ∫∫ J G_ret J. For δ(t) = Re δ_ω e^{−iωt},
helical symmetry (v14.878) makes the reduced kernel frequency-diagonal: a single
scalar inverse-response function

  𝒟(ω;Ω) = −k_C + μ0 Σ_n ∫ d³k/(2π)³ e^{−a²k²} Q_n / [k² − (ν_n/c)²],

  ν_n = ω + nΩ,
  Q_n = |P_T(ω b_n x̂ + k_x d_n)|²  (overall −i of J_n drops in |·|²),

where h(t) = e^{−ik·c(t)} = Σ_n b_n e^{−inΩt}, v(t)h(t) = Σ_n d_n e^{−inΩt}
(ledger v14.879 convention: b_n, d_n — NOT b_{−n}).

Anchors fixing every sign/factor:
1. Ω = 0: b_0 = e^{−ik·c}, d_n = 0 ⇒ 𝒟 = −k_C + ω² M_T(ω), whose zeros are
   v14.874's D(z) = 1/4 − z²F(z) after normalization. ✓ by construction.
2. Quasistatic (ω,Ω → 0): convective (d_n) sector must reproduce v14.877's
   magnetostatic coefficient as an ACTION term: 𝒟̂(0;α,β) ≈ −1/4 + (αβ)²/5.
   (v14.877's E_B is field energy, explicitly NOT the dynamical force; the
   on-shell action gives the seat SOFTENING sign, consistent with v14.860's
   "static magnetic seat coupling softens seat".)

## Dimensionless form (implemented)

z = aω/c, α = Ωa/c, β = R/a, p = ak. b_n depends on (p, μ=p̂_x, φ) through
ρ_b = β p √(1−μ²): b_n = e^{inφ} (1/2π)∫ e^{ins} e^{−iρ_b cos s} ds
(phase fixed numerically against this definition in code).
v(t) = Re[V e^{−iΩt}], V = ΩR(0,−i,1) ⇒
d_n = (V b_{n−1} + V* b_{n+1})/2 = αβc · e_n,
e_n := [(0,−i,1) b_{n−1} + (0,i,1) b_{n+1}]/2.
Channel continuity ⇔ p·e_n = (n/β) b_n (checked numerically).

  𝒟̂(z;α,β) := 𝒟/(M_T(0) c²/a²)
            = −1/4 + 6π^{3/2} Σ_n ∫ d³p/(2π)³ e^{−p²}
              |P_T(z b_n x̂ + αβ p_x e_n)|² / (p² − (z + nα)²)

with M_T(0) = μ0 g²/(6π^{3/2} a). At α = 0 this reduces EXACTLY to
−1/4 + z²F(z), F(z) = 1 + i√π z e^{−z²} erfc(−iz) (verified symbolically:
prefactor 6π^{3/2}·(8π/3)/(2π)³ = 2π^{−1/2} matches M_T(z)/M_T(0)).

Poles = zeros of 𝒟̂ on the retarded sheet (integral representation is the
analytic continuation from Im z > 0; for Im z < 0 no denominator zero crosses
the real p axis while Re(z+nα) ≠ 0). Damped ⇔ Im z < 0 for e^{−iωt}.

## Implementation notes (as executed, kernel5.py)

- Bilinear form in z (A_n · A_n^sharp, A^sharp = conj of A at conj(z)) — the
  sesquilinear |A|^2 form is NOT analytic in z and fails the alpha=0 anchor.
- Retarded sheet at Im z < 0: real-axis radial quadrature plus a per-channel
  residue correction +2 pi i Res_{p=nu_n} for every channel with
  Im(z + n alpha) < 0. Sign fixed by the frozen root test: with + sign,
  Dhat(z0; 0) = -4e-11 at the v14.874 root; with - sign, -0.467.
- Independent check (timedomain_check.py, v14.881 sinc route): sector kernels
  by finite-difference tensor derivatives of 4 pi sinc(k|Dc|), verified against
  brute-force (mu, phi, t) quadrature pointwise; tau-transform reproduces the
  harmonic Dhat to <= 2e-5 at finite alpha. In the tau domain the cross sector
  is odd in tau and pairs source-first, <A(t-tau) P_T A^sharp(t)>; with that
  pairing the two routes agree. (An earlier rotated-contour attempt,
  kernel2/3, lands on the advanced sheet — Im sign flipped on the real axis —
  and was discarded.)

## Declared sweep

β ∈ {0.5, 1, 2} (v14.880's sampled values); α ∈ {0.05, 0.1, 0.2, 0.35, 0.5}
with αβ = ΩR/c ≤ 0.7 (source speed < c; α=0.5, β=2 excluded as luminal).
Continuation from z0 = 0.4108337143730426 − 0.1700926343728676i at α = 0
(β-independent at α = 0, v14.879). Diagnostics: harmonic cutoff N, radial and
angular node doubling, independent mpmath residual at each reported pole via
brute-force time-quadrature b_n/d_n (second implementation), upper-half-plane
scan along each continuation path. No support mechanics — poles are of the
field-only effective kernel, exactly the scope of v14.874's frozen result.
