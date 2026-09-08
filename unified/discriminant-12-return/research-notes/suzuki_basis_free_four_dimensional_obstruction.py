#!/usr/bin/env python3
"""Basis-free certification criterion for the terminal four-dimensional sector.

Let F be the exact 10x10 effective core and Fhat a numerical approximation with
||F-Fhat|| <= eta.  Weyl gives |lambda_j(F)-lambda_j(Fhat)|<=eta.
If the fifth ordered eigenvalue lambda5(Fhat)>eta, then lambda5(F)>0 and hence
at most four eigenvalues of F can be nonpositive.

This avoids certifying a particular six-dimensional stiff basis.
"""

LAMBDA5_APPROX = 4.33e-8


def positive_fifth_margin(eta: float) -> float:
    return LAMBDA5_APPROX-eta


if __name__=='__main__':
    for eta in (1e-8,2e-8,3e-8,4e-8):
        print(eta, positive_fifth_margin(eta))
    print('criterion: eta < lambda5_approx gives at most four nonpositive directions')
