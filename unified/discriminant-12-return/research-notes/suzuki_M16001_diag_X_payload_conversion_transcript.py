#!/usr/bin/env python3
"""Close the remaining M16001 nominal payload-conversion gates: diag0 and X.

Certification target
--------------------
The residual replay treats the values returned by source_data_stop() and
finite_solve_stop() as the *frozen nominal binary64 payload*.  It does not need
X to approximate the exact solution before the residual is evaluated: backward
error uses any fixed candidate X, then certifies R=A_nom X-AFC.  Thus the only
payload-conversion question here is whether the frozen binary64 diag0 and X
entries are represented exactly after conversion to the longdouble arithmetic
used by the residual transcript.

Every finite IEEE-754 binary64 number is a dyadic with <=53 significand bits.
On the certified replay platform NumPy longdouble has >=64 significand bits and
an exponent range containing binary64.  Hence binary64 -> longdouble conversion
is exact and both conversion radii are identically zero.

This does NOT certify the arithmetic used to *produce* X.  That is unnecessary
for a residual/backward-error argument once X is frozen as the candidate.  It
also does not absorb exact-source vs nominal-source uncertainty, which remains
the separate ||A_exact-A_nom|| < 2e-13 operator shift.
"""
import hashlib
import numpy as np
from suzuki_M16001_even_index3_anisotropic_tail_split import source_data_stop, finite_solve_stop

LD=np.longdouble
F64=np.float64


def freeze_and_convert(a, name):
    a=np.asarray(a,dtype=F64)
    assert np.all(np.isfinite(a)), name+' contains nonfinite payload'
    b=a.astype(LD)
    assert np.all(b.astype(F64)==a), name+' failed exact round trip'
    # Immutable identity of the frozen binary64 byte payload.
    digest=hashlib.sha256(np.ascontiguousarray(a).view(np.uint8)).hexdigest()
    return a,b,digest


def main():
    fi=np.finfo(LD); f64=np.finfo(F64)
    assert fi.nmant+1 >= f64.nmant+1
    assert fi.maxexp >= f64.maxexp
    modes,Z,diag0,c=source_data_stop()
    _,_,_,X,_=finite_solve_stop()
    d64,dld,dsha=freeze_and_convert(diag0,'diag0')
    x64,xld,xsha=freeze_and_convert(X,'X')
    # Exact dyadic embeddings: interval radii are mathematically zero.
    rd=LD(0); rx=LD(0)
    # Any residual perturbation caused solely by these conversions is therefore
    # exactly zero, even after multiplication/contraction: delta diag=delta X=0.
    residual=LD(0)
    print('longdouble significand bits =',fi.nmant+1)
    print('binary64 significand bits =',f64.nmant+1)
    print('diag0 entries checked =',d64.size)
    print('X entries checked =',x64.size)
    print('X shape =',x64.shape)
    print('diag0 binary64 payload SHA256 =',dsha)
    print('X binary64 payload SHA256 =',xsha)
    print('max diag0 conversion radius =',rd)
    print('max X conversion radius =',rx)
    print('CERTIFIED diag0+X payload-conversion residual contribution <=',residual)
    print('BACKWARD-ERROR NOTE: X production accuracy is not assumed; X is the frozen candidate whose residual is certified.')
    print('SEPARATE source-function uncertainty: ||A_exact-A_nom|| < 2e-13 (not double-counted)')
    print('PAYLOAD-CONVERSION GATE: CLOSED for Z, c, PI, diag0, and X')

if __name__=='__main__': main()
