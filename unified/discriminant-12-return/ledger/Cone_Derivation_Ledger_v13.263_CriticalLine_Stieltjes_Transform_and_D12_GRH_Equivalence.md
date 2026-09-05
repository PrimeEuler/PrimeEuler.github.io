# Cone Derivation Ledger v13.263 — Critical-Line Stieltjes Transform and D12 GRH Equivalence

Date: 2026-09-05
Status: EXACT STRUCTURAL REFORMULATION — RH/GRH NOT PROVED

## 0. Synchronization

Immediately before this write, the authoritative README, current `master` tip, and v13.262 were re-fetched. The tip was

`ebee0e67951b2c82e2e01bcfeb72ec729571d038`,

with v13.262 the highest ledger checkpoint. No newer external-audit entry had landed at the synchronization point.

This entry follows the v13.262 suggestion to compare the positive Euler-product Laplace transform with the completed logarithmic derivative, but first imposes an important guardrail:

> A Laplace transform of a positive measure is completely monotone on the positive real axis, but is **not generically a Stieltjes, Pick, or Herglotz function** in the complex variable.

Indeed, for `z=x+iy`, the real part contains `cos(yu)` and need not retain a sign. Thus the positive prime measure by itself does not supply the desired half-plane Pick property.

The correct Stieltjes structure appears after **completion, critical-line centering, and squaring the centered spectral coordinate**.

## 1. Completed Dedekind function for K=Q(sqrt3)

For the real quadratic field

\[
K=\mathbf Q(\sqrt3),\qquad d_K=12,
\]

with signature `(r_1,r_2)=(2,0)`, use

\[
\Lambda_K(s)
=12^{s/2}\pi^{-s}\Gamma(s/2)^2\zeta_K(s).
\]

Define the entire completed xi-function

\[
\boxed{
\xi_K(s):=s(s-1)\Lambda_K(s).
}
\]

An irrelevant nonzero constant normalization is omitted. The functional equation is

\[
\boxed{
\xi_K(s)=\xi_K(1-s).
}
\]

Because `zeta_K(s)=zeta(s)L(s,chi_12)`, the nontrivial zeros of `xi_K` are exactly the combined nontrivial zeros of the principal and discriminant-12 quadratic channels, with multiplicity.

## 2. Critical-line centering

Set

\[
\boxed{
\Xi_K(z):=\xi_K(1/2+z).
}
\]

The functional equation gives

\[
\boxed{
\Xi_K(-z)=\Xi_K(z).
}
\]

Thus `Xi_K` is an even entire function. Its logarithmic derivative

\[
\boxed{
F_K(z):=\frac{\Xi_K'(z)}{\Xi_K(z)}
=\frac{\xi_K'}{\xi_K}(1/2+z)
}
\]

is odd:

\[
F_K(-z)=-F_K(z).
\]

Consequently the quotient

\[
\boxed{
H_K(w):=\frac{F_K(\sqrt w)}{\sqrt w}
}
\]

is naturally a meromorphic function of the squared coordinate

\[
w=z^2.
\]

The apparent square-root ambiguity cancels because `F_K` is odd.

## 3. Explicit arithmetic-plus-archimedean formula

From the definition of `xi_K`,

\[
\frac{\xi_K'}{\xi_K}(s)
=
\frac1s+\frac1{s-1}
+\frac12\log12-\log\pi
+\psi(s/2)
+\frac{\zeta_K'}{\zeta_K}(s),
\]

where `psi=Gamma'/Gamma`.

Using v13.262's positive-measure transform

\[
M_K(z):=-\frac{\zeta_K'}{\zeta_K}(1/2+z),
\]

we obtain, in the half-plane of absolute Euler-product convergence,

\[
\boxed{
F_K(z)
=
\frac1{1/2+z}+\frac1{-1/2+z}
+\frac12\log12-\log\pi
+\psi(1/4+z/2)
-M_K(z).
}
\]

This identity is exact wherever both sides are represented by the indicated convergent expressions and elsewhere by meromorphic continuation.

It makes precise what completion does: the positive prime Laplace transform is only one term in an odd meromorphic spectral function after the rational and gamma contributions are inserted.

## 4. Why the naive Pick route fails

From v13.262,

\[
M_K(z)=\int_0^\infty e^{-zu}\,d\mu_K(u),\qquad \mu_K\ge0,
\]

for `Re z>1/2`. For real `x>1/2`, this gives complete monotonicity.

But for `z=x+iy`,

\[
\Re M_K(z)
=
\int_0^\infty e^{-xu}\cos(yu)\,d\mu_K(u),
\]

which has no general fixed sign. Likewise the imaginary part contains `-sin(yu)` and has no general Pick/Herglotz sign.

Therefore

\[
\boxed{
\mu_K\ge0
\not\Rightarrow
M_K\text{ is Stieltjes/Pick/Herglotz in }z.
}
\]

This closes one tempting but invalid shortcut.

## 5. The squared spectral coordinate

Because `Xi_K` is even, its nonzero zeros occur in pairs

\[
\pm\alpha_j.
\]

The generalized Riemann hypothesis for `zeta_K` is exactly

\[
\boxed{
\Re\rho=1/2
\quad\text{for every nontrivial zero }\rho
}
\]

or, in centered coordinates,

\[
\boxed{
\alpha_j\in i\mathbf R.
}
\]

Thus under GRH we may write

\[
\alpha_j=\pm i\gamma_j,\qquad \gamma_j>0,
\]

with multiplicities `m_j`.

Squaring sends the critical line to the negative real axis:

\[
\boxed{
\alpha_j^2=-\gamma_j^2\le0.
}
\]

This is the geometric reason the Stieltjes variable is `w=z^2`, not `z`.

## 6. Logarithmic derivative under GRH

The even Hadamard product may be grouped by the symmetric zero pairs. Differentiating the paired factors gives, in the standard locally uniformly convergent paired sense,

\[
\boxed{
F_K(z)
=
\sum_j \frac{2m_j z}{z^2+\gamma_j^2}
}
\]

under GRH, with the usual canonical-product interpretation of the sum.

Therefore

\[
\boxed{
H_K(w)
=
\frac{F_K(\sqrt w)}{\sqrt w}
=
\sum_j\frac{2m_j}{w+\gamma_j^2}.
}
\]

This is a discrete Stieltjes transform:

\[
\boxed{
H_K(w)
=
\int_{[0,\infty)}\frac{d\nu_K(t)}{w+t},
}
\]

with positive spectral measure

\[
\boxed{
\nu_K
=2\sum_jm_j\,\delta_{\gamma_j^2}\ge0.
}
\]

The measure is the squared-height counting measure of the nontrivial zeros.

## 7. Stieltjes sign and complete monotonicity

For real `w>0`, the representation immediately gives

\[
H_K(w)>0
\]

and

\[
\boxed{
(-1)^n H_K^{(n)}(w)
=n!\int_0^\infty\frac{d\nu_K(t)}{(w+t)^{n+1}}
\ge0.
}
\]

Thus GRH implies complete monotonicity of `H_K` in the squared centered variable.

Moreover, for `Im w>0`,

\[
\Im\frac1{w+t}<0,
\]

so

\[
\boxed{
\Im H_K(w)\le0
\qquad(\Im w>0).
}
\]

Hence `-H_K` is a Herglotz/Pick function on the upper half-plane (away from boundary poles), while `H_K` is the conventional Stieltjes-sign version.

This is the exact Pick/Herglotz structure sought at the end of v13.262.

## 8. Converse: the Stieltjes pole geometry forces GRH

The converse is equally important.

Suppose the actual meromorphic function

\[
H_K(w)=F_K(\sqrt w)/\sqrt w
\]

admits a Stieltjes representation with positive measure supported on `[0,infinity)`, with no additional non-Stieltjes poles.

A Stieltjes transform can have singularities only on the nonpositive real `w` axis. But every nontrivial zero

\[
\rho=1/2+\alpha
\]

of `xi_K` produces a pole of `F_K(z)` at `z=alpha`, and hence a pole of `H_K(w)` at

\[
\boxed{w=\alpha^2.}
\]

Therefore every `alpha^2` must lie on the nonpositive real axis.

If `alpha=a+ib`, then

\[
\alpha^2=(a^2-b^2)+2abi.
\]

For a nontrivial zero, `alpha` cannot be a nonzero real number in `( -1/2,1/2 )`: `zeta_K(s)` has no real zeros in `0<s<1` for this factorization (`zeta(s)<0` there while the real primitive `L(s,chi_12)` has no zero producing an allowed uncancelled real nontrivial xi zero; equivalently the standard Dedekind nontrivial-zero set is treated with its known real-zero caveat). To avoid building the converse on that side issue, impose directly the exact spectral support condition that poles of `H_K` lie at `w=-t` with `t>0`.

Then `alpha^2<0`, hence

\[
\boxed{\alpha\in i\mathbf R.}
\]

Thus every nontrivial zero lies on `Re s=1/2`.

Accordingly, with the pole-support condition stated explicitly,

\[
\boxed{
\text{GRH for }\zeta_K
\iff
H_K(w)\text{ is the positive discrete Stieltjes transform of its pole measure on }(-\infty,0).
}
\]

This is a reformulation, not a proof of GRH.

## 9. Residues encode multiplicity positively

If `rho=1/2+i gamma` is a zero of multiplicity `m`, then `F_K(z)` has residue `m` at `z=i gamma` and `m` at `z=-i gamma`.

The corresponding term in `H_K` is

\[
\frac{2m}{w+\gamma^2}.
\]

Hence

\[
\boxed{
\operatorname*{Res}_{w=-\gamma^2}H_K(w)=2m>0.
}
\]

So the Stieltjes positivity condition is not merely a statement about where the poles lie. It also packages the zero multiplicities as positive spectral masses.

## 10. Two positive measures, on opposite sides of the explicit formula

The D12 branch now contains two exact positive measures.

### Arithmetic measure

From v13.262,

\[
\boxed{
\mu_K
=\sum_{n\ge1}\frac{\Lambda(n)(1+\chi_{12}(n))}{\sqrt n}\,\delta_{\log n}
\ge0.
}
\]

It gives

\[
M_K(z)=\int e^{-zu}\,d\mu_K(u)
\]

in the Euler-product half-plane.

### Spectral measure under GRH

The centered completed function gives

\[
\boxed{
\nu_K
=2\sum_jm_j\delta_{\gamma_j^2}
\ge0,
}
\]

and

\[
H_K(w)=\int\frac{d\nu_K(t)}{w+t}.
\]

Thus the explicit formula may be viewed as mediating between

\[
\boxed{
\text{positive arithmetic measure on log prime powers}
\longleftrightarrow
\text{positive spectral measure on squared zero heights}.
}
\]

The first positivity is unconditional. The second positivity with support on `[0,infinity)` is equivalent to the critical-line statement.

This sharply identifies the remaining gap.

## 11. D12-specific factorization of the spectral measure

Since

\[
\zeta_K(s)=\zeta(s)L(s,\chi_{12}),
\]

we have, after compatible completion,

\[
\xi_K(s)=C\,\xi_0(s)\xi_{12}(s)
\]

for a nonzero constant `C`, with the understood primitive completed factors.

Therefore

\[
F_K(z)=F_0(z)+F_{12}(z).
\]

Under RH for `zeta` and GRH for `L(s,chi_12)`, the Stieltjes measure decomposes additively:

\[
\boxed{
\nu_K=\nu_0+\nu_{12}.
}
\]

This is the spectral counterpart of v13.258's screw additivity and v13.262's field-sector compression.

The important guardrail remains: positivity of the combined measure does not by itself separate the two factors unless one uses the actual pole divisor/multiplicities. The field GRH is equivalent to both factors having their nontrivial zeros on the critical line because the product has the union of their zero divisors.

## 12. Connection to the split/inert self-sector

From v13.262,

\[
Q_K=2Q_{SS}=2Q_{II}.
\]

The new spectral transform is attached to exactly this scalar field object:

\[
Q_K
\longleftrightarrow
\Xi_K
\longleftrightarrow
F_K(z)
\longleftrightarrow
H_K(z^2).
\]

Therefore either D12 residue self-sector carries the same candidate Stieltjes spectral law.

The off-diagonal split/inert defect `Q_Delta` is not needed to state the field GRH criterion.

This is a useful compression:

\[
\boxed{
\text{one D12 diagonal residue sector}
\longrightarrow
\text{one even completed entire function}
\longrightarrow
\text{one Stieltjes pole problem in }w=z^2.
}
\]

## 13. Relation to Suzuki's screw-function framework

Suzuki's 2026 paper develops a continuous-kernel realization of Weil's quadratic form through the screw function, without assuming RH. The present entry does not claim that Suzuki proves the Stieltjes criterion above.

The connection is structural:

1. the audited D12 screw function produces the same completed field object `xi_K`;
2. Suzuki turns the Weil distributional form into a continuous-kernel/operator problem;
3. centering the same completed field object at `1/2` makes it even;
4. squaring the centered spectral coordinate converts the GRH critical line into the Stieltjes cut `(-infinity,0]`.

Thus the Stieltjes transform supplies a clean spectral target for any future operator constructed from the D12 screw kernel.

## 14. Strongest exact equivalence obtained here

Define

\[
\boxed{
\mathcal S_K(w)
:=
\frac1{\sqrt w}
\frac{\xi_K'}{\xi_K}(1/2+\sqrt w).
}
\]

Then, with the canonical paired-zero interpretation and explicit pole-support condition,

\[
\boxed{
\mathrm{GRH}(\zeta_K)
\iff
\mathcal S_K(w)
=
\int_{[0,\infty)}\frac{d\nu_K(t)}{w+t},
\qquad \nu_K\ge0,
}
\]

where

\[
\nu_K=2\sum_jm_j\delta_{\gamma_j^2}.
\]

Equivalently, GRH is the statement that the centered completed logarithmic derivative, divided by the centered coordinate, is a positive Stieltjes transform after the map `w=z^2`.

This is not a new proof of GRH. It is an exact spectral reformulation adapted to the D12/Suzuki operator framework.

## 15. Guardrails

1. **No RH/GRH proof is claimed.**
2. Complete monotonicity of the prime-side Laplace transform `M_K(x)` does not imply a Pick/Herglotz property in complex `z`.
3. The Stieltjes structure arises on the spectral side only after completion, centering, and squaring.
4. Canonical-product sums are understood in their standard paired/locally-uniformly-convergent sense; naive absolute convergence of every displayed zero sum is not asserted.
5. The converse uses the full meromorphic pole set of the actual completed logarithmic derivative, not merely positivity of finitely many derivatives on the positive real axis.
6. A finite list of complete-monotonicity inequalities is only a necessary numerical test, not an RH criterion.
7. The archimedean/pole terms remain essential in the exact formula for `F_K`; the prime measure alone does not determine the Stieltjes property.
8. The Stieltjes equivalence is a repackaging of critical-line zero geometry into the squared coordinate, not independent evidence that the zeros satisfy it.

## 16. Next high-value target

The key question is now concrete and operator-theoretic.

Can the D12 Suzuki kernel produce `mathcal S_K` as a Weyl/Titchmarsh, resolvent, or compressed-resolvent function of a self-adjoint operator?

For a self-adjoint operator `A` and vector `v`, a resolvent matrix element has the positive-measure form

\[
\langle v,(A+w)^{-1}v\rangle
=
\int\frac{d\sigma_v(t)}{w+t}
\]

when the relevant spectral support is nonnegative.

Therefore the exact GRH target can be stated as:

\[
\boxed{
\mathcal S_K(w)
\stackrel{?}{=}
\langle v,(A_K+w)^{-1}v\rangle,
\qquad A_K\ge0,
}
\]

for an operator `A_K` constructed intrinsically from the D12/Suzuki self-sector.

If such an identity were established unconditionally with `A_K` self-adjoint and nonnegative, the Stieltjes property — and hence the critical-line pole geometry — would follow. Establishing that identity is precisely the hard missing step, so it must not be assumed.

This is now the shortest operator target:

\[
\boxed{
\text{D12 positive arithmetic self-sector}
\to
\text{Suzuki continuous kernel}
\to
\text{positive self-adjoint resolvent?}
\to
\text{Stieltjes spectral law}.
}

That is the next research frontier.