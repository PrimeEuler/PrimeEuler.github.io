# Cone Derivation Ledger v14.245 — Sandbox: v14.243 Audited; Whole Far Residual Norm Consumer Derived

**Date:** 2026-10-10
**Track:** Sandbox / v14.243 handoff response
**Status:** [V] v14.243 audit: both payload SHAs match (73904/71372 bytes); 42 moment pairs per sector verified; six direct Far checks pass (all_256000_terms_outward_identity=True); geometric remainder HS²=50·2^{-168}(1/U+1/169) re-derived term-by-term; even/odd remainders 6.488e-16/1.283e-17 recomputed exactly. [D] Whole Far residual norm consumer: explicit formula combining ρ_n and (S_K y)_n with z_n oscillatory factor retained (not bounded separately); odd-sector 1/[n(n-1)] shift retained via 1/n²+O(1/n³); residual norm reduces to zeta-tails of explicit powers. No correction to v14.243.
**Parents:** v14.213, v14.223, v14.238–243.
**Collision check:** live ledger max v14.244 (External Audit R219) at write time; v14.245 is next-free. No collision.

---

## 1. v14.243 audit [V]

**Payloads:** even-v `d2feb4f3…` (73904 bytes) ✓; odd-v `690962a2…`
(71372 bytes) ✓. K=42, far_first_mode=1024001/1024002. ✓

**Moments:** 42 pairs (M_j,Z_j) per sector, j=0..41. Combined
support x: x_front=Z_full-ztilde_CI, x_Near=y. M_j=Σ m^{2j+1}x_m,
Z_j=Σ z_m m^{2j}x_m. ✓

**Direct checks:** 3 per sector (n=1024000+,1536000+,4096000+
start), each summing all 256000 support terms with 512-bit
downward rounding per term. All six pass with
all_256000_terms_outward_identity=True. ✓

**Remainder:** |c(z_n m-n z_m)/(n²-m²)|≤20/n verified
(|z_n m-n z_m|≤15n, |n²-m²|≥3n²/4). Omitted term ≤(20/n)(U/n)^{84}.
HS²≤50·2^{-168}(1/U+1/169) re-derived: 200·U^{169}·[(2U)^{-170}+
(2U)^{-169}/338]=50·2^{-168}(1/U+1/169). ✓
Even: 2.307e10·√HS²=6.488e-16 ✓; odd: 4.561e8·√HS²=1.283e-17 ✓.

**Scope:** Honest flags (no whole residual, no stationary).
CI pending at publication. ✓

## 2. Whole Far residual norm consumer [D]

**Residual.** For n>4R: r_n=ρ_n-(S_K y)_n.

ρ_n=W_far(n)-z_n·A_far(n)+δ_odd/[n(n-1)], with W_far=Σ_{j<11}
a_j/n^{2j+1}, A_far=c_midΣ_{j<11}M_j/n^{2j+2}, δ_odd∈{0,1}.

(S_K y)_n=c·z_nΣ_{j<42}A_j/n^{2j+2}-cΣ_{j<42}B_j/n^{2j+1}
+α·p_n·P-Σ_j M_j^K/n^{j+1}+Rem (v14.240/v14.243).

**Combine z_n terms** (do NOT bound |z_n|≤8 separately):
r_n = C(n) + z_n·D(n) + E(n) + Rem_total,
where
C(n)=W_far(n)+cΣB_j/n^{2j+1}+ΣM_j^K/n^{j+1},
D(n)=-A_far(n)-cΣA_j/n^{2j+2},
E(n)=δ_odd/[n(n-1)]+α·p_n·P.

**Odd shift.** 1/[n(n-1)]=1/n²+1/[n²(n-1)]≤1/n²+2/n³ (n>2).
Retained explicitly; contributes to n^{-4},n^{-6} tails.

**Norm.** |r_n|²≤4|C|²+4|z_n|²|D|²+4|E|²+4|Rem|².
Σ_{n>4R}|r_n|²≤4Σ|C|²+32Σ|D|²+4Σ|E|²+4Σ|Rem|² (using |z_n|²≤64
only AFTER combining, preserving the D(n) coefficient structure).

**Zeta tails.** Each of C,D,E,Rem is a finite linear combination
of n^{-p} (p≥1). Σ_{n>4R}n^{-p}≤(4R)^{-p}+(4R)^{1-p}/(p-1).
All coefficients explicit from: a_j,M_j (v14.223); A_j,B_j,P
(v14.243 moments); M_j^K (v14.243); p_n bound 2/n; δ_odd.

**Pole.** α·p_n·P: |p_n|≤2/n, so |α·p_n·P|²≤16|P|²/n²; contributes
to n^{-2} tail. P from v14.243 moments. ✓

**Required inputs.** All available: v14.223 far moments (a_j,M_j);
v14.243 combined moments (A_j,B_j,P,M_j^K); certified z_n bound
(only for the final |z_n|²≤64 step, after combining); pole
parameters L,t. No new scalar inputs.

## 3. Verdict

$$\boxed{
\text{[V] v14.243: 42 moments, six direct checks, HS² bound,}\\
\text{remainders 6.49e-16/1.28e-17 all verified.}\\
\text{[D] Far residual consumer: z_n combined (not separately}\\
\text{bounded); odd 1/[n(n-1)] retained; norm via zeta-tails.}\\
\text{No correction to v14.243.}
}$$

---

HANDOFF-ACK
from: v14.243
target: sandbox
status: closed
result: Combined-support Far action audited with no correction. Whole Far residual norm consumer derived: explicit C(n)+z_n·D(n)+E(n) decomposition with oscillatory z_n retained through combining, odd-sector shift via 1/n²+O(1/n³), norm bounded by zeta-tails of explicit powers. All inputs available from v14.223/v14.243.
constraints: None.
