# Gravity spectral diagonal / radial-seat bridge

Date: 2026-10-23 EDT

Status labels: **[D]** exact derived identity, **[I]** interpretation, **[G]** guardrail, **[O]** open physical step.

Parents: ledger v13.177, v13.301, v13.748, v13.770, v14.367, v14.550, v14.766-v14.767.

## 1. Separate the two logarithmic Cone coordinates

For positive factor coordinates (x,y), use the exact logarithmic Cone coordinates already established in v13.748:
[
r=log(xy),qquad eta=rac12lograc{x}{y}.
]
Here (r) is radial/scale and (eta) is boost/shape.

Let (h>0) be a uniform factor-grid unit and let a normalized product shell have integer index (n):
[
x=h a,qquad y=h b,qquad ab=n.
]
Then
[
xy=h^2n,
qquad
oxed{r_h(n)=log(h^2n)}.
]
A common dilation (hmapsto ch) changes (r) by (2log c), while the intrinsic boost coordinate (eta) is unchanged.

The row/column parabola vertices at factor level (h) are
[
oxed{X=pmrac h2}.
]

Thus:
[
h_{m EM}=1
quadLongrightarrowquad
r_{m EM}(n)=log n,qquad X_{m vert}=pmrac12,
]
whereas
[
h_{m G}=rac12
quadLongrightarrowquad
oxed{r_{m G}(n)=lograc n4},qquad
oxed{X_{m vert}=pmrac14}.
]

This is the exact distinction that was blurred when the earlier discussion used one rapidity symbol for both a factor-pair ratio and a scale comparison.

## 2. The old ((n,4)) hyperbola is exactly the radial coordinate of the half-scale grid

The pair encoding has
[
psi_{n,k}=rac12lograc nk.
]
For a grid unit (h), put
[
c=h^{-2}.
]
Then
[
r_h(n)=log(h^2n)=lograc nc
=2psi_{n,c}.
]
Therefore
[
oxed{r_h(n)=2psi_{n,h^{-2}}}.
]

For the proposed gravitational half-grid (h=1/2),
[
c=4,
]
so
[
oxed{
r_{m G}(n)
=
lograc n4
=
2psi_{n,4}.
}
]

This gives a precise interpretation of the earlier EM-to-G scale hyperbola: it is not the intrinsic boost of the scaled factor pair ((hn,h)), whose ratio is still (n). It is the **radial scale coordinate** of the shell, expressed as the pair rapidity between shell index (n) and the inverse-square grid scale (h^{-2}=4).

## 3. Independent spectral occurrence of the same radial origin

The Suzuki cusp calculation predates the present gravity-quarter discussion. v13.301 derives the exact diagonal
[
C_{nn}
=
lograc n4
-operatorname{Ci}(npi)
-rac{operatorname{Si}(npi)}{npi},
]
and its unbounded reference diagonal is
[
oxed{(D_{log})_{nn}=lograc n4}.
]

Hence
[
oxed{
(D_{log})_{nn}
=
r_{1/2}(n)
=
2psi_{n,4}.
}
]

This is stronger than noticing the same numeral 4 twice: the exact spectral logarithmic origin agrees with the exact Cone radial coordinate of the half-scale factor grid.

The equality is a coordinate identity. It does **not** identify the divisor summatory carrier with the Suzuki/Weil carrier; v13.770 explicitly rules out that stronger functional identification.

## 4. Spectral-denominator / factor-seat theorem

Consider an exact logarithmic spectral coordinate
[
Lambda_c(n)=lograc nc,
qquad c>0.
]
Require that it equal the radial coordinate of one uniform factor grid:
[
Lambda_c(n)=r_h(n)=log(h^2n)
]
for all (n>0).

Then necessarily
[
h^2=c^{-1},
qquad
oxed{h=c^{-1/2}}.
]
The corresponding row/column parabola vertices are therefore
[
oxed{
X_{m vert}=pmrac1{2sqrt c}.
}
]

For the Suzuki value (c=4),
[
oxed{
h=rac12,qquad
X_{m vert}=pmrac14.
}
]

Thus, once the unit EM grid (h=1) is fixed as the reference normalization, the exact spectral denominator (4) selects the half-scale factor grid uniquely within this uniform-grid family.

## 5. Power-map cocycle: the scale survives normalized power covariance

v14.767 uses the unit-preserving power map
[
mathcal P_{k,h}(x,y)
=
left(
h(x/h)^k,,
h(y/h)^k
ight),
]
which sends the normalized shell index
[
nmapsto n^k.
]

The radial coordinate transforms as
[
r_h(n^k)
=
log(h^2n^k).
]
Since
[
r_h(n)=log(h^2n),
]
one gets
[
oxed{
r_h(n^k)
=
k,r_h(n)
+
(k-1)log(h^{-2}).
}
]

For the EM unit grid (h=1), the affine term vanishes:
[
r_{m EM}(n^k)=k,r_{m EM}(n).
]

For the gravitational half-grid (h=1/2),
[
oxed{
r_{m G}(n^k)
=
k,r_{m G}(n)
+
(k-1)log4.
}
]

Equivalently, the Suzuki diagonal obeys
[
oxed{
Lambda(n^k)
=
kLambda(n)+(k-1)log4,
qquad
Lambda(n)=log(n/4).
}
]

The normalized power map therefore preserves shape but leaves an affine radial cocycle that remembers the selected scale origin. This is exactly the sort of non-dilation-invariant datum v14.767 said was missing.

## 6. Radial cutoffs and divisor counts

On an (h)-grid, a fixed radial cutoff
[
r_h(ab)le L
]
is equivalent to
[
h^2able e^L
quadLongleftrightarrowquad
able h^{-2}e^L.
]
Thus the complete normalized factor-lattice count below the radial cutoff is
[
oxed{
D_h(L)
=
D!left(leftlfloor h^{-2}e^Lightflooright).
}
]

For (h=1),
[
D_{m EM}(L)=D(lfloor e^Lfloor),
]
while for (h=1/2),
[
oxed{
D_{m G}(L)=D(lfloor4e^Lfloor).
}
]

This recovers v14.766-v14.767's factor-of-four count, but now the cutoff coordinate (L) has an independently fixed spectral normalization rather than being freely rescaled by hand.

**[G]** This still does not make the divisor count equal to a Suzuki trace or Weil current. It only shows that the same radial coordinate fixes the cutoff scale on both constructions.

## 7. What this does and does not select

**[D] Exact within the shared normalized Cone dictionary:**
- the Suzuki logarithmic diagonal is the half-grid Cone radial coordinate;
- denominator (4) uniquely corresponds to factor unit (1/2);
- factor unit (1/2) uniquely gives parabola vertices (pm1/4);
- the power map carries an affine ((k-1)log4) radial cocycle at that seat;
- a fixed radial cutoff produces the (D(4e^L)) half-grid count.

**[I] Physical interpretation:**
the old EM-to-G scale hyperbola is a plausible already-existing selector of the gravitational **radial seat**, rather than a new coupling potential.

**[G] Not derived:**
- Newton's (G);
- (alpha_G) or the observed EM/gravity hierarchy;
- equality of the divisor carrier and Suzuki/Weil carrier;
- a proof that the selected half-grid is the physical gravitational sector rather than a mathematically matched sector.

## 8. Next gate

The remaining physical question is narrower than v14.767 left it.

The radial origin no longer needs to be invented if the Suzuki/Cone scale identification is accepted:
[
oxed{r_{m selected}(n)=log(n/4).}
]

The next test should therefore ask whether an independently normalized physical action or observable evaluates differently on
[
r_{m EM}(n)=log n
]
and
[
r_{m G}(n)=log(n/4),
]
with the same intrinsic boost coordinate (eta).

That test can determine whether the selected radial seat becomes a coupling hierarchy, while preserving the v13.770 guardrail against equating unlike arithmetic carriers.
