# Cone Derivation Ledger v13.672 — Sign Completion: E_a^HB = W_pi - c_infty W_0 and tau_HB = -i/c_infty

Date: 2026-09-22

Status: exact sign correction to v13.670-v13.671 after tracking Suzuki's conjugated characteristic W versus the raw Section-7.8 boundary form. This correction restores the expected Hermite-Biehler half-plane orientation.

## 0. Live collision/relevance check

Immediately before this write the ledger ends at v13.671. No collision.

## 1. Raw boundary form versus conjugated characteristic

For the ordinary boundary triple of v13.661, a Gamma_0-normalized defect vector has coefficients
\[
a_z=(1-im(z))/2,\qquad b_z=(1+im(z))/2.
\]
The RAW boundary-form ratio at theta=0 versus theta=pi is
\[
\boxed{
\frac{\mathcal W(v_z,w_0)}
{\mathcal W(v_z,w_\pi)}
=-i\,m(z).
}
\]

Suzuki's entire characteristic, however, is
\[
W(a,\theta;z)
=
\overline{\mathcal W(v_{\bar z},w_\theta)}.
\]
Using m(z)=overline{m(bar z)},
\[
\boxed{
\frac{W_0(a,z)}{W_\pi(a,z)}
=+i\,m_a(z).
}
\]
This agrees with v13.661.

## 2. Apply the conjugation to the infinite de Branges formula

Suzuki Section 7.8 gives for the RAW boundary forms
\[
\frac{B_0(z)}{B_\pi(z)}
=
\frac{a_\infty}{b_\infty}
\frac{D(z)}{\Xi(z)},
\]
where
\[
a_\infty=\xi(3/2),\quad
b_\infty=\xi'(3/2),\quad
D(z)=\xi'(1/2-iz).
\]

Because
\[
\Xi^\sharp=\Xi,\qquad D^\sharp=-D,
\]
passing to Suzuki's conjugated characteristic changes the sign:
\[
\boxed{
\frac{W_0^\infty(z)}{W_\pi^\infty(z)}
=
-\frac{a_\infty}{b_\infty}
\frac{D(z)}{\Xi(z)}.
}
\]

Combining with W_0/W_pi=i m gives
\[
\boxed{
m_\infty(z)
=
i\,\frac{a_\infty}{b_\infty}
\frac{D(z)}{\Xi(z)}.
}
\]
Thus v13.670 had the correct factor i but the wrong overall sign.

## 3. Correct Möbius target

Set
\[
c_\infty=b_\infty/a_\infty>0.
\]
Then
\[
\frac{D}{\Xi}
=
-i c_\infty m_\infty.
\]
Therefore
\[
\boxed{
\frac{\Xi}{\Xi+D}
=
\frac1{1-i c_\infty m_\infty}.
}
\]

## 4. Correct complex boundary parameter

We need
\[
\tau_{HB}-m
\propto
1-i c_\infty m.
\]
The correct parameter is
\[
\boxed{
\tau_{HB}=-\frac{i}{c_\infty}
=-i\frac{a_\infty}{b_\infty}.
}
\]
Indeed
\[
\tau_{HB}-m
=
-\frac{i}{c_\infty}[1-i c_\infty m].
\]

Since c_infty>0, tau_HB lies in the LOWER half-plane. For the standard Nevanlinna convention Im m(z)>0 when Im z>0, the equation m(z)=tau_HB has no solutions in C_+. This is exactly the orientation expected for a Hermite-Biehler denominator with no upper-half-plane zeros.

## 5. Correct finite entire HB characteristic

Since
\[
W_0/W_\pi=i m,
\]
we have
\[
1-i c_\infty m
=
1-c_\infty W_0/W_\pi.
\]
Therefore the correct finite entire combination is
\[
\boxed{
E_a^{HB}(z)
=
W_\pi(a,z)-c_\infty W_0(a,z).
}
\]
and
\[
\boxed{
R_a^{HB}(z)
=
\frac{W_\pi(a,z)}
{W_\pi(a,z)-c_\infty W_0(a,z)}
=
\frac1{1-i c_\infty m_a(z)}.
}
\]

This supersedes the plus sign in v13.671.

At infinity,
\[
W_\pi^\infty-c_\infty W_0^\infty
\propto
\Xi+D=E,
\]
so
\[
R_\infty^{HB}=\Xi/E.
\]

## 6. Immediate half-plane consequence

For z in C_+, m_a(z) is Nevanlinna:
\[
\operatorname{Im}m_a(z)>0.
\]
But
\[
\operatorname{Im}\tau_{HB}<0.
\]
Hence
\[
m_a(z)\ne\tau_{HB}\quad(z\in C_+).
\]
Therefore
\[
\boxed{
E_a^{HB}(z)\ne0\quad\text{for Im z>0}.
}
\]

This proves the correct zero-free upper-half-plane property at every admissible finite a.

To prove the full strict Hermite-Biehler inequality |E_a|>|E_a^\sharp| in C_+, one still needs the precise relation between E_a^\sharp and the conjugate boundary parameter +i/c_infty. That is the next gate.

## 7. Supersession map

- v13.668: replace m_infty real-multiple formula by the displayed +i formula here.
- v13.669: remains retracted.
- v13.670: retain the non-self-adjoint insight but replace -i factor by +i and tau=+i/c by tau=-i/c.
- v13.671: replace E_a=W_pi+cW_0 by
\[
\boxed{E_a=W_\pi-cW_0.}
\]

The core structural discovery survives and is now sign-consistent with de Branges theory.
