# Gravity v15.190 — Independent ADM spatial trace 2k residual zero

Date 2026-10-30. Gravity parents v15.188 corrected traceless coefficient, v15.189 corrected forcing, Audit v15.182; concurrent Lane A v15.189 protected. Build-2, k>0, κC=1, a=t/sqrt(3), shift=0, conformal spatial f=1−2ψ.

Exact ADM trace evolution with positive Kij=dot h_ij/(2N), K^i_j=Vδ^i_j and V=(H−dotψ/f)/N:
3 dotV = D²N −3N V² −(2/3) sum(dotφI²)/N.
D²N=(Nzz+ωz Nz)/(a²f), ω=log(f)/2. Background gives −3/t²=−3H².

First-order P=(-k²p+td)/(3k²(1+k²)), A=((3k²+4)p+td)/(3k²(1+k²)), d=dotp, dotd=−3d/t−(3k²+4)p/t², D=dotP.
2k metric/lapse X,Y per v15.142 corrected q forcing E_corr v15.189. Define V1=−D−H A, V2=−dotX−H Y + [(A−2P)D+H A²]/2.
The cos2k trace residual is
R=3dotV2+(4k²Y+k²P A/2)/a²+3[2H V2+(V1²+2AHV1)/2+H²Y]−d²/(3k²).
Independent SymPy chain differentiation (including qdd and qddd from corrected forcing and first-order oscillator) yields EXACTLY factor(together(R))=0. This supplies previously missing trace equation for fixed k>0, 2k harmonic, in the restricted ansatz. Combined with audited R416 scalar wave W=0 and previous constraints/traceless closure: 2k scalar harmonic consistent. Source-native original-action reproduction, homogeneous 0-mode trace, multimode superposition, anisotropy/vector/tensor, IR uniformity, full nonlinear stability remain OPEN. Do not generalize.

Next: reproduce ADM trace against original corrected action and solve homogeneous second-order spatial trace equation alongside v15.124 homogeneous Hamiltonian. External audit requested. Other lanes and Suzuki parked weld untouched.
