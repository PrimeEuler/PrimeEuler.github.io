# Cone Derivation Ledger v13.316 — Finite Feshbach Buffer Anatomy and Multiscale Near-Null Core

## Status

This checkpoint begins the finite Feshbach reduction suggested by v13.315.

The odd Dirichlet sector at a=1 is split into

\[
\mathcal C=\operatorname{span}\{\psi_1,\psi_3,\ldots,\psi_{19}\}
\]

and the finite buffer

\[
\mathcal B_{399}=\operatorname{span}\{\psi_{21},\psi_{23},\ldots,\psi_{399}\}.
\]

The remote infinite tail is not folded into the finite matrix in this checkpoint; its certified coercive bounds remain those of v13.312-v13.315.

The purpose here is numerical anatomy:

1. determine whether the finite buffer itself is near-singular;
2. inspect the finite Feshbach correction on the low core;
3. resolve the low-core spectrum at high precision.

No positivity proof for the infinite complement, no exact kernel claim, and no RH/GRH conclusion is made.

---

## 1. Matrix decomposition used

The finite odd-sector direct-form matrix is assembled as

\[
A=C_{\rm cusp}+B_{\rm prime}+K_{\rm arch}+P_{\rm pole}.
\]

Each part is handled by the sharpest structure already established:

- \(C_{\rm cusp}\): exact Si/Ci formulas from v13.301;
- \(B_{\rm prime}\): exact v13.315 joint-prime factorization;
- \(K_{\rm arch}\): smooth one-dimensional quadrature of \(-r''(t)\) against the exact shift matrix element;
- \(P_{\rm pole}\): exact positive rank-one pole term in the even-v sector.

For odd \(m\ne n\), v13.315 gives

\[
(B_{\rm prime})_{mn}
=-\frac4\pi\frac{nA_m-mA_n}{n^2-m^2},
\]

with

\[
A_j=\sum_{q\in\{2,3,4,5,7\}}
\frac{\Lambda(q)}{\sqrt q}
\sin\!\left(\frac{j\pi}{2}\log q\right).
\]

The diagonal prime entry is evaluated from the exact truncated-shift diagonal

\[
\langle\psi_n,S_\ell\psi_n\rangle
=(2-\ell)\cos(k_n\ell)+\frac{\sin(k_n\ell)}{k_n},
\qquad k_n=\frac{n\pi}{2}.
\]

The smooth archimedean remainder uses

\[
r''(t)=\frac{e^{-t/2}}{1-e^{-2t}}-\frac1{2t}
\]

and the same exact shift matrix element integrated over \(0\le t\le2\).

---

## 2. External-audit sign guardrail

External audit round 17 landed immediately before this checkpoint.

It found a genuine sign error in the boxed exact shift formula of v13.314. The magnitude estimates used there were unaffected, because the downstream bounds used absolute values.

The same audit independently checked the restated v13.315 joint-prime formula against direct integrations and found it correct.

Therefore v13.316 uses only the v13.315 sign convention and explicitly treats the v13.314 exact-sign formula as superseded.

This is now a standing guardrail: any future exact matrix formula should be spot-checked against direct numerical integration before being promoted to proof input.

---

## 3. Finite buffer spectrum

Using odd modes \(21\le n\le M\), the lowest three numerical eigenvalues of the buffer principal block stabilize as follows:

| max odd mode | dimension | lowest | second | third |
|---:|---:|---:|---:|---:|
| 101 | 41 | 0.2770155047 | 0.7247459982 | 0.7690140733 |
| 151 | 66 | 0.2720499136 | 0.7232711223 | 0.7676628382 |
| 201 | 91 | 0.2704332502 | 0.7228127757 | 0.7672403231 |
| 237 | 109 | 0.2694541597 | 0.7225194468 | 0.7669689618 |
| 301 | 141 | 0.2682529544 | 0.7221678365 | 0.7666493294 |
| 351 | 166 | 0.2676602054 | 0.7219928057 | 0.7664917560 |
| 399 | 190 | 0.2672594580 | 0.7218751369 | 0.7663866321 |

Thus the finite buffer is numerically separated from zero by roughly

\[
\boxed{0.2673}
\]

at \(n\le399\).

This is evidence that the extreme near-null behavior is genuinely concentrated in the low modes rather than spread uniformly through the high finite buffer.

It is not yet a certified lower bound for the infinite complement, because the noncompact prime interface between the finite buffer and the remote tail remains to be enclosed.

---

## 4. Core-buffer coupling

For the split

\[
\mathcal C=\{1,3,\ldots,19\},\qquad
\mathcal B=\{21,23,\ldots,399\},
\]

the numerical coupling norms are

\[
\boxed{\|A_{CB}\|_2\approx0.7585905314}
\]

and

\[
\|A_{CB}\|_F\approx0.8269309438.
\]

A scalar Schur estimate based only on \(\|A_{CB}\|_2\) would therefore be much too crude near the low core.

---

## 5. Finite Feshbach correction is highly anisotropic

Define the finite Feshbach correction

\[
\Delta_{399}
=A_{CB}A_{BB}^{-1}A_{BC}.
\]

Its numerical spectral norm is

\[
\|\Delta_{399}\|_2\approx0.7124128392.
\]

However, its eigenvalues are strongly hierarchical:

\[
\begin{aligned}
&1.0\times10^{-17},\quad
7.8\times10^{-17},\quad
6.7\times10^{-13},\quad
1.0\times10^{-11},\\
&2.74\times10^{-8},\quad
1.38\times10^{-5},\quad
7.06\times10^{-5},\\
&1.11\times10^{-2},\quad
8.27\times10^{-2},\quad
7.124\times10^{-1}.
\end{aligned}
\]

Therefore

\[
\boxed{\text{the buffer correction is large in norm but effectively very low-dimensional.}}
\]

This is the central structural lesson of v13.316.

Replacing \(\Delta\) by \(\|\Delta\|I\) destroys precisely the geometry we need to preserve near the near-null subspace.

---

## 6. High-precision low-core spectrum

The \(10\times10\) core block on

\[
\{1,3,5,7,9,11,13,15,17,19\}
\]

was independently rebuilt at 60 decimal digits using mpmath, exact Si/Ci cusp formulas, the exact v13.315 prime matrix, one-dimensional high-precision archimedean integration, and the exact pole rank-one term.

The eigenvalues are

\[
\boxed{
1.1238941579916487\times10^{-20}
}
\]

\[
9.418812016765692\times10^{-16},
\]

\[
1.1214395739262330\times10^{-11},
\]

\[
4.7655600306065636\times10^{-8},
\]

\[
7.530016454725689\times10^{-5},
\]

\[
3.804528164115230\times10^{-2},
\]

followed by

\[
1.3421747575,
\quad1.7615486763,
\quad2.0591198594,
\quad2.46994327698.
\]

The first eigenvalue agrees with the v13.295 M20 value.

The new point is that the low block contains a whole multiscale hierarchy rather than one isolated tiny direction.

This does **not** imply six exact zero modes. The correct statement is only:

\[
\boxed{\text{the finite low core contains a strongly hierarchical near-null subspace.}}
\]

---

## 7. Consequence for the Feshbach strategy

The previous working picture was a single near-null vector coupled to a positive buffer and a coercive tail.

v13.316 refines this to

\[
\boxed{
\text{multiscale low near-null subspace}
\oplus
\text{numerically gapped finite buffer}
\oplus
\text{certified remote tail}.
}
\]

The buffer gap is encouraging, but the scalar norm of the finite Feshbach correction is misleading. The correction matrix itself must be retained.

The next useful object is therefore not a scalar Schur penalty but a small effective matrix on the low spectral subspace,

\[
F(\lambda)
=A_{CC}-\lambda
-A_{CB}(A_{BB}-\lambda)^{-1}A_{BC},
\]

with the remote tail incorporated as a matrix-valued enclosure rather than a scalar worst-case subtraction.

---

## 8. Proof-status guardrails

This checkpoint establishes or records:

- exact finite-matrix formulas for cusp/prime/pole structure inherited from earlier certified steps;
- a numerical finite-buffer gap near 0.2673 through mode 399;
- a numerical finite Feshbach correction with strongly anisotropic spectrum;
- a 60-digit finite-core near-null hierarchy.

It does **not** establish:

- positivity of the infinite complement \(n\ge21\);
- existence or multiplicity of an exact kernel;
- \(\lambda_1(a=1)=0\);
- RH or GRH.

The smallest finite eigenvalues remain Ritz data only.

---

## 9. Reproducibility

Companion script:

`research-notes/suzuki_feshbach_buffer_anatomy.py`

The large finite block uses ordinary double precision with a 500-point Gauss-Legendre archimedean integral. The low \(10\times10\) core is independently recomputed at 60-digit mpmath precision.

---

## 10. Next target

The next checkpoint should project onto the numerically resolved low spectral subspace rather than the raw first ten coordinate modes.

A practical route is:

1. choose the first 5-6 high-precision core eigenvectors as the active subspace;
2. treat the remaining core directions plus \(21\le n\le399\) as a finite positive buffer;
3. compute the matrix-valued finite Feshbach map on the active subspace;
4. derive a remote-tail matrix enclosure using the v13.315 exact prime sequence and compact cusp/arch bounds;
5. determine whether the effective low-dimensional matrix can be enclosed in sign without collapsing it to a scalar norm bound.

That is now the highest-leverage route toward a rigorous global sign statement in the even-v sector.
