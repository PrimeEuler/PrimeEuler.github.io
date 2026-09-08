#!/usr/bin/env python3
"""Buffer LDL margin audit for the N=155 finite certification target.

The finite buffer is B={21,23,...,153}, dimension 67.  This script uses the
existing exact/1D matrix assembly and reports Cholesky/LDL stability margins.
The purpose is not to call floating Cholesky a proof, but to determine how
coarse an interval entry enclosure could still certify B>0.

For a symmetric approximate buffer matrix A and an entrywise enclosure radius
epsilon, ||E||_2 <= d*epsilon.  Hence a sufficient perturbative certificate is

    lambda_min(A) - d*epsilon > 0.

This converts the observed buffer spectral gap into an explicit target for the
entrywise interval assembly.
"""
from __future__ import annotations

import numpy as np
from suzuki_feshbach_buffer_anatomy import finite_matrix


def audit(arch_order=1200):
    ns,A=finite_matrix(max_n=153,arch_order=arch_order)
    ib=np.where(ns>=21)[0]
    B=A[np.ix_(ib,ib)]
    eig=np.linalg.eigvalsh(B)
    L=np.linalg.cholesky(B)
    d=B.shape[0]
    gap=float(eig[0])
    # If every symmetric entry is enclosed within eps, ||E||_2 <= d eps.
    eps_sufficient=gap/(2*d)  # leaves 50% gap margin.
    return {
        'dimension':d,
        'lambda_min':gap,
        'lambda_2':float(eig[1]),
        'cholesky_min_diag':float(np.min(np.diag(L))),
        'entry_radius_for_half_gap':eps_sufficient,
        'condition_2':float(eig[-1]/eig[0]),
    }


if __name__=='__main__':
    print(audit())
    print('floating audit only; eps target is a perturbative certification design value')
