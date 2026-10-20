import numpy as np
from scipy.special import ellipk, ellipe
from scipy.optimize import brentq

# Loop field (radius a, unit mu0*I/2pi) at (X, r), X axial / r radial. Standard elliptic form.
def B_loop(X, r, a):
    m = 4*a*r / ((a+r)**2 + X**2)          # elliptic parameter k^2
    m = min(m, 1 - 1e-14)
    K, E = ellipk(m), ellipe(m)
    den = (a-r)**2 + X**2
    sq = np.sqrt((a+r)**2 + X**2)
    BX = (1.0/sq) * (K + (a*a - r*r - X*X)/den * E)
    Br = (X/(r*sq)) * (-K + (a*a + r*r + X*X)/den * E) if r > 1e-9 else 0.0
    return BX, Br

def Bmag(X, r, coils):
    BX = Br = 0.0
    for (Xc, a, turns) in coils:
        bx, br = B_loop(X - Xc, r, a)
        BX += turns*bx; Br += turns*br
    return np.hypot(BX, Br)

def profile(coils, Xs, r_throat=1.0):
    B0 = Bmag(0.0, r_throat, coils)
    grid = np.linspace(0.05, 8.5, 4000)
    out = []
    for X in Xs:
        vals = np.array([Bmag(X, r, coils) for r in grid]) - B0
        idx = np.where(np.diff(np.sign(vals)) > 0)[0]   # first upward crossing = interface nearest axis
        if len(idx) == 0:
            out.append(np.nan); continue
        i = idx[0]
        out.append(brentq(lambda r: Bmag(X, r, coils) - B0, grid[i], grid[i+1], xtol=1e-12))
    return np.array(out)

Xs = np.array([0, 0.5, 1, 2, 3, 4, 5.0])
r_par = np.sqrt(2*Xs + 1)

single = [(0.0, 6.5, 1.0)]
totient = [(0.0, 6.0, 50)] + [(s*xx, 6.0, t) for xx, t in ((2,106),(3,115),(5,92)) for s in (1,-1)]

for name, coils in (("single center loop (a=6.5)", single), ("totient ring set (a=6)", totient)):
    rp = profile(coils, Xs)
    dev = (rp - r_par)/r_par
    print(f"{name}: level set through throat (0,1)  [Rosensweig: interface = |B| level set, zero-g]")
    for X, a_, b_ in zip(Xs, rp, r_par):
        print(f"   X={X:4.1f}: r_phys={a_:7.4f}   r_parabola={b_:7.4f}   dev={100*(a_-b_)/b_:+6.2f}%")
    print(f"   max |dev| = {100*np.nanmax(np.abs(dev)):.2f}%\n")
