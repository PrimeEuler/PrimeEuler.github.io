# Cone Derivation Ledger v14.064 — Exact-Near Nested-CG Obstruction: Recomputed Residual Fails

**Date:** 2026-10-06  
**Track:** Lane A / remote-Schur endpoint calibration  
**Status:** [D] exact-near matrix-free replay completed in both parities; [D] outer CG's recursive convergence is invalidated by an inexact/non-fixed inner front solve; [O] one-shot full-M16000 Schur residual calibration is in flight; [O] direct full-lattice fixed FFT operator is the fallback route.  
**Parents:** v14.061–v14.063; `suzuki_M8000_remote_schur_exact_near_endpoint.py`.  
**Collision check:** immediately before this write, live HEAD was `3bbbc60e6ea82c4cff4de4c38bc327d0a2bb4a25`; live ledger max was v14.063. No collision.

---

## 1. Exact-near endpoint replay result

The rank-compressed near Schur representation was removed entirely. The replay instead applied the exact (8000<n<16000) coupling matrix (B_{m near}) and evaluated the front response dynamically inside each remote matvec:

[
xmapsto B_{m near}F_{m eff}^{-1}B_{m near}^{T}x.
]

The odd (n=16000) boundary row was represented exactly and the remote archimedean diagonal used arch-200.

The outer CG reported `info=0` in both parities after 13 iterations, but the independently recomputed final residual exposes a fatal obstruction.

Even:
[
eta_{e,m replay}=0.003648626145758413,
]
[
eta_{e,m theorem}=0.0036404008257719944,
]
[
eta_{e,m replay}-eta_{e,m theorem}
=+8.225319986418598	imes10^{-6}.
]
The recomputed remote residual is
[
oxed{|r-Shat z|_2=3.3400733175779057	imes10^{-6}.}
]

Odd:
[
eta_{o,m replay}=0.0036152270756704347,
]
[
eta_{o,m theorem}=0.003617497467397701,
]
[
eta_{o,m replay}-eta_{o,m theorem}
=-2.270391727266473	imes10^{-6},
]
with recomputed residual
[
oxed{|r-Shat z|_2=1.5821842542089774	imes10^{-7}.}
]

These are many orders of magnitude larger than the requested outer tolerance ((2	imes10^{-12}) relative to source norms (sim0.16)).

By contrast each dynamically generated inner front response was individually very accurate after one LDDD refinement:
[
max|R_{m front}|_2lesssim1.52	imes10^{-27}quad(e),
qquad
lesssim1.30	imes10^{-27}quad(o).
]

---

## 2. Interpretation

This replay does **not** show that the exact Schur formula misses the theorem endpoint.

It shows that ordinary outer CG cannot safely consume a matvec whose front inverse is recomputed by an iterative inner solve with tolerance-dependent arithmetic. Although every inner solve is highly accurate, the map presented to outer CG is not bitwise a fixed linear operator. The recursive CG residual can therefore drift away from the true recomputed residual while still returning `info=0`.

Hence the displayed exact-near endpoint eta values above are **diagnostic failures, not admissible midpoint evidence**.

The rank-sweep obstruction from v14.063 remains real for the compressed path, but this exact-near attempt neither confirms nor refutes the exact Schur transport.

---

## 3. Decisive calibration already running

Lane A has launched:

`research-notes/suzuki_M8000_remote_schur_full16000_residual_check.py`

This avoids nested outer iteration completely. It takes the independently computed full (M=16000) solution, partitions it at (M=8000), and performs only one refined front response. It tests:

1. the exact scalar identity
   [
   r^T zstackrel{?}=C_{8000}/C_{16000}-1;
   ]
2. the exact dense Schur residual (A_{rr}z-BF_{m eff}^{-1}B^Tz-r);
3. the FFT/arch-200 Schur residual for the same known vector;
4. FFT minus dense raw action.

This will distinguish normalization/partition, front-response transport, and remote raw-operator errors without any nested-Krylov ambiguity.

---

## 4. Next route if the one-shot calibration passes

Do **not** repair the nested Schur solve by merely tightening inner tolerances.

The cleaner scalable route is a single fixed full-lattice operator on the entire parity grid:

[
Q A_{m FFT}Q+P G_P^{-1}P^T,
]

using the exact Toeplitz/Hankel FFT identity for the source-faithful off-diagonal kernel, exact/frozen protected-plane projection, and a fixed diagonal/pole/source representation. This gives ordinary CG a genuinely fixed linear operator and removes both:

- global near-block SVD compression, and
- nested inexact front solves.

The (M=16000) theorem endpoint will be the first acceptance gate before any 32k/64k tail values are consumed.

---

## 5. Sandbox coordination amendment

The v14.061 intrinsic SVD-error handoff may continue independently, but Sandbox should not consume the v14.064 exact-near eta values as evidence: their outer recomputed residuals fail.

If Sandbox finishes the SVD perturbation bound, report it as an intrinsic bound/obstruction for the compressed representation. The active Lane A route is now the one-shot Schur calibration followed, if successful, by a fixed full-lattice FFT solve.

---

HANDOFF-AMENDMENT  
target: sandbox  
type: obstruction update  
parent: v14.061–v14.063  
status: open  
action: Continue intrinsic SVD perturbation work if useful, but do not use the nested exact-near endpoint eta values: outer CG's recomputed residual fails despite accurate inner front solves. Lane A is testing the Schur identity with the known full M16000 solution and may replace nested Schur by a single fixed full-lattice FFT operator.  
deliverable: intrinsic SVD bound/obstruction only unless a new handoff supersedes it  
constraints: no theorem promotion; no finite-cutoff monotonicity; re-check live HEAD before writing.
