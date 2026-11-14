# Cone Derivation Ledger v15.984 — Reuse existing opposing rotor acceleration parabolas to test EM saddle/transition rate

**Date:** 2026-11-14, Gravity. **Prompt:** user rightly insists existing acceleration/deceleration parabolas, requests direct test with Schwinger transition spectrum instead of introducing new oscillator. **Parents:** v15.897 outer osculating parabola; v15.898 conditional Lorentz energy/rest-circle dictionary; v15.899 angular-momentum-conserving rotor; v15.900 actual conditional radial force and two turning-point time parabolas; v15.906/968 J± fixed-D edge spectrum; v15.909 local circle/parabola; v15.983 null-boundary inverse-gamma rewrite. **Latest Audit:** Round 580/v15.980 confirmed through v15.979. **Prewrite live HEAD:** 561b9cec40af3c8774e5538ec2ad577444fb6fc6, exact script; target checked absent. Additive-only, certified, Audit and Suzuki work unchanged.

**Status:** [D] exact v15.900 rotor radial and azimuthal dynamics; [C] proposed physical bridge r/ri=gamma and EM normalized amplitude 1/gamma; [N] the rotor's radial/rapidity angle is not a constant-rate circle nor constant longitudinal force motion; [N] rotational energy law is different from relativistic particle kinetic energy; [O] genuine EM/G field-derived mapping and response.

## Gate 791 — mechanical equations already fixed by v15.900's conditional model

Reuse, do not substitute: a constant-inward-force rotor with mass M, angular momentum L and physical radii ri and ro=Gamma ri. Its Hamiltonian is H=M rdot²/2+L²/(2Mr²)+F0 r. Matching both radii as zero-radial-speed turning points yields

**F0=L²(Gamma+1)/(2M ri³ Gamma²)**.

Let dimensionless rho=r/ri, tau=t L/(M ri²), f=F0 M ri³/L²=(Gamma+1)/(2Gamma²), and energy e=1/2+f. Then

**(d rho/d tau)²=(Gamma−rho)(rho−1)(Gamma rho+Gamma+rho)/(Gamma² rho²)**.

For ri<r<ro this is positive, and both turning points are genuine. The physical radial parabolas from v15.900 have accelerations of opposite sign:
**ri_ddot (M²ri³/L²) = (Gamma−1)(2Gamma+1)/(2Gamma²)>0**;
**ro_ddot (M²ri³/L²) = −(Gamma−1)(Gamma+2)/(2Gamma³)<0**.

No identification with the different geometric osculating parabola of v15.897 is implicit.

## Gate 792 — a chosen Lorentz radial coordinate yields a squared AMPLITUDE–azimuthal clock identity

For comparison *only*, identify **gamma(r)=r/ri=rho**, **beta(r)=sqrt(1−rho^(−2))**, normalized EM Schwinger transition amplitude **A(r)=sqrt(1−beta²)=1/rho**. This applies v15.898's ratio to a continuously changing physical rotor radius rather than only its two selected circles: this extension is **an assumption**, not derived from a field action.

The actual rotor azimuthal angular rate is

**phi_dot=L/(Mr²)**, so **phi_dot(r)/phi_dot(ri)=rho^(−2)=A(r)²**,

and the rotor rotational energy at constant L also obeys **Krot(r)/Krot(ri)=rho^(−2)=A(r)²**. This is an exact standard fixed-L rotor relation after the chosen gamma map. It is not the relativistic particle's K_rel/(mc²)=rho−1. The two kinetic energies have *opposite radial slope*: as radius increases, Krot decreases whereas putative K_rel increases. Equating the two is false without additional energy-transfer account.

For the n=4 primitive pair, Gamma=5/4. At inner turning point A=1, phi_dot/phi_dot_i=1. At outer A=4/5, phi_dot/phi_dot_i=16/25. This connects the previously exact Schwinger edge k=1, D=5 value |J+|=2 relative to T=5/2, hence 4/5. However a prescribed physical angular speed is not a transition frequency/EM rate; the identifying coupling remains absent.

## Gate 793 — the *radial* parabola clock is not the EM ladder clock

Define a distinct conditional rapidity/radial angle **chi=arccos(ri/r)** so cos chi=A=1/rho, sin chi=beta. Then dr/dt=r tan chi * dchi/dt. The dimensionless radial-angle speed from the already-fixed rotor Hamiltonian is exactly

**(dchi/dtau)²=(Gamma−rho)(Gamma rho+Gamma+rho)/(Gamma² rho^4(rho+1))**.

It approaches **(Gamma−1)(2Gamma+1)/(2Gamma²)>0** at the inner bounce, if a signed branch of chi is used there; at the outer turning point **dchi/dtau=0** while A=1/Gamma>0. The apparent arccos derivative at inner requires a signed branch through the radial reversal; v15.900 already noted the degeneracy of r=ri cosh(s) at the seat. This angle chi is NOT the actual rotor azimuth phi.

Consequently neither constant circle-angle speed dchi/dt=Omega nor the standard constant-longitudinal-force rule dchi/dt=(F/mc)cos² chi can agree with BOTH inner and outer turning behavior for nonzero Omega or F. A constant force has strictly nonzero dchi/dt for finite gamma at outer turning, contradicting the rotor bounce. This tests the earlier conjecture that outer circle acceleration parabola plus EM saddle amplitude automatically determines time-rate.

The n=4, ri=1, ro=5/4, M=L=1 control (v15.900) has f=18/25, radial accelerations +7/25 and −26/125, and **chi_prime²(inner)=7/25, chi_prime²(outer)=0**, while **A_outer=4/5**. The actual radial-angle rate vanishes at the outer turning radius despite the nonzero EM J+ transition amplitude there.

## Gate 794 — discrete transition sampling and proper scope of the identity

Under this chosen gamma map, each edge k of the D=n+1 Schwinger ladder would correspond to rho_k=D/[2sqrt(k(D−k))]. For n=4, D=5, the k=1,4 edges are rho=5/4 (the outer rotor turning points), while k=2,3 edges are rho=5/(2sqrt6) strictly inside the rotor excursion. The continuous seat rho=1 would require k=D/2=5/2, not an integer transition edge. Thus the actual v15.900 rotor can **sample** the ladder envelope as a radial geometric curve, yet no natural physical abrupt transitions, emissions, oscillator frequencies, source power or energy jumps are specified at those radial stations.

The two-circle geometry *is already rich enough* to produce consistent conditional radii and acceleration parabolas, but the symmetry and turning-point dynamics are not the EM transition Hamiltonian. The basic Schwinger ladder J± has off-diagonal transitions, while the rotor's conserved L and classical radial H involve no corresponding operator that changes k. A measured EM→gravity conversion law, rate or new dimensionless observable has not been derived.

**Verification:** additive source `research-notes/k4_rotor_transition_parabola_v15_984.py`, commit **561b9cec40af3c8774e5538ec2ad577444fb6fc6**. Local exact SymPy **PASS** before commit: factored radial energy function, radial chi² law, both endpoint limits, n=4 values and D=5 edge sampling; no other-lane files changed. Independent Audit pending.

**Next gate:** instead of replacing the rotor or acceleration parabolas, derive a candidate *real field-sourced* coupling from Maxwell/K4 that connects the operator J± to the radial action, or prove the existing conserved-source equations preserve diagonal k and force the mixed matrix element to zero. Compare its frequency and polarization resolved response against the matched ordinary GR+EM model; do not import measured G or an arbitrary drive strength as a prediction.

**HANDOFF Audit/Muse:** separately verify true rotor azimuth phi versus mapped rapidity chi, signed branches at inner turning, radial angle endpoint mismatch, kinetic-energy monotonicity, and D=5 noninteger saddle k=5/2.
