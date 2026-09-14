# V4 All-Character Exponential Transform and Mod-24 Unit-Core Lift

Date: 2026-09-14

Status labels: **[D]** exact derived; **[N]** numerical diagnostic inherited from the Suzuki midpoint block; **[Audit]** guardrail.

## 1. Unit-sector exponential displacement measures [D]

For fixed integer n and residue r in U(12)={1,5,7,11}, define

\[
\mathcal F_r(n,t)
=
\sum_{\substack{k\le n\\k\equiv r\pmod{12}}}
\left(e^{t\delta_k(n)}-1\right),
\qquad
\delta_k(n)=\left\{\frac nk\right\}.
\]

Equivalently, if

\[
\mu_r^{(n)}=\sum_{\substack{k\le n\\k\equiv r\pmod{12}}}\delta_{\delta_k(n)},
\]

then

\[
\mathcal F_r(n,t)=\int_{[0,1)}(e^{tx}-1)\,d\mu_r^{(n)}(x).
\]

Thus each residue class carries a finite exponential/Laplace transform of the shell-displacement distribution.

## 2. Four character transforms [D]

For the four real characters

\[
1,\quad \chi_{-4},\quad \chi_{-3},\quad \chi_{12},
\]

define

\[
\mathcal G_\chi(n,t)
=
\sum_{k\le n}\chi(k)\left(e^{t\delta_k(n)}-1\right).
\]

Because all four characters vanish off U(12), only the unit residue sectors enter. Using the residue order (1,5,7,11) and character order (1,-4,-3,12),

\[
H_4=
\begin{pmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{pmatrix},
\qquad H_4^2=4I.
\]

Therefore

\[
\boxed{
\begin{pmatrix}
\mathcal G_1^\times\\
\mathcal G_{-4}\\
\mathcal G_{-3}\\
\mathcal G_{12}
\end{pmatrix}
=
H_4
\begin{pmatrix}
\mathcal F_1\\
\mathcal F_5\\
\mathcal F_7\\
\mathcal F_{11}
\end{pmatrix}.
}
\]

and hence

\[
\boxed{
\begin{pmatrix}
\mathcal F_1\\
\mathcal F_5\\
\mathcal F_7\\
\mathcal F_{11}
\end{pmatrix}
=
\frac14 H_4
\begin{pmatrix}
\mathcal G_1^\times\\
\mathcal G_{-4}\\
\mathcal G_{-3}\\
\mathcal G_{12}
\end{pmatrix}.
}
\]

This reconstructs the entire exponential shell-displacement distribution in each unit residue sector, not merely one moment.

## 3. Moment recovery [D]

Expanding

\[
e^{t\delta}-1=\sum_{j\ge1}\frac{t^j}{j!}\delta^j
\]

gives

\[
\mathcal F_r(n,t)
=
\sum_{j\ge1}\frac{t^j}{j!}M_{j,r}(n),
\]

where

\[
M_{j,r}(n)=\sum_{\substack{k\le n\\k\equiv r\pmod{12}}}\delta_k(n)^j.
\]

Similarly

\[
\mathcal G_\chi(n,t)
=
\sum_{j\ge1}\frac{t^j}{j!}M_{j,\chi}(n),
\qquad
M_{j,\chi}(n)=\sum_{k\le n}\chi(k)\delta_k(n)^j.
\]

Thus for every j>=1,

\[
\boxed{
\mathbf M_{j,\chi}=H_4\mathbf M_{j,r},
\qquad
\mathbf M_{j,r}=\frac14H_4\mathbf M_{j,\chi}.
}
\]

The first derivative recovers the V4 decomposition of E_chi, the second derivative the quadratic-energy decomposition, and all higher derivatives recover the complete moment hierarchy.

## 4. Distribution-level statement [D]

The previous identity can be stated directly at the level of finite measures. Define signed character measures

\[
\nu_\chi^{(n)}
=
\sum_{k\le n}\chi(k)\,\delta_{\delta_k(n)}.
\]

Then

\[
\boxed{
\begin{pmatrix}
\nu_1^\times\\
\nu_{-4}\\
\nu_{-3}\\
\nu_{12}
\end{pmatrix}
=
H_4
\begin{pmatrix}
\mu_1\\
\mu_5\\
\mu_7\\
\mu_{11}
\end{pmatrix},
\qquad
\begin{pmatrix}
\mu_1\\
\mu_5\\
\mu_7\\
\mu_{11}
\end{pmatrix}
=
\frac14H_4
\begin{pmatrix}
\nu_1^\times\\
\nu_{-4}\\
\nu_{-3}\\
\nu_{12}
\end{pmatrix}.
}
\]

So the Hadamard transform reconstructs the full finite displacement measure sector-by-sector.

## 5. First even stratum: exact mod-24 lift [D]

The Suzuki-side v13.423 checkpoint writes

\[
k=2u,
\qquad v_2(k)=1,
\qquad 3\nmid k,
\qquad (u,6)=1.
\]

Then

\[
\boxed{
\begin{array}{c|cccc}
k\bmod24&2&10&14&22\\
\hline
u=k/2\bmod12&1&5&7&11
\end{array}}
\]

so the first even ramified stratum retains the same four V4 labels exactly.

Define the four lifted residue-sector transforms

\[
\mathcal F_r^{(2)}(n,t)
=
\sum_{\substack{k\le n\\k\equiv 2r\pmod{24}}}
\left(e^{t\delta_k(n)}-1\right),
\qquad r\in\{1,5,7,11\}.
\]

On this restricted stratum define the lifted character weight

\[
\chi^{\uparrow 2}(k)=\chi(k/2).
\]

Then

\[
\mathcal G_\chi^{(2)}(n,t)
=
\sum_{\substack{k\le n\\v_2(k)=1,\ 3\nmid k}}
\chi(k/2)\left(e^{t\delta_k(n)}-1\right),
\]

and exactly the same Hadamard transform holds:

\[
\boxed{
\mathbf G^{(2)}=H_4\mathbf F^{(2)},
\qquad
\mathbf F^{(2)}=\frac14H_4\mathbf G^{(2)}.
}
\]

**[Audit]** The lifted function k -> chi(k/2) on this stratum is not a global Dirichlet character modulo 24. This is a stratum-restricted V4 labeling, exactly as v13.423 requires.

## 6. General unit-core lift [D/Audit]

For any nonzero integer k write uniquely

\[
k=2^a3^b u,
\qquad (u,6)=1.
\]

The pair

\[
(a,b;u\bmod12)
\]

separates ramification data from the unit-core V4 label. On each fixed (a,b) stratum one may define

\[
\chi^{\uparrow(a,b)}(k)=\chi(u)
\]

and perform the same finite V4 transform on the four unit-core sectors.

**[Audit]** This gives an exact bookkeeping/Fourier decomposition of observables restricted to a fixed ramification stratum. It does not imply that a matrix indexed by k commutes with these projectors or becomes block diagonal.

## 7. Suzuki midpoint diagnostic in V4 Fourier coordinates [N/Audit]

v13.423 reports squared lowest-eigenvector mass by unit-core class

\[
\mathbf m
\approx
(0.0670181,\ 0.5251509,\ 0.1133531,\ 0.2944779)^T
\]

in the order (1,5,7,11). Applying H_4 gives

\[
\boxed{
H_4\mathbf m
\approx
\begin{pmatrix}
1.0000000\\
0.1843380\\
-0.6392576\\
-0.2770080
\end{pmatrix}.
}
\]

Thus, among the nonprincipal class-mass imbalances, the largest magnitude lies in the chi_-3 channel, not chi_12.

This is consistent with the observed concentration in classes 5 and 11: chi_-3 takes the same negative sign on both of those classes, whereas chi_12 assigns opposite signs to 5 and 11.

**[Audit]** These are Fourier coordinates of the four class masses only. They are not eigenvalues, operator characters, or a proof that the Suzuki matrix decomposes into V4 channels. The exact v13.423 conclusion remains that the small global margin is an inter-channel phenomenon.

## 8. Structural consequence [D/I]

The shell-displacement side and the mod-24 Suzuki-side lift now share the same finite V4 harmonic-analysis template on different carriers:

\[
\boxed{
\text{unit residue / unit-core sectors}
\xleftrightarrow{\ H_4\ }
\text{four character coordinates}.
}
\]

On the shell side this is an exact decomposition of the full displacement measure. On the first even ramified stratum it is an exact decomposition of any stratum-restricted scalar observable by unit core. On the Suzuki matrix itself, no intertwining has yet been proved.

The mod-24 lift therefore supplies a rigorous way to retain V4 labels on even modes while preserving the guardrail that ordinary mod-12 Dirichlet characters vanish on those modes.

## 9. Next exact targets

1. Build the analogous lifted transforms on the other fixed (v2,v3) strata and identify the minimal modulus needed to recover u mod12 in each case.
2. Test whether row/column coupling norms of the Suzuki finite-high matrix have any reproducible low-rank structure after transforming the four unit-core class blocks with H_4.
3. Keep scalar-observable Fourier decomposition distinct from an operator-level intertwining claim unless an exact commutation or covariance relation is proved.
