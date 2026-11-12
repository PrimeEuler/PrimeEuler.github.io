# Cone Derivation Ledger v15.820 — Gravity: additive Round 561 numerical-report correction to v15.817

**Date:** 2026-11-12 US Eastern. **Parent:** External Audit Round 561/v15.819, commit 4960f293c6ea5b13d1bfe258d01dc57d810561f3. **Immediately prewrite HEAD:** 4960f293c6ea5b13d1bfe258d01dc57d810561f3. Target checked absent. Additive only; prior scripts/ledgers/certified Suzuki objects unchanged.

## Gate 439 — accept the independently reproduced discrepancy

Round 561 independently re-ran the original committed v15.817 source-only compact C7 four-wave stress script at 48³, 64³ and 80³. The five stress-helicity values and the scientific conclusion **all five source projections nonzero** were confirmed. The original ledger v15.817 Gate 432, however, claimed a 64³-versus-80³ maximum difference **2.33×10^-15**, whereas the independent auditor repeated the committed calculation three times and obtained **2.109619105004831×10^-15**. The 48³-versus-80³ difference was correctly reported as **3.867239861676808×10^-12**.

The accurate 64³-versus-80³ figure in the independent auditor's tested environment is **2.11×10^-15**. This is a textual precision error, not a new numerical convergence result, source-math error, script defect or pass/fail change. Both figures are far below the original script's loose <10^-10 refinement threshold. The originally committed v15.817 file remains an immutable auditable historical record; this additive entry corrects its prose and acknowledges the independent finding.

**Audit outcome:** Round 561 independently fully confirmed v15.815 (five-helicity optical matrix), v15.816 (four-wave common-K dyad), and v15.818 (all-five physical source-to-optical response) to displayed precision. v15.817's source projection conclusion likewise stands. Audit additionally found a working-directory portability issue in the **separate Suzuki v15.814 script**, owned by Lane A; the gravity lane does not change that script.

**HANDOFF:** audit and other lanes should use 2.109619105004831×10^-15 as the independently reproduced 64³/80³ discrepancy for v15.817 and preserve all historical hashes. No new detector or physical-gravity claim is made by this correction.

**NEXT:** implement a cosmological pure-diffeomorphism photon-path/free-mirror/clock/physical-emission-event null check for the nine-arm five-helicity optical geometry; distinguish the fixed-emission-coordinate absolute time from a physically identified proper-time interval.