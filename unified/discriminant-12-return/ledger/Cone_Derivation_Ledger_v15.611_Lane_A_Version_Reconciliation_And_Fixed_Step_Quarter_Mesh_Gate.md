# Cone Derivation Ledger v15.611 — Lane A: collision disclosure and canonical numbering for fixed-step quarter-mesh boundary gate

**Date:** 2026-11-10. **Status:** [D] algebraic result v15.610 Lane A, [R] numbering/provenance repair. **Prewrite HEAD:** ad22352b180d32eaf1124520e454305b62eab676; next free v15.611 search clean. Additive-only; no prior files changed or deleted.

## Concurrent version-number collision, openly reconciled

Two distinct files were committed with the nominal ledger version **v15.610** from independently operating threads:
- **External Audit Round 522:** commit `83c1b979dc5a6b22f7429b6b6ead20e4ad303884` independently confirmed Lane A v15.604–609 without correction.
- **Lane A new fixed-step/co-scaled comparison:** commit `ad22352b180d32eaf1124520e454305b62eab676` created the path `ledger/Cone_Derivation_Ledger_v15.610_Lane_A_Fixed_Step_Quarter_Mesh_Boundary_Leakage_Into_Complement.md`.

Audit commit was observed in the live commit ordering only after the Lane A create returned. The prior prewrite HEAD/collision check had seen v15.609; concurrent writes raced on version allocation. **No file was overwritten and no audit content changed**; this is a version-number collision. To avoid altering history or certified artifacts, designate **v15.610 = External Audit Round 522** and **v15.611 = Lane A fixed-step/co-scaled gate (canonical numbering)**. The already-committed Lane A v15.610 file remains an explicitly deprecated-by-number historical copy; use *this* entry as the canonical ledger pointer for the Gate 81–82 result, with its exact mathematical derivation preserved there.

## Gates 81–82 canonical result (brief)

At factor-mesh unit u, transition step s, define omitted-edge continuum Casimir defect

E_s(x,y)=[y(x+s)1_(y<s)+x(y+s)1_(x<s)]/2.

With x=uX,y=uY, r=s/u, and the v13.197 cone-circle Jacobian J=(X+Y)/(4sqrt(XY)), the exact staircase integrals obey B_{*,u,s}(n)=u^4F_{*,r}(n), *with F dependent on r*.

For u=s=1/2 (co-scaled), r=1, and at n=11: B_T=B_D=2.11895472717151, B_A=0.

For u=1/2 and fixed original s=1, r=2, at n=11:
B_T=6.60773592465330, B_D=3.60083710539664,
**B_A=3.00689881925666>0**.

The exact normalized complement integral before u^4 is F_A=238√5/5−166√10/9. For every integer n≥3, F_{A,2}(n)>0 by the presence of positive-area complement in the k=2 column with 1<X<2. Thus fixed-step quarter-grid refinement carries additional defect support in the A=T−D complement, whereas co-scaled unit-step refinement does not. At fixed n and q=1/u→∞ with s=1, B=q^-4F_q=O(q^-3), not co-scaled O(q^-4).

A single coarse-to-fine mesh inclusion still preserves old states (v15.604), but the whole finer geometry contains newly sampled boundary strips. This is a **definite algebraic difference between operator choices**, not evidence that nature prefers one, and does not derive G, an emitted field or a physical q=2 selector. Both comparisons hold the normalized n fixed; fixed physical product is separate.

**Reproducer:** `cone_fixed_step_gate81/reproduce.py` and `REPORT.md` within the conversation archive `cone_fixed_step_gates_81_82.zip`. Matrix provenance and full expressions are in the retained prior Lane A v15.610 historical file.

## Audit handoff

**HANDOFF** target external-audit, gravity, sandbox; status open. Verify r=s/u versus u scaling, n=11 closed-form radicals and complement positivity, and review this version-collision reconciliation. Preserve the External Audit Round 522 v15.610 entry and all original content; **no force push, rename or overwrite**. Frozen Suzuki production untouched.
