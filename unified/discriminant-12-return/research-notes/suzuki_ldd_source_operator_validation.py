#!/usr/bin/env python3
"""Validate the long-double double-double source operator at N=192."""
from __future__ import annotations

import argparse
import mpmath as mp
import numpy as np

from suzuki_ldd_source_operator import column,hp_parity_data_ld,ldd_to_mpf
from suzuki_form_core_bulk_subtracted_resonance import parity_components,source_overlap


def one(max_mode,sector,dps):
    modes=np.arange(1 if sector=="even-v" else 2,max_mode+1,2,dtype=int)
    data=hp_parity_data_ld(modes,sector,dps=dps)
    with mp.workdps(dps):
        ns,_,_,_,_,ref=parity_components(max_mode,sector)
        if list(modes)!=ns:
            raise RuntimeError("mode mismatch")
        ma=mp.mpf(0); mr=mp.mpf(0); sa=mp.mpf(0); worst=None
        for j in range(len(modes)):
            ah,al=column(data,j)
            for i in range(len(modes)):
                got=ldd_to_mpf(ah[i],al[i])
                want=ref[i,j]
                e=abs(got-want)
                rel=e/max(abs(want),mp.mpf("1e-120"))
                if e>ma:
                    ma=e; worst=(int(modes[i]),int(modes[j]),got,want)
                mr=max(mr,rel)
        for i,n in enumerate(modes):
            got=ldd_to_mpf(data.source_hi[i],data.source_lo[i])
            sa=max(sa,abs(got-source_overlap(int(n))))
        print("\nsector =",sector)
        print("longdouble nmant =",np.finfo(np.longdouble).nmant)
        print("max matrix abs error =",mp.nstr(ma,40))
        print("max matrix rel error =",mp.nstr(mr,40))
        print("max source abs error =",mp.nstr(sa,40))
        print("worst =",(
            worst[0],worst[1],
            mp.nstr(worst[2],40),mp.nstr(worst[3],40)
        ))
        if ma>=mp.mpf("2e-38"):
            raise RuntimeError((sector,"LDDD matrix validation failed",ma))
        if sa>=mp.mpf("2e-39"):
            raise RuntimeError((sector,"LDDD source validation failed",sa))


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--max-mode",type=int,default=192)
    p.add_argument("--dps",type=int,default=140)
    a=p.parse_args()
    one(a.max_mode,"even-v",a.dps)
    one(a.max_mode,"odd-v",a.dps)
    print("\nPASS: LDDD source operator agrees with independent mp producer.")
    print("Guardrail: midpoint arithmetic validation only.")


if __name__=="__main__":
    main()
