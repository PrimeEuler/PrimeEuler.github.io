# Cone Derivation Ledger v14.118 — Closed K=10 Far-Residual Norm Formula from Frozen-128k Moments

**Date:** 2026-10-07  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [D] Exact signed-moment expansion and closed same-parity (ell^2) bound for the frozen-(128k) residual source on (nge256k), preserving the full leading (1/n) cancellation among source, pole, and (Z_0); [O] insert outward finite-source moments from the (128k) Feshbach solve.  
**Parents:** v14.020, v14.022, v14.114, v14.117.  
**Collision check:** immediately before this write, live HEAD was `fa8b9568a25c1c0fef0824bde76f9c0e59ac83f7`; live ledger max was v14.117. No collision.

---

## 1. Frozen residual on the separated tail

Freeze the finite source solution

[
x_p=S_{p,128k}^{-1}u_{128k}
]

on modes

[
mle R,qquad R=128000.
]

For a same-parity tail mode

[
nge2R=256000,
]

the residual source is

[
ho_p(n)
=
u_p(n)
-
rac{2}{pi}
sum_{mle R}
rac{z_n m-nz_m}{n^2-m^2}x_p(m)
-
alpha_p,p_p(n),P_p,
]

where

[
P_p=sum_{mle R}p_p(m)x_p(m),
]

[
alpha_e=2,qquad alpha_o=-2,
]

and

[
p_e(n)
=
rac{4cosh(1/2)}{pi n}
rac{1}{1+1/(pi^2n^2)},
]

[
p_o(n)
=
rac{4sinh(1/2)}{pi n}
rac{1}{1+1/(pi^2n^2)}.
]

The paired remote source is

[
u_e(n)=rac1n,
qquad
u_o(n)=rac1{n-1}.
]

---

## 2. K=10 signed-moment expansion [D]

Define

[
M_{2j+1}^{(p)}
=
sum_{mle R}
m^{2j+1}x_p(m),
]

[
Z_{2j}^{(p)}
=
sum_{mle R}
z_m m^{2j}x_p(m),
qquad
j=0,ldots,10.
]

For (nge2R),

[
rac{1}{n^2-m^2}
=
rac1{n^2}
sum_{j=0}^{10}
left(rac mnight)^{2j}
+
mathcal R_{10}(m,n).
]

Therefore the frozen Cauchy action is

[
rac{2}{pi}
left[
z_n
sum_{j=0}^{10}
rac{M_{2j+1}^{(p)}}{n^{2j+2}}
-
sum_{j=0}^{10}
rac{Z_{2j}^{(p)}}{n^{2j+1}}
ight]
+
R_{10,p}(n).
]

The geometric remainder satisfies the audited v14.020 bound

[
|R_{10,p}(n)|
le
rac{2}{pi}rac43
left[
rac{S^{z,p}_{22}}{n^{23}}
+
rac{Z_{max}S^p_{23}}{n^{24}}
ight],
]

with

[
S^{z,p}_{22}
=
sum_{mle R}|z_m|m^{22}|x_p(m)|,
]

[
S^p_{23}
=
sum_{mle R}m^{23}|x_p(m)|,
]

and the already-audited

[
Z_{max}=8.
]

No low-order absolute (C_ho) is introduced.

---

## 3. Preserve the dangerous (1/n) channel exactly [D]

Set

[
c=rac2pi.
]

Define

[
h_e=cosh(1/2),
qquad
h_o=sinh(1/2),
]

and

[
d_p
=
alpha_p
rac{4h_p}{pi}
P_p.
]

The source, pole, and (Z_0) terms have a common (1/n) asymptotic channel.

Define its exact frozen coefficient

[
oxed{
A_{1,p}
=
1+cZ_0^{(p)}-d_p.
}
]

This coefficient is **not** split by absolute values.

For the pole factor,

[
-rac{d_p}{n}
rac1{1+1/(pi^2n^2)}
=
-rac{d_p}{n}
+
rac{d_p}{n}
rac{1/(pi^2n^2)}{1+1/(pi^2n^2)}.
]

Hence its leftover after extracting the leading (1/n) term is bounded by

[
rac{|d_p|}{pi^2n^3}.
]

For odd parity,

[
rac1{n-1}
=
rac1n
+
rac1{n(n-1)},
]

so after extracting the common (1/n) source channel the exact source remainder is

[
r_{m src,o}(n)=rac1{n(n-1)}.
]

For even parity there is no source remainder.

Thus the catastrophic low-order triangle inequality is avoided: the common source/pole/(Z_0) channel is paid only through (|A_{1,p}|).

---

## 4. Closed same-parity (ell^2) bound [D]

For a parity lattice

[
n=n_0,n_0+2,n_0+4,ldots
]

and (q>1), define

[
Sigma_q(n_0)
:=
n_0^{-q}
+
rac{n_0^{-(q-1)}}{2(q-1)}.
]

Then

[
sum_{nge n_0, {m same parity}}n^{-q}
le
Sigma_q(n_0).
]

Take

[
n_0=
egin{cases}
256001,&e,\
256002,&o.
end{cases}
]

By Minkowski,

[
|ho_{p,T}|_2
le
B_{1,p}
+
B_{{m src},p}
+
B_{{m pole},p}
+
B_{Z,p}
+
B_{M,p}
+
B_{{m geom},p},
]

where

[
B_{1,p}
=
|A_{1,p}|
sqrt{Sigma_2(n_0)},
]

[
B_{{m src},e}=0,
]

and, since (nge n_0),

[
B_{{m src},o}
le
rac1{1-1/n_0}
sqrt{Sigma_4(n_0)}.
]

The pole correction is

[
B_{{m pole},p}
le
rac{|d_p|}{pi^2}
sqrt{Sigma_6(n_0)}.
]

The higher signed (Z)-channels satisfy

[
B_{Z,p}
le
c
sum_{j=1}^{10}
|Z_{2j}^{(p)}|
sqrt{Sigma_{4j+2}(n_0)}.
]

Using (|z_n|le8), the oscillatory (M)-channels satisfy

[
B_{M,p}
le
8c
sum_{j=0}^{10}
|M_{2j+1}^{(p)}|
sqrt{Sigma_{4j+4}(n_0)}.
]

Finally, with

[
A_p^{m geom}
=
crac43 S^{z,p}_{22},
]

[
B_p^{m geom}
=
crac43 Z_{max}S^p_{23},
]

the genuine K=10 remainder obeys

[
B_{{m geom},p}
le
sqrt{
2(A_p^{m geom})^2Sigma_{46}(n_0)
+
2(B_p^{m geom})^2Sigma_{48}(n_0)
}.
]

Therefore

[
oxed{
|ho_{p,T}|_2
le
B_{1,p}
+
B_{{m src},p}
+
B_{{m pole},p}
+
B_{Z,p}
+
B_{M,p}
+
B_{{m geom},p}.
}
	ag{1}
]

Squaring (1) gives the separated-tail energy input required by v14.117.

---

## 5. Full residual-energy closure interface

Let

[
E_{p,M}
=
|ho_{p,128k}|_{ell^2(128k<nle256k)}^2
]

be the exact/correlated near-octave residual energy.

Let

[
E_{p,T}
=
|ho_{p,T}|_2^2
]

be bounded by (1).

Then

[
E_p
=
E_{p,M}+E_{p,T}.
]

By v14.117, the entire infinite scalar correction closes if

[
oxed{
E_{e,M}
+
E_{o,M}
+
E_{e,T}
+
E_{o,T}
le
4.96	imes10^{-9}.
}
	ag{2}
]

Thus the infinite (nge256k) problem is reduced to finitely many frozen-source moments:

[
P_p,quad
Z_{0}^{(p)},ldots,Z_{20}^{(p)},quad
M_1^{(p)},ldots,M_{21}^{(p)},quad
S_{22}^{z,p},quad
S_{23}^p.
]

The active fast Lane-A producer already emits these quantities at midpoint scale.

---

## 6. What must be made outward

For theorem promotion, Lane A must outward-enclose:

1. the near residual energies (E_{p,M});
2. the leading cancellation coefficient (A_{1,p});
3. the signed moments (Z_{2j}^{(p)},M_{2j+1}^{(p)});
4. the absolute moments (S^{z,p}_{22},S^p_{23});
5. the finite pole moment (P_p).

The public through-256k scalar-cap replay already in flight supplies the exact-source scalar envelopes needed on the residual octave.

The long LDDD finite-128k replay supplies the certification path for the frozen finite solution.

---

## 7. Verdict

The separated tail no longer requires an infinite solve or sampling argument.

[
oxed{
nge256k
quadLongrightarrowquad
	ext{finite signed moments + closed power-tail sums}.
}
]

Combined with v14.117, the final infinite scalar problem has become a finite residual-energy certificate.

---

HANDOFF
target: sandbox
type: far-residual-moment-formula
parent: v14.118
status: open
action: Independently check the frozen residual expansion, especially the combined leading coefficient A1=1+(2/pi)Z0-d and the odd-source identity 1/(n-1)=1/n+1/[n(n-1)]. Confirm the Minkowski/power-tail bound and insert it into the v14.117 residual-energy closure architecture.
deliverable: theorem-or-correction
constraints: Preserve the leading 1/n cancellation before absolute values; K=10 only for n>=256k; no low-order absolute C_rho.
