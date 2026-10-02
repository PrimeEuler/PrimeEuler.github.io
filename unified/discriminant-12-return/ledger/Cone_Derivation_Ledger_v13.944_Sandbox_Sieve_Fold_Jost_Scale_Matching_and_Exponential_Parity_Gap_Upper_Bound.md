# Cone Derivation Ledger v13.944 — Sandbox: Sieve-Fold/Jost Scale Matching and RH-Conditional Exponential Parity-Gap Upper Bound

**Date:** 2026-10-02  
**Track:** Sandbox / cross-lane cone-sieve ↔ Suzuki-Jost finite-size lane  
**Status:** [D] exact logarithmic scale matching; [D] RH-conditional exponential upper bound on the odd recentered gap; [I] one-lift interpretation; [G] no divisor-\(1/4\) import and no matching lower bound; [O] optimize tunneling rate and source-residue asymptotics  
**Authorization:** Jeremy, 2026-10-02 ("the cone update just landed")  
**Parents:** v13.938 (Jost normalization), v13.940–941 (overlap double scaling / parity-pole crossover), v13.942 (sieve renormalization flow), v13.943 (super-algebraic parity-gap bound)  
**Collision check:** v13.944 was absent immediately before this write.

---

## 0. Cross-lane verdict

The new sieve-renormalization entry v13.942 changes the finite-size interpretation of the Suzuki/Jost lane in a precise way.

For Suzuki's finite interval

\[
x,y\in(-a,a),
\]

the difference variable satisfies

\[
|x-y|\le 2a.
\]

The arithmetic breakpoints in the prime-power part of the Weil/screw kernel occur at logarithmic lengths

\[
\log n.
\]

Thus the full finite operator samples arithmetic data only through

\[
\log n\le 2a.
\]

Define the arithmetic cutoff

\[
\boxed{
N_a:=e^{2a}.
}
\tag{1}
\]

Then the finite Suzuki operator sees arithmetic through \(n\le N_a\).

The exact sieve theorem of v13.942 says arithmetic up to \(N_a\) is generated from seed primes

\[
p\le \sqrt{N_a}.
\]

But

\[
\sqrt{N_a}=e^a.
\]

Hence

\[
\boxed{
a=\log\sqrt{N_a},
\qquad
2a=\log N_a.
}
\tag{2}
\]

So the interval half-width is exactly the logarithmic seed scale, while the cross-edge distance is the logarithmic fully lifted scale.

---

## 1. The square-root sieve fold is \(a\mapsto a/2\) [D]

Under

\[
N\mapsto\sqrt N,
\]

the associated Suzuki half-width

\[
a(N):=\frac12\log N
\]

transforms as

\[
a(\sqrt N)
=
\frac12\log \sqrt N
=
\frac14\log N
=
\frac12 a(N).
\]

Therefore

\[
\boxed{
N\mapsto\sqrt N
\quad\Longleftrightarrow\quad
a\mapsto\frac a2.
}
\tag{3}
\]

This is the exact logarithmic representation of the new sieve RG fold.

No claim is made that Suzuki's operator itself obeys an exact RG conjugacy under \(a\mapsto a/2\); only the arithmetic support scale matches exactly.

---

## 2. Jost propagation in arithmetic variables [D]

v13.938 gives

\[
h_{a,\delta}^{\circ}(z)
=
e^{2iaz}
\frac{D_{a,\delta}^{\#}(z)}
{D_{a,\delta}(z)}.
\]

At the canonical deficiency point \(z=i\),

\[
e^{2ia i}
=
e^{-2a}
=
N_a^{-1}.
\]

Therefore the normalized deficiency overlap is

\[
\boxed{
\kappa_a(\delta)
=
N_a^{-1}
\frac{D_{a,\delta}(-i)}
{D_{a,\delta}(i)}.
}
\tag{4}
\]

The intrinsic double-scaling condition of v13.940,

\[
\kappa_a(\delta_\tau(a))
=
e^{-\tau},
\]

is exactly

\[
\boxed{
\frac{D_{a,\delta_\tau(a)}(-i)}
{D_{a,\delta_\tau(a)}(i)}
=
e^{-\tau}N_a.
}
\tag{5}
\]

Thus the critical Jost amplification compensates the entire arithmetic factor \(N_a\) associated with propagation across the full logarithmic distance \(2a\).

[I] In the sieve language, this is naturally interpreted as the threshold at which seed-scale edge data remain macroscopically coupled across one full lift from

\[
e^a=\sqrt{N_a}
\]

to

\[
e^{2a}=N_a.
\]

This is an interpretation of the exact identity (5), not an independent spectral theorem.

---

## 3. RH-positive zero-side form [D, conditional on RH]

Under RH,

\[
\boxed{
Q_W[f]
=
\sum_\gamma
m_\gamma
|\widehat f(\gamma)|^2,
}
\tag{6}
\]

with real nonzero zero ordinates \(\gamma\), multiplicities \(m_\gamma\), and

\[
\gamma_1:=\inf_\gamma|\gamma|>0.
\]

The aim is to sharpen v13.943's super-algebraic upper bound on the lowest odd finite-interval Rayleigh quotient.

---

## 4. Compactly supported convolution trial state [D]

Choose an even, nonnegative, nonzero function

\[
p\in C_c^\infty(-L,L),
\qquad
\int_{\mathbb R}p(x)\,dx=1.
\]

Let

\[
P(t):=\widehat p(t).
\]

Because \(p\) is a genuine probability density rather than a point mass,

\[
|P(t)|<1
\qquad(t\ne0).
\]

Also \(P(t)\to0\) as \(|t|\to\infty\).

Since the zero ordinates stay outside

\[
(-\gamma_1,\gamma_1),
\]

continuity gives

\[
\boxed{
q
:=
\sup_{|\gamma|\ge\gamma_1}
|P(\gamma)|
<1.
}
\tag{7}
\]

Let

\[
g_n:=p^{*n}.
\]

Then \(g_n\) is even and

\[
\operatorname{supp}g_n
\subset[-nL,nL].
\]

Define the odd trial state

\[
\boxed{
f_n:=g_n'.
}
\tag{8}
\]

Then

\[
\operatorname{supp}f_n
\subset[-nL,nL],
\]

and

\[
\boxed{
\widehat f_n(t)
=
it\,P(t)^n.
}
\tag{9}
\]

---

## 5. Exponential decay of the Weil numerator [D]

Under RH, from (6) and (9),

\[
Q_W[f_n]
=
\sum_\gamma
m_\gamma
\gamma^2
|P(\gamma)|^{2n}.
\]

Fix an integer \(m_0\) large enough that

\[
\sum_\gamma
m_\gamma
\gamma^2
|P(\gamma)|^{2m_0}
<
\infty.
\]

Such an \(m_0\) exists because \(P\) is Schwartz and

\[
N(T)=O(T\log T).
\]

For \(n\ge m_0\),

\[
|P(\gamma)|^{2n}
=
|P(\gamma)|^{2(n-m_0)}
|P(\gamma)|^{2m_0}
\le
q^{2(n-m_0)}
|P(\gamma)|^{2m_0}.
\]

Hence

\[
\boxed{
Q_W[f_n]
\le
C_p q^{2n}.
}
\tag{10}
\]

The harmless factor \(q^{-2m_0}\) is absorbed into \(C_p\).

---

## 6. Polynomial lower bound on the trial norm [D]

By Plancherel,

\[
\|f_n\|_2^2
=
c_F
\int_{\mathbb R}
t^2|P(t)|^{2n}\,dt,
\]

with \(c_F>0\) depending only on Fourier convention.

Since \(p\) is even with finite positive variance

\[
\sigma_p^2
=
\int x^2p(x)\,dx>0,
\]

we have

\[
P(t)
=
1-\frac{\sigma_p^2}{2}t^2+O(t^4)
\qquad(t\to0).
\]

Therefore there exist \(c_0,c_1>0\) such that for all sufficiently large \(n\),

\[
|P(t)|^{2n}\ge c_0
\qquad
\left(|t|\le c_1n^{-1/2}\right).
\]

Consequently

\[
\|f_n\|_2^2
\ge
c
\int_0^{c_1n^{-1/2}}t^2dt
\]

and hence

\[
\boxed{
\|f_n\|_2^2
\ge
c_p n^{-3/2}.
}
\tag{11}
\]

---

## 7. Exponential odd-sector Rayleigh upper bound [D]

Choose

\[
n(a)
=
\left\lfloor\frac{a}{L}\right\rfloor-1
\]

for all sufficiently large \(a\).

Then

\[
\operatorname{supp}f_{n(a)}
\subset(-a,a),
\]

and \(f_{n(a)}\) is odd.

Therefore

\[
\lambda_a^{(-)}
\le
\frac{Q_W[f_{n(a)}]}
{\|f_{n(a)}\|_2^2}.
\]

Using (10)–(11),

\[
\lambda_a^{(-)}
\le
C
n(a)^{3/2}
q^{2n(a)}.
\]

Since

\[
n(a)
=
\frac aL+O(1),
\]

there are constants \(C,c>0\) depending on \(p\) such that

\[
\boxed{
\lambda_a^{(-)}
\le
C a^{3/2}e^{-ca}.
}
\tag{12}
\]

One may take any

\[
c<
\frac{2|\log q|}{L}
\]

after increasing \(C\).

---

## 8. Recentered odd gap [D]

Assume, as in v13.943, RH and the standing even-ground hypothesis

\[
\lambda_a=\lambda_a^{(+)}
\]

for sufficiently large \(a\).

Then

\[
\lambda_a\ge0
\]

and

\[
\Delta_a
=
\lambda_a^{(-)}-\lambda_a
\]

satisfies

\[
0\le\Delta_a\le\lambda_a^{(-)}.
\]

Hence

\[
\boxed{
\Delta_a
\le
C a^{3/2}e^{-ca}.
}
\tag{13}
\]

This strictly sharpens the v13.943 stretched-exponential upper bounds.

No lower bound is claimed.

---

## 9. Arithmetic-cutoff form [D]

Using

\[
N_a=e^{2a},
\qquad
a=\frac12\log N_a,
\]

equation (13) becomes

\[
\boxed{
\Delta_a
\le
C
(\log N_a)^{3/2}
N_a^{-\beta},
}
\tag{14}
\]

for some

\[
\beta>0.
\]

Equivalently, in the seed size

\[
S_a:=e^a=\sqrt{N_a},
\]

\[
\boxed{
\Delta_a
\le
C
(\log S_a)^{3/2}
S_a^{-c}.
}
\tag{15}
\]

Thus:

\[
\boxed{
\text{exponential tunneling in the Suzuki log-length }a
\Longleftrightarrow
\text{power-law suppression in arithmetic cutoff }N_a.
}
\]

This is a coordinate conversion, not a new spectral equivalence.

---

## 10. Consequence for the overlap critical scale [C]

Under the one-pole crossover hypotheses of v13.941,

\[
\delta_\tau(a)
\sim
x_\tau\Delta_a.
\]

Therefore (13) implies

\[
\boxed{
\delta_\tau(a)
\le
C_\tau
a^{3/2}e^{-ca}
}
\tag{16}
\]

for sufficiently large \(a\).

In arithmetic variables,

\[
\boxed{
\delta_\tau(a)
\le
C_\tau
(\log N_a)^{3/2}
N_a^{-\beta}.
}
\tag{17}
\]

Thus the overlap-defined double scaling is at least exponentially close to the recentered threshold in logarithmic size.

---

## 11. Exact relevance of the new cone/sieve result [D/I]

The new v13.942 entry supplies three facts relevant here.

### 11.1 Seed/lift scale matching [D]

\[
\boxed{
\sqrt{N_a}=e^a
}
\]

is exactly the arithmetic seed cutoff for the operator whose full difference range reaches \(N_a=e^{2a}\).

### 11.2 Coordinate guardrail [D/I]

v13.942 observes:

- zeta-zero oscillations are naturally resolved in \(\log x\);
- divisor/Voronoi oscillations are naturally resolved in \(\sqrt x\).

The present Suzuki/Jost problem is in the first coordinate.

Therefore the divisor \(x^{1/4}\) phenomenon must **not** be imported into the Suzuki gap exponent.

### 11.3 One-lift interpretation [I]

Equation (5) says the critical overlap occurs when the Jost amplification grows like the full arithmetic lift \(N_a\).

Thus the finite deficiency overlap is naturally a transfer observable from seed logarithmic scale \(a\) to lifted logarithmic scale \(2a\).

This interpretation uses only exact finite identities already proved in the two lanes.

---

## 12. What this does not prove [G]

The present theorem does not establish:

- a matching exponential lower bound;
- an exact rate constant \(c\);
- one-pole dominance;
- a limit for the residue ratio \(r_a\);
- RH;
- an unconditional positive zero-side representation;
- a direct relation between the divisor \(1/4\) conjecture and the Suzuki gap.

In particular,

\[
\Delta_a
\]

may decay faster than \(e^{-ca}\).

---

## 13. Next nonredundant gate [O]

The remaining finite-size problem is now an extremal concentration problem.

Define the optimal odd gap rate

\[
\boxed{
\beta_*
:=
\liminf_{a\to\infty}
-\frac1a\log\Delta_a
}
\]

when the limit is meaningful.

The convolution theorem proves only

\[
\beta_*>0
\]

in the upper-bound sense that exponentially small odd trial quotients exist.

The next tasks are:

1. optimize the compactly supported probability kernel \(p\) to maximize
   \[
   \frac{-2\log q}{L};
   \]
2. compare this with the true Paley–Wiener concentration extremal for the zero-sampling set;
3. derive any matching lower bound;
4. track the source residues \(\alpha_a,\beta_a\);
5. test whether the exact sieve fold \(a\mapsto a/2\) induces a useful recursion for those extremals.

That is the correct point at which the new cone/sieve RG can feed back into the Suzuki threshold problem.

---

## 14. Result

The new cone/sieve flow and the Suzuki/Jost cutoff have the exact scale identification

\[
\boxed{
N_a=e^{2a},
\qquad
\sqrt{N_a}=e^a.
}
\]

The Jost overlap becomes

\[
\boxed{
\kappa_a(\delta)
=
N_a^{-1}
\frac{D_{a,\delta}(-i)}
{D_{a,\delta}(i)}.
}
\]

Under RH plus the even-ground hypothesis,

\[
\boxed{
\Delta_a
\le
C a^{3/2}e^{-ca}
}
\]

and therefore, in arithmetic cutoff,

\[
\boxed{
\Delta_a
\le
C(\log N_a)^{3/2}N_a^{-\beta}.
}
\]

So the relevant critical behavior is tunneling-like in logarithmic distance and algebraic in arithmetic size.

The divisor \(1/4\) structure remains a separate \(\sqrt x\)-coordinate phenomenon.
