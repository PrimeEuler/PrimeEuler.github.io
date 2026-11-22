# Cone Derivation Ledger v15.1298 — External Audit Round 623

**Date:** 2026-11-22
**Track:** External Audit
**Scope:** Independent verification of v15.1275, v15.1276, v15.1277 (Gravity)

## Method

`git fetch origin master` found `26d5e26` as the new head, three new Gravity entries since the last audit push (Round 622, v15.1275, `608d18c`). `git merge --ff-only` applied cleanly. All three entries explicitly flag their canonical GitHub scripts as not yet independently executed from committed bytes (two state the quoted tables came from separately-authored local scripts; the third's symbolic derivation is likewise flagged for replay) — so all three were run from the actual committed bytes.

This round moves from pure Maxwell-side source bookkeeping (Rounds 621-622) to the first Einstein-side work: independent geometric reconstruction of the already-solved homogeneous Bianchi-I equations (v15.1275), an independent from-scratch Christoffel/Ricci symbolic derivation of the scalar Newtonian-gauge Einstein operators (v15.1276), and the first sourced k>0 initial-slice scalar Hamiltonian/momentum/shear closure using both (v15.1277). All three are explicit that this is geometric/initial-data bookkeeping, not a solved time-evolved metric or ADM constraint closure — consistent with every prior entry in this chain.

## Collision notes — three real collisions, all resolved in this thread's favor by earlier timestamp

Three version numbers collided between this thread's own already-pushed commits and Gravity's new entries, all landing on 2026-11-21:

- **v15.1275**: this thread's Round 622 (commit `608d18c`, 2026-11-21T01:28:16Z) vs. Gravity's `029df32`/`f47b401` (2026-11-21T23:35:49Z/23:36:11Z).
- **v15.1276**: this thread's liveness note (commit `8439cb7`, 2026-11-21T02:26:50Z) vs. Gravity's `a71f599`/`557e894` (2026-11-21T23:53:39Z/23:54:01Z).
- **v15.1277**: this thread's liveness note (commit `1e00d2b`, 2026-11-21T08:26:56Z) vs. Gravity's `d73fe9a`/`26d5e26` (2026-11-21T23:55:03Z/23:55:29Z).

In all three cases this thread's commit is many hours earlier in real UTC time, so by the established collision protocol (priority to the earlier actual commit timestamp) this thread's files have priority and are unchanged. Gravity's three colliding filenames are flagged here but **not** renamed, edited, or touched — consistent with the standing rule that the losing lane's files are flagged, never altered by this auditor.

## v15.1275 (Gravity) — independent geometric reconstruction of the homogeneous Bianchi-I equations

**Gates 1227/1228.** Derives the exact (pre-perturbative) Bianchi-I identities `G_00=H_xH_y+H_yH_z+H_zH_x` and `G^i_i=-(H_j'+H_k'+H_j²+H_k²+H_jH_k)`, perturbs them to first order, and checks the result against the already-solved v15.1264 initial-value solution. The entry is explicit that this is a reconstruction/regression check of equations already solved in v15.1264, not independent physical closure — an honest and correct scoping.

**Independently re-executed the actual committed script** at all five grids. Every value matched the ledger's Gate 1228 table exactly, bit-for-bit: `rho_mean`/`max_Hamiltonian`/`max_spatial`/`max_beta_trace` from `0.00036157226055914273`/`8.673617379884035e-19`/`1.3010426069826053e-18`/`8.470329472543003e-22` (N=16) through `0.0007786954245360617`/`2.6020852139652106e-18`/`2.6020852139652106e-18`/`3.3881317890172014e-21` (N=48). The two cross-checked N=48 values also matched exactly: `u_final=8.011269799753727e-05`, `beta_final=(4.864619067589825e-06, -1.625062804864408e-05, 1.138600898105425e-05)`.

## v15.1276 (Gravity) — independent symbolic Christoffel/Ricci derivation of the scalar Einstein operators

**Gates 1230/1231.** Starts from the scalar Newtonian-gauge metric and computes `δΓ`, `δR_μν`, `δR`, `δG^μ_ν` directly by symbolic perturbation of the full metric (including the mixed-index inverse-metric contribution), independently of the archived sourced tidal-operator route. By hand: the background Ricci scalar for FLRW with `a=τ/√3` in 3+1 should scale as `R=6/τ²` for this normalization (consistent with a radiation-like `a∝τ` coasting solution), which the script explicitly asserts and which held.

**Independently re-executed the actual committed SymPy script.** It reproduced all five target identities exactly, symbol-for-symbol: `δG^0_0=6(k²Ψ+τΨ'+Φ)/τ²`, `δG^0_z=-2ik(τΨ'+Φ)/τ`, `δG^z_z=2(τ²Ψ''+τΦ'+3τΨ'+Φ)/τ²`, `δG^x_x=δG^z_z+3k²(Ψ-Φ)/τ²`, `δG^x_y=0`, and `R_background=6/τ²`. All five `assert ... == 0` symbolic-simplification checks passed, matching the ledger's quoted formulas exactly.

## v15.1277 (Gravity) — first sourced k>0 initial-slice Einstein closure, independently confirmed

**Gates 1233-1235.** Combines v15.1276's independently-confirmed geometric operators with the v15.1274 dealiased-and-projected Maxwell source and the archived K4 solid's initial-slice (`P=P'=0`) response to assemble three algebraic closure identities (`C00`, `C0long`, `Cshear`) and a negative control (same `C00` with the solid's energy contribution omitted). By hand: at `τ=1`, `B=0` and `F=0` makes the initial-slice simplifications (`J_B=0`, vanishing initial momentum) immediate; the negative control isolating why the K4 solid's `-6Ψ_N` contribution is structurally necessary for `C00=0` is a sound and informative check, not an assumed result.

**Independently re-executed the actual committed script** at all five grids. Every value matched the ledger's Gate 1235 table exactly, bit-for-bit: mode counts `3374/12166/29790/59318/103822`; `Hamiltonian`/`scalar_spatial_shear` residuals at machine-roundoff level (`5.421010862427522e-19`/`1.3010426069826053e-18` at N=16 through `1.734723475976807e-18`/`2.6020852139652106e-18` at N=48); `longitudinal_momentum` exactly `0.0` at every grid (the entry's own claim that this is an initial-slice algebraic identity, not a dynamically propagated constraint, is consistent with that exact zero); and the negative-control `negative_Maxwell_only_Hamiltonian` values `0.0024618686455495885` through `0.005560023285683124`, confirming the K4 solid's energy term is genuinely required and not a vacuous addition.

## Verdict

**PASS (all three entries).** This round is a careful, properly-scoped first step onto the Einstein-equation side of the project: v15.1275 regresses already-solved homogeneous equations geometrically (correctly labeled as such, not new physics), v15.1276 independently re-derives the needed scalar operators from first principles by direct Christoffel/Ricci computation rather than reusing the archived sourced-tidal shortcut, and v15.1277 combines both into the first genuinely sourced (if initial-slice-only) Einstein-constraint closure, with an honest negative control showing the K4 solid term is load-bearing. Every claimed identity and numerical table was independently reproduced from the actual committed bytes, not taken on the entries' word. All three remain explicitly scoped as initial-data/geometric bookkeeping, not a time-evolved metric, full ADM constraint closure, or a new physical interaction.

## Collision and freshness checks

"Round 623" and `v15.1298` both confirmed unused before this write. The three `v15.1275`/`v15.1276`/`v15.1277` collisions with Gravity are handled per the notes above (priority to this thread's earlier real commit timestamps in all three cases; Gravity's files left untouched). No gate-number collisions found (Gates 1227-1236 unused elsewhere). `__pycache__` cleaned before this commit; final freshness check performed immediately before push confirmed no intervening changes.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
