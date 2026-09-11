# Cone Derivation Ledger v13.393 — V4 Uniform Contact Measure from Odd-Residue Generation

Date: 2026-09-11

Status labels: **[D]** exact derived, **[I]** interpretation, **[G]** guardrail.

## Scope

Extend v13.382/v13.385 from squarefree and general-exponent contact distributions to a necessary-and-sufficient criterion for when the divisor-contact measure is uniform on its support subgroup in
\[
U(12)=\{1,5,7,11\}\cong V_4,
\]
under the standing assumption
\[
\gcd(n,6)=1.
\]

## 1. Support subgroup and odd-exponent subgroup

Write
\[
n=\prod_p p^{e_p}.
\]
Define
\[
H(n)=\langle p\bmod12:p\mid n\rangle\le V_4
\]
and
\[
\boxed{
H_{\rm odd}(n)
=
\left\langle
p\bmod12:p^{e_p}\parallel n,\ e_p\text{ odd}
\right\rangle.
}
\]

The contact vector is
\[
C_r(n)=\#\{d\mid n:d\equiv r\pmod{12}\},
\]
and its normalized form is
\[
P_r(n)=C_r(n)/\tau(n).
\]
By v13.385, the support of \(P\) is exactly \(H(n)\).

## 2. Character factorization

For any real character \(\chi\) of \(V_4\),
\[
D_\chi(n)=\sum_{d\mid n}\chi(d)
=
\prod_{p^{e_p}\parallel n}
\sum_{a=0}^{e_p}\chi(p)^a.
\]
Therefore
\[
\boxed{
D_\chi(n)=0
\iff
\exists p^{e_p}\parallel n:
\chi(p)=-1,\ e_p\text{ odd}.
}
\]
Equivalently,
\[
\boxed{
D_\chi(n)=0
\iff
\chi\notin H_{\rm odd}(n)^\perp.
}
\]

For every \(\chi\in H(n)^\perp\), all prime residues lie in \(\ker\chi\), hence
\[
\boxed{
D_\chi(n)=\tau(n).
}
\]

## 3. Uniformity theorem

The uniform probability measure on a subgroup \(H\le V_4\) has Fourier transform equal to 1 on \(H^\perp\) and 0 outside \(H^\perp\).

The normalized contact Fourier coefficients are
\[
\rho_\chi(n)=D_\chi(n)/\tau(n).
\]
Hence \(P\) is uniform on \(H(n)\) iff
\[
\rho_\chi=1\quad(\chi\in H(n)^\perp),
\]
which is automatic, and
\[
\rho_\chi=0\quad(\chi\notin H(n)^\perp).
\]
By the previous section, the zero set is the complement of \(H_{\rm odd}(n)^\perp\). Thus uniformity is equivalent to
\[
H_{\rm odd}(n)^\perp=H(n)^\perp.
\]
Finite V4 duality gives the exact criterion
\[
\boxed{
P\text{ is uniform on }H(n)
\iff
H_{\rm odd}(n)=H(n).
}
\]

## 4. Rank cases

### Rank 0
\[
H=\{1\}.
\]
Uniformity is automatic.

### Rank 1
If
\[
H=\{1,g\},\qquad g\in\{5,7,11\},
\]
then
\[
\boxed{
P\text{ uniform on }H
\iff
\text{at least one prime }p\equiv g\pmod{12}
\text{ occurs to odd exponent.}
}
\]

### Rank 2
If
\[
H=V_4,
\]
then
\[
\boxed{
P\text{ uniform on all four unit classes}
\iff
H_{\rm odd}=V_4.
}
\]
Any two distinct nontrivial elements generate \(V_4\), hence this is equivalent to odd exponents occurring in at least two distinct nontrivial residue directions among \(5,7,11\).

Equivalently,
\[
\boxed{
D_{-4}(n)=D_{-3}(n)=D_{12}(n)=0.
}
\]

## 5. Squarefree theorem as corollary

If \(n\) is squarefree, all prime exponents are odd, so
\[
H_{\rm odd}(n)=H(n).
\]
Therefore the squarefree contact measure is automatically uniform on its support subgroup, recovering v13.382.

The exact generalization is therefore not “squarefree” but
\[
\boxed{
\text{odd-exponent residue directions generate the full support subgroup.}
}
\]

## 6. Bias mechanism

If
\[
H_{\rm odd}\subsetneq H,
\]
then there exists a character
\[
\chi\in H_{\rm odd}^\perp\setminus H^\perp.
\]
For this character,
\[
D_\chi(n)>0,
\]
so a nontrivial Fourier mode survives and the contact distribution is biased on \(H\).

Thus even-exponent-only residue directions enlarge the support without necessarily annihilating the characters that detect them.

## 7. Guardrails

- **[G]** The factor \(1/4\) in V4 inversion is solely \(1/|V_4|\), the inverse-Hadamard/Fourier normalization. No Casimir/null-diamond/mixed-cell identification is made.
- **[G]** Uniform contact distribution is not a primality criterion.
- **[G]** The theorem assumes \(\gcd(n,6)=1\); factors 2 or 3 introduce divisor residues outside the unit group.
- **[G]** Character cancellation is finite arithmetic Fourier cancellation, not a spectral statement.

## 8. Exact checkpoint

\[
\boxed{
P_r(n)=\frac{C_r(n)}{\tau(n)}
\text{ is uniform on its support subgroup }H(n)
\iff
H_{\rm odd}(n)=H(n).
}
\]

This is the exact exponent-parity completion of the squarefree V4 contact-orbit classification.
