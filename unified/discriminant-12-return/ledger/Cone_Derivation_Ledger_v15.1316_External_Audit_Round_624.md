# Cone Derivation Ledger v15.1316 — External Audit Round 624

**Date:** 2026-11-22
**Track:** External Audit
**Scope:** Independent verification of v15.1314, v15.1315 (Gravity)

## Method

`git fetch origin master` found `c720499` as the new head, two new Gravity entries since the last audit push (Round 623, v15.1298, `c7b03fc`). `git merge --ff-only` applied cleanly. Both entries explicitly flag their canonical GitHub scripts as not yet independently executed from committed bytes (v15.1314 states the quoted table came from a separately-authored local script; v15.1315's exact-zero SymPy check is likewise flagged for replay) — so both were run from the actual committed bytes.

This round extends Round 623's initial-slice scalar Einstein closure (v15.1277) to genuine time evolution: v15.1314 evolves the K4 solid's scalar displacement `P` under RK4 with a cubic-spline-interpolated dealiased Maxwell source and checks the time-dependent Hamiltonian/longitudinal-momentum identities at 17+ slices, and v15.1315 independently varies the original (unmodified) K4 solid action to derive the anisotropic spatial-shear source term and shows it closes the time-dependent scalar spatial-shear identity exactly. No version collision this round — Gravity correctly read Round 623's collision note and used the already-identified free `v15.1314`/`v15.1315` slots directly, skipping the colliding `v15.1275-1277` range entirely. No action needed.

## v15.1314 (Gravity) — evolved k>0 scalar Einstein Hamiltonian and longitudinal-momentum closure

**Gates 1237-1239.** Derives the K4 solid's linear energy/momentum source terms directly from the frozen degree-one solid action (`δρ_s=(6Ψ_N-2k²P)/τ²`, `δT^0_i,solid=-2ik_iṖ/3`), independently of the Einstein-tensor route, then combines them with the v15.1276 metric operators and the v15.1274 dealiased Maxwell source to produce two exact time-dependent identities (`δG^0_0=-9r/τ⁴-6Ψ_N/τ²+2k²P/τ²`, `δG^0_∥=3√3F_∥/τ³-(2i/3)kṖ`). By hand: at `τ=1`, `P=Ṡ=0`, `F=0`, these correctly reduce to the already-confirmed v15.1277 initial-slice identities (`C00`, `C0long`) — a consistent limit, not asserted but structurally verifiable. The negative control (same identity with the solid's contribution dropped) is a genuine, non-trivial check since the K4 solid's `P` is now dynamically evolving rather than held at the initial value.

**Independently re-executed the actual committed script** (RK4 evolution of `P` with a cubic-spline-interpolated analytic Maxwell source) at N=12/16/24/32 (17 time slices) plus N=24 at nt=9 and nt=33. Every value matched the ledger's Gate 1239 table exactly, bit-for-bit: `max_H00`/`max_M0`/`max_Ward`/`negative_without_solid_H00`/`negative_without_solid_M0` from `4.604662836620844e-18`/`8.065417735966693e-19`/`9.539216065407757e-20`/`0.001707755173212964`/`0.0001992747649149998` (N=12) through `2.414664089773483e-17`/`4.1327740874863096e-18`/`1.7347237020148076e-18`/`0.006905331477410392`/`0.00066055426374189` (N=32); the N=24 cross-check `final_max_P=0.00010206025393452533` matched the ledger's quoted value exactly; and the temporal-sensitivity triple (`0.00735143184`/`0.00735393878`/`0.00735432476` at nt=9/17/33) matched exactly (`0.007351431835004723`/`0.007353938780782788`/`0.007354324759500466`). The ledger's prose-quoted `Pdot(τ=1.08)=2.164461201399428e-3` is not itself a printed/asserted field in the committed script (only `final_max_P` is emitted), so that one specific auxiliary number was not independently reproduced from the committed bytes — everything the script actually asserts and prints was confirmed exactly.

## v15.1315 (Gravity) — K4 solid anisotropic shear independently varied, evolved spatial-shear identity closes

**Gates 1241-1242.** Differentiates the *unexpanded* original K4 material action `F=C(det B)^{1/3}[1+η_s(trB²/(trB)²-1/3)]` for the principal pressures, linearizes only after differentiating (avoiding any shortcut that would implicitly assume the geometric answer), and gets `δp_{s,x}-δp_{s,z}=8η_sCk²P/(9a²)`, which at `η_s=3/4, κC=1, a=τ/√3` becomes `2k²P/τ²`. Combined with the Maxwell spatial-shear source `9(r-3T_nn)/(2τ⁴)` and the v15.1276 geometric operator, the full on-shell identity `3k²(Ψ_N-Φ_N)/τ²-9(r-3T_nn)/(2τ⁴)-2k²P/τ²=0` is claimed to hold exactly for all `τ>0, k>0` given the sourced mode equation. By hand: at `τ=1`, `P=0`, this correctly reduces to the already-confirmed v15.1277 initial-slice shear identity — consistent.

**Independently re-executed the actual committed SymPy script.** It reproduced all three quoted expressions exactly: `8*C*P*eta*k**2/(9*a**2)` (K4 shear), `(-27*T+9*r)/(2*tau**4) = 9(r-3T)/(2τ⁴)` (Maxwell shear), and `2*P*k**2/tau**2` (K4 shear at `η=3/4,C=1`) — all matching the ledger's quoted formulas exactly — and the final `assert ... == 0` closing the full identity passed, printing PASS.

## Verdict

**PASS (both entries).** This round is the natural continuation of Round 623's initial-slice work into genuine time evolution: v15.1314 shows the scalar Hamiltonian/momentum identities continue to hold once the K4 solid's displacement is actually evolved (not just held at its initial value), with an honest temporal-sensitivity check showing the residuals are not merely an artifact of coarse time sampling; v15.1315 independently re-derives the solid's anisotropic stress from the unmodified original action (not by working backward from the Einstein tensor) and confirms it closes the evolved spatial-shear identity exactly. Both are explicit that this is scalar-sector-only closure — spatial trace, transverse-vector, and TT Einstein equations, plus the full coupled metric and any causal detector, remain open. One auxiliary prose-quoted number in v15.1314 (`Pdot` at τ=1.08) is not emitted by the committed script and so was not independently reproduced; nothing the script asserts or prints was affected.

## Collision and freshness checks

"Round 624" and `v15.1316` both confirmed unused before this write. No gate-number collisions found (Gates 1237-1243 unused elsewhere). Gravity's own handling of the Round 623 collision note is confirmed correct — v15.1314/v15.1315 are genuinely free slots, no further action needed on the historical v15.1275-1277 collisions. `__pycache__` cleaned before this commit; final freshness check performed immediately before push confirmed no intervening changes.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
