#!/usr/bin/env python3
"""High-precision small-cutoff spectrum of the source-faithful even-v Suzuki matrix.

Purpose: distinguish the four machine-zero binary64 eigenvalues from genuine
small positive finite-cutoff levels.  Uses mpmath throughout, the canonical
source-faithful formulas, the five q=2,3,4,5,7 prime-power channels, and the
full even PSD cosh pole.

This is a numerical precision diagnostic only.  It does not certify the signs
of the infinite operator, prove exact kernels, RH, or GRH.
"""
from __future__ import annotations
import mpmath as mp

QS=(2,3,4,5,7)
VM=(2,3,2,5,7)


def h(t):
    if t == 0: return mp.mpf('0.25')
    return mp.e**(-t/2)/(1-mp.e**(-2*t))-1/(2*t)


def build(stop: int, dps: int=80):
    mp.mp.dps=dps
    modes=list(range(1,stop+1,2))
    ells=[mp.log(q) for q in QS]
    weights=[mp.log(vm)/mp.sqrt(q) for vm,q in zip(VM,QS)]
    H=[]; D=[]; Si=[]; cusp=[]; P=[]; Pd=[]
    for n in modes:
        k=mp.mpf(n)*mp.pi/2
        H.append(mp.quad(lambda t:h(t)*mp.sin(k*t),[0,1,2]))
        D.append(-mp.quad(lambda t:h(t)*((2-t)*mp.cos(k*t)+mp.sin(k*t)/k),[0,1,2]))
        si=mp.si(mp.mpf(n)*mp.pi); ci=mp.ci(mp.mpf(n)*mp.pi)
        Si.append(si)
        cusp.append(mp.log(mp.mpf(n)/4)-ci-si/(mp.mpf(n)*mp.pi))
        P.append(mp.fsum(w*mp.sin(mp.mpf(n)*mp.pi*ell/2) for w,ell in zip(weights,ells)))
        Pd.append(-mp.fsum(w*((2-ell)*mp.cos(k*ell)+mp.sin(k*ell)/k)
                            for w,ell in zip(weights,ells)))

    N=len(modes); A=mp.matrix(N)
    for i,m in enumerate(modes):
        km=mp.mpf(m)*mp.pi/2
        cm=2*km*mp.cosh(mp.mpf('0.5'))/(km*km+mp.mpf('0.25'))
        for j,n in enumerate(modes):
            if i == j:
                val=cusp[i]+Pd[i]+D[i]
            else:
                Zm=2*P[i]+Si[i]+2*H[i]
                Zn=2*P[j]+Si[j]+2*H[j]
                val=-(mp.mpf(2)/mp.pi)*(mp.mpf(n)*Zm-mp.mpf(m)*Zn)/(mp.mpf(n*n-m*m))
            kn=mp.mpf(n)*mp.pi/2
            cn=2*kn*mp.cosh(mp.mpf('0.5'))/(kn*kn+mp.mpf('0.25'))
            A[i,j]=val+2*cm*cn
    return A


def spectrum(stop,dps=80):
    A=build(stop,dps)
    ev,_=mp.eigsy(A)
    return [ev[i] for i in range(min(6,len(ev)))]


def report():
    for stop in (19,29,39,49,59,69):
        ev=spectrum(stop,80)
        print('M =',stop)
        for i,x in enumerate(ev,1):
            print('  lambda_%d ='%i,mp.nstr(x,30))

    # Precision-doubling regression at M=39.
    e80=spectrum(39,80)
    e100=spectrum(39,100)
    for a,b in zip(e80[:4],e100[:4]):
        assert abs(a-b) < mp.mpf('1e-45')
    assert all(x>0 for x in e100[:6])
    print('PASS: M=39 tiny levels are positive and stable under 80->100 dps replay')
    print('GUARDRAIL: finite-cutoff midpoint/precision diagnostic only')


if __name__=='__main__':
    report()
