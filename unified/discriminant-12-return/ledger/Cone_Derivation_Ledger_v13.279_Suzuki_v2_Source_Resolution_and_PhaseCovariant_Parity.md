# Cone Derivation Ledger v13.279 — Suzuki v2 Source Resolution and Phase-Covariant Parity

Date: 2026-09-06

Status: DEFINITIVE SOURCE RESOLUTION + PHASE-COVARIANT PARITY CORRECTION + SHARP NORMALIZATION CONSTRAINT — GRH NOT PROVED

## 0. Synchronization and correction of v13.278

Immediately before this write, the authoritative README and current `master` tip were re-fetched. The tip remained

`63ed0fc2a3154006264f048f8807ef7ed0e57b23`,

with v13.278 the highest checkpoint and no newer external-audit entry present.

A fresh direct check of the current arXiv v2 source of Masatoshi Suzuki, “Weil's quadratic form via the screw function,” arXiv:2606.09096v2, revised 17 Aug 2026, resolves the citation dispute conclusively.

The current source states in Corollary 1.6, equation (1.12),

\[
\boxed{
\lim_{a\to\infty}e^{\phi(a,z)}W(a,\theta;z)
=
z^2\frac{\xi(1/2-iz)}{\xi'(1/2-iz)}
}
\]

uniformly on every compact subset of `C`, provided suitable `theta(a)` and `phi(a,z)` can be chosen.

The source further says that the exponential factor is included to allow possible normalization, and that it is plausible no such correction is actually needed.

Therefore:

- v13.276 had the current Suzuki-v2 target correct;
- v13.278's claim that the target is `xi/(xi+xi')` is incorrect and is superseded here;
- all finite-interval mathematics in v13.274–v13.278 that does not depend on the infinite-volume target remains intact;
- all future Suzuki-v2 asymptotic work must use `z^2 xi/xi'` unless Suzuki revises the source again.

This is the citation state to use going forward.

---

## 1. Source-established Section 7 structure

Suzuki's Section 7 is explicitly heuristic and proceeds under RH / positivity of the infinite-volume Weil form.

The key source-established ingredients are:

1. the infinite-volume Weil energy space `H(A_infty)`;
2. an isometric isomorphism
   \[
   U:\mathcal H(A_\infty)\to\mathcal B
   \]
   with a de Branges space `B`;
3. the multiplication operator `M` on `B`, with deficiency indices `(1,1)`;
4. a self-adjoint extension `M_{pi/2}` whose spectrum is the set `Gamma` of ordinates of the nontrivial zeros of `xi(1/2-iz)`;
5. the finite operators `Dbar_{a,theta}` are heuristically expected to approximate the corresponding infinite self-adjoint operator as `a->infty`;
6. the characteristic function `W(a,theta;z)` is therefore expected, up to normalization, to approach the reciprocal logarithmic derivative target in Corollary 1.6.

Suzuki explicitly emphasizes that the finite-zero reality theorem is unconditional, whereas the Section 7 infinite-volume identification is heuristic and formulated under positivity/RH.

For D12 we therefore keep the exact same separation:

\[
\boxed{
\text{finite D12 operator and real finite zeros: project theorem,}
}
\]

but

\[
\boxed{
\text{D12 infinite de Branges limit: open project extension.}
}
\]

---

## 2. Correct centered D12 Suzuki target

Define

\[
\Xi_K(z):=\xi_K(1/2-iz).
\]

The functional equation gives

\[
\Xi_K(-z)=\Xi_K(z),
\]

so `Xi_K` is even and `Xi_K'` is odd.

Differentiating,

\[
\Xi_K'(z)=-i\xi_K'(1/2-iz),
\]

hence

\[
\xi_K'(1/2-iz)=i\Xi_K'(z).
\]

Therefore the Suzuki-faithful D12 target is

\[
\boxed{
\mathcal R_K(z)
:=
z^2\frac{\xi_K(1/2-iz)}{\xi_K'(1/2-iz)}
=
-i z^2\frac{\Xi_K(z)}{\Xi_K'(z)}.
}
\]

Since `Xi_K` is even and `Xi_K'` is odd,

\[
\boxed{
\mathcal R_K(-z)=-\mathcal R_K(z).
}
\]

Thus the actual Suzuki target is an **odd meromorphic function** of the centered spectral variable.

Near `z=0`, if `Xi_K(0) != 0` and `Xi_K''(0) != 0`,

\[
\Xi_K'(z)=\Xi_K''(0)z+O(z^3),
\]

so

\[
\mathcal R_K(z)
=
-i\frac{\Xi_K(0)}{\Xi_K''(0)}z+O(z^3),
\]

which confirms the expected simple odd zero at the origin.

---

## 3. Reflection symmetry revisited with the missing phase

The exact reflection statement from v13.278 survives, but its normalization must be formulated phase-covariantly.

Let

\[
(Rf)(x)=f(-x).
\]

The D12 finite operator satisfies

\[
RA_{K,a}=A_{K,a}R,
\qquad
RT_{K,a}=T_{K,a}R.
\]

If

\[
T_{K,a}v_+=e^x,
\qquad
T_{K,a}v_-=e^{-x},
\]

then `Rv_+` solves the same deficiency equation as `v_-`.

Because the deficiency space is one-dimensional,

\[
\boxed{
v_-=e^{i\alpha_a}Rv_+
}
\]

for some phase `alpha_a`.

The equal-norm normalization in Suzuki's Theorem 1.5 fixes only the modulus of this constant, not its phase.

This corrects the stronger statement in v13.278 that one may simply write `v_-=Rv_+` without recording the phase convention.

---

## 4. Phase-covariant one-function reduction

Define

\[
F_a(z):=\int_{-a}^{a}v_+(a,x)e^{izx}\,dx.
\]

Then

\[
\int_{-a}^{a}v_-(a,x)e^{izx}\,dx
=
e^{i\alpha_a}F_a(-z).
\]

Hence Suzuki's characteristic function becomes

\[
\boxed{
W_K(a,\theta;z)
=
(z-i)F_a(z)
+
e^{i(\theta+\alpha_a)}(z+i)F_a(-z).
}
\]

Only the combination

\[
\boxed{
\Theta_a:=\theta+\alpha_a\pmod{2\pi}
}
\]

is relevant to the parity of the characteristic function.

This is the phase-covariant extension parameter.

If the deficiency bases are rephased, `theta` changes oppositely so that `Theta_a` is the invariant datum.

Therefore the statements “theta=0 is odd” and “theta=pi is even” are basis-dependent shorthand. The invariant statements are

\[
\boxed{
\Theta_a=0\ \Longrightarrow\ W_K(a,\theta;-z)=-W_K(a,\theta;z),
}
\]

and

\[
\boxed{
\Theta_a=\pi\ \Longrightarrow\ W_K(a,\theta;-z)=W_K(a,\theta;z).
}
\]

This is the correct parity theorem.

---

## 5. Immediate comparison with the actual Suzuki target

The actual target

\[
\mathcal R_K(z)=-iz^2\Xi_K(z)/\Xi_K'(z)
\]

is odd.

Therefore the parity-matched finite sector is

\[
\boxed{
\Theta_a=0.
}
\]

In this sector, the characteristic function is already odd, exactly like the limiting arithmetic target.

This yields an important diagnostic:

\[
\boxed{
\text{if }e^{\phi_{K,a}(z)}\to 1
\text{ locally uniformly, then the natural parity sector is }\Theta_a=0.
}
\]

This is directly compatible with Suzuki's remark that the exponential correction may be unnecessary.

Suzuki's separate suggestion that `theta=pi` may be natural must therefore be interpreted together with his specific deficiency-vector phase convention. It cannot be transferred to D12 as an invariant parity statement without first identifying the corresponding `alpha_a`.

In particular, it is possible that Suzuki's `theta=pi` convention corresponds to invariant `Theta_a=0` after the implicit phase of the chosen deficiency vectors is taken into account.

No contradiction with Suzuki is present; the lesson is that `theta` alone is not phase-invariant.

---

## 6. Normalization law in the parity-matched sector

Suppose

\[
\Theta_a=0
\]

and

\[
e^{\phi_{K,a}(z)}W_K(a,\theta;z)
\longrightarrow
\mathcal R_K(z)
\]

locally uniformly on compacta in a region where the target is holomorphic.

Both `W_K` and `R_K` are odd.

Taking the ratio at `z` and `-z` gives

\[
\frac{e^{\phi_{K,a}(z)}W_K(z)}
     {e^{\phi_{K,a}(-z)}W_K(-z)}
\to
\frac{\mathcal R_K(z)}{\mathcal R_K(-z)}=-1.
\]

Since `W_K(-z)=-W_K(z)`, the minus signs cancel and one obtains

\[
\boxed{
\exp\{\phi_{K,a}(z)-\phi_{K,a}(-z)\}
\longrightarrow 1.
}
\]

Thus in the parity-matched sector the odd part of the normalization must vanish asymptotically modulo integral multiples of `2 pi i`:

\[
\boxed{
\phi_{K,a}^{\rm odd}(z)\to 0
}
\]

locally, under any coherent branch choice and normal-family hypothesis.

This is much cleaner than the v13.278 normalization law because that law was based on the wrong source target.

The actual Suzuki target therefore supports Suzuki's own remark that perhaps no normalization is necessary: parity places no obstruction at all once the phase-covariant odd sector is chosen.

---

## 7. What happens in the even sector

If instead

\[
\Theta_a=\pi,
\]

then `W_K` is even while `R_K` is odd.

Any convergence

\[
e^{\phi_{K,a}}W_K\to\mathcal R_K
\]

must therefore force all parity change through the exponential normalization.

Formally, away from zeros,

\[
\exp\{\phi_{K,a}(z)-\phi_{K,a}(-z)\}
\to -1.
\]

But at `z=0`, for every finite `a`,

\[
\phi_{K,a}(0)-\phi_{K,a}(0)=0,
\]

so the left side equals `1` exactly.

Hence there is no locally uniform convergence of the normalization ratio to `-1` on a neighborhood containing `0`.

More invariantly, a locally bounded/normal family of zero-free exponential normalizations cannot convert a stable even finite characteristic into an odd limit with a simple zero at the origin without a singular degeneration of the normalization or of the finite characteristic values.

Thus:

\[
\boxed{
\Theta_a=\pi
\text{ is incompatible with a regular normalization tending to a finite nonzero analytic factor near }z=0.
}
\]

This does not rule out Suzuki's full conjecture because `theta(a)` and the deficiency-vector phases may vary with `a`, and `phi(a,z)` is not assumed to form a bounded normal family.

It does, however, give a strong selection principle for any D12 implementation that aims to realize Suzuki's suggestion that no normalization is needed.

---

## 8. Section 7 de Branges interpretation

Suzuki's Section 7 identifies, under RH, the infinite-volume Weil energy space with a de Branges space in which multiplication has a self-adjoint extension whose spectrum is the zero ordinate set.

The D12 analogue should therefore not begin by guessing an even normalization factor. Instead it should first align the finite self-adjoint extension with the phase convention of the infinite de Branges extension.

The correct object to compare is the extension phase, not the bare parameter `theta`:

\[
\boxed{
\Theta_a=\theta(a)+\alpha_a.
}
\]

The target parity shows that a normalization-free limit would require

\[
\boxed{
\Theta_a\to 0\pmod{2\pi}.
}
\]

This is the first concrete asymptotic boundary-condition prediction produced by the D12 transfer of Suzuki's Section 7 heuristic.

It is independent of the scale normalization of `W_K`.

---

## 9. Relation to the squared-coordinate branch

The corrected Suzuki target is odd:

\[
\mathcal R_K(z)=-iz^2\Xi_K(z)/\Xi_K'(z).
\]

Dividing by `z` gives an even meromorphic function:

\[
\boxed{
\frac{\mathcal R_K(z)}{z}
=
-i z\frac{\Xi_K(z)}{\Xi_K'(z)}.
}
\]

Therefore there exists a meromorphic function `H_K(w)` such that

\[
\boxed{
\mathcal R_K(z)=z H_K(z^2).
}
\]

This is the correct parity bridge from Suzuki's first-order characteristic to the squared variable `w=z^2`.

It is distinct from the Stieltjes function

\[
\mathcal S_K(w)
=
\frac1{\sqrt w}
\frac{\xi_K'}{\xi_K}
\left(\frac12+\sqrt w\right),
\]

but the two are reciprocal-log-derivative companions.

Formally, in centered coordinates,

\[
H_K(z^2)
=-iz\frac{\Xi_K}{\Xi_K'}.
\]

Thus the Suzuki branch and the squared-resolvent branch are not competing constructions: they encode reciprocal first-order versus second-order characteristic data.

---

## 10. Current exact/open boundary

### Exact / source-established or derived

1. Current Suzuki v2 Corollary 1.6 target is `z^2 xi/xi'`.
2. The finite characteristic `W(a,theta;z)` has only real zeros.
3. The D12 finite operator is reflection symmetric.
4. Deficiency vectors satisfy `v_- = e^{i alpha_a} R v_+`.
5. The phase-covariant parameter is `Theta_a=theta+alpha_a`.
6. `Theta_a=0` gives an odd characteristic; `Theta_a=pi` gives an even characteristic.
7. The actual Suzuki D12 target is odd.
8. Therefore a normalization-free or regular-normalization limit selects the odd finite sector `Theta_a -> 0`.
9. In that sector the odd part of `phi_K` asymptotically vanishes rather than being forced to a nontrivial arithmetic expression.

### Open

1. Construct the D12 infinite-volume de Branges space unconditionally or under a clearly stated GRH hypothesis.
2. Identify the phase convention corresponding to Suzuki's `M_{pi/2}` extension in the finite D12 basis.
3. Prove `Theta_a -> 0` or determine the actual asymptotic extension phase.
4. Control `lambda_{K,a}` as `a->infty`.
5. Determine whether `phi_K` can be taken identically zero.
6. Prove any compact-uniform convergence of `W_K` to the Suzuki target.
7. GRH.

---

## 11. Next target

The highest-value next calculation is now the finite/infinite extension-phase comparison:

\[
\boxed{
\text{identify Suzuki's infinite }M_{\pi/2}\text{ boundary phase in the finite deficiency basis.}
}
\]

Concretely:

1. extract Suzuki's exact von-Neumann parameterization of `Dbar_{a,theta}` from Section 6;
2. track how reflection maps the normalized deficiency basis;
3. express the boundary Lagrangian condition in the phase-invariant variable `Theta_a`;
4. compare with the de Branges extension `M_{pi/2}` in Section 7;
5. determine whether the heuristic limit predicts `Theta_a -> 0` exactly.

This is now more informative than guessing the even part of `phi_K`, because the corrected Suzuki source shows that the first-order target already has the same odd parity as the phase-matched finite characteristic.