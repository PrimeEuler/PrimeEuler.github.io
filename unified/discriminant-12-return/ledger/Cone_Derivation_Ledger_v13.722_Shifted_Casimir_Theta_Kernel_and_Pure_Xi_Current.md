# Cone Derivation Ledger v13.722 — Shifted Casimir on the Theta Kernel and the Pure Xi Current

Date: 2026-09-23

Status: exact Xi/Zeta cone-lane continuation. This entry tests the observed quadratic correspondence
\[
w^2-\frac14=s(s-1)=j(j+1)\quad\text{under }w=j+\frac12
\]
at the operator level. It proves that the differential shifted-Casimir operator
\[
\mathscr C_r=D_r^2-\frac14
\]
acts directly on the folded full-line theta kernel of v13.717, with an exact origin contact term, and that removal of that contact term yields the classical pure positive even Xi kernel.

Status labels: **[D]** exact derived, **[O]** open, **[G]** guardrail.

## 0. Synchronization and collision check

Immediately before this write, the live repository head was v13.721 / Suzuki Transport Multiplier and Conditional Xi Identification at commit \`4893fd403a416545db8181c0e7ac2cc05fe464a8\`. The intended v13.722 filename was absent. No collision was present.

The Suzuki lane has therefore advanced independently through v13.718–721. The present entry is in the Xi/Zeta/Casimir lane and does not alter v13.721's conditional status for the source-faithful Suzuki–Xi identification.

## 1. Starting theta representation [D]

Let
\[
\psi(x)=\sum_{n\ge1}e^{-\pi n^2x},
\]
and define
\[
f(r)=e^{r/2}\psi(e^{2r}),\qquad r\ge0.
\]

The full-line folded theta kernel from v13.717 is
\[
\boxed{
K_\theta(r)=f(|r|)
=
e^{|r|/2}\psi(e^{2|r|}).
}
\]

Its bilateral transform is
\[
I_\theta(w)
=
\int_{\mathbb R}K_\theta(r)e^{wr}\,dr.
\]

v13.717 proved
\[
\boxed{
\Xi(w):=\xi\!\left(\frac12+w\right)
=
\frac12+
\left(w^2-\frac14\right)I_\theta(w).
}
\]

Because \(K_\theta\) decays super-exponentially, the transform is entire and all integrations by parts below have no boundary contribution at \(r=\pm\infty\).

## 2. Shifted-Casimir spectral polynomial [D]

Define
\[
\boxed{
\mathscr C_r=D_r^2-\frac14.
}
\]

For the exponential generalized eigenfunction,
\[
\boxed{
\mathscr C_r e^{wr}
=
\left(w^2-\frac14\right)e^{wr}.
}
\]

Under
\[
w=j+\frac12,
\]
the eigenvalue becomes
\[
\boxed{
w^2-\frac14=j(j+1),
}
\]
the standard rank-one shifted \(\mathfrak{sl}_2\)/\(SU(2)\) Casimir polynomial.

Also
\[
w=s-\frac12
\]
gives
\[
\boxed{
w^2-\frac14=s(s-1).
}
\]

Thus the same Weyl-invariant quadratic occurs exactly in the Xi completion and in the shifted rank-one Casimir character.

[G] This polynomial/operator correspondence does not by itself identify the Xi theta representation with an actual \(SU(2)\), \(SU(1,1)\), or \(\mathfrak{sl}_2\) representation, nor does it make Xi a Casimir spectral determinant.

## 3. Origin regularity and Jacobi fixed-point identity [D]

The folded kernel is continuous at the origin:
\[
K_\theta(0)=f(0)=\psi(1).
\]

For \(r>0\),
\[
f'(r)
=
\frac12e^{r/2}\psi(e^{2r})
+
2e^{5r/2}\psi'(e^{2r}),
\]
so
\[
f'(0)
=
\frac12\psi(1)+2\psi'(1).
\]

Write
\[
\vartheta(x)=1+2\psi(x).
\]

Jacobi inversion
\[
\vartheta(x)=x^{-1/2}\vartheta(1/x)
\]
differentiated at its fixed point \(x=1\) gives
\[
\boxed{
\vartheta'(1)=-\frac14\vartheta(1).
}
\]

Hence
\[
\psi(1)=\frac{\vartheta(1)-1}{2},
\qquad
\psi'(1)=-\frac18\vartheta(1),
\]
and therefore
\[
\boxed{
f'(0)=-\frac14.
}
\]

Since
\[
K_\theta(r)=f(|r|),
\]
we have
\[
\boxed{
K_\theta'(0+)=-\frac14,
\qquad
K_\theta'(0-)=+\frac14.
}
\]

Thus the derivative jump is
\[
\boxed{
[K_\theta']_0=-\frac12.
}
\]

The kernel is therefore continuous but not \(C^1\) at \(r=0\).

## 4. Distributional shifted-Casimir action [D]

For a continuous piecewise-\(C^2\) function whose first derivative jumps at the origin,
\[
D_r^2K
=
K''_{\rm reg}
+
[K']_0\delta_0.
\]

Therefore
\[
\boxed{
D_r^2K_\theta
=
f''(|r|)
-\frac12\delta_0.
}
\]

Define the regular even function
\[
\boxed{
\Phi(r)
=
f''(|r|)-\frac14f(|r|).
}
\]

Then the exact distributional identity is
\[
\boxed{
\left(D_r^2-\frac14\right)K_\theta
=
\Phi-\frac12\delta_0.
}
\]

The only boundary/contact contribution is at \(r=0\); there are none at infinity.

## 5. Explicit pure Xi kernel [D]

For \(r>0\), each summand of \(f\) is
\[
g_n(r)=e^{r/2-\pi n^2e^{2r}}.
\]

Put
\[
a=\pi n^2.
\]

Then
\[
\frac{g_n'}{g_n}
=
\frac12-2ae^{2r},
\]
and
\[
g_n''-\frac14g_n
=
\left(
4a^2e^{4r}-6ae^{2r}
\right)g_n.
\]

Hence
\[
\boxed{
\Phi(r)
=
\sum_{n\ge1}
\left[
4\pi^2n^4e^{\frac92|r|}
-
6\pi n^2e^{\frac52|r|}
\right]
e^{-\pi n^2e^{2|r|}}.
}
\]

Equivalently,
\[
\boxed{
\Phi(r)
=
2\pi
\sum_{n\ge1}
n^2e^{\frac52|r|}
\left(
2\pi n^2e^{2|r|}-3
\right)
e^{-\pi n^2e^{2|r|}}.
}
\]

Since
\[
2\pi n^2e^{2|r|}-3
\ge2\pi-3>0,
\]
every summand is positive. Therefore
\[
\boxed{
\Phi(r)>0
\quad\text{for every }r\in\mathbb R.
}
\]

Also
\[
\boxed{
\Phi(-r)=\Phi(r)
}
\]
and \(\Phi\) decays super-exponentially.

## 6. Bilateral transform of the Casimir current [D]

Distributionally,
\[
\left\langle D_r^2K_\theta,e^{wr}\right\rangle
=
\left\langle K_\theta,D_r^2e^{wr}\right\rangle
=
w^2I_\theta(w).
\]

Therefore
\[
\boxed{
\left\langle
\left(D_r^2-\frac14\right)K_\theta,
e^{wr}
\right\rangle
=
\left(w^2-\frac14\right)I_\theta(w).
}
\]

Using the v13.717 formula,
\[
\boxed{
\left\langle
\mathscr C_rK_\theta,e^{wr}
\right\rangle
=
\Xi(w)-\frac12.
}
\]

Thus the answer to the operator-level test is exact:
\[
\boxed{
\textbf{PASS: the shifted differential Casimir acting on }K_\theta
\textbf{ transforms to }\Xi(w)-\frac12.
}
\]

## 7. Origin contact cancellation and pure Xi transform [D]

From Section 4,
\[
\mathscr C_rK_\theta
=
\Phi-\frac12\delta_0.
\]

Taking bilateral transforms,
\[
\Xi(w)-\frac12
=
\int_{\mathbb R}\Phi(r)e^{wr}\,dr-\frac12.
\]

The contact contribution exactly cancels the external completion constant. Hence
\[
\boxed{
\Xi(w)
=
\int_{\mathbb R}\Phi(r)e^{wr}\,dr.
}
\]

Since \(\Phi\) is even,
\[
\boxed{
\Xi(w)
=
2\int_0^\infty\Phi(r)\cosh(wr)\,dr.
}
\]

On the critical line \(w=it\),
\[
\boxed{
\Xi(it)
=
2\int_0^\infty\Phi(r)\cos(tr)\,dr.
}
\]

This is the classical pure Riemann Xi Fourier kernel obtained directly by applying the shifted-Casimir differential operator to the folded theta current and accounting exactly for the origin jump.

## 8. Structural meaning of the external one-half [D]

The v13.717 formula contains
\[
\Xi(w)
=
\frac12+
\left(w^2-\frac14\right)I_\theta(w).
\]

The present calculation shows that
\[
\boxed{
[K_\theta']_0=-\frac12
}
\]
and hence
\[
\boxed{
\mathscr C_rK_\theta
=
\Phi-\frac12\delta_0.
}
\]

Because
\[
\mathcal B[\delta_0]=1,
\]
the contact term contributes exactly
\[
-\frac12
\]
in spectral space.

Therefore
\[
\boxed{
\frac12+
\mathcal B[\mathscr C_rK_\theta]
=
\mathcal B[\Phi].
}
\]

The completion constant \(+1/2\) exactly removes the delta contact generated by folding the theta kernel at the Jacobi fixed point \(r=0\).

## 9. Representation-theoretic interpretation [D/G]

At the level of the rank-one infinitesimal character,
\[
\boxed{
w=j+\frac12
}
\]
gives
\[
\boxed{
w^2-\frac14=j(j+1).
}
\]

The differential realization
\[
\boxed{
\mathscr C_r=D_r^2-\frac14
}
\]
has the same eigenvalue on \(e^{wr}\).

Thus the shared structure has advanced beyond a visual polynomial coincidence:
\[
\boxed{
\text{the shifted-Casimir differential operator itself acts directly on the theta current.}
}
\]

The exact chain is
\[
\boxed{
K_\theta
\xrightarrow{\;D_r^2-\frac14\;}
\Phi-\frac12\delta_0
\xrightarrow{\;\mathcal B\;}
\Xi-\frac12.
}
\]

After the origin contact is cancelled,
\[
\boxed{
\Phi\xrightarrow{\;\mathcal B\;}\Xi.
}
\]

[G] What remains unproved is an actual representation-theoretic intertwiner identifying this differential realization with the earlier finite-dimensional compact \(SU(2)\) ladder representation, or with Suzuki's operator. The common shifted-Casimir polynomial and its differential action are exact; equality of the surrounding representations is not established.

## 10. Consequences and guardrails [D/G]

Because \(\Phi\) is positive and even,
\[
\Xi(w)
=
\int_{\mathbb R}\Phi(r)e^{wr}\,dr
\]
is the bilateral moment-generating transform of a finite positive even measure.

Consequently
\[
\Xi^{(2m+1)}(0)=0
\]
and
\[
\boxed{
\Xi^{(2m)}(0)
=
\int_{\mathbb R}r^{2m}\Phi(r)\,dr>0.
}
\]

On the critical line the corresponding Taylor signs alternate because \(w=it\).

[G] Positivity/evenness of \(\Phi\) does not imply RH or constrain all zeros to the critical line. Fourier transforms of positive even measures can have real and nonreal complex zeros in their analytic continuation.

[G] No spectral-determinant or Hilbert--Pólya claim is promoted here.

## 11. Relation to the active Suzuki bridge [G/O]

v13.721 established that Suzuki's transport contributes the scalar factor \(z\) on exponential defects and reduced the remaining source-faithful bridge to an edge-resolvent theorem for \(S_A^{-1}\).

The present result is complementary:
\[
\boxed{
\Xi(w)=\mathcal B[\Phi](w)
}
\]
with \(\Phi\) generated canonically from \(K_\theta\) by the shifted differential Casimir.

If the conditional paired Suzuki–Xi identity of v13.721 is later promoted to an exact theorem, the natural comparison target should now be not only \(K_\theta\), but also its Casimir-transformed pure kernel \(\Phi\).

## 12. Main result

\[
\boxed{
\left(D_r^2-\frac14\right)K_\theta
=
\Phi-\frac12\delta_0,
}
\]
where
\[
\boxed{
\Phi(r)
=
\sum_{n\ge1}
\left[
4\pi^2n^4e^{\frac92|r|}
-
6\pi n^2e^{\frac52|r|}
\right]
e^{-\pi n^2e^{2|r|}}>0.
}
\]

Its bilateral transform is
\[
\boxed{
\Xi(w)
=
\int_{\mathbb R}\Phi(r)e^{wr}\,dr.
}
\]

Thus
\[
\boxed{
w^2-\frac14
}
\]
is not merely algebraically identical to the shifted rank-one Casimir polynomial: the corresponding differential operator
\[
\boxed{
D_r^2-\frac14
}
\]
acts directly on the theta kernel and produces the pure Xi current, with the completion constant exactly cancelling the origin contact term.

## 13. Next gates [O]

Three concrete gates are now separated:

1. **Representation gate:** construct an explicit intertwiner, if one exists, between the differential realization \(D_r^2-\tfrac14\) and the earlier compact/noncompact rank-one ladder/Casimir realizations.

2. **Arithmetic gate:** apply the logarithmic derivative/inverse-Laplace construction to the pure kernel \(\Phi\) and compare its resulting odd distribution directly with the prime–archimedean current of v13.715.

3. **Suzuki gate:** test whether the edge-resolvent asymptotics of v13.721 naturally act on \(K_\theta\) or on the Casimir-transformed kernel \(\Phi\).

No identification among these three surrounding operator realizations is assumed until the corresponding intertwiner or asymptotic theorem is proved.
