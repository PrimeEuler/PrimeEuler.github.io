# Cone Derivation Ledger v13.258 — Exact D12 Screw Factorization and Dedekind Additivity

Date: 2026-09-05
Status: EXACT NEW RESULT + SOURCE-ESTABLISHED SUZUKI SPECIALIZATION — continuation of v13.257; RH/GRH frontier remains open

## 0. Synchronization and strategy

Immediately before this write, the authoritative project README, current `master` tip, and v13.257 were re-fetched. The tip remained

`2bbe2ec3ffc610bfd9368cff61d989b43612caf9`

with v13.257 as the highest ledger checkpoint. No newer external-audit checkpoint had landed.

The strategic priority remains

\[
\boxed{
\text{D12/Suzuki bridge}
>
\text{H4/H8 analytic channels}
>
\text{q=11 lift side branch}.
}
\]

This entry works exactly at the point where the two routes identified in v13.257 meet:

\[
\text{D12 divisor coefficients}
\to
\text{logarithmic derivative}
\]

and

\[
\text{completed }L\text{-function}
\to
\text{Suzuki screw function}.
\]

The result is an explicit screw function for `L(s,chi_12)` and, more strongly, an exact Dedekind-field screw function reconstructed directly from the divisor/ideal coefficient sequence `a_12(n)`.

## 1. Source-established Suzuki input

Masatoshi Suzuki's paper *Screw functions of Dirichlet series in the extended Selberg class* proves the following for a member `F` of the semi-extended Selberg class.

If

\[
\xi_F(s)
=s^{m_F}(s-1)^{m_F}Q^s
\prod_{j=1}^r\Gamma(\lambda_j s+\mu_j)F(s),
\]

then the associated screw function `g_F` has a zero-free representation `Phi_F=-g_F` built from:

- the pole term determined by `m_F`;
- the logarithmic-derivative coefficients of `F`;
- the conductor factor `Q`;
- the gamma parameters `(lambda_j,mu_j)`.

Suzuki also proves the transform identity

\[
\boxed{
\int_0^\infty g_F(t)e^{izt}\,dt
=
\frac{1}{z^2}
\frac{\xi_F'}{\xi_F}
\left(\frac12-iz\right),
\qquad \Im z>\frac12,
}
\]

and, under the stated real-zero hypothesis, the GRH criterion

\[
\boxed{
\operatorname{GRH}(F)
\iff
\Re\bigl(-g_F(t)\bigr)\ge0
\text{ for all sufficiently large }t.
}
\]

For real-valued `F=F*`, the screw function is real-valued.

The present entry only specializes these source-established formulas to the already-audited D12 objects.

## 2. The primitive D12 completed L-function

Let

\[
\chi=\chi_{12},
\]

the primitive even quadratic character of conductor `12`.

Its completed function may be taken as

\[
\boxed{
\Lambda_{12}(s)
:=
\left(\frac{12}{\pi}\right)^{s/2}
\Gamma\left(\frac{s}{2}\right)
L(s,\chi_{12}).
}
\]

Thus, in Suzuki's Selberg-class notation,

\[
m_F=0,
\qquad
Q=\sqrt{\frac{12}{\pi}},
\qquad
\lambda=\frac12,
\qquad
\mu=0.
\]

The common gamma parameter is therefore

\[
\frac{\lambda}{2}+\mu=\frac14.
\]

Define

\[
C_{1/4}:=\Phi(1,2,1/4)=\zeta(2,1/4),
\]

where `Phi` is the Hurwitz-Lerch zeta function.

## 3. Exact D12 archimedean term

Specializing Suzuki's zero-free formula with the parameters above gives the D12 archimedean ramp

\[
\boxed{
\mathcal A_{12}(t)
=
\frac{t}{2}
\left[
\psi\left(\frac14\right)
+\log\frac{12}{\pi}
\right]
+
\frac14
\left[
C_{1/4}
-e^{-t/2}
\Phi\left(e^{-2t},2,\frac14\right)
\right],
\qquad t\ge0.
}
\]

Here `psi=Gamma'/Gamma`.

There is no `4(e^{t/2}+e^{-t/2}-2)` term because `L(s,chi_12)` has no pole at `s=1`.

## 4. Exact D12 character screw function

Define the prime-power ramp

\[
\boxed{
\mathcal R_{12}(t)
:=
\sum_{n\le e^t}
\frac{\Lambda(n)\chi_{12}(n)}{\sqrt n}
(t-\log n).
}
\]

This is exactly

\[
\mathcal R_{12}(t)
=
\mathcal S_{12}(e^t)
\]

in the notation of v13.256-v13.257.

The specialized Suzuki zero-free formula is then

\[
\boxed{
\Phi_{12}(t)
:=-g_{L(s,\chi_{12})}(t)
=
\mathcal A_{12}(t)-\mathcal R_{12}(t).
}
\]

Explicitly,

\[
\boxed{
\begin{aligned}
\Phi_{12}(t)
={}&
-\sum_{n\le e^t}
\frac{\Lambda(n)\chi_{12}(n)}{\sqrt n}
(t-\log n)
\\
&+
\frac{t}{2}
\left[
\psi\left(\frac14\right)
+\log\frac{12}{\pi}
\right]
\\
&+
\frac14
\left[
\zeta\left(2,\frac14\right)
-e^{-t/2}
\Phi\left(e^{-2t},2,\frac14\right)
\right].
\end{aligned}
}
\]

This is the exact quadratic-character analogue of Suzuki's zeta screw kernel for the discriminant-12 field character.

No cone-geometric interpretation is being imposed here; this is a direct specialization of the published Selberg-class formula.

## 5. Laplace form and the weighted Chebyshev channel

Put

\[
s=\frac12+z,
\qquad \Re z>\frac12.
\]

Then

\[
\int_0^\infty
\mathcal R_{12}(t)e^{-zt}\,dt
=
-\frac1{z^2}
\frac{L'}{L}
\left(\frac12+z,\chi_{12}\right).
\]

Indeed, term by term,

\[
\int_{\log n}^{\infty}
(t-\log n)e^{-zt}\,dt
=
\frac{n^{-z}}{z^2}.
\]

Therefore

\[
\boxed{
\int_0^\infty
\Phi_{12}(t)e^{-zt}\,dt
=
\frac1{z^2}
\frac{\Lambda_{12}'}{\Lambda_{12}}
\left(\frac12+z\right).
}
\]

This is exactly the real-Laplace form of Suzuki's Fourier-Laplace screw transform.

Thus the previously isolated weighted Chebyshev channel is precisely the non-archimedean part of the D12 screw function.

## 6. Insert the v13.257 coefficient bridge

From v13.257,

\[
a(n)=a_{12}(n)=\sum_{d\mid n}\chi_{12}(d)
\]

satisfies

\[
\sum_{n\ge1}\frac{a(n)}{n^s}
=
\zeta_{\mathbf Q(\sqrt3)}(s),
\]

and the Dedekind von Mangoldt coefficient is

\[
\boxed{
b=(a\log)*a^{-1}
=\Lambda(1+\chi_{12}).
}
\]

Hence

\[
\Lambda\chi_{12}=b-\Lambda.
\]

Substituting this into the screw formula gives

\[
\boxed{
\Phi_{12}(t)
=
\mathcal A_{12}(t)
-
\sum_{n\le e^t}
\frac{b(n)-\Lambda(n)}{\sqrt n}
(t-\log n).
}
\]

Equivalently,

\[
\boxed{
\Phi_{12}(t)
=
\mathcal A_{12}(t)
-
\sum_{n\le e^t}
\frac{[(a\log)*a^{-1}](n)-\Lambda(n)}{\sqrt n}
(t-\log n).
}
\]

This is the exact meeting point of the two research routes.

The D12 screw function is reconstructible from the divisor/ideal coefficient sequence `a_12` plus the universal principal von Mangoldt sequence.

## 7. The stronger field-level object: the Dedekind screw function

Now take

\[
K=\mathbf Q(\sqrt3),
\qquad D_K=12.
\]

The completed Dedekind zeta function can be written as

\[
\boxed{
\Lambda_K(s)
=
12^{s/2}\pi^{-s}
\Gamma\left(\frac{s}{2}\right)^2
\zeta_K(s).
}
\]

Because `zeta_K` has a simple pole at `s=1`, its Suzuki data are

\[
m_F=1,
\qquad
Q=\frac{\sqrt{12}}{\pi},
\qquad
r=2,
\qquad
\lambda_1=\lambda_2=\frac12,
\qquad
\mu_1=\mu_2=0.
\]

The non-archimedean logarithmic-derivative coefficient is exactly

\[
\boxed{
b(n)=\Lambda(n)(1+\chi_{12}(n)),}
\]

which v13.257 reconstructs directly from `a_12`.

Therefore the complete field-level zero-free screw function is

\[
\boxed{
\begin{aligned}
\Phi_K(t)
={}&
4\left(e^{t/2}+e^{-t/2}-2\right)
\\
&-
\sum_{n\le e^t}
\frac{b(n)}{\sqrt n}(t-\log n)
\\
&+
 t\left[
\psi\left(\frac14\right)
+\log\frac{\sqrt{12}}{\pi}
\right]
\\
&+
\frac12
\left[
\zeta\left(2,\frac14\right)
-e^{-t/2}
\Phi\left(e^{-2t},2,\frac14\right)
\right].
\end{aligned}
}
\]

Using

\[
b=(a\log)*a^{-1},
\]

we get the central coefficient-to-screw theorem of this entry:

\[
\boxed{
\begin{aligned}
\Phi_K(t)
={}&
4\left(e^{t/2}+e^{-t/2}-2\right)
\\
&-
\sum_{n\le e^t}
\frac{[(a_{12}\log)*a_{12}^{-1}](n)}{\sqrt n}
(t-\log n)
\\
&+
 t\left[
\psi\left(\frac14\right)
+\log\frac{\sqrt{12}}{\pi}
\right]
\\
&+
\frac12
\left[
\zeta\left(2,\frac14\right)
-e^{-t/2}
\Phi\left(e^{-2t},2,\frac14\right)
\right].
\end{aligned}
}
\]

Thus:

\[
\boxed{
\text{D12 divisor coefficients }a_{12}
\Longrightarrow
\text{complete Dedekind screw function }\Phi_K.
}
\]

No separate extraction of `chi_12` is required at field level.

This is stronger than v13.257.

## 8. Exact additivity of the principal and quadratic screw channels

The factorization

\[
\zeta_K(s)=\zeta(s)L(s,\chi_{12})
\]

extends to the completed factors:

\[
\Lambda_K(s)
=
\Lambda_\zeta(s)\Lambda_{12}(s)
\]

up to an irrelevant nonzero constant normalization.

Taking logarithmic derivatives gives

\[
\frac{\Lambda_K'}{\Lambda_K}
=
\frac{\Lambda_\zeta'}{\Lambda_\zeta}
+
\frac{\Lambda_{12}'}{\Lambda_{12}}.
\]

By uniqueness of Suzuki's inverse transform,

\[
\boxed{
\Phi_K(t)
=
\Phi_\zeta(t)+\Phi_{12}(t).
}
\]

Equivalently for the screw functions themselves,

\[
\boxed{
g_K(t)=g_\zeta(t)+g_{12}(t).}
\]

This is an exact analytic counterpart of the principal/quadratic Walsh decomposition already present in the V4 shell.

In words:

\[
\boxed{
\text{Dedekind field channel}
=
\text{principal zeta channel}
+
\text{D12 quadratic channel}.
}
\]

This is not an analogy; it is forced by multiplicativity of completed L-functions and linearity of the logarithmic derivative.

## 9. The V4 interpretation is now exact at three levels

The project now has the same principal/quadratic split at three distinct arithmetic levels.

### Coefficient level

\[
\boxed{
a_{12}=1*\chi_{12}.}
\]

### Logarithmic-derivative level

\[
\boxed{
b=\Lambda+\Lambda\chi_{12}.}
\]

### Screw-function level

\[
\boxed{
\Phi_K=\Phi_\zeta+\Phi_{12}.}
\]

So the same D12 character decomposition propagates through

\[
\boxed{
\text{Dirichlet coefficients}
\to
\text{von Mangoldt coefficients}
\to
\text{continuous screw kernel}.
}
\]

This is the first fully exact bridge from the finite V4 arithmetic shell to Suzuki's continuous Weil/GRH framework.

## 10. Distributional second derivative of the prime ramp

The non-archimedean ramp has an especially simple distributional structure.

For

\[
\mathcal R_{12}(t)
=
\sum_n
\frac{\Lambda(n)\chi_{12}(n)}{\sqrt n}
(t-\log n)_+,
\]

we have

\[
\boxed{
\mathcal R_{12}''(t)
=
\sum_{n\ge1}
\frac{\Lambda(n)\chi_{12}(n)}{\sqrt n}
\delta(t-\log n)
}
\]

in the sense of distributions.

Likewise, for the Dedekind ramp

\[
\mathcal R_K(t)
=
\sum_n
\frac{b(n)}{\sqrt n}(t-\log n)_+,
\]

\[
\boxed{
\mathcal R_K''(t)
=
\sum_{n\ge1}
\frac{[(a_{12}\log)*a_{12}^{-1}](n)}{\sqrt n}
\delta(t-\log n).
}
\]

Thus the discrete divisor coefficient sequence determines the atomic non-archimedean second derivative of the continuous field screw kernel exactly.

This is potentially useful for the Weil-quadratic-form route because the continuous kernel and the explicit-formula distribution are now visibly two integrations apart.

## 11. Relation to the Weil frontier

Suzuki's 2025 Selberg-class screw-function theorem states that, under its real-zero hypothesis,

\[
\operatorname{GRH}(F)
\iff
\Re\Phi_F(t)\ge0
\text{ eventually}.
\]

His subsequent work develops the relation between screw kernels and Weil's quadratic form, replacing distributional formulations by continuous-function kernels.

For the D12 field, the present entry supplies an arithmetic realization of that continuous kernel:

\[
\boxed{
\Phi_K
=
\text{explicit archimedean term}
-
\mathcal R_{(a_{12}\log)*a_{12}^{-1}}
+
\text{pole term}.
}
\]

Therefore the exact D12 route to the Weil frontier is now

\[
\boxed{
\begin{array}{c}
a_{12}(n)=\sum_{d\mid n}\chi_{12}(d)
\\[4pt]
\downarrow\ \mathcal L_D
\\[4pt]
b(n)=\Lambda(n)(1+\chi_{12}(n))
\\[4pt]
\downarrow\ \text{ramp integration}
\\[4pt]
\Phi_K(t)
\\[4pt]
\downarrow
\\[4pt]
\text{Suzuki / Weil positivity framework}.
\end{array}
}
\]

This chain is exact through the construction of `Phi_K`. The final positivity/GRH step remains a theorem of Suzuki subject to its stated hypotheses; this project has not proved the needed positivity.

## 12. Why this route has higher value than another finite resonance classification

The q=11 lift branch showed that finite modulo-q Hasse/jet conditions can become very flexible and can fail to control the exact integer signal.

By contrast, the D12 screw bridge here does not discard information modulo a crossing prime. It retains the complete logarithmic-derivative coefficient sequence and carries it directly into the analytic object whose sign/positivity is tied to zero location.

So the current strategic ordering is strengthened to

\[
\boxed{
\text{D12 Dedekind screw / Weil kernel}
>
\text{H4/H8 multi-L kernel structure}
>
\text{isolated finite crossing-lift classifications}.
}
\]

The finite resonance branch remains valuable when it supplies a reusable transform identity, but not as the main route to the RH frontier.

## 13. What is proved

Proved exactly in this entry:

1. the explicit Suzuki zero-free screw formula for `L(s,chi_12)`;
2. the exact Laplace transform of its weighted prime-power ramp;
3. the explicit field-level screw function for `zeta_{Q(sqrt3)}`;
4. direct reconstruction of the field screw function from `a_12` through
   \[
   b=(a_{12}\log)*a_{12}^{-1};
   \]
5. completed-factor additivity
   \[
   \Phi_K=\Phi_\zeta+\Phi_{12};
   \]
6. the distributional second derivative of the D12 and Dedekind prime ramps.

Not proved:

\[
\operatorname{GRH}(L(s,\chi_{12})),
\]

nor

\[
\operatorname{GRH}(\zeta_{\mathbf Q(\sqrt3)}).
\]

No claim is made that the cone geometry itself implies Suzuki/Weil positivity.

## 14. Next high-value target

The next step should not be numerical sign chasing by itself.

The next structural target is to insert the exact additive screw decomposition

\[
\Phi_K=\Phi_\zeta+\Phi_{12}
\]

into Suzuki's continuous kernel associated with the Weil quadratic form.

The key question is whether the quadratic V4 channel induces an exact orthogonal or signed decomposition of the corresponding Weil kernel / Hermitian form:

\[
\boxed{
G_K
\stackrel{?}{=}
G_\zeta+G_{12}
}
\]

and, if so, whether the `H4` character transform diagonalizes a direct sum of four such quadratic forms.

Because the screw kernel `G_g(t,u)` is linear in `g`, the first equality should be formally exact once notation and domains are aligned. The nontrivial issue is positivity: positivity of a sum does not imply positivity of each summand, so the V4/H4 structure must be audited at the Hermitian-form level rather than inferred from scalar sign identities.

That is the next frontier with the highest expected value.