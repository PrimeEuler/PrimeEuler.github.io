# Cone Derivation Ledger v14.119 — Frozen-128k Residual-Energy Shortcut Fails, Correlated Difference Lands on Target Scale

**Date:** 2026-10-07  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [N] Fast fixed-FFT/Feshbach midpoint payload completed in both parities; [O] the absolute residual-energy closure criterion from v14.117 fails by ~898x, so the program must use the parity-correlated fallback; [I] the raw residual-energy difference itself is already only 2.9183e-9, strongly supporting the correlated route. No theorem promotion.  
**Parents:** v14.116–v14.118.  
**Research commit:** `328a47893a277b410b337e1fce58b9f615ca3525`.  
**Workflow commit:** `fa8b9568a25c1c0fef0824bde76f9c0e59ac83f7`.  
**Successful workflow run:** `37635473798`.  
**Collision check:** immediately before this write, live HEAD was `ba498da6a8aac06bdf461e205de20ca118450038`; live ledger max was v14.118. No collision.

---

## 1. Purpose

v14.117 gave the sufficient absolute-energy criterion

[
E_e+E_o
=
|ho_{e,128k}|_2^2+|ho_{o,128k}|_2^2
le
4.96	imes10^{-9},
]

which would close the entire frozen-(128k) scalar correction without any further octave inverse.

The fast payload tests whether that cheap gate is numerically plausible before spending effort on outward certification.

---

## 2. Fast finite-(128k) Feshbach payload [N]

Using the fixed-FFT six-plane Feshbach architecture without the expensive dense LDDD refinement gives:

### even-v

[
K_{e,128k}^{m mid}
=
1.3107986553122965	imes10^{-6},
]

with finite raw residual

[
3.3626072574380274	imes10^{-12}.
]

### odd-v

[
K_{o,128k}^{m mid}
=
1.3117232138648390	imes10^{-6},
]

with finite raw residual

[
5.493740591722041	imes10^{-12}.
]

Using

[
C_S=639.8280818315513,
]

the finite-(128k) scalar midpoint is

[
oxed{
Q_{128k}^{m mid}
=
K_e-K_o-C_SK_oK_e
=
-2.024682171500376	imes10^{-9}.
}
]

Guardrail: this is a binary64/Feshbach midpoint diagnostic only; the long LDDD replay remains the certification path.

---

## 3. Frozen residual on (128k<nle256k) [N]

The reconstructed finite solution was padded by zero beyond (128k), and the source-faithful FFT operator was applied through (256k).

### even-v

[
|ho_{e,M}|_2
=
1.4915862497148218	imes10^{-3},
]

[
oxed{
E_{e,M}
=
|ho_{e,M}|_2^2
=
2.224829540338327	imes10^{-6}.
}
]

### odd-v

[
|ho_{o,M}|_2
=
1.4925641893306434	imes10^{-3},
]

[
oxed{
E_{o,M}
=
|ho_{o,M}|_2^2
=
2.227747859272241	imes10^{-6}.
}
]

Therefore

[
E_{e,M}+E_{o,M}
=
4.452577399610568	imes10^{-6}.
]

Against the v14.117 full infinite residual-energy budget,

[
4.96	imes10^{-9},
]

the near-octave energy alone is larger by

[
oxed{
897.7	imes.
}
]

Thus the v14.117 absolute-energy shortcut is numerically impossible and should be retired as the primary closure route.

---

## 4. Correlated difference is already on the required scale [N/I]

Although the individual residual energies are (10^{-6})-scale, their difference is

[
oxed{
E_{o,M}-E_{e,M}
=
2.918318933914138	imes10^{-9}.
}
]

Relative to the common mean energy, this is only

[
1.31	imes10^{-3}
]

((approx0.13%)).

This is exactly the common-mode cancellation pattern the project has repeatedly observed.

It also lands directly on the same few-(10^{-9}) scale as the v14.112/v14.114 scalar closure target.

No theorem is inferred from the raw energy difference, because

[
lambda_p
=
langleho_p,mathcal S_p^{-1}ho_pangle
]

contains the parity-dependent inverse operator, not merely the Euclidean residual norm.

But the result strongly supports the correlated fallback.

---

## 5. Next gate: exact correlated finite-(256k) Schur increment

The cheapest exact correlated octave payload is

[
oxed{
lambda_{p,M}^{m fin}
=
K_{p,256k}^{m fin}
-
K_{p,128k}^{m fin}.
}
]

This follows from block Gaussian elimination for the finite extension from (128k) to (256k).

Lane A has therefore launched a fast finite-(256k) paired-Schur replay.

The quantity of immediate interest is

[
Deltalambda_M^{m fin}
=
left(K_{e,256k}-K_{e,128k}ight)
-
left(K_{o,256k}-K_{o,128k}ight).
]

If this correlated increment is (lesssim) a few (10^{-9}), the (128k	o256k) octave is numerically compatible with closure and the remaining work is to bound the frozen-source (nge256k) tail via v14.118.

---

## 6. Verdict

[
oxed{
	ext{Absolute residual-energy closure: FAILS by }897.7	imes.
}
]

[
oxed{
E_{o,M}-E_{e,M}
=
2.9183	imes10^{-9},
}
]

so the failure is entirely common-mode.

The active route is now unequivocally the parity-correlated finite-Schur increment plus the v14.118 signed-moment far tail.

---

HANDOFF
target: sandbox
type: correlated-residual-obstruction-update
parent: v14.119
status: open
action: Retire v14.117's absolute-energy shortcut as the primary route. Consume the measured common-mode residual energies and focus on the exact correlated finite-Schur increment lambda_{p,M}=K_{p,256k}-K_{p,128k}, plus the v14.118 far-tail moment formula. Check whether any additional parity identity can bound the inverse-weighted difference more sharply than Euclidean energy difference alone.
deliverable: theorem-or-reduction
constraints: Do not infer lambda_e-lambda_o from E_e-E_o without accounting for the parity-dependent inverse operators; preserve exact correlation.
