#!/usr/bin/env python3
"""M16001 shifted-nominal replay on a completely frozen 10x7 low-core basis.

P (six columns) and v (seventh column) are hard-coded binary64 hex payloads
extracted once from the discovery calculation. No SVD, eigenspace construction,
or L0 inversion is used to define the proof subspace in this replay.

Status: fixed-basis midpoint target only. Outward arithmetic for finite
projection, remote Gram row formation, and far envelopes remains separate.
"""
import math, numpy as np
from suzuki_M16001_even_index3_shifted_nominal_target import finite_solve_shifted, DELTA_REMOTE_SHIFTED
from suzuki_M16001_even_index3_anisotropic_tail_split import remote_gram,far_moments,block_far_bound
H=lambda s: float.fromhex(s)
PHEX=(
('0x1.0891ccd76e086p+9','0x1.6603367d5fc9ap+1','0x1.36ec36c75ec96p-7','-0x1.c3b443affb662p-10','-0x1.3e3586cefa6fbp-12','-0x1.9eee925c47cf8p-10'),
('0x1.7b981394bd925p+10','0x1.0a8ce721412a7p+3','0x1.de350ca886180p-6','-0x1.655e5c98fa56fp-8','-0x1.e93b8d917f321p-11','-0x1.4540f0ce347bap-8'),
('0x1.1f6e474d4b767p+11','0x1.b529a5947f91fp+3','0x1.a4302cc9059d6p-5','-0x1.4e67c68c44787p-7','-0x1.ad34d4d3d35d4p-10','-0x1.29bbb3932e675p-7'),
('0x1.553dc1f38cac9p+11','0x1.2963ddf5196e5p+4','0x1.41444d18e1ec8p-4','-0x1.1e9752654df02p-6','-0x1.41679a33adb79p-9','-0x1.e7a92406e6e62p-7'),
('0x1.3d3e6e8651fdbp+1','-0x1.7638e541d1e69p-6','-0x1.3082c566998c0p-4','0x1.7240df0ba00e9p-3','-0x1.50fea588f4f7bp-1','-0x1.5a16ef24f6b2ap-3'),
('0x1.d43931f7fbbd4p+10','0x1.8aec636180c4dp+4','0x1.6ae7be2f80a39p-3','-0x1.264b822ba5876p-4','-0x1.5b1550c7f1a1ep-7','-0x1.87909bf29c0bap-5'),
('-0x1.0b7fa4cc8f374p+10','0x1.6f09ad669ab7bp+2','0x1.8e6d3ccf61f71p-2','-0x1.40f1d9545b6a2p-1','-0x1.7a97ff1344f7ep-4','-0x1.ddfdb53ea87fbp-3'),
('-0x1.aa639d45f8b77p+10','0x1.c5c0d3abe359cp+4','0x1.775f01844f226p-1','0x1.799831f96bcfep-2','0x1.76b56bc1815ebp-4','-0x1.02c116dec5799p-3'),
('-0x1.ac4135ed32c3fp+10','0x1.871468d83b72cp+5','-0x1.c784cb694f290p-2','-0x1.dbf2016ec95a5p-4','-0x1.6cf31efd31155p-4','0x1.15beef0a12507p-2'),
('0x1.3dfc57f5620e0p+8','-0x1.ad17c84ba0e16p+3','0x1.348bb0df8d4ebp-1','-0x1.531cb4eed8714p-4','-0x1.8f488b65c2754p-3','0x1.0069224443475p-1'))
VHEX=('-0x1.37d40258707bep-3','-0x1.83eb8e2eeeb57p-2','-0x1.95435ae16433ep-2','-0x1.1d704258cf30ap-3','-0x1.ad3f186df2516p-11','0x1.9366e901227c6p-1','-0x1.0d8171aa638a9p-3','-0x1.d8552d7a3c548p-4','-0x1.36c9644d49949p-4','0x1.48f97c9cd9609p-7')
P=np.array([[H(x) for x in r] for r in PHEX]); v=np.array([H(x) for x in VHEX])

def main():
    assert np.linalg.matrix_rank(np.column_stack([P,v]))==7
    modes,Z,c,X,S=finite_solve_shifted(); B7=np.column_stack([P,v])
    G,W,p=remote_gram(B7,modes,Z,c,X); L,B,C=far_moments(W,p,Z,modes)
    fP=block_far_bound(L,B,C,slice(0,6)); fv=block_far_bound(L,B,C,slice(6,7)); fx=math.sqrt(fP*fv)
    A=B7.T@S@B7; M=(A-G/DELTA_REMOTE_SHIFTED); M=(M+M.T)/2
    AP=M[:6,:6]-fP/DELTA_REMOTE_SHIFTED*np.eye(6)
    av=float(M[6,6]-fv/DELTA_REMOTE_SHIFTED)
    b=M[:6,6]; lam=float(np.linalg.eigvalsh(AP)[0])
    cross=float(np.linalg.norm(b)+fx/DELTA_REMOTE_SHIFTED)
    penalty=cross*cross/lam; margin=av-penalty
    print('fixed basis rank =',np.linalg.matrix_rank(B7))
    print('fixed P lower =',lam)
    print('fixed v scalar lower =',av)
    print('fixed P/v cross upper target =',cross)
    print('fixed Schur penalty =',penalty)
    print('fixed seven-plane midpoint margin =',margin)
    print('far P,v,cross =',fP,fv,fx)
    assert lam>.67 and av>9e-13 and cross<2.7e-7 and margin>8e-13
    print('PASS: fixed binary64 seven-plane preserves >8e-13 midpoint target')
    print('OPEN: outward arithmetic on this fixed basis; no theorem promotion')
if __name__=='__main__': main()
