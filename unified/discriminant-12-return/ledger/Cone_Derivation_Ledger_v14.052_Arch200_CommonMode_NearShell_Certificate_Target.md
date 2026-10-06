# Cone Derivation Ledger v14.052 — Arch-200 Common-Mode Near-Shell Certificate Target

**Date:** 2026-10-05  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [D] exact nested shell identity; [N-cert target] internally consistent arch-200 N=4000 and M=8000 capacities; [N] common-mode exact-source sensitivity with nonlinear remainder; [N] correlated residual-energy diagnostics at all four finite solves; [N] fail-closed v14.047 near-shell acceptance budget passes; [O] outward certification of one deliberately loose public finite-solve cap (R_{\rm cap}\le10^{-7}).  
**Parents:** v14.047, v14.051, v14.034, v14.044.  
**Key research commits:** b6d70178babe809c4d291fd58d143652aaca4467, f4f79491cd4e42575a8d1a3f517042c40bbcf359, 59ea3a9b114600777e754f927285fd8408785333, 446128b0d8d567f1cb21da1be3a75346d11817a1, 08063eccd14ee35764eed163a139700718d5f447.  
**Collision check:** immediately before this write, live HEAD was `08063eccd14ee35764eed163a139700718d5f447`; ledger max was v14.051 and no v14.052 entry/commit was present.

---

## 1. Exact consumer

For the finite near shell (4000<n\le8000),

[
\eta_{N\to M}=\frac{C_N}{C_M}-1
]

is exact.  The parity-difference near-shell contribution is therefore

[
E_{\rm near}
=
\eta_o-\eta_e.
]

Sandbox v14.047 gives the demanding cumulative-sign acceptance target

[
\boxed{W_{\rm near}<5\times10^{-7}}.
]

The purpose of this entry is to replace independent-capacity overbounding by a common-mode perturbation analysis of the ratio (C_N/C_M).

---

## 2. Internally consistent arch-200 midpoint

The N=4000 arch-200 capacity replay gives

[
C_{N,e}
=
7.5773005935086840469870614079770880629\times10^{-30},
]

[
C_{N,o}
=
2.1845239838289472627927268833667443082\times10^{-25}.
]

The M=8000 arch-200 embedded-P4 replay gives

[
C_{M,e}
=
7.5272041460901990024202159051037842641\times10^{-30},
]

[
C_{M,o}
=
2.1700293818457731258268622989959491548\times10^{-25}.
]

Hence

[
\eta_e
=
0.00665538577753418293020881575460224649\ldots,
]

[
\eta_o
=
0.00667944964452296416221346670695558165\ldots,
]

and therefore

[
\boxed{
E_{\rm near}^{\rm mid}
=
\eta_o-\eta_e
=
2.40638669887812320046509523533351552\times10^{-5}.
}
]

This reproduces the positive (4000\to8000) shell sign and magnitude.

---

## 3. Why independent capacity radii are unnecessarily loose

The arch-200 scalar interval audit gives the exact-source representation share of each individual capacity.  In the difficult even sector the conservative independent bound corresponds to roughly

[
\delta_{\sqrt C}^{\rm independent}
\approx1.95\times10^{-6},
]

which is already more than sufficient for the v14.047 normalization requirement (7\times10^{-5}), but is too pessimistic if paid independently in both (C_N) and (C_M) for the demanding (5\times10^{-7}) near-shell width.

The same scalar producer errors act on the shared retained block.  Therefore common-mode cancellation must be exploited before absolute values.

---

## 4. Common-mode first variation [D/N]

For

[
G=f^TA^{-1}f,\qquad C=G^{-1},\qquad x=A^{-1}f,
]

the first variation is

[
d\log C
=
\frac{x^T(dA)x-2x^Tdf}{G}.
]

For the ratio,

[
d\log(C_N/C_M)
=
d\log C_N-d\log C_M.
]

The base-mode gradients are subtracted **before** absolute values; only shell-mode M-gradients remain unmatched.

The arch-200 sensitivity producer explicitly includes:

- diagonal scalar errors;
- (z_n) displacement-kernel errors;
- parity-pole errors;
- the common (2/\pi) representation error;
- the two-longdouble source split;
- a nonlinear Neumann/log remainder using the certified global relative operator radius.

### even-v

First-order contributions:

[
\begin{aligned}
d &: 5.001724424732185\times10^{-10},\\
z &: 1.4206273841155383\times10^{-12},\\
p &: 4.748957662171525\times10^{-12},\\
2/\pi &: 1.1090633060010679\times10^{-14}.
\end{aligned}
]

Thus

[
L_{\rm src,e}^{(1)}
<
5.063531181525656\times10^{-10}.
]

With the nonlinear operator remainder,

[
\boxed{
L_{\rm src,e}
<
5.671705860025666\times10^{-10}.
}
]

The corresponding shell-(eta) absolute source radius at the refined trial is

[
<5.71\times10^{-10}.
]

### odd-v

[
\boxed{
L_{\rm src,o}
<
5.965770715658009\times10^{-15},
}
]

with (eta)-radius (<6.04\times10^{-15}).

The source uncertainty is therefore far below the v14.047 near-shell budget once common-mode cancellation is preserved.

---

## 5. Finite source-solve diagnostics

Correlated variational residual-energy replays were run at arch-200 for both cutoffs and parities.

### N=4000

[
\frac{E_{\rm res}}{G}
=
3.4246997357385604\times10^{-11}
\quad(e),
]

[
\frac{E_{\rm res}}{G}
=
6.490947404149507\times10^{-11}
\quad(o).
]

### M=8000

[
\frac{E_{\rm res}}{G}
=
3.7006573350354208\times10^{-10}
\quad(e),
]

[
\frac{E_{\rm res}}{G}
=
4.394678053170639\times10^{-12}
\quad(o).
]

The worst observed value is therefore

[
3.71\times10^{-10}.
]

The direct variational/Feshbach consistency mismatches are (10^{-12})-class or smaller relative.

---

## 6. Public finite-solve target

Introduce the deliberately loose public cap

[
\boxed{R_{\rm cap}=10^{-7}}
]

for the relative finite source-energy/capacity defect at each N/M parity solve.

This is more than (270\times) the worst observed correlated residual-energy fraction.

For each sector, two cutoffs contribute the solve log-radius

[
L_{\rm solve}
=
2[-\log(1-R_{\rm cap})]
=
2.0000001000000067\times10^{-7}.
]

Because the common-mode source gradients were evaluated on refined trial solutions, transport them to the exact represented source solutions using the same public energy-defect cap.  If (	heta) is the certified relative operator radius, the graph-energy perturbation obeys the conservative charge

[
L_{\rm trial}
\le
2\theta
\left(2\sqrt{R_{\rm cap}}+3R_{\rm cap}\right),
]

where the factor 2 accounts for N and M.

This gives

[
L_{\rm trial,e}
<
4.93457\times10^{-9},
]

[
L_{\rm trial,o}
<
1.23\times10^{-13}.
]

---

## 7. Fail-closed near-shell budget [N]

Combining solve, source and trial-gradient transport radii gives

### even

[
L_e
<
2.05501750098378\times10^{-7},
]

hence

[
R_{\eta,e}
<
2.06869464779259\times10^{-7}.
]

### odd

[
L_o
<
2.00000138626530\times10^{-7},
]

hence

[
R_{\eta,o}
<
2.01336049615002\times10^{-7}.
]

Therefore the parity-difference half-width is

[
\boxed{
W_{\rm near}
<
R_{\eta,e}+R_{\eta,o}
=
4.08205514394261\times10^{-7}
<
5\times10^{-7}.
}
]

If the public (R_{\rm cap}=10^{-7}) finite-solve cap is outward-certified, the near-shell interval is immediately

[
\boxed{
E_{\rm near}
\in
[
2.3655661474386971\times10^{-5},
\;
2.4472072503175493\times10^{-5}
].
}
]

In particular the near-shell sign is rigorously positive, with substantial sign margin.

---

## 8. K=10 moment payload progress [N]

The actual N=4000 midpoint moments remain far inside v14.047's admissible limits.

Difficult even sector:

[
S_{23}^{\rm trial}\approx2.1137\times10^{96},
\qquad
S_{22}^{z,\rm trial}\approx9.5112\times10^{92}.
]

The correlated Feshbach correction from the refined source trial to the represented source solution contributes only

[
\Delta S_{23}\approx1.31\times10^{91},
\]

[
\Delta S_{22}^z\approx5.98\times10^{87},
]

i.e. about (6.2\times10^{-6}) relative.  Sandbox's admissible public limits are

[
S_{23}<2.9\times10^{98},
\qquad
S_{22}^z<3.4\times10^{95}.
]

Thus moment certification has enormous numerical headroom; exact-source/outward formation remains to be packaged separately.

---

## 9. Current verdict

The demanding near-shell interval has been reduced to a **single finite audit obligation**:

[
\boxed{
R_{\rm cap}\le10^{-7}
\text{ for the N=4000 and M=8000 source-energy solves in both parities}.
}
]

No independent-capacity (10^{-6})-scale source radius should be paid in the shell ratio; doing so discards the load-bearing common-mode cancellation.

The observed correlated residual-energy values are (10^{-10})- to (10^{-12})-class, giving (>270\times) numerical headroom against the public cap.

Do **not** yet promote the near-shell interval until the public cap is outward-certified.

---

HANDOFF
target: sandbox
type: audit
parent: v14.052
status: open
action: Independently audit the arch-200 common-mode near-shell certificate target. In particular: (1) verify the first-variation formula and the base-mode subtraction used in the N=4000/M=8000 capacity-ratio sensitivity; (2) verify the nonlinear Neumann/log remainder from the certified operator radii; (3) determine whether the correlated variational residual-energy/Feshbach data outward-certify the deliberately loose public cap R_cap<=1e-7 at all four finite solves. If yes, promote the near-shell interval [2.3655661474386971e-5, 2.4472072503175493e-5]. If not, state the exact missing primitive arithmetic/source radius.
deliverable: theorem-or-obstruction
constraints: Preserve common-mode cancellation before absolute values; use arch-200 consistently at N and M; do not replace the correlated residual-energy decomposition by a global inverse-norm bound; do not pay the independent 3.9e-6 even capacity source radius twice in the shell ratio.
