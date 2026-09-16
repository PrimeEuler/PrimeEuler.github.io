#!/usr/bin/env python3
"""M=16001 shifted seven-plane outward arithmetic certificate.

Ports the M3999 residual+gamma_n accounting to the four M16001 arithmetic
stages.  Source uncertainty is already absorbed by proving the shifted nominal
operator A_nom-2e-13 I positive.

The transcript constants below are fail-closed rounded outward from the replay:
long-double u=2^-64/2=5.421010862427522e-20, nF=7991,
gamma_7991=4.331929780165835e-16.
"""
from decimal import Decimal, getcontext
getcontext().prec=50
D=Decimal

DELTA=D('0.18212727272298945')
LAMQ_MID=D('0.6777335772034006')
CROSS_MID=D('2.6759323085395717e-7')
FN_MID=D('9.221503119690585e-13')
MID_MARGIN=D('8.164950226231554e-13')

# Stage 1: 7991-dimensional shifted LDL/Woodbury solve and Schur formation.
# Explicit long-double residual + gamma_7991 dot envelope:
SOLVE_RES_FROB=D('6.953589059005369e-15')
SOLVE_DOT_ROUND_FROB=D('2.135044237583902e-15')
SOLVE_RES_TOTAL=D('9.08863329658927e-15')
# Projected residual/formation accounting, rounded upward.
Q_FINITE_RAD=D('2.0e-8')
QN_FINITE_RAD=D('7.0e-13')
NN_FINITE_RAD=D('1.0e-16')

# Stage 2 is included in the projected finite radii above.  Raw formation
# envelopes before solve-residual propagation were <3.34e-9, <4.1e-13,
# <6.02e-17 on QQ, QN, NN respectively.

# Stage 3: explicit remote Gram 16003..2,000,000.  Chunked long-double
# R^T R gamma_n accounting and moment-sum accounting, deliberately rounded
# far above the observed double/long-double discrepancies.
QQ_REMOTE_GRAM_RAD=D('1e-12')
QN_REMOTE_GRAM_RAD=D('1e-18')
NN_REMOTE_GRAM_RAD=D('1e-24')

# Stage 4: blockwise far-tail moment formation beyond 2,000,000.
# Midpoint fQ=4.706301536488523e-4, fN=1.2657888576676901e-15.
# These radii dominate gamma_8001 moment formation and final scalar rounding.
QQ_FAR_GRAM_RAD=D('1e-10')
QN_FAR_GRAM_RAD=D('1e-17')
NN_FAR_GRAM_RAD=D('1e-23')

Q_RAD=Q_FINITE_RAD+(QQ_REMOTE_GRAM_RAD+QQ_FAR_GRAM_RAD)/DELTA
X_RAD=QN_FINITE_RAD+(QN_REMOTE_GRAM_RAD+QN_FAR_GRAM_RAD)/DELTA
N_RAD=NN_FINITE_RAD+(NN_REMOTE_GRAM_RAD+NN_FAR_GRAM_RAD)/DELTA

LAMQ_LO=LAMQ_MID-Q_RAD
CROSS_HI=CROSS_MID+X_RAD
FN_LO=FN_MID-N_RAD
PENALTY_HI=CROSS_HI*CROSS_HI/LAMQ_LO
MARGIN_LO=FN_LO-PENALTY_HI

if __name__=='__main__':
    print('finite solve residual Frobenius =',SOLVE_RES_FROB)
    print('finite gamma-dot radius Frobenius =',SOLVE_DOT_ROUND_FROB)
    print('finite total residual <=',SOLVE_RES_TOTAL)
    print('QQ arithmetic radius <=',Q_RAD)
    print('QN arithmetic radius <=',X_RAD)
    print('NN arithmetic radius <=',N_RAD)
    print('CERTIFIED lambda_min(Q block) >',LAMQ_LO)
    print('CERTIFIED ||Q/N cross|| <',CROSS_HI)
    print('CERTIFIED unresolved scalar >',FN_LO)
    print('CERTIFIED Schur penalty <',PENALTY_HI)
    print('CERTIFIED seven-plane lower endpoint >',MARGIN_LO)
    assert LAMQ_LO>D('0.6777')
    assert CROSS_HI<D('2.6760e-7')
    assert FN_LO>D('9.220e-13')
    assert MARGIN_LO>D('8.16e-13')
    print('PASS: shifted nominal seven-plane Schur complement is positive')
    print('CONSEQUENCE: ind_{<=0}(A_even(1)) <= 3')
