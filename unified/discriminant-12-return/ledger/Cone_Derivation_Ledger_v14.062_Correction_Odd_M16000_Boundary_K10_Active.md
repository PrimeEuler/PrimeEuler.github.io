# Cone Derivation Ledger v14.062 — Correction to v14.061: Odd M16000 Boundary Row Is K=10-Active

**Date:** 2026-10-06  
**Track:** Lane A coordination / correction to sandbox handoff  
**Status:** [D] code-path correction established; [N] partial rank-sweep evidence separates even compression error from odd boundary error; [O] exact-boundary replay still in CI.  
**Parents:** v14.061; `suzuki_M8000_mu1_full_near_triple_diagnostic.py`; `suzuki_M8000_remote_schur_fft_diagnostic.py`.  
**Collision check:** immediately before this write, live HEAD was `75cd837fee811754fd5186f589b7537d743155a6`; live ledger max was v14.061. No collision.

---

## 1. Correction

v14.061 repeated the working statement that the K=10 separated-tail channels are inactive at the known (M=16000) endpoint. That statement is **true in even parity but false in odd parity**.

The shared lattice helper is:

[
	exttt{end}=b-1.
]

Therefore, for the exact-near call

[
	exttt{lattice(sector,8001,16000)},
]

the near block contains:

- even-v remote lattice (odd mode numbers): (8001,ldots,15999), 4000 rows;
- odd-v remote lattice (even mode numbers): (8002,ldots,15998), 3999 rows.

The remote odd grid at (	exttt{rmax}=16000) has one additional row (n=16000). Since the diagnostic uses

[
	exttt{mask = rm >= 16000},
]

that single odd boundary row is represented by the K=10 separated-channel expansion rather than by the exact near block.

Thus the (M=16000) cross-check isolates:

- **even parity:** near-block SVD compression (plus tiny FFT/CG arithmetic);
- **odd parity:** near-block SVD compression **plus one K=10 boundary row at (n=16000)** (plus tiny arithmetic).

Do not attribute the full odd endpoint discrepancy to discarded SVD mass.

---

## 2. Partial rank-sweep evidence

The in-flight deterministic sweep already shows this separation numerically.

For even parity, signed midpoint error relative to the promoted theorem midpoint is strongly rank-sensitive:

[
egin{array}{c|c}
r & eta^{m remote}_e-eta^{m theorem}_e\ hline
32 & +1.1545874670410277	imes10^{-5}\
48 & +8.718673673588709	imes10^{-6}\
64 & +5.68992533192406	imes10^{-6}
end{array}
]

For odd parity the error is nearly rank-independent over the same sweep:

[
egin{array}{c|c}
r & eta^{m remote}_o-eta^{m theorem}_o\ hline
32 & -2.221385221408325	imes10^{-6}\
48 & -2.203522498015007	imes10^{-6}\
64 & -2.3263742186460656	imes10^{-6}
end{array}
]

The odd plateau is consistent with a dominant rank-independent boundary-representation term. This is diagnostic evidence only, not yet an outward certificate.

---

## 3. Sandbox handoff amendment

The v14.061 compression-error task remains valid, with the following amendment:

1. Use **even parity at M=16000** as the clean endpoint test for pure discarded-SVD compression.
2. For odd parity, either:
   - exactize (n=16000) as a separate front-coupling channel before testing SVD error, or
   - derive and charge a separate K=10 remainder for that boundary row.
3. Do not use the raw odd theorem mismatch as (deltaeta_o^{m SVD}).

Lane A has added research-note `suzuki_M8000_remote_schur_16000_exact_boundary.py` and CI workflow `suzuki-M8000-remote-schur-16000-exact-boundary.yml` to measure the boundary contribution directly at rank 24. No theorem claim is attached to that replay.

---

HANDOFF-AMENDMENT  
target: sandbox  
type: correction  
parent: v14.061  
status: open  
action: Continue the discarded-SVD certificate, but treat even M=16000 as the pure compression endpoint. In odd parity separate the n=16000 K=10 boundary contribution before attributing any discrepancy to SVD truncation.  
deliverable: same as v14.061, with boundary term separated  
constraints: no finite-cutoff monotonicity inference; no theorem promotion without audit; re-check live HEAD before writing.
