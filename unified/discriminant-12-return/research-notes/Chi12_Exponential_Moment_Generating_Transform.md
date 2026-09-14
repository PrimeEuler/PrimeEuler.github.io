# χ12 Exponential Moment-Generating Transform

**Status:** exact continuation of the χ12 shell-displacement moment hierarchy. Exact identities are marked `[D]`; interpretive comments `[I]`.

## 1. Finite exponential transform of the shell-displacement field [D]

Let

\[
\delta_k(n)=\left\{\frac nk\right\}\in[0,1),
\qquad
\chi=\chi_{12}.
\]

For integer moments

\[
M_j(n)=\sum_{k\le n}\chi(k)\,\delta_k(n)^j,
\qquad j\ge1,
\]

define the exponential generating transform

\[
\boxed{
\mathcal G_n(t)
:=\sum_{j\ge1}\frac{t^j}{j!}M_j(n).
}
\]

Because the sum over `k` is finite,

\[
\boxed{
\mathcal G_n(t)
=\sum_{k\le n}\chi(k)\left(e^{t\delta_k(n)}-1\right).
}
\]

Using

\[
q_k=\left\lfloor\frac nk\right\rfloor,
\qquad
\delta_k=\frac nk-q_k,
\]

we also have

\[
\boxed{
\mathcal G_n(t)
=\sum_{k\le n}\chi(k)
\left(e^{tn/k-tq_k}-1\right).
}
\]

This is an entire function of `t` for each fixed `n`.

## 2. Recovery of the first three moments [D]

Taylor expansion gives

\[
\boxed{
\mathcal G_n(t)
=tE_{12}(n)
+\frac{t^2}{2}Q_{12}(n)
+\frac{t^3}{6}M_3(n)
+O(t^4).
}
\]

Thus

\[
\mathcal G_n'(0)=E_{12}(n),
\qquad
\mathcal G_n''(0)=Q_{12}(n),
\qquad
\mathcal G_n^{(3)}(0)=M_3(n).
\]

The whole integer-moment hierarchy is therefore encoded by one finite exponential transform.

## 3. Dirichlet-L kernel for the full moment tower [D]

Define

\[
\boxed{
\Phi_{12}(z)
:=\sum_{j\ge1}\frac{L(j,\chi_{12})}{j!}z^j.
}
\]

Since the factorial denominator dominates the bounded Dirichlet values, `Phi_12` is entire.

Equivalently,

\[
\boxed{
\Phi_{12}(z)
=\sum_{k\ge1}\chi_{12}(k)\left(e^{z/k}-1\right),
}
\]

where the linear `z/k` part is interpreted by Dirichlet convergence and the remaining `O(k^{-2})` part converges absolutely and locally uniformly.

Its first terms are

\[
\Phi_{12}(z)
=L(1,\chi_{12})z
+\frac{L(2,\chi_{12})}{2}z^2
+\frac{L(3,\chi_{12})}{6}z^3+\cdots.
\]

Thus the special values already found in the first three moments are coefficients of a single analytic kernel:

\[
L(1,\chi_{12})=\frac{\log(2+\sqrt3)}{\sqrt3},
\]

\[
L(2,\chi_{12})=\frac{\pi^2}{6\sqrt3},
\]

and

\[
L(3,\chi_{12})
=\frac1{12^3}
\left[
\zeta\!\left(3,\frac1{12}\right)
-\zeta\!\left(3,\frac5{12}\right)
-\zeta\!\left(3,\frac7{12}\right)
+\zeta\!\left(3,\frac{11}{12}\right)
\right].
\]

## 4. Exact transform decomposition [D]

Define the tail transform

\[
\boxed{
\Theta_n(t)
:=\sum_{k>n}\chi(k)\left(e^{tn/k}-1\right).
}
\]

Also define the quotient-skeleton correction

\[
\boxed{
\mathcal K_n(t)
:=\sum_{k\le n}\chi(k)e^{tn/k}
\left(e^{-tq_k}-1\right).
}
\]

Then

\[
\sum_{k\le n}\chi(k)(e^{tn/k}-1)
=\Phi_{12}(nt)-\Theta_n(t),
\]

so

\[
\boxed{
\mathcal G_n(t)
=\Phi_{12}(nt)-\Theta_n(t)+\mathcal K_n(t).
}
\]

Define the transform remainder

\[
\boxed{
\mathfrak R_n(t)
:=-\Phi_{12}(nt)-\mathcal K_n(t)
}
\]

or equivalently

\[
\boxed{
\mathfrak R_n(t)
=-\Phi_{12}(nt)
+\sum_{k\le n}\chi(k)e^{tn/k}
\left(1-e^{-tq_k}\right).
}
\]

Then the entire hierarchy collapses to the single exact identity

\[
\boxed{
\mathcal G_n(t)
=-\mathfrak R_n(t)-\Theta_n(t).
}
\]

## 5. Coefficient recovery of the moment remainders [D]

Expand

\[
\mathfrak R_n(t)
=\sum_{j\ge1}\frac{\mathcal R_j(n)}{j!}t^j.
\]

Then coefficient comparison with the exact general moment identity gives

\[
\boxed{
M_j(n)
=-\mathcal R_j(n)-n^jT_j(n),
}
\]

where

\[
T_j(n)=\sum_{k>n}\frac{\chi(k)}{k^j}.
\]

In particular,

\[
\mathcal R_1
=\sum_{k\le n}\chi(k)q_k
-nL(1,\chi),
\]

\[
\mathcal R_2
=2n\sum_{k\le n}\frac{\chi(k)q_k}{k}
-\sum_{k\le n}\chi(k)q_k^2
-n^2L(2,\chi),
\]

and

\[
\mathcal R_3
=3n^2\sum_{k\le n}\frac{\chi(k)q_k}{k^2}
-3n\sum_{k\le n}\frac{\chi(k)q_k^2}{k}
+\sum_{k\le n}\chi(k)q_k^3
-n^3L(3,\chi).
\]

Thus the first-, second-, and third-moment cancellation formulas are exactly the first three Taylor coefficients of `mathfrak R_n`.

## 6. Universal residue-boundary transform [D]

Let

\[
S(r)=\sum_{a=1}^{r}\chi_{12}(a),
\qquad 0\le r\le11.
\]

The previously established momentwise tail law is

\[
n^jT_j(n)\to -S(r)
\]

along every fixed residue class

\[
n\equiv r\pmod{12}.
\]

For each `j>=1`, summation by parts gives a uniform bound

\[
|n^jT_j(n)|\le 2
\]

(up to the harmless endpoint normalization already used in the earlier entries). Therefore the exponential series is dominated on compact `t`-sets by

\[
2\sum_{j\ge1}\frac{|t|^j}{j!}.
\]

Hence dominated convergence applies coefficientwise and locally uniformly in `t`:

\[
\boxed{
\Theta_n(t)
=\sum_{j\ge1}\frac{t^j}{j!}n^jT_j(n)
\longrightarrow
-S(r)(e^t-1).
}
\]

Consequently,

\[
\boxed{
\mathcal G_n(t)
=-\mathfrak R_n(t)
+S(r)(e^t-1)+o(1)
}
\]

locally uniformly in `t` along `n≡r (mod 12)`.

This is the generating-function form of the universal five-level residue profile.

## 7. Why the same boundary correction appears at every moment [D/I]

The common limit

\[
S(r)(e^t-1)
\]

has Taylor coefficients

\[
S(r),\ S(r),\ S(r),\ldots
\]

in exponential-generating normalization:

\[
S(r)(e^t-1)
=\sum_{j\ge1}\frac{S(r)}{j!}t^j.
\]

Therefore the fact that every fixed moment has the same asymptotic residue correction

\[
M_j(n)
=-\mathcal R_j(n)+S(r)+O(n^{-1})
\]

is not a sequence of unrelated coincidences. It is the coefficient shadow of one exponential boundary transform.

**[I]** Since `chi_12` is independently the Pell time-orientation character, this boundary transform packages the incomplete final mod-12 block's orientation imbalance across all displacement moments simultaneously. The shell-displacement carrier and Pell/Galois carrier remain distinct.

## 8. Guardrails

1. `Phi_12` packages Dirichlet `L(j,chi_12)` values; it is not itself a Pell orbit or cone trajectory.
2. The appearance of `L(1,chi_12)` as the Pell regulator is special to the first coefficient. Higher coefficients are distinct Dirichlet special values.
3. The exact transform identity does not make the positive-order displacement moments multiplicative.
4. The universal boundary factor `S(r)(e^t-1)` comes from periodic character tails, not from a Casimir/null-diamond quarter or from V4 shell motion.

## 9. Next exact targets

- study the ordinary (rather than exponential) generating transform in moment order;
- determine whether `Phi_12` admits a useful closed representation in terms of gamma/Hurwitz-Lerch functions;
- study centered/cumulant-like transforms of the signed displacement measure;
- compare the four V4 character transforms simultaneously by Hadamard inversion.

---

**Checkpoint conclusion.** The complete χ12 integer-moment hierarchy is encoded by one entire shell-displacement transform. Its analytic main-scale tower is the entire Dirichlet kernel `Phi_12`, its arithmetic quotient-skeleton correction is `mathfrak R_n`, and its residue-class boundary correction converges to the universal exponential profile `S(r)(e^t-1)`. The repeated five-level correction at every moment is therefore one generating-function phenomenon.