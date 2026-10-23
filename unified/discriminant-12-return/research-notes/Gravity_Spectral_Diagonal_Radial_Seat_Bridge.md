# Gravity spectral diagonal / radial-seat bridge

Date: 2026-10-23 EDT. Parents: v13.177, v13.301, v13.748, v13.770, v14.367, v14.550, v14.766–768. Formatting repaired after v14.769 external audit; claims unchanged.

## Exact Cone dictionary [D]

For \(x,y>0\),
\[
r=\log(xy),\qquad \beta=\frac12\log(x/y).
\]
A common dilation of both factors changes radial scale but not intrinsic boost. For a factor-grid step \(h\), write \(x=ha,y=hb\) with normalized shell \(ab=n\). Then
\[
r_h(n)=\log(h^2n),\qquad X_{\rm vertex}=\pm h/2.
\]
At \(h_{\rm EM}=1\), \(r_{\rm EM}=\log n\) and vertices are \(\pm1/2\). At \(h_{\rm G}=1/2\), \(r_{\rm G}=\log(n/4)\) and vertices are \(\pm1/4\).

## Earlier scale hyperbola [D]

With \(\psi_{n,k}=\frac12\log(n/k)\),
\[
\boxed{r_h(n)=2\psi_{n,h^{-2}}}.
\]
Thus the half-grid radial coordinate is \(r_{1/2}(n)=2\psi_{n,4}\). This must not be confused with the intrinsic pair boost of \((hn,h)\).

## Independently derived spectral logarithm [D]

The Suzuki cusp calculation in v13.301 gives
\[
C_{nn}=\log(n/4)-\operatorname{Ci}(n\pi)-\frac{\operatorname{Si}(n\pi)}{n\pi},
\]
and reference diagonal \(\Lambda(n)=\log(n/4)\). This matches \(r_{1/2}(n)\) exactly as a coordinate formula. The match does not establish that the Suzuki index and divisor shell carry the same physical or arithmetic spectral measure.

For a general logarithmic denominator \(c>0\), matching \(\log(n/c)=\log(h^2n)\) uniquely requires
\[
\boxed{h=c^{-1/2}},\qquad X_{\rm vertex}=\pm(2\sqrt c)^{-1}.
\]

## Power-map and radial cutoff [D]

The normalized power map sends \(n\mapsto n^k\), and
\[
\boxed{r_h(n^k)=k r_h(n)+(k-1)\log(h^{-2})}.
\]
For \(h=1/2\), the affine term is \((k-1)\log4\), while for \(h=1\) it vanishes. The shape coordinate does not detect this uniform change of scale.

Under fixed radial cutoff \(L\),
\[
D_h(L)=D(\lfloor h^{-2}e^L\rfloor),
\]
giving \(D(\lfloor e^L\rfloor)\) for the EM unit grid and \(D(\lfloor4e^L\rfloor)\) for the half-grid.

## Scope [I/O]

The repeated \(4\) is an exact cross-dictionary normalization match. Physical sector assignment and a coupling prediction require an independently normalized action, boundary condition, or observable. The divisor-current versus Suzuki/Weil-current nonidentity of v13.770 remains in force. No \(G\) derivation or Suzuki/far-tail payload modification is claimed.
