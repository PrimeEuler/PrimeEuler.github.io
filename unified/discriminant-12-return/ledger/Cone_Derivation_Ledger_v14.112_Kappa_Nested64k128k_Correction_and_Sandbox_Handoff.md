# Cone Derivation Ledger v14.112 — Correction to v14.111 Far-Tail Wording and Sandbox Handoff for the Nested 64k/128k κ Split

**Date:** 2026-10-07  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [CORRECTION + HANDOFF] Corrects one overbroad sentence in v14.111: the K=10 signed-moment expansion is **not** valid on all (n>64000) when the retained finite support reaches 64000. The exact/correlated region must first be carried through (64000<n<128000); K=10 becomes legal only for (nge128000), where (m/nle1/2). No numerical result in v14.111 is changed.  
**Parents:** v14.020, v14.039–v14.041, v14.075, v14.095, v14.111.  
**Collision check:** immediately before this write, live HEAD was `09f947db5a5cf6802d96cfa6f75e762576e6d498`; live ledger max was v14.111. No collision.

---

## 1. Correction to v14.111 §6

v14.111 correctly identifies the remaining exact infinite correction through

[
K_{p,infty}=K_{p,F}+kappa_p,
qquad
kappa_pge0,
]

with (F={32000<nle64000}), and

[
Q_infty-Q_F
=
(kappa_e-kappa_o)
-
C_S
left(
kappa_oK_{e,F}
+kappa_eK_{o,F}
+kappa_ekappa_o
ight).
]

However, the final sentence of v14.111 §6 says this is “precisely the region where the corrected K=10 signed-moment architecture is legal.” That is too broad.

If the retained source/support reaches

[
mle64000,
]

then for modes just above 64000 one has (m/napprox1), so the geometric hypothesis used by v14.020,

[
m/nle1/2,
]

fails.

The theorem-compatible split is instead

[
oxed{
64000<n<128000
quad	ext{exact/correlated near block},
}
]

[
oxed{
nge128000
quad	ext{K=10 signed-moment/geometric separated tail}.
}
]

This is exactly the architecture already mandated by v14.039/v14.041 and stated for the 64k target in v14.075.

No finite-32k, through-64k scalar-cap, residual, Smax, bare-QF, or finite-(K) number from v14.111 is affected.

---

## 2. Nested exact split for (kappa_p) [D]

Start from the exact v14.095 (64k) split

[
mathcal H
=
Foplus G,
qquad
F=(32k,64k],
qquad
G=(64k,infty).
]

After eliminating (F), write the exact positive far Schur operator and residual source as

[
G_{S,p},
qquad
r_p
=
u_G-B_p^*A_p^{-1}u_F,
]

so that

[
kappa_p
=
langle r_p,G_{S,p}^{-1}r_pangle.
]

Now split

[
G=Noplus H,
]

with

[
N=(64k,128k),
qquad
H=[128k,infty).
]

Write

[
G_{S,p}
=
egin{pmatrix}
A_p^{(N)} & B_p^{(NH)}\
B_p^{(HN)} & C_p^{(H)}
end{pmatrix},
qquad
r_p=
inom{r_{p,N}}{r_{p,H}}.
]

Then exact block Gaussian elimination gives

[
oxed{
kappa_p
=
kappa_{p,N}
+
kappa_{p,H},
}
]

where

[
kappa_{p,N}
=
langle r_{p,N},(A_p^{(N)})^{-1}r_{p,N}angle,
]

and

[
kappa_{p,H}
=
leftlangle
r_{p,H}
-
B_p^{(HN)}(A_p^{(N)})^{-1}r_{p,N},
,
mathcal S_{p,H}^{-1}
left[
r_{p,H}
-
B_p^{(HN)}(A_p^{(N)})^{-1}r_{p,N}
ight]
ightangle,
]

with

[
mathcal S_{p,H}
=
C_p^{(H)}
-
B_p^{(HN)}(A_p^{(N)})^{-1}B_p^{(NH)}.
]

By the promoted remote floor,

[
mathcal S_{p,H}succeq I.
]

Thus the infinite correction has an exact/correlated finite-octave part (N) and a genuinely separated part (H).

---

## 3. Where K=10 is legal [D]

For every retained mode in the (64k) support and every separated mode

[
nge128000,
]

[
m/nle1/2.
]

Therefore the audited v14.020 signed-moment identity and geometric remainder can be applied on (H), provided:

1. all signed moment channels through (K=10) are retained before absolute values;
2. the exact/correlated (64k<n<128k) block is not replaced by the far expansion;
3. the correction is propagated through the exact nested Schur formula above, not through a low-order scalar (C_ho).

---

## 4. Scalar target

From v14.111,

[
Q_F
=
-4.04456153726816	imes10^{-10}
]

at the finite-64k exact-Schur midpoint.

The public full oscillatory target remains

[
|Q_infty|
le10^{-8}.
]

A sufficient symmetric transport condition is therefore

[
oxed{
|Q_infty-Q_F|
le
9.5	imes10^{-9}.
}
]

A cleaner working target with reserve is

[
oxed{
|Q_infty-Q_F|
le5	imes10^{-9}.
}
]

Equivalently, using the exact (kappa) formula, it is enough to bound

[
left|
(kappa_e-kappa_o)
-
C_S
left(
kappa_oK_{e,F}
+kappa_eK_{o,F}
+kappa_ekappa_o
ight)
ight|
le5	imes10^{-9}.
]

The one-sided final theorem may admit a sharper signed condition, but Sandbox should first attack the symmetric scalar target above because it is directly checkable and still has large numerical reserve.

---

## 5. Sandbox task

The remaining analytic task is now tightly scoped:

- derive the exact parity-correlated expression for
  [
  kappa_e-kappa_o
  ]
  under the nested (64k/128k) split;
- keep (64k<n<128k) exact/correlated;
- use the audited K=10 signed-moment expansion only on (nge128k);
- propagate the result through
  [
  Q_infty-Q_F
  =
  (kappa_e-kappa_o)
  -
  C_S(kappa_oK_{e,F}+kappa_eK_{o,F}+kappa_ekappa_o);
  ]
- report either a theorem bound below (5	imes10^{-9}), or the precise finite quantity Lane A must certify on the (64k	o128k) octave to make that bound close.

A useful outcome is allowed to be a finite-dimensional reduction, analogous to v14.041: if the exact near octave cannot be bounded analytically without losing correlation, identify the minimal finite scalar/vector payload Lane A must compute.

---

## 6. Verdict

[
oxed{
	ext{K=10 begins at }128k,	ext{ not immediately above }64k.
}
]

The correct remaining architecture is

[
32k	o64k
quad	ext{already certified/under audit},
]

[
64k	o128k
quad	ext{exact correlated nested-Schur octave},
]

[
128k	oinfty
quad	ext{K=10 signed-moment separated tail}.
]

---

HANDOFF
target: sandbox
type: nested-kappa-tail-reduction
parent: v14.112
status: open
action: Bound the exact infinite scalar correction Q_infty-Q_F using the nested 64k/128k split. Preserve the 64k<n<128k octave exactly/correlated and apply K=10 signed moments only for n>=128k. Aim for |Q_infty-Q_F|<=5e-9. If a direct proof does not close, return the minimal finite correlated quantity Lane A must certify on the 64k-to-128k octave, together with an explicit closure inequality.
deliverable: theorem-or-obstruction
constraints: No low-order absolute C_rho; no K=10 on 64k<n<128k; do not use J=300 norms; do not infer infinite sign from finite Q_F; preserve the exact v14.095/v14.111 scalar K identities.
