#!/usr/bin/env python3
"""Independent full-front direct point sums at six numerical source rows."""
import argparse,json,sys,hashlib
from pathlib import Path
from fractions import Fraction as F
from suzuki_exact_outward_certificate import read_snapshot
from suzuki_full_stationary_source_transport import combine,PINS
from suzuki_exact_integer_source_action import dot
from suzuki_certified_remote_z import evaluate
from suzuki_frozen_trial_far_outward import atan_recip,hyperbolic,add,times,neg,constant,recip,enclose
sys.set_int_max_str_digits(0)
def build(root,source_root,numerical_root):
    rows=[]
    for sector in ('even-v','odd-v'):
        sp=root/f'joint-256000-{sector}.trace-256000.full.zip'
        assert hashlib.sha256(sp.read_bytes()).hexdigest()==PINS[sector][0]
        _,s,V,_=read_snapshot(sp)
        cert=json.loads((source_root/f'full-stationary-source-{sector}.json').read_text())
        Z=combine(V,[F(q) for q in cert['q_rational']]);P=dot(s['pole'],Z)
        pi=enclose(add(times(constant(16),atan_recip(5)),neg(times(constant(4),atan_recip(239)))))
        hyp=enclose(hyperbolic(sector=='odd-v'));Li=times(times(constant(4),hyp),recip(pi))
        ti=times(recip(pi),recip(pi));L=sum(Li)/2;t=sum(ti)/2
        buf=(numerical_root/(sector+'-rho-near.bin')).read_bytes()
        nc=json.loads((numerical_root/f'numerical-near-source-{sector}.json').read_text())
        assert hashlib.sha256(buf).hexdigest()==nc['point_buffer']['sha256']
        for i in (0,64000,127999):
            n=256000+s['modes'][0]+2*i;r=evaluate(n)
            zr=(F(r['lower_rational'])+F(r['upper_rational']))/2
            zb=max(s['z']['bits'],zr.denominator.bit_length()-1)
            zi=int(zr*(1<<zb));shift=zb-s['z']['bits'];cb=s['c']['bits'];xb=Z['bits']
            denpow=1<<(cb+zb+xb);total=0
            for m,zm,x in zip(s['modes'],s['z']['values'],Z['values']):
                num=s['c']['values'][0]*(zi*m-n*(zm<<shift))*x
                total+=(num<<256)//((n*n-m*m)*denpow)
            direct=F(1,n-1 if sector=='odd-v' else n)-F(total,1<<256)-s['alpha']*L*n/(n*n+t)*P
            stored=F(int.from_bytes(buf[i*17:(i+1)*17],'little',signed=True),1<<128)
            diff=abs(direct-stored);assert diff<F('1e-30')
            rows.append({'sector':sector,'mode':n,'absolute_point_direct_difference_rational':str(diff)})
    return {'schema':'cone.numerical-near-direct-kernel-checks.v1','rows':rows,
      'all_six_direct_full_front_checks_lt_1e_minus30':True,
      'checks_compare_point_recipes_not_physical_interval_errors':True}
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for name in ('root','source-root','numerical-root','output'):p.add_argument('--'+name,type=Path,required=True)
    a=p.parse_args();a.output.write_text(json.dumps(build(a.root,a.source_root,a.numerical_root),indent=2,sort_keys=True)+'\n')
    print('All six direct full-front point sums pass.')
