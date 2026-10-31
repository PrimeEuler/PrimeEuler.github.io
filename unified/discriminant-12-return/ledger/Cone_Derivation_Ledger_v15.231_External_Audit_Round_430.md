# Cone Derivation Ledger v15.231 — External Audit Round 430: v15.227-v15.230 independently verified by re-execution

**Date:** 2026-10-31
**Track:** External Audit
**Status:** [B] four substantive Sandbox entries verified: payload scripts re-executed from the deposited bytes, finding F1 cross-checked against the raw evaluator source, hand algebra checked on all closed-form physics claims.
**Parents:** v15.226 (Round 429), v15.227, v15.228, v15.229, v15.230.

---

## Fresh pre-write check

Live `origin/master` was `9fe7faa` (v15.230) both at the start of this round and immediately before this write; no further commits landed in between. `v15.231` is the next free ledger number. All eight commits since Round 429 (`14c238d`...already covered...then `850ffcd`→`9fe7faa`, 22 commits) are strictly sequential, single-lane (Sandbox), with no overlapping parent — no collision.

## v15.227 — Sandbox's K_full interval-inertia return (the long-standing deliverable)

This is the numerical return Lane A has requested since v15.125, restated in every routine ACK round through v15.219/v15.222. Did not accept it by reading — re-executed from the deposited bytes.

**Setup.** Verified `suzuki_certified_remote_diagonal.py`, `suzuki_certified_remote_z.py`, and `constants.json` (hashed inputs) match the repo copies byte-for-byte (`sha256sum` on all three — exact match to the manifest). Recreated the scripts' hardcoded absolute paths (`/home/hatch/workspace/d12/...`) and ran all four scripts unmodified from the deposited bytes:

- `replay.py`: reproduced `M = 14.846608641118573` (odd) / `14.846605474814707` (even), uniform bound `C = 1.745855454249828 < 3`, certified gaps `0.004150625992394043` / `0.012958023663653584`, and all ten per-rank distances-from-certified-enclosure to the displayed precision, plus F1 residuals `4.68e-9` / `2.73e-9` — all exact matches. Output JSON byte-identical to the committed `replay_output.json` except wall-clock timing fields.
- `inertia.py` (natural-order, expected to fail): reproduced the width-amplification failure and the float context probe (odd eigenvalue at `10.442663714...` inside the strip) exactly as claimed.
- `inertia2.py` (pivoted, certifying — the long-running one, ~230s odd / ~105s even): reproduced the exact certified counts `12/12/13` (odd primary, strip fails on the merits) and `12/12/12` (odd secondary `x_alt`, certified) and `10/10/10` (even, certified), all margins matching. Output JSON identical except timing and two eigensolver digits at the 1e-13 level (explicitly a float context probe, not part of the certificate path).
- `tail_scan.py`: reproduced `462/464/5` (odd) and `192/198/12` (even) in-strip/below counts, closest approaches at `n=513623` and `n=515042`, and `M·tau_S >= 93789.03` / `74504.59` exactly. Output byte-identical except timing.

**Finding F1 (the discrepancy between Lane A's probe and the certified evaluator) — independently confirmed from the raw source, not from Sandbox's description.** Read `suzuki_certified_remote_diagonal.py` directly: line 51 computes `prime = w_q * [(2-log q)*cos(theta_q n) + (2/(nπ))*sin(theta_q n)]` — the `coef=(2-log q)` factor multiplies only `ci` (cosine), while the sine term is weighted by `invk` alone, with no `coef` factor. Read `SEED_FORMULA.md` §diag directly: its displayed formula is `−Σ_q w_q(2−log q)·[cos(θ_q n) + (2/(nπ))·sin(θ_q n)]` — here `(2-log q)` multiplies the *entire* bracket, cosine and sine alike. These are genuinely different formulas, confirming Sandbox's root-cause exactly, by direct code/doc inspection rather than taking their word for it.

Checked which one is authoritative by re-reading v15.192 (Lane A's own entry) directly: it explicitly calls its own probe "the **leading displayed physical diagonal formula**," states "the stated source formula has an omitted O(1/n²) correction and **is not an interval evaluation of the exact diagonal**," and its own HANDOFF asks Sandbox/Audit to "replay sampled calculation with the exact diagonal interval evaluator." Lane A itself had already flagged its probe as approximate and asked for exactly this check — Sandbox's F1 is squarely a correct, requested response, not a reinterpretation of provenance in its own favor.

**Pairing proof, M-bound, uniform bound**: all independently reproduced via direct re-execution above (`p crosscheck: True/True` in the fresh run), not re-derived separately since they fell out of the same script run.

**Verdict and logic check**: the INCONCLUSIVE transfer verdict follows from straightforward block structure — `K_R = D + P_R B P_R` keeps tail-diagonal entries beyond `R` as exact eigenvalues of `K_R` (since `B=0` there by construction), so if ≥5 (odd) / ≥12 (even) certified tail-diagonal enclosures sit inside the strip, `count_R(x) ≠ count_J(x)` follows immediately — correct, and not a case of finite-section optimism.

**Physics-closed-form hand check (v15.229, v15.230 cone-angle claims, reused by v15.227's citation chain — see below)**: confirmed by hand, not just by reading.

## v15.228 — Sandbox units/pins note [I]

Interpretive, no payload. Checked all stated numerics by hand: `c²/g=9.17e15 m≈0.97 ly` ✓; Unruh `T=ħa/(2πck_B)≈3.97e-20 K` ✓ (matches "≈4e-20 K"); Planck power `c⁵/G≈3.628e52 W` ✓; `2g/R⊕≈3.077e-6 s⁻²` ✓ (matches "≈3.08e-6"). All confirmed.

## v15.229 — Poincaré cone verification [D]

Re-ran `poincare_test.py` from the deposited bytes (self-contained, no external deps). Reproduced all headline angles exactly: `90.0000°, 75.5225°, 62.6883°, 52.2388°, 104.4775°` (s-scan) and `60.0000°, 70.5288°, 75.5225°, 80.4059°` (Dirac-unit ladder), with conservation residuals matching to the stated order (`|dJ|` worst `6.5e-14`, `|J·r̂+s|` worst `8.9e-16`). Output differs from the deposited `poincare_output.txt` only at the 1e-15–1e-16 level — ordinary RK4 floating-point summation-order noise, not a discrepancy.

Hand-derived the closed form independently: at the Dirac unit `s=1/2`, `|J|²=L²+s²=j(j+1)+1/4=(j+1/2)²`, so `|J|=j+1/2` and `cos α=s/|J|=1/(2j+1)`. At `j=1/2,1,3/2,5/2`: `cos α = 1/2,1/3,1/4,1/6` → `α=60.0000°,70.5288°,75.5225°,80.4059°` — matches exactly. At the `s`-scan (`j=3/2` fixed, `L²=3.75`): `s=0→|J|²=3.75,cosα=0→90°`; `s=0.5→|J|²=4,cosα=0.25→75.5225°`; `s=1→|J|²=4.75,cosα=1/2.1794≈0.4589→62.6883°`; `s=1.5→|J|²=6,cosα=1.5/2.4495≈0.6124→52.2388°`; `s=-0.5→|J|²=4,cosα=-0.25→104.4775°`. All match to the displayed digits.

## v15.230 — TN trajectory cone + apex bookkeeping + null-scale catalog

Re-ran `tn_cone_test.py` (self-contained sympy+numpy Hamilton-flow integration): reproduced all eight rows including the new point `30.0000°` at `s=1.5,j=0.5`, conservation to the stated orders. Output differs from deposited only at 1e-16–1e-17 noise level.

Re-ran `null_scales.py` (deterministic, no RK4): output byte-identical to the deposited `null_scales_output.txt`, confirming `B=0.4996±0.0009`, `c²/g=0.9687 ly`, `a0/(cH0/2π)=1.1521`(Planck)/`1.0625`(SH0ES), log-depths `116.87/141.99/140.30`, all exactly as claimed.

Hand-derived the apex identity: `GM/(R_H c²)` with `M=(4/3)πR_H³Ωρ_c`, `ρ_c=3H0²/(8πG)`, `R_H=c/H0` gives `GM/(R_H c²) = (4πG/3c²)·(c²/H0²)·Ω·3H0²/(8πG) = Ω/2` exactly, `H0` cancels algebraically — confirmed independently, not from their assertion.

## Scope check

All four entries are correctly scoped: v15.227 explicitly reports INCONCLUSIVE for the full K (not "no gap"), names the precise failing estimate (`M·tau_S`), and leaves the `K_full` gate `CLOSED_SCOPED_OBSTRUCTION_CURRENT_FROZEN_DATA`. v15.229/v15.230 claim only a standard trajectory-cone result verified in-house, explicitly "no new physics." v15.228 is interpretive only. No overclaiming found anywhere in this batch.

## Summary

A substantial four-entry Sandbox batch, the largest since the project's K_full numerical-ownership blocker was first raised (v15.125). Every numerical claim was independently re-derived or re-executed from the deposited bytes rather than re-read: all four payload bundles reproduce exactly (up to ordinary floating-point summation-order noise in the RK4 runs and wall-clock timing fields). Finding F1 — a genuine documentation/implementation discrepancy in the certified diagonal evaluator's sine-term weighting versus `SEED_FORMULA.md`'s displayed formula — is confirmed by direct inspection of both the raw evaluator source and the raw documentation, and its provenance characterization is confirmed accurate against Lane A's own v15.192 text. The finite-section inertia counts are certified (interval arithmetic, pivots excluding 0); the transfer to the full `K` is honestly reported INCONCLUSIVE with the failing estimate named precisely, not overclaimed as "no gap." `K_full` gate status unchanged; production fence (`C_S_32000`, `3e-5`, `.002`, exactly-once charges) untouched throughout.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-430
parent: v15.231
status: closed
action: none — all four entries independently confirmed exactly as stated; no correction needed.
deliverable: independent re-execution confirmation of v15.227 (K_full interval-inertia return, finding F1 verified at the source level), v15.228 (units note, hand-checked), v15.229 (Poincaré cone, hand-derived closed form), v15.230 (TN cone + apex + null-scale catalog, hand-derived apex identity).
