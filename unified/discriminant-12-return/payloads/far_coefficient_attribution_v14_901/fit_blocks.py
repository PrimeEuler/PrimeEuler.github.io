"""Fit block means of N*S(N): NS = K - beta*X + gamma/ln n, for
X = ln ln(n/4) (natural: l_m = ln(m/4)) and X = ln ln n, beta free
and pinned at W_0/2. Also channel slopes (nU vs pi*W_0/2)."""
import json, sys
from math import log, pi
import numpy as np

def fit(pts, ys, beta_fixed=None, var='lam'):
    if var == 'lam':
        X = np.array([log(log(n / 4)) for n in pts])
    else:
        X = np.array([log(log(n)) for n in pts])
    li = np.array([1.0 / log(n) for n in pts])
    y = np.array(ys)
    if beta_fixed is None:
        A = np.column_stack([np.ones_like(X), -X, li])
        c, *_ = np.linalg.lstsq(A, y, rcond=None)
        r = y - A @ c
        return {'K': c[0], 'beta': c[1], 'gamma': c[2],
                'rms': float(np.sqrt(np.mean(r ** 2))),
                'max': float(np.max(np.abs(r)))}
    A = np.column_stack([np.ones_like(X), li])
    c, *_ = np.linalg.lstsq(A, y + beta_fixed * X, rcond=None)
    r = y - (A @ c - beta_fixed * X)
    return {'K': c[0], 'beta': beta_fixed, 'gamma': c[1],
            'rms': float(np.sqrt(np.mean(r ** 2))),
            'max': float(np.max(np.abs(r)))}

for sector, W0 in (('even-v', 1.1327596301371365),
                   ('odd-v', 1.1317098782051290)):
    try:
        d = json.load(open(f'blocks_{sector}.json'))
    except FileNotFoundError:
        print(sector, 'not ready'); continue
    pts = [r['center'] for r in d]
    NS = [r['NS_mean'] for r in d]
    NU = [r['nU_mean'] for r in d]
    print(f'== {sector}  ({len(pts)} blocks)')
    for var in ('lam', 'lnln'):
        print('  NS free   ', var, json.dumps(fit(pts, NS, var=var)))
        print('  NS pinned ', var,
              json.dumps(fit(pts, NS, W0 / 2, var=var)))
    print('  NS pinned, no gamma:', end=' ')
    X = np.array([log(log(n / 4)) for n in pts])
    K = float(np.mean(np.array(NS) + (W0 / 2) * X))
    resid = np.array(NS) + (W0 / 2) * X - K
    print(f'K={K:.5f} resid range [{resid.min():+.5f},{resid.max():+.5f}]')
    print('  nU slope vs lam: free fit',
          json.dumps(fit(pts, NU, var='lam')))
    print(f'  pi*W0/2 = {pi * W0 / 2:.5f}')
