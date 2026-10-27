# Reconciliation of v14.993 with v14.994/v14.935: both v14.993 phonon verdicts were action-build artifacts

**Blocker:** v14.994 (2-jet identity: AM vs elastic η=3/2 quadratic actions
identical ⇒ physical spectra must coincide). **Method per owner directive:**
compare UNREDUCED quadratic ADM actions first, then trace both reductions.

## Verdict

v14.993's scalar and vector "ghost/growth band below k_phys = 2H" and its
task-6 "NOT equivalent" verdict are **WITHDRAWN**. The corrected computation
agrees with v14.935 (elastic η=3/2) and with the v14.994 identity in every
sector: friction P = 3H, **Q τ² = 3k² + 4** (tensor, vector, scalar),
kinetic coefficients positive at all k. The tensor sector of v14.993 was
machine-built and is unaffected (m_T² = 4H² stands). v14.935's all-k
healthy verdict is consistent with everything found here.

## Root cause 1 — scalar: hand-rolled extrinsic curvature dropped D_i N_i

v14.993's scalar action (build 1) used K_xx = K_yy = ḣ/(2N), omitting the
shift's diagonal covariant derivatives D_xN_x = D_yN_y = −Γ^z_{xx}N_z,
which are nonzero because h depends on z. A machine-Christoffel rebuild
(build 2, same ansatz/gauge) differs by exactly one term:

  L2(build 2) − L2(build 1) = −2k² a ȧ B ψ / κ.

That term sits in the momentum constraint; its absence corrupted EL_B,
whose solution fed solΦ and the ψ-constraint — the (3k²−1) denominator
entered there, and (3k²−4) entered c₂/Q downstream. Build 1's reductions
and residuals were internally consistent (its characteristic determinant
reproduces its own reduced roots at k=1 and k=2): the reduction was
faithful, the ACTION was wrong. Corrected scalar results (build 2,
all-k symbolic, residuals 0):
c₂ = −√3τ³/(27(k²+1)) (kinetic A = −c₂/2 > 0 ∀k), P = 3/τ,
Q = (3k²+4)/τ². Its unreduced characteristic determinant factors as
(m²+2m+7) at k=1 and (m²+2m+16) at k=2 (k²=4) — the elastic factors.

## Root cause 2 — vector: truncated inverse metric in the matter action

v14.993's vector action used g^xx = h^xx, dropping −(N^x)²/N². The
missing term is +(C/6) a V². Restoring it changes the shift's algebraic
equation from k⁴V-type to (3k²+4)-type:
V = 4√3 τ ṗ_T/(9k³ + 12k), A_V = √3τ³/(18(3k²+4)) > 0 ∀k (action check
A = −c₂/2 passed), P = 3/τ, **Q_V = (3k²+4)/τ²**.

## Build 3 — full g^ij scalar: extra term present but physically inert

Build 3 = build 2 with g^zz = h^zz − (N^z)²/N² restored in kin3.
L3 − L2 = +(C/6) k² a B² exactly. Its (Φ, B) block is coupled (B is no
longer a multiplier) and its unreduced Euler determinant vanishes
identically (constraint syzygy of the true action), so the spectrum was
extracted after simultaneous (Φ, B) elimination: at k = 1, 2, 3
(k² = 1, 4, 9): P = 3/τ, Q = 7/τ², 16/τ², 31/τ² = (3k²+4)/τ², kinetic
sign positive — identical physics; the B² term only rotates the
auxiliary (Φ, B) block.

## Corrected certificate (AM three-scalar, κC = 1, a = τ/√3)

- Tensor: A = √3τ³/72 > 0, Q τ² = 3k² + 4. (as v14.991/v14.993)
- Vector (×2): A = √3τ³/(18(3k²+4)) > 0, Q τ² = 3k² + 4.
- Scalar: A = √3τ³/(54(k²+1)) > 0, Q τ² = 3k² + 4.
All sectors: P = 3H, unit sound speed, damped oscillations at all k,
no ghosts, no growing modes. Mode count 2+2+1 agrees with v14.992.
The AM and elastic (η=3/2) quadratic actions have identical physical
spectra — task 6 answer REVERSED: they are equivalent at quadratic order
(nonlinear completions still differ, cf. v14.965/971 vs v14.986/989).

## Lesson (recorded)

Build 1's residual checks all passed — a wrong action can be perfectly
self-consistent. What caught the error was an INDEPENDENT action build
(machine Christoffels, the same machinery that made the tensor build
agree with v14.991) plus the cross-model identity. Hand-rolled ADM
curvature/extrinsic formulas are unreliable precisely in shift-coupling
terms (D_iN_i diagonals, N^iN^j inverse-metric parts). Future SVT work
in this lane uses machine-built actions only.

**Payload:** scalar_adm2.py / scalar_final2.py (build-2 scalar),
vector_fix.py (vector), scalar_adm3.py / build3_numeric.py (build 3),
char_det2b.py (determinant check), this NOTE. v14.993 payload untouched.
