# Cone Derivation Ledger v13.828 — Numerical Grouped \(P_4\) Residue Polynomial and Uniform Inner-Window Enclosure

Date: 2026-09-27.

Lane: A.

Status: [N/C] residual-certified numerical grouped-residue center \(\widehat G(\delta)=C(\delta)^*\widehat P_4C(\delta)\) evaluated as an exact \(2\times2\) quadratic polynomial in \(\delta\); [C] uniform numerical-center Loewner enclosure on \(|\delta|\le0.02\); [C] immediate exact grouped-residue enclosure after combining with the externally audited v13.826 projector-error band; [G] no low-core determinant zero count or individual-channel residue claim yet.

Parents: v13.824–827.

Research artifact:

- research-notes/suzuki_grouped_residue_numerical_evaluation.py
  - commit 35984f15326cfc7acb820113f8322d0f55407d8a

External Audit Round 109, v13.827, independently replayed and confirmed the v13.826 grouped-residue projector-error certificate used in Section 8 below.

No GitHub workflow/status run is attached to the present numerical-center evaluation.

## 1. Numerical grouped residue

Let

\[
\widehat P_4
\]

be the orthogonal projector in transformed tail space onto the residual-certified numerical four-space of v13.824/v13.825.

Because the numerical basis \(\widehat Q_4\) is \(B_T\)-orthonormal,

\[
Y=B_T^{1/2}\widehat Q_4
\]

is orthonormal and

\[
\widehat P_4=YY^*.
\]

Therefore

\[
\widehat G(\delta)
=
C(\delta)^*\widehat P_4C(\delta)
\]

reduces exactly to

\[
\boxed{
\widehat G(\delta)
=
K(\delta)^TK(\delta),
}
\]

where

\[
K(\delta)
=
\widehat Q_4^TF_{TC}(\delta).
\]

Since

\[
F_{TC}(\delta)
=
A_{TC}-\delta B_{TC},
\]

one has

\[
K(\delta)=K_0-\delta K_1.
\]

Hence

\[
\boxed{
\widehat G(\delta)
=
G_0-\delta G_1+\delta^2G_2,
}
\]

with

\[
G_0=K_0^TK_0,
\]

\[
G_1=K_0^TK_1+K_1^TK_0,
\]

\[
G_2=K_1^TK_1\succeq0.
\]

No interval grid is needed.

## 2. Even-v polynomial coefficients

The reconstructed numerical four-space gives

\[
K_{0,e}
=
\begin{pmatrix}
2.4342088288\times10^{-14} & 7.3337777477\times10^{-14}\\
-9.7213595234\times10^{-12} & -2.9814713557\times10^{-11}\\
1.4373614920\times10^{-9} & 3.5315163723\times10^{-9}\\
7.7242566513\times10^{-6} & 2.2838239141\times10^{-5}
\end{pmatrix},
\]

\[
K_{1,e}
=
\begin{pmatrix}
0.0543593481240 & 0.0361580969593\\
-0.111678966066 & -0.0785217604605\\
-0.282935042702 & -0.208908126985\\
-0.425759131511 & -0.327852139045
\end{pmatrix}.
\]

Thus

\[
G_{0,e}
=
\begin{pmatrix}
5.9664142882\times10^{-11}
&
1.7640842566\times10^{-10}\\
1.7640842566\times10^{-10}
&
5.2158517952\times10^{-10}
\end{pmatrix},
\]

\[
G_{1,e}
=
\begin{pmatrix}
-6.5781567928\times10^{-6}
&
-1.2257298296\times10^{-5}\\
-1.2257298296\times10^{-5}
&
-1.4976601946\times10^{-5}
\end{pmatrix},
\]

\[
G_{2,e}
=
\begin{pmatrix}
0.276750206644
&
0.209428231415\\
0.209428231415
&
0.158602705438
\end{pmatrix}.
\]

Therefore

\[
\boxed{
\widehat G_e(\delta)
=
G_{0,e}
-
\delta G_{1,e}
+
\delta^2G_{2,e}.
}
\]

## 3. Odd-v polynomial coefficients

For odd-v,

\[
K_{0,o}
=
\begin{pmatrix}
-7.9011622362\times10^{-13} & -1.8215276775\times10^{-12}\\
-1.3842278501\times10^{-10} & -3.5379033276\times10^{-10}\\
2.9347887660\times10^{-7} & 5.3649516048\times10^{-7}\\
4.6763272113\times10^{-4} & 9.5182650110\times10^{-4}
\end{pmatrix},
\]

\[
K_{1,o}
=
\begin{pmatrix}
-0.0379474538573 & -0.0278565532462\\
-0.0783720945448 & -0.0600474561456\\
-0.152839203425 & -0.123909965254\\
-0.301000889322 & -0.254212283453
\end{pmatrix}.
\]

Hence

\[
G_{0,o}
=
\begin{pmatrix}
2.1868044800\times10^{-7}
&
4.4510537420\times10^{-7}\\
4.4510537420\times10^{-7}
&
9.0597397602\times10^{-7}
\end{pmatrix},
\]

\[
G_{1,o}
=
\begin{pmatrix}
-2.8160541827\times10^{-4}
&
-4.0549693149\times10^{-4}\\
-4.0549693149\times10^{-4}
&
-4.8406488820\times10^{-4}
\end{pmatrix},
\]

\[
G_{2,o}
=
\begin{pmatrix}
0.121543551934
&
0.101219553961\\
0.101219553961
&
0.0843592490961
\end{pmatrix}.
\]

Thus

\[
\boxed{
\widehat G_o(\delta)
=
G_{0,o}
-
\delta G_{1,o}
+
\delta^2G_{2,o}.
}
\]

## 4. Explicit endpoint matrices

### even-v, \(\delta=-0.02\)

\[
\boxed{
\widehat G_e(-0.02)
=
\begin{pmatrix}
1.10568579186\times10^{-4}
&
8.35263230085\times10^{-5}\\
8.35263230085\times10^{-5}
&
6.31420717215\times10^{-5}
\end{pmatrix}.
}
\]

Its eigenvalues are

\[
\boxed{
2.81117595124\times10^{-8},
\qquad
1.73682539148\times10^{-4}.
}
\]

### even-v, \(\delta=0\)

\[
\widehat G_e(0)
=
G_{0,e},
\]

with eigenvalues

\[
5.30\times10^{-20},
\qquad
5.81249322351\times10^{-10}.
\]

Thus the numerical grouped residue is essentially rank one and extremely small at the center.

### even-v, \(\delta=+0.02\)

\[
\boxed{
\widehat G_e(+0.02)
=
\begin{pmatrix}
1.10831705458\times10^{-4}
&
8.40166149404\times10^{-5}\\
8.40166149404\times10^{-5}
&
6.37411357993\times10^{-5}
\end{pmatrix}.
}
\]

Eigenvalues:

\[
\boxed{
3.29277257534\times10^{-8},
\qquad
1.74539913531\times10^{-4}.
}
\]

### odd-v, \(\delta=-0.02\)

\[
\boxed{
\widehat G_o(-0.02)
=
\begin{pmatrix}
4.32039928562\times10^{-5}
&
3.28229883289\times10^{-5}\\
3.28229883289\times10^{-5}
&
2.49683758506\times10^{-5}
\end{pmatrix}.
}
\]

Eigenvalues:

\[
\boxed{
2.03217526299\times10^{-8},
\qquad
6.81520469541\times10^{-5}.
}
\]

### odd-v, \(\delta=0\)

\[
\widehat G_o(0)
=
G_{0,o},
\]

with eigenvalues

\[
7.20\times10^{-16},
\qquad
1.12465442330\times10^{-6}.
\]

### odd-v, \(\delta=+0.02\)

\[
\boxed{
\widehat G_o(+0.02)
=
\begin{pmatrix}
5.44682095869\times10^{-5}
&
4.90428655883\times10^{-5}\\
4.90428655883\times10^{-5}
&
4.43309713784\times10^{-5}
\end{pmatrix}.
}
\]

Eigenvalues:

\[
\boxed{
9.54977038503\times10^{-8},
\qquad
9.87036832614\times10^{-5}.
}
\]

## 5. Uniform Loewner enclosure

Because

\[
\widehat G(\delta)=K(\delta)^TK(\delta)\succeq0
\]

for every \(\delta\), the lower Loewner bound is exact:

\[
\widehat G(\delta)\succeq0.
\]

The map

\[
\delta\mapsto \|K_0-\delta K_1\|
\]

is convex. Therefore its maximum on

\[
[-0.02,0.02]
\]

occurs at an endpoint.

The larger endpoint norm is the \(+0.02\) value in both sectors.

Using widened public caps,

\[
\boxed{
0
\preceq
\widehat G_e(\delta)
\prec
1.75\times10^{-4}\,I_2
\qquad
(|\delta|\le0.02),
}
\]

and

\[
\boxed{
0
\preceq
\widehat G_o(\delta)
\prec
1.00\times10^{-4}\,I_2.
}
\]

No grid or interpolation argument enters these bounds.

## 6. Uniform entrywise enclosure

Each entry is an explicit scalar quadratic, so its extrema are obtained analytically from the two endpoints and the possible stationary point.

### even-v

The actual scalar quadratic extrema are approximately

\[
2.05746\times10^{-11}
<
(\widehat G_e)_{11}
<
1.1083171\times10^{-4},
\]

\[
-2.93865\times10^{-12}
<
(\widehat G_e)_{12}
<
8.4016615\times10^{-5},
\]

\[
1.68031\times10^{-10}
<
(\widehat G_e)_{22}
<
6.3741136\times10^{-5}.
\]

The fail-closed public enclosure is

\[
\boxed{
2.0\times10^{-11}
<
(\widehat G_e)_{11}
<
1.109\times10^{-4},
}
\]

\[
\boxed{
-3.0\times10^{-12}
<
(\widehat G_e)_{12}
<
8.402\times10^{-5},
}
\]

\[
\boxed{
1.6\times10^{-10}
<
(\widehat G_e)_{22}
<
6.375\times10^{-5}.
}
\]

### odd-v

The actual extrema are approximately

\[
5.55669\times10^{-8}
<
(\widehat G_o)_{11}
<
5.4468210\times10^{-5},
\]

\[
3.89888\times10^{-8}
<
(\widehat G_o)_{12}
<
4.9042866\times10^{-5},
\]

\[
2.11566\times10^{-7}
<
(\widehat G_o)_{22}
<
4.4330972\times10^{-5}.
\]

The public enclosure is

\[
\boxed{
5.5\times10^{-8}
<
(\widehat G_o)_{11}
<
5.447\times10^{-5},
}
\]

\[
\boxed{
3.8\times10^{-8}
<
(\widehat G_o)_{12}
<
4.905\times10^{-5},
}
\]

\[
\boxed{
2.1\times10^{-7}
<
(\widehat G_o)_{22}
<
4.434\times10^{-5}.
}
\]

## 7. Center-versus-projector-error scale

The numerical-center variation is extremely small compared with the already certified uncertainty in replacing \(P_4\) by \(\widehat P_4\).

From v13.826/v13.827,

\[
\|G_e-\widehat G_e\|<0.0086,
\]

\[
\|G_o-\widehat G_o\|<0.0152.
\]

By contrast,

\[
\sup_{|\delta|\le0.02}\|\widehat G_e(\delta)\|
<
1.75\times10^{-4},
\]

\[
\sup_{|\delta|\le0.02}\|\widehat G_o(\delta)\|
<
1.00\times10^{-4}.
\]

Thus the current exact grouped-residue uncertainty is dominated overwhelmingly by the \(P_4\)-subspace error, not by the numerical grouped-residue center.

This identifies the next accuracy bottleneck cleanly: improving the \(P_4\) subspace certificate would tighten the residue far more than refining the quadratic center evaluation.

## 8. Immediate enclosure for the exact grouped residue

The exact grouped residue is positive semidefinite:

\[
G(\delta)=C(\delta)^*P_4C(\delta)\succeq0.
\]

Combining positivity, the numerical-center Loewner cap, and the externally audited v13.826 projector error gives the simple full exact-residue enclosures

### even-v

\[
\boxed{
0
\preceq
G_e(\delta)
\prec
0.008775\,I_2.
}
\]

### odd-v

\[
\boxed{
0
\preceq
G_o(\delta)
\prec
0.01530\,I_2.
}
\]

These are deliberately coarse compared with the numerical center, but they are rigorous consequences of the present certified projector accuracy.

The sharper pointwise statement remains

\[
\boxed{
\widehat G_e(\delta)-0.0086I_2
\prec
G_e(\delta)
\prec
\widehat G_e(\delta)+0.0086I_2,
}
\]

\[
\boxed{
\widehat G_o(\delta)-0.0152I_2
\prec
G_o(\delta)
\prec
\widehat G_o(\delta)+0.0152I_2,
}
\]

together with

\[
G_e(\delta),G_o(\delta)\succeq0.
\]

## 9. Interpretation for the low-core Feshbach map

The grouped numerical residue is smooth, explicit, and very small across the certified inner window.

Its dominant behavior is quadratic in \(\delta\), because the \(K_0\) coupling to the numerical four-space is extremely small near the center while \(K_1\) is \(O(10^{-1})\).

This makes the low-core pole contribution highly sensitive to the denominators

\[
(\delta-\delta_j)^{-1},
\]

rather than to large residue numerators.

That observation is numerical, not yet an individual-channel theorem: the grouped projector has been evaluated, but the four nearly degenerate channel residues have not been separated.

## Guardrails

This entry does not:

- assign individually certified residues to the four tail eigenvalues;
- prove simplicity or positivity of the individual \(\delta_j\);
- certify the two-mode Feshbach determinant zero count;
- prove \(\kappa_0\) convergence;
- unblock \(\kappa_1\);
- imply RH or GRH.

## Result

The residual-certified numerical grouped residue is an explicit quadratic matrix polynomial

\[
\boxed{
\widehat G(\delta)=G_0-\delta G_1+\delta^2G_2,
}
\]

with the endpoint matrices listed above.

Uniformly for

\[
|\delta|\le0.02,
\]

\[
\boxed{
0\preceq\widehat G_e(\delta)\prec1.75\times10^{-4}I_2,
}
\]

\[
\boxed{
0\preceq\widehat G_o(\delta)\prec1.00\times10^{-4}I_2.
}
\]

Together with the externally audited projector-error certificate, the exact grouped residues satisfy the pointwise symmetric-matrix bands

\[
\boxed{
G_e(\delta)\in
\widehat G_e(\delta)+[-0.0086I_2,+0.0086I_2],
}
\]

\[
\boxed{
G_o(\delta)\in
\widehat G_o(\delta)+[-0.0152I_2,+0.0152I_2],
}
\]

with exact positivity \(G_e,G_o\succeq0\).
