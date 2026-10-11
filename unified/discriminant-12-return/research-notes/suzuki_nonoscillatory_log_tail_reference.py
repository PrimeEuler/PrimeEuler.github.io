#!/usr/bin/env python3
"""Independent high-precision cross-check; never used as a proof enclosure."""
import argparse,json
from pathlib import Path
from fractions import Fraction as F
import mpmath as mp
p=argparse.ArgumentParser();p.add_argument('--payload',type=Path,required=True);p.add_argument('--output',type=Path,required=True);args=p.parse_args()
mp.mp.dps=90;rows=json.loads(args.payload.read_text())['cases'];checks=[]
for row in rows:
 if (row['a'],row['power']) not in ((512001,2),(512001,128),(512002,3)):continue
 a=mp.mpf(row['a']);power=row['power'];lam=mp.log(a/4)
 value=a*mp.quad(lambda u:mp.exp(-(power-1)*u)/(lam+u),[0,1,4,16,64,mp.inf])/2+1/(2*lam)
 f=lambda x:(a/x)**power/mp.log(x/4)
 for j in range(1,17):value-=mp.bernoulli(2*j)/mp.factorial(2*j)*2**(2*j-1)*mp.diff(f,a,2*j-1)
 lo,hi=[mp.mpf(F(x).numerator)/F(x).denominator for x in row['interval']]
 assert lo<=value<=hi
 checks.append({'a':int(a),'p':power,'independent_90_digit_reference_inside_directed_interval':True})
assert len(checks)==3
args.output.write_text(json.dumps({'schema':'cone.nonoscillatory-log-tail-reference.v1','checks':checks,'reference_not_used_for_certificate':True},indent=2,sort_keys=True)+'\n')
print(json.dumps(checks),flush=True)
