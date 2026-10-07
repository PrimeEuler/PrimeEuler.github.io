# Cone Derivation Ledger v14.129 — Analytic Cross-Octave Operator Cap Closes v14.128 Safety Constant

**Date:** 2026-10-07  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [D/N] Analytic same-parity cross-octave norm bound with deterministic finite source check; confirms the hard CROSS_CAP=128 used in v14.128 has >1.9x headroom on both active octaves.  
**Parents:** v14.128.  
**Research commit:** `4f85029faaf615062a8b81f8602aec9186721f84`.  
**Workflow commit:** `a5b95763007ae8d295539bba8e53d13d8d361718`.  
**Successful workflow run:** `37647911451`.  
**Collision check:** immediately before this write, live HEAD was `a5b95763007ae8d295539bba8e53d13d8d361718`; live ledger max was v14.128. No collision.

---

## 1. Cauchy/displacement cross block

On one parity lattice,

[
rac{2}{pi}rac{z_n m-nz_m}{n^2-m^2}
=
rac1pi
left[
rac{z_n-z_m}{n-m}
-
rac{z_n+z_m}{n+m}
ight].
]

For old modes (mle R) and new modes (R<nle2R), with same-parity spacing 2 and a deliberately conservative

[
|z|le Z_star=16,
]

[
|K_{nm}|
le
rac{2Z_star}{pi}
left(
rac1{|n-m|}
+
rac1{n+m}
ight).
]

Let (Mle R/2) be the number of old same-parity modes.

The worst difference-denominator sum is bounded by

[
rac12H_M
le
rac12(1+log M),
]

and the positive-sum denominator contributes at most (1/2).

Hence both the row-sum and column-sum norms obey

[
|K|_{infty},
|K|_1
le
rac{2Z_star}{pi}
left[
rac12(1+log M)+rac12
ight].
]

Therefore

[
|K|_2
le
sqrt{|K|_1|K|_infty}
]

with the same scalar bound.

---

## 2. Pole cross block

The pole term is rank one.

Using

[
|p_p(n)|
le
rac{4cosh(1/2)}{pi n},
qquad
|alpha_p|le2,
]

together with

[
sum_{nge1}rac1{n^2}
le
rac{pi^2}{6},
]

and the tail estimate

[
sum_{n>R}rac1{n^2}
le
rac2R,
]

gives an explicit analytic rank-one cross-block norm cap.

---

## 3. Deterministic replay

The producer also checks the actual source-faithful finite payload through (2R).

It finds

[
max_{nle256000}|z_n|_{m nominal}
=
7.1737092416771855,
]

well below the hard analytic allowance

[
16.
]

### (R=64000)

Cauchy/displacement cap:

[
63.017673116305964.
]

Pole cap:

[
0.029558311825293303.
]

Total:

[
oxed{
|B_{64	o128}|_2
<
63.047231428131255.
}
]

Against the v14.128 hard cap (128),

[
oxed{
	ext{headroom}=2.03022	imes.
}
]

### (R=128000)

Cauchy/displacement cap:

[
66.54784271874838.
]

Pole cap:

[
0.02090088273209141.
]

Total:

[
oxed{
|B_{128	o256}|_2
<
66.56874360148048.
}
]

Hence

[
oxed{
	ext{headroom}=1.92282	imes
}
]

under the same hard cap (128).

---

## 4. Consequence for v14.128

The only coarse transport constant used by the stressed Gram producer is therefore independently supported:

[
oxed{
|B_{R	o2R}|_2<128
qquad
(R=64k,128k).
}
]

Thus the v14.128 residual-to-Gram radii retain their intended conservative meaning.

The remaining open object is not the orthogonal leakage or the cross-octave transport constant.

It is solely the protected correlated term

[
DeltaLambda_parallel.
]

---

## 5. Verdict

[
oxed{
	ext{v14.128 CROSS_CAP=128 has >1.9x analytic headroom on both octaves.}
}
]

---

HANDOFF
target: external-audit
type: cross-octave-cap-audit
parent: v14.129
status: open
action: Independently verify the Toeplitz/Hankel row/column-sum bound, the rank-one pole estimate, and the deterministic source maximum. If confirmed, treat CROSS_CAP=128 in v14.128 as closed.
deliverable: theorem-or-correction
constraints: Preserve the same-parity spacing-2 sums; no numerical operator-norm estimate is needed.
