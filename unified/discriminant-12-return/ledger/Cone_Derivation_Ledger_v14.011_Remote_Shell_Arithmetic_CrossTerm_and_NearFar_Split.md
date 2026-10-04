# Cone Derivation Ledger v14.011 — Remote-Shell Arithmetic Cross Term and the Near/Far Split

**Date:** 2026-10-04
**Track:** Lane A / no-twist Suzuki Xi scalar certification
**Status:** [D] exact nested finite-shell correction and positive feedback decomposition; [N] corrected 180-digit M3072→4000 residual decomposition; [N] first arithmetic subleading term explains most of the one-term overshoot; [N] formal third term is not uniformly improving on the near shell; [G] an earlier 120-digit even-sector replay failed the known-capacity reproduction check and is discarded; [I] certification must split an exact near shell from a separated asymptotic far tail; [O] outward-certify the near-shell relative correction and prove the far-tail remainder after geometric separation.
**Parents:** v14.008–010, v13.989.
**Research commits:** aeefa05158a31325bdfd3bcde955ea09fc234fb8, b88f1843c8749d14144cce3c83117806aed94841, 859e4dd50bdd93a0b8b0d11cea3c57ded375c400, 7df4bcb0ce652f68191bf814fa3142eb5f864838, 8d0524c31f9aeb4dc8a8f539ec2aa120839c8d56, f9afe2b22dad9f2be19a1d3a74105ca4a34b5050, 534bebff5a6aee3edd12200753857dcfd7a79dbe, b237bce97b584604e61328bb8c459fa4edfeff05.
**Collision check:** immediately before this write, live HEAD was b237bce97b584604e61328bb8c459fa4edfeff05; no v14.011 or v14.012 ledger entry was present.

---

## 1. Exact nested finite-shell identity [D]

Let a positive finite section at cutoff M be partitioned into retained modes through N and the new shell Q=(N,M]:

\[
T_M=
\begin{pmatrix}
A&B^*\\
B&D
\end{pmatrix},
\qquad
f_M=\binom{f_N}{f_Q}.
\]

Let

\[
x_N=A^{-1}f_N,
\qquad
G_N=f_N^*A^{-1}f_N,
\]

and define the shell Galerkin residual

\[
\boxed{
r=f_Q-Bx_N.
}
\]

With shell Schur complement

\[
S=D-BA^{-1}B^*,
\]

the exact energy increment is

\[
\boxed{
G_M-G_N=r^*S^{-1}r.
}
\]

Hence the normalized finite-shell correction is

\[
\boxed{
\eta_{N\to M}
=
C_N(G_M-G_N)
=
\frac{C_N}{C_M}-1.
}
\]

This is exactly the finite-section quantity entering the v14.009 quotient identity.

---

## 2. Exact remote self-energy plus retained feedback [D]

Because

\[
S=D-BA^{-1}B^*\preceq D,
\]

we have

\[
\boxed{
r^*D^{-1}r\le r^*S^{-1}r.
}
\]

Equivalently, using the complementary Schur/Woodbury identity, define

\[
y=B^*D^{-1}r,
\qquad
T=A-B^*D^{-1}B.
\]

Then

\[
\boxed{
r^*S^{-1}r
=
r^*D^{-1}r
+
y^*T^{-1}y.
}
\]

The second term is positive retained-section feedback.

This identity separates the remote theorem into two natural consumers:

\[
\boxed{\text{standalone remote self-energy}}
\quad+\quad
\boxed{\text{positive retained feedback energy}}.
\]

---

## 3. Precision guardrail [G]

The first implementation of the full-shell residual decomposition used 120-digit reduced arithmetic. The odd sector remained stable, but the even reconstructed capacity became

\[
1.26\times10^{-23}
\]

instead of the already validated

\[
7.61\times10^{-30}.
\]

That replay is invalid and no parity conclusion from it is retained.

The scripts were changed to 180-digit arithmetic, matching v14.010, and now fail closed unless the reconstructed N=3072 capacity agrees with the frozen LDDD capacity to 1e-8 relative.

The corrected replay reproduces both capacities and the v14.010 remote leading coefficients.

---

## 4. Corrected M3072→4000 exact shell corrections [N]

The nested LDDD capacities give

\[
\eta_e
=
0.0036788620376626156\ldots,
\]

\[
\eta_o
=
0.0036440342214859158\ldots.
\]

Therefore

\[
\boxed{
\eta_o-\eta_e
=
-3.482781617669944\times10^{-5}.
}
\]

This is the exact finite-section parity correction over the N=3072 to M=4000 shell, up to the already stated midpoint/LDDD guardrails.

---

## 5. Actual remote residual decomposition on the standalone shell [N]

Write the actual shell residual as

\[
r=L u+\varepsilon,
\qquad
u_n=1/n.
\]

Then on the standalone shell block D,

\[
r^*D^{-1}r
=
L^2u^*D^{-1}u
+
2L u^*D^{-1}\varepsilon
+
\varepsilon^*D^{-1}\varepsilon.
\]

After multiplication by C_N, the corrected replay gives:

### Even

\[
\eta^{D}_{e,\mathrm{lead}}=0.004277840354752526,
\]

\[
\eta^{D}_{e,\mathrm{cross}}=-0.0009032709701700051,
\]

\[
\eta^{D}_{e,\varepsilon^2}=0.0001770102768913939,
\]

so

\[
\boxed{
\eta^{D}_{e,\mathrm{actual}}
=
0.003551579661473915.
}
\]

This is 96.5402% of the exact even shell correction.

### Odd

\[
\eta^{D}_{o,\mathrm{lead}}=0.004315671467586548,
\]

\[
\eta^{D}_{o,\mathrm{cross}}=-0.0009708804604729537,
\]

\[
\eta^{D}_{o,\varepsilon^2}=0.0001855751480221494,
\]

so

\[
\boxed{
\eta^{D}_{o,\mathrm{actual}}
=
0.003530366155135743.
}
\]

This is 96.8807% of the exact odd shell correction.

Thus the positive retained feedback is only

\[
\eta^{\rm fb}_e
=
0.0001272823761887003
\quad(3.4598\%),
\]

\[
\eta^{\rm fb}_o
=
0.0001136680663501727
\quad(3.1193\%).
\]

---

## 6. Anatomy of the parity difference [N/I]

The leading common-mode contribution alone gives the wrong sign:

\[
\Delta\eta_{\rm lead}
:=
\eta^{D}_{o,\rm lead}-\eta^{D}_{e,\rm lead}
=
+3.783111283402196\times10^{-5}.
\]

The arithmetic cross term contributes

\[
\boxed{
\Delta\eta_{\rm cross}
=
-6.760949030294868\times10^{-5}.
}
\]

The residual-square term contributes

\[
\Delta\eta_{\varepsilon^2}
=
+8.564871130755498\times10^{-6}.
\]

Therefore the standalone actual-residual parity difference is

\[
\boxed{
\Delta\eta_D
=
-2.121350633817187\times10^{-5}.
}
\]

The retained feedback difference is

\[
\boxed{
\Delta\eta_{\rm fb}
=
-1.361430983852757\times10^{-5}.
}
\]

and

\[
\Delta\eta_D+\Delta\eta_{\rm fb}
=
-3.482781617669944\times10^{-5}
=
\Delta\eta_{\rm exact}.
\]

Thus the parity sign is not carried by the common leading 1/n energy. It is created primarily by the correlated arithmetic cross term, with retained feedback supplying the remaining material correction.

---

## 7. Explicit first arithmetic subleading term [D/N]

For remote n above a finite solution supported on modes m≤N, the source-faithful row expands as

\[
\boxed{
r_n
=
\frac{L_N}{n}
-
\frac{2}{\pi}
\frac{z_n}{n^2}
\langle m,x_N\rangle
+
O(n^{-3})
}
\]

for fixed finite N as n→∞.

The second term retains the full arithmetic oscillation z_n.

At N=3072, using this two-term model on the 3072→4000 shell changes the standalone modeled correction from

\[
0.00427784035\to0.00356680331
\]

in the even sector, and

\[
0.00431567147\to0.00358131158
\]

in the odd sector.

Relative to the exact shell correction, this is

\[
96.95\%\quad\text{even},
\qquad
98.28\%\quad\text{odd}.
\]

At the outer edge of the shell, the direct row error improves from about 22.3% to 1.35% even and from 11.9% to 0.66% odd.

Therefore the z_n/n^2 moment term explains essentially all of the gross one-term overshoot.

---

## 8. Why a naive higher-order expansion is not the near-shell proof [N/I]

The formal n^{-3} coefficient is

\[
B_{3,N}
=
f_3
+
\frac{2}{\pi}\langle m^2z,x_N\rangle
+
\alpha\frac{4g}{\pi^3}\langle p,x_N\rangle.
\]

Adding B_3/n^3 moves the modeled shell energy to

\[
98.48\%\quad\text{of exact even},
\]

and

\[
100.44\%\quad\text{of exact odd}.
\]

But it does not improve the pointwise rows uniformly, and the modeled parity difference remains of the wrong sign.

The reason is structural. The geometric denominator expansion

\[
\frac1{n^2-m^2}
=
\frac1{n^2}
\sum_{k\ge0}\left(\frac mn\right)^{2k}
\]

is not uniformly rapidly convergent on the immediate shell n=N+O(1), m≤N, because m/n can be arbitrarily close to 1.

Thus the moment expansion is a valid far-tail tool, but not the correct proof device for the near shell.

---

## 9. Required near/far certification split [I/O]

The remote proof should now be organized with a fixed separation factor c>1, naturally c=2 as a first target:

\[
Q_{\rm near}
=
\{N<n<cN\},
\]

\[
Q_{\rm far}
=
\{n\ge cN\}.
\]

On the near shell:

- evaluate the source-faithful residual without a moment truncation;
- retain arithmetic z_n exactly/outward;
- certify the finite-shell self-energy and retained feedback jointly or by the exact positive decomposition above.

On the far tail:

- m/n≤1/c uniformly;
- the denominator expansion is geometrically controlled;
- keep the leading common-mode 1/n term and the arithmetic z_n/n^2 cross term before taking absolute values;
- bound the remaining geometric series explicitly.

This architecture preserves the parity-sensitive cancellation while avoiding a nonuniform asymptotic expansion at the cutoff boundary.

---

## 10. Consequence for v14.009–010

v14.010 correctly identified the common unit-energy leading amplitude.

The present gate shows why that alone cannot close v14.009:

\[
\boxed{
\text{leading common mode}
+
\text{arithmetic cross term}
+
\text{small positive feedback}
}
\]

must be retained as a correlated package.

An absolute norm bound applied separately to the even and odd leading tails would erase the sign-carrying term.

---

## 11. Result

The N=3072→4000 shell has now been numerically anatomized in a source-faithful way:

1. the actual standalone remote self-energy accounts for about 97% of each exact shell correction;
2. retained-section feedback is positive and only about 3–3.5%;
3. the common leading 1/n term predicts the wrong parity sign;
4. the arithmetic z_n/n^2 cross term is the dominant sign-carrying correction;
5. formal higher moments should only be used after geometric separation from the cutoff.

The next rigorous remote certificate should therefore be a near/far split rather than a single global tail norm.

---

HANDOFF
target: sandbox
type: payload
parent: v14.011
status: open
action: Incorporate the finite-shell parity anatomy into the v14.009/v14.010 analytic task. In particular, preserve the z_n/n^2 cross term and use a near/far split; do not attempt to certify eta_o-eta_e from the common 1/n term alone.
deliverable: theorem-or-obstruction
constraints: Treat the immediate shell without a nonuniform m/n expansion; for the far tail choose a separation c>1 and give an explicit geometric remainder; keep retained feedback as the positive Woodbury term y^*T^{-1}y or an equivalent relative formulation.
