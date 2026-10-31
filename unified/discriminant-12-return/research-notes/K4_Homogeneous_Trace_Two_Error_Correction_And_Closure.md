# Gravity v15.224 — Two independent errors in v15.191 homogeneous ADM trace; corrected residual zero

2026-10-31. Gravity parents v15.118 (certified mean Hamiltonian source), v15.124 (homogeneous Hamiltonian quadrature), v15.190 (2k spatial trace), v15.191 (homogeneous trace diagnostic), and audit R418 v15.193 (did NOT independently rederive v15.191). Live HEAD checked v15.223 before work. Other lanes and Suzuki physical quarter untouched.

FIRST GATE: independently verify mean source F0 from exact conformal ADM Hamiltonian. With f=1−2εPcos kz, N=1+εAcos kz, beta=0, H=1/t, a²=t²/3, triplet φ³=z+εp sin kz/k, d=pdot, D=dotP, exact V=(H−dotψ/f)/N and Hamiltonian R3+6V²−2κρ=0. The full quadratic spatial mean from direct expansion:
F0=−5k²P²/a²+3[(D+HA)²+2H(HA²+(A−2P)D)]−(p²+4Pp+12P²)/(3a²)−d²/(3k²).
Substitute audited P=(-k²p+td)/[3k²(1+k²)], A=((3k²+4)p+td)/[3k²(1+k²)], d_dot=−3d/t−(3k²+4)p/t². SymPy checked F0 EXACTLY equals certified v15.118 polynomial (difference 0). So do NOT retract F0 or v15.124 quadrature.

SECOND GATE: independently compute spatial mean of exact lapse Laplacian D²N=(N_zz+ω_z N_z)/(a² f), ω=log(f)/2. At order ε², N_zz=-εk²A cos kz; 1/f=1+2εP cos kz; ω_z=+ε kP sin kz; N_z=−ε kA sin kz. Thus
⟨D²N⟩₂=[⟨−2k²AP cos²⟩+⟨−k²AP sin²⟩]/a²=−3k²AP/(2a²)=−9k²AP/(2t²).
The v15.191 residual included +3k²AP/(2t²) after moving −D²N to LHS; correct is +9k²AP/(2t²), i.e. correction +3k²AP/t². Separately the exact trace equation written in v15.191, 3dotV−D²N+3NV²+(2/3)dotφ²/N=0, demands POSITIVE contribution +d²/(3k²) to the quadratic mean, since ⟨dotφ³²⟩₂=d²/(2k²). v15.191 printed NEGATIVE −d²/(3k²), a sign transcription error. Correction +2d²/(3k²).

THIRD GATE: v15.191's printed old polynomial R_old=[−(2k⁴+4k²+3)t²d²−2(k²+2)t p d+(3k⁴+4k²)p²]/[3k²t²(1+k²)²] is independently verified to obey
R_old + 3k² P A/t² + 2d²/(3k²)=0
identically (SymPy exact factor). Intermediate residual after only lapse correction = −2d²/(3k²), displaying independence of the two errors. Thus previously reported obstruction is RETRACTED. The homogeneous conformal m(t)=⟨ψ₂⟩ and n(t)=⟨α₂⟩ enter the mean Hamiltonian d(tm)/dt=t²F0/12−n (v15.124), and the CORRECTED mean ADM trace is automatically satisfied once that constraint and the source-certified linear mode hold. Choosing n=0 and the exact v15.124 quadrature supplies one explicit response; fixed k, F0=O_k(t^-4), future-normalized m=O_k(t^-2). This is a restricted order-2 zero-mode scalar-sector check, not arbitrary full solutions.

The quadratic one-standing-wave harmonics are 0 and ±2k. The ±2k constraint/traceless/wave/trace closure was independently verified in external Audit Round 418 v15.193 (after v15.138 correction). With corrected zero-mode trace, this provides a FORMAL complete order-2 scalar standing-wave Fourier harmonics closure in the source build-2 conformal, zero-shift ansatz at fixed k>0, PROVIDED the homogeneous scalar wave / zero-mode momentum and full spatial off-diagonal components are separately checked; parity suggests zero scalar-wave mean and global momentum, but do not promote without explicit check. Even when they hold, this does not imply full generic multimode nonlinear Einstein evolution, a build-3 original-action certificate, or uniform IR/future stability.

REPRODUCER SymPy minimal:
import sympy as s
k,t,p,d=s.symbols("k t p d", nonzero=True, real=True)
P=(-k*k*p+t*d)/(3*k*k*(1+k*k))
A=((3*k*k+4)*p+t*d)/(3*k*k*(1+k*k))
Rold=(-(2*k**4+4*k*k+3)*t*t*d*d-2*(k*k+2)*t*p*d+(3*k**4+4*k*k)*p*p)/(3*k*k*t*t*(1+k*k)**2)
assert s.factor(Rold+3*k*k*P*A/t**2)==-2*d*d/(3*k*k)
assert s.factor(Rold+3*k*k*P*A/t**2+2*d*d/(3*k*k))==0

AUDIT HANDOFF: independently derive exact quadratic mean D²N and scalar kinetic term from full ADM action, and independently certify corrected R0 zero; then check homogeneous scalar equation and complete second-order standing-wave harmonics. This note supersedes v15.191 obstruction claim without deleting original historical entry. All other lanes protected.
