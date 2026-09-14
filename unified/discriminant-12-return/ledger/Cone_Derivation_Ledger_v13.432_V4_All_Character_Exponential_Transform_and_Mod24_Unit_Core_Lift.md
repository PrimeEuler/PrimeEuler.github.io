# Cone Derivation Ledger v13.432 — V4 All-Character Exponential Transform and Mod-24 Unit-Core Lift

**Renumbering note:** originally filed as `v13.429`, then briefly as `v13.430`; both numbers collided with concurrently-created ledger entries. After a fresh live-head check showing `v13.431` as the newest occupied number, this entry is normalized to `v13.432`. Mathematical content is unchanged.

Date: 2026-09-14

Status labels: **[D]** exact derived; **[N]** numerical diagnostic; **[Audit]** guardrail.

## 0. Synchronization [Audit]

This checkpoint was normalized after checking the live ledger through v13.431. External Audit Round 30 independently verified the v13.427 chi12 exponential generating transform. The Suzuki-side v13.423 mod-24/unit-core lift and its finite-high diagnostics are incorporated here without promoting an operator symmetry that has not been proved.

## 1. Residue-sector exponential transforms [D]

For r in U(12)={1,5,7,11}, define

\[
\mathcal F_r(n,t)=\sum_{\substack{k\le n\\k\equiv r\pmod{12}}}\left(e^{t\{n/k\}}-1\right).
\]

For the four real mod-12 characters define

\[
\mathcal G_\chi(n,t)=\sum_{k\le n}\chi(k)\left(e^{t\{n/k\}}-1\right).
\]

With residue order (1,5,7,11), character order (1,-4,-3,12), and

\[
H_4=\begin{pmatrix}1&1&1&1\\1&1&-1&-1\\1&-1&1&-1\\1&-1&-1&1\end{pmatrix},\qquad H_4^2=4I,
\]

one has exactly

\[
\boxed{\mathbf G(n,t)=H_4\mathbf F(n,t)},\qquad\boxed{\mathbf F(n,t)=\frac14H_4\mathbf G(n,t)}.
\]

Thus all four character transforms determine the entire exponential shell-displacement distribution in each unit residue sector.

## 2. Distribution-level Hadamard decomposition [D]

Define finite sector measures

\[
\mu_r^{(n)}=\sum_{\substack{k\le n\\k\equiv r\pmod{12}}}\delta_{\{n/k\}}
\]

and signed character measures

\[
\nu_\chi^{(n)}=\sum_{k\le n}\chi(k)\delta_{\{n/k\}}.
\]

Then

\[
\boxed{\boldsymbol\nu=H_4\boldsymbol\mu},\qquad\boxed{\boldsymbol\mu=\frac14H_4\boldsymbol\nu}.
\]

The exponential transforms are simply

\[
\mathcal F_r(n,t)=\int(e^{tx}-1)\,d\mu_r^{(n)}(x),\qquad\mathcal G_\chi(n,t)=\int(e^{tx}-1)\,d\nu_\chi^{(n)}(x).
\]

Hence the V4 Fourier transform acts on the full finite displacement measures, not only on individual moments.

## 3. Every moment follows by differentiation [D]

For every integer j>=1,

\[
M_{j,r}(n)=\sum_{\substack{k\le n\\k\equiv r\pmod{12}}}\{n/k\}^j,\qquad M_{j,\chi}(n)=\sum_{k\le n}\chi(k)\{n/k\}^j.
\]

Differentiating at t=0 gives

\[
\boxed{\mathbf M_{j,\chi}=H_4\mathbf M_{j,r}},\qquad\boxed{\mathbf M_{j,r}=\frac14H_4\mathbf M_{j,\chi}}.
\]

Thus v13.410's first/quadratic V4 decompositions and v13.422's higher moments are coefficient slices of one distribution-level identity.

## 4. Exact mod-24 lift on the first even stratum [D]

From v13.423, for

\[
v_2(k)=1,\qquad 3\nmid k,
\]

write k=2u with (u,6)=1. Then

\[
\boxed{\begin{array}{c|cccc}k\bmod24&2&10&14&22\\\hline u=k/2\bmod12&1&5&7&11\end{array}}
\]

so mod 24 exactly retains all four V4 labels on this ramified even stratum.

Define

\[
\mathcal F_r^{(2)}(n,t)=\sum_{\substack{k\le n\\k\equiv2r\pmod{24}}}\left(e^{t\{n/k\}}-1\right),
\]

and on this stratum

\[
\chi^{\uparrow2}(k)=\chi(k/2).
\]

Then

\[
\mathcal G_\chi^{(2)}(n,t)=\sum_{\substack{k\le n\\v_2(k)=1,\ 3\nmid k}}\chi(k/2)\left(e^{t\{n/k\}}-1\right),
\]

with the same exact transform

\[
\boxed{\mathbf G^{(2)}=H_4\mathbf F^{(2)}},\qquad\boxed{\mathbf F^{(2)}=\frac14H_4\mathbf G^{(2)}}.
\]

**[Audit]** The lifted weights are stratum-restricted unit-core characters, not global Dirichlet characters modulo 24.

## 5. General ramified/unit-core decomposition [D/Audit]

Write uniquely

\[
k=2^a3^b u,\qquad (u,6)=1.
\]

Then the data

\[
(a,b;u\bmod12)
\]

split the ramification layer from the unit-core V4 label. On every fixed (a,b) stratum, scalar observables can be decomposed exactly into the same four V4 character coordinates by assigning the weight chi(u).

This is an exact harmonic-analysis statement for scalar observables restricted to a fixed stratum.

**[Audit]** It does not imply that an operator indexed by k commutes with these projectors or becomes block diagonal.

## 6. Suzuki finite-high class-mass Fourier diagnostic [N/Audit]

v13.423 reports the normalized lowest-eigenvector squared mass by unit-core class

\[
\mathbf m\approx(0.0670181,0.5251509,0.1133531,0.2944779)^T
\]

for classes (1,5,7,11). Its V4 Hadamard coordinates are

\[
\boxed{H_4\mathbf m\approx(1.0000000,\ 0.1843380,\ -0.6392576,\ -0.2770080)^T.}
\]

Therefore the largest nonprincipal class-mass imbalance is in the chi_-3 channel, not chi_12.

This matches the 5/11-heavy dangerous direction: chi_-3 assigns the same negative sign to both 5 and 11, whereas chi_12 assigns opposite signs.

**[Audit]** This is a Fourier transform of class masses only. It is not an operator eigen-decomposition, not a commutation theorem, and not a positivity certificate. The exact Suzuki-side conclusion remains that every individual unit-core diagonal block is safely positive and the small global margin is created by inter-channel coupling.

## 7. Structural synthesis [D/I]

The same finite group transform now appears on two rigorously separated carriers:

\[
\boxed{\text{unit residue / unit-core sectors}\xleftrightarrow{\ H_4\ }\text{four V4 character coordinates}.}
\]

On the shell-displacement side this acts on full finite displacement measures. On fixed ramification strata, including the mod-24 first even stratum, it exactly decomposes scalar observables by unit-core label.

The mod-24 lift therefore supplies the correct way to retain V4 information on even indices while respecting the fact that ordinary mod-12 Dirichlet characters vanish on ramified integers.

## 8. Next exact targets

1. Determine the minimal modulus required to recover u mod12 on each fixed (v2,v3) stratum.
2. Apply H4 to the four-by-four Suzuki block-coupling matrix at the class level and test whether any exact or numerically stable low-rank pattern appears.
3. Do not promote any such pattern to an operator symmetry without an exact commutation/covariance identity.

---

**Checkpoint conclusion.** The complete shell-displacement moment hierarchy is now unified at the distribution level by a single V4 Hadamard transform. The Suzuki mod-24 lift fits the same finite harmonic-analysis template on the first even ramified stratum, but only at the level of unit-core labeling and scalar observables. The current Suzuki lowest-vector mass diagnostic points most strongly to chi_-3, not chi_12, which is an important guardrail against over-interpreting the Pell/regulator channel.
