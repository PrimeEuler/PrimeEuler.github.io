# Cone Derivation Ledger v13.678 — Canonical QR–Character Incidence Object: AG(2,2) Lines

Date: 2026-09-22

Status: exact finite incidence geometry. Continuation of the Pell/QR obstruction result now numbered v13.663 after collision repair and independently confirmed in External Audit Round 73 (v13.664).

## 0. Live synchronization

The live repository was checked before and immediately before this write. The Pell/QR entry originally written as v13.662 was correctly renumbered to v13.663 after a collision; v13.664 audited it successfully. Other threads have since advanced the global ledger through v13.677. No v13.678 entry is present at the final freshness check, so this entry claims v13.678.

## 1. The object

Let
\[
V=U(12)\cong\mathbf F_2^2=\{1,5,7,11\}
\]
be the regular QR/V4 carrier, pointed at the identity \(1\). Let
\[
V^\vee_{\!*}=\{\chi_{12},\chi_{-4},\chi_{-3}\}
\]
be its three nontrivial characters.

For each nontrivial character define the quotient map
\[
\pi_\chi:V\longrightarrow\{\pm1\},\qquad \pi_\chi(v)=\chi(v).
\]
Its two fibers are
\[
L_{\chi,+}=\ker\chi,\qquad L_{\chi,-}=V\setminus\ker\chi.
\]
Define
\[
\mathcal L=\{L_{\chi,\epsilon}:\chi\in V^\vee_{\!*},\ \epsilon=\pm1\}.
\]
Then \(|V|=4\), \(|\mathcal L|=6\), every block has two points, every point lies on three blocks, and two distinct points lie on exactly one block. Therefore
\[
\boxed{(V,\mathcal L,\in)\cong AG(2,2).}
\]

This is the canonical incidence/dual object assembled from the three quotient maps.

## 2. Explicit six lines

\[
\begin{array}{c|c|c}
\chi&L_{\chi,+}&L_{\chi,-}\\ \hline
\chi_{12}&\{1,11\}&\{5,7\}\\
\chi_{-4}&\{1,5\}&\{7,11\}\\
\chi_{-3}&\{1,7\}&\{5,11\}.
\end{array}
\]

The three quotient maps are literally the three parallel classes of AG(2,2). Equivalently, the dual/projective directions are the three nonzero characters \(V^\vee_{\!*}=PG(1,2)\), each with two affine translates.

## 3. Identification with the six-cycle carrier

Using the audited stabilizers from v13.658/v13.664 and the identity point gives
\[
\boxed{
\begin{aligned}
a&\leftrightarrow\{1,11\},&b&\leftrightarrow\{5,7\},\\
c&\leftrightarrow\{1,5\},&d&\leftrightarrow\{7,11\},\\
e&\leftrightarrow\{1,7\},&f&\leftrightarrow\{5,11\}.
\end{aligned}}
\]
Thus
\[
\boxed{\mathcal C_6\cong\mathcal L(AG(2,2))}
\]
as U(12)-sets. The six cycle states are the six affine lines on the four QR/V4 points.

## 4. Explicit U(12) action

U(12)=V acts on points by translation \(\tau_r(v)=rv\). On a line,
\[
\boxed{\tau_r(L_{\chi,\epsilon})=L_{\chi,\chi(r)\epsilon}.}
\]
Thus translations preserve each parallel class and exchange its two lines exactly when \(\chi(r)=-1\).

On the six lines:
\[
\boxed{
\begin{array}{c|c}
1&\mathrm{id}\\
5&(a\,b)(e\,f)\\
7&(a\,b)(c\,d)\\
11&(c\,d)(e\,f).
\end{array}}
\]
On points:
\[
5=(1\,5)(7\,11),\quad
7=(1\,7)(5\,11),\quad
11=(1\,11)(5\,7).
\]
Incidence is invariant: \(v\in L\iff rv\in rL\).

## 5. Dual action

For the translation subgroup U(12), the direction/character label is fixed; only the affine sign changes:
\[
(\chi,\epsilon)\mapsto(\chi,\chi(r)\epsilon).
\]
Hence
\[
\boxed{\mathcal L=\mathcal L_{\chi_{12}}\sqcup\mathcal L_{\chi_{-4}}\sqcup\mathcal L_{\chi_{-3}}.}
\]
Linearizing again gives
\[
\mathbf Q[\mathcal L]\cong3\mathbf1\oplus\chi_{12}\oplus\chi_{-4}\oplus\chi_{-3}.
\]

## 6. Full automorphism group and S4

The full affine automorphism group is
\[
AGL(2,2)=V\rtimes GL(2,2),
\]
of order \(4\cdot6=24\), and its faithful action on the four points gives
\[
\boxed{AGL(2,2)\cong S_4.}
\]
The quotient \(GL(2,2)\cong S_3\) permutes the three nonzero dual characters/directions.

Thus the tetrahedral S4 is exactly the full affine automorphism group of the four-point QR/V4 carrier, acting naturally on its six affine lines.

The stabilizer of a line has order \(24/6=4\). In this six-line action it is a cyclic C4 (equivalently the oriented-cycle stabilizer already established), hence
\[
\boxed{\mathcal L\cong S_4/C_4.}
\]

## 7. What is canonical and what remains marked

Canonical from the pointed V4/QR carrier are the four points, three nonzero characters, three quotient maps, six fibers, incidence relation, and translation formula
\[
(\chi,\epsilon)\mapsto(\chi,\chi(r)\epsilon).
\]

The labels \(a,\ldots,f\) identify this object with the already-established cycle carrier. Pointing V at the identity canonically selects the \(+\) line in each parallel class as the kernel line.

The construction does not canonically order the three directions. \(GL(2,2)\cong S_3\) can permute \(\{\chi_{12},\chi_{-4},\chi_{-3}\}\). Therefore it does not by itself resolve the sigma_A/sigma_B marking obstruction.

## 8. Pell/QR interpretation

The QR/V4 carrier is literally the point set. The three character quotients are the three parallel classes. Pell orientation selects only the \(\chi_{12}\) class:
\[
\boxed{V\xrightarrow{\chi_{12}}\{a,b\}.}
\]
The other classes encode the \(\chi_{-4}\) and \(\chi_{-3}\) quotients.

So v13.663's negative result becomes geometrically transparent: Pell singles out one direction of the affine plane; it does not supply new dynamics on all six lines. There remains no U(12)-equivariant map from all six lines back to the regular four-point set because line stabilizers are nontrivial while point stabilizers under translations are trivial.

## 9. Publication-safe synthesis

\[
\boxed{
\left(V=\mathbf F_2^2,\;
\mathcal L=\{\chi^{-1}(\epsilon):0\ne\chi\in V^\vee,\epsilon=\pm1\}\right)
=AG(2,2).
}
\]

Its four points are the QR/V4 states; its six lines are the S4/C4 cycle states; its three parallel classes are the three quadratic-character quotients; and U(12) acts by translations
\[
\boxed{r:(\chi,\epsilon)\mapsto(\chi,\chi(r)\epsilon).}
\]

Thus the four-state QR carrier and six-state cone/cycle carrier are not competing realizations: they are the points and lines of one finite affine incidence geometry.

## 10. Next controlled test

Test whether the semilinear cone reversal
\[
\rho=(a\,b)(c\,d)(e\,f)
\]
extends to an incidence automorphism of this AG(2,2) point-line object, and whether any such extension supplies a canonical marking of the three directions or instead reproduces the existing sigma_A/sigma_B obstruction.
