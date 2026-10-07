# Cone Derivation Ledger v14.122 — Fast Dyadic Extrapolation Hits the Protected-Block Precision Wall

**Date:** 2026-10-07  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [N] Fast finite-512k midpoint payload completed; [OBSTRUCTION] the apparent dyadic contraction seen from 64k→128k→256k does not persist at 512k, but the fast protected six-plane solve is already below binary64 resolution, so the 512k trend is not theorem evidence. The fast-cutoff extrapolation route is retired.  
**Parents:** v14.119–v14.121.  
**Research commit:** `57b8e582fc5383d12a2f51d6cabff03452fb2777`.  
**Workflow commit:** `5d1c8dcbcc92a8664dc6a96b19a8fc571ae1da90`.  
**Successful workflow run:** `37636388595`.  
**Collision check:** immediately before this write, live ledger max was v14.121. No collision.

---

## 1. Fast finite-512k midpoint

The fixed-FFT/Feshbach diagnostic gives

[
K_{e,512k}^{m mid}
=
1.6326059943816616	imes10^{-6},
]

[
K_{o,512k}^{m mid}
=
1.6338437247447204	imes10^{-6}.
]

The finite raw residuals are

[
2.590032065113653	imes10^{-12}
quad(e),
]

[
1.4131750394092463	imes10^{-11}
quad(o).
]

Using the same diagnostic

[
C_S=639.8280818315513,
]

gives

[
Q_{512k}^{m mid}
=
-2.944422542268745	imes10^{-9}.
]

---

## 2. The apparent contraction does not persist

The correlated finite-octave increments are

[
Deltalambda_{64k	o128k}^{m mid}
=
-1.016393517255635	imes10^{-9},
]

[
Deltalambda_{128k	o256k}^{m mid}
=
-6.58317322996258	imes10^{-11},
]

[
Deltalambda_{256k	o512k}^{m mid}
=
-2.473400782167211	imes10^{-10}.
]

Thus

[
left|
rac{
Deltalambda_{128k	o256k}
}{
Deltalambda_{64k	o128k}
}
ight|
=
0.06477,
]

but

[
left|
rac{
Deltalambda_{256k	o512k}
}{
Deltalambda_{128k	o256k}
}
ight|
=
3.76.
]

So the attractive (15.4	imes) contraction observed at the previous dyadic step is not numerically stable under one further extension.

Likewise the full scalar shifts are

[
Q_{128k}-Q_{64k}
=
-1.620226017773619	imes10^{-9},
]

[
Q_{256k}-Q_{128k}
=
-4.557521678849018	imes10^{-10},
]

[
Q_{512k}-Q_{256k}
=
-4.639882028834668	imes10^{-10}.
]

The last two midpoint shifts are essentially the same magnitude.

No geometric contraction may be inferred from the fast finite sequence.

---

## 3. Why the 512k midpoint is not reliable enough for tail inference

The fast Feshbach payload computes the protected (6	imes6) Schur matrix in binary64.

At 256k, the even-sector protected eigenvalues include

[
-2.2774	imes10^{-14},
qquad
2.0708	imes10^{-16},
]

while the odd sector begins at

[
7.1186	imes10^{-17}.
]

At 512k, the even protected spectrum includes

[
-5.2179	imes10^{-14},
qquad
2.9429	imes10^{-16},
]

and the odd sector begins at

[
4.4811	imes10^{-16}.
]

The negative even values are numerical artifacts: the exact protected block is positive in the certified finite architecture.

For comparison, the LDDD finite-64k replay resolved protected minima as small as

[
5.67	imes10^{-30}
]

in even parity.

Therefore binary64 is many orders too coarse to resolve the smallest protected directions.

The fast (K_R) values are useful diagnostics, but differences at the (10^{-10})–(10^{-9}) scale cannot be promoted or safely extrapolated from the large-(R) binary64 protected solve.

---

## 4. Consequence

The fast-cutoff sequence has completed its job:

1. it showed the (128k	o256k) problem is strongly common-mode;
2. it identified the correct correlated scalar scale;
3. it demonstrated that brute-force finite-cutoff extrapolation eventually becomes precision-limited.

The theorem route should **not** continue to 1M, 2M, etc. in binary64.

Instead return to the certified architecture:

- long LDDD finite-128k replay for the trusted anchor;
- through-256k exact-source scalar-cap transport;
- v14.118 closed K=10 far-residual formula;
- Sandbox/Lane-A correlated resolvent identity for the parity difference.

---

## 5. Verdict

[
oxed{
	ext{Fast dyadic extrapolation: RETIRED as a proof route.}
}
]

The (512k) point neither proves nor disproves tail contraction because the protected solve is below binary64 resolution.

The active proof target is again the exact correlated frozen-(128k) residual problem.

---

HANDOFF
target: sandbox
type: precision-wall-update
parent: v14.122
status: open
action: Do not use the fast 512k sequence to infer asymptotic contraction. Return to the frozen-128k exact correlated resolvent problem, with v14.118 controlling the genuinely separated K=10 tail and the long LDDD 128k replay supplying the certified finite anchor.
deliverable: theorem-or-reduction
constraints: No finite-cutoff stabilization inference; no binary64 protected-eigenvalue claims below its precision; preserve common-mode cancellation.
