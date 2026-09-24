# Cone Derivation Ledger v13.754 — Basepointed Helix Boundary Intertwiner and Hermite–Biehler Determinant Closure

Date: 2026-09-24

Status: [D] exact algebraic/boundary-triple consequences of audited prior identities; [C] conditional Hilbert/infinite-operator interpretation; [G] guardrails.

Parents: v13.661, v13.667, v13.670, v13.706, v13.737, v13.747, v13.753.

## 0. Synchronization and correction guardrail

Live ledger checked immediately before write: v13.753 is current head; no collision.

This entry explicitly incorporates the v13.670 correction. In particular, E is NOT the characteristic of a second self-adjoint member of Suzuki's real theta family. The relevant boundary parameter is complex, hence maximal dissipative/accumulative according to the global Green-form sign convention.

## 1. Basepointed helix unitary and transported boundary triple [D/C]

v13.753 established the exact form identity
\[
\langle DF,DH\rangle_{\rm Suz}=\langle F,H\rangle_{\rm Weil},
\]
and, under positivity/completion, the derivative unitary between the Weil form space and the screw increment space.

This is the same derivative transport mechanism already exact at finite A in v13.667:
\[
\bar D:\mathcal H(T_A)\overset\sim\longrightarrow\mathcal H(S_A).
\]
For Suzuki deficiency vectors
\[
u_\pm=\bar Dv_\pm,
\]
the boundary maps transport as
\[
\boxed{\widetilde\Gamma_j=\Gamma_j\bar D^{-1},\qquad j=0,1,}
\]
and therefore
\[
\boxed{\widetilde\gamma_A(z)=\bar D\gamma_A(z),\qquad \widetilde m_A(z)=m_A(z).}
\]

Thus every boundary characteristic defined invariantly from the transported triple is unchanged by the derivative unitary.

## 2. Boundary meaning of the zero-mode quotient [D]

The basepointed helix carrier is
\[
\Psi_u(t)=e^{itu}-1,\qquad \Psi_0=0.
\]
The primitive-to-derivative map has
\[
\ker D=\operatorname{span}\{1\}
\]
on the enlarged primitive domain (and trivial kernel on compactly supported test functions).

Hence the zero-mode quotient is
\[
\boxed{\mathcal H_{\rm primitive}/\operatorname{span}\{1\},}
\]
the quotient required to make the primitive-to-derivative transport injective.

It is NOT itself a Suzuki boundary condition:
\[
\boxed{
\text{zero-mode quotient}\ne\ker\Gamma_0,\qquad
\text{zero-mode quotient}\ne\ker\Gamma_1.
}
\]
Instead it precedes the boundary triple:
\[
\boxed{
\text{primitive}/\mathbf1
\xrightarrow{\bar D}
\text{screw/continuous-kernel space}
\xrightarrow{\widetilde\Gamma_j=\Gamma_j\bar D^{-1}}
\mathbb C.
}
\]

This is the precise boundary-triple meaning of basepoint subtraction.

## 3. Deficiency reflection is preserved [D]

With
\[
\Gamma_0u=\sqrt h(\alpha+\beta),\qquad
\Gamma_1u=i\sqrt h(\alpha-\beta),
\]
the channel reflection \(u_+\leftrightarrow u_-\) gives
\[
\Gamma_0\mapsto\Gamma_0,\qquad
\Gamma_1\mapsto-\Gamma_1,
\]
hence
\[
\boxed{m\mapsto-m.}
\]
For
\[
s=(m-i)/(m+i),
\]
\[
\boxed{s\mapsto s^{-1}.}
\]
Thus the transported deficiency reflection retains exactly the rapidity orientation-inversion character.

## 4. Paired deficiency characteristic is intertwined [D]

Suzuki's exact infinite-volume Section-7 identity is
\[
\boxed{
T_{\rm pair}(z)
:=
(z-i)\widehat f_{+i}(z)-(z+i)\widehat f_{-i}(z)
=
C_\xi\frac{\Xi(-iz)}{E(z)},
}
\]
where
\[
C_\xi=\frac{2\xi'(3/2)}{\pi^2 i}.
\]

Since \(\bar D\) transports the deficiency vectors and boundary maps exactly, the paired boundary characteristic constructed from the transported deficiency data satisfies
\[
\boxed{\widetilde T_{\rm pair}=T_{\rm pair}.}
\]

[G] This does NOT identify a single bare helix vector with \(T_{\rm pair}\). The helix/screw current supplies logarithmic-derivative data; \(T_{\rm pair}\) includes the additional de Branges/Hermite–Biehler boundary normalization \(E^{-1}\).

## 5. Exact logarithmic decomposition [D]

Let
\[
s=\frac12-iz,\qquad L(s)=\frac{\xi'}{\xi}(s).
\]
Since
\[
E(z)=\xi(s)+\xi'(s)=\xi(s)[1+L(s)],
\]
\[
\boxed{
\frac{E'}E=-iL(s)-i\frac{L'(s)}{1+L(s)}.
}
\]
Also
\[
T_{\rm pair}=C_\xi/(1+L(s)),
\]
so
\[
\boxed{
\frac{T_{\rm pair}'}{T_{\rm pair}}
=i\frac{L'(s)}{1+L(s)}.
}
\]
Therefore
\[
\boxed{
-iL(s)
=
\frac{T_{\rm pair}'}{T_{\rm pair}}
+
\frac{E'}E.
}
\]

Multiplicatively,
\[
\boxed{E(z)T_{\rm pair}(z)=C_\xi\Xi(-iz).}
\]

## 6. E as the complex Hermite–Biehler boundary characteristic [D]

Use the corrected v13.670 infinite Weyl function. Write
\[
\Xi(z)=\xi(1/2-iz),\qquad D_\xi(z)=\xi'(1/2-iz),
\]
\[
a=\xi(3/2),\qquad b=\xi'(3/2),\qquad c_\infty=b/a.
\]
Then
\[
\boxed{
m_\infty(z)
=
-i\frac{a}{b}\frac{D_\xi(z)}{\Xi(z)}
}
\]
in the stabilized boundary convention. Hence
\[
D_\xi/\Xi=i c_\infty m_\infty
\]
and
\[
\boxed{
E(z)=\Xi(z)[1+i c_\infty m_\infty(z)].
}
\]

Define
\[
\boxed{
\tau_{\rm HB}=\frac{i}{c_\infty}=i\frac{a}{b}.
}
\]
Then
\[
1+i c_\infty m
=
i c_\infty(m-\tau_{\rm HB}),
\]
so
\[
\boxed{
E(z)
=
i c_\infty\,\Xi(z)[m_\infty(z)-\tau_{\rm HB}].
}
\]

Thus, up to a fixed nonzero scalar and the reference characteristic \(\Xi\), E carries exactly the complex boundary denominator for \(\tau_{\rm HB}\).

[G] Since \(\tau_{\rm HB}\notin\mathbb R\), this is NOT a second self-adjoint extension. It is the Hermite–Biehler maximal dissipative/accumulative boundary extension, with the dissipative sign convention dependent on the global Green-form convention.

## 7. Boundary perturbation determinant [D]

Relative to the reference extension
\[
H_\pi=\ker\Gamma_0,
\]
the normalized rank-one boundary determinant is
\[
\boxed{
\Delta_{\rm HB/\pi}(z;z_*)
=
\frac{\tau_{\rm HB}-m(z)}
{\tau_{\rm HB}-m(z_*)}.
}
\]
Using the previous section,
\[
\boxed{
\Delta_{\rm HB/\pi}(z;z_*)
=
\frac{E(z)/\Xi(z)}
{E(z_*)/\Xi(z_*)}.
}
\]
Any overall sign from writing \(m-\tau\) instead of \(\tau-m\) cancels in the normalized determinant.

Consequently
\[
\boxed{
T_{\rm pair}(z)
=
\text{z-independent constant}\times
\Delta_{\rm HB/\pi}(z;z_*)^{-1}.
}
\]

This is the exact boundary-determinant meaning of the paired deficiency transfer.

## 8. Log-determinant / resolvent-trace correction [D]

Differentiate:
\[
\boxed{
\partial_z\log\Delta_{\rm HB/\pi}
=
\frac{E'}E+iL(s).
}
\]
Since
\[
T_{\rm pair}'/T_{\rm pair}
=
-iL-E'/E,
\]
\[
\boxed{
\partial_z\log\Delta_{\rm HB/\pi}
=
-\frac{T_{\rm pair}'}{T_{\rm pair}}.
}
\]

For the rank-one boundary perturbation, with the determinant/resolvent convention of v13.661,
\[
\boxed{
-\partial_z\log\Delta_{\tau/\pi}(z)
=
\operatorname{Tr}\big[(H_\tau-z)^{-1}-(H_\pi-z)^{-1}\big].
}
\]
Hence
\[
\boxed{
\frac{T_{\rm pair}'}{T_{\rm pair}}
=
\operatorname{Tr}\big[(H_{\rm HB}-z)^{-1}-(H_\pi-z)^{-1}\big].
}
\]

Combining with the screw/helix analytic current gives
\[
\boxed{
-iL(s)
=
\operatorname{Tr}\big[(H_{\rm HB}-z)^{-1}-(H_\pi-z)^{-1}\big]
+
\frac{E'}E.
}
\]

Therefore \(E'/E\) is precisely the complementary Hermite–Biehler boundary-normalization/log-determinant term in the decomposition of the analytically regularized helix/Weil logarithmic current.

Equivalently,
\[
\boxed{
\frac{E'}E
=
-iL(s)+\partial_z\log\Delta_{\rm HB/\pi}.
}
\]

## 9. Closed operator architecture [D/C]

The resulting chain is
\[
\boxed{
e^{itu}-1
\xrightarrow{D}
it e^{itu}
\xrightarrow{\rm quadratic\ form}
\widehat{\mathscr W}=t^2\widehat g
\xrightarrow{\rm analytic\ regularization}
-i\,\Xi'/\Xi.
}
\]

The analytic current then decomposes as
\[
\boxed{
-i\,\Xi'/\Xi
=
T_{\rm pair}'/T_{\rm pair}
+
E'/E,
}
\]
where
- \(T_{\rm pair}'/T_{\rm pair}\) is the HB/reference boundary resolvent-trace contribution;
- \(E'/E\) is the complementary HB normalization term.

Multiplicatively,
\[
\boxed{
E\,T_{\rm pair}=C_\xi\Xi.
}
\]

Thus the original multiple-helix/screw picture now reaches Suzuki's paired de Branges deficiency architecture through an exact derivative/form transport plus an exact complex-boundary determinant normalization.

## 10. What is exact and what remains open

[D] Exact:
1. finite-A derivative transport of the boundary triple and invariance of m;
2. zero-mode quotient as the kernel quotient preceding the boundary maps;
3. infinite scalar identity \(T_{\rm pair}=C_\xi\Xi/E\);
4. corrected complex boundary parameter \(\tau_{\rm HB}=i/c_\infty\);
5. normalized determinant identity \(\Delta_{\rm HB/\pi}=(E/\Xi)/(E_*/\Xi_*)\);
6. logarithmic decomposition and rank-one trace identity, in the fixed determinant convention.

[C/O] Still open:
1. proving the infinite HB operator itself as a strong/generalized resolvent limit of finite-A transported extensions;
2. finite-A convergence \(m_A\to m_\infty\) in the required locally uniform sense;
3. unconditional positive Hilbert completion of the generalized screw spectrum (distinct from the exact form identity).

[G] Do not resurrect the retracted v13.669 claim that E comes from a real self-adjoint theta extension.

## 11. Next gate

The next nonredundant gate is finite-to-infinite: define
\[
\tau_{\rm HB}=i/c_\infty
\]
already at finite A, construct
\[
\Delta_{{\rm HB},A/\pi}(z;z_*)
=
\frac{\tau_{\rm HB}-m_A(z)}
{\tau_{\rm HB}-m_A(z_*)},
\]
and determine exactly which convergence of the transported gamma fields/reference resolvents suffices to imply
\[
\Delta_{{\rm HB},A/\pi}\to\Delta_{\rm HB/\pi}
\]
and hence convergence of the paired transfer to \(C_\xi\Xi/E\).