# Cone Derivation Ledger v13.433 — Suzuki Mod-24 Class-Average / Fluctuation Schur Diagnostic

Date: 2026-09-14

Status labels: **[D]** exact linear-algebra identity, **[N]** numerical midpoint diagnostic, **[Audit]** guardrail.

## 0. Synchronization [Audit]

This checkpoint was assigned only after two live-ledger checks. The numbered ledger had advanced through v13.432, with the V4 all-character entry renumbered there and v13.431 occupied by the cyclotomic zeta intertwiner graph. A final explicit search found no existing `v13.433` entry immediately before this write.

This entry continues the Suzuki mod-24 unit-core compression diagnostic previously recorded at v13.430.

## 1. Balanced mod-24 class-average projector [D]

On the finite-high even mode set

\[
F=\{22,24,\dots,4000\},
\]

use the balanced first even stratum

\[
v_2(n)=1,\qquad 3\nmid n.
\]

The exact mod-24 lift gives four equal classes

\[
2,10,14,22\pmod{24},
\]

each of cardinality 166, mapping under division by 2 to unit-core labels

\[
1,5,7,11\pmod{12}.
\]

Let \(U\) have as columns the four normalized class-indicator vectors and set

\[
P=UU^T,\qquad Q=I-P.
\]

Thus \(P\) has rank four.

## 2. Exact block and Schur decomposition [D]

For the shifted source-faithful pole-free matrix

\[
B=A_{FF}^{(0)}-0.53I,
\]

write

\[
B=
\begin{pmatrix}
C&K^T\\
K&D
\end{pmatrix}
\]

relative to \(P\oplus Q\), where

\[
C=U^TBU,\qquad
K=QBU,\qquad
D=QBQ|_{Q\mathcal H}.
\]

If \(C\succ0\), then

\[
\boxed{
B\succ0
\iff
S:=D-KC^{-1}K^T\succ0.
}
\]

The correction \(KC^{-1}K^T\) has rank at most four.

## 3. Safe average block [N]

The class-average compression is

\[
C\approx
\begin{pmatrix}
5.34419840&-0.05552908&-0.05752915&-0.05398995\\
-0.05552908&5.34332723&-0.05719122&-0.05339531\\
-0.05752915&-0.05719122&5.35859364&-0.05538436\\
-0.05398995&-0.05339531&-0.05538436&5.33092063
\end{pmatrix},
\]

with eigenvalues approximately

\[
\boxed{
5.17751806,\ 5.38769748,\ 5.39930798,\ 5.41251638.
}
\]

Therefore the average sector is safely positive and far from the global near-critical scale.

## 4. Average-to-fluctuation coupling [N]

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

Hence

\[
\boxed{
\|PBQ\|_2=\|QBP\|_2\approx1.50321699.
}
\]

This is not a small perturbation.

## 5. Fluctuation block and failure of scalar norm control [N/Audit]

The smallest positive eigenvalue of the projected fluctuation block is

\[
\boxed{
\lambda_{\min}(D)\approx0.01364327.
}
\]

This exceeds the full midpoint minimum

\[
\lambda_{\min}(B)\approx0.002842383786.
\]

However the crude bound

\[
\lambda_{\min}(D)-\frac{\|K\|_2^2}{\lambda_{\min}(C)}
\]

is negative. Therefore a norm-only Schur estimate is unusable.

This mirrors the earlier failure of four-block Gershgorin bounds: the coupling is structured but not small in operator norm.

## 6. Exact rank-4 Schur feedback reproduces the critical scale [N]

Retaining the full low-rank correction gives

\[
S=D-KC^{-1}K^T.
\]

Its smallest positive midpoint eigenvalue is

\[
\boxed{
\lambda_{\min}(S)\approx0.00284918.
}
\]

This is extremely close in scale to

\[
\lambda_{\min}(B)\approx0.00284238.
\]

Schur complementation preserves positivity rather than eigenvalues, so equality is neither expected nor claimed. The diagnostic conclusion is instead:

\[
\boxed{
\text{near-criticality lives in the fluctuation sector after rank-4 feedback from safe class averages.}
}
\]

## 7. Character structure of the coupling Gram matrix [N]

The class-space Gram matrix is

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

one obtains

\[
Q_4K^TKQ_4^T\approx
\begin{pmatrix}
2.25804074&0.00251604&-0.01483847&0.01778542\\
0.00251604&1.75246851&0.03448620&-0.02802276\\
-0.01483847&0.03448620&1.84389050&-0.01167941\\
0.01778542&-0.02802276&-0.01167941&1.95553185
\end{pmatrix}.
\]

Thus the average-to-fluctuation coupling energy is approximately separated into the four character channels

\[
(\mathbf1,\chi_{-4},\chi_{-3},\chi_{12}).
\]

The diagonal channel strengths are

\[
\boxed{
2.2580,\ 1.7525,\ 1.8439,\ 1.9555,
}
\]

while the largest off-diagonal entry is only about \(3.45\times10^{-2}\).

## 8. Feedback is genuinely rank four [N]

The four nonzero eigenvalues of

\[
C^{-1/2}K^TKC^{-1/2}
\]

are approximately

\[
\boxed{
0.32151382,\ 0.34311080,\ 0.36329337,\ 0.43641459.
}
\]

Hence the low-rank feedback is not numerically rank one. All four average directions participate.

## 9. Relation to v13.431 cyclotomic intertwiner [I/Audit]

The newly landed v13.431 checkpoint proves an exact \(V_4\)-character intertwiner graph for multiplication by \(\zeta_{12}\) in \(\mathbf Q(\zeta_{12})\), with an intrinsic \(\chi_{-3}\) bipartition.

The present Suzuki result is different:

- it is numerical, not exact;
- it concerns a finite analytic operator rather than cyclotomic multiplication;
- its Hadamard structure appears in a compressed coupling Gram matrix after the mod-24 unit-core lift.

Therefore the common language of \(V_4\) characters is useful, but no operator intertwining between the cyclotomic and Suzuki carriers is claimed.

## 10. Positivity-program consequence [Audit]

The mod-24/V4 organization suggests a sharper certification route:

\[
\boxed{
\text{certify }D\text{ together with an outward enclosure of the explicit rank-4 correction }KC^{-1}K^T.
}
\]

This is materially better targeted than a global norm bound because the scalar estimate loses the sign/geometry of the four coupling channels and fails by a wide margin.

The currently active source-faithful certification work on rational prime-trigonometric propagation, cusp bounds, and even-mode archimedean terms remains the rigorous path. The present Schur result is a structural diagnostic that may make the final finite-high proof more economical once those ingredients are outward-certified.

---

**Checkpoint conclusion.** The balanced mod-24 class-average sector is strongly positive and nearly character-diagonal, but it couples to the fluctuation space with norm about 1.50. Crude norm control fails. The exact rank-4 Schur correction lowers the projected fluctuation minimum from about 0.01364 to about 0.002849, reproducing the live near-critical scale. The coupling Gram matrix is itself almost diagonal in the four V4 character channels, suggesting an outward-certified low-rank Schur treatment rather than a forced character block decomposition.
