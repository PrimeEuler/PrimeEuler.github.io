# Cone Derivation Ledger v13.379 — V4 Multiplicative Divisor-Contact Factorization

Date: 2026-09-09

Status labels: **[D]** exact derived, **[I]** interpretation, **[G]** guardrail.

## 1. Scope

Continue from v13.378 on the divisor-contact side. Assume

\[
\gcd(n,6)=1,
\]

so all divisors of `n` lie in `U(12)=\{1,5,7,11\}\cong V_4`.

This checkpoint is independent of the Casimir/null-diamond quarter-shift thread. The only `1/4` used here is the inverse-Hadamard factor from `H_4^2=4I`.

## 2. Exact V4 contact transform

Define

\[
C_r(n)=\#\{d\mid n:d\equiv r\pmod{12}\},
\qquad r\in\{1,5,7,11\}.
\]

Then

\[
C_1+C_5+C_7+C_{11}=\tau(n).
\]

For

\[
D_\chi(n)=\sum_{d\mid n}\chi(d),
\]

with characters `1,\chi_{-4},\chi_{-3},\chi_{12}`, the sign matrix is

\[
H_4=
\begin{pmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{pmatrix},
\qquad H_4^2=4I.
\]

Therefore

\[
\boxed{
\begin{pmatrix}
D_1\\D_{-4}\\D_{-3}\\D_{12}
\end{pmatrix}
=H_4
\begin{pmatrix}
C_1\\C_5\\C_7\\C_{11}
\end{pmatrix}
}
\]

and

\[
\boxed{
\begin{pmatrix}
C_1\\C_5\\C_7\\C_{11}
\end{pmatrix}
=\frac14H_4
\begin{pmatrix}
D_1\\D_{-4}\\D_{-3}\\D_{12}
\end{pmatrix}.
}
\]

Since all divisors are units,

\[
\boxed{D_1(n)=\tau(n).}
\]

## 3. Prime-power factorization

For

\[
n=\prod_pp^{e_p},
\]

complete multiplicativity of the characters on unit residues gives

\[
\boxed{
D_\chi(n)
=\prod_{p^{e_p}\parallel n}
\left(1+\chi(p)+\cdots+\chi(p)^{e_p}\right).
}
\]

Because `\chi(p)=\pm1`, define

\[
G_e(+1)=e+1,
\]

\[
G_e(-1)=
\begin{cases}
1,&e\text{ even},\\
0,&e\text{ odd}.
\end{cases}
\]

Hence

\[
\boxed{
D_\chi(n)=0
\iff
\exists\,p^{e_p}\parallel n
\text{ with }\chi(p)=-1\text{ and }e_p\text{ odd}.
}
\]

If no such prime exists,

\[
\boxed{
D_\chi(n)=\prod_{\chi(p)=+1}(e_p+1).
}
\]

## 4. Residue-class form

For `p\nmid6`:

\[
\begin{array}{c|cccc}
p\bmod12&1&5&7&11\\\hline
\chi_{-4}&+&+&-&-\\
\chi_{-3}&+&-&+&-\\
\chi_{12}&+&-&-&+
\end{array}
\]

Thus:

\[
\boxed{
D_{-4}(n)=0
\iff
\text{some }p\equiv7,11\pmod{12}\text{ occurs to odd exponent}.
}
\]

Otherwise

\[
\boxed{
D_{-4}(n)=\prod_{p\equiv1,5\ (12)}(e_p+1).
}
\]

Similarly,

\[
\boxed{
D_{-3}(n)=0
\iff
\text{some }p\equiv5,11\pmod{12}\text{ occurs to odd exponent},
}
\]

otherwise

\[
\boxed{
D_{-3}(n)=\prod_{p\equiv1,7\ (12)}(e_p+1).
}
\]

And

\[
\boxed{
D_{12}(n)=0
\iff
\text{some }p\equiv5,7\pmod{12}\text{ occurs to odd exponent},
}
\]

otherwise

\[
\boxed{
D_{12}(n)=\prod_{p\equiv1,11\ (12)}(e_p+1).
}
\]

## 5. Group-convolution formulation

For a prime power `p^e`, define the local contact vector in the group algebra of `U(12)`:

\[
\boxed{
\mathbf G_{p,e}=\sum_{a=0}^{e}e_{p^a\bmod12}.
}
\]

Then divisor choices multiply independently, so the global contact vector is the V4 convolution

\[
\boxed{
\mathbf C(n)
=\mathop{*}_{p^{e_p}\parallel n}\mathbf G_{p,e_p}.
}
\]

The four-character transform diagonalizes the convolution:

\[
\boxed{
\widehat{\mathbf C}_\chi(n)
=\prod_{p^{e_p}\parallel n}
\widehat{\mathbf G}_{p,e_p}(\chi)
=D_\chi(n).
}
\]

This is the clean structural statement of the checkpoint: multiplicative prime-power divisor choices become componentwise products in the V4 character basis, while the inverse transform reconstructs additive contact counts in the four residue classes.

## 6. Explicit local prime-power vectors

For `r\in\{5,7,11\}`, every nontrivial unit has order 2:

\[
r^{2a}\equiv1,\qquad r^{2a+1}\equiv r\pmod{12}.
\]

Therefore if `p\equiv r\ne1\pmod{12}`,

\[
\boxed{
\mathbf G_{p,e}
=
\left(\left\lfloor\frac e2\right\rfloor+1\right)e_1
+\left\lceil\frac e2\right\rceil e_r.
}
\]

For `p\equiv1\pmod{12}`,

\[
\boxed{\mathbf G_{p,e}=(e+1)e_1.}
\]

## 7. Squarefree specialization

If `n` is squarefree and `\gcd(n,6)=1`, then for any nontrivial character

\[
\boxed{
D_\chi(n)\ne0
\iff
\chi(p)=+1\text{ for every }p\mid n.
}
\]

When it survives,

\[
\boxed{D_\chi(n)=2^{\omega(n)}=\tau(n),}
\]

otherwise

\[
\boxed{D_\chi(n)=0.}
\]

Thus each nontrivial V4 channel is a sharp subgroup-support test for squarefree prime support.

## 8. Link back to support inversion

From v13.378,

\[
D_\chi(n)=P_\chi(n)-S_\chi(n),
\]

where

\[
P_\chi(n)=\sum_{k=1}^{n}\chi(k),
\qquad
S_\chi(n)=\sum_{k\nmid n}\chi(k).
\]

Combining with the prime-power factorization gives

\[
\boxed{
P_\chi(n)-S_\chi(n)
=
\prod_{p^{e_p}\parallel n}
\left(1+\chi(p)+\cdots+\chi(p)^{e_p}\right).
}
\]

This identifies the global off-shell-support complement exactly with the multiplicative divisor-contact channel.

## 9. Example: `n=11^e`

Since `11` has character signs `(-1,-1,+1)`:

\[
D_1=e+1,\qquad D_{12}=e+1,
\]

and

\[
D_{-4}=D_{-3}
=
\begin{cases}
1,&e\text{ even},\\
0,&e\text{ odd}.
\end{cases}
\]

For `e=1`:

\[
(D_1,D_{-4},D_{-3},D_{12})=(2,0,0,2),
\]

which inverts to

\[
\boxed{(C_1,C_5,C_7,C_{11})=(1,0,0,1).}
\]

For `e=2`:

\[
(D_1,D_{-4},D_{-3},D_{12})=(3,1,1,3),
\]

which gives

\[
\boxed{(C_1,C_5,C_7,C_{11})=(2,0,0,1).}
\]

## 10. Guardrails

- **[G] `1/4` here is only inverse Fourier normalization.** It follows from `H_4^{-1}=H_4/4` and is unrelated to the SU(2) Casimir quarter, null-diamond midpoint norm, or factor-cell mixed-curvature quarter.
- **[G] Coprimality is essential for `D_1=\tau(n)` in this four-unit-class framework.** If `2|n` or `3|n`, non-unit divisors are omitted by Dirichlet characters mod 12.
- **[G] A zero twisted divisor sum is a parity obstruction, not a prime test.** It says at least one negative-sign prime occurs to odd exponent.
- **[G] Contact counts do not identify individual factors.** Fourier inversion reconstructs how many divisor contacts occupy each residue class, not their numerical locations.
- **[G] The multiplicative formulas are classical Dirichlet-character algebra.** The new role here is organizational: they supply the exact multiplicative side of the cone/divisor-contact V4 framework.

## 11. Companion note

`research-notes/V4_Multiplicative_Divisor_Contact_Factorization.md`
