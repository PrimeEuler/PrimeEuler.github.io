#!/usr/bin/env python3
"""Primitive arithmetic transcript for the M16001 FC pole update.

Certifies arithmetic, conditional on stored nominal c payloads, for every entry
    P_ij = 2*cF_i*cC_j,
    AFC_ij = A0FC_ij + P_ij.
It also reports the corresponding subtraction charge when AFC is consumed as
R_ij = (AFF X)_ij - AFC_ij.
Source/payload conversion radii for c and A0FC remain separate gates.
"""
import numpy as np
from suzuki_M16001_even_index3_anisotropic_tail_split import source_data_stop
LD=np.longdouble; U=LD(2)**LD(-64)
def g(k):
    ku=LD(k)*U; return ku/(1-ku)

def scan():
    modes,Z,diag0,c=source_data_stop()
    cC=np.asarray(c[:10],dtype=LD); cF=np.asarray(c[10:],dtype=LD)
    # Use stored nominal A0FC solely to measure the addition magnitude; its own
    # primitive radius is supplied by the displacement transcript, not hidden here.
    from suzuki_M3999_unresolved_fourplane_residual_gram_replay import off_block
    A0=np.asarray(off_block(modes[10:],Z[10:],modes[:10],Z[:10]),dtype=LD)
    max_prod=max_factor=max_pole=max_prod_rad=max_factor_rad=max_pole_rad=LD(0)
    max_add_rad=max_sub_rad=LD(0); max_afc=LD(0)
    # Product then factor-2 is deliberately charged as two operations even
    # though multiplication by 2 is exact for normal binary floating values.
    for i,x in enumerate(cF):
        for j,y in enumerate(cC):
            prod=x*y; rprod=g(1)*abs(prod)
            pole=LD(2)*prod
            rfactor=LD(2)*rprod + g(1)*abs(pole)
            # same value; retain names to make both requested stages explicit
            rpole=rfactor
            afc=A0[i,j]+pole
            radd=g(1)*(abs(A0[i,j])+abs(pole))
            # If AFC is later subtracted from a nominal matvec v, the primitive
            # subtraction rounding is bounded by gamma_1(|v|+|AFC|).  Without
            # v this script reports the AFC coefficient multiplying gamma_1.
            sub_coeff=abs(afc)
            max_prod=max(max_prod,abs(prod)); max_factor=max(max_factor,abs(pole)); max_pole=max(max_pole,abs(pole))
            max_prod_rad=max(max_prod_rad,rprod); max_factor_rad=max(max_factor_rad,rfactor); max_pole_rad=max(max_pole_rad,rpole)
            max_add_rad=max(max_add_rad,radd); max_sub_rad=max(max_sub_rad,g(1)*sub_coeff); max_afc=max(max_afc,abs(afc))
    print('entries =',len(cF)*len(cC))
    print('u =',U)
    print('max |cF*cC| =',max_prod)
    print('max product charge gamma1*|cF*cC| =',max_prod_rad)
    print('max |2*cF*cC| =',max_pole)
    print('max factor-2 propagated charge =',max_factor_rad)
    print('max AFC addition rounding charge =',max_add_rad)
    print('max |AFC| =',max_afc)
    print('max AFC-only subtraction rounding component =',max_sub_rad)
    print('POLE ENTRY arithmetic radius <=',max_pole_rad)
    print('AFC FORMATION arithmetic increment <=',max_pole_rad+max_add_rad)
    print('NOTE: add A0FC primitive radius and c/A0FC payload conversion radii separately.')
    return locals()
if __name__=='__main__': scan()
