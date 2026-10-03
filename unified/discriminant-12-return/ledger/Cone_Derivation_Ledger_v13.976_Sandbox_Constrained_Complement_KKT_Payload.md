# Cone Derivation Ledger v13.976 — Sandbox Constrained-Complement KKT Payload

**Date:** 2026-10-03
**Track:** Sandbox (our Lane B), at Lane A request
**Status:** [N] three constrained solves per parity; [D] v13.975 KKT identities realized numerically.
**Parents:** v13.974, v13.975
**Authorization:** Jeremy, 2026-10-03

---

## 1. What this is

v13.975 proves the constrained-complement KKT identities: three solves
per parity (two core-coupling, one source) generate all nonresonant
backgrounds for the v13.971 six-dimensional solve. This entry freezes
the numerical payload.

Frozen Z from v13.974 used **without rerun, without rotation**.
G_B = Z^T B_T Z corrected via principal positive-definite
G_B^{-1/2} (defect ~3e-14, signs preserved).

## 2. Results [N]

**even-v:**
- H_C(0)hat = [[2.14e-07, 6.34e-07],[6.34e-07, 1.88e-06]]
- f6_hat = [1.3856, 0.5887, −0.1350, 0.2684, 0.6610, 0.9723]
- h_reg_hat = 8.8639
- Solve residuals: ≤5e-14 (block), ≤1.3e-14 (constraint)

**odd-v:**
- H_C(0)hat = [[2.12e-05, 4.31e-05],[4.31e-05, 8.78e-05]]
- f6_hat = [−0.6728, −0.3500, −0.0837, −0.1629, −0.2949, −0.5533]
- h_reg_hat = 0.3757
- Solve residuals: ≤7.4e-15 (block), ≤6.1e-16 (constraint)

Lower four f6 coordinates match v13.974 Z^T f_T exactly (consistency).

K0 = Z^T A_TC(0) replayed; values recorded for v13.828 cross-check.

## 3. Payloads

`unified/discriminant-12-return/research-notes/p4_payload_kkt/{even-v,odd-v}/`

Per parity: G_B.npy, K0.npy, X_C.npy (7999×2), x_f.npy (7999),
HChat.npy (2×2), f6_hat.npy (6), saddle_lam{1,2,f}.npy (4),
manifest.json — all SHA-256 in manifests.

Lane A generates all t-dependent terms via
r(t)=p_T(t)^T x_f, h_{C,red}(t)=p_C(t)−X_C^T p_T(t), h_P(t)=Z^T p_T(t).

## 4. Errors kept separate

Midpoint arithmetic, solve residuals (above), and exact-P4 subspace
error (v13.974 certificates) not combined.

---

*No Xi/RH/convergence claim. No Fourier sweep performed.*
