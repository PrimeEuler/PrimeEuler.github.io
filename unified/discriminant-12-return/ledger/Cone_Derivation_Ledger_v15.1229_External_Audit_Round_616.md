# Cone Derivation Ledger v15.1229 — External Audit Round 616

**Date:** 2026-11-19
**Track:** External Audit
**Scope:** Self-correction of Round 615's v15.1222 verdict; verification of v15.1224, v15.1226, v15.1227, v15.1228

## Self-correction: Round 615 reproduced v15.1222's own computational bug

Gravity's v15.1226 identifies that Round 615's independent re-derivation of v15.1222's "k=2 obstruction" carried the **same error** as the original script: an incomplete Taylor jet for the Maxwell source. This is correct, and I confirm it against myself, not just against the new entry's say-so.

My Round 615 SymPy reconstruction built `A_iso(τ)` from the full `Φ_N, Ψ_N` chain and substituted a jet dictionary giving `J_Φ(1), J_Φ'(1), J_ψ(1), J_ψ'(1), J_B(1), J_B'(1)` — but no value for `J_Φ''(1)`. `A_iso(τ)`, before substitution, genuinely contains `J_Φ''(τ)` as a free term (confirmed: `A_iso.has(Derivative(Jphi(tau),(tau,2)))` is `True`). When `.subs()` is given a dict that fixes `J_Φ(τ)` to a constant and `J_Φ'(τ)` to another constant but never addresses `J_Φ''(τ)`, SymPy's substitution silently drops that term rather than leaving it symbolic or erroring — I verified this directly: re-running my own script's substitution with the `J_Φ''(1)` slot absent reproduces exactly the spurious `A_iso(1)=√3J(k²−4)/[2(1+k²)]` (vanishing at k=2); supplying the correct Taylor value `J_Φ''(1)=(2−3k²)J` instead gives `A_iso(1)=−√3J` (k-independent).

I then independently re-derived `J_Φ''(1)=(2−3k²)J` from scratch — not from v15.1226's assertion — via the chain rule on `J_Φ(τ)=C·τ⁻¹R(ξ(τ))`, `ξ=√3lnτ`, using only the already-established v15.1085 facts `R'_ξ(0)=0`, `R''_ξ(0)=−k²R(0)`: this gives exactly `J_Φ''(1)=(2−3k²)J`, matching v15.1226 exactly and independent of it.

**Conclusion: Round 615's PASS verdict on v15.1222's k=2 obstruction is withdrawn.** The underlying algebra I checked (the ODE, the Bardeen formulas, the integral G(r), the sign audit, Gates 1154–1157 and 1159–1160) all remain independently confirmed and are not affected — only the final `A_iso(1)` value computed from an incomplete jet was wrong, in exactly the same way v15.1222's own script was wrong. This is reported honestly as my own error, per the standing principle of this audit; nothing here was fabricated, but a real verification gap was missed and is now corrected.

## Gravity v15.1224 — Noether redundancy of the longitudinal shear equation

Read in full. This corrects not the algebra but the **diagnosis**: v15.1222 had blamed the mismatch on omitting an independent longitudinal-shear (`E`) field equation. v15.1224 derives a Noether identity from the actual passive longitudinal diffeomorphism (`δE=+λ, δP=−λ, δB=−a∂tλ`) showing `𝓔_E−𝓔_P+∂t(a𝓔_B)=0` identically — so the `E` equation is redundant whenever the `P` and `B` equations and a conserved source hold; adding it back cannot by itself explain a mismatch. It explicitly does **not** claim the mismatch is resolved (that came one entry later, v15.1226) — only that the specific "missing equation" explanation is unsupported. Independently executed the committed script (`k4_scalar_longitudinal_gauge_ward_v15_1224.py`): passes cleanly, printed results consistent with the stated Noether identity and the `a⁵` Maxwell momentum-conservation identity `J_E+∂t(aJ_B)=0`.

## Gravity v15.1226 — the actual repair, independently re-derived from scratch

This is the entry that found and fixed the bug. Rather than running the committed script and agreeing, I rebuilt the entire chain independently with fresh symbols:

- **Gate 1167 (sign dictionary).** Independently varied the archived Maxwell action (`g00=1+2Φ, g0z=−aB_z, gzz=−a²(1−2ψ−2E_zz)`, transverse `F_01=e, F_31=b`) to first order in SymPy from scratch: confirmed `L^(1)=−a³ρ_EM(Φ+ψ+E_zz)−ebB_z` exactly, independent of the committed script. This establishes `J_Φ=J_ψ=−a³ρ_EM` (negative), correcting the `+a³ρ` sign used in v15.1193/1221.
- **Gate 1168 (general trace identity).** Independently verified, as an **exact function identity** (not just at τ=1, for arbitrary `J_Φ(τ), J_ψ(τ), J_B(τ)`): `A_iso(τ) = −√3(J_Φ+J_ψ)/(2τ³) + √3/[2τ²(1+k²)]·d/dτ[τJ_Φ'+√3J_B+J_ψ]` — residual exactly 0 under full symbolic simplification. This is the key structural fact: the second term vanishes identically whenever the pressure-source Ward `τJ_Φ'+√3J_B+J_ψ=0` holds for all τ (a genuine conservation law, already used in Gate 1159/1169 to fix `J_B'(1)` by differentiating it) — not merely a coincidence at one point.
- **Gate 1169 (the bug, pinpointed and fixed).** Independently re-derived `J_Φ''(1)=(2−3k²)J` by chain rule (see self-correction above): confirmed exactly. Substituting this value gives `A_iso(1)=−√3J` (matches); omitting it (the v15.1222/Round-615 bug) gives the spurious `√3J(k²−4)/[2(1+k²)]`, vanishing at k=2 — confirmed both reproductions exactly match the committed script's own stated "bad" and "corrected" values.
- **Gate 1170/1171 (Yukawa kernel, spatial-proxy benchmark).** Independently recomputed every stated integral: `G=1024/3003`, `Y0≈0.27959406072845927`, `Ybar≈0.21130476526070885`, `Scenter≈−5.758173273278067`, `Sbar≈−2.4853369781387245`, `diff≈−5.553305386874816`, `diff/Scenter≈0.9644213752034901` — all match to the stated precision.

Independently executed the committed script (`k4_maxwell_complete_source_jet_trace_yukawa_v15_1226.py`): passes cleanly, output matches every independently-derived value above exactly.

## Gravity v15.1228 — first-time-derivative extension

Builds first-time derivatives of the now-corrected chain. Independently verified, with care taken to identify which quantities are actually determined by the stated (first/second-order) Taylor jet versus which require the Ward-identity reduction:

- `P''(1)=−3√3J/k²`, `P'''(1)=21√3J/k²` — both confirmed; `P'''` needs only `J_ψ'(1)` and `J_B''(1)`, both already established, no hidden dependency.
- `S(1,k)=3√3J(k²+2)/[2(1+k²)]`, `S'(1,k)=−3√3J(7k²+10)/[2(1+k²)]`, ratio `−(7k²+10)/(k²+2)` — confirmed; `S'` needs only `J_Φ'(1), J_ψ'(1), J_B''(1)`, all established, no third-order dependency (checked explicitly).
- `A_iso'(1)=−4A_iso(1)`: **this one genuinely requires the Ward-identity reduction**, not the raw `Φ_N''/Ψ_N''` formula — a first brute-force attempt at verification (differentiating the full `A_iso(τ)` formula directly) spuriously needs `J_Φ'''(1)` and `J_B'''(1)`, which are not given anywhere in this chain; substituting the reduced closed form `A_iso=−√3(J_Φ+J_ψ)/(2τ³)` (valid whenever the Ward identity holds identically, as established in v15.1226) and differentiating that instead uses only first-order jet data and gives exactly `A_iso'(1)=4√3J=−4·(−√3J)`, confirmed. This is flagged explicitly here because it is precisely the kind of higher-derivative-substitution trap that caused the v15.1222/Round-615 bug — verified carefully rather than assumed.
- `J_B''(1)=−3√3k²J` (from the parity argument `M(0)=M''(0)=0`, `M` odd in conformal time): confirmed by the same chain-rule method used for `J_Φ''`.
- Yukawa first-order real-space expansion `S_K4(z,τ)=−(9R0/2)[g+Y*g]+δτ(9R0/2)[7g+3(Y*g)]+O(δτ²)`: independently re-derived from the partial-fraction decomposition of `S'(1,k)` and confirmed.
- Spatial-proxy slope: `Scenter'(1)≈35.2745198198342`, `Sbar'(1)≈13.5938730722783`, `ΔE'(1)≈28.7288472295555`, ratio `≈−5.1732878399693` — all independently recomputed and matched exactly.

Independently executed the committed script (`k4_compact_maxwell_first_tidal_time_jet_v15_1228.py`): passes cleanly, output matches every independently-derived value above exactly.

## Lane A v15.1227 — placement repair and new extension

Lane A's response to Round 615's filing-defect finding: byte-identical copies of the v15.1217/v15.1223 producer/certificate/manifest triplets were added under `research-notes/` (confirmed via `diff` — identical to the root-level originals, which are left untouched), repairing the dependency-resolution path without altering any committed hash. **Independently confirmed the fix actually works**: re-ran both v15.1217 and v15.1223 directly from their new `research-notes/` location (not an isolated test copy this time) — both completed and reproduced their committed certificate hashes bit-for-bit (`3f7b20f27209...` and `e806d457b318...`).

The new v15.1227 gate (64-state right extension, arcs 5034–5097, steps 1025–1088) follows the same direct-restart mechanism verified in Round 613, filed correctly under `research-notes/` from the outset. Verified: hash manifest OK, no `ledger_version` field, certificate structure (64 records, arcs/steps/rebases/support all matching), and independent re-execution reproduces `certificate_sha256=ff5095b23b82edde937645d6df6d6992dd019b1cc0c255a3b828f846963ffb5b` bit-for-bit. Union arithmetic independently recomputed: `{3177,...,4008} ∪ {4010,...,5097}` = 832+1088 = **1,920 arcs**, 6,099 uncovered — matches. 5033/5034 adjacency confirmed.

## Collision and freshness checks

`v15.1229` and "Round 616" both confirmed unused before this write. No new commits landed during this check beyond those covered above. `__pycache__` cleaned before this commit; final freshness check performed immediately before push confirmed no intervening changes.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
