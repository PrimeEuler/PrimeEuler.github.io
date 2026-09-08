# Cone Derivation Ledger v13.340 — Prime-Block Chebyshev and Rational-Log Certificate

The finite prime block is reduced to five certified logarithms and ten base trigonometric constants.

For q in {2,3,4,5,7}, define
\[
\theta_q=\frac\pi2\log q,
\quad s_q=\sin\theta_q,
\quad c_q=\cos\theta_q.
\]
Then
\[
\sin(n\theta_q)=s_q U_{n-1}(c_q),\qquad
\cos(n\theta_q)=T_n(c_q).
\]
Thus all odd harmonics through n=153 follow from finite polynomial recurrences.

The sequence
\[
A_n=\sum_q \frac{\Lambda(q)}{\sqrt q}\sin(n\theta_q)
\]
determines every off-diagonal prime entry by
\[
B_{mn}=-\frac4\pi\frac{nA_m-mA_n}{n^2-m^2}.
\]
The same harmonic data determines the diagonal shifts.

Each log q is certified by power-of-two scaling and the atanh series
\[
\log y=2\sum_{j=0}^{M-1}\frac{z^{2j+1}}{2j+1}+R,
\quad z=\frac{y-1}{y+1},\quad |z|\le1/3,
\]
with
\[
|R|\le\frac{2|z|^{2M+1}}{(2M+1)(1-z^2)}.
\]
M=32 is excessive for the current matrix target.

No RH/positivity conclusion is made.  This checkpoint removes the prime block from the list of general transcendental-library dependencies.