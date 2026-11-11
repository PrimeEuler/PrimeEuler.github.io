#!/usr/bin/env python3
"""v15.683: degenerate swapped-mode sensitivity/overlap tradeoff.

For the centered PEC cube and TT magnetostatic source of v15.682, every
odd-index pair (m,n) has a degenerate partner (n,m).  This script derives
the exact normalized timelike-dispersion slope and quantifies the loss of
the weaker massless overlap when that slope is made large.

The simple alpha*min(|G|) quantity printed below is only a geometry proxy,
not an experimental SNR or sensitivity.
"""
import math
import sympy as s

u=s.symbols("u", real=True)
m,n=s.symbols("m n", positive=True)

N=m*m+n*n
# Ratio R=(m,n)/(n,m), normalized to its massless value (m/n)^4.
D=s.simplify((1-N*u/m**2)/(1-N*u/n**2))
alpha=s.simplify(s.diff(D,u).subs(u,0))
alpha_closed=s.simplify(N*(1/n**2-1/m**2))
assert s.simplify(alpha-alpha_closed)==0

def common_cos(m,n):
    # m,n odd.  Stable form of |cos(pi*sqrt(m^2+n^2)/2)|.
    N=m*m+n*n
    return abs(math.sin(math.pi*(math.sqrt(N)-m)/2.0))

def g_massless(m,n):
    # |G_mn(K=omega)| for E_mn=2 zhat cos(mx)cos(ny).
    c=common_cos(m,n)
    return 8.0*m*c/(math.pi**2*n**3)

def slope(m,n):
    N=m*m+n*n
    return N*(1.0/n**2-1.0/m**2)

# Exact low-order examples.
assert s.simplify(alpha_closed.subs({m:3,n:1})-s.Rational(80,9))==0
assert s.simplify(alpha_closed.subs({m:5,n:3})-s.Rational(544,225))==0

examples=[(3,1),(5,3),(5,1),(7,1)]
for mm,nn in examples:
    gs=g_massless(mm,nn)
    gw=g_massless(nn,mm)
    a=slope(mm,nn)
    print(
        f"(m,n)=({mm},{nn}) alpha={a:.9f} "
        f"|G_mn|={gs:.9e} |G_nm|={gw:.9e} "
        f"R0={(mm/nn)**4:.9e} proxy={a*min(gs,gw):.9e}"
    )

# Scan exact swapped degeneracies.  The proxy rewards a large dimensionless
# dispersion slope while penalizing a vanishing reference overlap.
rows=[]
for mm in range(3,100,2):
    for nn in range(1,mm,2):
        a=slope(mm,nn)
        g1=g_massless(mm,nn)
        g2=g_massless(nn,mm)
        rows.append((a*min(g1,g2),a,min(g1,g2),mm,nn,g1,g2))
rows.sort(reverse=True)

print("top alpha*min(|G|) geometry proxies for odd indices <100:")
for proxy,a,gmin,mm,nn,g1,g2 in rows[:10]:
    print(
        f"  ({mm},{nn}) alpha={a:.9f} minG={gmin:.9e} "
        f"proxy={proxy:.9e}"
    )

# Fixed-n, m->large odd asymptotics:
# sqrt(m^2+n^2)-m = n^2/(sqrt(m^2+n^2)+m) ~ n^2/(2m),
# so common_cos ~ pi*n^2/(4m).
# Therefore G_mn -> 2/(pi*n), G_nm ~ 2*n^3/(pi*m^4),
# alpha ~ m^2/n^2, and alpha*G_nm ~ 2*n/(pi*m^2) -> 0.
mm=9999
nn=1
gs=g_massless(mm,nn)
gw=g_massless(nn,mm)
a=slope(mm,nn)
assert abs(gs-2/math.pi) < 1e-7
assert abs(mm**4*gw-2/math.pi) < 1e-6
assert abs(a/mm**2-1.0) < 1e-7
assert a*gw < 1e-8

print("large-m n=1 check:")
print("  G_strong -> 2/pi =",gs)
print("  m^4 G_weak -> 2/pi =",mm**4*gw)
print("  alpha/m^2 -> 1 =",a/mm**2)
print("PASS: unbounded ratio slope is paid for by a vanishing reference-mode overlap")
