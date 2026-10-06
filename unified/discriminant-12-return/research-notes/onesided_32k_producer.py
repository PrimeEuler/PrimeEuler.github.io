#!/usr/bin/env python3
"""v14.077 handoff: one-sided 32k tail closure producer.

Computes (deterministic, numpy only, no RNG):
  1. Outward sign radii for ΔA_32k < 0 and C_S(32k) > 0 from v14.075/v14.077
     midpoint data + LDDD residuals, with generous safety factors.
  2. Coarse δu remainder at N=32k (γ=1, v14.073 formula).
  3. K=10 Q_sep geometric remainder scaled to n_0=64k (v14.020 base,
     v14.079 §12.2 methodology, adapted to the 32k cutoff).
  4. R_osc inputs: numerical envelope (v14.079, [N]) and Toeplitz-symbol
     rigorous bound for the q=7 off-diagonal channel [D].
  5. One-sided margin test: R^{res,+}_{32k} vs M = 1.37456583285676e-5.

Status of each piece is marked [D]/[N]/[O].
"""
import hashlib
import math

# ----------------------------------------------------------------------------
# 0. Inputs (from ledger entries — midpoints, not yet outward)
# ----------------------------------------------------------------------------
# v14.077 §2 (more precise than v14.075 §1; uses C_D to 16 digits)
A_e = 1200.4587051950723326859704612197054
A_o = 1184.9475540161082531811400666425518
M_e11 = 12707.2124123182497242938885399105553
M_o11 = 12062.9887449147195258219173308114421
C_D = -4.395585571978897  # v14.069 structural constant [D]

DeltaA_mid = A_o - A_e
Mo_minus_Me_mid = M_o11 - M_e11
C_S_mid = C_D - Mo_minus_Me_mid

# v14.075 §1: LDDD source residuals after arch-200 refinement
res_e = 6.28e-26
res_o = 1.44e-26

# One-sided margin (v14.076 §3, CONDITIONAL on promotion)
MARGIN = 1.37456583285676e-5

# v14.073 constants
A_MAX = 804.0
GAMMA = 1.0  # v14.071 theorem

out_lines = []

def emit(s=""):
    out_lines.append(s)
    print(s)

emit("=== v14.077 one-sided 32k tail closure producer ===")
emit()

# ----------------------------------------------------------------------------
# 1. Outward sign radii [N] (generous, not sharp)
# ----------------------------------------------------------------------------
emit("--- 1. Sign certification (generous radii) ---")
emit(f"ΔA midpoint = {DeltaA_mid:.10f}")
emit(f"C_S midpoint = {C_S_mid:.10f}  (C_D={C_D}, M_o-M_e={Mo_minus_Me_mid:.6f})")

# Generous relative error assumption: 1e-9 (1e17 x the 1e-26 LDDD residuals).
# This is enormously pessimistic; the true arch-200 error is ~1e-26 scale.
REL_ERR = 1e-9
dA_radius = (abs(A_o) + abs(A_e)) * 3 * REL_ERR  # A=C L^2: dC/C + 2 dL/L
dCS_radius = (abs(M_o11) + abs(M_e11)) * REL_ERR + 1e-12  # dC_D negligible

emit(f"assumed generous rel. err = {REL_ERR:.0e} (vs LDDD residuals {res_e:.2e}, {res_o:.2e})")
emit(f"ΔA radius = {dA_radius:.3e}  (need < {abs(DeltaA_mid):.2f} to certify sign)")
emit(f"C_S radius = {dCS_radius:.3e}  (need < {C_S_mid:.2f} to certify sign)")

dA_ok = dA_radius < abs(DeltaA_mid)
dCS_ok = dCS_radius < C_S_mid
emit(f"ΔA_32k < 0 CERTIFIED: {dA_ok}  [upper: {DeltaA_mid + dA_radius:.6f} < 0]")
emit(f"C_S(32k) > 0 CERTIFIED: {dCS_ok}  [lower: {C_S_mid - dCS_radius:.6f} > 0]")
emit()

# ----------------------------------------------------------------------------
# 2. Coarse δu remainder [D] (v14.073 §2, γ=1)
# ----------------------------------------------------------------------------
emit("--- 2. δu index-shift remainder [D] ---")
N = 32000
dU = 2 * A_MAX / (GAMMA * math.sqrt(12) * N ** 2)
emit(f"N={N}: δu ≤ 2·A_max/(√12·N²) = {dU:.4e}")
emit(f"  = {dU / MARGIN:.2%} of one-sided margin")
emit()

# ----------------------------------------------------------------------------
# 3. K=10 Q_sep geometric remainder [D] (v14.020 base, scaled to n0=64k)
# ----------------------------------------------------------------------------
emit("--- 3. K=10 Q_sep (n ≥ 64k) geometric remainder [D] ---")
# v14.020: ||R̃_10||_2 < 1.21e-10 at (N=4000, n0=8000).
# Scales as n0^{-22.5}. For 32k cutoff, Q_sep = {n ≥ 64000}.
n0_base, n0_new = 8000.0, 64000.0
scale = (n0_base / n0_new) ** 22.5
R10_base = 1.21e-10
# v14.079 §12.2 used 1e20 pessimistic moment growth; keep it.
MOMENT_GROWTH = 1e20
R10 = R10_base * scale * MOMENT_GROWTH
u_norm = 1.0 / math.sqrt(2 * N)
cross_Qsep = 2 * math.sqrt(A_MAX) * u_norm * R10 / GAMMA
sub_Qsep = R10 ** 2 / GAMMA
emit(f"scaling (8000/64000)^22.5 = {scale:.3e}")
emit(f"||R̃_10||_2 ≤ {R10:.3e}  (with 1e20 moment growth, pessimistic)")
emit(f"cross ≤ 2√A·||u||·||R̃||/γ = {cross_Qsep:.3e}")
emit(f"subleading ≤ ||R̃||²/γ = {sub_Qsep:.3e}")
emit(f"Q_sep total ≤ {cross_Qsep + sub_Qsep:.3e}  (negligible [D])")
emit()

# ----------------------------------------------------------------------------
# 4. R_osc inputs
# ----------------------------------------------------------------------------
emit("--- 4. R_osc quadratic form ---")
# [N] numerical envelope from v14.079 §9 (bare, J=300 window)
A_Rosc_num_32k = 8.14e-8  # A·|⟨w_o,R_osc^b w_e⟩| at 32k
emit(f"[N] numerical A·|⟨w_o,R_osc^b w_e⟩| at 32k = {A_Rosc_num_32k:.3e}")
emit(f"    = {A_Rosc_num_32k / MARGIN:.2%} of one-sided margin")
# [D] Toeplitz-symbol rigorous bound, q=7 off-diagonal leading term only.
# v14.079 §6: |⟨w_o,R_7^{off,lead}w_e⟩| ≤ c·2w_7·π·‖w_o‖‖w_e‖,
#   = 3.15e-9 at 64k with ‖w_o‖‖w_e‖ ≈ 1.07e-9 [N].
# Scale ‖w_o‖‖w_e‖ from 64k to 32k. v14.079 does not give the 32k norm
# product; use the rigorous γ=1 cap ‖w‖ ≤ 1/√(2N) — TOO LOOSE (see §5).
# Instead report the [N]-scaled value and flag the rigor gap.
wprod_64k_num = 1.07e-9  # [N] v14.079 §6
# Conservative scaling: ‖w‖² ~ 1/(N (log N)^3) ⇒ product scales ~2.43x 32k/64k
wprod_32k_num = wprod_64k_num * 2.43
c_2w7_pi = 2.942  # c·2·w_7·π [D]
toeplitz_q7_32k = c_2w7_pi * wprod_32k_num  # [N]-scaled norm product
emit(f"[D+N] Toeplitz q=7 off-diag leading, 32k: ≤ {toeplitz_q7_32k:.3e} "
     f"(norm product [N]-scaled)")
emit(f"    A_max· = {A_MAX * toeplitz_q7_32k:.3e} = "
     f"{A_MAX * toeplitz_q7_32k / MARGIN:.1%} of margin (q=7 channel only)")
emit(f"    NOTE: full-R_osc rigorous bound unavailable (v14.079 OBSTRUCTION;")
emit(f"    Lemma G/W open). Toeplitz-for-all-q ≈ 5x larger, over margin.")
emit()

# ----------------------------------------------------------------------------
# 5. One-sided margin test
# ----------------------------------------------------------------------------
emit("--- 5. One-sided margin test ---")
emit(f"margin M = {MARGIN:.4e}  (v14.076 CONDITIONAL)")
emit()
emit("Rigorous [D] pieces:")
emit(f"  δu            ≤ {dU:.4e}  ({dU/MARGIN:.1%})")
emit(f"  K=10 Q_sep    ≤ {cross_Qsep+sub_Qsep:.3e}  (negligible)")
emit(f"  R_osc         : NO rigorous full bound (v14.079 obstruction)")
emit()
emit("Numerical [N] pieces (not theorem-grade):")
emit(f"  R_osc (total) ≈ {A_Rosc_num_32k:.3e}  ({A_Rosc_num_32k/MARGIN:.1%})")
emit()
rigorous_sum = dU + cross_Qsep + sub_Qsep
emit(f"[D] subtotal (excl. R_osc) = {rigorous_sum:.4e} ({rigorous_sum/MARGIN:.1%})")
emit(f"[D+N] with numerical R_osc = {rigorous_sum + A_Rosc_num_32k:.4e} "
     f"({(rigorous_sum + A_Rosc_num_32k)/MARGIN:.1%})  ← fits comfortably [N]")
emit()
if dA_ok and dCS_ok:
    emit("Signs: T1_32k < 0, T2_32k < 0 CERTIFIED (generous) → discard for upper bound.")
else:
    emit("Signs: NOT certified — one-sided framework fails.")
emit()
emit("VERDICT: QUANTIFIED OBSTRUCTION.")
emit("  The [D] pieces fit (δu 3.3%, K=10 negligible).")
emit("  The [N] R_osc scale (0.6% of margin) fits comfortably.")
emit("  But no rigorous upper bound on |⟨w_o,R_osc w_e⟩| exists")
emit("  (v14.079: SBP fails, Toeplitz incomplete, Lemma G/W open).")
emit("  Hence R^{res,+}_{32k} < 1.3746e-5 is NOT established as theorem.")
emit("  Conditional premise (v14.076 interval) itself obstructed per v14.080;")
emit("  needs Lane A's μ_{32k} floor package.")
emit()

# SHA-256 of key outputs for determinism check
digest = hashlib.sha256("\n".join(out_lines).encode()).hexdigest()
print(f"SHA-256: {digest}")
