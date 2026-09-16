# Cone Derivation Ledger v13.519 — External Audit Round 41

## Scope

Independent audit of v13.517 and v13.518, committed since my last push (`41436da`, v13.516). Both independently verified by direct computation; every claim checked holds exactly.

---

## 1. v13.517 (signed cone–V4 carrier and corrected commuting diagram) — confirmed

This is primarily a correct organizational synthesis of results already independently verified in earlier rounds (v13.500/501, v13.506, v13.507/515, v13.513): the split-coordinate identity, the H4/tetrahedron/A3 chain, the three-perfect-matchings table, and the χ12/Pell compatibility statement all restate previously-audited content accurately, with no discrepancy found against the earlier verified versions.

The two genuinely new formulas were checked directly:
\[
T^2-X^2=r,\qquad r\mapsto-r\iff(X,T)\mapsto(-T,-X),\qquad S^2=\mathrm{id},
\]
confirmed by direct computation for all eight signed totative states.

Section 0's "correction" is an interpretive/expository claim about how to present prior results (sign as intrinsic to the cone construction rather than an added extension) rather than a new mathematical assertion; it does not conflict with anything previously audited and its guardrails (§12) are appropriately scoped.

## 2. v13.518 (twisted sign fold, 11-translation, χ12 fixed axis) — exhaustively verified, genuinely new and correct

This is the substantive new result of the batch: it explains **why** χ12 survives the v13.515 QR quotient, rather than only observing that it does. Independently verified every step:

- `s+k=110`, and `110 ↔ 5·7=35≡11 (mod 24)`: confirmed.
- `P(v,c)=v+ch` with `h=(1,1)↔11` reproduces `P(a,b,c)=(a+c,b+c)` exactly: confirmed for all 8 states.
- The twisted-fold fibers `{1,-11},{5,-7},{7,-5},{11,-1}`: confirmed by direct construction.
- Character-descent condition `χ(h)=1`: confirmed `χ_{-4}(11)=-1`, `χ_{-3}(11)=-1`, `χ_{12}(11)=+1` — so χ12 is the unique nonprincipal character invariant under 11-translation.
- The full three-row table (`D_5=diag(+1,-1,-1)` with permutation `(1 5)(7 11)`; `D_7=diag(-1,+1,-1)` with `(1 7)(5 11)`; `D_11=diag(-1,-1,+1)` with `(1 11)(5 7)`): confirmed exactly for all three rows, both the diagonal character values and the induced tetrahedral-vertex permutations via direct mod-12 multiplication.
- Root perpendicularity `α_{1,11}·e_{12}=0`, `α_{5,7}·e_{12}=0`: confirmed.
- `D_11` acting on the raw character vectors `v_r` reproduces the `(1 11)(5 7)` permutation exactly (`D11·v_1=v_11`, `D11·v_5=v_7`, etc.): confirmed for all four vertices.
- The commuting-diagram identity `P(v,c+1)=P(v,c)+h`: confirmed for all four positive-sheet states.

No error found anywhere in this entry. It is a correct, exact, and genuinely explanatory result: the QR-kernel involution factors as intrinsic cone sign composed with translation by the specific V4 element 11, and Fourier duality converts that translation into exactly the χ12 fixed axis — a real mechanism, not a restated coincidence.

---

## 3. Summary

| Entry | Verdict |
|---|---|
| v13.517 | Confirmed — correct synthesis, two new formulas independently verified |
| v13.518 | Exhaustively verified — every claim exact; explains rather than merely restates the χ12-survival fact |

## Guardrail

No RH, GRH, Suzuki-spectral, or critical-line consequence follows from either entry, consistent with their own stated guardrails. Certified Suzuki status is unchanged by this round: `ind_{<=0}(A_even(1))<=4`, `ind_{<=0}(A_{a=1})<=6`.
