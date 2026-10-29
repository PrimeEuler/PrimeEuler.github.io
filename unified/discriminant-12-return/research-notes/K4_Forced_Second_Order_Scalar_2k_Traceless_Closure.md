# v15.141 — Second-order 2k matter scalar repairs traceless Einstein residual via forced oscillator

Date 2026-10-29. Gravity parent v15.138 and v15.137. Muse v15.140 representation-boundary addendum noted, separate sector unchanged. Live HEAD checked. Source build-2 convention: h=a²(1−2ψ)δ, N=1+α, shift=0, κC=1, first-order p standing scalar. k>0.

Add second-order scalar displacement φ³=z+ε p sin(kz)/k+ε² q sin(2kz)/(2k), metric ψ=ε Ψ cos kz+ε² X cos2kz, lapse α=ε A cos kz+ε² Y cos2kz.

Second-order Hamiltonian cos2k and momentum sin2k constraints from previous source F2,Q augmented by linear q:
(4k²+1)X+t dotX+Y+q/3=t²F2/12,
dotX+Y/t+dotq/(12k²)=−Q/(4k).
Let L=4k²+1, X0=(t²F2/12+tQ/(4k))/L, define X=X0+δX, δX=[−q/3+t dotq/(12k²)]/L; Y=−t dotX−tQ/(4k)−t dotq/(12k²). These satisfy both constraint harmonics identically by elementary substitution.

Exact traceless spatial Einstein difference in conformal, zero-shift gauge from v15.138 has E2=4k²(Y−X)−4q/3 + S2(first order), where E0=4k²(Y0−X0)+S2 is v15.138 restricted traceless residual:
E0=−[(12k²+5)t²dotp²+(40k⁴+86k²+32)t p dotp+(3k⁶+43k⁴+71k²+24)p²]/[9k²(1+k²)²(4k²+1)].
Correction exactly
4k²(δY−δX)−4q/3 =−[t² qdd+3t dotq+(12k²+4)q]/[3(4k²+1)].
Verified by independent SymPy symbolic subtraction =0.
Thus E2=0 precisely when
qdd+3 dotq/t+(12k²+4)q/t²=3(4k²+1)E0/t².
Forced oscillator at second-order wavenumber 2k. For any fixed k>0 and smooth p source, linear ODE has local and global (t>0 finite) solutions by standard ODE, with two free homogeneous constants. X,Y then satisfy both second-order local constraints and traceless spatial equation.

CRITICAL SCOPE: This is not proof full second-order Einstein-scalar evolution; spatial trace Einstein equation, scalar wave equation and Bianchi compatibility not yet checked, and selected conformal/zero-shift gauge may exclude physical anisotropic corrections. If other equations require additional degrees, must enlarge ansatz. Fixed k only; X, Y have inverse k powers. No nonlinear future stability, uniform low-k estimate, or physical claim. Original v15.138 traceless E formula independently audited? Not yet: source verify requested. Source v15.118 build2 first-order certified, build3 auxiliaries separate.

Next check second-order scalar wave and spatial trace residuals with forced q and see whether they vanish by Bianchi or imply additional sourced evolution/gauge corrections. External audit requested. Suzuki physical quarter parked; other lanes untouched.
