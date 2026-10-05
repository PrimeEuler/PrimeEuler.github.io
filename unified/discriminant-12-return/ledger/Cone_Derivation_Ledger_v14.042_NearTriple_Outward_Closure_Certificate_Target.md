# Cone Derivation Ledger v14.042 — Near-Triple Outward Closure Certificate Target

**Date:** 2026-10-05
**Track:** Lane A / no-twist Suzuki Xi scalar certification
**Status:** [D] v14.041 closure algebra; [D] rigorous raw near shifted floors; [N-cert] correlation-preserving rank-24 near self-energy budget; [N-cert] full raw near-to-sep cross budget; [N] fail-closed public closure inequality passes with large room; [O] audit/derive the two public finite-arithmetic padding statements before theorem promotion.
**Parents:** v14.033–037, v14.039–041; External Audit Rounds 163–164.
**Research commits:** 51efb4bd2b6f27841153cf2a0b8906c45db09792, 88e4a6de308100280870d6d19c029f3957c4cc83, 5cccd9a48614924460c347cbcd5ec9da7c2731e6, 4c945a6b4743a11a8a114a3974b7887c6be70279, b826b3fb90106357037ac5fd0b56b4e317ec7b97, 8ff2153903eaca39c575a6d1cebce31ea8d59532, a8232884e21e8cc4476bfb3e4357a3b1451c80ff, 8adff10c56fdb5edbebb06115ce70e61bac89fed, 97b400370d9690fe52df08b31f2502ae3b3bb55e, ce6379abe1b13266e6aa8373b7aed5c10171810f.
**Collision check:** immediately before this write, live HEAD was ce6379abe1b13266e6aa8373b7aed5c10171810f and no v14.042 ledger entry was present.

---

## 1. v14.041 consumer

v14.041 reduces the remaining gamma_E=1 gate to

\[
(d_{sn}+\sqrt{0.941\,b_{nn}})^2
<
1.3457\,\delta_{nn}.
\tag{1}
\]

Here b_nn=||B_nF^{-1}B_n^*||, A_nn=(D_nn-I)-B_nF^{-1}B_n^* >= delta_nn I, and d_sn=||D_sn||.

---

## 2. Rigorous raw near floor [D]

The N8000 interval certificate proves

\[
D_{nn,e}-I
\succeq
2.9800144235164838344\,I,
\]

\[
D_{nn,o}-I
\succeq
2.9800844016128788246\,I.
\]

These are source-faithful outward interval bounds.

---

## 3. Correlated near self-energy target [N-cert]

A rank-24 SVD of the exact nominal front-to-near coupling is passed through the same frozen-six-plane LDDD/Feshbach architecture audited in v14.033/v14.034. The low-rank main Gram and explicit residual energy give

\[
b_{e}^{\rm mid,target}<0.289607180784709,
\qquad
b_{o}^{\rm mid,target}<0.255780876375452.
\]

The target residuals after one LDDD refinement are 1.85e-20 even and 2.34e-20 odd; graph residuals are 2.91e-28 even and 1.50e-27 odd.

Consume the already-audited v14.033 exact-front quadratic-form inflation 1.02 and reserve a public production/SVD/source-formation allowance 0.005. Then

\[
1.02(0.289607180784709)+0.005<0.3014<\boxed{0.31},
\]

\[
1.02(0.255780876375452)+0.005<0.2660<\boxed{0.27}.
\]

Thus the proposed public caps are

\[
\boxed{b_{nn,e}\le0.31,\qquad b_{nn,o}\le0.27}.
\tag{2}
\]

Before promotion, the 0.005 allowance must be tied explicitly to the existing primitive gamma_k/source-radius transcripts or independently audited.

Combining (2) with the rigorous raw floors gives proposed outward near floors

\[
\boxed{\delta_{nn,e}>2.67001442351648},
\]

\[
\boxed{\delta_{nn,o}>2.71008440161287}.
\tag{3}
\]

---

## 4. Full raw cross target [N-cert/D]

The source-faithful near-to-infinite-sep cross diagnostic uses:

- exact adjacent band through 32000 compressed by rank-12 SVD;
- a 17-feature inverse-power/pole low-rank representation through 1e6;
- an analytic completion beyond 1e6.

The midpoint low-rank-core-plus-near-residual values are

\[
0.9772424085368333\quad(e),
\qquad
0.8437524725666780\quad(o).
\]

For the omitted inverse-power remainder on 32000<=n<1e6, with |z|<=8 and m/n<=1/2,

\[
\|R_{\rm geom}\|_{HS}
\le
\frac{64}{3\pi}
\left(
\sqrt{\sum m^{34}\sum n^{-36}}
+
\sqrt{\sum m^{32}\sum n^{-34}}
\right)
<1.64\times10^{-6}.
\]

Consume the public cap 2e-6.

For n>=1e6, using only |z|<=8, the exact pole envelope p_n<=4g/(pi n), and same-parity power-sum integral bounds gives

\[
\boxed{\|D_{sn}^{n\ge10^6}\|<0.230}.
\]

Reserve a deliberately large 0.02 finite source/arithmetic allowance on the low-rank core. This yields

\[
0.977242409+0.020+0.000002+0.230<\boxed{1.25}\quad(e),
\]

\[
0.843752473+0.020+0.000002+0.230<\boxed{1.20}\quad(o).
\tag{4}
\]

A z-only interval audit over the entire 8k–32k cross band is queued to replace the source portion of this 0.02 allowance by an explicit scalar radius. Before promotion, the remaining floating accumulation portion of the 0.02 allowance must be tied to primitive gamma_k bounds or independently audited.

---

## 5. Fail-closed closure arithmetic [N]

Insert (2)–(4) into (1).

### even

\[
\delta_{nn,e}>2.67001442351648,
\]

\[
\mathrm{LHS}_e
\le
(1.25+\sqrt{0.941\cdot0.31})^2
=
3.204464605620732,
\]

\[
\mathrm{RHS}_e
>
1.3457(2.67001442351648)
=
3.593038409726132.
\]

Hence the provisional outward margin is

\[
\boxed{\mathrm{RHS}_e-\mathrm{LHS}_e>0.38857}.
\]

### odd

\[
\delta_{nn,o}>2.71008440161287,
\]

\[
\mathrm{LHS}_o
\le
(1.20+\sqrt{0.941\cdot0.27})^2
=
2.903798564596207,
\]

\[
\mathrm{RHS}_o
>
1.3457(2.71008440161287)
=
3.646960579250451.
\]

Thus

\[
\boxed{\mathrm{RHS}_o-\mathrm{LHS}_o>0.74316}.
\]

The corresponding closure ratios are <0.892 even and <0.797 odd.

---

## 6. Current verdict

The v14.041 finite triple is no longer numerically marginal. Under the two explicitly isolated finite-arithmetic padding statements, the closure inequality passes with order-0.4/order-0.7 margins.

Do NOT yet promote gamma_E=1 solely from this entry.

The only remaining obligations are:

1. audit/derive the 0.005 rank-24 production allowance;
2. audit/derive the 0.02 low-rank cross-core source/arithmetic allowance (the source part is being replaced by the queued 8k–32k z interval audit);
3. replay the executable fail-closed budget in CI (workflow queued at write time).

Once those are discharged, v14.041 gives

\[
S_{e,4000}\succ I,\qquad S_{o,4000}\succ I,
\]

and therefore the v14.016 Euclidean constant may be taken as

\[
\boxed{\gamma_E=1}.
\]

---

HANDOFF
target: sandbox
type: audit
parent: v14.042
status: open
action: Audit the proposed outward near-triple budget. In particular, determine whether the public 0.005 rank-24 production allowance follows from v14.033/v14.034 primitive residual/source bounds, and whether the 0.02 raw-cross low-rank-core allowance is justified by the historical validated N16003 cross arithmetic model plus the queued 8k–32k z interval audit. If both padding statements are valid, promote the v14.041 inequality and gamma_E=1; otherwise state the exact missing primitive radius.
deliverable: theorem-or-obstruction
constraints: Do not replace the correlated rank-24/Feshbach self-energy by ||F^{-1}||; preserve the exact v14.041 near/far split; consume the rigorous N8000 raw floor, analytic 2e-6 geometric cap, and analytic 0.230 far-tail cap as stated.
