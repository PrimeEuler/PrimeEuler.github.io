# Cone Derivation Ledger v14.020 — High-Order Far Geometric Remainder and a Useful Replacement for the Absolute \(C_\rho\)

**Date:** 2026-10-04  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [D] exact separated geometric-remainder formula for the frozen finite source solution; [N] unit-energy far remainder bounds through moment order \(K=10\); [N] the residual norm collapses from the useless v14.019 absolute \(n^{-3}\) bound to \(1.2\times10^{-10}\)-class on the full \(n\ge2N\) far tail and \(10^{-17}\)-class on \(n\ge4N\); [I] v14.017's sign-preserving moment extraction is quantitatively sufficient with enormous outward slack; [O] outward-enclose the finite signed/absolute moments or map this norm directly into the v14.016 \(R_N^{\rm bd}\) consumer.  
**Parents:** v14.011, v14.017, v14.019.  
**Research commit:** b74d68e617d37f9d5f3b1d1a90610d823621b4d9.  
**Workflow commit:** fd19ca112f7c2b98d86cb8a065fb5dc197ee7326.  
**Collision check:** immediately before this write, live HEAD was fd19ca112f7c2b98d86cb8a065fb5dc197ee7326 and no current v14.020 ledger file was present.

---

## 1. Purpose

v14.019 showed that an absolute-value residual constant taken immediately after the first two asymptotic channels is useless:

\[
C_{\rho,e}^{\rm abs}\sim1.18\times10^{16},
\qquad
C_{\rho,o}^{\rm abs}\sim2.22\times10^{14}.
\]

That failure comes from replacing the large, highly cancelling finite source moments by absolute coefficient moments too early.

v14.017 already prescribes the correct repair:

1. freeze the \(N=4000\) source solution;
2. treat the near shell exactly;
3. on the separated far tail, retain the correlated signed moment expansion;
4. absolute-bound only the genuine geometric remainder.

The present entry quantifies that repair.

---

## 2. Separated far expansion [D]

Fix the finite source solution \(x_N\) with support

\[
m\le N,
\qquad
N=4000.
\]

For a remote mode \(n\ge2N\),

\[
\frac{m}{n}\le\frac12.
\]

The Cauchy/displacement row is

\[
\frac{2}{\pi}
\sum_{m\le N}
\frac{z_n m-nz_m}{n^2-m^2}
x_m.
\]

For any integer \(K\ge0\),

\[
\frac1{1-r^2}
=
\sum_{j=0}^{K}r^{2j}
+
\frac{r^{2K+2}}{1-r^2},
\qquad
r=\frac mn.
\]

Define signed moments

\[
M_{2j+1}
=
\sum_{m\le N}
m^{2j+1}x_m,
\]

\[
Z_{2j}
=
\sum_{m\le N}
z_m m^{2j}x_m.
\]

Then the finite signed expansion is

\[
\frac{2}{\pi}
\left[
z_n
\sum_{j=0}^{K}
\frac{M_{2j+1}}{n^{2j+2}}
-
\sum_{j=0}^{K}
\frac{Z_{2j}}{n^{2j+1}}
\right],
\]

and the remainder is exact.

The source term and rank-one pole term are retained exactly and contribute no geometric remainder here.

---

## 3. Uniform geometric remainder [D]

Let

\[
S_j
=
\sum_{m\le N}m^j|x_m|,
\]

\[
S^z_j
=
\sum_{m\le N}|z_m|m^j|x_m|.
\]

For \(n\ge2N\), using

\[
\frac1{1-(m/n)^2}
\le
\frac43,
\]

and a valid remote bound

\[
|z_n|\le Z_{\max},
\qquad
Z_{\max}=8,
\]

the off-diagonal remainder after retaining \(j=0,\ldots,K\) obeys

\[
\boxed{
|R_K(n)|
\le
\frac{2}{\pi}\frac43
\left[
\frac{S^z_{2K+2}}{n^{2K+3}}
+
\frac{Z_{\max}S_{2K+3}}{n^{2K+4}}
\right].
}
\tag{1}
\]

This is an ordinary geometric-series inequality after all signed moment channels through order \(K\) have already been removed.

For the unit-energy source vector

\[
y_N=\sqrt{C_N}\,x_N,
\]

define

\[
A_K
=
\sqrt{C_N}
\frac{2}{\pi}\frac43
S^z_{2K+2},
\]

\[
B_K
=
\sqrt{C_N}
\frac{2}{\pi}\frac43
Z_{\max}S_{2K+3}.
\]

Then

\[
\boxed{
|\widetilde R_K(n)|
\le
\frac{A_K}{n^{2K+3}}
+
\frac{B_K}{n^{2K+4}}.
}
\tag{2}
\]

---

## 4. Same-parity \(\ell^2\) tail bound [D]

For a parity lattice

\[
n=n_0,n_0+2,n_0+4,\ldots
\]

and \(p>1\),

\[
\sum n^{-p}
\le
n_0^{-p}
+
\frac{n_0^{-(p-1)}}{2(p-1)}.
\tag{3}
\]

Using

\[
(a+b)^2\le2a^2+2b^2,
\]

equations (2)–(3) give an explicit closed same-parity \(\ell^2\) bound on the entire far remainder.

No remote row sampling is needed for this inequality.

---

## 5. Full far tail \(n\ge2N=8000\) [N]

The frozen LDDD \(N=4000\) source solutions were inserted into the exact geometric formula.

The resulting unit-energy \(\ell^2\) remainder bounds are:

### even-v

\[
\begin{array}{c|c}
K&\|\widetilde R_K\|_{\ell^2(n\ge8000)}\\ \hline
2&4.8365\times10^{-5}\\
4&1.5122\times10^{-6}\\
6&5.9020\times10^{-8}\\
8&2.5798\times10^{-9}\\
10&1.2084\times10^{-10}
\end{array}
\]

Thus

\[
\boxed{
\|\widetilde R_{10,e}\|_2
<
1.21\times10^{-10}.
}
\tag{4}
\]

### odd-v

\[
\begin{array}{c|c}
K&\|\widetilde R_K\|_{\ell^2(n\ge8000)}\\ \hline
2&4.8172\times10^{-5}\\
4&1.5030\times10^{-6}\\
6&5.8533\times10^{-8}\\
8&2.5540\times10^{-9}\\
10&1.1947\times10^{-10}
\end{array}
\]

Hence

\[
\boxed{
\|\widetilde R_{10,o}\|_2
<
1.20\times10^{-10}.
}
\tag{5}
\]

The parity values are themselves nearly common-mode.

---

## 6. More strongly separated tail \(n\ge4N=16000\) [N]

When the geometric expansion begins at

\[
n\ge4N,
\]

the ratio satisfies

\[
m/n\le1/4.
\]

The same \(K=10\) calculation gives

\[
\boxed{
\|\widetilde R_{10,e}\|_2
<
1.01\times10^{-17},
}
\tag{6}
\]

\[
\boxed{
\|\widetilde R_{10,o}\|_2
<
1.00\times10^{-17}.
}
\tag{7}
\]

Already at \(K=8\),

\[
\|\widetilde R_{8,e}\|_2
<
3.45\times10^{-15},
\]

\[
\|\widetilde R_{8,o}\|_2
<
3.44\times10^{-15}.
\]

Thus the truly far geometric remainder is numerically negligible once the signed moment hierarchy is retained.

---

## 7. Contrast with the v14.019 absolute-\(C_\rho\) failure [I]

v14.019 applied absolute values immediately after only the first two structural channels and obtained enormous constants.

The present calculation applies absolute values only after ten signed moment channels have been retained.

The improvement is not incremental.

It changes the full \(n\ge8000\) unit-energy remainder from an unusable absolute estimate to

\[
\boxed{
O(10^{-10})
\ \text{in }\ell^2.
}
\]

This confirms the central v14.017 instruction:

\[
\boxed{
\textbf{extract correlation first; absolute-bound only the geometric leftover.}
}
\tag{8}
\]

---

## 8. Energy-scale consequence [I]

Suppose the remote inverse used by the final enclosure has a certified coercivity floor \(\gamma\).

Then the pure geometric residual energy satisfies

\[
\widetilde R_K^*
S^{-1}
\widetilde R_K
\le
\gamma^{-1}
\|\widetilde R_K\|_2^2.
\]

Using merely a floor of order

\[
\gamma\sim10^{-1},
\]

the \(K=10\), \(n\ge8000\) remainder would contribute only on the order of

\[
10^{-19}
\]

to the normalized tail energy.

This is many orders below the observed

\[
10^{-5}
\]

parity-sensitive shell corrections.

Even substantial outward inflation of the frozen-source moment bounds would leave large numerical headroom.

This estimate is conditional on matching the norm/metric used by the final \(\gamma\), as flagged in v14.019.

---

## 9. What remains to make this outward [O]

The geometric algebra (1)–(3) is exact.

The remaining numerical inputs are the finite moments of the \(N=4000\) source solution and the capacity normalization.

The present replay uses the validated LDDD midpoint source solution rather than outward intervals.

To promote the bound one may either:

1. outward-enclose the finitely many signed/absolute moments used at \(K=10\); or
2. propagate a certified finite-source solution error directly into the moment sums.

Because the midpoint remainder is only \(10^{-10}\)-class in \(\ell^2\), the allowable inflation before it becomes relevant is extremely large.

---

## 10. Result

The residual-constant obstruction from v14.019 is not structural.

A high-order correlated far expansion gives

\[
\boxed{
\|\widetilde R_{10,e}\|_2
<
1.21\times10^{-10},
\qquad
\|\widetilde R_{10,o}\|_2
<
1.20\times10^{-10}
\quad(n\ge8000).
}
\]

At \(n\ge16000\),

\[
\boxed{
\|\widetilde R_{10,p}\|_2
\lesssim10^{-17}.
}
\]

Therefore the remaining relative-tail proof should not seek a single low-order absolute \(C_\rho\).

It should consume the finite signed moment channels explicitly and use a high-order geometric remainder bound only at the end.

---

HANDOFF
target: sandbox
type: payload
parent: v14.020
status: open
action: Replace the unusable low-order absolute \(C_\rho\) in the v14.016 conditional enclosure by the v14.020 high-order signed-moment plus geometric-remainder formulation, and state which finite moment intervals are minimally sufficient to turn the \(K=10\), \(n\ge8000\) \(1.2\times10^{-10}\)-class midpoint \(\ell^2\) bound into an outward \(R_N^{\rm bd}\).
deliverable: theorem-or-obstruction
constraints: Preserve all signed moment channels through the chosen order before taking absolute values; keep the near block \(4000<n\le8000\) separate; do not re-collapse the far tail to a low-order absolute coefficient constant.
