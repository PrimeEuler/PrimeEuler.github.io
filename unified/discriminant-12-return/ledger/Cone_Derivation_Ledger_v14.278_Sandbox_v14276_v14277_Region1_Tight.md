# Cone Derivation Ledger v14.278 — Sandbox: v14.276/v14.277 Consumed; Region-1 Far Evaluator Tight

**Date:** 2026-10-11
**Track:** Sandbox / v14.276+v14.277 handoff response
**Status:** [V] v14.276's direct a-start moments verified (SHAs d141dcda.../c9ece888... match; 85 moments/sector; max radii 8.946e-46/8.939e-46). [V] v14.277's compact Far coefficients noted (42 moment pairs/sector; direct row checks pass; remainders 6.88e-16/1.36e-17). [D] Updated sandbox evaluator (`sandbox_region1_evaluator_v2.py`) to use v14.276's direct moments (no subtraction). Far-moment intervals now tight: S_far(n=b−2) relative radius ~4.8e-22 (vs ~9.6 with subtraction). The v14.275 blocker is resolved. [W] Code remains in ~/workspace/d12/ sandbox namespace; v14.276 asked for repository commit but research-notes/ writes need Jeremy's explicit per-item approval (standing authorization covers ledgering only). Close-row evaluation (b≤m<a) and pole remain envelope-only; Regions 2–3 not yet coded.
**Parents:** v14.223, v14.250, v14.253, v14.263–277.
**Collision check:** live ledger max v14.277 (Lane A) at write time; v14.278 is next-free. No collision.

---

## 1. v14.276 verification [V]

Direct later-start moments at a=1024003/1024004:
- even-v: SHA d141dcdaafcd6b4d45315d17d009b7fd60953ae9b5707b1ac50c068b72c6a02d (55248 bytes) ✓
- odd-v: SHA c9ece88832d67f5c4a803d8063dc53bb41b037f4c42e75433424137dbf95179e (55090 bytes) ✓
- 85 moments/sector (42 Ubar + 42 Vbar + P_tail), max radii match v14.263 levels.
- Normalization uses a (not b): Ubar_j=a^{2j+2}Σ_{m≥a}, Vbar_j=a^{2j+1}Σ_{m≥a}. Correct per v14.276.
- No subtraction needed; blocker from v14.275 removed.

## 2. v14.277 noted [V]

Compact Far coefficients from actual CI lift (run 38187015223):
- 42 exact moment pairs/sector (M_j, Z_j as exact integers/rationals).
- Three direct Far row checks per sector pass.
- Geometric remainders 6.88e-16 (even) / 1.36e-17 (odd).
- Scope is compact component only; infinite D*y tail is separate (this sandbox work).
- No correction; not directly consumed by Region-1 evaluator (different component).

## 3. Updated evaluator [D]

`sandbox_region1_evaluator_v2.py`:
- Loads v14.276 direct a-start moments (no subtraction).
- Implements v14.276's formula:
  S_far(n) = (c/a)[Σ_j(n/a)^{2j+1}Ubar_j − z_nΣ_j(n/a)^{2j}Vbar_j]
             + α·p_n·P_tail + Rem.
- Uses v14.266 corrected ordering, v14.272 O(1/[b·log b]) remainder.
- Test at n=b−2 (worst-case Region-1 output):
  even: S_far ≈ −2.077e−7, radius 1e−28 (relative 4.8e−22).
  odd:  S_far ≈ −2.076e−7, radius 1e−28 (relative 4.8e−22).
- Moment radii (~1e−46) propagate cleanly; no subtraction blowup.

## 4. Repository commit note [W]

v14.276's handoff asks: "Please commit additive evaluator code and
evaluated payloads in the repository."

This is NOT done. Jeremy's standing authorization (2026-10-05)
covers autonomous LEDGERING of handoff responses only.
Research-notes/ writes explicitly require his per-item approval:
"Everything else — foundations papers, exploratory work,
non-handoff entries, research-notes writes — still needs his
explicit per-item approval."

The code (`sandbox_region1_evaluator.py`,
`sandbox_region1_evaluator_v2.py`) remains in ~/workspace/d12/.
If Jeremy wants it in research-notes/, he needs to say so explicitly.

## 5. Remaining open

- Close rows (b≤m<a): envelope-only via v14.274's coded bound (~1.2e-5).
  Explicit 8/|n−m| evaluation not yet coded.
- Pole contribution: separate, not yet included.
- Regions 2–3: not yet coded.
- Physical constants (c, z_n, α, p_n) as certified intervals:
  prototype uses floats; production needs directed intervals.

---

HANDOFF-ACK
from: v14.276 (sandbox part)
target: sandbox
status: closed
result: Direct a-start moments verified and consumed. Evaluator v2 uses them with tight intervals (rel radius ~5e-22). v14.275 subtraction blocker resolved. Repository commit declined pending Jeremy's explicit approval (standing auth covers ledgering only).
constraints: None.

HANDOFF-ACK
from: v14.277 (sandbox part)
target: sandbox
status: closed
result: Compact Far coefficients noted (not directly consumed by Region-1 evaluator; separate component). No correction. Infinite D*y tail work continues separately.
constraints: None.
