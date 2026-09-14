# Cone Derivation Ledger v13.427 — χ12 Exponential Moment-Generating Transform

Date: 2026-09-14

Status labels: **[D]** exact derived, **[I]** interpretation, **[Audit]** limitation/guardrail.

## 0. Synchronization [D]

Before assigning this checkpoint, the repository head was re-read.

- `v13.420` records the χ12 quadratic displacement/L(2) cancellation.
- `v13.421` records the cyclotomic V4 character projectors.
- `v13.422` records the general χ12 integer-moment hierarchy and cubic test.
- External Audit Round 29 independently verified the `L(2,chi12)` and `L(3,chi12)` values and the v13.420–425 arithmetic entries.
- The concurrent Pell/Suzuki work advanced the ledger through `v13.426`.

No `v13.427` existed when this entry was assigned.

This checkpoint records the generating-function closure of the χ12 shell-displacement moment hierarchy.

## 1. Shell-displacement exponential transform [D]

Let

\[
\delta_k(n)=\left\{\frac nk\right\},
\qquad
\chi=\chi_{12},
\]

and for integers `j>=1`,

\[
M_j(n)=\sum_{k\le n}\chi(k)\delta_k(n)^j.
\]

Define

\[
\boxed{
\mathcal G_n(t)
=\sum_{j\ge1}\frac{t^j}{j!}M_j(n).
}
\]

Since the `k`-sum is finite,

\[
\boxed{
\mathcal G_n(t)
=\sum_{k\le n}\chi(k)
\left(e^{t\delta_k(n)}-1\right).
}
\]

With

\[
q_k=\left\lfloor\frac nk\right\rfloor,
\qquad
\delta_k=\frac nk-q_k,
\]

this becomes

\[
\boxed{
\mathcal G_n(t)
=\sum_{k\le n}\chi(k)
\left(e^{tn/k-tq_k}-1\right).
}
\]

For fixed `n`, `G_n` is entire in `t`.

## 2. First three coefficients [D]

Taylor expansion gives

\[
\boxed{
\mathcal G_n(t)
=tE_{12}(n)
+\frac{t^2}{2}Q_{12}(n)
+\frac{t^3}{6}M_3(n)+O(t^4).
}
\]

Therefore

\[
\boxed{
\mathcal G_n'(0)=E_{12}(n),
\quad
\mathcal G_n''(0)=Q_{12}(n),
\quad
\mathcal G_n^{(3)}(0)=M_3(n).
}
\]

So the first-moment regulator identity, quadratic-energy identity, and cubic test are coefficients of one transform.

## 3. Entire Dirichlet-L kernel [D]

Define

\[
\boxed{
\Phi_{12}(z)
:=\sum_{j\ge1}\frac{L(j,\chi_{12})}{j!}z^j.
}
\]

This is entire. Equivalently,

\[
\boxed{
\Phi_{12}(z)
=\sum_{k\ge1}\chi_{12}(k)
\left(e^{z/k}-1\right),
}
\]

where the linear `z/k` contribution is summed by Dirichlet convergence and the remainder is absolutely and locally uniformly convergent because it is `O(k^{-2})`.

The first coefficients are

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

Thus the regulator and the higher special values belong to one analytic kernel, but they remain distinct coefficients.

## 4. Exact transform decomposition [D]

Define the tail transform

\[
\boxed{
\Theta_n(t)
:=\sum_{k>n}\chi(k)\left(e^{tn/k}-1\right).
}
\]

Define the quotient-skeleton correction

\[
\boxed{
\mathcal K_n(t)
:=\sum_{k\le n}\chi(k)e^{tn/k}
\left(e^{-tq_k}-1\right).
}
\]

Then

\[
\boxed{
\mathcal G_n(t)
=\Phi_{12}(nt)-\Theta_n(t)+\mathcal K_n(t).
}
\]

Define the remainder transform

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

Therefore

\[
\boxed{
\mathcal G_n(t)
=-\mathfrak R_n(t)-\Theta_n(t).
}
\]

This is the generating-function form of the entire moment hierarchy.

## 5. Coefficients recover every moment remainder [D]

Write

\[
\mathfrak R_n(t)
=\sum_{j\ge1}\frac{\mathcal R_j(n)}{j!}t^j.
\]

Then

\[
\Theta_n(t)
=\sum_{j\ge1}\frac{t^j}{j!}
\,n^jT_j(n),
\qquad
T_j(n)=\sum_{k>n}\frac{\chi(k)}{k^j}.
\]

Coefficient comparison gives

\[
\boxed{
M_j(n)
=-\mathcal R_j(n)-n^jT_j(n)
}
\]

for every integer `j>=1`, exactly reproducing v13.422.

The first coefficients are

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

\[
\mathcal R_3
=3n^2\sum_{k\le n}\frac{\chi(k)q_k}{k^2}
-3n\sum_{k\le n}\frac{\chi(k)q_k^2}{k}
+\sum_{k\le n}\chi(k)q_k^3
-n^3L(3,\chi).
\]

## 6. Universal exponential boundary profile [D]

Let

\[
S(r)=\sum_{a=1}^{r}\chi_{12}(a),
\qquad 0\le r\le11.
\]

The earlier momentwise result is

\[
\boxed{
n^jT_j(n)\to -S(r)
}
\]

along each fixed class

\[
n\equiv r\pmod{12}.
\]

Periodic partial sums of `chi_12` are bounded by `1`. Summation by parts gives a uniform bound of the form

\[
|n^jT_j(n)|\le2
\]

for all `j>=1` and `n>=1` (with the same harmless endpoint convention used in v13.413–422).

Hence for `t` in compact sets,

\[
\left|
\frac{t^j}{j!}n^jT_j(n)
\right|
\le
2\frac{|t|^j}{j!},
\]

and dominated convergence applies. Therefore

\[
\boxed{
\Theta_n(t)
\longrightarrow
-S(r)(e^t-1)
}
\]

locally uniformly in `t` along `n≡r mod 12`.

Consequently,

\[
\boxed{
\mathcal G_n(t)
=-\mathfrak R_n(t)
+S(r)(e^t-1)+o(1).
}
\]

The repeated five-level residue correction at every moment is therefore one exponential generating-function phenomenon.

## 7. Coefficient meaning of the universal profile [D/I]

Since

\[
S(r)(e^t-1)
=\sum_{j\ge1}\frac{S(r)}{j!}t^j,
\]

every exponential-generating coefficient equals the same `S(r)`. This explains exactly why

\[
M_j(n)
=-\mathcal R_j(n)+S(r)+O(n^{-1})
\]

has the same boundary term for each fixed integer moment.

**[I]** Combined with v13.414's exact identity

\[
\sigma_r(\lambda)=\lambda^{\chi_{12}(r)},
\]

the boundary factor may be read as the exponential generating transform of the incomplete final mod-12 block's χ12 orientation imbalance. The shell-displacement statistic and the Pell/Galois action remain distinct carriers.

## 8. Audit guardrails

1. `Phi_12` is an analytic package of Dirichlet `L`-values, not a Pell orbit.
2. Only its first coefficient contains the real-quadratic regulator `R_12`; higher coefficients are distinct special values.
3. No multiplicativity of `M_j` or `G_n` is inferred.
4. The boundary factor `S(r)(e^t-1)` comes from the periodic χ12 tail and must not be identified with V4 shell motion, Casimir quarters, or null-diamond invariants.
5. The locally uniform limit is a fixed-residue-class statement in `n mod 12`.

## 9. Next exact targets

- derive simultaneous exponential transforms for all four V4 characters and invert them by `H_4`;
- study the signed displacement measure whose Laplace transform is `G_n`;
- determine whether the four-character transform yields a clean residue-sector reconstruction at every `t`, not just coefficient-by-coefficient;
- investigate closed special-function representations of `Phi_12`.

---

**Checkpoint conclusion.** The complete χ12 shell-displacement moment hierarchy is the Taylor expansion of one entire finite transform. The full tower of analytic main scales is encoded by the entire Dirichlet kernel `Phi_12`; the quotient skeleton supplies the compensating remainder transform `mathfrak R_n`; and the universal residue boundary law sums exactly to `S(r)(e^t-1)`. This provides a single analytic object behind the first, quadratic, cubic, and all higher integer moments.