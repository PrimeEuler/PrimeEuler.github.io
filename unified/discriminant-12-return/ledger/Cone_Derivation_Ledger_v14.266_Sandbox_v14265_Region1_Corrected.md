# Cone Derivation Ledger v14.266 — Sandbox: v14.265 Region-1 Question Resolved (Auditor Correct)

**Date:** 2026-10-10
**Track:** Sandbox / v14.265 handoff response
**Status:** [C] The external auditor's Region-1 question is CORRECT. v14.264 §3 had the moments backwards. The z_n·m term factors z_n out, pairing it with V_j (z-free) at n^{2j}; the n·z_m term keeps z_m inside, giving U_j at n^{2j+1} with no extra z_n. Correct formula: (D·y_tail)_n = -c·z_n·Σ_j n^{2j}·V_j + c·Σ_j n^{2j+1}·U_j + α·p_n·P_tail + Rem_J. v14.264 §3 Region 1 is superseded; Regions 2–3 and diagonal treatment stand.
**Parents:** v14.223, v14.250, v14.253, v14.255–265.
**Collision check:** live ledger max v14.265 (External Audit R225) at write time; v14.266 is next-free. No collision.

---

## 1. The error [C]

v14.264 §3 Region 1 stated:
(D·y_tail)_n = -cΣ_j n^{2j}U_j + c·z_nΣ_j n^{2j+1}V_j + αp_nP_tail.

This pairs z_n with V_j at the WRONG power and U_j without z_n
at the WRONG power.

## 2. Correct derivation

D_{nm}=c(z_n·m-n·z_m)/(n²-m²)+αp_np_m.
For n<b≤m: 1/(n²-m²)=-Σ_{j≥0}n^{2j}/m^{2j+2}.

**z_n·m term:**
c·z_n·m·[-Σ_j n^{2j}/m^{2j+2}] = -c·z_n·Σ_j n^{2j}/m^{2j+1}.
Summing over m: -c·z_n·Σ_j n^{2j}·[Σ_m y_tail(m)/m^{2j+1}]
= -c·z_n·Σ_j n^{2j}·V_j.
(z_n factors out; V_j is z-free.) ✓

**n·z_m term:**
c·(-n·z_m)·[-Σ_j n^{2j}/m^{2j+2}] = +c·Σ_j n^{2j+1}·z_m/m^{2j+2}.
Summing: +c·Σ_j n^{2j+1}·[Σ_m z_m y_tail(m)/m^{2j+2}]
= +c·Σ_j n^{2j+1}·U_j.
(z_m inside U_j; no extra z_n.) ✓

**Correct formula:**
(D·y_tail)_n = -c·z_n·Σ_{j<J}n^{2j}V_j + c·Σ_{j<J}n^{2j+1}U_j
               + α·p_n·P_tail + Rem_J.

This matches the structural pattern from Round 221 (v14.240/v14.243):
z_n pairs with the z-free moment at the matching power.

## 3. Impact

v14.264 §3 Region 1 is SUPERSEDED. Regions 2–3, diagonal treatment,
and the t-integral framework stand. No certified numerical result
affected (Region 1 was [D] prose, no code). v14.262/v14.263 outputs
unchanged.

---

HANDOFF-ACK
from: v14.265
target: sandbox
status: closed
result: Region-1 formula corrected. Auditor's derivation confirmed exact. The z_n pairs with V_j (not U_j), at n^{2j} (not n^{2j+1}).
constraints: None.
