# Ledger v14.996 — Sandbox reconciliation: v14.993 phonon band WITHDRAWN (two action-build omissions); AM ≡ elastic η=3/2 spectra confirmed

**Lane:** Sandbox (little Euler), answering the v14.994 BLOCKER and the
owner's directive (compare unreduced actions first, then trace both
reductions). **Payload:** `payloads/am3scalar_svt_reconciliation_v14_996/`
(RECONCILIATION_NOTE.md + 6 scripts). v14.993 payload untouched/frozen.

## Verdict [D]

v14.994's 2-jet identity is CONFIRMED constructively. The AM
three-scalar and elastic η=3/2 quadratic spectra are IDENTICAL:
P = 3H and Qτ² = 3k² + 4 in all sectors, kinetic coefficients positive
at every k (tensor A = √3τ³/72; vector A = √3τ³/(18(3k²+4)); scalar
A = √3τ³/(54(k²+1))). **v14.993's low-k ghost/growth band and its
task-6 non-equivalence verdict are withdrawn as artifacts.** Its
tensor result (m_T² = 4H²) stands. v14.935's all-k healthy verdict is
consistent with all corrected computations; mode count 2+2+1 agrees
with v14.992.

## Root causes (both in the UNREDUCED action builds, not the eliminations)

1. **Scalar:** build 1's hand-rolled K_xx = K_yy = ḣ/(2N) omitted the
   shift's diagonal covariant derivatives D_xN_x = −Γ^z_{xx}N_z.
   Machine-Christoffel rebuild differs by exactly −2k²aȧBψ/κ, a term in
   the momentum constraint; its absence is where (3k²−1) entered, with
   (3k²−4) downstream in c₂/Q. Build 1's reduction was faithful to its
   (wrong) action — characteristic determinant reproduces its roots.
2. **Vector:** matter action used g^xx = h^xx, dropping −(N^x)²/N²;
   missing term +(C/6)aV² in the shift's algebraic equation. Restored:
   Q_V = (3k²+4)/τ², A_V > 0 ∀k, action check A = −c₂/2 passed.

Build 3 (full g^ij scalar) differs from build 2 by exactly
+(C/6)k²aB²; after simultaneous (Φ, B) elimination its (P, Q, kinetic
sign) equal the elastic values at k² = 1, 4, 9 — the term only rotates
the auxiliary block. Nonlinear AM-vs-elastic differences (finite
strain) are unaffected by this reconciliation.

**Flags:** v14_993_phonon_band=WITHDRAWN_ARTIFACT;
v14_993_task6_nonequivalence=REVERSED; v14_993_tensor=STANDS;
v14_994_identity=CONFIRMED_CONSTRUCTIVELY; v14_935=CONSISTENT;
blocker_v14_994=ANSWERED; Suzuki_quarter=PARKED; protected untouched.

## Handoffs

→ **external-audit:** verify payload (builds reproduce every number;
key identities: L2(build2) − L2(build1) = −2k²aȧBψ/κ; L3 − L2 =
(C/6)k²aB²; vector dL2 = (C/6)aV²).
→ **gravity lane:** your v14.991 NEXT is answered with the opposite
sign from v14.993's claim: the coupled AM system IS healthy at all k,
and its quadratic spectrum is exactly your elastic η=3/2 spectrum.
Standing lesson for all lanes: residual checks cannot catch a wrong
action; independent action builds can.
