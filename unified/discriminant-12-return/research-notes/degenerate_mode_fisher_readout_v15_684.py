#!/usr/bin/env python3
"""v15.684: two-mode Fisher/readout model for the v15.683 dispersion family.

The model treats u=m_T^2/omega^2 as the small dispersion parameter and
marginalizes the unknown common GW/source amplitude.  It derives coherent
amplitude and incoherent power limits, then ranks the exact odd-index
swapped-mode family under equal absolute noise.

This is a detector-statistics toy, not a complete amplifier/thermal-noise
budget and not a K4 source prediction.
"""
import math
import sympy as s

# ----------------------------------------------------------------------
# Gate 223: coherent amplitude/complex-voltage Fisher matrix.
# y_i = A g_i(u) + n_i, g_i(u)=g_i[1+a_i u+O(u^2)]
# ----------------------------------------------------------------------
A,g1,g2,sg1,sg2,a1,a2=s.symbols(
    "A g1 g2 sigma1 sigma2 a1 a2", positive=True, real=True
)
FAA=g1**2/sg1**2+g2**2/sg2**2
FAu=A*(g1**2*a1/sg1**2+g2**2*a2/sg2**2)
Fuu=A**2*(g1**2*a1**2/sg1**2+g2**2*a2**2/sg2**2)
Fmarg=s.factor(Fuu-FAu**2/FAA)
Fmarg_expected=s.factor(
    A**2*g1**2*g2**2*(a1-a2)**2/(g1**2*sg2**2+g2**2*sg1**2)
)
assert s.simplify(Fmarg-Fmarg_expected)==0

rho1,rho2,alpha=s.symbols("rho1 rho2 alpha", positive=True, real=True)
sigma_u=s.sqrt(rho1**-2+rho2**-2)/alpha
# Equivalent inverse-Fisher form.
Finrho=s.simplify(alpha**2*rho1**2*rho2**2/(rho1**2+rho2**2))
assert s.simplify(sigma_u-1/s.sqrt(Finrho))==0

# ----------------------------------------------------------------------
# Gate 224: power readout.
# p_i=P0 g_i(u)^2+epsilon_i, so log slope is 2 a_i.
# With power SNR varrho_i=P0 g_i^2/tau_i:
# sigma_u=(1/(2|alpha|))*sqrt(varrho1^-2+varrho2^-2).
# ----------------------------------------------------------------------
vr1,vr2=s.symbols("varrho1 varrho2", positive=True, real=True)
sigma_u_power=s.sqrt(vr1**-2+vr2**-2)/(2*alpha)

# ----------------------------------------------------------------------
# Gate 225: correlated log-calibration errors.
# q=ln s1-ln s2 has slope alpha for amplitude and 2 alpha for power.
# ----------------------------------------------------------------------
c,slog1,slog2=s.symbols("c slog1 slog2", real=True)
var_log_ratio=s.simplify(slog1**2+slog2**2-2*c*slog1*slog2)
assert s.simplify(var_log_ratio.subs({c:1,slog1:slog2}))==0

# ----------------------------------------------------------------------
# Exact swapped-mode geometry from v15.683.
# ----------------------------------------------------------------------
def common_cos(m,n):
    N=m*m+n*n
    return abs(math.sin(math.pi*(math.sqrt(N)-m)/2.0))

def g_massless(m,n):
    return 8.0*m*common_cos(m,n)/(math.pi**2*n**3)

def slope(m,n):
    N=m*m+n*n
    return abs(N*(1.0/n**2-1.0/m**2))

rows=[]
for m in range(3,100,2):
    for n in range(1,m,2):
        aa=slope(m,n)
        gw=min(g_massless(m,n),g_massless(n,m))
        # Equal absolute coherent-voltage noise -> weak-mode SNR propto gw.
        voltage_proxy=aa*gw
        # Equal absolute power noise -> weak-mode power SNR propto gw^2.
        power_proxy=aa*gw**2
        rows.append((m,n,aa,gw,voltage_proxy,power_proxy))

vbest=sorted(rows,key=lambda r:r[4],reverse=True)
pbest=sorted(rows,key=lambda r:r[5],reverse=True)

assert vbest[0][0:2]==(3,1)
assert pbest[0][0:2]==(5,3)

print("coherent amplitude readout:")
print("  sigma_u = sqrt(rho1^-2+rho2^-2)/|alpha|")
print("  weak-mode limit sigma_u ~ 1/(|alpha| rho_weak)")
print("power readout:")
print("  sigma_u = sqrt(varrho1^-2+varrho2^-2)/(2|alpha|)")
print("  equal absolute power noise penalizes weak overlap as g_weak^2")
print("correlated log-calibration:")
print("  Var[ln(s1/s2)] = s1^2+s2^2-2 c s1 s2")
print("  exactly common multiplicative calibration cancels in the ratio")

print("\ntop coherent-voltage geometry proxies |alpha| g_weak:")
for m,n,aa,gw,vp,pp in vbest[:8]:
    print(f"  ({m},{n}) alpha={aa:.9f} gweak={gw:.9e} proxy={vp:.9e}")

print("\ntop power geometry proxies |alpha| g_weak^2:")
for m,n,aa,gw,vp,pp in pbest[:8]:
    print(f"  ({m},{n}) alpha={aa:.9f} gweak={gw:.9e} proxy={pp:.9e}")

print("PASS: marginalized two-mode Fisher limit and readout-dependent geometry ranking")
