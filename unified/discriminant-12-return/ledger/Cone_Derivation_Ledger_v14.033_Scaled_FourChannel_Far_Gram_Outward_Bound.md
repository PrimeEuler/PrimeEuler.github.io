# Cone Derivation Ledger v14.033 — Scaled Four-Channel Far-Gram Outward Bound

**Date:** 2026-10-05
**Track:** Lane A / no-twist Suzuki Xi scalar certification
**Status:** [D] correct channel-weighted operator consumer; [D] residual/complement outward envelope; [D] exact-source inverse perturbation; [N-cert] three-correction stability replay; **THEOREM:** v14.027 §6(b) four-channel far Schur correction is bounded outward in both parities; [O] only §6(c) geometric remainder remains before gamma_E=1.
**Parents:** v14.024, v14.027, v14.031, v14.032.
**Research/workflow commits:** d46e8baccc7c85738d72a084ffadbf0a1df4817c; 60890be02a9743fde93a9b32134d7a8cecb89db2; b57421a2df7eebb7216c567f9b4de9d665a2cd39; b762867bc07b60de973bc6a56ac04d23972eb5dd; 4dfce4d840a06b897eb2cdec9825bdb122997da3.
**Collision check:** immediately before this write, live HEAD was 4dfce4d840a06b897eb2cdec9825bdb122997da3 and no v14.033 ledger entry was present.

---

## 1. Normalization correction

The raw four-channel coefficient Gram

\[
M_{ij}=\langle w_i,F^{-1}w_j\rangle
\]

is strongly anisotropically scaled. Its raw eigenvalues reach 10^{25} because the higher signed-moment vectors carry powers m^2 and m^3.

Therefore the shorthand raw-basis estimate

\[
\lambda_{\max}(M)\,\|U\|^2
\]

appearing in the criterion discussion of v14.027 is **not** the numerical consumer that reproduces the v14.024 far budgets. In the raw channel basis it is uselessly large.

The load-bearing bound is instead the channel-weighted triangle estimate already used by v14.024:

\[
B_{\rm far}=\sum_{i=1}^4 u_i\otimes w_i,
\]

so

\[
B_{\rm far}F^{-1}B_{\rm far}^*
=
\sum_{i,j}M_{ij}\,u_i\otimes u_j
\]

and hence

\[
\boxed{
\left\|B_{\rm far}F^{-1}B_{\rm far}^*\right\|
\le
\Delta_4
:=
\sum_{i,j}|M_{ij}|\,f_i f_j,
}
\tag{1}

where

\[
f_i\ge\|u_i\|_2
\]

are rigorous same-parity far-lattice norm caps.

Equivalently, (1) is an entrywise absolute bound on the naturally scaled Gram D_f M D_f. This correction changes no structural theorem in v14.027; it specifies the correct normalized numerical consumer.

---

## 2. Midpoint weighted budgets and refinement stability [N-cert]

For n>8000 the four scalar channels are

\[
u_1=n^{-1},\quad
u_2=z_n n^{-2},\quad
u_3=n^{-3},\quad
u_4=z_n n^{-4},
\]

with |z_n|<=8 from v14.025.

The rigorous lattice norms used by the replay satisfy approximately

\[
f_1<0.008,
\quad
f_2<4.6\times10^{-6},
\quad
f_3<5.6\times10^{-11},
\quad
f_4<4.7\times10^{-14}.
\]

The original high-precision shifted-front replay gave

\[
\Delta_{4,e}^{\rm mid}
=
1.2428000003133971099\ldots,
\]

\[
\Delta_{4,o}^{\rm mid}
=
1.1869700135759419654\ldots.
\]

A three-correction replay reduces the target residuals to

\[
7.88\times10^{-8}\quad(e),
\qquad
7.11\times10^{-8}\quad(o),
\]

and returns

\[
1.2428000003133694596\ldots\quad(e),
\]

\[
1.1869700135759422945\ldots\quad(o).
\]

The weighted budgets are therefore stable many orders beyond the precision needed below.

---

## 3. Coarse production-computation enclosure [D]

We intentionally avoid sharp interval inversion of the raw 4x4 Gram.

Scale each finite target vector w_i by its corresponding far norm f_i. Direct power-sum bounds, |z|<=10 on the finite front, and the exact channel formulas give the public uniform bound

\[
\boxed{\|f_i w_i\|_2\le4}
\]

for all four channels in both parities. The individual bounds are in fact approximately 3.22, 0.85, 0.64, 0.37 or smaller.

Use the deliberately loose raw target residual cap

\[
\|R_{w_i}\|\le10^{-6}.
\]

Since max f_i<0.008, every scaled residual is bounded by

\[
\rho_t\le8\times10^{-9}.
\]

With the theorem complement floors from v14.031,

\[
\delta_e=7.795385618610192746\times10^{-6},
\]

\[
\delta_o=3.262507025086259604\times10^{-5},
\]

the complement target energy obeys

\[
h_i\le\frac{16}{\delta_p}.
\]

For an approximate complement solution with residual r,

\[
|b^TD^{-1}r|
\le
\sqrt{h_i}\,\frac{\|r\|}{\sqrt\delta}.
\]

Thus the public single-entry h error caps are

\[
4.1050\times10^{-3}\quad(e),
\qquad
9.809\times10^{-4}\quad(o).
\]

The graph residual is bounded much more tightly by the public cap

\[
\|R_{\rm graph}\|\le10^{-24},
\]

which has thousands of times headroom over the outward LDDD action uncertainty. Consequently

\[
\|\Delta S\|\le\frac{10^{-48}}{\delta_e}<1.3\times10^{-43}
\]

and the induced scaled-target g error is below 6\times10^{-19} even and smaller odd.

Using the protected lower bound from v14.032, the resulting protected inverse perturbation contributes below 10^{-3} per scaled Gram entry. LDDD dot/solve arithmetic is vastly smaller: the same EFT bound as v14.032 applied to the scaled positive magnitude is below 10^{-20}.

Summing all 16 entry charges leaves substantial room inside the public production allowance

\[
\boxed{E_{\rm prod}\le0.15}.
\tag{2}

The executable fail-closed budget records the sharper internal numbers but consumes only (2).

---

## 4. Exact-source passage [D]

The production finite front itself has a global positive floor of at least

\[
\boxed{F_{e,0}\succeq3\times10^{-30}I}
\]

and

\[
\boxed{F_{o,0}\succeq10^{-26}I}.
\]

Indeed v14.032 gives the protected production Schur lower bound after LDDD/residual charges, the frozen carrier satisfies ||P^*P-I||<10^{-12}, and the graph correction has ||Y||<0.11 from ||W||_F^2<6.01 and P^*Y approximately zero. The standard triangular Schur congruence then loses less than a factor (1.12)^2; the displayed floors are conservative.

The full scalar interval audit gives exact-source operator radii

\[
\epsilon_{F,e}<3.01\times10^{-32},
\qquad
\epsilon_{F,o}<7.51\times10^{-33}.
\]

Hence

\[
F_{\rm exact}
\succeq
(1-\theta)F_0
\]

with

\[
\theta_e<0.01004,
\qquad
\theta_o<7.51\times10^{-7}.
\]

Thus exact inverse quadratic forms inflate by at most

\[
1.01014\quad(e),
\qquad
1.000000752\quad(o).
\]

We consume the common public cap

\[
\boxed{1.02}.
\tag{3}

The scalar interval radii also imply ||f_i Delta w_i||<10^{-35} for every scaled channel; their direct target-vector contribution is negligible compared with (2).

---

## 5. Outward four-channel theorem

Combining (2) and (3) gives the coarse exact budgets

\[
\Delta_{4,e}^{\rm exact}
<
1.02\left(1.2428000003133972+0.15\right)
=
1.42065600032\ldots,
\]

\[
\Delta_{4,o}^{\rm exact}
<
1.02\left(1.1869700135759420+0.15\right)
=
1.36370941385\ldots.
\]

For a simple public theorem cap we inflate the midpoint by 50%:

\[
\boxed{
\Delta_{4,e}
\le
1.864200000470096,
}
\]

\[
\boxed{
\Delta_{4,o}
\le
1.780455020363913.
}

The rigorous raw far floors from v14.024 are

\[
3.2867753186523356094\quad(e),
\qquad
3.2869152822833307687\quad(o).
\]

After the mu=1 shift, the available floors are 2.28677531865 and 2.28691528228. Therefore, before the geometric remainder,

\[
\boxed{
m_e
>
0.422575318182240,
}
\]

\[
\boxed{
m_o
>
0.506460261919418.
}

Thus v14.027 §6(b), the outward four-channel far Schur correction, is closed.

---

## 6. Remaining gamma_E obligation

Only v14.027 §6(c) remains: outward enclosure of the high-order geometric remainder beyond the four retained channels.

v14.020/v14.022 already place its midpoint l2 scale near 10^{-10} at n>8000, versus the order-0.4 margins above. Hence enormous inflation remains available, but the required moment intervals must still be stated outwardly before gamma_E=1 is promoted.

---

HANDOFF
target: sandbox
type: audit
parent: v14.033
status: open
action: Independently audit the scaled four-channel far-Gram theorem. Verify the normalization correction from raw lambda_max(M) to the channel-weighted bound Delta4=sum |Mij| f_i f_j, the public scaled target norm <=4 and residual/error envelope, the finite-front exact-source inverse inflation <=1.02, and the final 1.5x public Gram caps. Confirm whether v14.027 §6(b) is rigorously closed.
deliverable: theorem-or-obstruction
constraints: Preserve the channel scaling; do not use raw lambda_max(M) in the unscaled moment basis; consume v14.032 finite-front positivity and v14.031 complement floors; leave the geometric remainder §6(c) separate.
