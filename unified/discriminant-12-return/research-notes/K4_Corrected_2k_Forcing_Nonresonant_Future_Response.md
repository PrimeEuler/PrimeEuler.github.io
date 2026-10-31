# v15.189 — Corrected quadratic scalar forcing: explicit polynomial and fixed-k nonresonant future response

Date 2026-10-30. Gravity parent erratum v15.188, External Audit v15.182. Live master HEAD checked. All findings in source build-2, conformal zero-shift standing-wave sector at fixed k>0, t>0; spatial TRACE Einstein equation still OPEN. Other lanes protected.

Source-certified first-order strain oscillator pdd+(3/t)pdot+(3k²+4)p/t²=0, so p=t^-1u(s), s=ln(t/t0), u_ss+ω²u=0, ω²=3(k²+1). Let d=pdot. Correct v15.138 traceless source correction is E_corr=E_old+2k² A P, where P=(-k²p+td)/[3k²(1+k²)] and A=((3k²+4)p+td)/[3k²(1+k²)]. Exact polynomial simplifies:
E_corr=−[(4k²+3)t²d²+(24k⁴+50k²+24)t p d+(27k⁶+81k⁴+79k²+24)p²]/[9k²(1+k²)²(1+4k²)].
This algebra has been checked with SymPy and is the corrected replacement for v15.138 old E0 polynomial. In particular E_corr=t^-2 times a quadratic trigonometric polynomial in u,u_s, carrying only log-time harmonics λ=0 and λ=±2ω.

Forced scalar amplitude from v15.142 corrected by v15.188 obeys
qdd+(3/t)qdot+(12k²+4)q/t² = 3(1+4k²)E_corr/t².
Let Ω2²=12k²+3 be the unforced q log-time squared frequency (q=t^-1 v, v_ss+Ω2²v=0). Source decays t^-4 at fixed k. Seek particular q=t^-2 Σ_{λ∈{0,±2ω}} c_λ e^{iλs}; for any harmonic forcing t^-4 f_λ e^{iλs} the Euler operator sends t^-2 e^{iλs} to t^-4 D(λ)e^{iλs}, with
D(λ)=12k²+4−λ²−2iλ.
At λ=0 D=12k²+4>0. At λ=±2ω, λ²=12(k²+1), giving D=−8−2iλ !=0. Thus there is NO quadratic logarithmic resonance of this t^-4 forcing at any k>0. An exact particular solution q_part=t^-2Σ(f_λ/D(λ))e^{iλs} exists and obeys q_part=O_k(t^-2), dotq_part=O_k(t^-3). General solution includes homogeneous O_k(t^-1) oscillations, whose two constants may be set to zero for a future-normalized response; not automatically absent.

Consequences for second-order 2k constraint correction X,Y from v15.142: source F2=O_k(t^-4), Q=O_k(t^-3); X0=(t²F2/12+tQ/(4k))/(1+4k²)=O_k(t^-2), δX=[−q/3+t dotq/(12k²)]/(1+4k²)=O_k(t^-2) on future-normalized particular q, and Y=−t dotX−tQ/(4k)−t dotq/(12k²)=O_k(t^-2). The corrected chain's scalar wave residual W=0 was independently established by Audit v15.182. This is a fixed-k formal second-order constrained/traceless/matter-wave construction, not proof of spatial trace Einstein equation, full nonlinear evolution, spatial Fourier superposition closure, or k-uniform estimates. Coefficients may diverge as k→0. Muse sector algebra and Suzuki quarter physical weld stay separate/PARKED.

NEXT: independent original-action spatial trace Einstein equation, test corrected q/X/Y and Bianchi propagation. External audit requested.
