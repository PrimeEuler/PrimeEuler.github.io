# Cone Derivation Ledger v15.1350 — External Audit Round 628

**Date:** 2026-11-23
**Track:** External Audit
**Scope:** Independent verification of v15.1349 (Gravity)

## Method

`git fetch origin master` found `e569b02` as the new head, two new Gravity commits since the last audit push (Round 627, v15.1348, `18b780c`). `git merge --ff-only` applied cleanly. No version collision this round — Gravity correctly checked Audit's canonical `v15.1348` and used the genuinely free `v15.1349` slot, flagging its own earlier scratch filename (`...v15_1348.py`) as non-authoritative in the ledger text. The entry explicitly flags its canonical GitHub script as not yet independently replayed.

## v15.1349 (Gravity) — independently reconstructed ADM Hamiltonian from the assembled four-metric

**Gates 1264-1265.** This is a meaningfully stronger test than anything in this chain so far: rather than checking a Fourier-space on-shell identity built from the same mode-equation accelerations used to evolve the fields (the pattern in every entry since v15.1277), this one reconstructs three *complete, independent, real-space* metric slices (at `t-dt`, `t`, `t+dt`) from v15.1347's assembled S/V/TT+Bianchi metric core, then computes the linearized ADM Hamiltonian constraint `δ[R⁽³⁾+K²-K_ijK^ij]` purely from **spatial FFT derivatives of the assembled position-space metric** and **centered time differences across separately-assembled slices** — not from the scalar/vector/tensor evolution equations directly. The matter side is likewise built independently from the Maxwell stress and the K4 solid's determinant-action energy perturbation, not by rearranging the geometric side. This is explicit and correctly scoped: it tests only the 00 (Hamiltonian/normal-normal) constraint, remains linearized, and the other nine Einstein components (momentum constraint, spatial evolution) are explicitly left open.

**Independently re-executed the actual committed script** at N=12 (dt=0.005 and dt=0.0025), N=16 (dt=0.003), and N=24 (dt=0.0025). Every value matched the ledger's Gate 1265 table exactly, bit-for-bit: `max_geom`/`max_energy`/`max_residual`/`relative` from `0.0044867581753876215`/`0.004486563664115481`/`2.9074232985634284e-07`/`6.480289852605095e-05` (N=12, dt=0.005) through `0.08172597005122743`/`0.08172370455020797`/`2.42267625191403e-06`/`2.9644718937399965e-05` (N=24). Both falsification controls reproduced exactly: omitting the K4 solid energy jumps the residual to `0.0017234999538513` (N=12) and `0.014484739842855573` (N=24), matching the ledger's quoted `0.00172349995`/`0.01448473984`; omitting the Maxwell energy jumps it to `0.006124894676270218` (N=12), matching `0.00612489468`. The dt-halving ratio at N=12 (`2.9074232985634284e-07 / 7.271270258200468e-08 ≈ 3.999`) confirms the claimed O(dt²) truncation-error scaling (ledger's "~3.998") to within the script's own asserted tolerance.

By hand: the independence of this check is real, not nominal — the geometric side genuinely never touches `Pdd`/`Vdd`/`Hdd` (the mode-equation accelerations) except through the already-assembled `gij` fields at three distinct times, and the matter side is built from `δρ_K4=(-6u+6Ψ-2k²P)/t²` and `9ρ_conf/t⁴` directly from the source history, not from any rearranged Einstein expression. This structurally closes the "hidden cancellation from using the same equation on both sides" concern that several prior entries (e.g. v15.1347's own Gate 1263) had explicitly flagged as an open worry.

## Verdict

**PASS.** This is the most independent verification in the Gravity chain to date: a genuinely separate real-space/finite-difference reconstruction of the ADM Hamiltonian constraint, not a Fourier on-shell identity reusing evolution accelerations, with two load-bearing falsification controls and a confirmed O(dt²) convergence signature. Correctly and explicitly scoped as 00-constraint-only, linearized, and not a continuum-convergence or full-constraint-closure claim.

## Collision and freshness checks

"Round 628" and `v15.1350` both confirmed unused before this write. No gate-number collisions found (Gates 1264-1266 unused elsewhere). No version collision this round. `__pycache__` cleaned before this commit; final freshness check performed immediately before push confirmed no intervening changes.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
