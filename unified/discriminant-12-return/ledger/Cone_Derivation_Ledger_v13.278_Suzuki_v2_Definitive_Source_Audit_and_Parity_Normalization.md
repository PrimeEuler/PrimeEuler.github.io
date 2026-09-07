# Cone Derivation Ledger v13.278 — Suzuki v2 Definitive Source Audit and D12 Parity Normalization

Date: 2026-09-06

Status: DEFINITIVE SOURCE CORRECTION + EXACT PARITY REDUCTION + NECESSARY NORMALIZATION LAW — GRH NOT PROVED

## 0. Synchronization and external audit reconciliation

Immediately before this write, the authoritative project README and current `master` tip were re-fetched. The tip was

`278b4b95c1c77176907ca1271f8c3d59be48f3e1`,

whose new checkpoint is `v13.277 — External Audit Round 11`.

That audit independently verified the mathematics in v13.272–v13.276, but explicitly left unresolved which of the two competing formulas had actually appeared in Suzuki's current arXiv v2 Corollary 1.6.

This entry resolves that ambiguity directly from the current arXiv HTML for

Masatoshi Suzuki, “Weil's quadratic form via the screw function,” arXiv:2606.09096v2, 17 Aug 2026.

The current source states at Corollary 1.6, equation (1.12):

\[
\boxed{
\lim_{a\to\infty}e^{\phi(a,z)}W(a,\theta;z)
=
\frac{\xi(1/2-iz)}{\xi(1/2-iz)+\xi'(1/2-iz)}
}
\]

uniformly on compact subsets, for a suitable choice of `theta(a)` and `phi(a,z)`.

Therefore:

- **v13.274 had the current v2 formula correct**;
- **v13.276's attempted source correction to `z^2 xi/xi'` was incorrect**;
- the finite-form mathematics of v13.276 remains unaffected, exactly as external audit round 11 observed;
- all future Suzuki-v2 asymptotic work in this project must use `xi/(xi+xi')` unless the source itself changes again.

Suzuki also states immediately after (1.12) that `theta=pi` is plausibly the most natural choice, but does not pursue the question there.

---

## 1. Source-established finite characteristic function

Suzuki's Theorem 1.5 gives, for normalized deficiency vectors `v_+`, `v_-`,

\[
W(a,\theta;z)
=(z-i)\int_{-a}^a v_+(a,x)e^{izx}\,dx
+e^{i\theta}(z+i)\int_{-a}^a v_-(a,x)e^{izx}\,dx.
\]

Its zeros are exactly the eigenvalues of the self-adjoint extension `Dbar_{a,theta}`, hence all zeros are real.

For the D12 transfer, write the analogous object as

\[
W_K(a,\theta;z).
\]

The exact D12 finite-form closure from v13.276 and the transfer mechanism of v13.275 put this finite characteristic function on the same abstract footing, without asserting the infinite-volume convergence.

---

## 2. Reflection symmetry of the D12 finite operator

The D12 screw kernel is real and even in the difference variable. The interval `(-a,a)` is reflection symmetric. Define

\[
(Rf)(x)=f(-x).
\]

Every component of the D12 finite form commutes with reflection:

1. the pole/normalization contribution is even;
2. the doubled real gamma contribution is even;
3. the conductor contribution `(log 12)I` is scalar;
4. the prime-power operator occurs in symmetric pairs
   \[
   S_{a,v}+S_{a,v}^*,
   \]
   which are interchanged by reflection.

Hence

\[
\boxed{RA_{K,a}=A_{K,a}R}
\]

and therefore, for any real `lambda<lambda_{K,a}`,

\[
\boxed{RT_{K,a}=T_{K,a}R},
\qquad T_{K,a}=A_{K,a}-\lambda I.
\]

The deficiency equations are

\[
T_{K,a}v_+=e^x,
\qquad
T_{K,a}v_-=e^{-x}.
\]

Since `Re^x=e^{-x}` and `T_{K,a}` commutes with `R`, uniqueness gives

\[
\boxed{v_-=Rv_+}
\]

once the two deficiency vectors are given the same normalization.

This is exact and does not require GRH.

---

## 3. One-function reduction of the characteristic function

Define

\[
F_a(z):=\int_{-a}^{a}v_+(a,x)e^{izx}\,dx.
\]

Using `v_-(x)=v_+(-x)`, substitution `x -> -x` gives

\[
\int_{-a}^{a}v_-(a,x)e^{izx}\,dx=F_a(-z).
\]

Thus the full one-parameter characteristic family reduces to

\[
\boxed{
W_K(a,\theta;z)
=(z-i)F_a(z)+e^{i\theta}(z+i)F_a(-z).
}
\]

The two parity-fixed extensions are immediate.

For `theta=0`,

\[
W_K(a,0;z)
=(z-i)F_a(z)+(z+i)F_a(-z),
\]

so

\[
\boxed{W_K(a,0;-z)=-W_K(a,0;z).}
\]

For `theta=pi`,

\[
W_K(a,\pi;z)
=(z-i)F_a(z)-(z+i)F_a(-z),
\]

so

\[
\boxed{W_K(a,\pi;-z)=W_K(a,\pi;z).}
\]

Therefore Suzuki's suggested `theta=pi` is precisely the even finite characteristic sector for the D12 reflection-symmetric problem.

---

## 4. The current Suzuki target in centered coordinates

Define the centered completed D12 function

\[
\Xi_K(z):=\xi_K(1/2-iz).
\]

The functional equation gives

\[
\boxed{\Xi_K(-z)=\Xi_K(z).}
\]

Differentiating,

\[
\Xi_K'(z)=-i\xi_K'(1/2-iz),
\]

hence

\[
\xi_K'(1/2-iz)=i\Xi_K'(z).
\]

The Suzuki-faithful D12 target is therefore

\[
\boxed{
R_K(z)
:=
\frac{\Xi_K(z)}{\Xi_K(z)+i\Xi_K'(z)}.
}
\]

Because `Xi_K` is even and `Xi_K'` is odd,

\[
R_K(-z)
=
\frac{\Xi_K(z)}{\Xi_K(z)-i\Xi_K'(z)}.
\]

Thus the target itself is generically **not even**.

This is important: choosing the natural finite extension `theta=pi` makes `W_K` even, so the entire asymmetry of the Suzuki target must be carried by the normalization factor `exp(phi_K)`.

---

## 5. Exact necessary odd normalization law

Suppose the Suzuki-type convergence holds in the `theta=pi` sector:

\[
e^{\phi_{K,a}(z)}W_K(a,\pi;z)
\longrightarrow R_K(z)
\]

locally uniformly away from poles of the target, or equivalently in a meromorphic formulation on compacta.

Since

\[
W_K(a,\pi;-z)=W_K(a,\pi;z),
\]

taking the ratio at `z` and `-z` forces

\[
\boxed{
\lim_{a\to\infty}
\exp\{\phi_{K,a}(z)-\phi_{K,a}(-z)\}
=
\frac{R_K(z)}{R_K(-z)}.
}
\]

The right side is explicit:

\[
\boxed{
\frac{R_K(z)}{R_K(-z)}
=
\frac{\Xi_K(z)-i\Xi_K'(z)}
     {\Xi_K(z)+i\Xi_K'(z)}.
}
\]

Therefore the odd part of the normalization is not arbitrary. Locally, after a branch of the logarithm is chosen,

\[
\phi_{K,a}^{\rm odd}(z)
:=\frac12\bigl(\phi_{K,a}(z)-\phi_{K,a}(-z)\bigr)
\]

must satisfy asymptotically

\[
\boxed{
\phi_{K,a}^{\rm odd}(z)
\longrightarrow
\frac12\log
\frac{\Xi_K(z)-i\Xi_K'(z)}
     {\Xi_K(z)+i\Xi_K'(z)}
}
\]

modulo the usual local logarithmic branch ambiguity.

This is a new exact necessary condition on Suzuki's previously-unspecified normalization.

---

## 6. Parity product removes the odd normalization

Multiplying the target at `z` and `-z` gives

\[
R_K(z)R_K(-z)
=
\frac{\Xi_K(z)^2}
{(\Xi_K+i\Xi_K')(\Xi_K-i\Xi_K')}.
\]

Hence

\[
\boxed{
R_K(z)R_K(-z)
=
\frac{\Xi_K(z)^2}
     {\Xi_K(z)^2+\Xi_K'(z)^2}.
}
\]

This object is even.

Likewise, in the `theta=pi` finite sector,

\[
W_K(a,\pi;z)W_K(a,\pi;-z)=W_K(a,\pi;z)^2.
\]

Thus the parity-symmetrized convergence target becomes

\[
\boxed{
e^{\phi_{K,a}(z)+\phi_{K,a}(-z)}
W_K(a,\pi;z)^2
\longrightarrow
\frac{\Xi_K(z)^2}
     {\Xi_K(z)^2+\Xi_K'(z)^2}.
}
\]

Only the **even** part of `phi_K` remains in this equation.

This cleanly separates Suzuki's unknown normalization into two pieces:

- the odd part is forced by the explicit ratio in Section 5;
- only the even part remains genuinely free to absorb finite-volume growth/normalization.

That is a substantial reduction of the asymptotic normalization problem.

---

## 7. Relation to the project's squared-coordinate branch

Earlier project work introduced the even characteristic

\[
\Psi_K(w)=\Xi_K(\sqrt w).
\]

The present parity reduction explains why squared coordinates arose naturally even though Suzuki's current v2 target itself is not even: the `theta=pi` finite characteristic is even, and parity symmetrization of Suzuki's target produces an even function.

This does **not** identify Suzuki's target with the earlier Stieltjes characteristic. They remain different functions. But it gives a precise bridge:

\[
\boxed{
\text{Suzuki finite even sector}
\quad\longleftrightarrow\quad
\text{parity-symmetrized arithmetic target}.
}
\]

Writing `w=z^2`, the symmetrized target can be viewed as a meromorphic function of `w`.

No claim is made here that its poles or zeros directly yield the Stieltjes criterion of v13.263–v13.269.

---

## 8. What this changes in the research frontier

The source ambiguity is now resolved directly from current arXiv v2.

The finite D12 operator remains valid from v13.275–v13.276, but the correct Suzuki-v2 infinite target is

\[
\boxed{
\frac{\xi_K}{\xi_K+\xi_K'}
}
\]

in the centered `1/2-iz` variable, not `z^2 xi_K/xi_K'`.

Reflection symmetry then yields an exact one-function representation

\[
\boxed{
W_K(a,\theta;z)
=(z-i)F_a(z)+e^{i\theta}(z+i)F_a(-z),
}
\]

and singles out

\[
\boxed{\theta=\pi}
\]

as the even extension.

Most importantly, if the natural `theta=pi` choice is used, the odd part of Suzuki's normalization is forced asymptotically:

\[
\boxed{
2\phi^{\rm odd}_K(z)
\sim
\log
\frac{\Xi_K-i\Xi_K'}{\Xi_K+i\Xi_K'}.
}
\]

Therefore the remaining normalization problem is only the even part.

---

## 9. Next target

The next calculation should stay with Suzuki's actual Section 7 mechanism and ask whether its de Branges/infinite-volume heuristic determines the even normalization.

Concretely:

1. rewrite Suzuki's Section 7 boundary characteristic in the reflection basis;
2. isolate the `theta=pi` even characteristic;
3. factor out the forced odd normalization derived above;
4. compare the remaining even normalization against the D12 completed gamma/conductor asymptotics;
5. test whether the parity product
   \[
   \Xi_K^2/(\Xi_K^2+\Xi_K'^2)
   \]
   admits a cleaner finite-interval Fredholm or de Branges representation than the unsymmetrized target.

The key advance of this checkpoint is that `phi_K(a,z)` is no longer a completely free unknown: half of it, its odd part, is determined by parity if Suzuki's natural `theta=pi` extension is adopted.
