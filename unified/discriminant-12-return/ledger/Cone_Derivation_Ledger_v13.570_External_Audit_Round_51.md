# Cone Derivation Ledger v13.570 — External Audit Round 51

## Scope

Independent audit of everything committed since my last push (`9da1944`, Round 50): three new entries continuing the V4/J-compatibility classification from v13.562/v13.563, plus the next M16001 outward-certification specification checkpoint. One version collision found and fixed (the new work landed in the v13.566 slot my own Round 50 entry had just taken). Every claim independently re-derived by hand or by direct computation. Everything checks out; no errors found this round.

---

## 1. Housekeeping

`Cone_Derivation_Ledger_v13.566_Orientation_Selects_SigmaB.md` (commit `c49870b`, 2026-09-17 16:57:47 -0400 = 20:57:47 UTC) collided with my own `Cone_Derivation_Ledger_v13.566_External_Audit_Round_50.md` (commit `9da1944`, 20:56:50 UTC — 57 seconds earlier). Renumbered the colliding file to **v13.569**, and fixed its two inbound cross-references in `Cone_Derivation_Ledger_v13.567_Cyclotomic_i_Selects_Sigma_A_Not_Sigma_B.md` (lines referring to "the cyclic-order selection from v13.566" and "orientation from v13.566").

## 2. v13.569 (ex-v13.566, cyclic-order orientation selects sigma_B) — verified exactly

This tests which of the two v13.563 J-compatible automorphisms (`sigma_A=(7 11)`, `sigma_B=(5 11 7)`) preserves the orientation of the v13.560 six-cyclic-order labeling. Independently applied both permutations entrywise to all six labeled cyclic orders

`a=[1,5,11,7], b=[1,7,11,5], c=[1,11,5,7], d=[1,7,5,11], e=[1,5,7,11], f=[1,11,7,5]`

by hand:

- `sigma_A` (swap 7,11, fix 1,5): `a→[1,5,7,11]=e`, `b→[1,11,7,5]=f`, `c→[1,7,5,11]=d`, confirming `(a e)(b f)(c d)` exactly. As a permutation of `{1,5,7,11}` this is one transposition, sign `-1` — confirmed.
- `sigma_B` (5→11→7→5 cycle): `a→[1,11,7,5]=f`, `f→[1,7,5,11]=d`, `d→[1,5,11,7]=a`, confirming `(a f d)`; and `b→[1,5,7,11]=e`, `e→[1,11,5,7]=c`, `c→[1,7,11,5]=b`, confirming `(b e c)`. Together `(a f d)(b e c)` exactly. This is a 3-cycle on `{1,5,7,11}`, sign `+1` — confirmed.

Both permutation actions and both signs match the ledger exactly.

## 3. v13.567 (cyclotomic i selects sigma_A, not sigma_B) — verified exactly

Independently recomputed `sigma_r(i)=i^r` for `i=zeta_12^3` and `r in {1,5,7,11}`: `i^1=i, i^5=i^4·i=i, i^7=i^4·i^3=-i, i^11=i^8·i^3=-i`, giving the character row `chi_{-4}=(+1,+1,-1,-1)` — this is exactly the standard `chi_{-4}` (determined by `r mod 4`: `1,5≡1 mod4 → +1`; `7,11≡3 mod4 → -1`), confirmed independently rather than taken on the ledger's assertion.

- `chi_{-4}∘sigma_A`: since `sigma_A` only swaps `7↔11`, and `chi_{-4}(7)=chi_{-4}(11)=-1` are equal, the composed row is unchanged: `(+,+,-,-)=chi_{-4}` exactly, confirmed.
- `chi_{-4}∘sigma_B`: `sigma_B` sends `5→11,7→5,11→7`. Row becomes `(chi_{-4}(1),chi_{-4}(11),chi_{-4}(5),chi_{-4}(7))=(+,-,+,-)`. Independently confirmed this equals the standard `chi_{-3}` (determined by `r mod 3`: `1,7≡1 mod3→+1`; `5,11≡2 mod3→-1`), i.e. `chi_{-4}∘sigma_B=chi_{-3}≠chi_{-4}` exactly as claimed.

So the two independent selection criteria (v13.569's cyclic-order-orientation vs. this entry's cyclotomic-character-preservation) genuinely disagree — `sigma_B` vs `sigma_A` — and the entry correctly reports this as a new obstruction rather than glossing over it or silently picking a side.

## 4. v13.568 (M16001 remote-row and pre-Gram certificate spec) — architecture verified, formulas re-derived

Explicitly self-labeled as a specification checkpoint with no new numerical closure; checked accordingly.

Independently re-derived the central pre-Gram error-propagation formula by hand from the bilinear perturbation `(R̂+δ)ᵢ(R̂+δ)ⱼ`:

`G_ij - Ĝ_ij = Σ_n [R̂_ni δ_nj + δ_ni R̂_nj + δ_ni δ_nj]`, bounded entrywise by `Σ_n[|R̂_ni|ρ_nj + ρ_ni|R̂_nj| + ρ_niρ_nj]`,

which matches the stated `E_preGram = |R̂|^T ρ_R + ρ_R^T |R̂| + ρ_R^T ρ_R` exactly (this is the same formula independently re-derived and confirmed against v13.555/DAG in Round 49; this entry now gives it its full production interface).

Also independently re-derived the two- and three-uncertain-factor product error bounds in section 3 by direct expansion of `(x̂+δx)(ŷ+δy)` and `(x̂+δx)(ŷ+δy)(ẑ+δz)` minus their nominal products — both match the stated `rho_xy` and `rho_xyz` bounds exactly, term for term.

The "closed/frozen by specification" vs. "still open numerically" status lists are internally consistent with each other and with the stated scope (no inertia promotion, gate unchanged at `a_N^L - (||B_QN||_2^U)^2/lambda_Q^L > 0`).

---

## 5. Summary

| Entry | Verdict |
|---|---|
| v13.569 (ex-v13.566, orientation selects sigma_B) | Verified exactly — all six cyclic-order permutation actions and both signs confirmed by hand |
| v13.567 (cyclotomic i selects sigma_A) | Verified exactly — independently recomputed both character compositions |
| v13.568 (M16001 remote-row/pre-Gram spec) | Architecture sound; central error-propagation formulas independently re-derived and confirmed exactly |

## Guardrail

No RH, GRH, or critical-line consequence follows from anything this round. Certified Suzuki status unchanged: `ind_{<=0}(A_even(1))<=4`, `ind_{<=0}(A_{a=1})<=6`. The v13.567/v13.569 disagreement (cyclic-order orientation selects `sigma_B`, cyclotomic character selects `sigma_A`) is a genuine open obstruction, correctly reported as such rather than resolved by fiat.
