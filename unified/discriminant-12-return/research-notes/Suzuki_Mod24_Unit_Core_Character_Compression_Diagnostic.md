# Suzuki Mod-24 Unit-Core Character Compression Diagnostic

Date: 2026-09-14

Status labels: **[D]** exact linear algebra / definition; **[N]** binary64/scipy midpoint diagnostic; **[Audit]** limitation / non-theorem.

## 1. Purpose

This note continues the unit-core/mod-24 diagnostic of ledger v13.423 and the all-character Hadamard transform of v13.429.  The question is deliberately narrow:

> Does the actual pole-free Suzuki finite-high operator show any approximate V4/character structure at the level of class-average coupling?

This is not a claim that the Suzuki operator has a V4 symmetry.  The current positivity target and source-faithful matrix construction remain unchanged.

## 2. Source matrix and unit-core classes [D/N]

Use the existing source-faithful midpoint script

`research-notes/suzuki_even_mode_unit_core_mod24_diagnostic.py`

which reconstructs

\[
B=A_{FF}^{(0)}-0.53I,
\qquad
F=\{22,24,\ldots,4000\}.
\]

For each even Fourier mode define its unit core

\[
u(n)=\frac{n}{2^{v_2(n)}3^{v_3(n)}}\pmod{12}
\in\{1,5,7,11\}.
\]

The four class sizes are

\[
N_1=518,\qquad N_5=499,\qquad N_7=492,\qquad N_{11}=481.
\]

Let

\[
e_r=\frac{1}{\sqrt{N_r}}\mathbf 1_{\{u(n)=r\}}
\]

be the normalized class-indicator vectors.  They are orthonormal because their supports are disjoint.

Define the exact four-dimensional compression operation

\[
C_{rs}=e_r^TBe_s,
\qquad r,s\in\{1,5,7,11\}.
\]

The definition is exact linear algebra; the following entries are midpoint numerics inherited from the current source-faithful binary64/scipy reconstruction.

## 3. Full unit-core compression [N]

In class order \((1,5,7,11)\),

\[
C\approx
\begin{pmatrix}
5.14243214&-0.19510244&-0.16688223&-0.16814434\\
-0.19510244&5.26538070&-0.14659515&-0.17857258\\
-0.16688223&-0.14659515&5.29176780&-0.13757489\\
-0.16814434&-0.17857258&-0.13757489&5.27574075
\end{pmatrix}.
\]

Its eigenvalues are approximately

\[
\boxed{
4.73600920,\quad
5.37132507,\quad
5.41688232,\quad
5.45110481.
}
\]

Thus the constant-on-unit-core subspace is very far from the nearly critical full direction:

\[
\lambda_{\min}(B)\approx0.002842383786,
\qquad
\lambda_{\min}(C)\approx4.73600920.
\]

So any class-average reduction alone cannot explain the live small margin.

## 4. Hadamard character basis [D/N]

Let

\[
H_4=
\begin{pmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{pmatrix},
\qquad
Q=\frac12H_4,
\]

so \(Q\) is orthogonal.  The row order is

\[
(1,\chi_{-4},\chi_{-3},\chi_{12}).
\]

Conjugating the compression gives

\[
\widehat C=QCQ^T.
\]

Numerically,

\[
\widehat C\approx
\begin{pmatrix}
4.74739454&-0.06868771&-0.02088520&-0.04551850\\
-0.06868771&5.40758883&-0.02396930&-0.03257555\\
-0.02088520&-0.02396930&5.39481135&-0.01116015\\
-0.04551850&-0.03257555&-0.01116015&5.42552668
\end{pmatrix}.
\]

The off-diagonal Frobenius norm falls from

\[
\|C-\operatorname{diag}C\|_F\approx0.57704820
\]

to

\[
\|\widehat C-\operatorname{diag}\widehat C\|_F\approx0.13406245,
\]

a ratio of about

\[
\boxed{0.2323.}
\]

This is numerical evidence that the Hadamard basis is a substantially better class-average basis, but it is not close enough here to call the full unit-core compression character-diagonal.

## 5. Balanced first even stratum: exact mod-24 lift [D/N]

Now restrict to the stratum

\[
v_2(n)=1,
\qquad 3\nmid n.
\]

As proved in v13.423,

\[
\begin{array}{c|cccc}
n\bmod24&2&10&14&22\\
\hline
u=n/2\bmod12&1&5&7&11
\end{array}
\]

and each class occurs exactly 166 times on the finite-high range.  Hence the four normalized residue indicators have exactly equal support size.

The resulting compression is

\[
C_{24}\approx
\begin{pmatrix}
5.34419840&-0.05552908&-0.05752915&-0.05398995\\
-0.05552908&5.34332723&-0.05719122&-0.05339531\\
-0.05752915&-0.05719122&5.35859364&-0.05538436\\
-0.05398995&-0.05339531&-0.05538436&5.33092063
\end{pmatrix}.
\]

Its eigenvalues are

\[
\boxed{
5.17751806,\quad
5.38769748,\quad
5.39930798,\quad
5.41251638.
}
\]

Again, the compressed subspace is very safely positive and does not contain the dangerous global mode.

## 6. Near diagonalization on the balanced stratum [N]

Hadamard conjugation gives

\[
\widehat C_{24}=QC_{24}Q^T
\approx
\begin{pmatrix}
5.17775044&-0.00056952&0.00506913&-0.00509982\\
-0.00056952&5.39985607&-0.00830109&0.00920296\\
0.00506913&-0.00830109&5.39984505&-0.00042480\\
-0.00509982&0.00920296&-0.00042480&5.39958834
\end{pmatrix}.
\]

Hence every off-diagonal character-mixing entry has magnitude below

\[
\boxed{9.21\times10^{-3}}.
\]

The three nonprincipal diagonal channels are also tightly clustered:

\[
5.39985607,\qquad5.39984505,\qquad5.39958834.
\]

The principal channel is separated at about

\[
5.17775044.
\]

This is a much cleaner near-character decomposition than on the full unbalanced unit-core partition.

## 7. Projection onto the exact V4-circulant algebra [D/N]

A real symmetric four-class matrix is exactly diagonalized by the Hadamard character basis iff it belongs to the V4 convolution/circulant algebra.  For any symmetric \(4\times4\) matrix \(M\), the orthogonal Frobenius projection onto this algebra is

\[
\boxed{
\Pi_{V_4}(M)
=Q^T\operatorname{diag}(QMQ^T)Q.
}
\]

For \(C_{24}\),

\[
\Pi_{V_4}(C_{24})\approx
\begin{pmatrix}
5.34425997&-0.05545672&-0.05546223&-0.05559058\\
-0.05545672&5.34425997&-0.05559058&-0.05546223\\
-0.05546223&-0.05559058&5.34425997&-0.05545672\\
-0.05559058&-0.05546223&-0.05545672&5.34425997
\end{pmatrix}.
\]

The residual obeys

\[
\frac{\|C_{24}-\Pi_{V_4}(C_{24})\|_F}{\|C_{24}\|_F}
\approx
\boxed{1.89785\times10^{-3}}.
\]

Thus the balanced mod-24 class-average compression is about **0.19% away in relative Frobenius norm** from the exact V4-circulant algebra.

For comparison, the same relative residual for the full unit-core compression is about

\[
1.2763\times10^{-2},
\]

or roughly 1.28%.

## 8. Interpretation and guardrails [I/Audit]

The balanced mod-24 lift therefore does more than recover the four labels: at the level of class-average coupling, it produces a compression numerically very close to a matrix that is exactly character-diagonal.

A plausible reason for the improvement is that the first even stratum is perfectly balanced among the four lifted residue classes, while the full unit-core partition mixes many 2-adic and 3-adic strata with unequal class counts.  This is an interpretation, not yet a theorem.

Crucially:

\[
\boxed{
\text{near V4-circulant class averages}
\not\Rightarrow
\text{V4 symmetry of the full Suzuki operator}.
}
\]

The source matrix contains nonperiodic archimedean and prime-source dependence on the actual Fourier indices.  No exact commutation with the unit-core class action has been proved.

Also,

\[
\boxed{
\lambda_{\min}(C_{24})\approx5.1775
\gg
\lambda_{\min}(B)\approx0.0028424.
}
\]

Therefore the near-critical global direction lives largely outside the constant-on-class subspace.  Any positivity use would require a controlled decomposition into class-average directions plus within-class fluctuations and certified bounds on their coupling.

## 9. Relation to the earlier character-mass diagnostic [I/Audit]

v13.429 observed that the lowest-vector **class masses** have their largest nonprincipal Hadamard imbalance in the \(\chi_{-3}\) channel.  The present calculation answers a different question: the operator's class-average compression is nearly character-diagonal on the balanced mod-24 stratum.

These facts are compatible but should not be conflated:

- mass imbalance concerns one eigenvector after squaring amplitudes classwise;
- \(C_{24}\) concerns operator matrix elements between normalized class indicators;
- neither alone determines the full near-critical eigenspace.

## 10. Next exact/numerical target

The next useful decomposition is

\[
\mathcal H
=\mathcal H_{\mathrm{class-avg}}
\oplus
\mathcal H_{\mathrm{within-class}},
\]

with the first summand spanned by the four normalized class indicators (or their Hadamard combinations).  Compute the cross operator

\[
P_{\mathrm{avg}}B(I-P_{\mathrm{avg}})
\]

and its norm, first on the balanced mod-24 stratum and then on the full finite-high block.  This will quantify exactly how strongly the nearly character-diagonal class-average sector couples to the fluctuation sector where the dangerous direction must live.

---

**Checkpoint conclusion.** The mod-24 lift uncovers a genuine numerical near-symmetry at the class-average level: on the balanced first even stratum the Suzuki compression is only about 0.19% away from the exact V4-circulant algebra, and the Hadamard character basis nearly diagonalizes it.  But this sector remains safely positive and far from the live near-critical mode.  The next question is therefore the certified or tightly bounded coupling from this near-character class-average sector into within-class fluctuations.