#!/usr/bin/env python3
"""Grouped leave-one-component Schur sensitivity for the unresolved even four-plane.

Builds on `suzuki_even_terminal_leave_one_prime_schur_sensitivity.py` and asks
how the frozen unresolved four-plane changes when the entire cusp,
archimedean, PSD-pole, or aggregate-prime block is removed *before* the finite
high block is eliminated.

This is midpoint structural diagnostics only.  It does not identify kernels or
prove signs, RH, or GRH.
"""
from __future__ import annotations
import numpy as np
from scipy.linalg import eigvalsh
from suzuki_even_terminal_leave_one_prime_schur_sensitivity import (
    components, schur, unresolved_data, QS
)


def one_cutoff(stop,N,exceptional):
    cusp,arch,primes,pole=components(stop)
    prime_all=sum(primes.values())
    A=cusp+arch+pole+prime_all
    S=schur(A)
    groups={'cusp':cusp,'arch':arch,'pole':pole,'prime_all':prime_all}
    rows={}
    for name,B in groups.items():
        Sl=schur(A-B)
        dS=N.T@(Sl-S)@N
        rows[name]={
            'exceptional_delta':float(exceptional@(Sl-S)@exceptional),
            'fourplane_norm':float(np.linalg.norm(dS,2)),
            'leaveout_eigs':eigvalsh(Sl)[:4],
        }
    return rows


def report():
    _,N,_,exceptional=unresolved_data()
    for stop in (399,799,1599,3999):
        rows=one_cutoff(stop,N,exceptional)
        print('\nM =',stop)
        for name,r in rows.items():
            print(name,
                  'exc_delta=',r['exceptional_delta'],
                  'fourplane_norm=',r['fourplane_norm'],
                  'leaveout_first4=',r['leaveout_eigs'])

    rows=one_cutoff(3999,N,exceptional)
    a=rows['arch']['leaveout_eigs']
    assert np.all(a>1.2e-4) and np.all(a<1.1e-3)
    assert rows['cusp']['leaveout_eigs'][-1] < -0.12
    assert rows['pole']['leaveout_eigs'][0] < -5.3
    assert rows['prime_all']['leaveout_eigs'][0] < -0.58
    print('GUARDRAIL: midpoint structural diagnostic only; no theorem promotion')


if __name__=='__main__':
    report()
