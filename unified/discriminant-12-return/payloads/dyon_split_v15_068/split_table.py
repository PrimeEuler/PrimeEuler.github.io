"""Dyon pair split, layer 1: rest-frame Casimir budget fractions f(j,n) = (n/2)^2/(j(j+1))
and boost bounds psi_max(j,n) = arcosh(2 sqrt(j(j+1))/n), from v14.731 S5."""
import numpy as np
for j2 in [1, 2, 3, 4, 6]:
    j = j2 / 2
    nmax = int(np.floor(2 * np.sqrt(j * (j + 1))))
    cells = []
    for n in range(1, nmax + 1):
        f = (n / 2) ** 2 / (j * (j + 1))
        cells.append(f"n={n}: f={f:.4f}, psi_max={np.arccosh(2 * np.sqrt(j * (j + 1)) / n):.3f}")
    print(f"j={j}: " + " | ".join(cells))
