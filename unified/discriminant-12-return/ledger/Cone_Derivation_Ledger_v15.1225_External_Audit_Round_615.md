# Cone Derivation Ledger v15.1225 — External Audit Round 615

**Date:** 2026-11-19
**Track:** External Audit
**Scope:** Independent verification of v15.1217, v15.1221, v15.1222, v15.1223

## Method

`git fetch origin master` + `git merge --ff-only` confirmed `2bf0c82` as the head at the start of this round (a further commit, `dcb62d4`/Gravity v15.1224, landed mid-round but has not yet published its `.md` ledger entry — only a supporting script — following the same pattern v15.1221/1222 used; it is left for a future check once complete). Four new ledger entries since Round 614/liveness v15.1216: Lane A's v15.1217 and v15.1223 (further direct-restart right extensions), and Gravity's v15.1221 and v15.1222 (K4/Maxwell isotropic-trace physics). Read all four in full.

## Lane A v15.1217 and v15.1223 — direct-restart right extensions

Both are further 64-state right extensions using the direct-restart mechanism already scrutinized and confirmed sound in Round 613 (v15.1217: arcs 4906–4969, steps 897–960; v15.1223: arcs 4970–5033, steps 961–1024).

**Finding: both producers, certificates, and manifests were committed to the wrong directory.** Every prior Lane A entry placed its producer/certificate/manifest in `unified/discriminant-12-return/research-notes/`; these two instead landed directly in `unified/discriminant-12-return/`. This is not cosmetic: the script's own dependency-resolution logic (`SOURCE_CANDIDATES = (HERE / SOURCE_NAME, HERE.parent / "research-notes" / SOURCE_NAME)`) assumes the script lives in `research-notes/`, so when actually committed one level up, `HERE.parent` lands in `unified/` rather than `unified/discriminant-12-return/`, and neither candidate path resolves. **Verified by direct reproduction:** running each committed script from its own committed location raises `FileNotFoundError: cannot locate lane_a_v15_842_suzuki_r4_streamed_exact_support_scaling.py` for both v15.1217 and v15.1223. The "replay the committed producer" instruction in each entry's audit handoff therefore fails out of the box from a clean checkout.

This is a filing/deployment defect, not a mathematical one. To confirm the certificates themselves are still sound, both scripts and the two frozen dependencies were copied (unmodified) into an isolated scratch directory with the layout the scripts expect (frozen deps and producer together in a `research-notes/` folder), and re-executed there:

- v15.1217 emitted `certificate_sha256 = 3f7b20f2720920dfb2538a6d2735757aeb0c7c0a5e1c4d046763b17ec1f8a2bb` — **bit-for-bit identical** to the committed certificate.
- v15.1223 emitted `certificate_sha256 = e806d457b3188da237832e9f23592fb062f7ab58e2095cc8fa4462eb8e8bf30d` — **bit-for-bit identical** to the committed certificate.

Both also passed the standard checks: hash manifest verification (`sha256sum -c`, all four files OK), no `ledger_version` provenance field in either script or certificate, and independently parsed certificate structure matching the ledger exactly:
- v15.1217: 64 records, arcs `{4906,...,4969}`, direction +1, steps 897–960, 16 rebase flags, max support 160, all pass.
- v15.1223: 64 records, arcs `{4970,...,5033}`, direction +1, steps 961–1024, 16 rebase flags, max support 160, all pass.

**Union arithmetic**, independently recomputed: after v15.1217, `{3177,...,4008} ∪ {4010,...,4969}` = 832+960 = **1,792 arcs**, 6,227 uncovered — matches. After v15.1223, `{3177,...,4008} ∪ {4010,...,5033}` = 832+1024 = **1,856 arcs**, 6,163 uncovered — matches. 4969/4970 adjacency confirmed.

**Verdict: PASS on mathematics, FLAG on filing.** The certificates are genuine and bit-exact; the misplacement should be corrected in the next entry from that lane so the committed scripts are reproducible as-is, but nothing here is silently patched or renamed by this auditor — the files are left exactly as committed.

## Gravity v15.1221 and v15.1222 — K4/Maxwell isotropic trace and the k=2 obstruction

This is dense physics content; every load-bearing formula was independently re-derived from scratch in SymPy (not by re-running the committed scripts and agreeing), and cross-checked against the actual archived source files it claims to build on, not just the new entry's restated prose.

**Gate 1154 (K4 homogeneity).** Read the frozen material energy density `F(B)=C·b^(2/3)(1+η_s J)`, `b=√(det B)`, `J=tr(B²)/(tr B)²−1/3`. Independently built `B=diag(x,y,z)` in SymPy and confirmed exactly: `F(λB)−λF(B)` simplifies to 0 (degree-1 homogeneity), and Euler's identity `x·F_x+y·F_y+z·F_z−F` simplifies to 0. This gives `T^μ_μ=−2F` and hence `ρ_K4+Σp_i=0` exactly, as claimed.

**Gate 1155/1157 (Einstein trace and the sign audit).** By hand: `tr E=R_00=κ(T_00+T/2)`; with the K4 solid's `ρ+Σp=0` and Maxwell's zero stress trace (`Σp_EM=ρ_EM`), this gives `R_00=κρ_EM` and `A_iso=κρ_EM/3` exactly — confirmed independently, matches the entry. For the sign audit: with `J_Phi=a³ρ_EM`, `a(1)=1/√3`, `κ=1`: `ρ_EM=J0/a³=3√3 J0`, so `A_iso=κρ_EM/3=√3 J0` — the **opposite sign** from v15.1198's own formal result `A_iso=−√3 J0` at τ=1. Confirmed by hand; this is a genuine, correctly-identified open sign discrepancy, not resolved by this entry (appropriately — it says so itself).

**Gate 1156 (compact-packet spatial proxy).** Independently computed `G(r)=(1/r)∫_0^r(1−u²)^6 du` in SymPy: closed form confirmed, and both stated numeric values confirmed exactly: `G(1/2)` gives `(8G+1)/9 = 9518623/13837824`, `G(1)` gives `(8G+1)/9 = 11195/27027`. Also independently confirmed the algebraic identity `[(2G+1)/3]S0+(G−1)A0 = [(8G+1)/9]S0` given `A0/S0=2/9` (stated), by direct substitution.

**Gates 1159–1161 (the k-dependent obstruction — the most substantial new claim).** Read the actual archived source files this builds on (not just trusted the restated formulas): `k4_maxwell_full_initial_svt_source_v15_1085.py` (confirms the Maxwell stress split `T=diag(P,−P,R)`, `tr(T)=R`, longitudinal anisotropic stress `2R/3`, and the Ward identities `ρ̇=−iqS_z`, `Ṡ_z=−iqT_zz`), `k4_traceful_scalar_ward_v15_728.py` and `k4_traceful_scalar_weyl_v15_729.py` (confirms the exact pressure-corrected `P` ODE and Bardeen potential formulas), and `k4_full_fermi_riemann_v15_787.py` (confirms the `R_STF=−k²Φ/a²` and `A_raw` formulas are genuinely the actual Riemann tensor components derived there, not invented for this entry).

Built an independent SymPy reconstruction from scratch (fresh function/symbol names, not copied from the committed script) of the full chain: the `P` ODE and its self-consistent third-derivative elimination, the Bardeen potentials, `R_STF`, `A_raw`, and `A_iso`, then substituted the stated Maxwell initial-jet Taylor data (`J_Φ(1)=J_ψ(1)=J`, `J_Φ'(1)=J_ψ'(1)=−J`, `J_B(1)=0`, `J_B'(1)=√3k²J`, from the stated Ward identity and conservation jet) at τ=1. Result, matching the ledger exactly in every term:
- `P''(1) = −3√3J/k²`
- `Φ_N(1) = −√3J(k²+2)/[2k²(1+k²)]`
- `Ψ_N(1) = √3J/[2(1+k²)]`
- `R_STF(1) = 3√3J(k²+2)/[2(1+k²)]`
- `A_iso(1) = √3J(k²−4)/[2(1+k²)]` — vanishes exactly at k=2, confirmed; derivative w.r.t. k confirmed to be `5k/(1+k²)²`, confirmed nonconstant so no single sign flip or normalization fixes it at every k.

This is a real, independently-reproduced counterexample: a physically sourced (positive-energy) Maxwell packet gives zero isotropic curvature response at k=2 under the E-fixed reduced equations, which cannot be reconciled with the k-independent physical Einstein-trace requirement `A_iso=κρ_EM/3` by any overall sign or constant rescaling. Gravity's own conclusion — that the E-fixed reduction is missing the longitudinal shear-stress equation (Gate 1162, independently confirmed against v15.1085's `Π_L=2R/3≠0`) — is the correct, appropriately cautious reading of this result, not an overclaim.

**Script execution.** All three committed scripts (`k4_compact_maxwell_active_trace_sign_audit_v15_1221.py`, `k4_v15_1198_symbolic_limit_additive_repair_v15_1221.py`, `k4_compact_maxwell_shear_constraint_obstruction_v15_1222.py`) were independently executed end-to-end and passed cleanly, with printed results matching the independent derivation above exactly.

**v15.1198 repair wrapper, re-checked.** Confirmed the original `k4_null_maxwell_full_riemann_arm_proxy_v15_1198_corrected.py` still contains the exact buggy line (`assert s.limit(geom,kr,0)==R`) exactly once, untouched. The wrapper reads this file from disk, asserts the exact string occurs exactly once (refusing to patch silently otherwise), substitutes only that one line in memory, and executes the corrected version — confirmed this actually runs and passes, closing the "await execution by independent Audit" note left open in v15.1221's own text.

**Verdict: PASS.** Every mathematical claim in both entries is independently confirmed, correctly sourced from the genuine archived files it builds on, and the open issues (sign convention, missing shear equation) are honestly flagged rather than glossed over.

## Collision and freshness checks

`v15.1225` and "Round 615" both confirmed unused before this write. No other new `.md` ledger entries landed during this check (only the v15.1224 supporting script, whose `.md` has not yet been published). `__pycache__` and scratch test directories cleaned before this commit; final freshness check performed immediately before push confirmed no intervening ledger changes.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
