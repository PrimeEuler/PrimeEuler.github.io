# Cone Derivation Ledger v14.449 — Sandbox replay of the v14.447 beyond-gap moments freeze and exact split

**Timestamp:** 2026-10-15 (EDT)
**Lane:** Sandbox (our Lane B) — independent replay
**Parent:** v14.447 (Lane A freeze of beyond-gap moments and exact direct-middle/far split)
**Handoff answered:** v14.447 HANDOFF (External Audit and Sandbox replay of the frozen hashes and split contract)

## What was replayed

The frozen payload at `unified/discriminant-12-return/payloads/beyond_gap_inverse_moments_v14_447/` (both sector certificates, `return-manifest.json`, `split-contract.json`) was fetched fresh and replayed with sandbox code written for this check (63 discrete checks, exact integer/Fraction arithmetic where the contract is exact). No moments were re-evaluated from scratch and no direct-middle rows were computed; the scope is exactly the freeze and the split, as handed off.

## Results — all checks pass

**Frozen hashes.** SHA-256 of the freshly fetched certificate bytes equals the v14.447 table exactly, both sectors:

- even-v certificate `4f127165733ab1e359661a7430cad76913ab1f23e842d3ddc41b8791021222ee`
- odd-v certificate `d7f103b96a5e4f6b3888774fc430c840dc462433519dcb28420bbd8855da4d53`

The manifest's artifact ZIP hashes, certificate hashes, first-tail modes, and radius maxima all agree with the ledger entry; workflow run `38752704973`, conclusion success.

**Certificate contents.** Both sectors: first tail mode 2080767 (even) / 2080768 (odd); original seed first mode 512001 / 512002; `all_85_infinite_inverse_moments_evaluated` true with Ubar 42 + Vbar 42 + P_tail = 85; oscillatory scalar values 1736; positive-V envelope checks 42; physical nonprime-pole odd-model errors included exactly once; scope flags `whole_action_evaluated` and `infinite_capacity_tail_closed` false.

**Directed radii.** The reported maximum radius fraction equals the ledger entry in both sectors, and the maximum recomputed from each certificate's own 85 radius fields equals the reported maximum exactly: even `2615/2923003274661805836407369665432566039311865085952` ≈ 8.946e-46, odd `2613/2923003274661805836407369665432566039311865085952` ≈ 8.939e-46 — each strictly below 1e-40 in exact arithmetic.

**Split contract.** Recomputed from the index maps (even-v mode = 2i+1, odd-v mode = 2i+2): compact last index 1040382 (modes 2080765 / 2080766); direct-middle indices 1040383..2080765 → modes 2080767..4161531 (even) and 2080768..4161532 (odd), row count exactly 1,040,383 per sector from the index span; far first index 2080766 → modes 4161533 / 4161534. Contiguity holds at both seams. Endpoint ratios strict in exact arithmetic: even `2080765/4161533 < 1/2` (2·2080765 = 4161530 < 4161533), odd `1040383/2080767 < 1/2` (2·1040383 = 2080766 < 2080767). Geometric power 84 = 2K with K = 42; coarse factor `2^-84 = 1/19342813113834066795298816` exact. Split scope flags (`beyond_gap_residual_evaluated`, `direct_middle_rows_evaluated`, `whole_action_evaluated`) all false, matching the entry's scope fence.

## Verdict

The v14.447 freeze and split contract are confirmed as recorded: hashes byte-exact, certificate contents consistent, radius maxima internally recomputed and matched, split arithmetic exact. No defect found. This replay certifies the freeze and the split only; it evaluates no direct-middle rows, no beyond-gap residual, and no tail closure.

**HANDOFF v14.447 (sandbox arm): CLOSED.**
