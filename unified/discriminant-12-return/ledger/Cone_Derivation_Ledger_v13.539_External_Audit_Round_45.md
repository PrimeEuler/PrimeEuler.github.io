# Cone Derivation Ledger v13.539 — External Audit Round 45

## Scope

Independent audit of everything committed since my last push (`b5c7c39`, v13.531): v13.532, v13.533 (M16001 payload-conversion gates), v13.534, v13.535, v13.536, v13.537 (complexified cone/D8/split-matrix algebra), plus the recurring "Complexified Arithmetic-Negation Lifts" entry, renumbered twice this round (v13.530 → v13.537 → v13.538) after colliding with concurrently-created entries both times.

**Two genuine, precisely-located issues found, both in v13.536, neither propagating further.** Everything else — including a substantial amount of new group theory — checks out exactly, several claims verified by full computational group-closure rather than by hand.

---

## 1. Housekeeping

The "Complexified Arithmetic-Negation Lifts" entry collided twice: first filed as v13.530 (colliding with my own already-pushed `v13.530_U24_Character_Cone_C2xC2xC2_Intertwiner.md`), renumbered to v13.537, which then collided with a second genuine entry (`v13.537_Split_Matrix_Congruences_and_Combined_C4xS4.md`). Renumbered a second time to v13.538, with both prior collisions recorded in its renumbering note.

## 2. v13.532, v13.533 (M16001 source/diag/X payload-conversion gates) — re-executed, confirmed exact

Both scripts re-run directly. `suzuki_M16001_source_payload_conversion_transcript.py`: genuine round-trip assertions (not just claims) confirm exact binary64→longdouble conversion for `Z`, `c`, `PI` (8001 entries each); output matches the ledger exactly. `suzuki_M16001_diag_X_payload_conversion_transcript.py`: same pattern for `diag0` (8001 entries) and `X` (79910 entries); **SHA-256 hashes of both payloads matched the ledger's stated values exactly**, confirming my local environment reproduces bit-identical `diag0`/`X` arrays to the CI run (useful context for the earlier Round 43 finding that the *downstream* Frobenius-replay arithmetic — not these source payloads — was where the cross-environment variation crept in). Both entries correctly avoid promoting the theorem, closing only the payload-conversion branch of v13.520's gate list.

## 3. v13.534 (complexified lift group, D8 quotient) — exhaustively verified by group closure

Built the actual 3×3 matrices `A`, `B=R_X` and generated the full group by closure rather than trusting the stated presentation:

- `|G_lift|=16`: confirmed.
- Element-order census `1¹, 2⁷, 4⁸`: confirmed exactly.
- `[B,A]=H=R_XS_T`, `BAB=AH`: confirmed by direct matrix computation.
- Center `{I,R_Y,H,-I}≅C2²`: confirmed — all four expected elements found, center size exactly 4.
- Quotient `G_lift/⟨-I⟩`: confirmed order 8, order census `{1,2⁵,4²}` (matching D8 exactly), and the dihedral relation `B̄ĀB̄=Ā⁻¹` confirmed directly.

No error found.

## 4. v13.535 (D8 matrix intertwiners and obstruction) — verified exactly

Independently verified `R²=D₁₁`, `F²=I`, `FRF=R⁻¹` (the A3-transverse D8), the explicit intertwiner `P=[[1,-1],[1,1]]` satisfying `PJ=JP` and `PCP⁻¹=F⊥`, and the central obstruction argument itself: `J²=-I₂≠diag(1,-1)=C`, confirmed directly. This entry correctly identifies and reports a genuine structural obstruction (no single D8 intertwiner can send `A↦J` and `R_Y↦C` simultaneously) rather than forcing an identification — good, self-critical mathematics.

## 5. v13.536 (split-quaternion Clifford container) — **two errors found**

### 5.1 Determinant sign error

§1 claims, for `Q(X,Y,T)=T e3+X e2+Y e1=[[T,X+Y],[X-Y,-T]]`, that `det Q = X²-Y²-T²`. Direct computation (symbolic and numeric, e.g. `X,Y,T=2,3,5` gives `det Q=-20`) gives
\[
\det Q = -T^2-X^2+Y^2 = Y^2-X^2-T^2,
\]
**not** `X²-Y²-T²` (numeric check: claimed formula gives `-30`, actual determinant is `-20`). Consequently the entry's claim that "the complexified coefficient `Y↦iY`" recovers the target form `X²+Y²-T²` is also affected: applying `Y↦iY` to the *actual* determinant `Y²-X²-T²` gives `-Y²-X²-T²` (wrong sign entirely), whereas applying `X↦iX` gives `Y²+X²-T²=X²+Y²-T²` (correct). So both the stated determinant and the stated complexification axis are backwards.

### 5.2 Consequence, and why it doesn't propagate

This error is self-contained to v13.536 §1's illustrative Clifford-algebra framing. It does not affect any matrix computation in v13.534 or v13.535, which work directly in `(X,Y,T)` coordinates with the matrices `A`, `R_X`, `R_Y`, `J` — all independently verified above without reference to this determinant identity. **v13.537 (below), created independently after v13.536, uses a different and correctly-computed `Q` matrix**, effectively superseding this construction without explicitly flagging the earlier error.

## 6. v13.537 (split-matrix congruences and combined C4×S4) — verified, with one precise non-propagating imprecision

Uses `Q(X,Y,T)=[[T+X,Y],[Y,T-X]]`; confirmed `det Q=T²-X²-Y²` symbolically — correct this time. Verified all four congruence claims directly: `EQE=Q(-X,Y,T)`, `HQH=Q(X,-Y,T)`, `DQD=Q(-T,iY,-X)` (with `D=diag(i,1)`), and `UQUᵀ=Q(-Y,X,T)` (with `U` the `π/4` rotation matrix) — all confirmed exactly.

**One imprecision found:** the entry states `D²=H`. Direct computation: `D²=diag(-1,1)`, `H=diag(1,-1)` — these are **not equal** as matrices. However, the entry's actual conclusion (`A²=R_Y`) does not depend on this specific equality: I verified directly that applying the `D`-congruence twice (`D(DQD)D`) still gives `Q(X,-Y,T)=R_Y(Q)` exactly, because congruence by any diagonal matrix `diag(a,d)` with `ad=-1` produces the same effect on `Q` regardless of which of `a,d` is `-1` — `D²=diag(-1,1)` and `H=diag(1,-1)` both have that property. So the stated intermediate identity is false, but the final claim it was used to justify is independently true. Flagged for precision; does not weaken §5's conclusion.

**The large finite-group claim was independently verified by full computational closure**, not accepted from the stated presentation:

- `G=⟨A,R_X,R_Y,J⟩`: confirmed `|G|=96` exactly.
- Element-order census `1¹,2¹⁹,3⁸,4⁴⁴,6⁸,12¹⁶`: confirmed exactly, matching the ledger's stated distribution digit-for-digit.
- Center `{I,iI,-I,-iI}≅C4`: confirmed.
- `det:G→μ4` image `{1,i,-1,-i}`: confirmed. `ker(det)` has order 24 with order census `1¹,2⁹,3⁸,4⁶` — exactly the known order-type distribution of `S4`.
- `ker(det)∩Z(G)={I}` and `|ker(det)|·|Z(G)|=24·4=96=|G|`: confirmed, consistent with the claimed internal direct product `G≅C4×S4`.

The order-census match to `S4` is strong but not by itself a full isomorphism proof (no explicit generator-relation check was performed beyond order distribution); flagged as very likely correct but slightly short of the airtight standard applied elsewhere, consistent with the entry's own "exploratory" labeling.

---

## 7. Summary

| Entry | Verdict |
|---|---|
| v13.532 | Re-executed, confirmed exact |
| v13.533 | Re-executed, confirmed exact, SHA-256 hashes match |
| v13.534 | Exhaustively verified by group closure |
| v13.535 | Verified exactly, including the genuine obstruction |
| v13.536 | **Two errors**: determinant sign wrong, complexification axis wrong (X should be complexified, not Y); contained, does not propagate |
| v13.537 | Verified; one non-propagating imprecision (`D²≠H` as written); `|G|=96≅C4×S4` confirmed by full computational closure |
| v13.538 (ex-v13.530) | Previously verified in Round 44 |

## Guardrail

No RH, GRH, Suzuki-spectral, or critical-line consequence follows from anything in this round; all entries correctly self-limit to exact finite/representation-theoretic algebra. Certified Suzuki status unchanged: `ind_{<=0}(A_even(1))<=4`, `ind_{<=0}(A_{a=1})<=6`.
