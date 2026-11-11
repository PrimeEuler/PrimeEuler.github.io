#!/usr/bin/env python3
"""Suzuki small-radius positive-polynomial resource probe.

Exhausts every v15.650 candidate arc for R=1,2,3 and evaluates
  ||B|| <= sqrt(||B^2||_infinity).
All arithmetic is binary64: output is orientation/resource evidence only,
NOT an outward certificate and NOT a bound for R=16.
"""
import time
from itertools import combinations, product

import numpy as np
from scipy.sparse import coo_matrix

Q = (2, 3, 4, 5, 7)
V = {2:(1,0,0,0), 3:(0,1,0,0), 4:(2,0,0,0),
     5:(0,0,1,0), 7:(0,0,0,1)}
L = {q:np.log(q) for q in Q}
ALPHA = {q:L[q]/(2*np.sqrt(q)) for q in Q}
L4 = np.array([L[2], L[3], L[5], L[7]])

def saw(x): return 1-np.mod(x, 2)
def D(x, sign, ell): return saw(x-sign*ell)-saw(x)
def G(x, sigma, tau, a, b):
    y = x+sigma*a
    z = x-tau*b
    return (D(y,sigma,a)*D(y,tau,b)
            + D(z,-tau,b)*D(z,-sigma,a))

def assemble(radius, x):
    width = 2*radius+1
    sites = np.indices((width,)*4, dtype=np.int16).reshape(4,-1).T
    h = sites.astype(np.int32)-radius
    field = x+h@L4
    rows=[]; cols=[]; data=[]
    for q,r in combinations(Q,2):
        for sigma,tau in product((-1,1),repeat=2):
            g = np.array([tau*V[r][i]-sigma*V[q][i] for i in range(4)])
            source = sites-g
            mask = np.all((source>=0)&(source<width),axis=1)
            rr = np.flatnonzero(mask)
            cc = np.ravel_multi_index(source[mask].T,(width,)*4)
            # Physical sigma*tau factor retained.  G itself is the v15.420
            # definition, so the Round-530 sigma*tau correction to v15.650's
            # alternate four-corner identity is respected automatically.
            values = (sigma*tau*ALPHA[q]*ALPHA[r]
                      * G(field[mask],sigma,tau,L[q],L[r]))
            rows.append(rr); cols.append(cc); data.append(values)
    return coo_matrix((np.concatenate(data),
                      (np.concatenate(rows),np.concatenate(cols))),
                      shape=(len(sites),len(sites))).tocsr()

def cuts(radius):
    ans=[]
    for k0 in range(-radius-1,radius+2):
        for k1,k2,k3 in product(range(-radius,radius+1),repeat=3):
            ans.append((-np.dot((k0,k1,k2,k3),L4))%2)
    ans=np.sort(np.array(ans))
    assert len(ans)==(2*radius+3)*(2*radius+1)**3
    assert np.min(np.diff(ans))>0 # binary64 orientation, not exact proof
    return ans

def exhaustive(radius):
    cs=cuts(radius)
    max_row=(-1.0,None)
    max_b2=(-1.0,None)
    start=time.time()
    for i,left in enumerate(cs):
        right=cs[(i+1)%len(cs)]+(2 if i+1==len(cs) else 0)
        x=((left+right)/2)%2
        b=assemble(radius,x)
        defect=b-b.T
        assert (np.max(np.abs(defect.data)) if defect.nnz else 0)<2e-13
        row=float(np.asarray(abs(b).sum(axis=1)).ravel().max())
        b2=b@b
        b2bound=float(np.asarray(abs(b2).sum(axis=1)).ravel().max()**0.5)
        if row>max_row[0]: max_row=(row,x)
        if b2bound>max_b2[0]: max_b2=(b2bound,x)
    return len(cs),max_row,max_b2,time.time()-start

if __name__=='__main__':
    results={}
    for radius in (1,2,3):
        results[radius]=exhaustive(radius)
        print('R,arcs,max_abs_row,max_sqrt_abs_B2_row,seconds=',
              radius,results[radius],flush=True)
    # Degree four at the R=3 degree-two worst arc is only a scoped follow-up
    # probe; it is not an exhaustive degree-four statement.
    x=results[3][2][1]
    b=assemble(3,x); b2=b@b; b4=b2@b2
    b4bound=float(np.asarray(abs(b4).sum(axis=1)).ravel().max()**0.25)
    print('R3_degree2_worst_arc_degree4_probe=',x,b4bound,
          'B2_nnz=',b2.nnz,'B4_nnz=',b4.nnz)
    print('STATUS=NUMERICAL_RESOURCE_PROBE_ONLY')
    print('NO_OUTWARD_NORM_CERTIFICATE')
