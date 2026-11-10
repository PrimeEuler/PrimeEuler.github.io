#!/usr/bin/env python3
"""Suzuki v15.644: NONCERTIFYING sparse regular-representation reconnaissance.
Uses binary64 np.log/sawtooth and eigsh; eigenvalues are sampled probes,
NOT outward interval enclosures of the essential-supremum spectral norm.
"""
import time
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh
from itertools import combinations, product

Q=(2,3,4,5,7)
V={2:(1,0,0,0),3:(0,1,0,0),4:(2,0,0,0),5:(0,0,1,0),7:(0,0,0,1)}
L={q:np.log(q) for q in Q}
A={q:L[q]/(2*np.sqrt(q)) for q in Q}
def saw(x): return 1-np.mod(x,2)
def D(x,s,l): return saw(x-s*l)-saw(x)
def G(x,s,t,la,lb):
    y=x+s*la
    z=x-t*lb
    return D(y,s,la)*D(y,t,lb)+D(z,-t,lb)*D(z,-s,la)

def assemble(R,x):
    B=2*R+1
    sites=np.indices((B,)*4,dtype=np.int16).reshape(4,-1).T
    h=sites.astype(np.int32)-R
    n=len(sites)
    shifts=np.array([L[2],L[3],L[5],L[7]])
    y=x+h@shifts
    row=[];col=[];data=[]
    for q,r in combinations(Q,2):
        for s,t in product((-1,1),repeat=2):
            g=np.array([t*V[r][i]-s*V[q][i] for i in range(4)])
            source=sites-g
            mask=np.all((source>=0)&(source<B),axis=1)
            rr=np.flatnonzero(mask)
            cs=np.ravel_multi_index(source[mask].T,(B,)*4)
            vals=s*t*A[q]*A[r]*G(y[mask],s,t,L[q],L[r])
            row.append(rr);col.append(cs);data.append(vals)
    return coo_matrix((np.concatenate(data),(np.concatenate(row),np.concatenate(col))),
                      shape=(n,n)).tocsr()

if __name__=='__main__':
    for R in (2,4,6,8,10,12,16):
        start=time.time()
        mat=assemble(R,0.12345)
        defect=mat-mat.T
        hermitian_defect=np.max(np.abs(defect.data)) if defect.nnz else 0.
        assert hermitian_defect < 1e-11
        lam=eigsh(mat,k=1,which='LA',tol=3e-7,
                   return_eigenvectors=False,maxiter=350)[0]
        memory=(mat.data.nbytes+mat.indices.nbytes+mat.indptr.nbytes)/1e6
        print(R,mat.shape[0],mat.nnz,
              'memory_MB',round(memory,1),
              'max_hermiticity_defect',hermitian_defect,
              'sampled_lambda_max',lam,
              'elapsed_s',round(time.time()-start,2),flush=True)
    print('STATUS=NUMERICAL_RECONNAISSANCE_ONLY')
    print('NO_CERTIFIED_MATRIX_NORM_UPPER_BOUND')
