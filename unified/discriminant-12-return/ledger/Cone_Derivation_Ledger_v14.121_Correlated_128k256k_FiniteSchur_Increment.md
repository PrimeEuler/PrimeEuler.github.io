# Cone Derivation Ledger v14.121 — Correlated 128k→256k Finite-Schur Increment Collapses to 6.58e-11

**Date:** 2026-10-07  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [N] Fast fixed-FFT/Feshbach finite-Schur midpoint payload at 256k; [I] the exact finite-octave parity-correlated K increment is only 6.58e-11 despite individual octave increments of 2.15e-7; [O] outward certification and infinite-tail closure remain open.  
**Parents:** v14.095, v14.111, v14.114, v14.119, v14.120.  
**Research commit:** `f69ca656f09760a6a2f0878358935fd1b1366ab4`.  
**Workflow commit:** `ba498da6a8aac06bdf461e205de20ca118450038`.  
**Successful workflow run:** `37635959167`.  
**Collision check:** immediately before this write, live ledger max was v14.120 (External Audit Round 187). v14.121 is next free.

---

## 1. Promoted context

External Audit Round 187 (v14.120) independently reran and promoted:

- through-64k scalar-cap transport;
- through-128k scalar-cap transport;
- full (32k	o64k) bare outward QF certificate
  [
  |Q_{m bare}^{32k	o64k}|
  le7.66163003022406	imes10^{-10};
  ]
- full (64k	o128k) bare outward QF certificate
  [
  |Q_{m bare}^{64k	o128k}|
  le1.932592637896439	imes10^{-10}.
  ]

The corrected frozen-tail architecture v14.114/v14.116 was also independently reviewed and accepted.

---

## 2. Finite 128k midpoint

From the fast frozen-residual payload:

[
K_{e,128k}^{m mid}
=
1.3107986553122965	imes10^{-6},
]

[
K_{o,128k}^{m mid}
=
1.3117232138648390	imes10^{-6}.
]

With

[
C_S=639.8280818315513,
]

[
Q_{128k}^{m mid}
=
K_e-K_o-C_SK_oK_e
=
-2.024682171500376	imes10^{-9}.
]

These are diagnostic midpoint values pending the long LDDD replay.

---

## 3. Fast finite 256k midpoint

The fast paired-Schur replay on the full finite problem through 256k gives:

### even-v

[
K_{e,256k}^{m mid}
=
1.5255518725755883	imes10^{-6},
]

finite raw residual

[
2.3555764299686553	imes10^{-12}.
]

### odd-v

[
K_{o,256k}^{m mid}
=
1.5265422628604304	imes10^{-6},
]

finite raw residual

[
9.538707095926386	imes10^{-12}.
]

Thus

[
Q_{256k}^{m mid}
=
K_e-K_o-C_SK_oK_e
=
oxed{
-2.480434339385278	imes10^{-9}
}.
]

---

## 4. Exact finite-octave correlated increment [N]

By finite block Gaussian elimination,

[
lambda_{p,[128k,256k]}^{m fin}
=
K_{p,256k}^{m fin}
-
K_{p,128k}^{m fin}.
]

At midpoint:

[
lambda_{e,M}^{m mid}
=
2.147532172632918	imes10^{-7},
]

[
lambda_{o,M}^{m mid}
=
2.148190489955914	imes10^{-7}.
]

Individually these are (2.15	imes10^{-7})-scale.

But the parity-correlated difference is

[
oxed{
lambda_{e,M}^{m mid}
-
lambda_{o,M}^{m mid}
=
-6.58317322996258	imes10^{-11}.
}
]

So more than (99.96%) of the octave increment is common-mode.

The corresponding full scalar shift is

[
oxed{
Q_{256k}^{m mid}
-
Q_{128k}^{m mid}
=
-4.55752167884902	imes10^{-10}.
}
]

This is already an order of magnitude below the working (5	imes10^{-9}) infinite-tail transport target.

---

## 5. Dyadic contraction diagnostic

Using the finite 64k values from v14.111,

[
K_{e,64k}^{m mid}
=
8.807633721674243	imes10^{-7},
]

[
K_{o,64k}^{m mid}
=
8.806715372027112	imes10^{-7},
]

the previous octave correlated increment was

[
Deltalambda_{64k	o128k}^{m mid}
=
-1.016393517255635	imes10^{-9}.
]

Therefore

[
rac{
|Deltalambda_{128k	o256k}^{m mid}|
}{
|Deltalambda_{64k	o128k}^{m mid}|
}
=
oxed{
0.06477
}.
]

The parity-correlated increment shrank by about

[
15.4	imes
]

over one dyadic step.

Guardrail: this observed contraction is not yet a theorem and is not extrapolated to infinity.

---

## 6. Active next gate

Lane A has launched the same fast finite-Schur replay through

[
512k.
]

The immediate test is whether

[
Deltalambda_{256k	o512k}^{m mid}
]

continues to contract strongly.

If so, the remaining analytic task becomes sharply targeted: prove a dyadic contraction or a direct signed-moment envelope for the correlated increment, rather than bounding individual tail energies.

---

## 7. Verdict

[
oxed{
	ext{128k→256k individual increments: }2.15	imes10^{-7};
}
]

[
oxed{
	ext{parity-correlated difference: }6.58	imes10^{-11}.
}
]

The current obstruction is therefore not tail size but theorem-grade preservation of common-mode cancellation.

---

HANDOFF
target: sandbox
type: correlated-dyadic-increment
parent: v14.121
status: open
action: Use the exact finite-Schur identity and the observed 64k→128k / 128k→256k correlated increments to look for an analytic dyadic contraction mechanism. Do not extrapolate the numerical ratio as a theorem. Prefer a direct relation for Delta lambda between consecutive dyadic cutoffs, or a K=10/signed-moment bound that preserves parity cancellation.
deliverable: theorem-or-obstruction
constraints: Individual lambda magnitudes are not the target; preserve correlated difference before absolute values. Do not infer the infinite tail from finite stabilization alone.
