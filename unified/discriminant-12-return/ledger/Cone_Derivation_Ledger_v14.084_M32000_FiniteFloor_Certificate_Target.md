# Cone Derivation Ledger v14.084 — M32000 Finite-Section Floor Certificate Target and Outward 32k Sign Flip

**Date:** 2026-10-06  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [D] two-stage complement/Feshbach floor reduction; [N-cert target] 32k graph shear and pre-cancellation protected magnitude; [N-cert target] conservative outward budget gives \(\mu_{e,32k}>8.13\times10^{-31}\), \(\mu_{o,32k}>1.28\times10^{-26}\); [I] the v14.080 operator-radius obstruction would close and the 4k→32k cumulative interval would be strictly negative if the public padding caps below survive independent audit; **NOT PROMOTED pending audit.**  
**Parents:** v14.029–v14.034, v14.044–v14.045, v14.071, v14.075–v14.083.  
**Research commits:** \`fb4b7ef47817a5c044809f2e6ca993c9f0df9631\`, \`08b83556fd2f1967397e19a95ab97cd4036de35a\`, \`fd5d3b4401c4f988a72224feebb5c917e2663f7c\`, \`ad31a741ba3050911f03ca471426a2b698a62fa1\`.  
**Workflow commits:** \`5d45f97415a135df43143a52b5aefde4b36ce3bb\`, \`21060637bd1a86d65b4bfb477d39433555331733\`.  
**Collision check:** immediately before this write, live HEAD was \`21060637bd1a86d65b4bfb477d39433555331733\`; live ledger max was v14.083. No collision.

---

## 1. Target from v14.080

Sandbox v14.080 reduced the failed 16k→32k radius transport to one missing finite primitive:

\[
\mu_{32k}=\lambda_{\min}(A_{p,\le 32000})
\]

in coefficient-space Euclidean norm.

Its binary-search acceptance threshold is

\[
\theta_{e,32k}<1.174454\times10^{-5},
\]

and, at the current scalar/operator error scale, a floor of order

\[
\mu_{e,32k}\gtrsim1.2\times10^{-31}
\]

is sufficient.

This entry constructs a conservative certificate target for that floor using the same frozen six-plane and graph/Feshbach architecture as v14.034, but avoids a dense 16000-dimensional Cholesky.

---

## 2. Exact graph congruence and shear factor [D]

Split the 32k finite section into the frozen protected six-plane \(P\) and its Euclidean complement \(Q\):

\[
A_{32k}=
\begin{pmatrix}
A_{PP}&A_{PQ}\\
A_{QP}&C_{32k}
\end{pmatrix}.
\]

Let

\[
Y=C_{32k}^{-1}A_{QP},
\qquad
S=A_{PP}-A_{PQ}C_{32k}^{-1}A_{QP}.
\]

Then the exact block factorization is a unit-triangular congruence

\[
A_{32k}=T^*
\begin{pmatrix}
S&0\\
0&C_{32k}
\end{pmatrix}
T.
\]

For \(\tau=\|Y\|_2\), the worst two-dimensional singular value of the unit triangular shear is

\[
\sigma_{\min}(T)
\ge
\frac{2}{\sqrt{\tau^2+4}+\tau}.
\]

Therefore

\[
\boxed{
\lambda_{\min}(A_{32k})
\ge
\min\{\lambda_{\min}(S),\lambda_{\min}(C_{32k})\}
\left(
\frac{2}{\sqrt{\tau^2+4}+\tau}
\right)^2.
}
\tag{1}
\]

This is the only conversion needed from the protected Schur floor to the global finite-section floor.

---

## 3. Coarse 32k complement floor without a 16k Cholesky [D]

Let \(Q_8\) be the frozen-\(P\) complement in modes through 8000 and let \(H\) denote modes \(8000<n\le32000\).

v14.029/v14.031 prove, for the shifted M=8000 front,

\[
F_{QQ}^{(e)}\succeq\delta_e I,
\qquad
\delta_e=7.795385618610192746\times10^{-6},
\]

\[
F_{QQ}^{(o)}\succeq\delta_o I,
\qquad
\delta_o=3.262507025086259604\times10^{-5}.
\]

The unshifted \(Q_8\) block is larger, hence also \(\succeq\delta_p I\).

Now write the 32k frozen-\(P\) complement as

\[
C_{32k}=
\begin{pmatrix}
C_8&B\\
B^*&D
\end{pmatrix}.
\]

After eliminating \(Q_8\), its shell Schur complement is **larger** than the shell obtained after also eliminating the protected finite directions. The latter is the principal compression of the exact remote operator \(S_{p,8000}\), and v14.071 gives

\[
S_{p,8000}\succeq I.
\]

Thus the partial shell Schur complement is \(\succeq I\).

A public cross-block norm cap

\[
\boxed{\|B\|_2\le40}
\tag{2}
\]

is sufficient. It follows conservatively from the source-faithful kernel with \(|z_n|<10\): on the same-parity lattice the displacement cross-block has row/column harmonic sums below the \(31.9/28.7\) scale, hence spectral norm below about 30.3, while the even pole cross-block is below 5.1 (odd is smaller). The round cap 40 leaves additional slack.

Applying the same unit-triangular factorization with

\[
\tau_Q\le \frac{40}{\delta_p}
\]

gives the deliberately coarse floors

\[
\boxed{
\lambda_{\min}(C_{32k}^{(e)})
>
2.9606892578456869\times10^{-19},
}
\]

\[
\boxed{
\lambda_{\min}(C_{32k}^{(o)})
>
2.1703730290087791\times10^{-17}.
}
\tag{3}
\]

These are many orders above the protected \(10^{-30}\) / \(10^{-26}\) scales, so the final finite-section floor is protected-block limited.

---

## 4. 32k graph/shear diagnostic [N-cert target]

The calibrated fixed full-lattice FFT operator solved the six graph columns

\[
(QA_{32k}Q)Y=QA_{32k}P.
\]

The measured shears are

\[
\|Y_e\|_2=0.03635979038096641,
\]

\[
\|Y_o\|_2=0.09601786333514434.
\]

The frozen graph matrices remain small:

\[
\|W_e\|_F^2=6.001322761658969,
\qquad
\|W_o\|_F^2=6.009269878833603.
\]

We therefore propose the public outward caps

\[
\boxed{\tau_e\le0.04,\qquad \tau_o\le0.11,\qquad \|W_p\|_F^2\le8.}
\tag{4}
\]

The represented binary graph-solve residuals are already \(<1.5\times10^{-15}\), while the arch-200 LDDD replay after refinement gives protected/source joint residual maxima

\[
6.28414475481085\times10^{-26}\quad(e),
\]

\[
1.435106127025862\times10^{-26}\quad(o).
\]

For the outward target we use the much looser per-column cap

\[
\boxed{\|R_j\|_2\le10^{-25}\qquad(j=1,\ldots,6).}
\tag{5}
\]

With (3), the exact-graph correction then satisfies

\[
\|R\|_2^2/\gamma_Q
\le
6\times10^{-50}/\gamma_Q.
\]

---

## 5. Scalar/operator radius through 32k [N-cert/D]

The incremental arch-200 scalar interval replay on \(16000<n\le32000\) found only one failure of the old through-16k caps:

\[
\epsilon_{z,e}^{\rm ext}
=
5.877332881956699\times10^{-39}
\]

versus the previous cap \(5.862773801458821\times10^{-39}\), a roughly 0.25% increase.

All even diagonal/pole caps pass unchanged; all odd caps pass unchanged.

Use the widened public cap

\[
\boxed{\epsilon_{z,e}\le5.88\times10^{-39}.}
\]

Applying the same v14.034 Schur-row scalar-to-operator estimate, now with \(H_{15999}<11\), gives

\[
\boxed{
\epsilon_{A,e}^{32k}
=
1.0914650487773005\times10^{-36},
}
\]

\[
\boxed{
\epsilon_{A,o}^{32k}
=
8.786870658639323\times10^{-38}.
}
\tag{6}
\]

With \(\|W\|_F^2\le8\), the exact-source protected-form charge is negligible compared with the rounding charge.

---

## 6. Pre-cancellation LDDD magnitude and conservative rounding cap [N-cert target]

The 32k positive pre-cancellation component replay gives

\[
Q_{{\rm comp},e}^{\rm mid}
=
6.831462611825017,
\]

\[
Q_{{\rm comp},o}^{\rm mid}
=
2.4199994307658286.
\]

These are essentially unchanged from the old M=8000 values.

Use the public cap

\[
\boxed{Q_{\rm comp}\le12.}
\tag{7}
\]

For the LDDD arithmetic envelope, use

\[
\boxed{C_{\rm DD}=8192}
\]

rather than 4096. This deliberately resolves the old audit transparency caveat that the literal combinatorial product displayed around v14.034 could be read as 8192. With \(N=16000\), \(u=2^{-64}\),

\[
E_{\rm DD}
\le
8192\cdot16000\cdot u^2\cdot12
=
\boxed{
4.6222318665293660\times10^{-30}.
}
\tag{8}
\]

The actual even \(Q_{\rm comp}\) is only 56.9% of the public cap.

---

## 7. Protected outward target [N-cert target]

The completed full arch-200/LDDD 32k replay gives protected variational minima

\[
s_{e,\rm mid}
=
5.6712681659491925661\times10^{-30},
\]

\[
s_{o,\rm mid}
=
1.4295909196387792208\times10^{-26}.
\]

Subtract:

1. exact-source protected-form radius from (6) and \(\|W\|_F^2\le8\);
2. the conservative LDDD charge (8);
3. the exact-graph residual charge from (3),(5).

This gives the certificate targets

\[
\boxed{
s_{e,\rm out}
>
8.4637205482856398\times10^{-31},
}
\]

\[
\boxed{
s_{o,\rm out}
>
1.4291284199316580\times10^{-26}.
}
\tag{9}
\]

No theorem is claimed here until the public caps (2),(4),(5),(7),(8) are independently audited.

---

## 8. Global finite-section floor target [N-cert target]

Using (1), (4), and (9),

\[
\boxed{
\mu_{e,32k}
>
8.1318749997980791\times10^{-31},
}
\]

\[
\boxed{
\mu_{o,32k}
>
1.2803329289819406\times10^{-26}.
}
\tag{10}
\]

The difficult even floor has

\[
\boxed{
\mu_{e,32k}/(1.2\times10^{-31})>6.7765.
}
\]

Thus the v14.080 target has nearly sevenfold outward headroom even under \(C_{\rm DD}=8192\).

---

## 9. Consequence for the 16k→32k operator radius and shell [I, pending audit]

Using the exact perturbation consumer

\[
\theta=\frac{\epsilon_A}{\mu-\epsilon_A},
\]

the candidate floors give

\[
\boxed{
\theta_{e,32k}
<
1.3422076873749061\times10^{-6},
}
\]

\[
\boxed{
\theta_{o,32k}
<
6.8629576415616564\times10^{-12}.
}
\]

The difficult even value is only about 11.4% of Sandbox v14.080's maximum admissible

\[
1.174454\times10^{-5}.
\]

Feeding these values into the already-audited v14.080 coarse-shell formula with \(R_{\rm cap}=10^{-7}\) gives

\[
E_{16k\to32k}
\subset
\boxed{
[-2.7025903241562132\times10^{-5},
 -2.0845256355333730\times10^{-5}]
}.
\tag{11}
\]

Combining (11) with the promoted v14.059/v14.060 interval through 16k gives

\[
\boxed{
E_{4k\to32k}
\subset
[-2.6680345349120028\times10^{-5},
 -1.8869797018800170\times10^{-5}]
}.
\tag{12}
\]

So, **if the floor budget is audited**, the finite cumulative sign flips rigorously negative by 32k with a lower-magnitude one-sided margin of about

\[
1.887\times10^{-5},
\]

substantially larger than the earlier conditional v14.076 margin.

---

## 10. Reproducer

Deterministic producers:

- \`research-notes/suzuki_M32000_fixed_fft_graph_shear.py\`
  - graph shear;
  - \(\|W\|_F^2\);
  - positive pre-cancellation \(Q_{\rm comp}\);
  - source/operator budget diagnostics.

- \`research-notes/suzuki_M32000_mu_floor_outward_budget.py\`
  - two-stage complement floor;
  - protected outward charges;
  - \(\mu_{32k}\);
  - \(\theta_{32k}\);
  - 16k→32k and cumulative 4k→32k fail-closed intervals.

The latter CI run passed every embedded check.

---

## 11. Audit target and guardrail

**This entry is a certificate target, not a promotion.**

External audit should focus on:

1. the comparison proving the partial \(Q_8\)-eliminated shell Schur is \(\succeq I\) from v14.071;
2. the analytic cross-block cap \(\|B\|_2\le40\);
3. the public \(Q_{\rm comp}\le12\) inflation over the midpoint values;
4. the per-column LDDD residual cap \(10^{-25}\);
5. the public shear caps \(0.04/0.11\), including exact-graph correction through the coarse complement floor;
6. the deliberately conservative \(C_{\rm DD}=8192\) envelope;
7. the final arithmetic in (9)–(12).

If all pass, promote (10), thereby closing the v14.080 finite-floor obstruction and promoting the strictly negative 4k→32k finite cumulative interval. If any cap fails, return the exact replacement cap and its resulting \(\mu_{32k}\) / shell interval.

Sandbox remains assigned to the independent Lemma G/W analytic handoff in v14.083; no duplicate Sandbox task is created here.
