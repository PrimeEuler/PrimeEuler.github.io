# Cone Derivation Ledger v15.236 — External Audit Round 431: v15.232-v15.235 independently verified

**Date:** 2026-11-01
**Track:** External Audit
**Status:** [B] one Lane A freeze/ACK and three Sandbox geometric addenda verified; all checks pass.
**Parents:** v15.231 (Round 430), v15.232, v15.233, v15.234, v15.235.

---

## Fresh pre-write check

Live `origin/master` was `0ed6580` (v15.235) both at the start of this round and immediately before this write; no further commits landed in between. `v15.236` is the next free ledger number. All fifteen commits since Round 430 are strictly sequential (Lane A then Sandbox, in order); no collision.

## v15.232 — Lane A's ACK/freeze of v15.227 and v15.231

Verified the frozen GitHub blob SHAs independently via `git hash-object` on the actual repo files, not by trusting the ACK's table: `MANIFEST.sha256`, `replay_output.json`, `inertia2_output.json`, `tail_scan_output.json`, and `BUILD_LOG.md` all reproduce the exact blob hashes stated (`345528a9...`, `57129f69...`, `4ee4be07...`, `ac862e58...`, `ba0ad8eb...`). The restated numbers (gaps, `M<15`, `C<3`, inertia counts, tail-scan obstruction) match Round 430's own independently-reproduced values exactly. This is an accurate freeze; no correction needed.

## v15.233 — Sandbox: acceleration parabola vs. Dirac depth, crossing range

Re-executed `accel_parabola.py` from the deposited bytes — byte-identical to the committed output. Independently hand-verified every numeric claim (own script, own derivation, not theirs): with `g=9.80665` (confirmed from the script's own constant, not the loose `g=9.8` used informally in v15.228's interpretive note), `ln(a_P/g)=116.8645` ✓, ratio to Dirac depth `2.57924×ψ_D` ✓, `a_P e^{-ψ}=1.1675e32` ✓, Rindler length `l_P e^{ψ}=7.698e-16 m` ✓. Independently derived the three crossing-range claims algebraically:
- parabola×edge: `ξ=u²/2=u ⟹ u=2` ✓ (`t=x=2c/g=1.9374` in matched yr/ly units, confirmed via `c/g` in years ≡ `c²/g` in light-years by construction since `ly=c·yr` in their convention);
- parabola×own Rindler hyperbola: `(u²/2+1)²-(1+u²)=u⁴/4>0` for all `u≠0` ⟹ parabola strictly outside, never crosses — confirmed by direct algebra, not asserted;
- parabola×interval hyperbola `u²-ξ²=σ²`: substituting `ξ=u²/2` gives `u²=2±2√(1-σ²)`, requiring `σ≤1`, grazing at `σ=1` (`u=√2,ξ=1`), none for `σ>1` — confirmed by direct solve, matches exactly.

## v15.234 — Sandbox: parabola in the Rindler frame; grid's view of boost hyperbolas

Re-executed both `rindler_parabola.py` and `boost_grid.py` from the deposited bytes — both byte-identical. Independently re-derived §A's full family result from scratch (not from their formula): with `X=x+c²/g`, Galilean trajectory of acceleration `a` in an observer frame of `g`, set `r=a/g`, `u=gt/c`; derived `ρ²/(c⁴/g²)=(r²/4)u⁴+(r-1)u²+1` and maximized over `u` to get `η_max=arcsinh(1/√(2r-1))` for `r>1/2`. Evaluated this independently-derived closed form at `r=3/4,1,2,4`: `1.1462, 0.8814, 0.5493, 0.3695` — all four match the stated catalog exactly. Also independently confirmed the `a=g` special case (cross term `(r-1)u²` vanishes identically at `r=1`, giving the stated "flat to fourth order") and the `u=√2` fold point (`η_max=ln(1+√2)` exactly) and the `u=1`/`u=2` equal-η coincidence (`g(1)=g(2)=0.8` in the reduction variable, both giving `η=(1/2)ln5`) via direct algebra. §B's AM/GM and confocal-grid claims are standard hyperbolic-parametrization facts, checked structurally.

## v15.235 — Sandbox: opposite-sign parabola pairs, confocal at apex

Re-executed `parabola_pairs.py` — byte-identical. Independently solved the two parabola equations by hand: `Y²=n²-2nX` and `Y²=k²+2kX` subtract to `2X(n+k)=(n-k)(n+k)`, giving `X=(n-k)/2`, then back-substituting gives `Y²=nk` — both match the claimed intersection formula exactly, confirming claims 1–2. For claim 3 (confocal at the apex), rewrote each parabola in standard form: row `Y²=-2n(X-n/2)` has focus at `X=n/2+(-n/2)=0`; column `Y²=2k(X+k/2)` has focus at `X=-k/2+k/2=0` — both independently confirmed to sit at the origin for every `n,k`, confirming the confocal claim exactly, not just trusting the assertion.

## Scope check

All four entries are scoped correctly: v15.232 explicitly freezes only the stated scope and reiterates `FULL_K_TRANSFER = INCONCLUSIVE` (not "no gap"), opens a new HANDOFF for an alternative transfer strategy, and leaves all production-fence thresholds untouched. v15.233–v15.235 are explicitly scoped as grid-geometry/kinematics addenda with "no gate, classification, or selector statement changes" — accurate; nothing here promotes beyond that.

## Summary

One Lane A freeze (blob hashes independently re-verified via `git hash-object`, not trusted) and three Sandbox geometric addenda (all payload scripts re-executed byte-identical, all closed-form claims independently re-derived by hand rather than read and accepted) all check out exactly. Nothing to correct. `K_full` gate unchanged; Lane A has opened a new HANDOFF requesting an alternative full-K transfer strategy or a resource-certified large-block (~1.4e5-mode) return, which remains open going forward.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-431
parent: v15.236
status: closed
action: none — all four entries independently confirmed exactly as stated; no correction needed.
deliverable: independent confirmation of v15.232 (blob-hash freeze), v15.233-v15.235 (Sandbox geometric addenda, hand-derived and re-executed).
