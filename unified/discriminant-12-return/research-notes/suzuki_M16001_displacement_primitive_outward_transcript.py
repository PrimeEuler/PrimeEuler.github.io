#!/usr/bin/env python3
"""Primitive long-double outward transcript for M16001 displacement entries.

For every off-diagonal entry
  a=-(2/pi)*(n Zi-m Zj)/(n^2-m^2)
this code propagates standard first-order absolute roundoff bounds through the
primitive products, subtraction, division, reciprocal-pi scaling and final
multiplication.  It covers A0_FF and A0_FC.  Diagonal A0_FF entries are payload
values and deliberately excluded: their conversion/provenance is a separate
v13.520 gate.

Input Z and PI are the nominal source payloads.  Source-function uncertainty is
not included here; it is handled by the global shifted-nominal source bound.
"""
import numpy as np
from suzuki_M16001_even_index3_anisotropic_tail_split import source_data_stop, PI

LD=np.longdouble; U=LD(2)**LD(-64)
def g(k):
    ku=LD(k)*U; return ku/(1-ku)

def one(m,z_m,n,z_n,pi):
    # numerator: p=n*z_m, q=m*z_n, num=p-q
    p=n*z_m; q=m*z_n; num=p-q
    ep=g(1)*abs(p); eq=g(1)*abs(q)
    enum=ep+eq+g(1)*(abs(p)+abs(q))
    # denominator: n*n-m*m (integer modes are exactly represented, but charge
    # generic long-double multiply/subtract anyway, hence conservative).
    n2=n*n; m2=m*m; den=n2-m2
    en2=g(1)*abs(n2); em2=g(1)*abs(m2)
    eden=en2+em2+g(1)*(abs(n2)+abs(m2))
    # quotient q0=num/den: input perturbation + one rounded division.
    ad=abs(den)
    if ad<=eden: raise ArithmeticError('denominator enclosure crosses zero')
    quot=num/den
    equot=enum/(ad-eden) + abs(num)*eden/(ad*(ad-eden)) + g(1)*abs(quot)
    # k=2/pi. Charge pi as nominal long-double input and division rounding.
    # Payload-conversion/source radius for pi remains separate; this is the
    # arithmetic charge conditional on the stored nominal pi.
    k=LD(2)/pi
    ek=g(1)*abs(k)
    val=-k*quot
    eval_=abs(k)*equot + abs(quot)*ek + ek*equot + g(1)*abs(val)
    return val,eval_,abs(num),enum,abs(den),eden,abs(quot),equot,abs(k),ek

def scan():
    modes,Z,diag0,c=source_data_stop()
    C=modes[:10].astype(LD); F=modes[10:].astype(LD)
    ZC=Z[:10].astype(LD); ZF=Z[10:].astype(LD); pi=LD(PI)
    stats={k:LD(0) for k in ['entry','num','numrad','den','denrad','quot','quotrad','k','krad']}
    count=0
    def upd(t):
        nonlocal count
        val,rad,an,rn,ad,rd,aq,rq,ak,rk=t; count+=1
        for key,x in [('entry',rad),('num',an),('numrad',rn),('den',ad),('denrad',rd),('quot',aq),('quotrad',rq),('k',ak),('krad',rk)]: stats[key]=max(stats[key],x)
    # FF: exploit symmetry, but visit every ordered off-diagonal entry so the
    # transcript count matches the residual matvec payload.
    for i in range(len(F)):
        m=F[i]; zm=ZF[i]
        for j in range(len(F)):
            if i==j: continue
            upd(one(m,zm,F[j],ZF[j],pi))
    # FC: every 7991 x 10 entry.
    ff_stats=dict(stats); ff_count=count
    fc={k:LD(0) for k in stats}; count0=count
    for i in range(len(F)):
        for j in range(len(C)):
            t=one(F[i],ZF[i],C[j],ZC[j],pi)
            val,rad,an,rn,ad,rd,aq,rq,ak,rk=t
            for key,x in [('entry',rad),('num',an),('numrad',rn),('den',ad),('denrad',rd),('quot',aq),('quotrad',rq),('k',ak),('krad',rk)]: fc[key]=max(fc[key],x)
            count+=1
    print('u =',U)
    print('FF ordered offdiagonal entries =',ff_count)
    for k,v in ff_stats.items(): print('FF max',k,'=',v)
    print('FC entries =',count-count0)
    for k,v in fc.items(): print('FC max',k,'=',v)
    print('FF ENTRYWISE primitive arithmetic radius <=',ff_stats['entry'])
    print('FC ENTRYWISE primitive arithmetic radius <=',fc['entry'])
    return ff_stats,fc

if __name__=='__main__': scan()
