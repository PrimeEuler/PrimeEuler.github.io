# v15.011: joint Hamiltonian–momentum ADM constraints, regular linear lapse pivot

Date 2026-10-27. Parent v15.010; live HEAD checked. Gravity-only additive, protected separate Muse/Suzuki work untouched.

Choose ADM metric signature +---, Kij=(dot hij−Di Nj−Dj Ni)/(2N), h=a²(δ+ε), N=1+α, N^i=β^i, phiI=zi+πI, κC=1, a=τ/√3, H=1/τ. Exact constraints:
H_GR := R3+K²−KijKij−2κ ρ_n=0,
ρ_n=(C/3)Σ_I[(dotφI−N^j∂jφI)²/N²+h^ij∂iφI∂jφI].
Momentum H_i=−2 h_ij DkΠjk+pI∂iφI=0 with Πjk=√h(Kjk−hjkK)/(2κ), pI=(2C/3)√h(dotφI−N^j∂jφI)/N.

Background R3=0,Kij=Hhij so K²−KijKij=6H²; ρ_n=C/a², 2κρ=2κC/a²=6H².

At first order R3(1)=a^-2(∂i∂jεij−Δ trε), δK=dot(trε)/2−divβ−3Hα, δ(K²−Kij²)=4HδK=2Hdot(trε)−4Hdivβ−12H²α. Matter δρ=(C/3a²)(2divπ−trε). Hence H_GR(1)=R3(1)+2Hdot(trε)−4Hdivβ−12H²α−4H²divπ+2H²trε=0. Nonzero algebraic lapse pivot -12H² for τ>0, no k^-2 needed to solve α from this equation for prescribed other fields. This does NOT by itself fix shift or show full coupled matrix invertible, and lapse formula may grow with τ due to 1/H²; late-time uniform estimates are open.

At perturbative degree two H_GR(2)=R3(2)+[K²−KijKij](2)−2κρ_n(2)=0 and H_i(2) explicitly supplied by v15.010. The second-order constraints are linear in unknown second-order α2,β2,ε2,π2, etc with known bilinear source from first-order fields. The coefficient of α2 remains -12H², so second-order Hamiltonian constraint admits algebraic solving for α2 after other unknown fields and quadratic sources specified. No explicit full second-order expansion of R3, inverse metric, K or shift solve performed, no claim complete second-order operator bounds or IR stability. A zero-mode integrated global constraint and momentum/current boundary conditions remain necessary. On spatial torus phiI=zi requires winding fields/internal compact labels or boundary formulation.

NEXT: assemble gauge-fixed combined linear constraint matrix (scalar and transverse vector) with exact second-order source operators, including k=0 and time-uniform weighted Sobolev estimates; avoid claim linear lapse pivot suffices for stability.
