# Cone Derivation Ledger v13.341 — Cusp Si/Ci Laplace Remainder and Small-Mode Series Certificate

For odd x=nπ,
\[
\operatorname{Si}(x)=\frac\pi2+F(x),\qquad \operatorname{Ci}(x)=G(x),
\]
where
\[
F(x)=\int_0^\infty\frac{e^{-xt}}{1+t^2}\,dt,
\qquad
G(x)=\int_0^\infty\frac{t e^{-xt}}{1+t^2}\,dt.
\]
Finite division of 1/(1+t²) gives
\[
F=\sum_{j=0}^{M-1}(-1)^j\frac{(2j)!}{x^{2j+1}}+R_F,
\quad |R_F|\le\frac{(2M)!}{x^{2M+1}},
\]
\[
G=\sum_{j=0}^{M-1}(-1)^j\frac{(2j+1)!}{x^{2j+2}}+R_G,
\quad |R_G|\le\frac{(2M+1)!}{x^{2M+2}}.
\]
At n=9 the best modest truncation already gives a remainder about 2.54e-13; n=11 is about 4.23e-16.  Hence n>=9 is certified asymptotically with large margin.

For n=1,3,5,7 use the convergent entire series for Si and Ci.  Euler's constant is enclosed independently by Euler-Maclaurin at N=64, using rational harmonic numbers, log 64=6 log2, Bernoulli numbers, and an explicit remainder.

This permits a uniform Si/Ci scalar radius target 5e-13.  Off-diagonal cusp-entry propagation is damped by odd-mode spacing:
\[
|\delta C_{mn}|\le \frac{2\varepsilon}{\pi|m-n|}\le \frac{\varepsilon}{\pi}.
\]
The resulting full cusp-block operator radius can be targeted below about 4e-11.

No exact zero, positivity, λ1=0, RH, or GRH claim follows.