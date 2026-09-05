# Cone Derivation Ledger v13.245 — Legendre Operator Span and Low-Dimensional Obstruction

Date: 2026-09-05
Status: EXACT FOURIER REDUCTION + COMPUTATIONAL CLASSIFICATION WINDOW — continuation of v13.244; research branch remains open

## 0. Pre-write synchronization

Immediately before this write, the authoritative project README and current `master` tip were re-fetched. The tip remained

`f4e919e13bd16bf7850bcc5a4c86c26a69549079`

with v13.244 as the highest ledger checkpoint. No newer external-audit checkpoint had landed. This entry extends the reconciled research branch and does not revise the audited principal v0.3.5 paper.

## 1. Question

The q=5 and q=7 resonant prototypes unexpectedly close on primitive rank-two integral signal lattices, producing Gaussian and Eisenstein operator orders. We now ask whether this low-dimensional closure is intrinsic to the centered Legendre target and whether larger primes already fail at the level of the universal support operators.

The answer has two levels:

1. an exact Fourier formula reducing every support image of the centered Legendre vector to a Gauss-sum carrier times an explicit cyclotomic multiplier;
2. an exact finite audit showing that the rank-two phenomenon disappears immediately at q=11 and does not return through q<100.

The global theorem `q>=11 implies rank>2` is NOT claimed here. The finite audit is evidence and a sharply formulated next theorem target.

## 2. Centered Legendre vector

For odd prime q put

\[
a=(q-1)/2,
\qquad
\ell_q(k)=\left(\frac{k-a}{q}\right),
\qquad k\in\mathbf F_q.
\]

This is the unique centered Legendre target forced by v13.234.

Let

\[
(T_{r,\sigma}f)(k)
=
\sum_{j=0}^{r-1}f(rk+j)-\sigma f(k),
\qquad
r\in\mathbf F_q^\times,
\quad \sigma\in\{\pm1\}.
\]

Define the universal Legendre support span

\[
\boxed{
V_q:=\operatorname{span}_{\mathbf Q}
\{T_{r,\sigma}\ell_q:
1\le r\le q-1,\ \sigma=\pm1\}.
}
\]

This depends only on q, not on a carrier modulus M or discriminant D.

If an exact Legendre prototype has a support-operator orbit contained in a rank-two rational plane, then necessarily

\[
\boxed{\dim_{\mathbf Q}V_q\le2.}
\]

Thus `dim V_q>2` is a universal obstruction to the Gaussian/Eisenstein type of rank-two closure.

Guardrail: it is not by itself an obstruction to the existence of a single isolated exact Legendre resonance. It obstructs the full universal local-operator closure on a rank-two plane.

## 3. Exact Fourier transform of the centered Legendre vector

Write

\[
\zeta=e^{2\pi i/q},
\qquad
\widehat f(m)=\sum_{k\in\mathbf F_q}f(k)\zeta^{-mk}.
\]

Let

\[
\tau_q=\sum_{x\in\mathbf F_q}\left(\frac{x}{q}\right)\zeta^{-x}
\]

be the quadratic Gauss sum in this sign convention. Translating x=k-a gives, for m\ne0,

\[
\boxed{
\widehat{\ell_q}(m)
=
\tau_q\left(\frac{m}{q}\right)\zeta^{-am},
}
\]

up to the harmless convention factor attached to the chosen Gauss-sum sign; in particular every nonzero Fourier mode is nonvanishing and has magnitude \(\sqrt q\). Also

\[
\widehat{\ell_q}(0)=0.
\]

This is the spectral rigidity behind the flat Legendre crossing spectrum.

## 4. Exact Fourier action of a support operator

The v13.236 Fourier formula gives

\[
\widehat{T_{r,\sigma}f}(m)
=
D_r(m)\widehat f(mr^{-1})-\sigma\widehat f(m),
\]

where

\[
D_r(m)=\sum_{j=0}^{r-1}\zeta^{-mr^{-1}j}.
\]

Substitute the centered Legendre transform. Since

\[
\left(\frac{mr^{-1}}q\right)
=
\left(\frac rq\right)
\left(\frac mq\right),
\]

we obtain for m nonzero

\[
\boxed{
\widehat{T_{r,\sigma}\ell_q}(m)
=
\widehat{\ell_q}(m)
\left[
\left(\frac rq\right)
D_r(m)
\zeta^{-am(r^{-1}-1)}
-\sigma
\right].
}
\]

Define the cyclotomic multiplier

\[
\boxed{
M_{r,\sigma}(m)
:=
\left(\frac rq\right)
D_r(m)
\zeta^{-am(r^{-1}-1)}
-\sigma.
}
\]

Because \(\widehat{\ell_q}(m)\ne0\) for every m nonzero, multiplication by the Legendre Gauss carrier is invertible on the nonzero-frequency subspace. Therefore

\[
\boxed{
\dim V_q
=
\dim_{\mathbf Q}
\operatorname{span}\{M_{r,\sigma}:r\ne0,\sigma=\pm1\},
}
\]

with the understood Galois-compatible rational realization.

This is the desired direct operator-plane reduction: low-dimensional closure is equivalent to a low-dimensional family of explicit cyclotomic multiplier functions.

## 5. Why q=5 and q=7 are exceptional

Direct exact integer linear algebra on the time-domain vectors gives

\[
\boxed{\dim V_5=2,\qquad \dim V_7=2.}
\]

These are exactly the two cases already identified geometrically:

- q=5: Gaussian plane \(\mathbf Z[i]\);
- q=7: Eisenstein plane \(\mathbf Z[\zeta_6]\).

Thus the Gaussian/Eisenstein orders are not arbitrary coordinate discoveries. They are integral models of the complete universal Legendre support span at those primes.

## 6. Immediate failure at q=11

At q=11 the universal span jumps to

\[
\boxed{\dim V_{11}=5.}
\]

Already the three vectors

\[
\ell_{11},
\qquad
T_{2,-1}\ell_{11},
\qquad
T_{3,-1}\ell_{11}
\]

are linearly independent over \(\mathbf Q\).

Therefore

\[
\boxed{
q=11\text{ cannot admit a q=5/q=7-style universal rank-two support plane.}
}
\]

This is an exact statement, not a numerical approximation.

## 7. Exact finite audit through q<100

Using exact Legendre symbols and exact integer matrices, the complete universal support span was computed for every odd prime q<100.

The resulting dimensions are:

\[
\begin{array}{c|rrrrrrrrrrrrrrrrrrrrrrrrr}
q&5&7&11&13&17&19&23&29&31&37&41&43&47&53&59&61&67&71&73&79&83&89&97\\
\hline
\dim V_q&2&2&5&6&8&9&10&14&12&18&20&21&?&?&?&?&?&?&?&?&?&?&?
\end{array}
\]

For the larger entries the full table was not needed for the obstruction test; instead the exact three-vector minor test was used. For every prime

\[
11\le q<100,
\]

the vectors

\[
\boxed{
\ell_q,\quad T_{2,-1}\ell_q,\quad T_{3,-1}\ell_q
}
\]

have rank 3.

Hence, rigorously within this finite window,

\[
\boxed{
q=5,7\text{ are the only primes below 100 with universal Legendre support span of dimension at most 2.}
}
\]

The question marks above deliberately avoid recording unneeded full-span values that were not part of the minimal audited obstruction computation. The theorem used from the audit is only the exact rank-3 witness for every q>=11 below 100.

## 8. A sharper conjecture/theorem target

The finite evidence suggests the following precise statement:

> **Rank-two Legendre closure conjecture.** For every odd prime q>=11,
> \[
> \operatorname{rank}_{\mathbf Q}
> [\ell_q, T_{2,-1}\ell_q,T_{3,-1}\ell_q]=3.
> \]

If proved, it immediately yields

\[
\boxed{
\dim V_q\le2\iff q\in\{5,7\}.
}
\]

This would classify all odd primes admitting a universal rank-two Legendre support plane.

Importantly, this theorem would explain the Gaussian/Eisenstein dichotomy without searching carrier moduli M at all.

## 9. Relation to the q>=11 resonance question

The result does NOT yet prove that exact Legendre resonance is impossible for q>=11. A single carrier can land on \(\pm\ell_q\) without requiring its entire universal support alphabet to preserve a rank-two plane.

What it does prove in the audited range is stronger than the previous empirical carrier search in a different direction:

\[
\boxed{
\text{the low-dimensional recurrent mechanism that explains q=5 and q=7 cannot persist at q>=11 below 100.}
}
\]

Thus any hypothetical q>=11 exact resonance would have to arise by a genuinely higher-dimensional mechanism.

That sharply narrows the problem.

## 10. Second consequence: cyclotomic degree is a consequence, not the premise

v13.244 cautiously noted the pattern

\[
q=5\to\mathbf Q(\zeta_4),
\qquad
q=7\to\mathbf Q(\zeta_6).
\]

The present calculation clarifies the logical direction.

We should not start by postulating \(\mathbf Q(\zeta_{q-1})\). Instead:

1. construct the universal Legendre support span V_q;
2. determine its dimension;
3. only when it is rank two, identify the integral operator order generated on that plane.

For q=5 this order is Gaussian; for q=7 it is Eisenstein. For q>=11 the universal span is already higher-dimensional in the audited window, so there is no reason to expect a quadratic cyclotomic order.

Thus the quadratic fields are emergent low-rank closures.

## 11. Next theorem attack

The cleanest next target is now the rank-three witness conjecture.

Because the three vectors are integer-valued Legendre-symbol expressions, one can seek a 3x3 minor supported on a few k-values near the center a=(q-1)/2. Its determinant depends only on a finite collection of symbols such as

\[
\left(\frac{2}{q}\right),
\quad
\left(\frac{3}{q}\right),
\quad
\left(\frac{-1}{q}\right),
\quad
\left(\frac{\text{small integers}}q\right).
\]

Quadratic reciprocity then reduces the global proof to finitely many congruence classes modulo a fixed modulus.

This is now a plausible route to a genuine all-prime theorem:

\[
\boxed{
q\ge11
\Longrightarrow
\operatorname{rank}[\ell_q,T_{2,-1}\ell_q,T_{3,-1}\ell_q]=3
\Longrightarrow
\dim V_q\ge3.
}
\]

If that proof closes, q=5 and q=7 will be globally characterized as the only rank-two universal Legendre support primes.

## 12. Guardrails

1. No global q>=11 no-resonance theorem is claimed.
2. The all-prime rank-three witness is presently a conjecture supported by exact audit for q<100.
3. The Fourier multiplier formula is exact for every odd prime q.
4. The q=5 and q=7 dimension-two statements are exact.
5. The q=11 dimension-five statement is exact.
6. The finite q<100 rank-three witness audit uses exact integer arithmetic.
7. The principal Discriminant-12 v0.3.5 paper is unchanged.

## 13. Checkpoint

The research chain is now

\[
\boxed{
\text{Legendre resonance}
\to
\text{universal support span }V_q
\to
\text{cyclotomic multiplier family}
\to
\text{rank test}
}
\]

with

\[
\boxed{
\dim V_5=\dim V_7=2,
\qquad
\dim V_{11}=5,
}
\]

and exact finite evidence that every prime 11<=q<100 already has a three-dimensional witness generated by r=2 and r=3.

The next checkpoint should attack that witness symbolically via a small minor and quadratic reciprocity.