# Cone Derivation Ledger v14.010 — Unit-Energy Remote Amplitude Common-Mode Diagnostic

**Date:** 2026-10-04
**Track:** Lane A / no-twist Suzuki Xi scalar certification
**Status:** [D] exact interpretation of C_N L_N^2 as the squared remote 1/n coefficient of the unit-energy finite source solution; [N] source-faithful LDDD reconstruction through N=4000; [N] direct remote rows verify the 1/n coefficient; [N] normalized even/odd leading amplitudes converge to within 8.85e-4 relative at N=4000; [I] strong evidence that the leading normalized remote correction is common-mode and cancels from the parity quotient; [O] prove the common leading term and bound the residual parity difference.
**Parents:** v14.008–009, v13.989.
**Research commits:** 362d20e4087c808dfe27ed1394785dabde1edc72, 47426645a132516795b0ac297940e3af81f87891, 9a60585d65413724d3fead754fb49a26cef899a6.
**Collision check:** immediately before this write, live HEAD was 9a60585d65413724d3fead754fb49a26cef899a6 and no v14.010 ledger file was present.

---

## 1. Remote coefficient for the finite source solve [D]

For parity p and cutoff N, let

\[
x_{p,N}=T_{p,N}^{-1}f_{p,N},
\qquad
G_{p,N}=\langle f_{p,N},x_{p,N}\rangle,
\qquad
C_{p,N}=G_{p,N}^{-1}.
\]

For remote modes n beyond the finite section, the source-faithful operator formulas give

\[
r_{p,N}(n)
:=
f_p(n)-(T_px_{p,N})(n)
=
\frac{L_{p,N}}{n}
+
O\!\left(\frac{\log n}{n^2}\right).
\]

With the current basis conventions,

\[
L_{p,N}
=
f_{p,\mathrm{lead}}
+
\frac{2}{\pi}\langle z,x_{p,N}\rangle
-
\alpha_p\frac{4g_p}{\pi}\langle p,x_{p,N}\rangle.
\]

Here

\[
f_{e,\mathrm{lead}}=\frac{4\cosh1}{\pi},
\qquad
f_{o,\mathrm{lead}}=-\frac{4\sinh1}{\pi},
\]

while

\[
g_e=\cosh(1/2),\quad \alpha_e=2,
\qquad
g_o=\sinh(1/2),\quad \alpha_o=-2.
\]

This is the source-solve analogue of the v13.989 remote leading-moment formula.

---

## 2. Projective normalization [D]

Define the unit-energy finite source vector

\[
y_{p,N}=\sqrt{C_{p,N}}\,x_{p,N}.
\]

Since

\[
\langle x_{p,N},T_{p,N}x_{p,N}\rangle
=
G_{p,N},
\]

we have

\[
\boxed{
\langle y_{p,N},T_{p,N}y_{p,N}\rangle=1.
}
\]

The remote residual of y is

\[
\sqrt{C_{p,N}}\,r_{p,N}(n)
=
\frac{\sqrt{C_{p,N}}L_{p,N}}{n}
+
O\!\left(\frac{\sqrt{C_{p,N}}\log n}{n^2}\right).
\]

Therefore

\[
\boxed{
A_{p,N}:=C_{p,N}L_{p,N}^2
}
\]

is exactly the squared leading remote 1/n amplitude of the unit-energy finite source solution.

This is the natural projective quantity to compare across parity.

---

## 3. LDDD reconstruction [N]

The finite source solution is reconstructed from the same v14.008 refined protected/complement state:

\[
x_N=y_f+Ww,
\qquad
w=S^{-1}g.
\]

The seven protected/source complement columns are first refined in LDDD arithmetic, then the moments

\[
\langle z,x_N\rangle
\quad\text{and}\quad
\langle p,x_N\rangle
\]

are accumulated in the same expansion arithmetic.

Independent direct high-precision remote rows are evaluated at approximately 2N, 4N, and 8N to verify the asymptotic coefficient.

---

## 4. Cutoff profile [N]

The normalized leading amplitudes are:

\[
\begin{array}{c|cc|c}
N&A_{e,N}=C_eL_e^2&A_{o,N}=C_oL_o^2&A_o/A_e\\ \hline
768&432.1566706&438.3903018&1.01442447\\
1536&574.3846199&580.4572551&1.01057242\\
3072&741.2231221&743.2821499&1.00277788\\
4000&802.9912333&802.2809153&0.99911541
\end{array}
\]

The parity mismatch shrinks from about 1.44 percent at N=768 to about

\[
\boxed{8.85\times10^{-4}}
\]

relative at N=4000.

The difference changes sign between 3072 and 4000:

\[
A_{o,3072}-A_{e,3072}\approx2.0590,
\]

\[
A_{o,4000}-A_{e,4000}\approx-0.7103.
\]

Thus the data do not support a one-sided parity inequality; they support convergence toward a common leading coefficient with an oscillatory subleading difference.

---

## 5. Theorem-scale raw coefficients [N]

At the N=4000 theorem-scale cutoff,

\[
C_e
\approx
7.57730075636926\times10^{-30},
\]

\[
L_e
\approx
1.0294331258567363\times10^{16},
\]

giving

\[
\boxed{
C_eL_e^2\approx802.9912333068.
}
\]

For odd parity,

\[
C_o
\approx
2.18452398382966\times10^{-25},
\]

\[
L_o
\approx
-6.060170207673761\times10^{13},
\]

giving

\[
\boxed{
C_oL_o^2\approx802.2809152753.
}
\]

The raw L coefficients differ by more than two orders of magnitude, but the energy-normalized squared amplitudes nearly coincide.

That is the projective cancellation expected by v14.009.

---

## 6. Direct remote-row checks [N]

For even parity at N=4000, the ratios

\[
\frac{n\,r_n}{L_e}
\]

at remote modes near 2N, 4N, 8N are approximately

\[
0.8716,\quad0.9612,\quad1.0119.
\]

For odd parity they are

\[
0.9717,\quad1.0090,\quad0.9725.
\]

The residual rows therefore have the predicted 1/n scale and leading coefficient, with bounded arithmetic oscillations still visible at these finite distances.

At the earlier cutoffs the same direct checks approach the predicted coefficient as the remote evaluation point is moved outward.

---

## 7. Connection to the v14.009 normalized tail [I]

v14.009 shows

\[
\frac{q_\infty}{q_N}
=
\frac{1+\eta_{o,N}}{1+\eta_{e,N}},
\qquad
\eta_{p,N}=C_{p,N}H_{p,N}.
\]

If the remote Schur inverse has a parity-common leading asymptotic kernel, then the leading contribution to eta_p is proportional to

\[
C_{p,N}L_{p,N}^2=A_{p,N}.
\]

The observed convergence

\[
A_{o,N}/A_{e,N}\to1
\]

is therefore direct numerical evidence that the leading normalized tail correction is common-mode and cancels in

\[
\eta_{o,N}-\eta_{e,N}.
\]

This does not yet prove the required remote Schur asymptotic.

---

## 8. Result

The finite source solutions exhibit a strong projective parity matching in their leading remote tails:

\[
\boxed{
C_eL_e^2
\approx
C_oL_o^2
}
\]

with only 8.85e-4 relative mismatch at N=4000.

Combined with v14.009, this identifies a sharply localized analytic target:

1. prove the remote Schur inverse has a parity-common leading kernel;
2. prove or enclose the common limit of C_pL_p^2;
3. control only the subleading parity difference.

The large separate tail corrections need not be certified sharply if their common leading term is cancelled before absolute values are taken.

---

HANDOFF
target: sandbox
type: payload
parent: v14.010
status: open
action: Use the measured sequence C_e L_e^2 versus C_o L_o^2 as the numerical target/check for the v14.009 analytic normalized-tail calculation; determine whether the leading remote Schur term is provably parity-common and whether its coefficient can be expressed from the unit-energy boundary trace.
deliverable: theorem-or-obstruction
constraints: This supplements rather than replaces the v14.009 handoff; do not promote the apparent common limit from numerics alone; retain oscillatory prime/subleading terms explicitly.
