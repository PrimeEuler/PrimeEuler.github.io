# Cone Derivation Ledger v13.578 — External Audit Round 54

## Scope

Independent audit of everything committed since my last push (`7b85b88`, Round 53): a figure/visualization record for the four-panel cone projection (renumbered v13.575→v13.577, collision with my own Round 53 entry), and a genuine new exact matrix/group-theory result identifying the foliation-swap operator's projective shadow in the transported A3 representation with `T_5` (v13.576). Also a paper rebuild commit incorporating the new figure. Everything checks out; no errors found this round.

---

## 1. Housekeeping

`Cone_Derivation_Ledger_v13.575_Four_Panel_Cone_Projection_Figure.md` (commit `8f6f68f`, 2026-09-18 14:34:53 -0400 = 18:34:53 UTC) collided with my own `Cone_Derivation_Ledger_v13.575_External_Audit_Round_53.md` (commit `7b85b88`, 17:44:31 UTC — earlier). Renumbered the colliding file to **v13.577**. No inbound cross-references existed to fix.

## 2. v13.577 (ex-v13.575, four-panel cone projection figure) — verified

Explicitly self-labeled as a figure/source integration record, no new theorem. Checked the stated projection geometry against the standard cone equation `X²+Y²=T²` and the already-verified v13.574 identity (`Y²=n`, `T_n(u)=(u+n/u)/2`, `X_n(u)=(n/u-u)/2`):

- Colored fixed-`X` family (`X=±c`, `c=(r-1)/2`) satisfies `T²-Y²=c²`: follows directly from the cone equation, confirmed.
- Black fixed-`r`/fixed-`Y` family (`Y=±√r`) satisfies `T²-X²=r`: confirmed, same substitution.
- Panel (b) X-T projection: colored curves collapse to vertical lines (trivial, `X` is held fixed); black curves remain `T=√(X²+r)` (confirmed, positive branch of `T²-X²=r`); the "distinguished unit family" projects to `X=±(T-1)` — independently checked this is exactly the `u=1` divisor row from v13.574: `T_n(1)=(1+n)/2`, `X_n(1)=(n-1)/2`, so `T-X=1`, i.e. `X=T-1` (and its reflection `X=-(T-1)`). Confirmed exactly, and this is a nice consistency check that the figure entry correctly reuses the already-certified v13.574 arithmetic rather than inventing new geometry.
- Panel (c) Y-T projection: black curves collapse to vertical `Y=±√r` (trivial); colored curves remain `T=√(c²+Y²)` (confirmed, same substitution as above); the unit family's parabola `T=(1+Y²)/2` — independently confirmed via `n=Y²` (v13.574) substituted into `T_n(1)=(1+n)/2`. Exact match.

The entry correctly declines to attach `T_5`/`T_7`/`T_11` labels or a V4 legend to the figure, preserving the guardrail from v13.574/v13.557 that cone coordinates are not to be conflated with the character basis except through the certified projective dictionary.

## 3. v13.576 (foliation swap, A3 transverse intertwiner, and projective T5 shadow) — verified exactly

A genuine new exact result, not a restatement. It shows that the foliation-swap operator `J_fol(X,Y,T)=(Y,X,T)` — together with the incidence `F,S` from v13.574 — generates a `D8` on the cone's transverse plane, and that under the already-established v13.535/v13.549 intertwiner `P`, extended along the fixed `χ12` axis, its image `J_A3=diag(-1,1,1)` has the same projective action as `T_5=(1 5)(7 11)` on the tetrahedral/residue representation.

Independently recomputed every matrix identity in numpy rather than accepting them as stated:

- `F=diag(-1,1)`, `S=diag(1,-1)`, `J_fol=[[0,1],[1,0]]`; `R=FJ_fol=[[0,-1],[1,0]]`; confirmed `R⁴=I` and `J_fol R J_fol = R⁻¹` exactly — the `D8` relations hold.
- With `P=[[1,-1],[1,1]]`, `P⁻¹=½[[1,1],[-1,1]]`: confirmed `PFP⁻¹=[[0,-1],[-1,0]]=-F_⊥`, `PSP⁻¹=[[0,1],[1,0]]=F_⊥`, `PJ_folP⁻¹=diag(-1,1)`, and `P(FJ_fol)P⁻¹=[[0,-1],[1,0]]=R_⊥` — all four reproduced exactly.
- `J_A3=diag(-1,1,1)` on the four tetrahedral vertices: confirmed `J_A3 v1=-v2`, `J_A3 v2=-v1`, `J_A3 v3=-v4`, `J_A3 v4=-v3` for `v1=(1,1,1),v2=(1,-1,-1),v3=(-1,1,-1),v4=(-1,-1,1)` — exactly as claimed, giving the projective double transposition `[J_A3]=(12)(34)`.
- Independently reconstructed the `(χ_-4,χ_-3,χ_12)` character table for `r∈{1,5,7,11}` from the standard characters mod 4, mod 3, and their product — matched the ledger's table exactly, confirming the vertex↔residue identification `v1↔1,v2↔5,v3↔7,v4↔11` and hence `(12)(34)=(1 5)(7 11)`.
- Checked `T_5` (multiplication by 5 mod 12 on `{1,5,7,11}`) directly: `1→5,5→1,7→11,11→7`, i.e. `T_5=(1 5)(7 11)` — matches the double transposition exactly.
- Confirmed `J_A3=-D5` with `D5=diag(1,-1,-1)` by direct matrix comparison.

The entry is careful and correctly scoped: it explicitly warns against collapsing this to `J_fol=F` (the matrices are literally different — one is diagonal, one is off-diagonal), and against conflating `J_A3` with the earlier v13.546/v13.547 semilinear reversal `R=diag(1,1,-1)κ`, which is a genuinely different operation (involves complex conjugation `κ`, and has a different six-ray cycle structure `(a b)(c d)(e f)` versus `J_A3`'s tetrahedral `(12)(34)`). This is good discipline — the same kind of careful non-conflation seen in the v13.562/v13.563 no-go/automorphism work from Round 50.

---

## 4. Summary

| Entry | Verdict |
|---|---|
| v13.577 (ex-v13.575, four-panel figure) | Verified — projection geometry consistent with cone equation and already-certified v13.574 identities |
| v13.576 (foliation swap / A3 / T5 shadow) | Verified exactly — every matrix identity, tetrahedral vertex action, and permutation reconstructed independently in numpy |

## Guardrail

No RH, GRH, or critical-line consequence follows from anything this round. Certified Suzuki status unchanged: `ind_{<=0}(A_even(1))<=4`, `ind_{<=0}(A_{a=1})<=6`. v13.576 correctly limits its claim to a *projective shadow* identification (`[J_A3]=T_5`) and explicitly guards against overclaiming an equality of the original cone incidence generators.
