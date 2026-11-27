# Cone Derivation Ledger v15.1569 — Sandbox: Chandrasekaran Eq. (4.21) H² is the Gravity lane's Einstein–H² target metric — exact chart bridge via the determinant–Lorentz identification; same geometry, different role; no selector

**Deposit type:** Sandbox comparison note, run at
Jeremy's direction 2026-11-27. External comparator:
V. Chandrasekaran, "An algebraic quantization of
gravity from the null cone," arXiv:2611.34924v1
(submitted 2026-11-25), eqs (3.26c), (3.27), (4.21),
(4.22). Parents: the Gravity lane's Einstein–H² arc
— v15.1386 (sigma kinetic geometry), v15.1415–1416
(energy exchange), v15.1451 (Noether identity),
v15.1453–1454 (constrained slice / FLRW). Parallel
same-day work: Gravity v15.1567–1568 treat the same
preprint from the covariance/optical side and agree
on the metric identification; this note's scope is
the part they did not do — the lane-sigma chart
change, the kinetic/prefactor comparison, and three
wording flags on the lane's own entries. Prewrite
HEAD 6ecf990fd05dbd055d41cf5b567d2f585a0f8743
(v15.1568); version search empty. Additive only.

**Decisive answer: the geometry is IDENTICAL; the
dynamics are not shared.** Chandrasekaran's DeWitt
metric (4.21b) on the unit-determinant conformal
transverse metrics and the lane's normalized target
metric G_AB are the same unit H² metric (K = −1),
identified by an explicit diffeomorphism with no
constant rescaling, and his focusing functional is
the Dirichlet energy of a curve in that same H² —
the same integrand as the lane's sigma energy. But
his coefficients are fixed by GR while the lane's
F², κ and interaction g are free inputs; nothing
here selects anything, derives G on either side, or
certifies a new observable. Grade: same geometry,
different role — consistent with Gravity v15.1567's
nonselector verdict from the covariance side.

**The bridge [D].** Identify his q̄ with the unit
hyperboloid by the determinant–Lorentz map
`Q = [[T+Y, X],[X, T−Y]]`, `det Q = T²−X²−Y² = 1`
(the Casimir Null Diamond paper's identity). The
lane's chart is graph coordinates `(u, v) = (X, Y)`,
`T = sqrt(1+u²+v²)`, embedding
`n = r(sqrt(1+u²+v²), u, v)` at r = 1/4 with
normalized induced metric
`G_AB = δ_AB − phi_A phi_B/(1+u²+v²)`. Then:

- Forward: `u = e^{z¹} z²`,
  `v = sinh z¹ − (1/2) e^{z¹} (z²)²`,
  `T = cosh z¹ + (1/2) e^{z¹} (z²)²`
  (T²−u²−v² = 1 verified symbolically).
- Inverse: `z¹ = log(T + v)`, `z² = u/(T + v)`.
- Pullback: `Jᵀ G J = diag(1, e^{2z¹})` EXACTLY —
  his (4.21c). Numeric round-trip at 5 random
  points: max error 4.4e-16.
- His (4.21c) independently re-derived from
  (4.21a)+(4.21b): the DeWitt pullback
  `(1/2) tr(q̄⁻¹ ∂_α q̄ q̄⁻¹ ∂_β q̄)` is exactly
  `diag(1, e^{2z¹})`; Gaussian curvature −1.
- The lane's G_AB likewise has K = −1 exactly
  (det G, G⁻¹, and Γ^A_BC = −phi^A G_BC all
  re-verified): the r = 1/4 embedding radius does
  NOT rescale the normalized metric; r survives
  only in prefactors. (Frame note: the transposed
  convention `M = [[T+X, Y],[Y, T−X]]` used in
  v15.1567 gives the equivalent chart
  `z¹ = log(T+u)`, `z² = v/(T+u)`.)

**The integrand [D].** His classical focusing
functional (3.26c) is
`Xi_y(v) = (1/8) ∫ s (∂_s q̄)_AB (∂_s q̄)^{AB} ds`,
and `(∂_s q̄)_AB(∂_s q̄)^{AB}
= 2[(∂_s z¹)² + e^{2z¹}(∂_s z²)²]` (verified), so
Xi is (1/4)∫ s·(H² speed²) ds — the Dirichlet
energy of the curve `s ↦ q̄(s, y)` in H² — and the
clock is its exponential,
`u*(y) = ϱ_S(y) ∫ e^{Xi_y(v)} dv` (3.27); the
quantum form (4.22) is the same density as a sum
of squares, hence ≥ 0. The lane's curved-target
energy (v15.1416) `E_H² = (1/2) G_ab(phi)(phi_t^a
phi_t^b + phi_x^a phi_x^b)` is the same Dirichlet
integrand read as a spacetime field energy. The
variational structures differ: his Xi is a
monotone focusing delay with no exchange partner
and no conservation law; the lane's E_H² is one
summand of a conserved `H = E_A + E_H² + E_mix`
whose sectors trade energy through the chosen
coupling `g A_t Ω_uv (u_t v_x − u_x v_t)`, which
has no counterpart in his construction — and his
exponentiation has none in the lane's. Same
variational integrand; different variational
structure.

**Prefactors [I].** His H² coefficients are fixed
by the constraint/symplectic structure: the 1/2
DeWitt convention in (4.21b), 1/8 in the focusing
equation (3.25f), and a single overall
`1/(16πG_N)` in the cone symplectic form (3.39)
with corner charge `K = A/(8πG_N)` (3.43). G_N
never enters the H² metric itself — det q̄ = 1
fixes the hyperboloid radius, hence K = −1. The
lane's density is the same Dirichlet form times a
free dial: F² (written f² in v15.1386/1454,
(fr)² in v15.1451, set to 1 in v15.1416/1453),
with κ = 8πG a second free dial and the
Weyl–Maxwell–area coupling g = ζ/Λ² a third.

**Flags on the lane's entries (wording-level; no
computational defects — every load-bearing formula
used was re-verified or is internally
consistent).** (1) Prefactor normalization drift:
the same sigma action appears as −(f²/2)∫G
(v15.1386), −(f²r²/2)∫G (v15.1451), unit prefactor
(v15.1416; v15.1453 at fr = 1), f = 1 (v15.1454).
All entries declare the scale freely chosen and
every stated result is scale-covariant or
evaluated at the declared setting, so no
conclusion moves — but "f" is not one fixed
normalization across the arc. (2) v15.1454 calls
(u, v) "Poincare-type" coordinates; they are
hyperboloid graph coordinates
(u = sinh d·cos θ, v = sinh d·sin θ), and the
mislabel obscures exactly this chart
identification. (3) v15.1415 is flat-target by its
own statement; the curved-H² exchange result is
v15.1416 only, and 1415 must not be cited for it.

**Scope.** This note certifies a chart/metric
identification and an integrand identity only. It
does not audit Chandrasekaran's quantization or
his finite-dimensionality argument (whose §5.1
clock-existence step he himself flags as heuristic
for noncommuting operators, his footnote 18); the
preprint is v1 and unreviewed. `G_derived = false`
stands on both sides — his G_N is an input, the
lane's κ is imposed. No selector is claimed, no
gate is touched, and nothing here changes the
standing verdict that no parameter-free Cone
observable is certified.

**Verification.** Executed
`research-notes/chandrasekaran_h2_chart_bridge_v15_1569.py`
(SymPy 1.12): (4.21c) from (4.21a)+(4.21b) exact;
K = −1 for both metrics; lane det/inverse/
Christoffel identities componentwise; forward map
on-shell T²−u²−v² = 1; pullback JᵀGJ =
diag(1, e^{2z¹}) exact; shear-trace identity
(∂q̄)(∂q̄) = 2[(∂z¹)² + e^{2z¹}(∂z²)²]; numeric
round-trip max error 4.4e-16. ALL PASS. Audit
pending.
