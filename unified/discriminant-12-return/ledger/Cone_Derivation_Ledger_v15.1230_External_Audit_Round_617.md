# Cone Derivation Ledger v15.1230 — External Audit Round 617

**Date:** 2026-11-19
**Track:** External Audit
**Scope:** Version-number collision flag; independent verification of Gravity's flagged v15.1229 (3D compact Maxwell finite-time evolution)

## Collision found and resolved

Two ledger files both claim version `v15.1229`:

- `Cone_Derivation_Ledger_v15.1229_External_Audit_Round_616.md` — committed by this thread at `edf0e96a42371c9cc2e1c143f6c26b58c41d3178`, **2026-11-19 17:47:42 UTC**.
- `Cone_Derivation_Ledger_v15.1229_Gravity_Compact_Maxwell_Finite_Time_Longitudinal_K4_Scalar_Curvature.md` — committed by Gravity across `842f279f...`→`6872dc8aca1f9544c31ff29a96ea951f1407f8b9`, **2026-11-19 17:51:48–17:56:45 UTC** (source timestamps `12:51:48`–`12:56:45 -0500`, converted).

Per the standing collision protocol: Round 616's commit (17:47:42 UTC) precedes Gravity's entire v15.1229 commit chain (17:51:48 UTC onward) by about 4 minutes. **Round 616 retains the `v15.1229` filename; Gravity's file is flagged here and left untouched** — not renamed, not edited by this auditor. This entry is numbered `v15.1230`.

## Independent verification of Gravity's flagged entry

Read `Cone_Derivation_Ledger_v15.1229_Gravity_Compact_Maxwell_Finite_Time_Longitudinal_K4_Scalar_Curvature.md` in full: a genuine 3D compact, divergence-free vacuum Maxwell Cauchy field (frozen v15.1078 stream-function source) is evolved exactly in Fourier time on three spectral grids (48³, 64³, 80³), its longitudinal k=1 Fourier mode drives the now-corrected (v15.1226/1228) pressure-corrected K4 scalar ODE, and the resulting full-Riemann STF/isotropic curvature is tracked with an explicit Ward-identity convergence study. This is numerical, not purely symbolic, so verification combined analytic cross-checks with independent re-execution:

1. **Propagator physics, re-derived from scratch.** The script's exact Maxwell time-evolution formulas (`Ê(ξ)=cos(|Q|ξ)Ê(0)`, `B̂(ξ)=−i(Q×Ê(0))sin(|Q|ξ)/|Q|`) were independently re-derived from the vacuum Maxwell curl equations: combining `∂Ê/∂ξ=iQ×B̂`, `∂B̂/∂ξ=−iQ×Ê` gives `∂²Ê/∂ξ²=Q×(Q×Ê)=−|Q|²Ê` for the divergence-free (`Q·Ê=0`) compact source, a standard wave equation; with `B(0)=0` (hence `Ê'(0)=0`) this gives exactly `Ê(ξ)=cos(|Q|ξ)Ê(0)`, and integrating `∂B̂/∂ξ` gives exactly `B̂(ξ)=−i(Q×Ê(0))sin(|Q|ξ)/|Q|`. Both match the committed code's `EH*cos(mod*xi)` and `-curl*sin(mod*xi)/mod` exactly. This confirms the physics engine itself, not merely its output.

2. **Initial-jet consistency with already-verified Round 616 formulas.** The entry's stated identities `S_K4(1)=−27R_k(1)/4` and `S_K4dot(1)=+153R_k(1)/4` (for k=1) were checked by substituting `J=J_Φ(1)=−√3R_k(1)` (the signed-source convention confirmed in Round 616/v15.1226) into the already-independently-verified general formulas `S(1,k)=3√3J(k²+2)/[2(1+k²)]` and `S'(1,k)=−3√3J(7k²+10)/[2(1+k²)]` from Round 616/v15.1228: at k=1 these reduce to exactly `−27R_k(1)/4` and `+153R_k(1)/4` — matching the entry's claims exactly, and matching the committed script's own hardcoded `init_exact`/`slope_exact` expressions (`−9r(k²+2)/[2(1+k²)]` and `9r(7k²+10)/[2(1+k²)]` with `r=R_k(1)`, algebraically identical once `J=−√3r` is substituted).

3. **Independent numerical re-execution.** Ran the committed script end-to-end from a clean environment (all three grids, N=48/64/80). Output matched the ledger's table **to every displayed digit**:
   - N=48: `R_k(1)=0.000753143428611668`, `S_K4(1)=−0.005083718143128759`, `S_K4dot(1)=0.028807736144396304`, `S_K4(1.2)=0.0032623991771046283`, `A_iso(1.2)=0.001050383088068395`, energy/momentum Ward residuals `4.5868e-4`/`3.6142e-4`.
   - N=64 and N=80: likewise matched exactly, including the Ward-residual convergence (`4.59e-4 → 5.03e-5 → 4.91e-6` energy; `3.61e-4 → 3.45e-5 → 2.54e-6` momentum) and the final-STF grid-difference bounds (`~2.9e-5` 48-vs-64, `~9.1e-6` 64-vs-80).
   - The script's own internal assertions (initial-jet match to `1e-12`, Ward residuals below `6e-4`, monotonic convergence across grids, STF/isotropic stability bounds) all passed, exit 0, `PASS finite-time free Maxwell source, Ward convergence, K4 scalar integration`.

4. **Scope check.** The entry's own stated boundaries (only the longitudinal k=(0,0,1) scalar mode is integrated; no complete 3D S/V/T metric, no k=0/background handling, no causal photon/mirror/clock detector, matched-model residual against ordinary Einstein+Maxwell+identical-solid remains exactly zero) are consistent with what the script actually computes — no overclaim found.

## Verdict

**PASS.** Gravity's flagged v15.1229 (3D compact Maxwell finite-time evolution driving the corrected K4 scalar channel) is independently confirmed: the underlying propagator physics was re-derived from first principles (not just re-run), the initial-jet values are algebraically consistent with the already-audited Round 616 formulas, and the full three-grid numerical re-execution reproduces the published table exactly with properly converging Ward residuals. The version-number collision is a bookkeeping issue only, not a defect in either entry's substance.

No other new commits landed during this check. `__pycache__` cleaned before this commit; final freshness check performed immediately before push confirmed no intervening changes.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
