# Cone Derivation Ledger v13.321
## Archimedean channel, third active tail direction, and N^{-5/2} remainder

### Status
This checkpoint continues v13.320 in Suzuki's a=1 even-v sector.  It extracts the exact leading remote-tail channel of the smooth archimedean remainder and compares that channel with the exact prime and cusp channels from v13.318-v13.320.

Guardrail: this is a tail-structure reduction and numerical/high-precision audit.  It does not prove positivity, an exact zero mode, lambda_1=0, RH, or GRH.

## 1. Exact archimedean off-diagonal form
Let

\[
h(t)=r''(t)=\frac{e^{-t/2}}{1-e^{-2t}}-\frac1{2t},\qquad h(0)=\frac14.
\]

For odd Dirichlet modes define

\[
H_m=\int_0^2 h(t)\sin\!\left(\frac{m\pi t}{2}\right)dt.
\]

Using the exact shift entry from v13.315,

\[
(K_{\rm arch})_{mn}
=-\frac4\pi\frac{nH_m-mH_n}{n^2-m^2},\qquad m\ne n.
\]

Thus, for fixed core m and remote n,

\[
(K_{\rm arch})_{mn}
=-\frac4\pi\frac{H_m}{n}+R^{(a)}_{mn}.
\]

The active arch channel is therefore

\[
\boxed{T_j=-\frac4\pi\sum_{m\le19}q_m^{(j)}H_m.}
\]

## 2. Stronger arch remainder decay
From v13.311, h is positive and strictly decreasing on (0,2].  For odd n, integration by parts gives

\[
H_n=\frac{h(0)+h(2)}{k_n}+\frac1{k_n}\int_0^2 h'(t)\cos(k_nt)dt,
\qquad k_n=\frac{n\pi}{2}.
\]

Since \(\int_0^2|h'|=h(0)-h(2)\),

\[
|H_n|\le\frac{2h(0)}{k_n}=\frac1{\pi n}.
\]

Therefore

\[
\boxed{
|R^{(a)}_{mn}|
\le
\frac{4/\pi}{1-m^2/n^2}
\left(
\frac{|H_m|m^2}{n^3}+\frac{m}{\pi n^3}
\right).
}
\]

So the extracted arch remainder is \(O(n^{-3})\), and its fixed-active Hilbert-Schmidt tail is

\[
\boxed{O(N^{-5/2}).}
\]

Conservative active 4D remainder bounds:

- N=237: 5.77e-6
- N=301: 3.15e-6
- N=401: 1.53e-6
- N=501: 8.74e-7
- N=701: 3.76e-7
- N=1001: 1.54e-7

These are ordinary floating evaluations of analytic bounds, not interval enclosures.

## 3. Active arch channel geometry
The first four active components are approximately

\[
\boxed{T\approx(-0.2234203332,\ 0.1587790341,\ 0.1379919797,\ 0.1037910729).}
\]

For comparison, v13.320 has

\[
L\approx(1.3465633763,-0.9226606081,-0.7161152964,-0.3705007563),
\]

\[
S\approx(-0.5852224134,0.5265860837,0.6307779422,0.7374339543).
\]

Least-squares projection of T to span{L,S} gives coefficients approximately

\[
(-0.13336946,\ 0.07131754),
\]

with transverse norm about

\[
4.14468\times10^{-3},
\]

only about 1.2794% of \(\|T\|\).

The singular values of the 4x3 channel matrix [L S T] are approximately

\[
\boxed{2.17382638,\quad0.50546923,\quad0.00409808.}
\]

Hence the arch term creates a genuinely third active channel, but it is extremely weak relative to the first two.

## 4. One fully protected active direction
Since [L S T] has rank three, the four-dimensional active space contains a one-dimensional line orthogonal to all three leading 1/n channels.

A numerical unit vector in active-eigenvector coordinates is

\[
\boxed{p\approx(-0.23116867,-0.73865405,0.60819101,-0.17622408).}
\]

On this line:

- prime leading 1/n channel vanishes exactly by construction;
- cusp leading 1/n channel vanishes exactly by construction;
- arch leading 1/n channel vanishes exactly by construction;
- prime and cusp remainders are O(N^{-3/2}) in tail norm;
- arch remainder is O(N^{-5/2}).

This is the first active direction protected from all three extracted adverse remote-tail channels.

## 5. Pole term
In the even-v sector the pole form remains

\[
Q_{\rm pole}(v)=2|\langle v,\cosh(x/2)\rangle|^2\ge0.
\]

For lower-bound purposes it can be retained as a positive term rather than treated as an adverse tail channel.  No negative Schur penalty is assigned to it here.

## 6. Interpretation
The four-dimensional active tail geometry is now organized as

\[
\operatorname{span}\{L,S,T\}\oplus\mathcal P_1,
\]

where the third singular value is tiny.  Thus the full adverse remote-tail coupling is effectively two strong channels plus one weak channel, leaving one fully protected active line.

This does not establish an exact kernel or positivity.  It gives a substantially sharper matrix geometry for the next Feshbach reduction.

## Files
- `research-notes/suzuki_arch_channel_and_third_tail_direction.py`
