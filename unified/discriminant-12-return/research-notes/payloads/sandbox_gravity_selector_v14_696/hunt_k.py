"""Hunt for a FORCED exponent k: eps_12^k = a target, k from a cone
construction named in advance. No crossings harvested."""
import numpy as np
from fractions import Fraction
lne = np.log(2 + np.sqrt(3))
targets = {'psi': 45.310004305, 'depth_p': 44.012412, 'depth_e': 51.52784,
           '2psi=lnD': 90.620008610, 'ln(1/aG,p)': 88.024824,
           'ln(1/aG,e)': 103.05568, 'ln N_pairs': 184.09}
# PRE-REGISTERED candidate k's, each with its construction:
cands = {
    4: 'phi(12), |U(12)|', 6: 'helix radius', 10: '# diving channels (v14.612)',
    11: 'helix antinodes', 12: 'conductor / helix nodes', 22: 'sum q, odd channels',
    24: 'sum of U(12) = 1+5+7+11', 36: 'Y^2 max = 6^2', 42: 'K, the v14.447 split',
    83: 'sum q, even channels', 85: 'inverse moments per sector',
    105: 'sum q, all diving channels', 144: 'n^2 at n=12 (bicone sector dim)',
}
print('=== single native integers ===')
best = []
for k, story in sorted(cands.items()):
    v = k * lne
    t, tv = min(targets.items(), key=lambda kv: abs(kv[1] - v))
    gap = abs(tv - v)   # corrected 2026-10-22 (Audit R330): was the target's raw value, not the difference
    best.append((gap, k, story, t))
    print(f'  k={k:4d} ({story:38s}) log={v:8.3f}  nearest {t} gap {gap:.3f}')
print()
print('=== the one genuinely forced construction: order of eps mod conductor ===')
# eps^k = a_k + b_k sqrt(3); find ord mod 12 and mod 24 (a=1, b=0 mod m)
a, b = 2, 1
for m in (12, 24):
    a, b, k = 2, 1, 1
    while not (a % m == 1 and b % m == 0) and k < 500:
        a, b = 2*a + 3*b, a + 2*b; k += 1
    print(f'  ord_{m}(eps) = {k}  -> log = {k*lne:.2f}' if k < 500 else f'  ord_{m} > 500')
print()
print('=== exact-integer predictions for the baryon count ===')
# Tr(eps^k) = eps^k + eps^-k, exact integers via recurrence T_{k+1}=4T_k - T_{k-1}
T = [2, 4]
for _ in range(141): T.append(4*T[-1] - T[-2])
for k in (138, 139, 140, 141):
    print(f'  Tr(eps^{k}) = {T[k]:.6e}   vs eta-census N_pairs = 8.94e79 (ratio {T[k]/8.94e79:.2f})')
print()
g, k, s, t = min(best)
print(f'BEST single: k={k} ({s}) vs {t}, gap {g:.3f} in log = factor {np.exp(g):.2f}')
print('Chance floor: with 13 candidates x 7 targets, min gaps ~0.2-0.4 are expected.')
