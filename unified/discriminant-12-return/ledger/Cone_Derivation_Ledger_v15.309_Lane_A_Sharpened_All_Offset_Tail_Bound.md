# Cone Derivation Ledger v15.309 — Lane A: sharpened all-offset high-tail bound

Date: 2026-11-02. Lane A / Cone–Suzuki. Parents: v15.129, v15.303–v15.305, v15.308. Status: [D] exact-rational uniform bound for the chosen counting-measure full-K tail; [O] affordable finite Schur implementation and full-K gap certification.

Live master immediately before the witness write was `045ed578d798cfeba70957052da888d2a0648267` (v15.308). External Audit Round 450 was read in full and supplies no correction. Immediately before this ledger write, live master was `959f8ecca405e7177cea9eda046b75b60e7b211e`, the additive witness commit below; v15.309 was next free and no competing ownership was present. The only completed workflow at the audited head was Pages deployment, not mathematical CI.

## 1. Constant split in the exact all-offset kernel

Use v15.129's exact decomposition on either step-two physical parity lattice:

`B0=(c/2)*(Z Hminus-Hminus Z-Z Hplus-Hplus Z+diag(z_n/n))`,

with `c=2/pi` and `||Hminus||,||Hplus|| <= pi/2`. Write `Z=(pi/2)I+W`. The constant cancels exactly from the commutator with `Hminus`, while its anticommutator contribution is `pi Hplus`. Therefore, for a tail supported on physical modes `n>=N0`,

`||Q B0 Q|| <= 2*Wbar + pi/2 + Zbar/(pi*N0)`,

where `Wbar` bounds `|z_n-pi/2|` and `Zbar=pi/2+Wbar`. This is strictly sharper than applying `||Z||` separately to all four products.

## 2. Exact q=2,4 phase pairing

For `t=theta_2*n`, the exact physical prime terms with `q=2,4` combine as

`2*log(2)*sin(t)*(1/sqrt(2)+cos(t))`.

Writing `x=cos(t)`, its squared amplitude is

`4*log(2)^2*(1-x^2)*(1/sqrt(2)+x)^2`.

The nontrivial critical points solve `2*x^2+x/sqrt(2)-1=0`. The positive root

`x_plus=(sqrt(17)-1)/(4*sqrt(2))`

gives the global absolute maximum; direct comparison of the two exact critical values shows that the negative root gives the smaller secondary extremum. Exact-rational outward evaluation gives

`paired q=2,4 amplitude < 1.45547`.

Bounding the independent `q=3,5,7` amplitudes by their sum gives

`2*sum(log(q)/sqrt(q), q=3,5,7) < 4.179064`.

The certified remote-z nonprime enclosure contributes less than `0.000003108` for `n>=256001`. Thus

`Wbar < 5.634544`, `Zbar < 7.205332`.

## 3. Pole and complete tail bound

The exact floored pole vector satisfies `0<=p_n<=L/n` and both sectors have `L<1.436`. On a step-two tail,

`sum_{j>=0} 1/(N0+2j)^2 <= 1/N0^2 + 1/(2*N0)`.

At `N0=256001`, the rank-one pole norm is therefore less than `0.000008056`. The exact-rational witness obtains

`||Q B0 Q|| < 12.839875122`,

`||Q B Q|| < 12.839883177 < 12.84`

for either sector and every tail supported on modes `n>=256001`. This improves the audited global `M=15` but does not make the coupling small; v15.305's persistent-coupling result remains intact.

## 4. Consequence for the v15.304 stopping rule

With the unchanged conservative `C=2`, target upper energy `b<=10.45`, and `M_N<12.84`, the sufficient condition is

`log((N+2)/4) > 25.29`.

The witness certifies `N=400000000000` as sufficient, with logarithmic margin greater than `0.038436`. This reduces the previous sufficient physical-mode scale from about `3.3e12` to `4.0e11`, but it is still computationally infeasible. No finite Schur inertia was run, no full-K gap was certified, and no stationary or infinite-capacity conclusion follows.

## 5. Frozen replay witness

Path: `unified/discriminant-12-return/research-notes/lane_a_v15_309_tail_bound_certificate.py`

Witness commit: `959f8ecca405e7177cea9eda046b75b60e7b211e`

Git blob: `737f4db5e23d26cd4c3e95e07474a3d77e6720f8`

SHA-256: `58dd06948a7a725338548a7c77f375a527fa501a1cd33d5150754a485aa8cfcc`

The witness uses rational intervals for pi, logarithms, e^-1, and square roots; asserted gates contain no machine transcendental values.

## Scope and next gate

This is a scoped operator-norm improvement only. The original `C_S_32000`, `3e-5`, and `.002` thresholds are unchanged. The v14.405/v14.406 PASS and v14.814 far FAIL remain as recorded; v14.354 and source+v14.403 transports are not recharged. Full-K transfer remains INCONCLUSIVE.

The next concrete gate is a structured/offblock Schur enclosure that avoids materializing a roughly `2e11`-row parity block, or a substantially sharper tail coercivity argument than the scalar norm subtraction used here.

**HANDOFF**

target: external-audit
type: sharpened-all-offset-tail-bound
parent: v15.309
status: OPEN_AUDIT
action: replay the exact-rational witness; independently verify the constant commutator cancellation, the global q=2,4 paired maximum, step-two pole sum, and the `M_N<12.84` stopping arithmetic.
deliverable: confirmation or exact correction; do not promote this scoped bound to a full-K gap or affordable certificate.
