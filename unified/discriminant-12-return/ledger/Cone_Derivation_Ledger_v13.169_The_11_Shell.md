# Cone Derivation Ledger v13.169 — The 11-Shell

**Status:** Audited extension of v13.168  
**Date:** 2026-09-03  
**Scope:** Exact bridge among Paper A divisor geometry, the mod-12 V4 unit packet, and the discriminant-12 / narrow-class arithmetic.

## Audit convention

- **[S]** source-established
- **[D]** exact derived
- **[N-cert]** rigorous finite numerical/computer-assisted
- **[I]** interpretation
- **[O]** open
- **[Audit]** correction / limitation

---

## 1. Dirichlet divisor geometry in Cone coordinates

For a divisor–quotient pair `(k,q)` define the Paper A mean coordinates

\[
T=\frac{k+q}{2},\qquad X=\frac{k-q}{2},\qquad Y=\sqrt{kq}.
\]

Then

\[
\boxed{X^2+Y^2=T^2}
\]

and, equivalently,

\[
\boxed{T^2-X^2=kq=Y^2}.
\]

Therefore the Dirichlet boundary `kq=n` is exactly the Lorentz shell

\[
\boxed{T^2-X^2=n}
\]

and simultaneously the constant-`Y` section

\[
\boxed{Y^2=n}.
\]

**[D]** The classical divisor hyperbola is therefore a Lorentz level set of the same real split quadratic geometry used by the Cone framework.

The null coordinates recover the original factors exactly:

\[
\boxed{k=T+X,\qquad q=T-X},
\]

so

\[
\boxed{(T+X)(T-X)=n}.
\]

---

## 2. Divisor summatory hierarchy

Let

\[
D(n)=\sum_{m\le n}d(m)=\sum_{k=1}^{n}\left\lfloor\frac nk\right\rfloor,
\qquad
T_n=\frac{n(n+1)}2.
\]

For OEIS A161664,

\[
\boxed{A_n=T_n-D(n)}.
\]

Hence

\[
\boxed{T_n=D(n)+A_n}.
\]

**[D]** `T_n` counts the full triangular domain `1<=k<=m<=n`; `D(n)` counts the divisibility incidences `k|m`; `A_n` is the exact complementary nondivisibility count.

The unrounded hyperbolic column sum is

\[
\boxed{nH_n=\sum_{k=1}^{n}\frac nk},
\]

and therefore

\[
\boxed{D(n)=nH_n-\sum_{k=1}^{n}\left\{\frac nk\right\}}.
\]

The continuous hyperbolic area is

\[
\boxed{\int_1^n\frac n{x}\,dx=n\log n}.
\]

Thus the natural hierarchy is

\[
n\log n\quad\longrightarrow\quad nH_n\quad\longrightarrow\quad D(n),
\]

with meanings respectively: continuous area, discretely sampled hyperbola, and integer lattice count after flooring. The exact complement inside the triangular domain is then `A_n=T_n-D(n)`.

**[Audit]** This hierarchy is a precise continuous/sampled/lattice comparison; it is not by itself a discriminant-12 identification.

---

## 3. The n=11 shell

At `n=11`,

\[
D(11)=29,\qquad T_{11}=66,\qquad A_{11}=37,
\]

so

\[
\boxed{66=29+37}.
\]

Also

\[
11\log 11\approx26.37685,
\qquad
11H_{11}\approx33.21865,
\]

and hence

\[
\boxed{11\log11<D(11)<11H_{11}<T_{11}}.
\]

The factor pair `(11,1)` gives

\[
T=6,\qquad X=5,\qquad Y=\sqrt{11},
\]

while `(1,11)` gives the mirror point `X=-5`. Therefore

\[
\boxed{6^2-5^2=11}
\]

and

\[
\boxed{(T-X,T+X)=(1,11)}
\]

at the positive endpoint.

Since `11+1=12`, these points lie simultaneously on

\[
\boxed{kq=11}
\]

and on the outer anti-diagonal

\[
\boxed{k+q=12}.
\]

**[D] 11-shell intersection theorem.** The two points `(11,1)` and `(1,11)` are exactly the intersections of the positive `n=11` constant-product shell with the `K=12` anti-diagonal. In Cone coordinates these are

\[
\boxed{(X,Y,T)=(\pm5,\sqrt{11},6)}.
\]

This explains the outer `r=11` points in the mod-12 V4 cone figure without introducing any new visual convention.

---

## 4. The mod-12 V4 packet and the shell points

For

\[
U(12)=\{1,5,7,11\},
\]

the current V4 cone construction uses the factor pair `(r,1)` and therefore

\[
\boxed{T=\frac{r+1}{2},\quad |X|=\frac{r-1}{2},\quad Y^2=r}.
\]

Thus the four positive shell representatives are

\[
\begin{array}{c|c|c|c}
r&T&|X|&Y^2\\ \hline
1&1&0&1\\
5&3&2&5\\
7&4&3&7\\
11&6&5&11
\end{array}
\]

and each satisfies

\[
\boxed{T^2-X^2=r}.
\]

For `r=11`, the same point is distinguished further by `2T=12`.

**[D]** The mod-12 unit packet is therefore represented geometrically by four explicit Lorentz shell points, with the `11` representative landing exactly on the outer `K=12` boundary.

---

## 5. Frobenius meaning of {1,5,7,11}

Let

\[
K=\mathbb Q(\zeta_{12}),
\qquad
\operatorname{Gal}(K/\mathbb Q)\cong(\mathbb Z/12\mathbb Z)^\times.
\]

For every rational prime `p` not dividing 12,

\[
\boxed{\operatorname{Frob}_p(\zeta_{12})=\zeta_{12}^{p}},
\]

so the residue class `p mod 12` is its cyclotomic Frobenius class.

In particular, because `11` is prime,

\[
\boxed{\operatorname{Frob}_{11}=T_{11}}.
\]

Since

\[
11\equiv-1\pmod{12},
\]

we have

\[
T_{11}(\zeta_{12})=\zeta_{12}^{11}=\zeta_{12}^{-1}=\overline{\zeta_{12}}.
\]

Therefore

\[
\boxed{T_{11}=\kappa}
\]

in the complex-compatible Galois labeling, where `kappa` is complex conjugation.

**[D]** The label `11` in the V4 packet is simultaneously a geometric shell label and the actual cyclotomic Frobenius class of the rational prime 11.

**[Audit]** The element `1` in the packet is the identity residue representative, not a rational prime; primes congruent to 1 mod 12 realize the identity Frobenius class.

---

## 6. The prime 11 in F=Q(sqrt(3))

Let

\[
F=\mathbb Q(\sqrt3).
\]

The element

\[
\alpha_{11}=1+2\sqrt3
\]

has norm

\[
\boxed{N_{F/\mathbb Q}(1+2\sqrt3)=1-12=-11}.
\]

Thus

\[
(1+2\sqrt3)(1-2\sqrt3)=-11,
\]

and the rational prime 11 splits in `F`:

\[
\boxed{(11)=\mathfrak p_{11}\mathfrak p'_{11}},
\]

where one may take

\[
\boxed{\mathfrak p_{11}=(1+2\sqrt3)},
\qquad N(\mathfrak p_{11})=11.
\]

**[D]** The same integer 11 appearing as the divisor shell and the V4/Frobenius representative is the absolute norm of a distinguished negative-norm generator in the real quadratic field of discriminant 12.

---

## 7. Narrow-class identification with p_2

Recall

\[
\mathfrak p_2=(1+\sqrt3),
\qquad N(1+\sqrt3)=-2.
\]

Both `1+sqrt(3)` and `1+2sqrt(3)` have negative norm. Their product is

\[
(1+\sqrt3)(1+2\sqrt3)=7+3\sqrt3.
\]

Its two real embeddings are

\[
7+3\sqrt3>0,
\qquad
7-3\sqrt3>0.
\]

Hence `7+3sqrt(3)` is totally positive and

\[
\boxed{\mathfrak p_2\mathfrak p_{11}=(7+3\sqrt3)}
\]

is narrow-principal. Since `Cl^+(F)` has order 2 and `[p_2]` is its unique nontrivial class,

\[
\boxed{[\mathfrak p_{11}]=[\mathfrak p_2]\in\mathrm{Cl}^+(F)}.
\]

Consequently, in the narrow Hilbert class field

\[
K=F(i)=\mathbb Q(\zeta_{12}),
\]

the Artin class is

\[
\boxed{\operatorname{Art}_{K/F}(\mathfrak p_{11})=T_{11}}.
\]

Together with the previously audited operator correspondence `T_11 <-> J`, this gives

\[
\boxed{
11
\longrightarrow
\mathfrak p_{11}
\longrightarrow
[\mathfrak p_{11}]=[\mathfrak p_2]
\longrightarrow
T_{11}
\longrightarrow
J.
}
\]

**[D]** This is an exact arithmetic chain; the final `T_11 <-> J` arrow is the already-audited representation correspondence, not a field homomorphism.

---

## 8. Splitting interpretation of the four mod-12 classes

For rational primes `p` not dividing 12, the residue class in `U(12)` determines the Frobenius in `K/Q`. Relative to the tower

\[
\mathbb Q\subset F=\mathbb Q(\sqrt3)\subset K=\mathbb Q(\zeta_{12}),
\]

the four classes may be summarized as follows:

| `p mod 12` | Frobenius in `K/Q` | behavior in `F/Q` | behavior above `F` |
|---|---|---|---|
| 1 | `T_1` | splits | split primes split in `K/F` |
| 5 | `T_5` | inert | the degree-2 prime splits after adjoining `i` |
| 7 | `T_7` | inert | the degree-2 prime splits after adjoining `i` |
| 11 | `T_11` | splits | the degree-1 primes are inert in `K/F` |

**[D]** This gives the V4 packet a genuine cyclotomic splitting/Frobenius interpretation in addition to its geometric realization.

---

## 9. Comparison with the discriminant-12 norm cone

The discriminant-12 form is

\[
q_{12}(x,y)=2x^2-2xy-y^2.
\]

With

\[
U=2x-y,\qquad V=\sqrt3\,y,
\]

we have

\[
\boxed{2q_{12}(x,y)=U^2-V^2}.
\]

Its null coordinates are

\[
\eta_+=U+V=2x+(\sqrt3-1)y,
\]

\[
\eta_-=U-V=2x-(\sqrt3+1)y,
\]

and

\[
\boxed{\eta_+\eta_-=2q_{12}(x,y)}.
\]

This has exactly the same real split Lorentz form as

\[
\boxed{(T+X)(T-X)=kq}.
\]

**[D]** Over `Q(sqrt(3))` there is an explicit split-norm comparison between the divisor hyperbola and the discriminant-12 arithmetic light cone.

**[Audit]** The two arithmetic lattices are not rationally or integrally equivalent. The primitive divisor product form `kq` has discriminant 1, whereas `q_12` has discriminant 12. Their discriminant square classes differ over `Q`; the split equivalence appears only after adjoining `sqrt(3)`.

---

## 10. The 11-shell does not lie in the p_2 norm lattice

For

\[
\alpha=2x+(\sqrt3-1)y\in\mathfrak p_2,
\]

we have

\[
N(\alpha)=2q_{12}(x,y),
\]

which is even for integral `(x,y)`. Therefore

\[
\boxed{N(\alpha)=\pm11}
\]

has no solution inside the integral `p_2` lattice.

Indeed, solving

\[
1+2\sqrt3=2x+(\sqrt3-1)y
\]

gives

\[
\boxed{y=2,\qquad x=\frac32}.
\]

Thus the norm-11 generator lies at a half-integral displacement relative to this chosen `p_2` basis.

**[Audit]** This prevents identification of the `n=11` divisor shell with the `p_2` norm lattice.

**[I/O]** The half-integral displacement is suggestive in view of the project's independent dyadic/cyclotomic gluing phenomena, but no canonical connection is presently established. Do not promote this observation beyond an open comparison without a separate derivation.

---

## 11. Consolidated 11-shell bridge

The exact three-way meeting is

\[
\boxed{
\begin{array}{ccc}
\text{Paper A divisor geometry}
&\text{mod-12 V4 / cyclotomic Galois}
&\text{discriminant-12 arithmetic}\\[2mm]
kq=11
&11\in U(12)
&N(1+2\sqrt3)=-11\\
T=6,\ |X|=5
&\operatorname{Frob}_{11}=T_{11}
&[\mathfrak p_{11}]=[\mathfrak p_2]\\
k+q=12
&T_{11}=\kappa
&\operatorname{Art}(\mathfrak p_{11})=T_{11}.
\end{array}}
\]

### Ledger conclusion

**[D]** The integer `11` participates independently and exactly in three structures already present in the project:

1. the constant-product divisor shell `kq=11`, whose extreme factor pair `(11,1)` lies on the `k+q=12` outer Cone boundary;
2. the mod-12 unit / cyclotomic Frobenius class `T_11`, equal to complex conjugation in the complex-compatible labeling;
3. the norm-11 split prime of `Q(sqrt(3))`, whose prime ideal represents the same unique nontrivial narrow class as `p_2` and therefore has Artin image `T_11` in `K/F`.

These are exact bridges, but they do **not** identify the ordinary divisor lattice with the discriminant-12 ideal lattice.

---

## Publication guardrails added in v13.169

1. Do not claim that the divisor form `kq` and `q_12` are `GL_2(Z)`- or `GL_2(Q)`-equivalent; their discriminants are 1 and 12.
2. Do not claim that the norm-11 generator `1+2sqrt(3)` lies in the integral `p_2` lattice.
3. Do not infer significance from the half-integral `p_2` coordinates without a separate dyadic-gluing derivation.
4. The V4 residue `1` is an identity class representative, not itself a prime Frobenius example.
5. `T_11 <-> J` remains an audited representation correspondence, not a field/operator identity.
6. The appearance of 11 is now supported by exact geometric, Frobenius, and narrow-class statements; no claim about zeta-zero location follows from these bridges.
