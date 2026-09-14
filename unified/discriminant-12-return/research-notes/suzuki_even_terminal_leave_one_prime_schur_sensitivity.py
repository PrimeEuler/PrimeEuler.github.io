#!/usr/bin/env python3
"""Leave-one-prime Schur sensitivity on the unresolved even Suzuki four-plane.

Diagnostic only.  Uses the source-faithful even-v formulas from
`suzuki_canonical_A0_matrix_assembly.py`, adds the full even PSD pole, freezes
the unresolved four-plane as ker(Q^T) from the exact-dyadic M3999 verifier Q,
and compares:

  * raw low-core prime quadratic forms;
  * the nonlinear finite Schur response after removing one prime channel from
    the entire finite matrix before inversion.

The cutoff ladder 399,799,1599,3999 is included to check stability.  No exact
kernel, sign, RH, or GRH claim follows.
"""
from __future__ import annotations
import math
import numpy as np
from scipy.integrate import quad_vec
from scipy.special import sici
from scipy.linalg import solve, eigvalsh
from suzuki_M3999_frozen_dyadic_Q_L0 import Q_HEX

QS=(2,3,4,5,7)
VM=(2,3,2,5,7)  # von Mangoldt base for q=4 is log 2
ELLS=np.log(np.array(QS,dtype=float))
WEIGHTS=np.log(np.array(VM,dtype=float))/np.sqrt(np.array(QS,dtype=float))


def fmat(H):
    return np.array([[float.fromhex(x) for x in row] for row in H],dtype=float)


def h(t: float) -> float:
    if t == 0.0: return 0.25
    if abs(t) < 1e-7:
        return 0.25-t/48.0-t*t/32.0+7.0*t**3/11520.0
    return math.exp(-t/2.0)/(1.0-math.exp(-2.0*t))-1.0/(2.0*t)


def unresolved_data():
    Q=fmat(Q_HEX)
    _,_,vh=np.linalg.svd(Q.T,full_matrices=True)
    N=vh[6:].T
    core=np.arange(1,20,2,dtype=int)
    R=np.column_stack([(core%12==r).astype(float) for r in (1,5,7,11)])
    V,_=np.linalg.qr(R)
    U,s,_=np.linalg.svd(N.T@V)
    exceptional=N@U[:,-1]
    exceptional/=np.linalg.norm(exceptional)
    return core,N,s,exceptional


def components(stop: int):
    modes=np.arange(1,stop+1,2,dtype=float)
    k=modes*math.pi/2.0
    H,_=quad_vec(lambda t:h(float(t))*np.sin(k*t),0.0,2.0,epsabs=1e-10,epsrel=1e-10)
    D,_=quad_vec(lambda t:-h(float(t))*((2.0-t)*np.cos(k*t)+np.sin(k*t)/k),
                 0.0,2.0,epsabs=1e-10,epsrel=1e-10)
    Si,Ci=sici(modes*math.pi)
    m=modes[:,None]; n=modes[None,:]
    den=n*n-m*m
    np.fill_diagonal(den,1.0)

    cusp=-(2.0/math.pi)*(n*Si[:,None]-m*Si[None,:])/den
    np.fill_diagonal(cusp,np.log(modes/4.0)-Ci-Si/(modes*math.pi))

    arch=-(4.0/math.pi)*(n*H[:,None]-m*H[None,:])/den
    np.fill_diagonal(arch,D)

    primes={}
    for q,w,ell in zip(QS,WEIGHTS,ELLS):
        P=w*np.sin(modes*math.pi*ell/2.0)
        B=-(4.0/math.pi)*(n*P[:,None]-m*P[None,:])/den
        np.fill_diagonal(B,-w*((2.0-ell)*np.cos(k*ell)+np.sin(k*ell)/k))
        primes[q]=B

    c=2.0*k*math.cosh(0.5)/(k*k+0.25)
    pole=2.0*np.outer(c,c)
    return cusp,arch,primes,pole


def schur(A):
    Acc=A[:10,:10]; Acf=A[:10,10:]; Aff=A[10:,10:]
    X=solve(Aff,Acf.T,assume_a='sym')
    S=Acc-Acf@X
    return 0.5*(S+S.T)


def one_cutoff(stop,N,exceptional):
    cusp,arch,primes,pole=components(stop)
    A=cusp+arch+pole+sum(primes.values())
    S=schur(A)
    rows=[]
    for q in QS:
        Sq=schur(A-primes[q])
        raw=N.T@primes[q][:10,:10]@N
        dS=N.T@(Sq-S)@N
        rows.append({
            'q':q,
            'raw_exc':float(exceptional@primes[q][:10,:10]@exceptional),
            'schur_exc':float(exceptional@(Sq-S)@exceptional),
            'raw_4plane_norm':float(np.linalg.norm(raw,2)),
            'schur_4plane_norm':float(np.linalg.norm(dS,2)),
        })
    return eigvalsh(S)[:6],float(exceptional@S@exceptional),rows


def report():
    core,N,pc,exceptional=unresolved_data()
    print('V4 principal cosines =',pc)
    print('exceptional direction =',list(zip(core,exceptional)))
    for stop in (399,799,1599,3999):
        ev,ex,rows=one_cutoff(stop,N,exceptional)
        print('\nM =',stop)
        print('base first six Schur eigenvalues =',ev)
        print('exceptional base Rayleigh =',ex)
        for r in rows:
            print('q={q}: raw_exc={raw_exc:.15g}  schur_exc={schur_exc:.15g}  '
                  'raw4={raw_4plane_norm:.15g}  schur4={schur_4plane_norm:.15g}'.format(**r))

    # M3999 regression guards.
    _,_,rows=one_cutoff(3999,N,exceptional)
    d={r['q']:r for r in rows}
    assert -0.584 < d[2]['schur_exc'] < -0.583
    assert  0.277 < d[3]['schur_exc'] <  0.278
    assert  0.113 < d[4]['schur_exc'] <  0.115
    assert abs(d[7]['schur_exc']) < 1e-7
    assert d[2]['schur_4plane_norm'] > 0.68
    assert d[3]['schur_4plane_norm'] > 0.63
    print('GUARDRAIL: midpoint structural diagnostic only; no theorem promotion')


if __name__=='__main__':
    report()
