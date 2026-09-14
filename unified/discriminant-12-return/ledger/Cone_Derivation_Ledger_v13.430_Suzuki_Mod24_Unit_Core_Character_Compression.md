# Cone Derivation Ledger v13.430 — Suzuki Mod-24 Unit-Core Character Compression

Date: 2026-09-14

Status labels: **[D]** exact definition/linear algebra; **[N]** binary64/scipy midpoint diagnostic; **[Audit]** limitation/guardrail.

## 0. Synchronization

This entry was assigned only after two live ledger checks.  The latest numbered checkpoint before writing remained v13.429; no collision with v13.430 was present.

Relevant prior entries:

- v13.423: exact unit-core lift and exact mod-24 recovery of the four V4 labels on the first even stratum;
- v13.429: all-character exponential/Hadamard transform and the observation that the lowest-vector class-mass imbalance is largest in the chi_-3 channel;
- External Audit Round 30: independent numerical verification of the chi12 exponential generating transform.

The present entry asks a different operator-level diagnostic question: whether the source-faithful Suzuki matrix itself has an approximately character-diagonal **class-average compression**.

## 1. Four-dimensional unit-core compression [D]

Use the current pole-free finite-high midpoint matrix

\[
B=A_{FF}^{(0)}-0.53I,
\qquad F=\{22,24,\ldots,4000\},
\]

reconstructed by

`research-notes/suzuki_even_mode_unit_core_mod24_diagnostic.py`.

For each class \(r\in\{1,5,7,11\}\), let

\[
G_r=\{n\in F:u(n)\equiv r\pmod{12}\},
\qquad
u(n)=\frac{n}{2^{v_2(n)}3^{v_3(n)}},
\]

and define the normalized class indicator

\[
e_r=|G_r|^{-1/2}\mathbf1_{G_r}.
\]

Then

\[
\boxed{C_{rs}=e_r^TBe_s}
\]

is the exact compression of \(B\) to the constant-on-unit-core subspace.

The class sizes are

\[
518,\ 499,\ 492,\ 481.
\]

## 2. Full unit-core compression [N]

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

Its eigenvalues are

\[
\boxed{4.73600920,\ 5.37132507,\ 5.41688232,\ 5.45110481.}
\]

Since

\[
\lambda_{\min}(B)\approx0.002842383786,
\]

we have the decisive separation

\[
\boxed{\lambda_{\min}(C)\approx4.7360\gg\lambda_{\min}(B).}
\]

Thus the near-critical Suzuki direction is not contained in the constant-on-unit-core sector.

## 3. Character basis [D/N]

Let

\[
H_4=
\begin{pmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{pmatrix},
\qquad Q=\frac12H_4.
\]

The row order is \((1,\chi_{-4},\chi_{-3},\chi_{12})\), and \(Q\) is orthogonal.

The character-basis compression

\[
\widehat C=QCQ^T
\]

is numerically

\[
\widehat C\approx
\begin{pmatrix}
4.74739454&-0.06868771&-0.02088520&-0.04551850\\
-0.06868771&5.40758883&-0.02396930&-0.03257555\\
-0.02088520&-0.02396930&5.39481135&-0.01116015\\
-0.04551850&-0.03257555&-0.01116015&5.42552668
\end{pmatrix}.
\]

The off-diagonal Frobenius norm is reduced by a factor

\[
\boxed{
\frac{\|\widehat C-\operatorname{diag}\widehat C\|_F}
{\|C-\operatorname{diag}C\|_F}
\approx0.2323.
}
\]

So the Hadamard basis is a substantially better class-average basis, but the full unit-core compression is not exactly or nearly perfectly character-diagonal.

## 4. Balanced first even stratum and exact mod-24 lift [D]

Restrict to

\[
v_2(n)=1,
\qquad3\nmid n.
\]

Then v13.423 gives the exact lift

\[
\begin{array}{c|cccc}
n\bmod24&2&10&14&22\\
\hline
u=n/2\bmod12&1&5&7&11
\end{array}
\]

with exactly 166 modes in each of the four classes.

Let \(C_{24}\) be the normalized class-indicator compression on this stratum.

## 5. Balanced-stratum compression [N]

Numerically,

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
\boxed{5.17751806,\ 5.38769748,\ 5.39930798,\ 5.41251638.}
\]

Again the constant-on-class sector is safely positive and far from the global near-critical direction.

## 6. Near character diagonalization [N]

Hadamard conjugation gives

\[
\widehat C_{24}\approx
\begin{pmatrix}
5.17775044&-0.00056952&0.00506913&-0.00509982\\
-0.00056952&5.39985607&-0.00830109&0.00920296\\
0.00506913&-0.00830109&5.39984505&-0.00042480\\
-0.00509982&0.00920296&-0.00042480&5.39958834
\end{pmatrix}.
\]

Thus

\[
\boxed{
\max_{\chi\ne\psi}|(\widehat C_{24})_{\chi\psi}|
<9.21\times10^{-3}.
}
\]

The nonprincipal diagonal channels are nearly degenerate:

\[
5.39985607,\quad5.39984505,\quad5.39958834.
\]

## 7. Exact V4-circulant projection [D/N]

The Frobenius-orthogonal projection of any symmetric four-class matrix \(M\) onto the algebra exactly diagonalized by \(Q\) is

\[
\boxed{
\Pi_{V_4}(M)=Q^T\operatorname{diag}(QMQ^T)Q.
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

The relative Frobenius residual is

\[
\boxed{
\frac{\|C_{24}-\Pi_{V_4}(C_{24})\|_F}{\|C_{24}\|_F}
\approx1.89785\times10^{-3}.
}
\]

Thus the balanced mod-24 class-average compression is approximately **0.19% away** from the exact V4-circulant algebra.

For the full unit-core compression the corresponding relative residual is about

\[
1.2763\times10^{-2},
\]

or 1.28%.

## 8. Structural interpretation [I/Audit]

The exact mod-24 balancing markedly sharpens the numerical character structure at the class-average level.

A plausible interpretation is that mixing multiple 2-adic/3-adic strata and unequal class counts obscures the near-circulant structure present on the balanced first even stratum.  This is not yet derived from the source formula.

The following non-implications are binding:

\[
\boxed{
C_{24}\text{ nearly V4-circulant}
\not\Rightarrow
B\text{ has V4 symmetry}.
}
\]

\[
\boxed{
\widehat C_{24}\text{ nearly diagonal}
\not\Rightarrow
\text{the Suzuki positivity proof decomposes into four characters}.
}
\]

The source matrix contains actual-index-dependent prime and archimedean terms, and no exact commutator theorem has been proved.

## 9. Relation to v13.429 [Audit]

v13.429 found that the Hadamard transform of the lowest-vector **class masses** has its largest nonprincipal component in the chi_-3 channel.

The present entry concerns the operator's class-average compression.  These are different observables:

- squared eigenvector mass by class;
- matrix elements between normalized class-indicator directions.

The near-character compression therefore does not by itself explain the chi_-3-heavy mass imbalance or the global near-critical mode.

## 10. Next target

Let \(P\) be the orthogonal projector onto the four-dimensional class-average subspace.  Compute

\[
\boxed{PB(I-P)}
\]

and its operator norm, first for the balanced mod-24 stratum and then for the full unit-core decomposition.

Since the small global eigenvalue lies outside \(P\mathcal H\), the quantity

\[
\|PB(I-P)\|_2
\]

measures directly how strongly the safe, nearly character-diagonal class-average sector couples into the within-class fluctuation sector where the dangerous mode must live.

---

**Checkpoint conclusion.** The exact mod-24 lift uncovers a strong numerical near-symmetry in the Suzuki class-average compression: on the balanced first even stratum the compressed matrix is only about 0.19% away from the exact V4-circulant algebra, and Hadamard conjugation makes it nearly diagonal.  However the compressed minimum is about 5.1775 while the live full margin is about 0.0028424, so the nearly critical direction necessarily resides in within-class fluctuations and their coupling.  The next diagnostic is therefore the average-to-fluctuation cross norm, not a stronger V4 symmetry claim.