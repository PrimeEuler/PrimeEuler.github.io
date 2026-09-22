# Cone Derivation Ledger v13.675 — Reproducible Suzuki v2 Source Transcript and Boundary-Form/Characteristic Convention Lemma

Date: 2026-09-22

Status: audit-requested stabilization checkpoint. This entry responds directly to v13.674 §§2,5,8 by recording a reproducible line-level live-source transcript and deriving the raw-boundary-form versus entire-characteristic conversion once, from Suzuki's definitions, before any further asymptotic claims.

## 0. Live collision/relevance check

Immediately before this write the ledger ends at v13.674. The audit recommendations are:
1. stop relying on prose assertions about Corollary 1.6; preserve inspectable source evidence;
2. pin down the exact conjugation convention relating Suzuki's raw boundary form to the entire W characteristic before extending the HB lane;
3. audit v13.673 carefully.

This entry addresses (1) and (2). v13.673 is treated separately after this convention lemma.

## 1. Reproducible source locator

Source URL:
https://arxiv.org/html/2606.09096v2

Live fetch metadata on 2026-09-22:
- arXiv identifier: 2606.09096v2 [math.NT]
- revision date displayed by arXiv: 17 Aug 2026
- title: "Weil's quadratic form via the screw function"
- author: Masatoshi Suzuki.

The current source can be reproduced by fetching that exact versioned URL and inspecting:
- HTML lines 206-226 for Theorem 1.5 / Corollary 1.6;
- lines 733-760 for the von Neumann basis and raw boundary form;
- lines 902-945 for Section 7.8.

## 2. Corollary 1.6 transcript

Theorem 1.5 defines
\[
W(a,\theta;z)
=(z-i)\int_{-a}^{a}v_+(a,x)e^{izx}dx
+e^{i\theta}(z+i)\int_{-a}^{a}v_-(a,x)e^{izx}dx.
\]

The prose immediately before Corollary 1.6 says that W is expected to approximate "the reciprocal of one plus its logarithmic derivative."

Equation (1.12) is
\[
\boxed{
\lim_{a\to\infty}e^{\phi(a,z)}W(a,\theta;z)
=
\frac{\xi(1/2-iz)}
{\xi(1/2-iz)+\xi'(1/2-iz)}
}
\]
uniformly on compact subsets.

This settles the source attribution at the exact versioned URL above.

## 3. Raw boundary form from Section 6

Suzuki defines
\[
\mathcal W(u,v)
=
\langle\mathscr D_a^*u,v\rangle_{T_a}
-\langle u,\mathscr D_a^*v\rangle_{T_a}.
\]
With
\[
w_\theta=v_++e^{i\theta}v_-,
\]
Section 6.5 obtains
\[
\boxed{
\mathcal W(v_z,w_\theta)
=
(z+i)\langle v_z,v_+\rangle
+
e^{-i\theta}(z-i)\langle v_z,v_-\rangle.
}
\]
Also
\[
\langle v_z,v_\pm\rangle
=
\overline{\widehat v_\pm(\bar z)}.
\]

Take complex conjugates at \bar z:
\[
\overline{\mathcal W(v_{\bar z},w_\theta)}
=
(z-i)\widehat v_+(z)
+
e^{i\theta}(z+i)\widehat v_-(z).
\]
The right-hand side is exactly Theorem-1.5 W(a,theta;z). Therefore the convention is
\[
\boxed{
W(a,\theta;z)
=
\overline{\mathcal W(v_{\bar z},w_\theta)}.
}
\]
This is not a guessed convention; it follows directly from equations (6.2)-(6.3) and (1.11).

## 4. Section-7.8 raw form and sharp conversion

Write
\[
\Xi(z)=\xi(1/2-iz),\qquad D(z)=\xi'(1/2-iz),
\]
\[
E=\Xi+D,\qquad E^\sharp=\Xi-D.
\]
Suzuki gives
\[
\mathcal W(K(\bar z,\cdot),W_\theta)
=
-\frac{e^{-i\theta/2}}{\pi i}
[C_\theta E-\bar C_\theta E^\sharp],
\]
where
\[
C_\theta=a\cos(\theta/2)+ib\sin(\theta/2),
\quad
a=\xi(3/2),\ b=\xi'(3/2).
\]
Hence
\[
\boxed{
B_\theta(z):=\mathcal W(K(\bar z,\cdot),W_\theta)
=
-\frac{2e^{-i\theta/2}}{\pi i}
[ib\sin(\theta/2)\Xi+a\cos(\theta/2)D].
}
\]
At the two endpoints:
\[
\boxed{B_\pi=(2ib/\pi)\Xi,\qquad B_0=(2ia/\pi)D.}
\]

Now use the Section-6 convention:
\[
W_\theta^\infty(z)=\overline{B_\theta(\bar z)}=B_\theta^\sharp(z).
\]
The functional equation gives
\[
\Xi^\sharp=\Xi,\qquad D^\sharp=-D.
\]
Therefore
\[
\boxed{
W_\pi^\infty=(2ib/\pi)\Xi,
\qquad
W_0^\infty=-(2ia/\pi)D.
}
\]
So
\[
\boxed{
\frac{W_0^\infty}{W_\pi^\infty}
=
-\frac{a}{b}\frac{D}{\Xi}.
}
\]

This is the stable sign conversion requested by v13.674.

## 5. Weyl-function sign

From the audited finite boundary-triple identity v13.661, theta=0 gives
\[
\boxed{\frac{W_0}{W_\pi}=i\,m_a.}
\]
Thus at infinity
\[
i m_\infty
=
-\frac{a}{b}\frac{D}{\Xi},
\]
hence
\[
\boxed{
m_\infty(z)
=
i\frac{a}{b}\frac{D(z)}{\Xi(z)}.
}
\]

Set c=b/a. Then
\[
D/\Xi=-icm_\infty
\]
and
\[
\boxed{
\frac{\Xi}{\Xi+D}
=
\frac{1}{1-icm_\infty}.
}
\]

Therefore v13.672 has the correct final sign.

## 6. Finite HB combination

Since W_0/W_pi=i m_a,
\[
1-icm_a=1-cW_0/W_\pi.
\]
Thus
\[
\boxed{
E_a^{HB}=W_\pi-cW_0
}
\]
is the finite entire denominator corresponding to the complex boundary parameter
\[
\boxed{\tau_{HB}=-i/c.}
\]

At infinity:
\[
W_\pi^\infty-cW_0^\infty
=
(2ib/\pi)\Xi
+
(2ib/\pi)D
=
(2ib/\pi)E.
\]
Hence
\[
\boxed{
E_a^{HB}\rightsquigarrow (2ib/\pi)E
}
\]
under the common finite-to-infinite normalization.

## 7. Supersession status

This source-fixed derivation stabilizes the cascade:
- v13.668 real-multiple m_infty: superseded.
- v13.669 real-self-adjoint quotient: retracted.
- v13.670 factor-i insight: retained, sign superseded.
- v13.671 plus-sign E_a: superseded.
- v13.672 final sign: CONFIRMED by direct source-definition derivation.

No further sign choice is left at this gate.

## 8. Artifact limitation

The GitHub connector available to this thread can create text files but does not provide a direct raw-byte HTTP download primitive. Therefore this ledger entry records the exact versioned URL, fetch date, line locators, formulas, and derivation needed for reproducibility. If a raw HTML attachment mechanism becomes available, the exact fetched HTML should additionally be archived under research-notes without altering the mathematical status established here.
