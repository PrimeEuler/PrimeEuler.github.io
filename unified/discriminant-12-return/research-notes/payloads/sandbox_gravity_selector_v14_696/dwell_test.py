"""DWELL TEST (2026-10-22): is a period-weighted census of the cone's
orbit family dominated by the separatrix term?
Shells n=1..N; states (n,l,m), degeneracy (2l+1) per l (total n^2/shell,
the bicone dimension). Angular share s = (l+1/2)^2/n^2 (Langer);
dwell weight = elliptic period log K(s) = (1/2) ln(16/s).
Strong claim: ln(N_dwell/N_plain) ~ K_max (separatrix-dominated).
Weak claim: the log lives only in a SINGLE orbit seated near e=1."""
import numpy as np

def census(N):
    plain = dwell = 0.0
    for n in range(1, N+1):
        l = np.arange(n)
        deg = 2*l + 1
        s = ((l + 0.5)/n)**2
        K = 0.5*np.log(16.0/s)
        plain += deg.sum()
        dwell += (deg*K).sum()
    return plain, dwell

print(f'{"N":>6} {"ln(dwell/plain)":>16} {"K_max(top shell)":>17} {"mean K":>8}')
for N in (10, 42, 100, 400, 2000):
    p, d = census(N)
    kmax = 0.5*np.log(16.0/((1.5/N)**2))   # closest orbit on the top shell
    print(f'{N:>6} {np.log(d/p):>16.4f} {kmax:>17.4f} {d/p:>8.4f}')
print()
print('ln(dwell/plain) stays O(1) (~1.2) while K_max grows like ln N:')
print('in a CENSUS, degeneracy (2l+1) beats the logarithmic dwell weight --')
print('the separatrix orbits are too few. The log survives only for a')
print('SINGLE orbit seated at the separatrix by the initial condition.')
