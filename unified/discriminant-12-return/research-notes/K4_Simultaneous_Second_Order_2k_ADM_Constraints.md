# v15.137 — Simultaneous fixed-k second-order 2k Hamiltonian and momentum constraint solve

Date: 2026-10-29. Gravity parents v15.107, v15.118 (Sandbox source-certified build-2 first order), v15.124 homogeneous Hamiltonian, v15.131 local momentum. Latest live HEAD checked v15.136. Muse v15.135 phase/ladder/Casimir classification read: two sector Casimir residue classes, no claim physical weld; separate lane protected.

Gauge and definitions: spatial h_ij=a²(1−2ψ)δij, N=1+α, contrav shift zero, κC=1, a=t/√3, H=1/t. First-order standing wave ψ=ε Ψ(t)cos kz, α=ε A(t)cos kz, φ3=z+ε p(t)sin kz/k, πdot=d. Certified build-2 reconstruction Ψ=(−k²p+t d)/[3k²(1+k²)], A=[(3k²+4)p+t d]/[3k²(1+k²)], d_dot=−3d/t−(3k²+4)p/t²; D:=dotΨ=[−(k²+2)d−(3k²+4)p/t]/[3k²(1+k²)]. All k>0.

Coefficient of cos(2kz) in complete quadratic Hamiltonian source v15.107 (β1=0):
F2=−11 k² Ψ²/a² +3D²+12H(A−Ψ)D+9H²A² +d²/(3k²)−(p²+4Ψp+12Ψ²)/(3a²).
SymPy exact factor with a²=t²/3:
F2=[−(3k^8+13k^6+15k^4+16k²)p²+(8k^4−6k²+8)t p d+(k^6+3k^4−6k²+3)t²d²]/[3k^4t²(1+k²)²].
This is the cos2 harmonic, not the mean F0 of v15.118. Matter kinetic d² sin²/k² yields plus sign in F2 and minus sign in F0, and conformal curvature gives −11 k²Ψ²/a² in F2 vs −5 k²Ψ²/a² in F0.

From v15.131, local momentum source sin2k is (a³/κ)Q sin2k with
Q=[−(3k²+7)t²d²+(3k^6+13k^4+6k²−12)t p d+(12k^4+16k²)p²]/[9k³t(1+k²)²].
Independently checked exact Q identity against the unexpanded v15.131 formula using SymPy, difference=0.

For second-order corrections ψ2=X(t)cos(2kz), α2=Y(t)cos(2kz), π2=0, β2=0, linear Hamiltonian correction harmonic is
H1[U2]_(cos2k)=−12/t²[(4k²+1)X+t dotX+Y].
Linear momentum correction harmonic is (2a³/κ)[2k(dotX+Y/t)]sin2k.
Therefore simultaneous local second-order constraints H1+H2=0 and momentum M1+M2=0 read
(4k²+1)X+t dotX+Y=t²F2/12,
dotX+Y/t=−Q/(4k).
These are compatible for every fixed k>0, and explicitly solved by
X=[t²F2/12+t Q/(4k)]/(4k²+1),
Y=−t dotX−t Q/(4k).
SymPy exact simplification of X yields
X=[−(3k^8+13k^6+3k^4)p²+(3k^6+21k^4−4)t p d+(k^6+3k^4−9k²−4)t²d²]/[36k^4(1+k²)²(4k²+1)].
Symbolic reconstruction residual (4k²+1)X−t²F2/12−tQ/(4k) =0 exactly. Both constraints therefore vanish by construction; Y involves time derivative evaluated using certified p equation. No need to posit second-order scalar strain or shift to solve THESE TWO local constraint harmonics in this conformal gauge. Homogeneous/zero Fourier mode handled separately by v15.124; no claim higher harmonics or multi-mode closure beyond this restricted standing wave.

Important boundaries: lapse Y chosen as algebraic response not arbitrary time gauge; conformal spatial gauge and φ2=β2=0 may fail to be preserved by Einstein spatial evolution. This solves 2k constraint equations on a chosen slice/family, NOT the full second-order Einstein-matter evolution. k→0 singular X∼k^-4 for generic data, no uniform IR estimate; no nonlinear future stability or physical gravitational theory claim. Periodic scalar φ³ winding/background requires appropriate target/boundary convention. Original source scalar build-2 certification v15.118 used; build-3 auxiliary signature not independently checked. Muse Casimir sector algebra independent of present continuous gravity scalar.

Next: compute second-order 2k metric evolution residual (spatial trace and traceless equations), test if conformal/no-shift/no-matter2 corrections propagate, and examine IR weighted class; independent audit of F2 and simultaneous constraints needed.
