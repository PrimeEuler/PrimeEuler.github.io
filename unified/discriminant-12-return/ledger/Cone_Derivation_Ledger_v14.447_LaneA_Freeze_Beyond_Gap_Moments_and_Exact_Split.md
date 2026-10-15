# Cone Derivation Ledger v14.447 — Lane A freeze of beyond-gap moments and exact direct-middle/far split

**Timestamp:** 2026-10-15 11:05:58 EDT  
**Lane:** A (Cone/Suzuki)  
**Parent HEAD:** `98bd3d4dcd02a4aecdd5ec73af9fcc8a677528de`  
**Source instruction:** v14.446 HANDOFF / completed workflow run `38752704973`

## Receipt and exact freeze

The v14.446 two-sector workflow completed successfully. Lane A read and accepted that returned CI result and, in this same continuation, froze the exact certificates rather than treating the workflow status alone as a mathematical result.

| sector | artifact | ZIP SHA-256 | certificate SHA-256 | first tail mode | original seed start | maximum directed radius |
|---|---:|---|---|---:|---:|---|
| even-v | 11981533760 | `a5ca7303d3f6aed643e36847a42ae0b63a1f2adc6cda53b546935adf20af9828` | `4f127165733ab1e359661a7430cad76913ab1f23e842d3ddc41b8791021222ee` | 2080767 | 512001 | `2615/2923003274661805836407369665432566039311865085952` |
| odd-v | 11981114768 | `9e68af17680a598dda010ba248ff8783e05530b26f9a94a9494a58996535a084` | `d7f103b96a5e4f6b3888774fc430c840dc462433519dcb28420bbd8855da4d53` | 2080768 | 512002 | `2613/2923003274661805836407369665432566039311865085952` |

Each returned certificate reports all 85 inverse moments evaluated, 1736 oscillatory scalar values evaluated, 42 positive-V envelope checks, inclusion of the physical nonprime-pole odd-model errors exactly once, and every directed radius below `1e-40`. The exact JSON bytes and a hash manifest are frozen under `payloads/beyond_gap_inverse_moments_v14_447/`.

## Concrete next action executed: exact split contract

With compact index count `U = 1040383` and moment order `K = 42`, Lane A evaluated and froze the following integer split:

| sector | compact support last mode | direct-middle modes | row count | far first mode | support/far endpoint ratio |
|---|---:|---|---:|---:|---|
| even-v | 2080765 | 2080767 through 4161531 | 1040383 | 4161533 | `2080765/4161533 < 1/2` |
| odd-v | 2080766 | 2080768 through 4161532 | 1040383 | 4161534 | `1040383/2080767 < 1/2` |

The geometric power is `2K = 84`, with the common coarse upper factor `2^-84 = 1/19342813113834066795298816`. The executable contract and its exact JSON output are included in this checkpoint.

## Scope fence and next gate

This checkpoint certifies the returned inverse moments and the exact index split only. It does **not** evaluate the 1,040,383 direct-middle rows, a beyond-gap residual, a whole action, stationary-cone closure, or infinite-capacity closure. The original `C_S_32000`, the `3e-5` finite-plus-gap threshold, and all prior acceptance thresholds remain unchanged.

The next physical gate is to evaluate the direct-middle compact contribution and compose it with the unchanged seed actions and the fresh far-moment bound, charging v14.354 exactly once and source plus v14.403 fresh-lift transport exactly once. No beyond-gap acceptance claim is made before that composition is evaluated.

## HANDOFF — External Audit and Sandbox

Please replay the two frozen certificate hashes and the exact split contract. In particular, verify the first-tail starts, all-85 flags, directed-radius maxima, integer endpoints, and the two strict `< 1/2` endpoint inequalities. This handoff requests review only; no response is presumed.
