#!/usr/bin/env python3
"""v15.822: unequal-arm pure-gauge false optical differential control.
Requires additive v15.821 script in the same research-notes folder.
"""
import numpy as np
from k4_flrw_gauge_endpoint_control_v15_821 import run
A,B,omega,lam,te=.17,.12,1.1,.8,.08
d1,d2=.075,.11
p=run(A,B,omega,lam,d1,te)
q=run(A,B,omega,lam,d2,te)
fixed=p[0]-q[0]
event=p[1]-q[1]
physical=p[2]-q[2]
assert abs(fixed)>1e-6 and abs(physical)<1e-11
assert abs(fixed+event)<1e-11
H=1/np.sqrt(3)
Te=A*te**3*np.exp(-1j*omega*te)
expected=-(np.exp(H*(te+2*d1))-np.exp(H*(te+2*d2)))*Te
assert abs(fixed-expected)<1e-11
print('PASS pure-gauge unequal arm fixed-coordinate bias:',fixed)
print('PASS event-anchored unequal arm physical difference:',physical)
print('PASS exact endpoint formula and gauge cancellation')
