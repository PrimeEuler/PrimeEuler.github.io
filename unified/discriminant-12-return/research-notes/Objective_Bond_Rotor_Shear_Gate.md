# Objective bond–rotor interaction: recover positive shear without laboratory pinning

Date 2026-10-24. Parents v14.626, v14.827–835. Gravity/combinatorics subgate. No Suzuki/far-tail modification.

## 1. Exact objectivity of bond lengths [D]

Consider lattice vertices with positions r_i=R_i+u_i, and each undirected bond ij with equilibrium length ell_ij and unit orientation n_ij=(R_j-R_i)/ell_ij. Let delta ell_ij=|r_j-r_i|-ell_ij. Under any common Euclidean rigid motion r_i→Q r_i+c, Q∈SO(3), delta ell_ij is invariant EXACTLY, not just to linear order. A central-force spring energy E_b=(k_b/2)(delta ell_ij)^2 is objective. Linearizing, delta ell_ij=ell_ij n_i e_ij n_j+O(u²), where e=sym grad u. Such an interaction does not penalize pure rigid rotation.

## 2. Isotropic bond network elasticity [D]

For a homogeneous, isotropically distributed population of central bonds with equal reference length ell, bond number density n_b and spring stiffness k_b>=0, energy per volume at quadratic order is
 W=(n_b k_b ell²/2) <(n·e·n)^2>_sphere.
The rotational average <n_i n_j n_k n_l>=(δijδkl+δikδjl+δilδjk)/15 gives
 W=(n_b k_b ell²/30)[(tr e)^2+2 e:e].
Match to W=(B/2)(tr e)^2+mu dev(e):dev(e), obtaining
 \boxed{mu=n_b k_b ell²/15,\qquad B=n_b k_b ell²/9,\qquad B=5mu/3}.
Hence a positive objective elastic shear emerges from longitudinal bond extension, not from the pinned angular curl term of v14.831. The nonzero mu requires a network with oblique bond orientations, not a single set of axial nearest-neighbor springs (which may have floppy shear modes).

## 3. Internal pendulum rotor in the bond frame [D/O]

Let alpha_b be a *relative* internal rotor libration angle measured against its own co-rotating bond frame. Relative angle and delta ell are invariant under common rigid rotations. A minimal harmonic bond energy is
 E_b=(k_s/2)(delta ell)^2+(K_r/2)alpha_b²+g_b delta ell alpha_b,
 with K_r>0. The linear stability criterion is k_s K_r-g_b²>=0. Static elimination gives alpha_*=-g_b delta ell/K_r and
 \boxed{k_eff=k_s-g_b²/K_r}.
In the isotropically distributed network, mu_eff=n_b ell²(k_s-g_b²/K_r)/15 and B_eff=5mu_eff/3. Thus an internal freely relaxing rotor can modify ordinary shear in an objective way, but it SOFTENS the static spring network. It cannot create positive long-wave shear from k_s=0 with a stable linear cross-coupling g_b≠0. Dynamical rotor inertia would yield k_eff(omega)=k_s-g_b²/(K_r-I_r omega²), valid off resonance, not an instantaneous modulus.

A gravity-driven pendulum may supply a calibrated K_r, but the origin and sign of k_s and g_b from hyperbola geometry remain open; an external gravity source cannot be used to claim that Newton G was derived. This establishes a concrete objective microscopic bridge, not a GR microphysical completion.

## 4. Relativistic matching caveat [O]

If (and only if) objective isotropic spring-network mu_eff can be covariantly coarse-grained to the shear mu_cov of v14.830, its local stability target is rho/6<=mu_eff<=2rho/3. The central-force network also forces B=5mu/3>0, so it does not reproduce the w=-1/3 background by itself. An additional, separately selected negative-pressure background sector would be needed. The matching of nonrelativistic n_b,k_s,K_r,g_b,ell to relativistic energy density and stress tensor remains open.
