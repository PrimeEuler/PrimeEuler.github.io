# Cone Derivation Ledger v15.1320 — External Audit Round 625

**Date:** 2026-11-22
**Track:** External Audit
**Scope:** Independent verification of v15.1317, v15.1318, v15.1319 (Gravity)

## Method

`git fetch origin master` found `f33e8f5` as the new head, three new Gravity entries since the last audit push (Round 624, v15.1316, `25e6bfc`). `git merge --ff-only` applied cleanly. No version collision this round — Gravity correctly skipped v15.1316 (owned by this thread's Round 624) and used the free v15.1317-1319 slots directly. All three entries flag their committed scripts as not yet independently executed from committed bytes; v15.1318's entry explicitly notes Gravity's own attempt to fetch and run its exact committed file failed on their end due to DNS/network restrictions, making this round's independent execution of that script the first confirmation of its committed bytes by anyone.

This is a significant round: v15.1317 and v15.1318 close the remaining scalar-spatial and transverse-vector sectors (continuing v15.1314-1316's pattern of conditional on-shell closure), but v15.1319 is a genuine, well-diagnosed **negative** result — a sign inconsistency between the archived TT tensor-evolution equation (v15.750/v15.1234/v15.1235/v15.1262) and the explicitly declared spatial-metric convention (v15.787), caught by deriving the TT Einstein operator directly from the metric rather than reusing the electric-Riemann shortcut.

## v15.1317 (Gravity) — scalar spatial trace and longitudinal/transverse pressure closure

**Gates 1244-1246.** Differentiates the unexpanded original K4 action for both individual scalar-projected principal pressures (not just their difference, which v15.1315 already covered), getting `δp_{s,trans}=-2Ψ_N/τ²+4k²P/(3τ²)` and `δp_{s,long}=-2Ψ_N/τ²-2k²P/(3τ²)` (difference `2k²P/τ²` matches the already-confirmed v15.1315 shear exactly, a good consistency check). Combines these with the v15.1276 geometric operators and the already-confirmed v15.1314 sourced `P` equation to close two more time-dependent scalar spatial identities (`C_long`, `C_trans`).

**Independently re-executed the actual committed SymPy script.** Both `assert s.factor(Gz-Tz)==0` and `assert s.factor(Gx-Tx)==0` passed exactly, as did the two independently-varied solid pressure checks (`px+2Ψ/τ²-4k²P/(3τ²)==0`, `pz+2Ψ/τ²+2k²P/(3τ²)==0`) — all four exact-zero symbolic assertions reproduced, matching the ledger's claimed PASS.

## v15.1318 (Gravity) — transverse-vector Einstein momentum and offdiagonal closure

**Gates 1247-1249.** Derives the vector-sector metric-to-Einstein operators (`δG^0_y`, `δG^y_z`) by direct Christoffel/Ricci computation from an explicit `g_{0y}` metric perturbation, independently varies the original K4 action's offdiagonal stress (explicitly using the archived **minus-sign** vector-displacement convention `φ^y=y-f_V e^{ikz}`, flagged as a convention that must not be silently swapped with the scalar `+` convention), and closes both sourced vector Einstein equations (`C_0y`, `C_yz`) using the archived vector Euler equation and Maxwell transverse-momentum Ward.

**Independently re-executed the actual committed script** — notably, the one entry this round that Gravity itself could not run from committed bytes (its own network access to raw GitHub failed). All five `assert s.simplify(...)==0` checks passed exactly: the two geometric operator identities, the background curvature check, the offdiagonal solid-stress identity, and both sourced vector Einstein closures. This is the first confirmation that the actual committed bytes of this script execute correctly at all, not just that the separately-tested mathematical pieces work.

## v15.1319 (Gravity) — genuine negative result: TT tensor source sign inconsistency

**Gates 1251-1254.** Derives the TT-sector metric-to-Einstein operator directly from the explicitly declared spatial metric `g_{xx}=a²(1+γe^{ikz})`, `g_{yy}=a²(1-γe^{ikz})` (the same convention stated in v15.787), getting `δG^x_x=+(γ''+3γ'/τ+3k²γ/τ²)/2`. Independently varies the original K4 action's TT principal-pressure difference (inheriting the already-Audited v15.1264 homogeneous tensor-shear constitutive law) to get the solid's TT stress `δT^x_x,solid=-γ/τ²`. Combining these gives `γ''+3γ'/τ+(3k²+2)γ/τ²=+18Π_plus/τ⁴` — but the archived tensor evolution equation in v15.750/v15.1234/v15.1235/v15.1262 uses `...=-18Π_plus/τ⁴`, an explicit sign flip, with the same `Π_plus` Maxwell stress projector in both. The entry correctly notes the tidal trace used in prior rounds (v15.1267 etc.) cannot detect this, since the TT sector is traceless — this fault was invisible to every previously passing trace-based check.

By hand: this is a real, structural ambiguity of exactly the kind that arises in GW/TT literature from differing sign conventions for the strain variable (`γ_metric` vs. a possibly separately-defined `γ_evolution=-γ_metric`) or for the stress projector. The entry does not paper over it — it explicitly computes the magnitude of the discrepancy and proposes two candidate resolutions (sign-flipped evolution variable, or sign-flipped source projector) without picking one, correctly leaving the actual historical-code trace to a dedicated follow-up.

**Independently re-executed the actual committed NumPy script** (using the real, non-trivial oblique-mode compact Maxwell source, not a toy input) at N=24/32/48. Every value matched the ledger's Gate 1253 table exactly, bit-for-bit: `Pi_plus_real` = `0.00048158021257934346`/`0.0004546200702725532`/`0.0004612348231110169`, and `archived_Einstein_plus_residual_real` = `-0.008668443826428182`/`-0.008183161264905958`/`-0.008302226815998303` at N=24/32/48 respectively — confirming the sign-mismatch residual is genuinely large (several orders of magnitude above roundoff), not a numerical artifact.

## Verdict

**PASS (v15.1317, v15.1318); NEGATIVE, correctly reported (v15.1319).** The scalar and vector sectors now have conditional on-shell closure consistent with every prior round in this chain, independently re-derived from the frozen K4 action rather than inferred from Einstein geometry, and both committed scripts reproduce exactly — including v15.1318, whose committed bytes nobody (not even its author) had run until this round's replay. v15.1319 is exactly the kind of honest, well-isolated negative finding this audit exists to confirm: a genuine sign inconsistency in the TT sector, invisible to every previously-passing trace-based test, correctly diagnosed down to two concrete candidate causes without prematurely picking one or silently patching the historical code. This in no way invalidates the already-Audited scalar/vector closures or the trace-based Maxwell-K4 composition work from Rounds 620-624, as the entry itself correctly notes.

## Collision and freshness checks

"Round 625" and `v15.1320` both confirmed unused before this write. No gate-number collisions found (Gates 1244-1254 unused elsewhere). No version collision this round. `__pycache__` cleaned before this commit; final freshness check performed immediately before push confirmed no intervening changes.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
