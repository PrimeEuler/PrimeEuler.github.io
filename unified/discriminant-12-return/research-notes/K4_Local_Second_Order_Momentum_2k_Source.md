# v15.130 — Local second-order 2k ADM momentum source and solvable linear correction
Date 2026-10-29. Parent gravity v15.127, build-2 source certificate v15.118. Check live HEAD before write. Other lanes untouched; Suzuki physical quarter parked.

For conformal h_ij=a² f δij, f=1−2ψ, lapse N=1+α, shift β=0, triplet φI=(x,y,z+π), use exact canonical ADM Π^{ij}=−a√f A δij/κ where A=(H−dotψ/f)/N, p3=(2C/3)a³ f^{3/2}dotπ/N, κC=1. The exact local z momentum constraint is H_z=(2a³ f^{3/2}/κ)[∂z A+(1/3)dotπ (1+∂zπ)/N]. This exact identity follows from −2∂j(h_zkΠ^{kj})+Π^{jk}∂z h_jk+p3∂zφ³, with the conformal-gradient terms canceling between the two grav pieces.

Set ψ=εΨ cos kz, α=εL cos kz, π=ε p sin(kz)/k. Extract first order H_z1=(2a³/κ)[k(dotΨ+HL)+dotp/(3k)] sin kz; source certified Ψ=(−k²p+t dotp)/[3k²(1+k²)], L=((3k²+4)p+t dotp)/[3k²(1+k²)], oscillator pdd+3dotp/t+(3k²+4)p/t² imply H_z1=0 exactly. Second-order H_z2=(a³/κ)Q_k sin2kz with Q_k= k(Ψ dotΨ−2L dotΨ−2H L²−3HΨL)+(dotp/(3k))(p−L−3Ψ). Symbolic simplification (independently executed SymPy) gives
Q_k=[−(3k²+7)t²dotp²+(3k⁶+13k⁴+6k²−12)t p dotp+(12k⁴+16k²)p²]/[9k³ t(1+k²)²].
Generically nonzero; global spatial mean zero by parity as v15.127.

Second-order harmonic ψ2=Ψ2(t)cos(2kz), α2=L2 cos2kz, π2=p2 sin2kz/(2k), β2=0. H_z1[U2]=(2a³/κ)[2k(dotΨ2+H L2)+dotp2/(6k)] sin2kz. H_z1[U2]+H_z2[U1]=0 gives dotΨ2+H L2=−Q_k/(4k)−dotp2/(12k²). Thus e.g. L2=p2=0, Ψ2(t)=Ψ2(t0)−∫Q_k(r)/(4k)dr solves local SECOND-ORDER MOMENTUM harmonic for fixed k>0. This is not simultaneous second-order Hamiltonian solvability or full Einstein evolution, nor IR uniform: Q_k contains k^-3 and correction has k^-4. Additional second-order modes and lapse/shift may be required to satisfy other constraints. No nonlinear stability proof.

Source verification boundary: relies on certified build-2 first-order auxiliary B=0 (v15.118); exact canonical momentum derivation is independent algebra; the Q factor checked with SymPy, not yet externally audited. Next solve nonzero 2k Hamiltonian together with local momentum, scrutinize IR and gauge; independent audit requested.
