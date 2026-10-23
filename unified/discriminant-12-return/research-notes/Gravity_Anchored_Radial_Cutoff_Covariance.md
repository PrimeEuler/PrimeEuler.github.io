# Gravity anchored radial-boundary / divisor-window covariance

Date: 2026-10-23. Lane: gravity. Parents: v13.770, v14.766–770. No Suzuki payload, far-tail, or certificate changes. All mathematics below concerns factor-pair counting; no identification with Weil/Suzuki spectral measures.

## Fixed geometric radial wall [D]

For each grid step \(h>0\), include ordered integer factor pairs \(a,b\ge1\), located at \(x=ha,y=hb\). With radial coordinate \(r=\log(xy)\), the counting function at one common geometric wall \(r\le L\) is
\[
N_h(L)=\#\{(a,b):ab\le h^{-2}e^L\}
=D(\lfloor h^{-2}e^L\rfloor),
\]
where \(D(N)=\sum_{n\le N}d(n)\), \(D(N)=0\) for \(N<1\).
For \(h=1\) (EM) and \(h=1/2\) (the gravity half-grid), exactly
\[
\boxed{N_G(L)-N_{\rm EM}(L)=D(\lfloor4e^L\rfloor)-D(\lfloor e^L\rfloor)}.
\]
For \(t=e^L\to\infty\), the classical Dirichlet hyperbola method gives
\[
D(\lfloor t\rfloor)=t\log t+(2\gamma-1)t+O(\sqrt t),
\]
hence
\[
\boxed{N_G(L)-N_{\rm EM}(L)
=t[3\log t+4\log4+3(2\gamma-1)]+O(\sqrt t)}
\]
and
\[
\boxed{N_G(L)/N_{\rm EM}(L)\longrightarrow4}.
\]
This factor-four limit is a *density of normalized factor pairs at equal geometric product-wall*, not a coupling ratio.

## Coordinate covariance and a no-go [D]

A passive global radial reparametrization \(r'=r+s\), accompanied by a transformed wall \(L'=L+s\), preserves each inequality \(r\le L\) and all counts. The common-wall ratio above is consequently coordinate invariant under simultaneous translation of geometry and detector.

But if the two sectors are free to choose *separate* wall origins, the apparent count contrast disappears:
\[
\boxed{N_{1/2}(L-\log4)=N_1(L)}.
\]
Indeed \(N_{1/2}(L-\log4)=D(\lfloor4e^{L-\log4}\rfloor)=D(\lfloor e^L\rfloor)\). Therefore comparison is not physical until there is one externally fixed reference/detector for the two sectors. Sharing the coordinate letter L alone does not prove shared operational calibration.

## Mellin/Laplace formulation [D]

For \(\Re s>1\), the normalized shell Dirichlet series is
\[
\sum_{n\ge1}d(n)(h^2n)^{-s}=h^{-2s}\zeta(s)^2.
\]
At fixed index-sector weight, the half-grid gives
\[
\boxed{Z_G(s)=4^s Z_{\rm EM}(s)}.
\]
This is the Laplace transform of the radial pair-counting atomic measure \(\sum d(n)\delta_{r_h(n)}\), and its multiplicative factor is exactly the transform of a translation by \(-\log4\); it is not a dynamical partition function. The logarithmic derivative satisfies
\[
-\frac{d}{ds}\log Z_G(s)
=-\frac{d}{ds}\log Z_{\rm EM}(s)-\log4,
\]
while all second and higher derivatives of \(\log Z\) with respect to s agree. Thus centered radial cumulants/shape fluctuations are identical under this pure translation, in line with v14.770's spectral-gap no-go.

## Boundary contract [O]

An actionable physical selector requires (i) one common calibrated radial/product wall, (ii) a derivation that EM and G truly populate these factor-pair shell measures, (iii) an independently normalized detector/action whose measured response depends on absolute \(r-L\), and (iv) a non-circular computation of a coupling-sensitive response after varying the regulator and wall. Absent (i)–(iv), factor four is a kinematic difference, not Newton's G.

Flags: common-wall count identity exact; asymptotic factor four exact; independently shifted walls erase contrast; Laplace translation exact; physical wall and G selector open.
