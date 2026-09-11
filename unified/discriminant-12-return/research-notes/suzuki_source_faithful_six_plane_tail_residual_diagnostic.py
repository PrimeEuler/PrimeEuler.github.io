#!/usr/bin/env python3
"""Source-faithful six-plane tail-residual reduction for Suzuki S10.

This checkpoint follows v13.387-v13.390, which restored and independently
re-verified the source-faithful rank-two archimedean formula.

Split the even-v odd-mode basis as

    C = {1,3,...,19},
    F = {21,23,...,M},
    T = {M+2,M+4,...}.

After eliminating F, define

    S_F = A_CC - A_CF A_FF^{-1} A_FC,
    R   = A_TC - A_TF A_FF^{-1} A_FC,
    T_e = A_TT - A_TF A_FF^{-1} A_FT.

Then the exact Schur-of-Schur identity is

    S_infty = S_F - R^* T_e^{-1} R.

Hence if T_e >= delta I and Q has orthonormal columns spanning a candidate
positive core subspace, it suffices to prove

    Q^T S_F Q - delta^{-1} (R Q)^*(R Q) > 0.

For the final split M=16001, the existing source-faithful validated inputs

    A0_FF >= 0.22 I,
    A0_TT >= 4.6732 I,
    ||A0_FT|| < 0.994

give

    delta >= 4.6732 - 0.994^2/0.22.

The full operator A=A0+P_pole has the same lower bound for the effective tail
because adding a PSD operator can only increase a Schur complement in the
variational characterization.

The table below is an ordinary floating-point diagnostic from smaller cutoffs.
For each M, F was eliminated directly, Q was chosen as the eigenvectors 5..10
of the finite S_F, and R was sampled only on the next equal-width odd tail
band. Therefore the displayed delta_crit values are NOT full-tail bounds and
are NOT certificates. They reveal the anisotropic residual geometry that
motivates the six-plane target.

    M      sigma1(R)       sigma2/sigma1      delta_crit(partial)
    199    3.9070542e-1    5.03e-3            0.4702043
    399    3.0397291e-1    2.125e-3           0.3978217
    799    2.3431651e-1    9.117e-4           0.2713112
    1199   2.0109175e-1    5.529e-4           0.2108109

At M=1199 the dominant right singular vector of R has approximate absolute
overlaps

    |<r1,v5>| = 2.13e-5,
    |<r1,v6>| = 1.08e-1,
    |<r1,v7>| = 9.94e-1,
    |<r1,v8>| = 2.0e-2,

so the largest residual channel lands mainly in a large-positive Schur
direction rather than the tiny fifth direction.

Final certification target
--------------------------
Use the actual F={21,...,16001}. Fix a reproducible six-plane Q, enclose
Q^T S_F Q from below, and enclose the full infinite tail Gram

    G_R = (R Q)^*(R Q)

from above with the same source-faithful rank-two/Cauchy tail machinery used in
v13.365. Then verify

    Q^T S_F Q - delta^{-1} G_R > 0.

This is sharper than demanding a uniform ~1e-11 ten-column residual because
the omitted tail enters quadratically and anisotropically.

Guardrail: no finite-band delta_crit in this file is a proof of the full-tail
inequality. No exact-zero, RH, GRH, or final inertia conclusion follows.
"""

FINITE_LOWER = 0.22
TAIL_LOWER = 4.6732
CROSS_UPPER = 0.994
DELTA = TAIL_LOWER - CROSS_UPPER**2 / FINITE_LOWER

DIAGNOSTICS = {
    199:  {"sigma1": 0.39070542, "sigma2_over_sigma1": 5.03e-3,  "delta_crit_partial": 0.4702043},
    399:  {"sigma1": 0.30397291, "sigma2_over_sigma1": 2.125e-3, "delta_crit_partial": 0.3978217},
    799:  {"sigma1": 0.23431651, "sigma2_over_sigma1": 9.117e-4, "delta_crit_partial": 0.2713112},
    1199: {"sigma1": 0.20109175, "sigma2_over_sigma1": 5.529e-4, "delta_crit_partial": 0.2108109},
}

if __name__ == '__main__':
    print('effective-tail lower bound delta >=', DELTA)
    for M, row in DIAGNOSTICS.items():
        print(M, row)
    assert DELTA > 0.182
    print('terminal target: certify Q^T S_F Q - delta^{-1} G_R > 0')
    print('guardrail: partial-tail diagnostics only; no RH/GRH or exact-kernel claim')
