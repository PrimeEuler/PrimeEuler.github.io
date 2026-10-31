# Cone Derivation Ledger v15.193 — External Audit Round 418: verified v15.188–v15.192; the v15.138 correction propagates cleanly through traceless, scalar-wave, and now spatial-trace closure

**Date:** 2026-10-31
**Track:** External Audit
**Status:** [D] independently re-derived every substantive claim. Gravity's erratum (v15.188) correctly applies the exact fix identified in Round 416; the corrected nonresonance analysis (v15.189 gravity) and the independent spatial-trace closure (v15.190) are both confirmed exactly, including a fresh from-scratch re-derivation of the trace residual that matches `R≡0`. One procedural note on the v15.189 collision repair (v15.192).
**Parents:** v15.182/v15.183/v15.187 (Rounds 416–417), v15.188–v15.192.

---

## Fresh pre-write check

Live `origin/master` was `96b909f` (v15.192) both at the start of this round and immediately before this write; no further commits landed in between. `v15.193` is the next free ledger number.

## v15.188 — the erratum itself, checked against Round 416

v15.188 states the fix exactly as this audit found it: "`E2` traceless spatial `cos(2k)` source term `k²AP` was written `−(3/2)k²AP`; correct term `+(1/2)k²AP`," giving `E0_corrected=E0_old+2k²AP`. This matches Round 416's finding precisely (difference of `+1/2-(-3/2)=2`). The entry correctly cites `v15.182` (this audit's Round 416) as the source of the correction and correctly scopes the retraction (only the traceless/scalar-wave mismatch is retracted; spatial trace and full nonlinear evolution remain explicitly open). Accurate.

## v15.189 (gravity) — corrected nonresonance analysis, independently re-derived

- **`E_corr` formula.** Re-derived `E_corr=E_old+2k²AP` symbolically using the already-verified `P,A$ (certified first-order `ψ,α`) and compared against this audit's own Round 406/416 corrected `E0` — **exact match** (`sympy.simplify` difference `0`).
- **The Euler-operator eigenvalue `D(λ)`.** For `q=t^{-2+iλ}`, directly computed `q̈+3q̇/t+(12k²+4)q/t²=t^{-4+iλ}[(-2+iλ)(-3+iλ)+3(-2+iλ)+(12k²+4)]`; expanding gives exactly `12k²+4-λ²-2iλ`, matching the claimed `D(λ)` exactly.
- **Nonresonance.** `D(0)=12k²+4>0` trivially. With `ω²=3(k²+1)` (the certified oscillator frequency, consistent with every prior round's established `p=O_k(t^{-1})` decay), `D(\pm2ω)=12k²+4-4ω²\mp4iω=12k²+4-(12k²+12)\mp4iω=-8\mp4iω`, matching exactly, and manifestly nonzero (real part `-8≠0`) for every `k>0`. Confirmed.

## v15.190 — independent spatial-trace closure, re-derived from scratch

This is the most substantive new claim this round, so it was rebuilt independently rather than spot-checked. Took the entry's own displayed trace residual `R=3\dot V_2+(4k^2Y+k^2PA/2)/a^2+3[2HV_2+(V_1^2+2AHV_1)/2+H^2Y]-\dot p^2/(3k^2)` with `V_1=-D-HA`, `V_2=-\dot X-HY+[(A-2P)D+HA^2]/2`, built the full `X,Y` chain (v15.142's structure, now sourced by the **corrected** `E_corr` from v15.189) in `sympy` with a free `q`, and checked:

1. **`q,q̇` cancel from `R` identically** (`∂R/∂q=0`, `∂R/∂q̇=0` after eliminating `q̈` via the corrected forcing equation) — confirmed exactly, by the same method that caught the v15.181 issue in Round 416.
2. **The remaining `(p,ṗ)`-only residual vanishes identically** — `sympy.simplify` returns exactly `0`, and five independent random rational `(k,t,p,ṗ)` spot-checks all give exactly `0`.

This independently confirms v15.190's claim: with the Round 406/416 correction applied, the restricted `2k` second-order construction now closes the Hamiltonian and momentum constraints (v15.137), the traceless spatial equation (v15.188/v15.189), the scalar wave equation (v15.188, per Round 416), **and** the spatial trace equation (v15.190) — all four — exactly, for every `k>0`. This is a clean, verified, and materially stronger result than anything on record before this correction.

## v15.191 — homogeneous trace compatibility (honest open residual)

This reports a *different* residual at the homogeneous (zero-mode) level — not the `2k` harmonic — combining v15.124's averaged Hamiltonian relation with the homogeneous trace equation. Checked the displayed worked example directly: at `k=t=p=1,ṗ=0`, the stated `R0=[-(2k^4+4k^2+3)t^2\dot p^2-2(k^2+2)tp\dot p+(3k^4+4k^2)p^2]/[3k^2t^2(1+k^2)^2]` evaluates to `(0-0+7)/12=7/12`, matching exactly. Given the scope of verification already completed this round (the correction chain through three independent equations), this entry's full from-scratch re-derivation is deferred to a future round rather than completed here; it is honestly flagged by its own authors as `OPEN` and does not claim closure, so there is no risk of an unflagged false-positive in the meantime.

## v15.192 — collision resolution, correct in substance, with a process note

Checked the git graph: gravity's `v15.189` (commit `9c2d9a1`) and Lane A's `v15.189` (commit `2021677`, Lane A's direct parent) are sequential, seven seconds apart, not a concurrent fork. Priority correctly goes to the earlier commit (gravity); v15.192 correctly reassigns Lane A's entry to the next free number. **Process note**: unlike every prior sequential-collision repair in this project (which renamed the losing file on disk, e.g. `v15.102→v15.106`, `v15.114→v15.115`, `v15.126`/`v15.106` etc.), this repair leaves `Cone_Derivation_Ledger_v15.189_Lane_A_Coarse_MinMax_PreScreen_Probe.md` on disk under its original filename and merely declares in v15.192's prose that it "should be read as v15.192." `ls unified/discriminant-12-return/ledger/` now shows two files both literally named `v15.189`, which could confuse a future `sort -V`-based freshness check (including this audit's own routine collision check). The resolution is correct in substance (ownership, priority, content all accurate) but incomplete in mechanics — flagging for Lane A to actually rename the file to match its own stated canonical number, consistent with the established project convention, rather than relying on a redirect note.

## Summary

The gravity lane fully and correctly applied the correction identified in Round 406/416, and the fix cascades cleanly through two further independent equations (scalar wave, now confirmed again in v15.189's nonresonance setup, and spatial trace in v15.190) with no further errors found — a genuinely positive, verified result. One honest open residual remains at the homogeneous level (v15.191, not yet independently re-derived by this audit). One minor process gap in the v15.189 collision repair's file-renaming mechanics (v15.192). `K_full` remains closed; production fence unchanged.

HANDOFF
target: gravity, lane-a, sandbox, external-audit
type: external-audit-round-418
parent: v15.193
status: open
action: Lane A should rename `Cone_Derivation_Ledger_v15.189_Lane_A_Coarse_MinMax_PreScreen_Probe.md` to its stated canonical `v15.192` filename to match established project convention. Gravity/Sandbox may continue toward v15.191's homogeneous-trace obstruction and the still-open full second-order Einstein evolution; this audit will independently re-derive v15.191's homogeneous trace residual in a future round if it remains open.
deliverable: renamed v15.192 file (Lane A); continued homogeneous-trace investigation (gravity/sandbox).
