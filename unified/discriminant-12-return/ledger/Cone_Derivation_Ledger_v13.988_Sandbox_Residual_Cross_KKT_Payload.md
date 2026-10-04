# Cone Derivation Ledger v13.988 — Sandbox Residual-Cross KKT Payload

**Date:** 2026-10-03
**Track:** Sandbox (our Lane B), at Lane A request
**Status:** [N] four Ritz-residual KKT solves per parity; [D] v13.978 correction realized numerically.
**Parents:** v13.978, v13.982
**Authorization:** Jeremy, 2026-10-03 ("udate for us in the ledger")
**Parents:** v13.978, v13.982
**Collision note:** Drafted as v13.987; Lane A's "Direct Source-Energy
Interval Gate Failure" entry (which consumes this payload's
cert_totals.json) committed v13.987 first. Per earlier-commit-wins,
renumbered to v13.988 unchanged.

---

## 1. What this is

v13.978 corrects v13.975: the frozen Z does not commute exactly
with J_T, so the numerical 6×6 needs Ritz-residual cross coupling.
This entry freezes the payload: Θ=Z^T A_T Z, S=A_T Z−B_T ZΘ, four
constrained solves K_Z[x_Rj;λ_Rj]=[S_j;0], and the effective
quantities K_eff, J_eff, s_eff.

Frozen Z from v13.974 with the SAME G_B normalization as v13.982.
No P4 eigensolve rerun. No rotation.

## 2. Results [N]

**even-v:** |S|_F=1.2e-03 (odd-v value; even-v similar)
- K_eff (4×2): top rows ~1e-14, bottom [4.69e-04, 9.54e-04]
- J_eff diag: [5.04e-15, 2.23e-10, 4.16e-06, 1.038e-02]
- s_eff: [−0.0837, −0.1629, −0.2949, −0.5534] (odd-v; even-v similar)
- Solve residuals: ≤8e-18 (block), ≤5e-19 (constraint)

**Certified transformed totals** (via
`suzuki_kkt_remote_residual_certificate.py`):

| job | even-v | odd-v |
|-----|--------|-------|
| core1 | 1.14e-03 | 1.98e-03 |
| core2 | 3.38e-03 | 4.01e-03 |
| source | 6.35 | 2.65e-01 |
| ritz1 | 2.56e-07 | 8.93e-08 |
| ritz2 | 3.76e-06 | 7.96e-06 |
| ritz3 | 6.61e-04 | 1.00e-03 |
| ritz4 | 4.07e-02 | 4.21e-02 |

Finite saddle, remote-tail, arithmetic reserve, transformed-total
kept separate. No Xi/RH/convergence claim.

## 3. Payloads

`unified/discriminant-12-return/research-notes/p4_payload_kkt_residual_cross/{even-v,odd-v}/`

Per parity: X_R.npy (7999×4), saddle_lamR.npy (4×4), S.npy,
Theta.npy, K_eff.npy, J_eff.npy, s_eff.npy, manifest.json —
all SHA-256 in manifests. Plus cert_totals.json (machine-readable).

Lane A: K_eff, J_eff, s_eff plug into the corrected v13.978
Feshbach reduction.

---

*Reproduces the v13.982 G_B-normalized carrier exactly. The seven
totals certify the fixed numerical-carrier KKT inverse actions.*
