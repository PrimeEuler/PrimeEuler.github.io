# Cone Derivation Ledger v14.012 — Common-Mode Remote Amplitude: Sandbox Response to v14.010

**Date:** 2026-10-04
**Track:** Sandbox / no-twist Suzuki Xi scalar certification
**Status:** [D] leading remote Schur term is provably parity-common (structural theorem); [D] coefficient is exactly A_{p,N}=C_{p,N}L_{p,N}^2 from the unit-energy boundary trace; [N] A_{p,N} sequence characterized as check-target for the v14.009 calculation; [O] quantitative kernel bounds (resolvent contraction, sampling difference) belong to the v14.009 track.
**Parents:** v14.010, v14.009, v14.008.
**Collision resolution:** this entry was originally committed as v14.011 at 20:57:44Z, but Lane A v14.011 committed earlier at 20:54:55Z. Per the project collision rule, the earlier entry keeps v14.011 and this sandbox response is renumbered v14.012 without changing its theorem content.

---

## 1. Handoff

This entry responds to the v14.010 HANDOFF (target: sandbox, type: payload, status open):

> Use the measured sequence C_e L_e^2 versus C_o L_o^2 as the numerical target/check for the v14.009 analytic normalized-tail calculation; determine whether the leading remote Schur term is provably parity-common and whether its coefficient can be expressed from the unit-energy boundary trace.

Deliverable: theorem-or-obstruction. Constraints honored: supplements (not replaces) the v14.009 handoff; the common limit is not promoted from numerics alone; prime oscillations retained explicitly.

---

## 2. Numerical target: the A_{p,N} sequence [N]

A_{p,N} := C_{p,N} L_{p,N}^2, the squared remote 1/n coefficient of the unit-energy finite source solution y_{p,N} = sqrt(C_{p,N}) x_{p,N}.

| N | A_e | A_o | A_o - A_e | rel. |
|---|---|---|---|---|
| 768 | 432.1566706 | 438.3903018 | +6.2336 | +1.442% |
| 1536 | 574.3846199 | 580.4572551 | +6.0726 | +1.057% |
| 3072 | 741.2231221 | 743.2821499 | +2.0590 | +0.278% |
| 4000 | 802.9912333 | 802.2809153 | -0.7103 | -0.0885% |

Verified: A = C L^2 reproduces the reported A to all 13 digits from the reported (C, L) at N=4000. Unit-energy 1/n amplitudes sqrt(C)L: +28.33709995 (even), -28.32456381 (odd) — the 170x raw-L difference is exactly compensated by C-normalization.

Gap characterization [N/I]: |A_o - A_e| decreases monotonically 6.234 -> 0.710; the sign change between N=3072 and N=4000 supports oscillation around a common limit, not a one-sided parity inequality. Both A_e, A_o increase with slowing increments, consistent with a shared A_infinity near 810-830 (extrapolation, not certified).

Independent structural verification [N]: running the LDDD producer (suzuki_ldd_source_operator.py) on a common mode set: max|z^{(e)} - z^{(o)}| = 0.0, max|diag^{(e)} - diag^{(o)}| = 0.0 — the z-vector and diagonal are exactly sector-independent. T^{(e)} - T^{(o)} = 2 pe pe^T + 2 po po^T verified to 3.2e-20 (LDDD arithmetic floor). Pole decay: n pole^{(e)}_n -> 4cosh(1/2)/pi = 1.43573797, n pole^{(o)}_n -> 4sinh(1/2)/pi = 0.66347915, monotone from below.

---

## 3. Analytic: parity-commonality [D]

**Proposition 1.** For p in {e, o}: T^{(p)} = T^{cm} + alpha_p v_p v_p^T, where T^{cm} is sector-independent, alpha_e = +2, alpha_o = -2, and v_p(n) = pole^{(p)}_n satisfies 0 < v_p(n) <= (4 c_p / pi)(1/n) with c_e = cosh(1/2), c_o = sinh(1/2).

*Proof.* The off-diagonal (2/pi)(n_i z_{n_i} - n_j z_{n_j})/(n_i^2 - n_j^2) and diagonal diag_n use only z_n, diag_n, which never reference the sector in hp_parity_data_ld and are verified 0.0 sector-independent. The only sector-dependent terms are alpha_p pole_i pole_j (off-diagonal) and alpha_p pole_j^2 (diagonal). ∎

**Corollary.** The sector difference is rank-two with |(T^{(e)} - T^{(o)})_{ij}| <= C/(ij), C = 2(4/pi)^2 (cosh^2(1/2) + sinh^2(1/2)).

**Proposition 2 (structural).** S^{(p)}_{Q,N} = S^{cm}_{Q,N} + Delta^{(p)}_N, where S^{cm}_{Q,N} is sector-independent and Delta^{(p)}_N is an explicit sum of O(1) rank-one terms with |(Delta^{(p)}_N)_{nm}| <= C_p/(nm) for n, m remote. (Proof via Woodbury on the finite block; the quantitative finite-section constant in the coupling bound is [O].)

**Proposition 3 (common-mode form).** eta_{p,N} = A_{p,N} K_{N,p} + R_{p,N}, where K_{N,p} := sum_{n,m in R_p} (K^{cm}_N)_{nm}/(nm) with K^{cm}_N = (S^{cm}_{Q,N})^{-1} sector-independent, and R_{p,N} collects the kernel correction, subleading residual, and cross terms. Hence:

eta_{o,N} - eta_{e,N} = (A_{o,N} - A_{e,N}) Kbar_N + Abar_N (K_{N,o} - K_{N,e}) + (R_{o,N} - R_{e,N}).

The leading term is proportional to (A_o - A_e), numerically 8.85e-4-relative and shrinking. The coefficient Kbar_N is parity-common by construction.

**Prime oscillations [D].** The common kernel inherits sector-independent prime oscillations (z_n contains 2 sum_q w_q sin(n pi log q / 2); diag_n contains -sum_q w_q (2 - log q) cos(n pi log q / 2), q in {2,3,4,5,7}, all O(1) non-decaying). They do not break parity-commonality but forbid replacing K^{cm}_N by a smooth envelope in any quantitative bound.

---

## 4. Answers

**Q1: Is the leading remote Schur term provably parity-common?** YES, structurally (Propositions 1-3). The entire sector dependence of the source operator is a rank-one O(1/(nm)) pole term; it propagates to a parity-common leading kernel with explicitly-structured corrections.

**Q2: Can its coefficient be expressed from the unit-energy boundary trace?** YES. The coefficient is exactly A_{p,N} = C_{p,N} L_{p,N}^2, computed solely from finite-section data (L_{p,N} from <z, x_{p,N}>, <p, x_{p,N}>; sqrt(C_{p,N}) the unit-energy normalization). No remote data enters.

**Not yet proved [O]:** quantitative bounds on Kbar_N, the resolvent contraction ||K^{cm} Delta^{(p)}|| < 1, the sampling difference K_{N,o} - K_{N,e}, and R_{p,N}. These are the v14.009 track's enclosure work; no structural obstruction was found.

---

## 5. Verdict

**THEOREM (structural) with quantitative gaps.** The leading remote Schur term is parity-common with coefficient from the unit-energy boundary trace. The A_{p,N} sequence is delivered as the numerical check-target for the v14.009 eta-difference calculation.

---

HANDOFF-ACK
target: Lane A
type: audit
parent: v14.010
status: closed
closes: v14.010 handoff (target sandbox, type payload)
result: THEOREM (structural) — leading remote Schur term provably parity-common; coefficient A_{p,N} from unit-energy boundary trace; prime oscillations retained explicitly. Quantitative kernel bounds remain open and belong to the v14.009 track (active).
