# Cone Derivation Ledger v13.575 — External Audit Round 53

## Scope

Independent audit of everything committed since my last push (`c889e89`, Round 52): a new exact arithmetic theorem connecting the AM-GM cone factor-hyperbola with the classical divisor summatory function and the Dirichlet hyperbola identity, mapped onto the already-certified v13.557 projective V4 correspondence. One version collision found and fixed (new work landed in the v13.573 slot my own Round 52 entry had just taken). Also noted a batch of figure/paper rebuild commits (reverts + PDF regeneration) that carry no new mathematical claim. Everything mathematical checks out; no errors found this round.

---

## 1. Housekeeping

`Cone_Derivation_Ledger_v13.573_Arithmetic_Incidence_and_Mod12_V4.md` (commit `efc1fa5`, 2026-09-18 13:38:47 -0400 = 17:38:47 UTC) collided with my own `Cone_Derivation_Ledger_v13.573_External_Audit_Round_52.md` (commit `c889e89`, 22:39:13 UTC the previous day — earlier). Renumbered the colliding file to **v13.574**. No inbound cross-references existed yet to fix (the entry is new and nothing else in the ledger referenced it by number).

Also present in this batch: `discriminant12_mod12_v4_cone_triple.py` figure-source reverts (`a805bb1`, `9de3e88`) and a paper/figure rebuild (`0b6cdfa`, `275b9ab`, regenerating the three PDFs). These are non-mathematical production changes (a figure-source revert to a prior state plus a rebuild) and carry no new numerical or algebraic claim to verify.

## 2. v13.574 (ex-v13.573, arithmetic incidence theorem and mod-12 V4 action) — independently verified exactly

This is a genuinely new exact theorem, not a restatement: it connects the AM-GM cone coordinates `(T,X,Y)` on the fixed-`n` factor hyperbola directly to the classical divisor summatory function `D(n)`, the harmonic sum `nH_n`, and the Dirichlet hyperbola method, then identifies the resulting factor-exchange/root-sheet-exchange V4 with the already-certified (Round 49) v13.557 projective correspondence `T_5↔-R_X, T_7↔R_XR_Y, T_11↔-R_Y`.

Independently re-derived and/or numerically checked every claim rather than accepting the algebra as stated:

- **Cone identity.** By hand: `T_n(u)^2-X_n(u)^2 = [(u+n/u)^2-(n/u-u)^2]/4 = ab = n` (using `(a+b)^2-(b-a)^2=4ab`). Exact, confirmed.
- **Square fixed-point claim** (`X_n(u)=0 ⟺ n=u^2`): trivial and confirmed.
- **Pronic claim** (`n=m(m+1) ⟹ X_n(m)=1/2`): checked exactly for `m=1,2,3,10` via `Fraction` arithmetic — `X_n(m)=1/2` in every case, confirmed.
- **Harmonic/divisor/residual identities** (`nH_n=D(n)+Σ{n/u}`, and `{g_n(u)}={n/u}` since `u` is an integer): re-derived algebraically and independently checked exactly (exact `Fraction` arithmetic, no floating point) for `n∈{1,2,6,11,12,30,42,100,143}` — `n H_n - D(n)`, `Σ{n/u}`, and `Σ{g_n(u)}` matched exactly in every case.
- **Dirichlet hyperbola identity** (`D(n)=2Σ_{u=1}^{m}⌊n/u⌋-m^2`, `m=⌊√n⌋`): independently recomputed `D(n)` directly by definition and via the hyperbola formula for the same nine values of `n` — matched exactly every time. This is also standard, well-known analytic number theory, correctly cited.
- **Incidence involutions form V4**: `F(X,Y,T)=(-X,Y,T)`, `S(X,Y,T)=(X,-Y,T)` obviously satisfy `F^2=S^2=I`, `FS=SF` — trivial, confirmed.
- **Projective correspondence to v13.557.** Reconstructed `R_X=diag(-1,1,1)`, `R_Y=diag(1,-1,1)` and the claimed `K_5=-R_X,K_7=R_XR_Y,K_11=-R_Y` directly in numpy, confirmed `F↔R_X`, `S↔R_Y`, `FS↔R_XR_Y` act on `(X,Y,T)` exactly as the stated incidence involutions. Then checked the **full 4×4 multiplication table** (all 16 pairs `a,b∈{1,5,7,11}`, not just the three cited examples) against the label dictionary `1→I,5→F,7→FS,11→S`: every product `label_mat[a]@label_mat[b] == label_mat[(a*b)%12]` held exactly. Fully consistent.
- **n=11,u=1 special case**: `X_11(1)=5`, `T_11(1)=6`, `T^2-X^2=36-25=11=n`, `X^2+Y^2=25+11=36=T^2` — all confirmed exactly.

The entry's own guardrails are appropriately conservative: it explicitly declines to identify the cone coordinates `(X,Y,T)` with the character basis `(chi_-4,chi_-3,chi_12)`, correctly notes the correspondence is only projective (the certified kernel elements are `-R_X`/`-R_Y`, not `R_X`/`R_Y` literally), and correctly distinguishes the positive unfloored sum `nH_n` from the (identically zero) signed reflection cancellation. This is careful, well-scoped work building cleanly on prior certified results rather than re-deriving them from scratch.

---

## 3. Summary

| Entry | Verdict |
|---|---|
| v13.574 (ex-v13.573, arithmetic incidence theorem) | Independently verified exactly — cone identity, divisor/harmonic identities (9 test values), Dirichlet hyperbola formula, full V4 multiplication table (16/16 pairs), and the n=11 special case all confirmed |
| Figure/paper rebuild commits | Non-mathematical production changes (revert + PDF regeneration); no claim to verify |

## Guardrail

No RH, GRH, or critical-line consequence follows from anything this round. Certified Suzuki status unchanged: `ind_{<=0}(A_even(1))<=4`, `ind_{<=0}(A_{a=1})<=6`. v13.574 is a self-contained exact number-theory result (divisor summatory / Dirichlet hyperbola tied to the AM-GM cone) that correctly reuses, rather than re-litigates, the already-certified v13.557 projective V4 dictionary.
