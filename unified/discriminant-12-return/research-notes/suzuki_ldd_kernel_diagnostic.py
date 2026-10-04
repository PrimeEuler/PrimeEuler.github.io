#!/usr/bin/env python3
"""Isolate the LDDD arithmetic failure on the even mode-3 diagonal."""
from __future__ import annotations
import mpmath as mp
import numpy as np

from suzuki_ldd_source_operator import (
    LD, add, column, hp_parity_data_ld, ldd_to_mpf, mul, mul_d,
    split_mpf_ld, two_prod, two_sum, ld_string
)
from suzuki_form_core_bulk_subtracted_resonance import parity_components


def main():
    with mp.workdps(140):
        modes=np.array([1,3,5,7,9],dtype=int)
        data=hp_parity_data_ld(modes,"even-v",dps=140)
        _,_,_,_,_,ref=parity_components(9,"even-v")

        j=1 # mode 3
        p_exact=ldd_to_mpf(data.pole_hi[j],data.pole_lo[j])
        d_exact=ldd_to_mpf(data.diag_hi[j],data.diag_lo[j])

        ph,pl=mul(
            data.pole_hi[j],data.pole_lo[j],
            data.pole_hi[j],data.pole_lo[j]
        )
        ph,pl=mul_d(ph,pl,data.alpha)
        p2=ldd_to_mpf(ph,pl)

        dh,dl=add(data.diag_hi[j],data.diag_lo[j],ph,pl)
        composed=ldd_to_mpf(dh,dl)

        ah,al=column(data,j)
        got=ldd_to_mpf(ah[j],al[j])
        want=ref[j,j]

        p2_true=mp.mpf(2)*p_exact*p_exact

        # Primitive product test at the high components.
        qh,ql=two_prod(data.pole_hi[j],data.pole_hi[j])
        q=ldd_to_mpf(qh,ql)
        qtrue=mp.mpf(ld_string(data.pole_hi[j]))**2

        print("np.longdouble nmant =",np.finfo(np.longdouble).nmant)
        print("pole exact split =",mp.nstr(p_exact,60))
        print("diag exact split =",mp.nstr(d_exact,60))
        print("two_prod hi*hi error =",mp.nstr(q-qtrue,60))
        print("pole square LDDD =",mp.nstr(p2,60))
        print("pole square true =",mp.nstr(p2_true,60))
        print("pole square error =",mp.nstr(p2-p2_true,60))
        print("composed diag =",mp.nstr(composed,60))
        print("column diag =",mp.nstr(got,60))
        print("reference =",mp.nstr(want,60))
        print("final error =",mp.nstr(got-want,60))

        # Compare split_mpf_ld itself on the exact reference.
        rh,rl=split_mpf_ld(want)
        rec=ldd_to_mpf(rh,rl)
        print("direct split/recombine reference error =",mp.nstr(rec-want,60))

        # A generic product pair.
        x=mp.mpf("0.473123456789012345678901234567890123456")
        xh,xl=split_mpf_ld(x)
        mh,ml=mul(xh,xl,xh,xl)
        print("generic square error =",mp.nstr(ldd_to_mpf(mh,ml)-x*x,60))


if __name__=="__main__":
    main()
