# Cone Derivation Ledger v13.634 — Four-Term Magnetic Endpoint Residual-Order Audit

Date: 2026-09-21

## 0. Collision and relevance check

The live ledger advanced while this gate was being prepared: v13.632 is External Audit Round 67 and v13.633 is chi_-4 homotopy work. Round 67 independently confirmed the v13.630 g^7/g^8 Floquet coefficients and endpoint series using high-precision ODE/Richardson and an independent symbolic reconstruction. The residual-test reproducer then collided with the newly occupied v13.633 filename tag, so this ledger entry is intentionally v13.634. Live head was rechecked immediately before commit.

## 1. Test

Subtract all four known phase terms
[
R_phi=
Deltaphi_j-
left(c_1epsilon+c_3epsilon^3+c_5epsilon^5+c_7epsilon^7ight)
]
and all four known inversion terms
[
R_P=
(1-P_j^{inv})-
left(d_2epsilon^2+d_4epsilon^4+d_6epsilon^6+d_8epsilon^8ight).
]

The v13.630 prediction is
[
oxed{R_phi=O(epsilon^9)},qquad
oxed{R_P=O(epsilon^{10})}.
]

## 2. High-precision exact dynamics

The reproducer uses 70-decimal-digit mpmath evolution of the original time-dependent spin-1/2 Hamiltonian, rather than the Floquet approximation, at epsilon=.20,.10,.05. The higher-j quantities are lifted by the exact SU(2) symmetric-power identities.

The normalized residuals stabilize to finite constants as epsilon is halved. Representative asymptotic values are

[
{R_phioverepsilon^9}	o
-7.64	imes10^{-7},j,
]
with the expected exact linear scaling in j, while
[
{R_Poverepsilon^{10}}
]
approaches finite j-dependent constants of order 10^{-6}. Raw residual ratios under epsilon -> epsilon/2 approach 2^-9 and 2^-10 respectively.

This directly tests the remainder orders after all four analytically fixed terms have been removed; no coefficient is refit in this audit.

## 3. Decision

The exact time-dependent evolution supports
[
oxed{
Deltaphi_j=
c_1epsilon+c_3epsilon^3+c_5epsilon^5+c_7epsilon^7+O(epsilon^9)
}
]
and
[
oxed{
1-P_j^{inv}=
d_2epsilon^2+d_4epsilon^4+d_6epsilon^6+d_8epsilon^8+O(epsilon^{10})
}.
]

Together with External Audit Round 67's independent confirmation of the underlying v13.630 coefficients, this closes the requested four-term residual-order gate.

## 4. Reproducer

`research-notes/magnetic_driver_fourterm_residual_order_v13_633.py`

The filename retains the version tag assigned when the script was created; v13.633 became occupied by the parallel chi_-4 ledger before this ledger entry was committed. The authoritative ledger version for this gate is v13.634.

## 5. Guardrails

This is a high-precision numerical asymptotic-order certification, not a rigorous analytic remainder bound. It applies to fixed j and the same bare-resonance stroboscopic endpoint protocol. No epsilon^9 phase or epsilon^10 inversion coefficient is promoted here.
