#!/usr/bin/env python3
"""Outward-arithmetic transcript for M16001 nominal source-payload conversion.

This gate is deliberately about *conversion*, not source-function evaluation.
source_data_stop() freezes Z and c, and the imported PI constant, as IEEE-754
binary64 nominal payloads.  Converting any finite binary64 value to x86
80-bit/NumPy longdouble (64-bit significand) is exact: every binary64 dyadic
(significand <=53 bits) is representable with the same exponent and no rounding.
Therefore the conversion radii for Z, c, and PI are exactly zero.

The already-certified exact-source versus nominal-source uncertainty is a
separate operator-level 2e-13 shift and is NOT duplicated here.  Arithmetic
using the converted payloads is charged by the displacement/pole transcripts.
"""
import numpy as np
from suzuki_M16001_even_index3_anisotropic_tail_split import source_data_stop, PI

LD=np.longdouble

def exact_binary64_to_ld(a):
    a=np.asarray(a,dtype=np.float64)
    b=a.astype(LD)
    # Round-trip equality is a necessary executable check.  The proof of zero
    # radius is format-theoretic: p_ld >= 53 and exponent range contains binary64.
    assert np.all(np.isfinite(a))
    assert np.all(b.astype(np.float64)==a)
    return b

def main():
    finfo=np.finfo(LD)
    assert finfo.nmant+1 >= 53
    assert finfo.maxexp >= np.finfo(np.float64).maxexp
    modes,Z,diag0,c=source_data_stop()
    Zld=exact_binary64_to_ld(Z)
    cld=exact_binary64_to_ld(c)
    p64=np.float64(PI)
    pld=exact_binary64_to_ld(np.array([p64]))[0]
    # Exact dyadic conversion => propagated payload radius is identically zero.
    rZ=LD(0); rc=LD(0); rpi=LD(0)
    # Residual contribution from conversion alone is therefore zero, including
    # all downstream linear/bilinear propagation.  Subsequent arithmetic is
    # charged separately in v13.521/v13.527-style transcripts.
    residual_sq=LD(0)
    residual=np.nextafter(np.sqrt(residual_sq),LD(np.inf),dtype=LD) if residual_sq else LD(0)
    print('longdouble significand bits =',finfo.nmant+1)
    print('binary64 significand bits =',np.finfo(np.float64).nmant+1)
    print('Z entries checked =',len(Zld))
    print('c entries checked =',len(cld))
    print('PI binary64 hex =',p64.hex())
    print('max Z conversion radius =',rZ)
    print('max c conversion radius =',rc)
    print('PI conversion radius =',rpi)
    print('CERTIFIED source-payload conversion residual contribution <=',residual)
    print('SEPARATE source-function uncertainty: ||A_exact-A_nom|| < 2e-13 (not double-counted)')
    print('FAIL-CLOSED remainder: diag_payload_conversion, X_payload_conversion')

if __name__=='__main__': main()
