# Cone Derivation Ledger v13.690 — Geometric Mirror, C2^3 Sign Cube, and Harmonic/Divisor Continuation Checkpoint

Date: 2026-09-22

Status: exact finite-sign decomposition plus exact cone-mean identities. This entry checkpoints the geometric mirror comparison against the QR/V4 character-line carrier and explicitly preserves the nH_n–D(n) divisor-summatory continuation so it is not lost behind the mirror/character work.

## 0. Live synchronization and scope

The project README was re-read immediately before this write. All active work remains under:

\`unified/discriminant-12-return/\`

The live repository was rechecked immediately before committing. The highest current ledger entry is v13.689 (External Audit Round 78). No v13.690 entry was present at the freshness check, so this entry claims v13.690.

This checkpoint builds on v13.678, which identifies the six affine character lines of AG(2,2) with the six-state carrier:

\[
\begin{aligned}
a&=L_{\chi_{12},+},&b&=L_{\chi_{12},-},\\
c&=L_{\chi_{-4},+},&d&=L_{\chi_{-4},-},\\
e&=L_{\chi_{-3},+},&f&=L_{\chi_{-3},-}.
\end{aligned}
\]

It also cross-references the existing research note
\`research-notes/Divisor_Summatory_V4_Mod12_Findings.md\`, whose exact identities are retained in §7 below.

## 1. Cone coordinates and the geometric mirror

For the cone figure coordinates,
\[
T=A,\qquad X=D=\frac{x-y}{2},\qquad Y=G=\sqrt{xy},
\]
with null/additive coordinates
\[
x=T+X,\qquad y=T-X.
\]

The geometric mirror
\[
\sigma_X:(T,X,Y)\mapsto(T,-X,Y)
\]
is exactly row/column exchange:
\[
x\leftrightarrow y,\qquad T+X\leftrightarrow T-X.
\]

Therefore
\[
\boxed{
\sigma_X(A)=A,\qquad
\sigma_X(D)=-D,\qquad
\sigma_X(G)=G.
}
\]

Since
\[
H_{\rm harm}=\frac{G^2}{A}=A-\frac{D^2}{A},
\]
we also have
\[
\boxed{\sigma_X(H_{\rm harm})=H_{\rm harm}.}
\]

Thus \(D\) generates the odd/sign representation of the geometric mirror \(C_2\), while \(A,G,H_{\rm harm}\) descend to the quotient by \(X\sim -X\).

## 2. Row/column parabolas as mirror pairs

The figure code contains the two families
\[
T+X=k,\qquad T-X=k.
\]
They are exchanged by \(\sigma_X\).

Projecting to the \((Y,T)\) panel forgets the sign of \(X\), and both branches become
\[
\boxed{Y^2=k(2T-k).}
\]

Equivalently,
\[
G^2=k(2A-k),
\]
and along this quotient parabola,
\[
\boxed{
H_{{\rm harm},k}(A)=\frac{G^2}{A}
=2k-\frac{k^2}{A}.
}
\]

Hence the Y-triangle/parabola view is a quotient of an oriented row/column pair under \(X\mapsto -X\), not a second unrelated geometry.

## 3. Three character pairs and the full sign cube

Use the three ordered character pairs
\[
P_1=(a,b),\qquad P_2=(c,d),\qquad P_3=(e,f).
\]

Represent a pairwise-flip action by
\[
s=(s_1,s_2,s_3)\in\{\pm1\}^3,
\]
where \(s_i=-1\) swaps the two lines in \(P_i\) and \(s_i=+1\) fixes them.

Composition is componentwise multiplication:
\[
(s_1,s_2,s_3)(t_1,t_2,t_3)
=(s_1t_1,s_2t_2,s_3t_3).
\]

Therefore the full signed-pair action group is
\[
\boxed{\Sigma\cong C_2^3.}
\]

The eight actions are:

\[
\begin{array}{c|c|c}
\text{pattern}&\text{permutation}&\text{parity}\\ \hline
(+,+,+)&1&\text{even}\\
(-,-,+)&(a\,b)(c\,d)&\text{even}\\
(-,+,-)&(a\,b)(e\,f)&\text{even}\\
(+,-,-)&(c\,d)(e\,f)&\text{even}\\
(-,+,+)&(a\,b)&\text{odd}\\
(+,-,+)&(c\,d)&\text{odd}\\
(+,+,-)&(e\,f)&\text{odd}\\
(-,-,-)&(a\,b)(c\,d)(e\,f)&\text{odd}.
\end{array}
\]

## 4. Even-parity V4 subgroup

The v13.678 translation action is
\[
\boxed{
\begin{aligned}
1&=(+,+,+),\\
7&=(-,-,+)=(a\,b)(c\,d),\\
5&=(-,+,-)=(a\,b)(e\,f),\\
11&=(+,-,-)=(c\,d)(e\,f).
\end{aligned}}
\]

Hence
\[
\boxed{
V_4
=
\{s\in C_2^3:s_1s_2s_3=+1\}.
}
\]

Equivalently, under \(+\leftrightarrow0\), \(-\leftrightarrow1\),
\[
\boxed{
V_4=\{000,110,101,011\}
=
\ker(x_1+x_2+x_3).
}
\]

This restates the character identity
\[
\chi_{12}\chi_{-4}\chi_{-3}=1:
\]
every genuine U(12) translation flips an even number of the three character pairs.

## 5. Odd coset and semilinear reversal

Define
\[
\boxed{
\rho=(-,-,-)=(a\,b)(c\,d)(e\,f).
}
\]

Then
\[
\boxed{
C_2^3=V_4\sqcup \rho V_4,
}
\]
where
\[
\boxed{
\rho V_4
=
\{
\rho,\,
(a\,b),\,
(c\,d),\,
(e\,f)
\}.
}
\]

Explicitly,
\[
\begin{aligned}
\rho\cdot 1&=(a\,b)(c\,d)(e\,f),\\
\rho\cdot 7&=(e\,f),\\
\rho\cdot 5&=(c\,d),\\
\rho\cdot 11&=(a\,b).
\end{aligned}
\]

The parity character
\[
p:C_2^3\to C_2,\qquad
p(s_1,s_2,s_3)=s_1s_2s_3
\]
gives the exact short sequence
\[
\boxed{
1\to V_4\to C_2^3\xrightarrow{p}C_2\to1.
}
\]

The even subgroup is the affine U(12) action. The odd coset is external to that affine translation action.

## 6. Geometric mirror versus semilinear reversal

On every row/column pair,
\[
T+X=k\longleftrightarrow T-X=k
\]
under \(X\mapsto -X\).

Thus on the three abstract signed character-pair coordinates, the geometric mirror acts as
\[
\boxed{
\sigma_X\rightsquigarrow(-,-,-)=\rho.
}
\]

Therefore the two actions are identical as permutations of the six-state signed-pair carrier:
\[
\boxed{\sigma_X=\rho\quad\text{on }\{a,b,c,d,e,f\}.}
\]

However, they are not internal U(12) translations. No element of V4 flips all three character pairs because every translation has even flip parity.

Moreover, \(\rho\) does not preserve the AG(2,2) point-line incidence while fixing all three directions: any affine automorphism preserving all three directions would have trivial linear part and hence be a translation, but no translation realizes \((-,-,-)\).

Thus:
\[
\boxed{
\text{geometric mirror / semilinear reversal}
\in C_2^3\setminus V_4,
}
\]
and
\[
\boxed{
\text{its six-state permutation is meaningful even though it is external to the affine AG(2,2) incidence action.}
}
\]

This is the precise affine-versus-semilinear distinction.

## 7. Preserve the nH_n–D(n) divisor thread

Do not let the mirror/character development displace the earlier divisor-summatory thread. The existing research note
\`research-notes/Divisor_Summatory_V4_Mod12_Findings.md\`
already records the exact identities:

\[
\boxed{
D(n)
=
\sum_{k=1}^n\left\lfloor\frac nk\right\rfloor
=
nH_n-\sum_{k=1}^n\left\{\frac nk\right\}.
}
\]

Here \(H_n=\sum_{k=1}^n1/k\) is the harmonic number; it must remain notationally distinct from the two-variable harmonic mean \(H_{\rm harm}(x,y)\).

For the prior GeoGebra/continuous construction,
\[
v_k=\frac{n-k^2}{2k},
\]
and
\[
A(n)=2\sum_{k=1}^n v_k
=
\boxed{nH_n-T_n},
\qquad
T_n=\frac{n(n+1)}2.
\]

Also,
\[
B(n)=2\sum_{k=1}^n(v_k\bmod 0.5)
=
\boxed{\sum_{k=1}^n\{n/k\}},
\]
hence
\[
\boxed{nH_n-B(n)=D(n).}
\]

Combining these gives
\[
\boxed{
T_n-D(n)=\mathrm{A161664}(n),
}
\]
the existing A161664 / non-dividing-pairs quantity already used in the project.

The cone/means work now supplies a new exact geometric dictionary that should be tested against these identities:
\[
A=T,\qquad D_{\rm cone}=X,\qquad G=|Y|,\qquad
H_{\rm harm}=\frac{Y^2}{T}.
\]

For a fixed product/divisor hyperbola
\[
xy=n,
\]
we have
\[
\boxed{
G^2=n,\qquad
A\,H_{\rm harm}=n.
}
\]

The divisor summatory function is equivalently
\[
\boxed{
D(n)
=
\#\{(x,y)\in\mathbb N^2:xy\le n\}
=
\#\{(x,y)\in\mathbb N^2:A\,H_{\rm harm}\le n\}.
}
\]

This does not identify the harmonic number \(H_n\) with the harmonic mean. Rather, both arise from reciprocal structure on the same multiplicative hyperbola:
\[
\frac nk
\]
is the column height of \(xy=n\), while
\[
H_{\rm harm}=\frac nA
\]
on that same shell.

## 8. Controlled continuation

Two next gates are preserved explicitly:

1. **Mirror/sign-cube gate.** Determine whether the external odd-parity coset \(\rho V_4\) has a natural realization in the continuous cone or semilinear extension beyond the six-state permutation representation, without incorrectly promoting it to an AG(2,2) incidence symmetry.

2. **Harmonic/divisor gate.** Reconcile the newly exposed Pythagorean-means coordinates
\[
A^2=D_{\rm cone}^2+G^2,\qquad
A\,H_{\rm harm}=G^2
\]
with the established divisor identities
\[
D(n)=nH_n-\sum\{n/k\},\qquad
A(n)=nH_n-T_n,\qquad
T_n-D(n)=\mathrm{A161664}(n),
\]
and determine whether the existing divisor-summatory three-panel figure can be rewritten as an exact four-view circle/hyperbola/parabola/cone dictionary without conflating \(H_n\) and \(H_{\rm harm}\).

Publication status: the finite sign-cube decomposition and cone mirror identities above are exact. The proposed deeper bridge between harmonic mean geometry and the \(nH_n,D(n),T_n,\mathrm{A161664}\) package is a controlled continuation target and is not yet promoted as a new theorem.
