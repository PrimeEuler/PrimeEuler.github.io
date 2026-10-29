# v15.138 — Traceless spatial Einstein gate rejects restricted 2k constraint ansatz

Date 2026-10-29. Parent gravity v15.137; live HEAD prewrite checked. Source build-2 canonical triplet and conformal spatial gauge.

Exact traceless spatial equation in zero-shift conformal ansatz:
h_ij=a²f δij, f=1−2ψ, ω=(1/2)ln f, N=1+α, φI=(x,y,z+π).
As K^i_j is pure trace, the longitudinal-minus-transverse tracefree spatial Einstein evolution equation reduces (within this ansatz) to
E:=−(D_zD_zN−D_xD_xN)+N[(R3_zz−R3_xx)−(2κC/3)((∂zφ)^2−(∂xφ)^2)]=0.
With κC=1 and transverse background ∂xφ1=1, this is
E=−N''+2ω' N'+N[−ω''+(ω')²−(2/3)(2π'+(π')²)].
At linear order ψ=Ψ cos kz, α=A cos kz, π=p sin kz/k gives E1 cosine k: k²(A−Ψ)−4p/3=0, which source-certified build-2 coefficients satisfy EXACTLY: A−Ψ=4p/(3k²). This provides a direct independent consistency check of signs.

At order ε², with ψ=εΨ cos kz+ε²X cos2kz, α=ε A cos kz+ε²Y cos2kz, π=ε p sin kz/k and shift=0, the cos2k coefficient is
E2=4k²(Y−X)−(3/2)k² A Ψ−(5/2)k² Ψ²−(2/3) A p−(1/3)p².
Insert the v15.137 simultaneous Hamiltonian–momentum solution:
X=[t²F2/12+tQ/(4k)]/(4k²+1), Y=−t dotX−t Q/(4k), with exact F2,Q expressions from v15.137 and first-order oscillator pdd=−3pdot/t−(3k²+4)p/t².
Symbolic factor (direct independently performed SymPy) gives
E2=−[ (12k²+5)t²pdot²+(40k⁴+86k²+32)t p pdot+(3k⁶+43k⁴+71k²+24)p² ]/[9k²(1+k²)²(4k²+1)].
For p=0, pdot≠0 E2=−(12k²+5)t²pdot²/[9k²(1+k²)²(4k²+1)] ≠0. NB earlier preliminary p=0 display −5 alone applies only leading small-k coefficient; retain full (12k²+5) factor. For any k>0 restricted solution generally fails spatial traceless equation. This is a decisive NON-CLOSURE of *restricted corrections* π2=β2=0, conformal metric only, not proof nonlinear constraint non-solvability, instability, or failure of full Einstein system. Allow anisotropic spatial h2, matter π2, or shift, and retest all Einstein equations including trace and scalar-wave evolution.

Important: metric convention + K sign and matter coefficient checked against exact linear anisotropy relation. Audit full nonlinear spacetime decomposition explicitly; current source zero-shift spatial tracefree identity assumes pure-trace K and expected standard ADM evolution equations. No claim independent external verification yet. Suzuki physical-quarter weld parked, other lanes untouched.
