#!/usr/bin/env python3
"""Suzuki R=3 exhaustive degree-four positive-polynomial resource probe.

Evaluates ||B(x)|| <= ||B(x)^4||_infinity^(1/4) on every one of the
3,087 v15.650 candidate arcs.  All matrix and cut arithmetic is binary64:
this is NOT an outward certificate and NOT a radius-16 bound.
Run from the repository root with OPENBLAS_NUM_THREADS=1.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import time
from multiprocessing import Pool
import numpy as np
from importlib.util import spec_from_file_location, module_from_spec

PRODUCER=('unified/discriminant-12-return/research-notes/'
          'lane_a_v15_657_suzuki_positive_polynomial_small_radius_probe.py')
spec=spec_from_file_location('v15657',PRODUCER)
producer=module_from_spec(spec)
spec.loader.exec_module(producer)

RADIUS=3
CUTS=producer.cuts(RADIUS)
ARC_MIDPOINTS=[]
for i,left in enumerate(CUTS):
    right=CUTS[(i+1)%len(CUTS)]+(2 if i+1==len(CUTS) else 0)
    ARC_MIDPOINTS.append(float(((left+right)/2)%2))
assert len(ARC_MIDPOINTS)==(2*RADIUS+3)*(2*RADIUS+1)**3==3087

def work(x):
    b=producer.assemble(RADIUS,x)
    defect=b-b.T
    assert (np.max(np.abs(defect.data)) if defect.nnz else 0)<2e-13
    b2=b@b
    b4=b2@b2
    value=float(np.asarray(abs(b4).sum(axis=1)).ravel().max()**0.25)
    return value,x,b2.nnz,b4.nnz

if __name__=='__main__':
    start=time.time()
    best=(-1.0,None,None,None)
    with Pool(processes=6) as pool:
        for count,result in enumerate(
                pool.imap_unordered(work,ARC_MIDPOINTS,chunksize=1),1):
            if result[0]>best[0]: best=result
            if count%250==0:
                print('progress',count,'best',best,
                      'seconds',time.time()-start,flush=True)
    print('R3_ARCS',len(ARC_MIDPOINTS),
          'MAX_B4_BOUND',best,'SECONDS',time.time()-start)
    print('STATUS=BINARY64_RESOURCE_PROBE_ONLY')
    print('NO_OUTWARD_NORM_CERTIFICATE')
