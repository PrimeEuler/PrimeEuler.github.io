#!/usr/bin/env python3
"""Split-precision driver for the M8000 scalar interval audit.

Modes <=192 use the original 420-digit interval context because the direct
Si/Ci power series has large intermediate cancellation.  Modes >192 use
100-digit interval arithmetic on the asymptotic branch, still >60 decimal
digits beyond the 1e-37 representation-error target.

The underlying interval formulas are unchanged.
"""
import json
import mpmath as mp

if not hasattr(mp.iv, "cosh"):
    mp.iv.cosh = lambda x: (mp.iv.exp(x) + mp.iv.exp(-x)) / 2
if not hasattr(mp.iv, "sinh"):
    mp.iv.sinh = lambda x: (mp.iv.exp(x) - mp.iv.exp(-x)) / 2

import suzuki_M8000_scalar_interval_audit as a

LOW_DPS=420
HIGH_DPS=100

def one_sector(sector):
    modes=a.parity_modes(sector,a.TARGET_MAX)
    data=a.hp_parity_data(
        modes,sector,dps=a.MPDPS,arch_terms=a.ARCH_TERMS,
        correction_terms=a.CORR_TERMS
    )
    max_z=(0.0,None); max_d=(0.0,None); max_p=(0.0,None)
    for i,n in enumerate(modes):
        mp.iv.dps=LOW_DPS if int(n)<=a.LOW_SERIES_MAX else HIGH_DPS
        z,d,p=a.exact_scalar_intervals(int(n),sector)
        zm=a.ldd_to_mpf(data.z_hi[i],data.z_lo[i])
        dm=a.ldd_to_mpf(data.diag_hi[i],data.diag_lo[i])
        pm=a.ldd_to_mpf(data.pole_hi[i],data.pole_lo[i])
        ez=a.abs_error_bound(z,zm); ed=a.abs_error_bound(d,dm); ep=a.abs_error_bound(p,pm)
        if ez>max_z[0]: max_z=(ez,int(n))
        if ed>max_d[0]: max_d=(ed,int(n))
        if ep>max_p[0]: max_p=(ep,int(n))
        if (i+1)%500==0:
            print(sector,"checked",i+1,"/",len(modes),"max z",max_z,"max diag",max_d)
    mp.iv.dps=HIGH_DPS
    cm=a.ldd_to_mpf(data.c_hi,data.c_lo)
    ec=a.abs_error_bound(2/mp.iv.pi,cm)
    row={
        "sector":sector,
        "dimension":len(modes),
        "last_mode":int(modes[-1]),
        "max_z_abs_error":{"value":max_z[0],"mode":max_z[1]},
        "max_diag_abs_error":{"value":max_d[0],"mode":max_d[1]},
        "max_pole_abs_error":{"value":max_p[0],"mode":max_p[1]},
        "two_over_pi_abs_error":ec,
    }
    print("\n",sector,row)
    return row

def main():
    old=mp.iv.dps
    mp.mp.dps=a.MPDPS
    try:
        rows=[one_sector("even-v"),one_sector("odd-v")]
    finally:
        mp.iv.dps=old
    out={
        "low_iv_dps":LOW_DPS,
        "high_iv_dps":HIGH_DPS,
        "split_at":a.LOW_SERIES_MAX,
        "rows":rows,
        "theorem_scope":(
            "Same interval formulas as the original M8000 scalar audit; only "
            "the interval precision is reduced above mode 192, where the "
            "asymptotic branch is stable and 100 digits exceed the target."
        ),
    }
    a.OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("\nwrote",a.OUT)

if __name__=="__main__":
    main()
