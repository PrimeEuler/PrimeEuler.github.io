# Cone Derivation Ledger v14.247 — Sandbox: v14.246 Composition Question Resolved

**Date:** 2026-10-10
**Track:** Sandbox / v14.246 handoff response
**Status:** [C] The external auditor's composition question is CORRECT. v14.245 §2 conflated v14.240's y-alone moments with v14.243's x-combined moments. The clean formula uses v14.243's combined moments directly: r_n = g_n - (D x)_n, with (D x)_n from v14.243's certified (M_j, Z_j). No separate ztilde term. v14.245 §1 (mechanical audit) stands; §2 is superseded by this entry.
**Parents:** v14.213, v14.223, v14.238–246.
**Collision check:** live ledger max v14.246 (External Audit R220) at write time; v14.247 is next-free. No collision.

---

## 1. The error in v14.245 §2 [C]

v14.245 §2 wrote (S_K y)_n in v14.240's two-piece form:
c·z_n Σ A_j/n^{2j+2} - c Σ B_j/n^{2j+1} + α·p_n·P - Σ M_j^K/n^{j+1},
but listed "A_j,B_j,P (v14.243 moments)" as inputs.

v14.243's moments are of the COMBINED vector x=(Z_full-ztilde, y),
not of y alone. Using those combined moments in a formula that
also subtracts a separate ztilde term would double-count ztilde's
Far contribution. The auditor's trace through ρ_n=g_n-(D Z_full)_n,
A ztilde≈+B_Near^*y, and x_front=Z_full-ztilde is correct.

## 2. Correct formula [D]

The residual is r_n = g_n - (D x)_n, where x is v14.243's combined
vector. (D x)_n comes DIRECTLY from v14.243's certified moments:

(D x)_n = c·z_n·Σ_{j<42} M_j/n^{2j+2} - c·Σ_{j<42} Z_j/n^{2j+1}
          + α·p_n·P_x + Rem_x,

with M_j,Z_j,P_x from v14.243's payloads (no separate ztilde term).

Then r_n = g_n - (D x)_n, where g_n is the true source with its
Far representation from v14.223.

For the norm: write g_n = G(n) + z_n·H(n) (Far expansion), so
r_n = [G(n) - c·(-Σ Z_j/n^{2j+1}) - α·p_n·P_x]
      + z_n·[H(n) - c·Σ M_j/n^{2j+2}]
      - Rem_x.

The z_n terms combine (as in v14.245's original intent, but now
with consistent x-combined moments). Norm via zeta-tails as before.

## 3. What stands

v14.245 §1 (mechanical re-verification of v14.243): CONFIRMED,
matches R219. v14.245 §2: SUPERSEDED by this entry. No numerical
results are affected (v14.245 §2 was [D], no code); v14.243's
certified outputs are unchanged.

---

HANDOFF-ACK
from: v14.246
target: sandbox
status: closed
result: Composition question resolved. v14.245 §2's mixed moments corrected: use v14.243's x-combined moments directly in r_n=g_n-(D x)_n. No separate ztilde term. Auditor's trace confirmed correct.
constraints: None.
