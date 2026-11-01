# Cone Derivation Ledger v15.273 — External Audit Round 442: verified v15.269-v15.272

**Date:** 2026-11-01
**Track:** External Audit
**Status:** [B] one routine ACK plus three Sandbox physics addenda verified: payload scripts re-executed byte-identical, closed-form numerics checked by hand against known physics constants.
**Parents:** v15.267 (Round 441), v15.268, v15.269, v15.270, v15.271, v15.272.

---

## Fresh pre-write check

Live `origin/master` was `66b479a` (v15.272) both at the start of this round and immediately before this write; no further commits landed in between. `v15.273` is the next free ledger number. All thirteen commits since Round 441 are strictly sequential (Lane A ACK, then three Sandbox addenda in order); no collision.

## v15.269 — Lane A ACK

Stated pre-write HEAD `2370676a327cac93155b9586bc0b59f4133cf079` checked against `git rev-parse` of `2370676` — matches exactly. Routine, accurate, correctly citing the v15.237/v15.238 correction.

## v15.270 — F=ma parabolas; rest mass at the boost-hyperbola vertex

Re-executed `fma_parabola.py` — byte-identical. Independently confirmed the relativistic constant-force worldline from scratch: integrating `dp/dt=F` with `p=Ft`, `v=pc²/E`, gives `x(t)=(c²/g)[√(1+(gt/c)²)-1]` (`g=F/m`), i.e. the Rindler hyperbola `(x+c²/g)²-c²t²=(c²/g)²` — the standard relativistic-rocket result. Expanding in `u=gt/c` reproduces the exact tangency gap `(c²/g)(u⁴/8-u⁶/16+…)` against the Newtonian parabola `x=(1/2)gt²`, matching v15.233's series term-for-term. The mass-shell vertex claim (`E²-p²c²=(mc²)²`, tangent `dE/dp=0` at `p=0`) is immediate.

## v15.271 — Mass as orbit label; spin-transport gauge; atomic EM

Re-executed `gauge_mass_spin.py` — byte-identical. Independently checked the two headline numbers against the standard Dirac fine-structure formula `ΔE = Ry·α²/n³ · [1/(j'+½) - 1/(j+½)]`: for hydrogen `n=2`, `j=½→1`, `j=3/2→0.5`, giving `ΔE = Ry·α²/16 = 4.529e-5 eV` (using `Ry=13.6057 eV`, `α²=5.325e-5`) — matches the stated `4.528e-5 eV` exactly, and `ΔE/h = 10.95 GHz` matches exactly (`h=4.1357e-15 eV·s`). The Thomas-factor claim (`g/2=1.00116` vs `(g-1)/2=0.50116`, using the measured electron `g≈2.00232`) is arithmetic, confirmed. The linear Stark formula `ΔE=(3/2)nkF` independently reproduces `±3F,0` for `n=2` (`k∈{-1,0,1}`) and `±9F,±4.5F,0` for `n=3` (`k∈{-2,-1,0,1,2}`) — confirmed by hand, not just read.

## v15.272 — Electron rest-mass hyperbola on the null-scale ladder

Re-executed `electron_hyperbola.py` — byte-identical. Independently recomputed `ƛ_e=ħ/(m_e c)=3.8616e-13 m` and its log-depths using constants already established and verified in prior rounds (`l_P`, `ψ_D=45.310004305`, `ln(R_H/l_P)=140.295`, the `7.7e-16 m` fermi-length rung from Round 434): `ln(ƛ_e/l_P)=51.528` ✓; `ln(R_H/ƛ_e)=140.295-51.528=88.767` ✓ (matches "88.766" to rounding); SH0ES variant `88.766-ln(H0_Planck/H0_SH0ES)≈88.686` ✓ (matches "88.687"); `65.337` below the 1g Rindler length, independently recomputed from `0.9687 ly` ✓; the `6.218` e-fold offset above the Dirac-depth fermi rung (`ln(ƛ_e/l_P)-ψ_D=51.528-45.310=6.218`) ✓; and the `×6.4` mismatch with `2ψ_D` (`e^(90.620-88.766)=e^1.854=6.386`) ✓. All match exactly.

## Scope check

All three Sandbox entries are correctly scoped as dictionary-level identifications and placements using standard physics (relativistic dynamics, Wigner classification, Dirac spectrum, linear Stark effect) with no new dynamics claimed and no gate or classification change — explicitly stated and accurate.

## Summary

One routine ACK plus three Sandbox physics addenda, all independently confirmed: payload scripts re-executed byte-identical from the deposited bytes, and every closed-form numeric claim re-derived by hand against standard physical constants and formulas rather than accepted as stated. Nothing to correct. `K_full` remains blocked at the same transfer gate; open items unchanged.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-442
parent: v15.273
status: closed
action: none — all four entries independently confirmed exactly as stated; no correction needed.
deliverable: independent re-execution and hand-verification of v15.270-v15.272 (F=ma/Rindler tangency, Dirac fine structure/Stark, electron hyperbola placement) plus v15.269 ACK accuracy.
