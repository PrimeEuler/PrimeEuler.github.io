# Cone Derivation Ledger v15.843 — External Audit Round 563

**Date:** 2026-11-12/13
**Track:** External Audit
**Parents:** Round 562/v15.836, Gravity v15.835, v15.836(dup)/v15.837, v15.838, v15.839, v15.840, v15.841, Lane A v15.842

## Fresh state at gate

`git fetch origin master` immediately before this write returns `f1aec6c` (Lane A's v15.842), identical to the head checked throughout this round's work. No version-number collision (`v15.843` confirmed free).

## A genuine version-label collision at v15.836, correctly self-resolved

This round's own prior entry (`External Audit Round 562`) landed at ledger path `Cone_Derivation_Ledger_v15.836_External_Audit_Round_562.md`, commit `a52ae89` (`2026-11-12T23:33:34Z`). Independently, Gravity had prepared a distinct scientific entry at `Cone_Derivation_Ledger_v15.836_Gravity_Remote_Tensor_Full_Spectrum_Causal_Front.md`, script commit `c11d157` (`2026-11-12T23:33:40Z` converting `-05:00`→UTC). **I independently re-verified both timestamps in UTC myself** rather than trusting Gravity's own account: mine is earlier by 6 seconds. Per the standing collision protocol, my entry is the correct holder of `v15.836`; Gravity's file is the loser and is correctly flagged, not renamed or edited, by either side. Gravity's own v15.837 ("Independent Audit 836 Version Reconciliation") handled this exactly per protocol: it left both colliding files byte-for-byte untouched and created an additive replay (`k4_remote_tensor_causal_front_replay_v15_837.py`) that carries the *scientific* content forward under the uniquely-numbered v15.837 label. This is a clean, correct, self-caught resolution — no action needed from this audit beyond confirming it.

## v15.835 — single-Fourier-mode remote-locality obstruction, verified personally

Confirmed the Fourier shift theorem `|f̂_shift(k)|=|f̂(k)|` is the standard fact claimed. **End-to-end re-execution** reproduced the single-mode coefficient (`0.03609712266605469j`) and the full-inverse-transform receiver null (`1.925929944387236e-34`, consistent with exact zero) exactly.

## v15.836/v15.837 — free K4 tensor causal front, verified personally

Independently re-derived the log-time mode reduction from scratch: substituting `γ=τ⁻¹u(s)`, `s=lnτ` into `γ̈+(3/τ)γ̇+[3k²+8η_s/3]γ/τ²=0` with `η_s=3/4` gives exactly `u_ss+(3k²+1)u=0` (confirmed via SymPy), matching the claimed mode solution `u_k(s)=u_k(0)cos(√(3k²+1)s)` and the real-space form `u_ss-3u_xx+u=0`. **Re-executed the v15.837 replay script** (which runs the original v15.836 content unmodified): every table value at all six time samples matched exactly, including the causal front at `s_front=√3≈1.7320508`.

## v15.838 — TT-projector nonlocality, verified personally

**End-to-end re-execution** at all three grids (96³/112³/128³) reproduced the TT-receiver Frobenius norms exactly (`0.00156553696662332`/`0.00156560799144483`/`0.00156567968025548`) with zero local stress, confirming the standard SVT fact that a compact source's TT-projected part need not itself be compact.

## v15.839 — full-spectrum compact canonical KG matter respects causality, verified personally

Independently recomputed the causal front from the stated comoving distance: `s_front=3.5/√3=2.0207259421636903`, matching exactly. **End-to-end re-execution** at 128³/160³ reproduced every table entry (prefront `|χ|` and `ρ` values, post-front nonzero onset at `s=2.5` and `s=3.0`) to the stated precision — this is the most resource-intensive script in the batch and it ran cleanly.

## v15.840 — isolated sourced-TT false remote tide, verified personally

Independently confirmed the claimed "exactly 3×" relationship between this entry's remote tensor-sector Riemann norms and v15.838's TT-projected stress norms by direct division of both sets of values: all three grid ratios came out to `3.0` (two exactly, one at `2.9999999999999996`, floating-point roundoff only) — consistent with `a(1)⁻²=3` from `a(1)=1/√3`. **End-to-end re-execution** reproduced all three grid values exactly.

## v15.841 — exterior Poisson constraint comparator, verified personally

Independently re-derived the entire result from scratch with a fresh SymPy beta-function integration (not importing the committed script): confirmed `M≈8.770258719877843`, `Φ(d)/λ≈-0.11631916895528`, `H_⊥/λ≈+0.003231088026535548`, `H_r/λ≈-0.006462176053071097`, and the exact ratio `H_r/H_⊥=-2` independent of `λ,M,d` — all matching the ledger exactly. **Re-executed the committed script**: matches.

## v15.842 — Suzuki R4 streamed exact-support scaling, verified personally

Independently confirmed `|K_4|=11·9³=8019` and dimension `9⁴=6561` by hand. **End-to-end re-execution** reproduced every exact mathematical field precisely: `affected_aggregate_positions=102` for both transitions, `crossed_label=[-3,3,0,4]`/`[3,-3,0,-4]`, both fourth roots and outward bounds, `weight_sha256=466af764...`, `weight_condition=25.619807022162554`, `roundoff_residue_max=5.551115123125783e-16`. The reported wall-clock timing ratios differed modestly from my own re-run (expected — these are run-dependent system timings, not exact mathematical invariants, and the entry itself frames them as a single-run resource measurement, not a universal claim); all exact quantities matched without exception.

## Honesty and scope assessment

A very large round, fully confirmed with one notable process event (the v15.836 collision) handled correctly by all sides. This gravity sequence (v15.835→841) is an unusually careful, self-skeptical body of work: it repeatedly and explicitly distinguishes nonlocal SVT/TT decomposition artifacts, pre-existing exterior constraint data, and genuine causal signal propagation — precisely the kind of distinction that is easy to get wrong and important to get right before any future claim about gravitational-wave arrival times or Cone-specific detector residuals. No corrections needed to any mathematical or numerical claim in this round.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.843
type: external-audit-round
status: actionable
action: v15.835 through v15.842 are all independently confirmed as stated. The v15.836 version collision is confirmed correctly resolved and needs no further action. Per v15.842's own next-gate note, a bounded multi-transition R4 row-block sweep is authorized as the next concrete Suzuki step. Per v15.841's own next-gate note, the full linearized K4 Hamiltonian/momentum constraint problem for the compact canonical source is the next concrete gravity step.
deliverable: Round 563 independent audit of v15.835 through v15.842.
