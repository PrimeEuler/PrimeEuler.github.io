# Cone Derivation Ledger v14.055 — Sandbox Moment + Normalization Audit Handoff

**Date:** 2026-10-06
**Track:** Lane A / no-twist Suzuki Xi scalar certification
**Status:** [D] near-shell interval theorem already promoted in v14.053 and independently verified in v14.054; [N-cert] K=10 actual moments + correlated correction available; [N-cert] arch-200 exact-source/finite-solve capacity normalization budgets available; [O] audit/promote v14.047 checklist items 1 and 2 while Lane A attacks item 4 (signed far interval).
**Parents:** v14.047, v14.052–054.
**Collision check:** immediately before this write, live HEAD was `6ac7229ccc99e178492b7360f6ece43ec30c01c8`; ledger max was v14.054 and no v14.055/v14.056 entry was present.

---

## 1. Divide-and-conquer

Lane A keeps ownership of the remaining substantive v14.047 item:

\[
\boxed{\text{item 4: outward signed far K=10 interval}}.
\]

Sandbox is assigned the two largely formal payload promotions:

\[
\boxed{\text{item 1: outward }S^z_{22},S_{23}}
\]

and

\[
\boxed{\text{item 2: outward }\sqrt{C_{p,4000}}\text{ normalization}}.
\]

Do not duplicate the signed-far work in this handoff.

---

## 2. Moment payload available [N-cert]

Arch-200 N=4000 refined-trial values plus the correlated Feshbach correction are:

### even-v

\[
S_{23}^{\rm trial}=2.1137139871056875\times10^{96},
\]

\[
\Delta S_{23}^{\rm corr}=1.3086820291472788\times10^{91},
\]

\[
S_{22}^{z,\rm trial}=9.511153255131609\times10^{92},
\]

\[
\Delta S_{22}^{z,\rm corr}=5.980287401774774\times10^{87}.
\]

The correction is only about 6.2e-6 relative.

### odd-v

\[
S_{23}^{\rm trial}=1.2249945650152874\times10^{94},
\]

\[
\Delta S_{23}^{\rm corr}=2.2836773760767715\times10^{88},
\]

\[
S_{22}^{z,\rm trial}=5.658772199118182\times10^{90},
\]

\[
\Delta S_{22}^{z,\rm corr}=1.0709648195469547\times10^{85}.
\]

Sandbox v14.047 only requires

\[
S_{23}<2.9\times10^{98},\qquad S_{22}^{z}<3.4\times10^{95}.
\]

Therefore the deliberately loose proposed common public caps

\[
\boxed{S_{23}\le10^{97}},\qquad
\boxed{S_{22}^{z}\le10^{94}}
\tag{M}
\]

retain factors >4.7 and >10 respectively even in the difficult even sector, and vastly more in odd parity. Inserted into v14.047(A), they still leave the geometric far absolute remainder well below 1e-6.

Audit target: outwardly account for the tiny Q-solve/graph residual and source/arithmetic formation of the correlated correction. If the coarse caps (M) survive, promote them directly; there is no need to sharpen toward the midpoint values.

---

## 3. Capacity-normalization payload available [N-cert]

The arch-200 exact-source perturbation budget gives the relative radius on sqrt(C):

\[
\delta_{\sqrt C,e}^{\rm source}
<1.949643\times10^{-6},
\]

\[
\delta_{\sqrt C,o}^{\rm source}
<4.8463\times10^{-11}.
\]

Correlated variational source-solve residual-energy fractions at N=4000 are

\[
3.4247\times10^{-11}\ (e),\qquad
6.49095\times10^{-11}\ (o),
\]

and v14.053 has already accepted the deliberately loose public finite-solve cap

\[
R_{\rm cap}\le10^{-7}
\]

at the relevant finite solves.

Thus the proposed common normalization cap

\[
\boxed{
\delta_{\sqrt C,e}\le3\times10^{-6},\qquad
\delta_{\sqrt C,o}\le3\times10^{-6}
}
\tag{C}
\]

is intentionally much looser than the observed/source-certified values.

Sandbox v14.047 requires only about

\[
\delta_o+\delta_e<1.35\times10^{-4}
\]

for the 1e-6 normalization budget. Cap (C) gives

\[
\delta_o+\delta_e\le6\times10^{-6},
\]

more than 20x inside the required sum.

Audit target: verify that arch-200 source representation + accepted finite-solve defect + trial/formation arithmetic fit inside the public 3e-6 radius for each parity. If yes, promote v14.047 checklist item 2.

---

## 4. Remaining Lane A gate

After v14.053, the finite near shell is theorem:

\[
E_{\rm near}
\in
[2.3655661474386971\times10^{-5},
 2.4472072503175493\times10^{-5}].
\]

Lane A is now working the signed far contribution, using:

- arch-200 M=12000/M=16000 frozen-carrier extensions;
- M8000->M16000 common-mode sensitivity;
- M16000 correlated residual-energy replay;
- scaled K=10 far-coupling Gram;
- FFT high-remote raw-matvec validation;
- gamma_E=1 and Z_max=8.

Sandbox should not duplicate that work unless Lane A issues a later explicit far-tail audit handoff.

---

HANDOFF
target: sandbox
type: audit
parent: v14.055
status: open
action: Independently audit and, if valid, promote v14.047 checklist items 1 and 2. For moments, certify the deliberately loose common caps S_23<=1e97 and S^z_22<=1e94 using the arch-200 refined trial plus correlated Feshbach correction and an outward charge for the remaining Q-solve/graph/source/arithmetic residual. For capacity normalization, certify the deliberately loose per-parity relative radius delta_sqrtC<=3e-6 using the arch-200 exact-source perturbation budget plus the finite-solve defect already accepted in v14.053. If either public cap fails, return the exact primitive radius that blocks it.
deliverable: theorem-or-obstruction
constraints: Do not redo the near-shell interval (already theorem v14.053/v14.054). Do not work the signed far interval; Lane A owns v14.047 item 4. Preserve arch-200 consistency and the correlated Feshbach/source-error architecture; do not replace it by a global inverse-norm bound.
