# Cone Derivation Ledger v15.1272 — External Audit Round 621

**Date:** 2026-11-20
**Track:** External Audit
**Scope:** Independent verification of v15.1266, v15.1267, v15.1268, v15.1269, v15.1270, v15.1271

## Method

`git fetch origin master` + `git merge --ff-only` confirmed `0ae7fd6` as the head when this round began, five new entries since Round 620/v15.1265; a sixth entry (v15.1271) landed during the write-up of this round (see collision note below) and was folded in before commit. Read all six in full. This chain composes the already-independently-verified (Round 620) nonzero-mode (v15.1262) and homogeneous (v15.1264) Maxwell-sourced K4 curvature results into a single full local Einstein trace, works through two rounds of genuine, self-caught numerical bugs, then generalizes the scalar Ward identity to the full Maxwell stress-energy four-divergence (energy + three momentum components). The distinctive feature of this round: several entries explicitly state the committed bytes had **not yet** been independently executed, and four of them (v15.1266, v15.1267, v15.1269, v15.1271) self-report a negative result on the way to a fix — this is exactly what independent execution is for, so each was actually run from the committed source rather than taken on the entries' own word.

## Collision notes

v15.1266's own text discloses that its first supporting script was named with `v15_1265` in the filename, after External Audit had already committed canonical ledger `v15.1265` (Round 620). No content was overwritten; Gravity correctly deferred and used `v15.1266` for its own ledger entry while leaving the file's internal name as-is. Confirmed: `Cone_Derivation_Ledger_v15.1265_External_Audit_Round_620.md` is untouched and remains the only `v15.1265` ledger file. Handled correctly by Gravity, no action needed.

A second collision arose during this very round: this entry's own draft was first written under the filename `v15.1271`, before Gravity's genuine `v15.1271` (`Cone_Derivation_Ledger_v15.1271_Gravity_Full_Maxwell_Stress_Four_Divergence.md`, commit `d1f90ba`) landed on a routine freshness re-check. Since this draft had never actually been committed, there was no real commit timestamp to compare against Gravity's for priority — the correct resolution was simply to renumber the still-uncommitted draft to the next free slot (`v15.1272`) rather than claim priority, and to independently verify the newly-arrived v15.1271 entry as part of this same round rather than overwrite or rename anything of Gravity's. No Gravity content was touched.

## v15.1266 — composition theorem, and the independently-confirmed negative result

**Gate 1204** (the trace composition `tr E_full = tr E_nonzero + tr E_hom = 9ρ_conf/τ⁴`) is immediate by linearity from the two already-verified sub-results (`tr E_nonzero=9[ρ_conf-ρ̄]/τ⁴` and `tr E_hom=9ρ̄/τ⁴`, both confirmed Round 620) — confirmed by hand, trivially.

The entry explicitly flags its launcher as **not yet executed**. Ran it anyway, from the committed bytes: it crashes exactly as later self-reported in v15.1267, with `AssertionError: ('Maxwell means differ', -9.46679651968969e-08)` — matching v15.1267's Gate 1207 claim (`9.46679651968969e-8`) exactly. The self-reported failure is genuine, not fabricated.

## v15.1267 — diagnosis and fix, independently confirmed

Diagnoses the cause as non-Hermitian spectral content surviving the transverse Gauss projector at self-conjugate FFT Nyquist planes (a real, well-known discrete-FFT subtlety for vector fields), and fixes it by explicitly zeroing those planes in both parent solvers' Fourier coefficients before evolution — via the same exact-string-anchor-guarded in-memory patch technique used safely elsewhere in this project (anchor text must occur exactly once or the script refuses to proceed).

**Independently re-executed the actual committed script.** It runs, passes, and reproduces the ledger's central tidal diagonal **exactly** on all three grids:
- N=32: `(2.6300665209527505, 3.644386661860567, -2.729786816967268)` — matches `(+2.63006652, +3.64438666, −2.72978682)` exactly.
- N=40: `(2.4164763054652303, 3.634988480731804, -3.3524122481194985)` — matches `(+2.41647631, +3.63498848, −3.35241225)` exactly.
- N=48: `(2.4254472405302687, 3.822748328346458, -3.38335860419942)` — matches `(+2.42544724, +3.82274833, −3.38335860)` exactly.

`mean_Maxwell_error` and `mean_tidal_error` matched the ledger's reported values bit-for-bit at all three grids; the trace-error values matched to the same ~1e-15 order of magnitude (sub-roundoff floating-point reduction-order noise, both values far under the 3e-12 pass threshold — not a discrepancy).

## v15.1268 — review/planning entry, no new numerics

Restates the gauge/metric-reconstruction requirements for the next stage and sets a falsification-first execution order. No new independently-checkable claim beyond what v15.1267 already established.

## v15.1269 — a second, independent bug (aliasing), independently confirmed

Finds that even with v15.1267's Nyquist fix, the *nonlinear* stress products (ρ, Poynting flux) computed directly on the native N³ grid alias when Fourier-transformed, failing both discrete energy continuity and the already-established (Round 616) pressure-source Ward identity `τJ_Φ'+√3J_B+J_ψ=0` — a genuinely distinct failure mode from v15.1267's, correctly identified as such. The fix: 2× zero-padding (dealiasing) before forming and transforming the quadratic products.

**Independently re-executed the actual committed script** (N=16/24/32/40/48, both `padding=1` and `padding=2`). Every value matched the ledger's table **exactly**, bit-for-bit: direct (aliased) Ward residuals `2.0151611240e-3 / 8.3825508732e-3 / 8.4706948205e-3 / 2.2323604358e-3 / 1.5986389343e-3`, and dealiased residuals all at `~1e-18`–`1e-19`, matching to full displayed precision at every grid.

## v15.1270 — a cheaper alternative, independently confirmed

Offers strict 2/3-rule band-limiting (a standard pseudospectral anti-aliasing technique) as a native-grid alternative to v15.1269's 2× oversampling: band-limit the *source* field to `|m_j|<N/3` before evolving, then check the Ward identity only within that retained band on the native grid. Explicitly reports the full (unretained) band still fails, as expected and not swept under the rug.

**Independently re-executed the actual committed script** (same five grids). Every value — retained-band residuals (`~1e-18`–`1e-19`) and full-band residuals (`8.2954864308e-4` through `1.08867991397e-4`) alike — matched the ledger's table exactly, bit-for-bit, at every grid.

## v15.1271 — scalar Ward generalized to full Maxwell stress four-divergence, independently confirmed

Generalizes the already-verified (v15.1269) scalar energy-continuity Ward identity to the full flat conformal Maxwell stress-energy conservation: `rho_dot+(√3/τ)∂_jF_j=0` (energy, the already-tested case) **and** `F_i_dot+(√3/τ)∂_jT_ij=0` (three momentum components, new), with `T_ij=ρδ_ij-E_iE_j-B_iB_j` the standard Maxwell stress tensor. By hand: `T_ij` is symmetric with `tr(T)=3ρ-(E·E+B·B)=3ρ-2ρ=ρ`, consistent with the ordinary flat-space Maxwell stress tensor; the momentum equation is the vector generalization of the already-confirmed scalar case using the same `cos(kξ)`/`sin(kξ)` analytic time-derivative evolution, transverse projector, and Nyquist-plane cleaning established in v15.1267/v15.1269 — no new field-evolution assumption is introduced.

The entry explicitly discloses that its quoted table came from a separately-authored local script (`/tmp/momentum_gate.py`), not yet from the newly-committed canonical reproducer (`k4_maxwell_four_stress_conservation_v15_1271.py`, committed at `cb56970`) — flagging itself as not yet independently Audited from committed bytes. **Independently re-executed the actual committed script** at all five grids (N=16/24/32/40/48), all three product conventions (native/full-1, 2×-padded/full-2, strict-2/3-band/cutoff-1). Every value matched the ledger's Gate 1219 table exactly, bit-for-bit:
- Native (aliased, expected-negative) energy/momentum residuals: `1.163454e-3/1.451467e-3` (N=16) through `9.229746e-4/2.251753e-4` (N=48) — all five grids matched exactly.
- 2×-padded (dealiased) energy/momentum residuals: `2.192e-19/5.216e-19` (N=16) through `2.270e-18/2.763e-18` (N=48) — all five grids matched exactly.
- 2/3-band retained-only energy/momentum residuals: `1.491e-19/1.636e-19` (N=16) through `1.748e-18/1.737e-18` (N=48) — all five grids matched exactly.
- The two cross-check ρ values quoted in prose also matched exactly: N=32 full-field `0.0007676608970155842` vs. two-thirds-band `0.000742165825182177`; N=48 `0.000778695424536061` vs. `0.0007764440607162524`.

The self-reported native-grid aliasing failure is genuine (matches the already-established v15.1267/v15.1269 Nyquist/aliasing pattern, now shown to extend to the momentum sector, not just energy), and both resolutions (2× oversampling, 2/3-band) are genuine passes, independently reproduced from the committed script rather than from the separately-authored local script the entry itself flagged as a stand-in.

## Verdict

**PASS (all six entries).** This round's self-correction loop (compose → fail → diagnose Nyquist bug → fix → discover a second, independent aliasing bug → fix two different ways → generalize the scalar Ward identity to the full stress four-divergence and confirm the same aliasing/fix pattern holds for momentum) is exactly the kind of honest, incremental numerical work this audit exists to check, and every claimed pass or failure was independently reproduced from the actual committed bytes, not taken on the entries' word or on a stand-in local script — including the three self-reported negative results, which were all genuine. The composition and stress-conservation checks remain explicitly scoped as algebraic consequences of Maxwell's equations and the Einstein trace equation for a declared periodic-cell model, not a full metric solution, constraint closure, or detector claim; nothing here asserts a new physical interaction.

## Collision and freshness checks

"Round 621" confirmed unused before this write. `v15.1271` collided with Gravity's own genuine use (resolved per the collision notes above by renumbering this entry to `v15.1272`, the next free slot); `v15.1272` confirmed unused. `__pycache__` cleaned before this commit; final freshness check performed immediately before push confirmed no intervening changes.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
