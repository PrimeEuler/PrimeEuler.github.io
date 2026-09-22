# Cone Derivation Ledger v13.671 — Finite Hermite-Biehler Characteristic: E_a = W_pi + c_infty W_0

Date: 2026-09-22

Status: exact finite-a algebraic construction from the audited boundary triple. This gives a canonical entire finite approximant whose infinite de Branges limit is E=Xi+xi', conditional only on the corresponding finite-to-infinite convergence.

## 0. Live collision/relevance check

Immediately before this write the ledger ends at v13.670. No collision. v13.670 corrected the missing i and identified the target denominator with a non-self-adjoint boundary parameter.

## 1. Two audited self-adjoint characteristics determine m_a

From v13.661,
\[
\frac{W(a,\theta;z)}{W(a,\pi;z)}
=
-i e^{i\theta/2}\cos(\theta/2)
[\tau_\theta-m_a(z)].
\]
At theta=0, tau_0=0, so
\[
\boxed{
\frac{W_0(a,z)}{W_\pi(a,z)}=i\,m_a(z).
}
\]
Equivalently,
\[
\boxed{
m_a(z)=-i\,\frac{W_0(a,z)}{W_\pi(a,z)}.
}
\]

Thus the Weyl function is exactly recoverable from the two real self-adjoint characteristics theta=0 and theta=pi.

## 2. Hermite-Biehler complex boundary parameter

Let
\[
a_\infty=\xi(3/2),\qquad b_\infty=\xi'(3/2),\qquad
c_\infty=b_\infty/a_\infty.
\]
The corrected Corollary denominator is
\[
1+i c_\infty m_\infty.
\]
Set
\[
\boxed{\tau_{HB}=i/c_\infty=i\,a_\infty/b_\infty.}
\]
Then
\[
\tau_{HB}-m_a
=
\frac{i}{c_\infty}[1+i c_\infty m_a].
\]
This is the Krein denominator for the complex boundary condition
\[
\Gamma_1 f=\tau_{HB}\Gamma_0f.
\]
Since tau_HB is nonreal, this is a maximal dissipative or accumulative extension according to the sign convention for the Green identity.

## 3. Exact finite entire HB characteristic

Using W_0/W_pi=i m_a,
\[
1+i c_\infty m_a
=
1+c_\infty\frac{W_0}{W_\pi}.
\]
Therefore define
\[
\boxed{
E_a^{HB}(z):=
W_\pi(a,z)+c_\infty W_0(a,z).
}
\]
This is entire because W_pi and W_0 are entire.

Moreover
\[
\boxed{
E_a^{HB}(z)
=
W_\pi(a,z)[1+i c_\infty m_a(z)].
}
\]
The apparent poles of m_a at zeros of W_pi cancel exactly in the entire linear combination.

The canonical finite ratio is therefore
\[
\boxed{
R_a^{HB}(z)
:=
\frac{W_\pi(a,z)}
{E_a^{HB}(z)}
=
\frac{1}{1+i c_\infty m_a(z)}.
}
\]

No arbitrary finite c_a is required.

## 4. Infinite de Branges match

Suzuki Section 7.8 gives, in compatible characteristic normalization,
\[
\frac{W_0^\infty(z)}{W_\pi^\infty(z)}
=
\frac{a_\infty}{b_\infty}
\frac{\xi'(1/2-iz)}{\Xi(z)}.
\]
Therefore
\[
c_\infty\frac{W_0^\infty}{W_\pi^\infty}
=
\frac{\xi'}{\Xi}.
\]
Hence
\[
\boxed{
E_\infty^{HB}
=
W_\pi^\infty+c_\infty W_0^\infty
\propto
\Xi+\xi'
=
E.
}
\]
And
\[
\boxed{
R_\infty^{HB}
=
\frac{W_\pi^\infty}{E_\infty^{HB}}
=
\frac{\Xi}{\Xi+\xi'}.
}
\]

Thus Suzuki's Corollary-1.6 target is exactly the infinite limit of the finite ratio W_pi/(W_pi+c W_0), provided the relevant finite characteristics converge after their common normalization.

## 5. Why this is better than raw W_pi normalization

Any common nonzero multiplicative factor q_a(z) applied to all theta characteristics cancels:
\[
\frac{q_aW_\pi}{q_aW_\pi+c_\infty q_aW_0}
=
R_a^{HB}.
\]
Therefore R_a^{HB} is invariant under the unknown theta-independent normalization e^{phi(a,z)}.

This does NOT recover the raw asymptotic of W_pi, but it gives a normalization-free finite observable with exactly the desired infinite target.

## 6. Spectral interpretation

- zeros of W_pi: spectrum of the theta=pi self-adjoint extension;
- zeros of W_0: spectrum of the theta=0 self-adjoint extension;
- poles of R_a^{HB}: zeros of E_a^{HB}, i.e. eigenvalues of the complex-boundary extension tau_HB;
- zeros of R_a^{HB}: theta=pi spectrum, unless canceled by a simultaneous zero (excluded generically by simplicity/interlacing for distinct self-adjoint extensions).

Because m_a is a scalar Nevanlinna function, the location of solutions m_a(z)=tau_HB is controlled by the sign of Im tau_HB. This provides a direct route to a finite Hermite-Biehler zero-half-plane statement.

## 7. Next gate

Prove the half-plane zero location of E_a^{HB} from the Nevanlinna property of m_a, fix the dissipative/accumulative sign convention, and derive the corresponding Schur function
\[
S_a(z)=\frac{m_a(z)-\overline{\tau_{HB}}}{m_a(z)-\tau_{HB}}.
\]
Then compare the finite E_a^{HB} to its sharp transform and determine whether it is genuinely Hermite-Biehler for every admissible finite a. If yes, the project obtains a finite-a de Branges object directly from Suzuki's two self-adjoint characteristics.
