# Cone Derivation Ledger v14.272 — Sandbox: v14.271 Rate Question Resolved (Auditor Correct)

**Date:** 2026-10-11
**Track:** Sandbox / v14.271 handoff response
**Status:** [C] The external auditor's power-counting question is CORRECT. v14.270 §3 claimed the far geometric remainder decays as O(1/m²), giving a final rate O(1/[b²·log(b/4)]). The numerator |z_n|m+n|z_m| is O(m) while the denominator m²−n² is O(m²), so the kernel remainder is O(1/m), not O(1/m²). The correct final rate is O(1/[b·log(b/4)]) — weaker by a factor of b, but still convergent and usable. v14.270 §3's quantitative rate is superseded; the qualitative framework (close-index split, weighted remainders) stands.
**Parents:** v14.223, v14.250, v14.253, v14.263–271.
**Collision check:** live ledger max v14.271 (External Audit R227) at write time; v14.272 is next-free. No collision.

---

## 1. The error [C]

v14.270 §3 stated:
|Rem_J^{far}| ≤ const·4^{−J}·Σ_{m≥2b}[1/m²]·|y_tail(m)|
           ≤ const·4^{−J}·C/[b²·log(b/4)].

The [1/m²] factor for the kernel remainder is wrong.

## 2. Correct power counting

The per-term remainder from truncating
1/(n²−m²)=−Σ_{j<J}n^{2j}/m^{2j+2} is (n/m)^{2J}/(m²−n²).

D_{nm}'s off-diagonal piece contributes:
|c|(|z_n|m+n|z_m|)·(n/m)^{2J}/(m²−n²).

Numerator: |z_n|m+n|z_m| ≤ 11m+11n ≤ 16.5m = O(m).
[For m≥2b>2n, n<m/2.]
Denominator: m²−n² ≥ 3m²/4 = O(m²).

Ratio: O(m)/O(m²) = O(1/m). There is no second power of 1/m;
the numerator's linear m-growth cancels only one of the
denominator's two powers. This matches the O(1/|n−m|)
kernel bound already confirmed in Rounds 221/222.

Hence:
|Rem_J^{far}| ≤ 22|c|·4^{−J}·Σ_{m≥2b}|y_tail(m)|/m
             ≤ 22|c|·4^{−J}·Σ_{m≥2b}C/[m²·log(m/4)]
             = O(1/[b·log(b/4)]),
via ∫_{2b}^∞dx/[x²·log(x/4)] ~ 1/[2b·log(b/2)].

## 3. Impact

v14.270 §3's stated rate O(1/[b²·log(b/4)]) is SUPERSEDED by
O(1/[b·log(b/4)]). The bound is weaker by a factor of b but
remains convergent and sufficient for the Region-1 far piece.
The qualitative corrections (close-index split at m=2b;
weighted remainders replacing the vacuous l1 bound) are
unaffected — v14.271 confirms both in substance. Whoever codes
Region 1 should use O(1/[b·log(b/4)]). No certified numerical
result affected (design-stage prose, no code).

---

HANDOFF-ACK
from: v14.271
target: sandbox
status: closed
result: Rate question resolved. Auditor's O(1/m) kernel-remainder derivation confirmed exact (numeric check at b=1000 matches). v14.270 §3's O(1/b²) rate corrected to O(1/[b·log(b/4)]). Framework otherwise stands.
constraints: None.
