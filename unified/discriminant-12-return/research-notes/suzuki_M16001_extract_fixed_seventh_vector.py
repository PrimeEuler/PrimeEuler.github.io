#!/usr/bin/env python3
"""Extraction-only helper: print a binary64 seventh direction for later freezing.

The vector is chosen from the shifted-nominal M16001 anisotropic calculation:
it is the low-core 10-vector corresponding to the largest eigenvector of the
remote/far-corrected unresolved 4x4 block.  This script is NOT a certificate.
Its only purpose is to emit a deterministic binary64 payload which a subsequent
certificate will hard-code, removing SVD/eigensolver arithmetic from the proof.
"""
import math, numpy as np
from suzuki_M16001_even_index3_shifted_nominal_target import finite_solve_shifted, DELTA_REMOTE_SHIFTED
from suzuki_M16001_even_index3_anisotropic_tail_split import (
    Q_HEX,L0_HEX,fmat,remote_gram,far_moments,block_far_bound)

def main():
    modes,Z,c,X,S=finite_solve_shifted()
    Q=fmat(Q_HEX); L0=fmat(L0_HEX)
    _,_,vh=np.linalg.svd(Q.T,full_matrices=True); N=vh[6:].T
    P=Q@np.linalg.inv(L0.T); B10=np.column_stack([P,N])
    G,W,p=remote_gram(B10,modes,Z,c,X)
    L,B,C=far_moments(W,p,Z,modes)
    fN=block_far_bound(L,B,C,slice(6,10))
    A=np.block([[P.T@S@P,P.T@S@N],[N.T@S@P,N.T@S@N]])
    M=(A-G/DELTA_REMOTE_SHIFTED); M=(M+M.T)/2
    FN=M[6:,6:]-fN/DELTA_REMOTE_SHIFTED*np.eye(4)
    ew,ev=np.linalg.eigh(FN); y=ev[:,-1]
    v=N@y; v=v/np.linalg.norm(v)
    # Canonical sign: largest-magnitude component positive.
    if v[np.argmax(np.abs(v))] < 0: v=-v
    print('FN largest eigenvalue =',repr(float(ew[-1])))
    print('Q^T v diagnostic norm =',repr(float(np.linalg.norm(Q.T@v))))
    print('v norm =',repr(float(np.linalg.norm(v))))
    print('FROZEN_V_HEX = (')
    for x in v: print('    %r,'%float(x).hex())
    print(')')

if __name__=='__main__': main()
