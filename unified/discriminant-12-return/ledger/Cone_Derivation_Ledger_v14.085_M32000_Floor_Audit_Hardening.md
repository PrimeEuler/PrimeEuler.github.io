# Cone Derivation Ledger v14.085 — M32000 Floor Audit Hardening: Derived Cross-Block Cap and 2x Residual Stress

**Date:** 2026-10-06  
**Track:** Lane A / audit hardening for v14.084  
**Status:** [D] analytic cross-block cap sharpened below the public 40; [N-cert stress] v14.084 floor budget rerun with a doubled protected-column residual cap; [I] the 32k sign-flip target remains strictly negative under both stresses; **still not promoted pending independent audit.**  
**Parent:** v14.084.  
**Research commit:** \`43bea4af6158285beba5896ef2fa9243da46e0c9\`.  
**Collision check:** immediately before this write, live HEAD was \`43bea4af6158285beba5896ef2fa9243da46e0c9\`; live ledger max was v14.084. No collision.

---

## 1. Cross-block cap 40 is derived, not assumed [D]

For the frozen-\(P\) complement extension from modes through 8000 to the shell \(8000<n\le32000\), use the source-faithful bound \(|z_n|\le10\).

For same-parity modes,

\[
|K_{\rm disp}(n,m)|
\le
\frac{20}{\pi|n-m|}.
\]

Since \(|n-m|=2k\), the worst row and column harmonic sums satisfy

\[
R_{\rm disp}
\le
\frac{10}{\pi}H_{12000},
\qquad
C_{\rm disp}
\le
\frac{10}{\pi}H_{4000}.
\]

Hence Schur's test gives

\[
\|B_{\rm disp}\|_2
\le
\sqrt{R_{\rm disp}C_{\rm disp}}.
\]

The deterministic producer evaluates

\[
\|B_{\rm disp}\|_2<29.94.
\]

For the rank-one pole cross-block, even parity is worst and

\[
\|B_{\rm pole}\|_2
\le
2\|p_{\rm base}\|_2\|p_{\rm shell}\|_2
\le
4\cosh^2(1/2)
<5.09.
\]

Therefore

\[
\boxed{
\|B\|_2<35.0221<40.
}
\]

So the public v14.084 cap \(\|B\|\le40\) has about 14% direct analytic slack.

---

## 2. Double the LDDD residual cap [N-cert stress]

v14.084 used the public per-column protected residual cap

\[
\|R_j\|_2\le10^{-25}.
\]

Observed arch-200/LDDD residual maxima are

\[
6.2841\times10^{-26}\quad(e),
\qquad
1.4351\times10^{-26}\quad(o).
\]

As an adversarial audit stress, rerun the entire outward floor and shell budget with

\[
\boxed{
\|R_j\|_2\le2\times10^{-25}
}
\]

for all six protected columns, leaving every other conservative public cap unchanged:

\[
C_{\rm DD}=8192,
\quad
Q_{\rm comp}\le12,
\quad
\|W\|_F^2\le8,
\quad
\tau_e\le0.04,
\quad
\tau_o\le0.11,
\quad
\|B\|\le40.
\]

The residual quadratic charge grows by a factor four.

Even under that doubled cap, the deterministic producer gives

\[
\boxed{
\mu_{e,32k}^{(2R)}
>
2.2905811292683846\times10^{-31},
}
\]

so

\[
\boxed{
\mu_{e,32k}^{(2R)}/(1.2\times10^{-31})
>
1.9088.
}
\]

Odd parity remains nonbinding:

\[
\mu_{o,32k}^{(2R)}
\approx1.28033\times10^{-26}.
\]

Thus v14.084 does not depend on the residual cap being tuned close to the measured value.

---

## 3. Transport still closes under the doubled-residual stress [N-cert stress]

The stressed even operator radius becomes

\[
\theta_{e,32k}^{(2R)}
=
4.76503641674819\times10^{-6},
\]

still well below the v14.080 maximum admissible

\[
1.174454\times10^{-5}.
\]

Re-evaluating the same audited shell consumer gives a strictly negative 16k→32k interval and, after addition of the promoted 4k→16k interval,

\[
\boxed{
\sup E_{4k\to32k}^{(2R)}
<
-1.20109620629\times10^{-5}.
}
\]

Therefore even a factor-two residual inflation leaves a one-sided finite margin above \(1.2\times10^{-5}\).

---

## 4. Audit consequence

v14.084 remains the actual certificate target. This entry only hardens two likely audit pressure points:

1. \(\|B\|\le40\) is now backed by a direct analytic \(<35.03\) derivation.
2. The protected residual allowance may be doubled and the target still closes.

No theorem is promoted here. External audit should still check the remaining public caps, especially \(Q_{\rm comp}\le12\), the graph-shear caps, and the \(C_{\rm DD}=8192\) arithmetic envelope.

Sandbox remains on the v14.083 Lemma G/W task; no duplicate Sandbox assignment is created.
