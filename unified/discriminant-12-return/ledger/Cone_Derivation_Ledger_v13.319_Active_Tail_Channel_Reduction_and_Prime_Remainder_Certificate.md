# Cone Derivation Ledger v13.319

## Active-tail channel reduction and prime remainder certificate

This checkpoint continues v13.318 in the Suzuki/Weil a=1 even-v sector.

### 1. Prime leading channel and exact remainder

From v13.315, for odd core/tail modes m != n,

\[
(B_{\rm prime})_{mn}
=-\frac{4}{\pi}\frac{nA_m-mA_n}{n^2-m^2},
\qquad
A_j=\sum_{q\in\{2,3,4,5,7\}}\frac{\Lambda(q)}{\sqrt q}\sin\!\left(\frac{j\pi}{2}\log q\right).
\]

Subtract the fixed-core leading term \(-(4/\pi)A_m/n\). Then

\[
\boxed{
R^{(p)}_{mn}
=-\frac{4}{\pi}\frac{1}{1-m^2/n^2}
\left(
\frac{A_m m^2}{n^3}-\frac{mA_n}{n^2}
\right).
}
\]

Therefore for every fixed core mode m, \(R^{(p)}_{mn}=O(n^{-2})\). After projection onto any fixed finite active subspace, the remainder Hilbert-Schmidt norm is \(O(N^{-3/2})\).

For the first four high-precision core eigenvectors, an elementary infinite-tail estimate gives the following projected prime-remainder HS bounds:

- N=237: 0.00918274
- N=301: 0.00638854
- N=401: 0.00413888
- N=501: 0.00295714
- N=701: 0.00178222
- N=1001: 0.00104252

These are analytic-formula bounds evaluated in ordinary floating arithmetic, not interval-certified enclosures.

### 2. Cusp leading channel

Use the v13.301/v13.303 decomposition

\[
C_{\rm cusp}=D_{\log}-H_{\rm odd}+K_{\rm cusp},
\]

with

\[
(H_{\rm odd})_{mn}=\frac1{m+n},
\qquad
(K_{\rm cusp})_{mn}=-\frac{2}{\pi^2mn}+E_{mn}.
\]

For an active vector \(q^{(j)}\), the fixed-core to remote-tail cusp coupling has leading coefficient

\[
\boxed{
C_j
=-\sum_m q_m^{(j)}
-\frac{2}{\pi^2}\sum_m\frac{q_m^{(j)}}m.
}
\]

Numerically for the first four active eigenvectors,

\[
L\approx(1.34656338,-0.92266061,-0.71611530,-0.37050076),
\]

\[
C\approx(-0.60412382,0.53777673,0.63826016,0.74134455).
\]

The channel angle satisfies

\[
\cos\angle(L,C)\approx-0.88337937.
\]

Thus the prime and cusp leading channels are strongly aligned but not collinear. The leading active-tail geometry is consequently confined to a small channel space rather than behaving like a generic 4D correction.

The singular values of the 4x2 channel matrix [L C] are approximately

\[
2.16214201,\qquad 0.50090573.
\]

So the second channel is real but substantially weaker.

### 3. Structural consequence

The remote-tail active coupling should now be organized as

\[
\boxed{
\text{dominant rank-one prime channel}
\oplus
\text{secondary cusp channel}
\oplus
\text{lower-order remainders}
}
\]

rather than bounded by a scalar multiple of the 4x4 identity.

The prime remainder after rank-one subtraction is already certified to decay as \(N^{-3/2}\) in HS norm. The next target is to derive a comparable projected bound for the cusp remainder after subtracting its explicit leading channel, then incorporate the smooth archimedean remainder and favorable pole term without destroying the low-rank matrix structure.

### 4. Guardrails

- v13.314's earlier sign convention is superseded; all prime formulas here use the v13.315 formula independently checked by external audit round 17.
- The high-precision active basis is numerical, not interval-certified.
- No exact kernel, \(\lambda_1=0\), RH, or GRH conclusion is made.
- Tail channel reduction is a localization/model-reduction step only.

### Files

- `research-notes/suzuki_active_tail_channel_reduction.py`
