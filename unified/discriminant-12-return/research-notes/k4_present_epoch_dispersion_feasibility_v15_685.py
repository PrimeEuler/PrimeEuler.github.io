#!/usr/bin/env python3
"""v15.685: present-epoch K4 tensor-dispersion scale and Fisher feasibility.

Uses the certified K4 tensor relation m_T^2=(8 eta/3) H^2 with
3/8 < eta <= 3/2 and the independently verified fact that H is the FLRW
cosmological expansion rate.  For a present-epoch scale example this script
uses H0=73.50 km/s/Mpc (2026 H0 Distance Network central value).

No measured Newton G enters these dimensionless ratios.  This is a scale
diagnostic, not an endorsement of the observationally disfavored exact K4
coasting cosmology.
"""
import math

MPC_M=3.08567758149e22
H0_KM_S_MPC=73.50
H0=H0_KM_S_MPC*1000.0/MPC_M  # s^-1
ETA_MIN=3.0/8.0
ETA_MAX=3.0/2.0
ALPHA_31=80.0/9.0  # v15.683 swapped (3,1)/(1,3) coherent-ratio slope

def u_range(f_hz):
    omega=2.0*math.pi*f_hz
    base=(H0/omega)**2
    # 8 eta/3 ranges from 1 (open lower edge) to 4.
    return base,4.0*base

def rho_weak_required(u,alpha=ALPHA_31):
    # Favorable weak-mode Fisher limit sigma_u ~= 1/(|alpha| rho_weak);
    # requiring sigma_u <= u gives this minimum.
    return 1.0/(abs(alpha)*u)

print(f"H0 = {H0:.12e} s^-1 for {H0_KM_S_MPC:.2f} km/s/Mpc")
print("K4 stable-window m_T/H = sqrt(8 eta/3) lies in (1,2]")
print("u=m_T^2/omega_g^2 lies in ((H/omega_g)^2, 4(H/omega_g)^2]")

freqs=[1e-3,1.0,1e3,1e6,1e8,1e9]
print("\nfrequency scale:")
for f in freqs:
    umin,umax=u_range(f)
    rho=rho_weak_required(umax)
    print(
        f"  f_g={f:.3e} Hz: u in ({umin:.3e}, {umax:.3e}], "
        f"best-case rho_weak(3,1) >= {rho:.3e}"
    )

print("\nGW frequency needed for a chosen favorable upper-edge u (eta=3/2):")
for target in (1e-6,1e-12,1e-18,1e-24,1e-30):
    # target = 4 (H/omega)^2
    omega=2.0*H0/math.sqrt(target)
    f=omega/(2.0*math.pi)
    period=1.0/f
    years=period/(365.25*86400.0)
    print(
        f"  u={target:.0e}: f_g={f:.3e} Hz, "
        f"period={period:.3e} s = {years:.3e} yr"
    )

# Exact scale assertions for regression.
umin_1k,umax_1k=u_range(1e3)
assert 1e-44 < umin_1k < 2e-43
assert 5e-43 < umax_1k < 6e-43
umin_100m,umax_100m=u_range(1e8)
assert 1e-54 < umin_100m < 2e-53
assert 5e-53 < umax_100m < 6e-53
_,umax_mhz=u_range(1e-3)
assert 5e-31 < umax_mhz < 6e-31
assert rho_weak_required(umax_mhz) > 1e29

print("\nPASS: certified cosmological-H K4 mass gives extreme present-lab suppression")
