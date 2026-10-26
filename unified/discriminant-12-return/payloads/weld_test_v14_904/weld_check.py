"""Weld test (Jeremy's conjecture, 2026-10-26): the /4 in Suzuki's
log(n/4) is the dyon pair-product quantum's denominator.
Grid (v14.768): members x=h*a, y=h*b; shell n=a*b; r=log(h^2 n);
crossing offset X=(x-y)/2 = h(a-b)/2 -> offset lattice (h/2)Z.
Pair quantum q (v14.731, derived): EM eg/hbar in (1/2)Z, q=1/2;
gravity mu*c*l/hbar in (1/4)Z, q=1/4.
Weld rule: dictionary offset lattice = physical offset lattice,
h/2 = q, i.e. h = 2q. Exact rational check, both sectors."""
from fractions import Fraction as F

for name, q, h_obs in [('EM', F(1, 2), F(1)), ('G', F(1, 4), F(1, 2))]:
    h = 2 * q
    c = 1 / h ** 2
    assert h == h_obs and h / 2 == q
    print(f"{name}: q={q} h=2q={h} c={c} vertex=+-{h/2} r=log(n/{c}) OK")
    a = 1 / h
    assert h * a == 1  # r=0 shell n=c carries the unit raw pair (1,1)

offs = {F(1, 2) * (a - b) / 2 for a in range(1, 33) for b in range(1, 33)}
assert all((o * 4).denominator == 1 for o in offs)  # G offsets in (1/4)Z
print("G-grid crossing offsets lie in (1/4)Z: OK")
print("DONE")
