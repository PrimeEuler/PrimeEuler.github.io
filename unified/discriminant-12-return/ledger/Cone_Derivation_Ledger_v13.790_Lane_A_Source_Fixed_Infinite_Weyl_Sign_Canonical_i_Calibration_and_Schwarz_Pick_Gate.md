# Cone Derivation Ledger v13.790 — Lane A Source-Fixed Infinite Weyl Sign, Canonical Calibration at z=i, and Schwarz–Pick Quotient Gate

Date: 2026-09-25

Lane: A.

Status: [R] correction of a later sign regression in v13.754/v13.756/v13.757/v13.777/v13.788/v13.789; [P/D] source-fixed sign from v13.672/v13.675; [D] exact finite calibration \(m_a(i)=i\); [D] exact Schwarz–Pick factorization of the one-function quotient; [C] new bounded scalar convergence gate.

Parents: v13.661, v13.672, v13.675–677, v13.754–756, v13.788–789.

## 0. Synchronization and reason for correction

Immediately before this write the live ledger head is v13.789. No collision is present.

The canonical point \(z=i\) exposes a sign regression that entered after the source-fixed convention had already been settled.

The authoritative source/convention chain is:

- v13.661:
\[
\frac{W_0}{W_\pi}=i\,m_a;
\]
- v13.672, derived by tracking the raw boundary form versus Suzuki's conjugated characteristic:
\[
\boxed{
m_\infty(z)
=
+i\,\frac{\xi(3/2)}{\xi'(3/2)}
\frac{\xi'(1/2-iz)}{\xi(1/2-iz)};
}
\]
- v13.675 independently repeats the source transcript and explicitly states that v13.672 has the correct final sign;
- v13.676 uses that sign in the finite Hermite–Biehler theorem.

v13.754 later wrote the opposite sign, and that sign propagated into several descendants. The later sign was not rederived from the source and conflicts with the canonical boundary normalization at \(z=i\).

## 1. Exact finite calibration at the deficiency point [D]

Use the ordinary boundary triple of v13.661:
\[
\Gamma_0f=\sqrt{h_a}(\alpha+\beta),
\qquad
\Gamma_1f=i\sqrt{h_a}(\alpha-\beta),
\]
for
\[
f=f_0+\alpha v_++\beta v_-.
\]

At \(z=i\), the defect space is spanned by \(v_+\). The normalized gamma vector is
\[
\gamma_a(i)=\frac{v_+}{\Gamma_0v_+}
=\frac{v_+}{\sqrt{h_a}}.
\]
Therefore
\[
\boxed{
m_a(i)
=
\Gamma_1\gamma_a(i)
=
i.
}
\tag{1}
\]

Similarly,
\[
m_a(-i)=-i
\]
in the reflected lower-half-plane sense.

Equation (1) is exact for every finite \(a\).

## 2. Source-fixed infinite sign [P/D]

Define
\[
\boxed{
R_\xi(z)
:=
\frac{\xi(3/2)}{\xi'(3/2)}
\frac{\xi'(1/2-iz)}
{\xi(1/2-iz)}.
}
\tag{2}
\]

The source-fixed convention of v13.672/v13.675 is
\[
\boxed{
m_\infty(z)=+i\,R_\xi(z).
}
\tag{3}
\]

At \(z=i\),
\[
\frac12-i(i)=\frac32,
\]
so
\[
R_\xi(i)
=
\frac{\xi(3/2)}{\xi'(3/2)}
\frac{\xi'(3/2)}{\xi(3/2)}
=
1.
\]
Hence
\[
\boxed{
m_\infty(i)=i,
}
\tag{4}
\]
exactly matching the finite calibration (1).

The later negative-sign formula would instead give \(m_\infty(i)=-i\), contradicting the canonical finite normalization and the source-fixed v13.675 convention.

## 3. Correct Hermite–Biehler boundary parameter [R/D]

Let
\[
c_\infty:=\frac{\xi'(3/2)}{\xi(3/2)}>0.
\]
From (3),
\[
\frac{\xi'}{\xi}(1/2-iz)
=
-i c_\infty m_\infty(z).
\]
Thus
\[
\boxed{
\frac{\Xi}{\Xi+D}
=
\frac{1}{1-i c_\infty m_\infty}.
}
\tag{5}
\]

The corresponding complex boundary parameter is
\[
\boxed{
\tau_{\rm HB}
=
-\frac{i}{c_\infty},
}
\tag{6}
\]
and the finite entire Hermite–Biehler combination is
\[
\boxed{
E_a^{\rm HB}
=
W_\pi-c_\infty W_0.
}
\tag{7}
\]

Equations (5)–(7) are exactly those of v13.672/v13.675/v13.676.

## 4. Supersession map for the sign regression [R/G]

The following later formulas must use (3), not the regressed negative sign:

- v13.754 §6 and all formulas depending on \(m_\infty=-iR_\xi\);
- v13.756's displayed \(\tau_{\rm HB}=+i/c_\infty\), which must be replaced by (6);
- v13.757's infinite Weyl target;
- v13.777's infinite parity-ratio target;
- v13.788's infinite reflection-ratio target;
- v13.789's infinite Schur target.

The structural finite-\(a\) algebra in those entries survives whenever it does not depend on the wrong infinite sign.

## 5. Correct reflection-quotient and Schur targets [D]

From v13.788,
\[
\rho_a(z)
=
\frac{F_a(-z)}{F_a(z)}
=
\frac{z-i}{z+i}
\frac{i\,m_a(z)-1}
{i\,m_a(z)+1}.
\]

Using \(m_\infty=iR_\xi\),
\[
i m_\infty=-R_\xi,
\]
so
\[
\boxed{
\rho_\infty(z)
=
\frac{z-i}{z+i}
\frac{R_\xi(z)+1}
{R_\xi(z)-1}.
}
\tag{8}
\]

For the Cayley transform
\[
s_a(z)
=
\frac{m_a(z)-i}{m_a(z)+i},
\]
the corrected infinite target is
\[
\boxed{
s_\infty(z)
=
\frac{R_\xi(z)-1}
{R_\xi(z)+1}.
}
\tag{9}
\]

At \(z=i\), both finite and target Schur functions vanish:
\[
\boxed{
s_a(i)=0,
\qquad
s_\infty(i)=0.
}
\tag{10}
\]

## 6. Schwarz–Pick factorization [D]

Because \(m_a\) is a scalar Nevanlinna function,
\[
s_a:\mathbb C_+\to\mathbb D.
\]

Define the half-plane Blaschke factor
\[
\boxed{
\phi_i(z):=\frac{z-i}{z+i}.
}
\tag{11}
\]
It maps \(\mathbb C_+\) to \(\mathbb D\) and satisfies \(\phi_i(i)=0\).

Since \(s_a(i)=0\), Schwarz–Pick gives
\[
\boxed{
|s_a(z)|
\le
|\phi_i(z)|
\qquad(z\in\mathbb C_+).
}
\tag{12}
\]

Therefore
\[
\boxed{
h_a(z)
:=
\frac{s_a(z)}{\phi_i(z)}
}
\tag{13}
\]
extends holomorphically through \(z=i\) and satisfies
\[
\boxed{
|h_a(z)|\le1
\qquad(z\in\mathbb C_+).
}
\tag{14}
\]

Using the one-function formula from v13.789,
\[
s_a(z)
=
\phi_i(z)\frac{F_a(z)}{F_a(-z)},
\]
hence
\[
\boxed{
h_a(z)
=
\frac{F_a(z)}{F_a(-z)}.
}
\tag{15}
\]

Thus the raw one-function reflection quotient inverse, after its canonical removable continuation, is itself a Schur function.

## 7. Stronger normal-family gate [D]

The family
\[
\boxed{\{h_a\}}
\]
is uniformly bounded by \(1\) on \(\mathbb C_+\), hence is Montel-normal.

The correct target implied by (9) is
\[
\boxed{
h_\infty(z)
=
\frac{z+i}{z-i}
\frac{R_\xi(z)-1}
{R_\xi(z)+1},
}
\tag{16}
\]
with the singularity at \(z=i\) removable whenever this target arises as a locally uniform Schur limit.

Therefore, if for any uniqueness set
\[
S\subset\mathbb C_+
\]
with an interior accumulation point one proves
\[
h_a(z)\to h_\infty(z)
\qquad(z\in S),
\]
then Vitali yields
\[
\boxed{
h_a\to h_\infty
}
\]
locally uniformly, followed by
\[
s_a=\phi_i h_a\to s_\infty
\]
and hence
\[
m_a\to m_\infty
\]
away from the inverse-Cayley divisor.

This is a strictly cleaner bounded scalar target than the meromorphic \(\rho_a=1/h_a\).

## 8. Necessary-condition interpretation [G]

The finite functions \(h_a\) are Schur unconditionally.

Therefore any proposed locally uniform infinite target must itself be a Schur-class function on \(\mathbb C_+\).

The project must **not** assume this for (16) unless it has been independently established. If (16) fails the Schur condition, that would obstruct the claimed finite-to-infinite Weyl convergence rather than justify modifying the finite theory.

Thus the Schur property of the target is a necessary analytic consistency test and may encode genuinely nontrivial information about \(\xi\).

## 9. Result

The source-fixed sign and the canonical deficiency calibration agree:
\[
\boxed{
m_a(i)=m_\infty(i)=i.
}
\]

The finite spectral problem admits the stronger bounded one-function observable
\[
\boxed{
h_a(z)
=
\frac{F_a(z)}{F_a(-z)}
=
\frac{s_a(z)}{(z-i)/(z+i)},
\qquad
|h_a(z)|\le1
\quad(z\in\mathbb C_+).
}
\]

The corrected target is
\[
\boxed{
h_\infty(z)
=
\frac{z+i}{z-i}
\frac{R_\xi(z)-1}{R_\xi(z)+1}.
}
\]

Consequently Lane A's finite-to-infinite spectral convergence is now reduced to pointwise identification of a uniformly bounded holomorphic family on any interior uniqueness set.
