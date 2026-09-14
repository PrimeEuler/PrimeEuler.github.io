# Suzuki Mod-24 Class-Average / Fluctuation Schur Diagnostic

Date: 2026-09-14

Status labels: **[D]** exact linear-algebra identity, **[N]** numerical midpoint diagnostic, **[Audit]** guardrail.

## 1. Setup

Use the source-faithful midpoint pole-free Suzuki finite-high matrix

\[
B=A_{FF}^{(0)}-0.53I,
\qquad F=\{22,24,\dots,4000\}.
\]

Restrict attention to the balanced first even stratum

\[
v_2(n)=1,\qquad 3\nmid n,
\]

whose four mod-24 classes are

\[
2,10,14,22\pmod{24},
\]

corresponding after division by 2 to the unit-core labels

\[
1,5,7,11\pmod{12}.
\]

Each class occurs exactly 166 times in the finite-high range.

Let \(U\in\mathbf R^{1990\times4}\) have as columns the four normalized class-indicator vectors, and define

\[
P=UU^T,\qquad Q=I-P.
\]

Thus \(P\) projects onto the four class-average directions and \(Q\) onto all within-class and outside-stratum fluctuations.

## 2. Block decomposition [D]

Relative to \(P\oplus Q\), write

\[
B=
\begin{pmatrix}
C & K^T\\
K & D
\end{pmatrix},
\]

where

\[
C=U^TBU,\qquad
K=QBU,\qquad
D=QBQ\big|_{Q\mathcal H}.
\]

The exact Schur complement is

\[
\boxed{
S=D-KC^{-1}K^T.
}
\]

Whenever \(C\succ0\), positivity of \(B\) is equivalent to positivity of \(S\).

This is an exact finite-dimensional linear-algebra identity. The values below are midpoint diagnostics only.

## 3. Safe class-average block [N]

The four-dimensional compression is

\[
C\approx
\begin{pmatrix}
5.34419840&-0.05552908&-0.05752915&-0.05398995\\
-0.05552908&5.34332723&-0.05719122&-0.05339531\\
-0.05752915&-0.05719122&5.35859364&-0.05538436\\
-0.05398995&-0.05339531&-0.05538436&5.33092063
\end{pmatrix}.
\]

Its eigenvalues are approximately

\[
5.17751806,\ 5.38769748,\ 5.39930798,\ 5.41251638.
\]

Hence the class-average sector is very far from the near-critical global scale.

## 4. Class-average / fluctuation coupling [N]

The singular values of

\[
K=QBU
\]

are approximately

\[
\boxed{
1.50321699,\ 1.40015505,\ 1.36070225,\ 1.31845573.
}
\]

Therefore

\[
\boxed{
\|PBQ\|_2=\|QBP\|_2\approx1.50321699.
}
\]

The coupling is not perturbatively small.

The fluctuation block itself has smallest positive eigenvalue

\[
\boxed{
\lambda_{\min}(D)\approx0.01364327.
}
\]

This is substantially larger than the full matrix minimum

\[
\lambda_{\min}(B)\approx0.002842383786.
\]

Thus removing the four class-average directions raises the raw fluctuation minimum, but the feedback through \(K\) lowers it again.

## 5. Norm-only Schur estimate fails badly [N/Audit]

The crude bound

\[
\lambda_{\min}(S)
\ge
\lambda_{\min}(D)
-
\frac{\|K\|_2^2}{\lambda_{\min}(C)}
\]

gives approximately

\[
0.01364327-\frac{1.50321699^2}{5.17751806}<0.
\]

So scalar norm control loses far too much, exactly as the earlier block-Gershgorin attempt did.

The structured rank-4 correction must be retained.

## 6. Exact rank-4 Schur correction [N]

Using the full low-rank operator

\[
KC^{-1}K^T,
\]

the smallest positive eigenvalue of the Schur complement is

\[
\boxed{
\lambda_{\min}(S)\approx0.00284918.
}
\]

This is extremely close in scale to the full midpoint minimum

\[
\lambda_{\min}(B)\approx0.00284238.
\]

The two eigenvalues need not coincide: Schur complementation preserves positivity, not the spectrum. But the numerical proximity shows that the near-critical scale is already present in the fluctuation block after the exact rank-4 feedback from the four class-average directions is integrated out.

Thus the correct structural statement is

\[
\boxed{
\text{safe class averages}
\xrightarrow{\text{rank-4 feedback}}
\text{near-critical fluctuation Schur complement}.
}
\]

## 7. Coupling Gram matrix in the V4 character basis [N]

The class-space coupling Gram matrix is

\[
K^TK\approx
\begin{pmatrix}
1.95260641&0.05986945&0.10507487&0.14595300\\
0.05986945&1.94319602&0.16265379&0.09189057\\
0.10507487&0.16265379&1.90949816&0.04567400\\
0.14595300&0.09189057&0.04567400&2.00463101
\end{pmatrix}.
\]

With normalized Hadamard matrix

\[
Q_4=\frac12H_4,
\]

its character-coordinate form is

\[
Q_4K^TKQ_4^T\approx
\begin{pmatrix}
2.25804074&0.00251604&-0.01483847&0.01778542\\
0.00251604&1.75246851&0.03448620&-0.02802276\\
-0.01483847&0.03448620&1.84389050&-0.01167941\\
0.01778542&-0.02802276&-0.01167941&1.95553185
\end{pmatrix}.
\]

So the average-to-fluctuation coupling energy is itself nearly character-diagonal on the balanced mod-24 stratum.

Its four diagonal channel strengths are approximately

\[
\boxed{
2.2580,\quad1.7525,\quad1.8439,\quad1.9555
}
\]

in the ordered character basis

\[
(\mathbf1,\chi_{-4},\chi_{-3},\chi_{12}).
\]

The largest off-diagonal character-mixing term in this Gram matrix is only about \(3.45\times10^{-2}\), much smaller than the diagonal channel energies.

## 8. Rank-4 feedback scale [N]

The four nonzero eigenvalues of the normalized feedback operator

\[
C^{-1/2}K^TKC^{-1/2}
\]

are approximately

\[
\boxed{
0.32151382,\ 0.34311080,\ 0.36329337,\ 0.43641459.
}
\]

Thus all four class-average directions participate in the feedback; it is not numerically rank one.

## 9. Relation to the cyclotomic character graph [I/Audit]

Ledger v13.431 independently shows that multiplication by \(\zeta_{12}\) has an exact \(V_4\)-character intertwiner graph with intrinsic \(\chi_{-3}\) bipartition. The present Suzuki diagnostic also finds an approximately character-diagonal class-space coupling Gram matrix after the mod-24 unit-core lift.

These are mathematically distinct carriers:

- the cyclotomic result is exact multiplication in \(\mathbf Q(\zeta_{12})\);
- the Suzuki result is a numerical compression of a finite analytic operator.

No intertwining between the two operators is claimed.

## 10. Consequence for the positivity program [Audit]

This diagnostic sharpens the earlier conclusion:

1. the four mod-24 class averages are very safe;
2. their coupling to fluctuations is large enough that norm-only estimates fail;
3. the exact coupling is only rank four;
4. integrating it out produces a Schur complement already at the near-critical positivity scale;
5. the coupling energy is almost separated by the four V4 characters.

Therefore a potentially useful certification strategy is not to block-diagonalize by characters, but to certify the fluctuation operator together with an explicit outward enclosure of the rank-4 Schur correction.

That would preserve the source-faithful Suzuki operator and use the mod-24/V4 structure only as a low-rank organizational device.
