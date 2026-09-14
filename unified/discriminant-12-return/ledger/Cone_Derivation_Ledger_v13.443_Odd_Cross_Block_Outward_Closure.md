# Cone Derivation Ledger v13.443 — Odd M=4000 Cross-Block Outward Closure

Date: 2026-09-14

Status labels: **[D]** exact derived; **[N]** midpoint numerical; **[N-cert]** outward-certified numerical inequality; **[Audit]** guardrail.

## 0. Synchronization [Audit]

A fresh live-ledger check immediately before this write found `v13.442` (`prime-2 tangent V4 and S3 automorphism bridge`) as the newest numbered ledger entry. Three unnumbered Suzuki research-note commits then landed for the present cross audit, so `v13.443` remained free.

The active odd-sector cross target is

\[
\boxed{\|A_{FT}\|<1.015},
\]

with

\[
F=\{22,24,\ldots,4000\},
\qquad
T=\{4002,4004,\ldots\}.
\]

This was the principal remaining tail-elimination obligation after the finite-high closure in v13.434.

## 1. Historical transcript is no longer used as provenance [Audit]

The old file

`research-notes/suzuki_odd_M4000_index2_fail_closed_verifier.py`

contains the rounded constants

\[
0.97957,\qquad 0.03519,\qquad 1.015,
\]

but does not generate them.  Those numbers were therefore treated only as historical regression targets.

Three new artifacts now reconstruct and certify the cross calculation:

1. `research-notes/suzuki_odd_M4000_cross_midpoint_replay.py`;
2. `research-notes/suzuki_odd_M4000_cross_outward_verifier.py`;
3. `research-notes/suzuki_odd_M4000_cross_lowrank_factor_certificate.py`.

No theorem-level step below imports the old transcript constants as unexplained proof inputs.

## 2. Source-faithful cross formula [D]

For even modes `m in F`, `n in T`, the odd-sector same-parity cross entry is

\[
A_{mn}
=-\frac{2}{\pi}\frac{nZ_m-mZ_n}{n^2-m^2}
+2d_md_n,
\]

where

\[
d_n=\frac{2k_n\sinh(1/2)}{k_n^2+1/4},
\qquad k_n=\frac{n\pi}{2}.
\]

For even `n`, the source-faithful midpoint replay uses the equivalent scalar identity

\[
\operatorname{Si}(n\pi)+2H_n
=
\Im\psi\!\left(\frac14+\frac{i n\pi}{4}\right)
-
 n\pi\sum_{j\ge0}
\frac{e^{-2a_j}}{a_j^2+(n\pi/2)^2},
\qquad a_j=2j+\frac12.
\]

Together with the five prime channels `q=2,3,4,5,7`, this independently regenerates `Z_n` and hence the entire cross block.

## 3. Three-way tail split [D]

Use

\[
T_{\rm near}=\{4002,4004,\ldots,16000\},
\]

\[
T_{\rm rem}=\{16002,16004,\ldots,2,000,000\},
\]

\[
T_{\rm far}=\{2,000,002,2,000,004,\ldots\}.
\]

The near band is explicit, the remote band is represented by an inverse-power low-rank expansion, and the final infinite tail is controlled analytically.

## 4. Near band reconstruction [N]

The explicit near matrix has dimension

\[
1990\times6000.
\]

Its leading singular value is reproduced as

\[
\boxed{\sigma_1(A_{F,T_{\rm near}})\approx0.92281131}.
\]

The best numerical rank-12 candidate has direct a-posteriori residual

\[
\boxed{
\|A_{F,T_{\rm near}}-U\Sigma V^T\|_F
=0.0023073371285179884\ldots
}.
\]

This independently recovers the historical `0.0023073371285179897` checkpoint.

The orthogonality defects of the computed factors are only

\[
\|U^TU-I\|_F\approx2.4\times10^{-15},
\qquad
\|VV^T-I\|_F\approx4.2\times10^{-15}.
\]

For the outward proof we discard the historical last digits and use the relaxed bound

\[
\boxed{\|R_{\rm near}\|_2\le\|R_{\rm near}\|_F<0.002308.}
\]

## 5. Remote inverse-power representation [D/N]

For `n>=16002`, `m<=4000`,

\[
\frac1{n^2-m^2}
=
\frac1{n^2}\sum_{r\ge0}\left(\frac mn\right)^{2r},
\qquad
\rho:=\frac{4000}{16002}<\frac14.
\]

Each `r` contributes two separable channels:

\[
-\frac{2}{\pi}Z_m m^{2r}\,n^{-(2r+1)},
\qquad
\frac{2}{\pi}m^{2r+1}Z_n\,n^{-(2r+2)},
\]

plus the exact rank-one pole channel.

Eight inverse-power levels are retained.  The combined near-rank-12 plus remote-low-rank point norm is

\[
\boxed{0.977251930755\ldots}.
\]

This recovers the old `0.977251921...` scale without importing it.

## 6. A-posteriori low-rank norm certificate [N-cert]

The low-rank certificate does not trust the SVD/eigensolver as an oracle.

The remote feature Gram is factored numerically and checked directly; its reconstruction defect in the full finite-side Gram is

\[
<10^{-16}
\]

at midpoint scale, with a proof allowance `1e-12`.

Concatenating the near and remote factors gives a `1990 x 29` factor `W`.  To prove

\[
\|W\|_2<0.977255,
\]

form the `29 x 29` shifted Gram

\[
M=0.977255^2I-W^TW.
\]

Its midpoint smallest eigenvalue is approximately

\[
5.999\times10^{-6}.
\]

A Cholesky candidate `M=LL^T` is checked a posteriori:

\[
\|M-LL^T\|_F\approx4.9\times10^{-16},
\]

and the verified-inverse route gives

\[
\|X\|_F<409,
\qquad
\|I-LX\|_2<10^{-10}.
\]

Therefore

\[
\lambda_{\min}(LL^T)
>
\frac{(1-10^{-10})^2}{409^2}
\approx5.978\times10^{-6}.
\]

After charging `1e-8` for Gram formation and `1e-12` for the remote Gram factorization, the shifted Gram still has floor

\[
>5.9\times10^{-6}.
\]

Hence

\[
\boxed{\|W\|_2<0.977255.}
\]

## 7. Remote geometric remainder [D/N-cert]

After eight inverse-power levels, use only

\[
|Z_m|<8,
\qquad |Z_n|<8,
\qquad \rho<1/4.
\]

The two omitted Frobenius channels give

\[
\|R_{\rm rem,geom}\|_F
<1.19\times10^{-11}.
\]

We round outward to

\[
\boxed{\|R_{\rm rem,geom}\|<1.2\times10^{-11}.}
\]

## 8. Certified source perturbations through 2M [N-cert]

The v13.434 finite-side source enclosure gives the conservative uniform bound

\[
\boxed{|\Delta Z_m|<2.1\times10^{-9}},
\qquad m\in F.
\]

Extending the exact-rational prime base-rotation recurrence from
`research-notes/suzuki_prime_trig_rational_certificate.py` gives

\[
\text{prime sequence error for }r\le8000
<3.56\times10^{-9},
\]

and

\[
\text{prime sequence error for }r\le10^6
<4.44\times10^{-7}.
\]

Because the prime sequence enters `Z` with coefficient two, and the already-certified cusp/arch contributions are far smaller, we use

\[
\boxed{|\Delta Z_n|<7.2\times10^{-9}}
\quad(4002\le n\le16000),
\]

\[
\boxed{|\Delta Z_n|<8.9\times10^{-7}}
\quad(16002\le n\le2,000,000).
\]

For the near Cauchy error maps, simple Frobenius bounds give coefficients below

\[
0.536,\qquad0.434.
\]

For the remote band, analytic Frobenius bounds give coefficients below

\[
0.169,\qquad0.0142.
\]

Thus the total source perturbation of the explicit-through-2M cross operator is

\[
\boxed{<2\times10^{-8}}.
\]

A deliberately loose global allowance

\[
\boxed{10^{-6}}
\]

is reserved for source perturbations plus binary64 assembly and low-dimensional moment arithmetic.  The source component therefore occupies less than `1/50` of the reserve.

## 9. Explicit cross through 2M [N-cert]

Combining the outward pieces,

\[
\begin{aligned}
\|A_{F,T_{\le2M}}\|
&<0.977255
+0.002308
+1.2\times10^{-11}
+10^{-6}\\
&=0.979564000012.
\end{aligned}
\]

Therefore

\[
\boxed{
\|A_{F,T_{\le2M}}\|<0.97957.
}
\]

The rounding step retains approximately

\[
5.999988\times10^{-6}
\]

of slack.

## 10. Analytic far tail beyond 2M [D/N-cert]

For `n>=2,000,002`, extract the signed leading channel

\[
\frac{L}{n},
\qquad
L=-\frac2\pi Z_F+\frac{8\sinh(1/2)}{\pi}d_F.
\]

The leading rank-one contribution is

\[
\boxed{0.03511180837295223\ldots}.
\]

For the remainder, with

\[
\rho=\frac{4000}{2,000,002},
\]

use

\[
\|r_n-L/n\|_2\le\frac{B}{n^2}+\frac{C}{n^3},
\]

\[
B=
\frac{16/\pi}{1-\rho^2}\|F\|_2,
\]

\[
C=
\frac{2/\pi}{1-\rho^2}\,8\|F^2\|_2
+
\frac{8\sinh(1/2)}{\pi^3}\|d_F\|_2.
\]

Using only the uniform `|Z_F|<8` envelope in `C`, the Frobenius tail sum is

\[
\boxed{<7.604\times10^{-5}}.
\]

The finite-side source perturbation changes the leading channel by less than

\[
3.0\times10^{-11},
\]

and an additional `1e-9` scalar arithmetic allowance is charged.  Hence

\[
\boxed{
\|A_{F,T_{>2M}}\|
<0.035187847724
<0.03519.
}
\]

This outward rounding retains more than

\[
2.15\times10^{-6}
\]

of slack.

## 11. Full cross closure [N-cert]

Finally,

\[
\begin{aligned}
\|A_{FT}\|
&\le
\|A_{F,T_{\le2M}}\|
+
\|A_{F,T_{>2M}}\|\\
&<0.97957+0.03519\\
&=1.01476\\
&<1.015.
\end{aligned}
\]

Therefore the outstanding cross obligation is closed:

\[
\boxed{\|A_{FT}\|<1.015.}
\]

The final rounded target retains

\[
\boxed{1.015-1.01476=2.4\times10^{-4}}
\]

of slack.

## 12. Consequence for the effective odd tail floor [N-cert]

Using the already-audited raw odd-tail bound

\[
\alpha_{4002}
=
\log(4002/4)-\pi/2-2.05-0.706-0.00040766761547103477
=
2.5810511596134207\ldots,
\]

and the v13.434 finite-high floor

\[
A_{FF}\succeq0.53I,
\]

Schur elimination gives

\[
\delta_{\rm odd}
>
\alpha_{4002}-\frac{1.015^2}{0.53}
=
0.6372304048964401\ldots.
\]

Hence

\[
\boxed{\delta_{\rm odd}>0.637.}
\]

## 13. Interaction with the mod-12 / mod-24 structural thread [Audit]

No mod-12 character cancellation is used in this certificate.  This is consistent with v13.415, which showed that the current `q=5,7` arithmetic source support makes the `chi_12` source channel a sign copy of the unit channel for sign-invariant norms.

The mod-24 unit-core decomposition remains structurally informative, but the present cross closure is source-faithful and independent of it.

## 14. Remaining odd-sector obligations [Audit]

The following are now closed:

\[
\boxed{A_{FF}\succeq0.53I}
\qquad\text{(v13.434)},
\]

\[
\boxed{\|A_{FT}\|<1.015}
\qquad\text{(this checkpoint)},
\]

and therefore

\[
\boxed{\delta_{\rm odd}>0.637}.
\]

The odd-sector index theorem is **not yet promoted**.  The remaining proof-grade obligation is the normalized frozen 8D subspace:

\[
\boxed{C_{\rm odd}\succeq0.80I},
\qquad
\boxed{H_{\rm odd}<0.225I}.
\]

The old scalar transcript arithmetic for those targets has been independently checked and gives

\[
C_{\rm lower,raw}\approx0.8041358387211434,
\]

\[
H_{\rm outward}\approx0.2248974554604973,
\]

but source/provenance replay of the normalized matrices remains to be completed before theorem promotion.

No exact-zero, kernel, RH, or GRH conclusion is made.

---

**Checkpoint conclusion.** The odd `M=4000` finite-high / infinite-tail cross norm has now been independently reconstructed from the source-faithful same-parity formula and outward-certified below `1.015`.  Together with v13.434 this closes the high-complement Schur floor at `delta_odd>0.637`.  The only remaining odd-sector theorem-level certification is the normalized frozen-8D pair `C_odd>=0.80I`, `H_odd<0.225I`.