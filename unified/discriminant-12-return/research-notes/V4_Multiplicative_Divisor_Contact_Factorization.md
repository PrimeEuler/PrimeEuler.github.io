# V4 Multiplicative Divisor-Contact Factorization

Date: 2026-09-09

Status labels: **[D]** exact derived, **[I]** interpretation, **[G]** guardrail.

## Scope

This note continues the arithmetic V4 support/contact thread after v13.378. It does **not** use the Casimir/null-diamond quarter-shift identifications. The only `1/4` below is the inverse Fourier normalization on the four-element group `U(12) \cong V_4`, because `H_4^2=4I`.

Throughout this note assume

\[
\gcd(n,6)=1,
\]

so every divisor of `n` lies in one of the four unit classes

\[
U(12)=\{1,5,7,11\}.
\]

## 1. Divisor-contact vector

Define

\[
C_r(n):=\#\{d\mid n:d\equiv r\pmod{12}\},
\qquad r\in\{1,5,7,11\}.
\]

Let

\[
\mathbf C(n)=
\begin{pmatrix}
C_1(n)\\C_5(n)\\C_7(n)\\C_{11}(n)
\end{pmatrix}.
\]

Since all divisors are units mod 12,

\[
\boxed{C_1+C_5+C_7+C_{11}=\tau(n).}
\]

## 2. Character channels

Use the four real characters

\[
1,\qquad \chi_{-4},\qquad \chi_{-3},\qquad \chi_{12}=\chi_{-4}\chi_{-3}.
\]

On residues `(1,5,7,11)` their sign table is

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

Define divisor-character sums

\[
D_\chi(n):=\sum_{d\mid n}\chi(d).
\]

Then exactly

\[
\boxed{
\begin{pmatrix}
D_1\\D_{-4}\\D_{-3}\\D_{12}
\end{pmatrix}
=H_4\mathbf C(n).
}
\]

Therefore

\[
\boxed{
\mathbf C(n)
=\frac14H_4
\begin{pmatrix}
D_1\\D_{-4}\\D_{-3}\\D_{12}
\end{pmatrix}.
}
\]

In particular,

\[
\boxed{D_1(n)=\tau(n).}
\]

Explicitly,

\[
\boxed{
C_1=\frac14(D_1+D_{-4}+D_{-3}+D_{12}),
}
\]

\[
\boxed{
C_5=\frac14(D_1+D_{-4}-D_{-3}-D_{12}),
}
\]

\[
\boxed{
C_7=\frac14(D_1-D_{-4}+D_{-3}-D_{12}),
}
\]

\[
\boxed{
C_{11}=\frac14(D_1-D_{-4}-D_{-3}+D_{12}).
}
\]

## 3. Multiplicative factorization

Let

\[
n=\prod_{p}p^{e_p}.
\]

Because every Dirichlet character is completely multiplicative on units,

\[
D_\chi(n)
=\sum_{d\mid n}\chi(d)
=\prod_{p^{e_p}\parallel n}
\left(1+\chi(p)+\cdots+\chi(p)^{e_p}\right).
\]

Thus

\[
\boxed{
D_\chi(n)
=\prod_{p^{e_p}\parallel n}G_{e_p}(\chi(p)),
}
\]

where

\[
G_e(+1)=e+1,
\]

and

\[
G_e(-1)=
\begin{cases}
1,&e\text{ even},\\
0,&e\text{ odd}.
\end{cases}
\]

Hence the exact channel rule is

\[
\boxed{
D_\chi(n)=0
\iff
\exists\,p^{e_p}\parallel n
\text{ with }\chi(p)=-1\text{ and }e_p\text{ odd}.
}
\]

If no such prime exists, then

\[
\boxed{
D_\chi(n)
=\prod_{\substack{p^{e_p}\parallel n\\\chi(p)=+1}}(e_p+1).
}
\]

The primes with `\chi(p)=-1` and even exponent contribute factor `1`.

## 4. Residue-class prime factors

For a prime `p\nmid 6`, its residue mod 12 determines its signs:

\[
\begin{array}{c|cccc}
p\bmod12&1&5&7&11\\\hline
\chi_{-4}(p)&+&+&-&-\\
\chi_{-3}(p)&+&-&+&-\\
\chi_{12}(p)&+&-&-&+
\end{array}
\]

Therefore:

### `D_{-4}`

\[
D_{-4}(n)=0
\]

iff some prime in residue class `7` or `11` occurs to odd exponent. Otherwise

\[
\boxed{
D_{-4}(n)
=\prod_{p\equiv1,5\ (12)}(e_p+1).
}
\]

### `D_{-3}`

\[
D_{-3}(n)=0
\]

iff some prime in residue class `5` or `11` occurs to odd exponent. Otherwise

\[
\boxed{
D_{-3}(n)
=\prod_{p\equiv1,7\ (12)}(e_p+1).
}
\]

### `D_{12}`

\[
D_{12}(n)=0
\]

iff some prime in residue class `5` or `7` occurs to odd exponent. Otherwise

\[
\boxed{
D_{12}(n)
=\prod_{p\equiv1,11\ (12)}(e_p+1).
}
\]

These products are taken over prime powers dividing `n`; a residue-class product is `1` when no prime lies in that positive-sign class.

## 5. Group-convolution form

Let `e_r` denote the basis vector of the group algebra of `U(12)`. For a prime power `p^e`, define its local divisor-contact vector

\[
\boxed{
\mathbf G_{p,e}:=\sum_{a=0}^{e}e_{p^a\bmod12}.
}
\]

Every divisor of `n` is obtained by choosing one exponent independently from each prime power. Therefore the global contact distribution is the V4 convolution

\[
\boxed{
\mathbf C(n)
=\mathop{*}_{p^{e_p}\parallel n}\mathbf G_{p,e_p}.
}
\]

The four-character transform diagonalizes this convolution:

\[
\boxed{
\widehat{\mathbf C}_\chi(n)
=\prod_{p^{e_p}\parallel n}
\widehat{\mathbf G}_{p,e_p}(\chi)
=D_\chi(n).
}
\]

So the multiplicative divisor structure and the additive residue-class contact distribution are related exactly by finite Fourier transform on `V_4`.

## 6. Prime-power local vectors

Because every nontrivial unit residue has order 2 in `U(12)`, for `r\in\{5,7,11\}`:

\[
r^{2a}\equiv1\pmod{12},\qquad
r^{2a+1}\equiv r\pmod{12}.
\]

Hence for a prime `p\equiv r\ne1\pmod{12}`,

\[
\boxed{
\mathbf G_{p,e}
=
\left(\left\lfloor\frac e2\right\rfloor+1\right)e_1
+\left\lceil\frac e2\right\rceil e_r.
}
\]

If `p\equiv1\pmod{12}`,

\[
\boxed{\mathbf G_{p,e}=(e+1)e_1.}
\]

Thus each prime-power contact distribution is known explicitly before any global convolution is performed.

## 7. Squarefree specialization

If `n` is squarefree and coprime to 6, every exponent is `1`. Then a nontrivial character channel survives iff every prime factor lies in its `+1` residue half:

\[
\boxed{
D_\chi(n)\ne0
\iff
\chi(p)=+1\quad\text{for every }p\mid n.
}
\]

When it survives,

\[
\boxed{D_\chi(n)=2^{\omega(n)}=\tau(n).}
\]

Otherwise

\[
\boxed{D_\chi(n)=0.}
\]

So for squarefree `n`, each nontrivial V4 channel is a sharp yes/no test of whether the prime support lies entirely in the corresponding index-two subgroup of `U(12)`.

## 8. Example: `n=11^e`

Since `11` has signs

\[
(\chi_{-4},\chi_{-3},\chi_{12})=(-1,-1,+1),
\]

we have

\[
D_1=e+1,
\qquad
D_{12}=e+1,
\]

and

\[
D_{-4}=D_{-3}=
\begin{cases}
1,&e\text{ even},\\
0,&e\text{ odd}.
\end{cases}
\]

If `e=1`,

\[
(D_1,D_{-4},D_{-3},D_{12})=(2,0,0,2),
\]

so

\[
(C_1,C_5,C_7,C_{11})=(1,0,0,1),
\]

corresponding exactly to divisors `1,11`.

If `e=2`,

\[
(D_1,D_{-4},D_{-3},D_{12})=(3,1,1,3),
\]

so

\[
(C_1,C_5,C_7,C_{11})=(2,0,0,1),
\]

corresponding to divisors `1,11,121\equiv1\pmod{12}`.

## 9. Relation to v13.378 support inversion

v13.378 gave

\[
D_\chi(n)=P_\chi(n)-S_\chi(n),
\]

where

\[
S_\chi(n)=\sum_{k\nmid n}\chi(k),
\qquad
P_\chi(n)=\sum_{k=1}^{n}\chi(k).
\]

Combining with the multiplicative factorization gives

\[
\boxed{
P_\chi(n)-S_\chi(n)
=
\prod_{p^{e_p}\parallel n}
\left(1+\chi(p)+\cdots+\chi(p)^{e_p}\right).
}
\]

This is an exact equality between the global off-shell support channel and the multiplicative divisor-contact channel. It is a complement identity, not a factoring algorithm.

## 10. Guardrails

- **[G] No quarter-shift bridge.** The factor `1/4` in the inverse transform is only `|V_4|^{-1}` from `H_4^{-1}=H_4/4`; it is unrelated to the SU(2) Casimir completion, the null-diamond midpoint norm, or mixed-cell `\delta^2/4`.
- **[G] Coprimality scope.** The clean four-class contact vector here assumes `\gcd(n,6)=1`. For general `n`, divisors divisible by 2 or 3 lie outside `U(12)` and the principal unit channel no longer equals `\tau(n)`.
- **[G] Character zeros are parity obstructions, not primality tests.** A vanishing `D_\chi` records the presence of at least one prime with `\chi(p)=-1` to odd exponent. It does not by itself identify the prime or imply compositeness in a novel way.
- **[G] Fourier inversion reconstructs residue counts, not factor labels.** The vector `(C_1,C_5,C_7,C_{11})` gives counts of divisor contacts by residue class; it does not recover the individual divisors without additional information.
- **[G] Multiplicativity is classical Dirichlet-character algebra.** The value here is its exact placement in the cone/divisor-contact framework, not a claim of a new multiplicative theorem.
