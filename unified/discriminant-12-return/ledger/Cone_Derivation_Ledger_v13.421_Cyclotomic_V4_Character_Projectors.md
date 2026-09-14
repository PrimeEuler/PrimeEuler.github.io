# Cone Derivation Ledger v13.421 — Cyclotomic V4 Character Projectors

Date: 2026-09-14

Status labels: **[D]** exact derived, **[I]** interpretation, **[Audit]** limitation/guardrail.

## 0. Synchronization

This entry was assigned after checking the live ledger through `v13.420`. It continues the exact character-splitting picture from `v13.414` and `v13.416` and incorporates the external-audit confirmation of `v13.413`–`v13.416`.

## 1. Cyclotomic carrier and Galois action [D]

Let

\[
K_{12}=\mathbf Q(\zeta_{12}),
\qquad
\zeta:=\zeta_{12},
\]

with

\[
\Phi_{12}(X)=X^4-X^2+1,
\qquad
\zeta^4=\zeta^2-1.
\]

Use the integral power basis

\[
B=(1,\zeta,\zeta^2,\zeta^3).
\]

For

\[
r\in U(12)=\{1,5,7,11\},
\]

define

\[
\sigma_r(\zeta)=\zeta^r.
\]

Reducing powers with \(\zeta^4=\zeta^2-1\), the four Galois operators on the basis \(B\) are

\[
[\sigma_1]_B=
\begin{pmatrix}
1&0&0&0\\
0&1&0&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix},
\]

\[
[\sigma_5]_B=
\begin{pmatrix}
1&0&1&0\\
0&-1&0&0\\
0&0&-1&0\\
0&1&0&1
\end{pmatrix},
\]

\[
[\sigma_7]_B=
\begin{pmatrix}
1&0&0&0\\
0&-1&0&0\\
0&0&1&0\\
0&0&0&-1
\end{pmatrix},
\]

\[
[\sigma_{11}]_B=
\begin{pmatrix}
1&0&1&0\\
0&1&0&0\\
0&0&-1&0\\
0&-1&0&-1
\end{pmatrix}.
\]

These matrices commute, square to the identity, and realize

\[
\operatorname{Gal}(K_{12}/\mathbf Q)\cong V_4.
\]

## 2. The four real characters [D]

On the ordered group elements \((1,5,7,11)\), the four real characters are

\[
\mathbf 1=(+,+,+,+),
\]

\[
\chi_{-4}=(+,+,-,-),
\]

\[
\chi_{-3}=(+,-,+,-),
\]

\[
\chi_{12}=(+,-,-,+).
\]

As already recorded,

\[
\boxed{\chi_{12}=\chi_{-4}\chi_{-3}.}
\]

## 3. Group-algebra projectors [D]

For each character \(\chi\), define the rational projector

\[
\boxed{
P_\chi
=\frac14\sum_{r\in U(12)}\chi(r)\sigma_r.
}
\]

Direct matrix summation gives

\[
P_{\mathbf1}=
\begin{pmatrix}
1&0&\frac12&0\\
0&0&0&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix},
\]

\[
P_{-4}=
\begin{pmatrix}
0&0&0&0\\
0&0&0&0\\
0&0&0&0\\
0&\frac12&0&1
\end{pmatrix},
\]

\[
P_{-3}=
\begin{pmatrix}
0&0&-\frac12&0\\
0&0&0&0\\
0&0&1&0\\
0&0&0&0
\end{pmatrix},
\]

\[
P_{12}=
\begin{pmatrix}
0&0&0&0\\
0&1&0&0\\
0&0&0&0\\
0&-\frac12&0&0
\end{pmatrix}.
\]

Each has rank one, and

\[
P_\chi^2=P_\chi,
\qquad
P_\chi P_\psi=0\quad(\chi\ne\psi),
\]

with

\[
\boxed{
P_{\mathbf1}+P_{-4}+P_{-3}+P_{12}=I_4.
}
\]

Hence the regular \(V_4\)-representation carried by \(K_{12}\) decomposes over \(\mathbf Q\) into its four one-dimensional character lines.

## 4. Explicit character lines [D]

Using

\[
i=\zeta^3,
\qquad
\sqrt3=2\zeta-\zeta^3,
\qquad
i\sqrt3=2\zeta^2-1,
\]

one obtains

\[
\boxed{\operatorname{im}P_{\mathbf1}=\mathbf Q\cdot1,}
\]

\[
\boxed{\operatorname{im}P_{-4}=\mathbf Q\cdot i,}
\]

\[
\boxed{\operatorname{im}P_{-3}=\mathbf Q\cdot i\sqrt3,}
\]

\[
\boxed{\operatorname{im}P_{12}=\mathbf Q\cdot\sqrt3.}
\]

Thus

\[
\boxed{
K_{12}
=\mathbf Q\cdot1
\oplus\mathbf Q\cdot i
\oplus\mathbf Q\cdot i\sqrt3
\oplus\mathbf Q\cdot\sqrt3.
}
\]

Equivalently, in the character-adapted basis

\[
B_\chi=(1,i,i\sqrt3,\sqrt3),
\]

every Galois operator is diagonal with diagonal entries equal to the four character values.

## 5. Exact interpretation of the three nontrivial channels [D/I]

The three nontrivial one-dimensional lines now have direct operator meaning:

\[
\boxed{
\chi_{-4}\text{ channel}=\mathbf Q\cdot i,
}
\]

so \(\chi_{-4}\) records the sign of the complex direction.

\[
\boxed{
\chi_{12}\text{ channel}=\mathbf Q\cdot\sqrt3,
}
\]

so \(\chi_{12}\) records the sign of the real-quadratic direction and therefore the Pell-time orientation:

\[
\sigma_r(2+\sqrt3)=(2+\sqrt3)^{\chi_{12}(r)}.
\]

\[
\boxed{
\chi_{-3}\text{ channel}=\mathbf Q\cdot i\sqrt3,
}
\]

which is the product channel and is the one that survives as the nontrivial Galois action on the ramified residue field \(\mathbf F_4\), consistent with `v13.416`.

Therefore the character factorization

\[
\chi_{12}=\chi_{-4}\chi_{-3}
\]

has an exact field-theoretic carrier decomposition: the sign of \(\sqrt3\) equals the product of the signs of \(i\) and \(i\sqrt3\).

## 6. Relation to multiplication by zeta_12 [D]

The project also uses the integral operator

\[
\mathcal Z=\times\zeta_{12}
\]

on the ramified cyclotomic ideal.

The Galois projectors above are not spectral projectors of \(\mathcal Z\). Instead, Galois covariance gives

\[
\boxed{
\sigma_r\,\mathcal Z\,\sigma_r^{-1}
=\times\zeta_{12}^{\,r}.
}
\]

Thus multiplication by \(\zeta\) moves between the character lines rather than commuting with the entire Galois action.

In the character-adapted basis, this is the expected semilinear relation: the regular Galois decomposition and the cyclotomic multiplication operator are complementary structures, not one common diagonalization.

## 7. Integral versus rational decomposition [Audit]

The Galois matrices above are integral in the power basis \(B\), but the character projectors contain denominators \(1/2\) and \(1/4\) through the standard group-algebra averaging.

Therefore

\[
K_{12}=\bigoplus_\chi K_{12}^{(\chi)}
\]

is an exact \(\mathbf Q\)-linear character decomposition, but it is **not** by itself an integral direct-sum decomposition of \(\mathbf Z[\zeta_{12}]\).

This distinction is consistent with the already-recorded index

\[
[\mathcal O_{K_{12}}:\mathbf Z[\sqrt3,i]]=4.
\]

No claim is made that the four character lines independently form a \(\mathbf Z\)-basis of the full ring of integers.

## 8. Structural synthesis [I]

The exact operator picture is now

\[
\boxed{
V_4
\curvearrowright
K_{12}
=K_{\mathbf1}\oplus K_{-4}\oplus K_{-3}\oplus K_{12},
}
\]

with

\[
K_{\mathbf1}=\mathbf Q,
\quad
K_{-4}=i\mathbf Q,
\quad
K_{-3}=i\sqrt3\,\mathbf Q,
\quad
K_{12}=\sqrt3\,\mathbf Q.
\]

This gives a literal operator-level realization of the three character roles already observed separately:

- \(\chi_{-4}\): complex sign;
- \(\chi_{-3}\): ramified-residue/Frobenius sign;
- \(\chi_{12}\): real-quadratic/Pell-time sign.

The four mod-12 unit labels are therefore not merely a character table attached externally to the project: they are the simultaneous eigencharacters of the full cyclotomic Galois action on the four-dimensional field carrier.

## Guardrails

- The character lines are field/Galois eigenspaces, not the four geometric Cone shells.
- The Pell cyclic subgroup remains distinct from \(V_4\).
- The finite \(\mathbf F_4\) reduction loses the literal Pell multiplication because \(2+\sqrt3\equiv1\); only the transported/additive Frobenius layer remains.
- The rational projectors do not imply an integral splitting of \(\mathcal O_{K_{12}}\).
- No new Suzuki positivity estimate follows from this decomposition.

---

**Checkpoint conclusion.** The full cyclotomic Galois action admits an exact rank-one character decomposition over \(\mathbf Q\). The four lines are generated by \(1,i,i\sqrt3,\sqrt3\), making the project’s three nontrivial mod-12 characters literal simultaneous eigensign channels. In particular, the previously separate complex, ramified-residue, and Pell-time signs are the three nontrivial character coordinates of one exact \(V_4\)-representation.