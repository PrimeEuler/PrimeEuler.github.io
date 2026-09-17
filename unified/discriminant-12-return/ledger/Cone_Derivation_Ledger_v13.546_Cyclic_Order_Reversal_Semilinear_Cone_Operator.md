# Cone Derivation Ledger v13.546 — Cyclic-order reversal is a semilinear cone involution

## Context

Continue v13.545, where the verified six null rays

\[
a=[1:0:1],\quad b=[1:0:-1],\quad c=[0:1:1],\quad d=[0:1:-1],\quad e=[1:i:0],\quad f=[1:-i:0]
\]

were identified equivariantly with the six oriented cyclic orderings of \(\Omega=\{1,5,7,11\}\), modulo cyclic rotation:

\[
\begin{array}{c|c}
a&[1,5,11,7]\\ b&[1,7,11,5]\\ c&[1,11,5,7]\\ d&[1,7,5,11]\\ e&[1,5,7,11]\\ f&[1,11,7,5]\end{array}
\]

The task is to identify the cone operator inducing orientation reversal of these cyclic orders.

## 1. Reversal permutation

Reverse a cyclic order while keeping the first displayed entry fixed, then reduce modulo cyclic rotation. From the table above:

\[
[1,5,11,7]^{\rm rev}=[1,7,11,5],
\]
\[
[1,11,5,7]^{\rm rev}=[1,7,5,11],
\]
\[
[1,5,7,11]^{\rm rev}=[1,11,7,5].
\]

Hence orientation reversal acts on the six rays as

\[
\boxed{\rho=(a\ b)(c\ d)(e\ f).}
\]

## 2. No complex-linear 3x3 cone matrix realizes rho

Let \(M\in GL_3(\mathbb C)\). Requiring projectively

\[
Ma\sim b,\ Mb\sim a,\ Mc\sim d,\ Md\sim c,\ Me\sim f,\ Mf\sim e
\]

produces only the zero solution for the entries of \(M\) (together with zero projective scale factors). Therefore there is no invertible complex-linear \(3\times3\) matrix whose projective action on the six rays is \(\rho\).

This is structurally expected: reversal is the nontrivial right-normalizer action on \(S_4/C_4\), commuting with the left \(S_4\) action, whereas the previously constructed linear cone group is projectively the left \(S_4\) action.

## 3. Exact semilinear cone operator

Let \(\kappa\) denote coordinatewise complex conjugation and set

\[
M_T=\operatorname{diag}(1,1,-1).
\]

Define the antilinear/semilinear involution

\[
\boxed{\mathcal R=M_T\kappa,}
\]

that is,

\[
\boxed{\mathcal R(X,Y,T)=(\overline X,\overline Y,-\overline T).}
\]

Directly on the six rays:

\[
\mathcal R(1,0,1)=(1,0,-1)=b,
\]
\[
\mathcal R(1,0,-1)=(1,0,1)=a,
\]
\[
\mathcal R(0,1,1)=(0,1,-1)=d,
\]
\[
\mathcal R(0,1,-1)=(0,1,1)=c,
\]
\[
\mathcal R(1,i,0)=(1,-i,0)=f,
\]
\[
\mathcal R(1,-i,0)=(1,i,0)=e.
\]

Therefore

\[
\boxed{\mathcal R|_{\mathcal N_6}=(a\ b)(c\ d)(e\ f).}
\]

Since \(M_T\) is real and \(M_T^2=I\),

\[
\boxed{\mathcal R^2=I.}
\]

## 4. Cone preservation

For the complexified cone quadratic form

\[
q(X,Y,T)=X^2+Y^2-T^2,
\]

we have

\[
q(\mathcal R(X,Y,T))
=\overline X^2+\overline Y^2-(-\overline T)^2
=\overline{q(X,Y,T)}.
\]

Hence \(q=0\) is preserved exactly. Thus \(\mathcal R\) is a genuine semilinear automorphism of the complexified projective null cone.

## 5. Coset interpretation

Let \(C_4=\langle R\rangle\), with \(R=(1\ 5\ 7\ 11)\). The six cyclic orders are \(S_4/C_4\). The normalizer is

\[
N_{S_4}(C_4)\cong D_8,
\]

and

\[
N_{S_4}(C_4)/C_4\cong C_2.
\]

The nontrivial quotient element acts on cyclic orders by orientation reversal. The cone operator \(\mathcal R\) realizes exactly this commuting involution on the six-ray model.

Thus the natural symmetry visible on the six rays is larger than the projective left \(S_4\) alone: adjoining \(\mathcal R\) supplies the right-normalizer reversal of the cyclic-order torsor.

## 6. Important distinction

There is **no exact complex-linear cone matrix alone** for cyclic-order reversal. The exact realization is semilinear:

\[
\boxed{\mathcal R=\operatorname{diag}(1,1,-1)\circ\text{complex conjugation}.}
\]

This distinction is essential. Writing only \(\operatorname{diag}(1,1,-1)\) gives \((a\ b)(c\ d)\) while fixing \(e,f\); complex conjugation alone gives \((e\ f)\) while fixing \(a,b,c,d\). Their composition gives the full reversal

\[
(a\ b)(c\ d)(e\ f).
\]

## Status

**Exact.** The six-ray permutation and semilinear cone realization are verified directly. The nonexistence statement concerns complex-linear \(3\times3\) projective realizations on this six-ray configuration. No claim is made here that this semilinear reversal is identical to any previously named arithmetic or cyclotomic involution; that identification requires a separate intertwining argument.
