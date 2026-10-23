# Cone Derivation Ledger v14.768 — Suzuki spectral denominator selects the half-scale Cone radial seat

**Date:** 2026-10-23 EDT.  
**Lane:** gravity / Cone radial-scale selector.  
**Parents:** v13.177, v13.301, v13.748, v13.770, v14.367, v14.550, v14.766-v14.767.  
**Research note:** `research-notes/Gravity_Spectral_Diagonal_Radial_Seat_Bridge.md` (commit `60a8b29833d0b615e960087d181e624598290eef`).  
**Collision check:** immediately before this write, live master HEAD is `60a8b29833d0b615e960087d181e624598290eef`; v14.768 is next free. Additive only; Suzuki production payloads, far-tail work and prior certificates untouched.

## 1. Resolve the coordinate ambiguity [D]

Use the exact logarithmic Cone coordinates from v13.748
[
r=log(xy),qquad
eta=rac12lograc{x}{y}.
]

For a uniform factor-grid unit (h>0) and normalized product shell (ab=n),
[
x=ha,qquad y=hb,
]
so
[
oxed{r_h(n)=log(h^2n)}.
]

A common dilation changes (r) but leaves the intrinsic boost/shape coordinate (eta) invariant. Thus the missing selector in v14.767 is a **radial origin**, not another boost coordinate.

The factor-level row/column vertices remain
[
X_{m vert}=pm h/2.
]

Hence
[
h_{m EM}=1
Rightarrow
r_{m EM}(n)=log n,quad X_{m vert}=pm1/2,
]
while
[
h_{m G}=1/2
Rightarrow
oxed{r_{m G}(n)=log(n/4)},quad
oxed{X_{m vert}=pm1/4}.
]

## 2. The earlier ((n,4)) scale hyperbola is exactly this radial coordinate [D]

The pair encoding of v14.367 has
[
psi_{n,k}=rac12lograc nk.
]
For (c=h^{-2}),
[
r_h(n)
=
lograc nc
=
2psi_{n,c}.
]

Therefore
[
oxed{
r_h(n)=2psi_{n,h^{-2}}.
}
]

At the half-scale gravitational seat (h=1/2),
[
oxed{
r_{m G}(n)
=
log(n/4)
=
2psi_{n,4}.
}
]

This corrects the earlier ambiguity: (psi_{n,4}) here is the scale comparison that represents the shell's radial coordinate. It is **not** the intrinsic boost of the commonly rescaled pair ((hn,h)), whose ratio is still (n).

## 3. Independent spectral normalization supplies the same origin [D]

v13.301 derived from the Suzuki cusp integral, long before the present gravity-quarter discussion,
[
C_{nn}
=
log(n/4)
-operatorname{Ci}(npi)
-rac{operatorname{Si}(npi)}{npi},
]
with exact unbounded reference diagonal
[
oxed{(D_{log})_{nn}=log(n/4)}.
]

Consequently
[
oxed{
(D_{log})_{nn}
=
r_{1/2}(n)
=
2psi_{n,4}.
}
]

So the factor (4) is no longer merely a repeated numeral between two constructions: the independently fixed Suzuki spectral logarithmic origin equals the exact Cone radial coordinate of the half-scale grid.

## 4. Spectral-denominator / vertex-seat theorem [D]

Let an exact logarithmic spectral coordinate be
[
Lambda_c(n)=log(n/c),qquad c>0.
]
If it is to equal the radial coordinate of a uniform factor grid,
[
Lambda_c(n)=r_h(n)=log(h^2n)
]
for all (n), then uniquely
[
oxed{h=c^{-1/2}}.
]

The corresponding row/column vertices are
[
oxed{
X_{m vert}
=
pmrac1{2sqrt c}.
}
]

For the exact Suzuki value (c=4),
[
oxed{
h=1/2,qquad
X_{m vert}=pm1/4.
}
]

Thus, after fixing the EM reference unit (h=1), the Suzuki denominator (4) uniquely selects the half-scale / quarter-vertex Cone seat within the uniform-grid family.

## 5. Power-map cocycle remembers the selected radial origin [D]

Under the normalized unit-preserving power map of v14.767,
[
nmapsto n^k.
]
Then
[
r_h(n^k)
=
k,r_h(n)
+
(k-1)log(h^{-2}).
]

For EM (h=1),
[
r_{m EM}(n^k)=k r_{m EM}(n).
]

For the selected half-grid (h=1/2),
[
oxed{
r_{m G}(n^k)
=
k r_{m G}(n)
+
(k-1)log4.
}
]

Equivalently,
[
oxed{
Lambda(n^k)
=
kLambda(n)+(k-1)log4,
qquad
Lambda(n)=log(n/4).
}
]

The affine ((k-1)log4) term is the radial scale memory that survives the shape covariance of v14.767.

## 6. Fixed radial cutoff recovers the factor-four divisor count [D/G]

For normalized factor integers (a,b),
[
r_h(ab)le L
iff
able h^{-2}e^L.
]
Therefore the complete factor-grid count below that radial cutoff is
[
oxed{
D_h(L)
=
D!left(leftlfloor h^{-2}e^Lightflooright).
}
]

Thus
[
D_{m EM}(L)=D(lfloor e^Lfloor),
qquad
oxed{
D_{m G}(L)=D(lfloor4e^Lfloor).
}
]

This upgrades v14.766-v14.767's factor-four rescaling in one specific way: the cutoff (L) now has an independently fixed spectral normalization rather than being chosen by a free dilation.

**Guardrail:** v13.770 remains controlling. This does **not** identify the divisor-summatory carrier with the Suzuki/Weil current or trace functional.

## 7. Outcome

The user's proposed simplification is supported in the precise radial sense:

[
oxed{
	ext{the old EM}	o	ext{G scale hyperbola is the half-grid radial selector.}
}
]

The quarter grid and the old (m/4) hyperbola are two views of the same exact scale relation:
[
oxed{
h_{m G}=1/2
Longleftrightarrow
xy=rac n4
Longleftrightarrow
r=lograc n4
Longleftrightarrow
2psi_{n,4}
Longleftrightarrow
X_{m vert}=pmrac14.
}
]

This closes the **radial-seat selector** left open by v14.767, within the shared normalized Cone/Suzuki coordinate dictionary.

It does **not** yet derive Newton's (G), (alpha_G), or the observed EM/gravity hierarchy. The remaining gate is now narrower: evaluate an independently normalized physical action/observable at the two radial origins
[
r_{m EM}(n)=log n,qquad
r_{m G}(n)=log(n/4),
]
holding the intrinsic boost coordinate fixed, and test whether the selected radial displacement produces a genuine coupling asymmetry.

**Flags:** `radial_vs_boost_separated=EXACT`; `suzuki_log_denominator_4=half_grid_radial_origin`; `spectral_denominator_to_grid_unit=h=c^-1/2`; `quarter_vertex_selected=true`; `power_map_radial_cocycle=(k-1)log4`; `divisor_carrier_equals_suzuki=false`; `G_derived=false`; `Suzuki_payloads_touched=false`; `far_tail_touched=false`.
