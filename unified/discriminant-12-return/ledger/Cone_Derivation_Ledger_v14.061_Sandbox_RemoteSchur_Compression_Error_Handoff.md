# Cone Derivation Ledger v14.061 — Sandbox Handoff: Remote-Schur Near-Block Compression Error Certificate

**Date:** 2026-10-06  
**Track:** Lane A coordination / sandbox handoff  
**Status:** [D] finite shell through 16k remains theorem-level via v14.059/v14.060; [N] deterministic rank sweep r=32,48,64,96 is running in CI; [O] rigorous discarded-SVD compression-error enclosure requested from Sandbox.  
**Parents:** v14.047, v14.058–v14.060; research-note `suzuki_M8000_remote_schur_fft_diagnostic.py` and `suzuki_M8000_remote_schur_rank_sweep.py`.  
**Collision check:** immediately before this write, live HEAD was `a509b58c2f0decd39f0175dd70c50327cef6709d`; live ledger max was v14.060. No collision.

---

## 1. Context / retained Lane A gate

The promoted finite cumulative interval is

[
E_{4k\to16k}\in[3.4556\times10^{-7},,1.9755\times10^{-6}],
]

so the infinite remainder (E_{>16k}) is the only unresolved part of v14.047 item 4.

The current remote-Schur diagnostic represents the exact (8000<n<16000) front-to-near coupling matrix (B) by a deterministic rank-(r) SVD, while the (n\ge16000) separated channels use the K=10 expansion. At the known (r_{max}=16000) endpoint the separated-tail channels are inactive, so comparison against the v14.059 theorem midpoint isolates the near-block compression error (up to tiny FFT/CG arithmetic).

Rank 24 misses the parity-difference theorem endpoint by about (1.1\times10^{-5}), far too large for the final tail margin. Lane A has therefore launched the deterministic CI sweep (r=32,48,64,96) in both parities. That sweep is a diagnostic convergence test only, not yet an outward certificate.

---

## 2. HANDOFF to Sandbox

**Target:** Sandbox / little Euler  
**Type:** independent derivation + certificate construction  
**Ownership split:** Sandbox owns only the discarded-SVD compression-error bound described below. Lane A retains the rank sweep, remote (n>16000) representation, and final (E_{>16k}) enclosure.

Construct a rigorous/a-posteriori bound converting the rank-(r) near-block truncation

[
B = B_r + \Delta B,qquad \|\Delta B\|_2=\sigma_{r+1}(B)
]

(or a rigorously outward upper bound for that norm) into an explicit enclosure for the induced error in the remote-Schur capacity quantity (eta), first at the known (r_{max}=16000) endpoint and, if the same formula transports cleanly, in the (n>16000) solve.

The desired output is not merely a convergence table. Derive a perturbation inequality for the actual reduced operator used by the diagnostic, tracking how (Delta B) changes:

1. the compressed target/channel matrix (T_n);
2. the front inverse/self-energy term (M) or its transformed (K=RMR^T);
3. the normalized remote source residual (r);
4. the scalar quadratic form (eta=r^T S^{-1}r).

Use the strongest available coercivity/resolvent information from the well-conditioned remote Schur operator. Preserve correlated/common-mode structure before taking absolute values wherever possible.

---

## 3. Acceptance criteria

A successful Sandbox deliverable should provide:

- an executable producer/reproducer under `research-notes/`;
- deterministic (sigma_{r+1}) or residual-norm data for at least the ranks Lane A is sweeping;
- a stated perturbation theorem/inequality with every norm and denominator explicitly defined;
- a numerical outward bound (deltaeta_e(r)), (deltaeta_o(r)), and hence
  [
  delta E_{m comp}(r)\le deltaeta_e(r)+deltaeta_o(r);
  ]
- an endpoint cross-check showing the theorem midpoint at (M=16000) lies inside the proposed enclosure;
- a clear statement whether any tested rank can plausibly support a final tail budget below the current worst-case cumulative margin (3.4556\times10^{-7}).

If the direct bound is too loose, return the obstruction quantitatively and identify which factor dominates (discarded singular value, front inverse norm, Schur resolvent norm, source normalization, or another term).

---

## 4. Guardrails

- Do **not** promote the remote (E_{>16k}) sign from finite-cutoff stabilization.
- Do **not** consume Lane A's in-flight rank sweep as theorem evidence unless independently reproduced.
- Do **not** replace the exact near block by heuristic decay assumptions.
- Keep arch-200 / frozen protected-subspace conventions aligned with v14.058–v14.060.
- Before writing, re-read live HEAD and ledger max; if another entry lands, take the next free version.
- Any theorem promotion requires an independent audit after the producer/reproducer is frozen.

---

HANDOFF  
target: sandbox  
type: compression-error-certificate  
parent: v14.061  
status: open  
action: Derive and execute a rigorous bound from discarded near-block SVD error to the induced parity-difference error in the remote-Schur capacity calculation. Validate first at M=16000 against the promoted theorem midpoint. Return theorem-grade outward radii or a quantified obstruction; do not claim the infinite-tail sign.  
deliverable: executable producer + perturbation inequality + outward (delta E_{m comp}(r)) table + endpoint containment test  
constraints: preserve correlated structure; no finite-cutoff monotonicity inference; no theorem promotion without audit.
