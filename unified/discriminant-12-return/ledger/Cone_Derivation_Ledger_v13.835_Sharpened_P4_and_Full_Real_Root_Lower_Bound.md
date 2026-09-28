# Cone Derivation Ledger v13.835 — Sharpened \(P_4\) Carrier and Exact Full Real-Root Lower Bound

Date: 2026-09-28.

Lane: A finite/resonance branch.

Status: [C] sharpened residual-certified numerical carrier for the exact rank-four tail projector; [C] exact full-pencil real-root lower bound from the externally audited endpoint spectral flow; [G] ordinary six-root count remains a separate \(2+4\)-dimensional Riesz/Feshbach gate.

Parents: v13.824–834.

Research artifact:

- research-notes/suzuki_tail_P4_block_energy_refinement.py
  - commit 8d8982919a279ab7f11593e29bef2674dab1ee08

External Audit Round 112, v13.834, independently executed and confirmed the full \(\rho=0.02\) endpoint theorem of v13.832:

\[
\operatorname{ind}_-(F^-_{0.02})=4,
\qquad
\operatorname{ind}_-(F^+_{0.02})=2,
\]

with zero kernel at both endpoints, in both parity sectors.

No GitHub workflow/status run is attached to the new block-energy refinement.

## 1. Block-energy sharpening of the unchanged numerical \(P_4\) basis

The numerical basis itself is exactly the v13.824 basis.

Only the transformed-residual estimate is changed.

Split the positive tail into finite and remote blocks

\[
\mathcal H_T=\mathcal H_F\oplus\mathcal H_R.
\]

The certified smooth-bulk geometry gives

\[
B_{FF}\ge bI,
\qquad
B_{RR}\ge gI,
\qquad
\|B_{FR}\|\le c,
\]

with public constants

\[
b_e=0.0415-10^{-10},
\qquad
b_o=0.2400-10^{-10},
\]

\[
c<0.417,
\qquad
g>5.33.
\]

For residual

\[
r=(r_F,r_R),
\]

define

\[
M=
\begin{pmatrix}
b&-c\\
-c&g
\end{pmatrix}.
\]

The quadratic-form lower bound on \(B_T\) and the dual variational formula imply

\[
\boxed{
\langle r,B_T^{-1}r\rangle
\le
\begin{pmatrix}
\|r_F\|\\
\|r_R\|
\end{pmatrix}^{T}
M^{-1}
\begin{pmatrix}
\|r_F\|\\
\|r_R\|
\end{pmatrix}.
}
\]

This avoids charging the entire residual against the weakest global tail floor.

## 2. Sharpened transformed residual

Using the audited finite residual caps

\[
\|r_{F,e}\|<2.60\times10^{-4},
\]

\[
\|r_{F,o}\|<1.31\times10^{-3},
\]

and, conservatively, the entire v13.824 Euclidean residual cap for the remote component, gives

\[
\boxed{
\|B_{T,e}^{-1/2}R_e\|<0.00542,
}
\]

\[
\boxed{
\|B_{T,o}^{-1/2}R_o\|<0.00832.
}
\]

The numerical four-space is unchanged.

## 3. Sharpened exact-projector error

The exact complementary tail spectrum lies outside

\[
[-0.10,0.10].
\]

The public Ritz-location caps are

\[
\max|\widehat\delta_j|<0.00030
\quad\text{even-v},
\]

\[
\max|\widehat\delta_j|<0.01050
\quad\text{odd-v}.
\]

Thus the certified separations from the complement are

\[
0.09970,
\qquad
0.08950.
\]

The invariant-subspace residual theorem gives

\[
\boxed{
\|P_{4,e}-\widehat P_{4,e}\|<0.0544,
}
\]

\[
\boxed{
\|P_{4,o}-\widehat P_{4,o}\|<0.0930.
}
\]

Equivalently,

\[
\boxed{
\theta_{\max,e}<3.12^\circ,
\qquad
\theta_{\max,o}<5.34^\circ.
}
\]

## 4. Sharpened grouped-residue error

The uniform coupling-energy caps remain

\[
\|C_e(\delta)\|^2<0.0256,
\qquad
\|C_o(\delta)\|^2<0.0416
\]

for

\[
|\delta|\le0.02.
\]

Hence

\[
\boxed{
\|C_e^*(P_{4,e}-\widehat P_{4,e})C_e\|<0.00140,
}
\]

\[
\boxed{
\|C_o^*(P_{4,o}-\widehat P_{4,o})C_o\|<0.00387.
}
\]

These supersede the older \(0.0086/0.0152\) projector-error bounds whenever the block-energy refinement is invoked.

## 5. Exact full real spectral flow

For the full parity pencil

\[
F(\delta)=A-\delta B_{\rm sm},
\]

External Audit Round 112 confirms

\[
\operatorname{ind}_-F(-0.02)=2,
\]

\[
\operatorname{ind}_-F(+0.02)=4.
\]

Both endpoint kernels are zero.

Thus the self-adjoint Fredholm path has spectral flow

\[
\boxed{
\operatorname{sf}\{F(\delta):-0.02\to+0.02\}=+2.
}
\]

The sign convention is that a positive-\(B\) crossing increases the negative Morse index by one.

## 6. Exact real-root lower bound

A nonzero spectral flow across an interval with invertible endpoints requires real singular parameters inside the interval.

More quantitatively, the absolute spectral flow cannot exceed the sum of the algebraic crossing multiplicities of the real singular points.

Therefore, in each parity sector,

\[
\boxed{
\sum_{\delta_*\in(-0.02,0.02)}
m_{\rm cross}(\delta_*)
\ge2.
}
\]

In particular,

\[
\boxed{
\text{the full generalized pencil has at least two real roots in }(-0.02,0.02),
}
\]

counting crossing multiplicity.

This conclusion is exact and infinite-dimensional; it does not come from the N=96 finite diagnostic.

## 7. Why this is not yet a six-root theorem

The certified positive tail problem has four generalized eigenvalues in the inner window.

After restoring the two negative-metric low-core directions, those tail eigenvalues become poles of the meromorphic two-mode Feshbach map. They are not automatically roots of the coupled full pencil.

The full smooth bulk has Pontryagin index two. This severely limits non-real and nonpositive-type spectral pathologies, but it does not by itself prove that four positive-type coupled roots remain in the interval.

Hence the implication

\[
4\ \text{tail roots}
+
2\ \text{full spectral-flow units}
\Rightarrow
6\ \text{full roots}
\]

is invalid without an additional coupled-root argument.

## 8. Final finite/resonance gate

The correct carrier is now

\[
\boxed{
\mathcal H_C\oplus\operatorname{Ran}P_4,
}
\]

of dimension

\[
2+4=6.
\]

The complement

\[
P_4^\perp
\]

has an exact \(0.08\) spectral moat throughout the inner window and hence can be eliminated as a uniformly regular analytic background.

The sharpened projector error of Sections 1–4 makes a certified numerical \(6\times6\) reduction substantially more accurate than was available at v13.824.

The remaining gate is to certify the Riesz/root count of this six-dimensional reduced full pencil, including exclusion or accounting of non-real pairs.

## Guardrails

This entry does not claim:

- exactly six full roots;
- reality or simplicity of all six candidate roots;
- that the four tail eigenvalues survive unchanged under low-core coupling;
- that signed spectral flow equals ordinary multiplicity in the Pontryagin pencil;
- anything about the separate Hilbert–Pólya boundary-normalization gate identified by v13.833.

## Result

The numerical tail carrier improves to

\[
\boxed{
\|P_{4,e}-\widehat P_{4,e}\|<0.0544,
\qquad
\|P_{4,o}-\widehat P_{4,o}\|<0.0930,
}
\]

and the exact full pencil satisfies

\[
\boxed{
N_{\rm real}^{\rm crossing}(-0.02,0.02)\ge2
}
\]

in each parity sector.

The sole remaining ordinary-multiplicity question in this finite/resonance branch is the certified \(2+4=6\) coupled Riesz/root count.
