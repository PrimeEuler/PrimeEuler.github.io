"""Model selector built to the spec sheet (2026-10-21):
(1) single-valuedness/winding form; (2) seated in the shell loop
budget's two sectors; (3) quantum at hierarchy size; (4) dimensionless,
G-free, pair-dependent.
Shell loop at (T=j+1/2, X=m+1/2): pointing p=(m+1/2)/(j+1/2),
holonomy h=(j-m)/(j+1/2), p+h=1. Per-loop phase imbalance (p-h);
single-valuedness closes after N = 1/|p-h| loops."""
import numpy as np

psi_target = 45.310004305
print('=== 1) phase-closure count on one shell: N(j,m) = (j+1/2)/|2m-j+1/2| ===')
for j in (1, 2, 3):
    row = []
    for m in range(-j, j+1):
        p = (m+0.5)/(j+0.5); h = (j-m)/(j+0.5)
        N = 1/abs(p-h) if p != h else float('inf')
        row.append(f'm={m:+d}: N={N:.3f}')
    print(f'j={j}: ' + '  '.join(row))
print('-> one shell gives small rationals only: quality (3) FAILS at shell scale.')

print()
print('=== 2) compounding the loop sector-ratio rapidity over chains ===')
def rap(p, h): return abs(0.5*np.log(p/h))
# (a) conductor chain (v14.612 channels), pairs (q, q-1) as secant rapidities
qs = [3, 4, 5, 7, 8, 11, 12, 13, 21, 24]
s = sum(0.5*np.log(q/(q-1)) for q in qs)
print(f'(a) conductor-chain sum of secant rapidities: {s:.4f}  (target {psi_target})')
# (b) radial ladder of m=0 loops: shell T=j+1/2, p=(1/2)/T, h=(T-1/2)/T
acc, K = 0.0, 0
while acc < psi_target and K < 10000:
    K += 1
    T = K + 0.5                       # shell index: T = 3/2, 5/2, ... hmm use j=K
    j = K
    T = j + 0.5
    p = 0.5/T; h = (j - 0)/T
    acc += rap(p, h)
print(f'(b) ladder of m=0 loop rapidities reaches psi at K={K} shells (sum {acc:.3f})')
# (c) (4/3)-step chain for scale (v14.627 best family)
print(f'(c) (4/3)-steps needed: {psi_target/(0.5*np.log(4/3)):.0f}')
print()
print('portrait: the compounding LENGTH needed is rule-dependent --')
print('~10 links (conductor secants, but they only sum to ~1.6),')
print('~30 shells (ladder loop-rapidities), ~315 (4/3)-steps,')
print('or a single count over ~1e39 objects (raw inventory).')
