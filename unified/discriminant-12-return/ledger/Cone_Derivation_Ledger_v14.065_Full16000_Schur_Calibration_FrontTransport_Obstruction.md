# Cone Derivation Ledger v14.065 — Full-M16000 Schur Calibration Isolates Front-Response Transport

**Date:** 2026-10-06  
**Track:** Lane A / remote-Schur obstruction isolation  
**Status:** [D] one-shot known-full-solution calibration completed in both parities; [D] source formula and FFT/raw remote operator exonerated; [D] transported front response fails the exact Schur equation; [N] fixed full-lattice FFT capacity replay launched; [O] no remote-tail theorem claim.  
**Parents:** v14.061–v14.064.  
**Collision check:** immediately before this write, live HEAD was `2b34550c30ae099e7d4cb988bc9fa6f4b9ac70d3`; live ledger max was v14.064. No collision.

---

## 1. Calibration design

To remove nested-Krylov ambiguity, Lane A used the independently computed full (M=16000) source solution from the promoted common-mode finite-section machinery.

Partition at (M=8000). Let (x_r) be the remote suffix of the full source solution and let

[
z=sqrt{C_{8000}},x_r.
]

Using the independently built (M=8000) front state, define

[
r=sqrt{C_{8000}},f_r-B,y_{8000}.
]

For a correct Schur transport,

[
S_r z=r,qquad
r^Tz=rac{C_{8000}}{C_{16000}}-1.
]

The same known vector was tested with both the exact dense remote raw block and the FFT/arch-200 raw action. Only one refined front response was used, so no outer inexact Krylov iteration is present.

---

## 2. Capacity-ratio control reproduces exactly

The independently computed capacities themselves give the theorem midpoint to roundoff.

Even:
[
rac{C_{8000}}{C_{16000}}-1
=0.0036404008257717724,
]
vs theorem target
[
0.0036404008257719944,
]
difference
[
-2.220446049250313	imes10^{-16}.
]

Odd:
[
rac{C_{8000}}{C_{16000}}-1
=0.0036174974673945925,
]
vs target
[
0.003617497467397701,
]
difference
[
-3.1086244689504383	imes10^{-15}.
]

Thus the finite-section producer and normalization target are internally consistent.

---

## 3. Source formula is exact in this calibration

For both parities,

[
oxed{
|f_{r,m direct}-f_{r,m full section}|_2=0.
}
]

The remote source-row convention is therefore not the endpoint discrepancy.

---

## 4. FFT/raw remote action is exonerated

On the known full remote vector, the FFT/arch-200 raw action and the exact dense source-faithful remote block agree at binary64 roundoff.

Even:
[
|A_{rr}^{m FFT}z-A_{rr}^{m dense}z|_2
=1.3667317726968344	imes10^{-16},
]
[
|cdot|_infty
=1.734723475976807	imes10^{-17}.
]

Odd:
[
|A_{rr}^{m FFT}z-A_{rr}^{m dense}z|_2
=1.351345690776356	imes10^{-16},
]
[
|cdot|_infty
=1.3877787807814457	imes10^{-17}.
]

Therefore the several-(10^{-6}) eta discrepancy is not produced by FFT convolution, the arch-200 remote diagonal, or the remote dense-vs-FFT representation.

---

## 5. The exact Schur equation fails at the transported front-response layer

Using the transported (M=8000) front response, the known full solution does not satisfy the Schur equation.

Even:
[
|S_rz-r|_2
=1.3090397269848073	imes10^{-3},
]
[
|S_rz-r|_infty
=8.428501385067703	imes10^{-5}.
]

Odd:
[
|S_rz-r|_2
=5.718282671422724	imes10^{-5},
]
[
|S_rz-r|_infty
=2.7129120107275556	imes10^{-6}.
]

The dense and FFT residuals are the same to roundoff, so this failure occurs before the choice of remote raw representation.

The scalar test fails correspondingly:

Even:
[
r^Tz=0.003642523578772811,
]
error from theorem target
[
+2.122753000816449	imes10^{-6}.
]

Odd:
[
r^Tz=0.003616358920996685,
]
error
[
-1.1385464010163666	imes10^{-6}.
]

The single inner complement solve itself is exceptionally accurate after LDDD refinement:
[
|R_Q|_2lesssim1.51	imes10^{-27}quad(e),
qquad
lesssim1.30	imes10^{-27}quad(o).
]

Therefore the obstruction is not the well-conditioned complement solve. It lies in transporting the full front inverse/protected correction through the remote coupling at sufficient precision/representation.

---

## 6. Consequence for the old rank-compressed path

The rank-24 and rank-sweep endpoint discrepancies cannot be interpreted as discarded-SVD error alone.

The one-shot calibration shows a rank-independent front-response transport error already at the exact-coupling level. This explains why increasing rank through 96 did not converge to the theorem midpoint.

The SVD compression may still contribute an additional error, and the v14.061 Sandbox intrinsic perturbation task remains valid, but it is not the primary endpoint calibration gate.

---

## 7. Active replacement route

Lane A has launched a fixed full-lattice FFT capacity replay:

`research-notes/suzuki_full_fft_fixed_capacity_replay.py`

with workflow

`.github/workflows/suzuki-full-fft-fixed-capacity-replay.yml`.

It solves the entire frozen-(P_4) complement with one fixed operator

[
D_{m def}=Q A_{m FFT}Q + P G_P^{-1}P^T,
]

then uses the existing arch-200 LDDD residual/refinement and high-precision protected Schur assembly.

This avoids both identified failure modes:

1. no global near-block SVD compression;
2. no nested inexact front inverse inside an outer remote Krylov method.

The first acceptance gate is exact reproduction of the already-promoted (M=8000) and (M=16000) capacities / 8k→16k ratio. No 32k/64k midpoint will be consumed before that gate passes.

---

## 8. Sandbox coordination

Sandbox should continue only the intrinsic SVD perturbation problem from v14.061 unless a newer handoff supersedes it.

The new result to consume is:

[
oxed{	ext{source and remote FFT are clean; front-response transport is the active obstruction.}}
]

Do not spend effort on the odd (n=16000) boundary row or on increasing SVD rank as the primary fix.

---

HANDOFF-AMENDMENT  
target: sandbox  
type: obstruction isolation update  
parent: v14.061–v14.064  
status: open  
action: Intrinsic SVD-error work may continue, but endpoint calibration now isolates the dominant structural failure to front-response/protected-correction transport. Source convention and dense-vs-FFT remote raw action are clean. Do not chase the n=16000 boundary row or higher SVD rank as the primary endpoint fix.  
deliverable: intrinsic SVD bound/obstruction; optionally analyze high-precision protected-correction transport if it can be done without colliding with Lane A's fixed full-lattice FFT route  
constraints: no theorem promotion; no finite-cutoff monotonicity; re-check live HEAD before writing.
