# v15.117 — Conditional single-mode quadratic Hamiltonian zero mode
Date 2026-10-29. Parent v15.114. Latest live HEAD checked. Original-action EL residuals still OPEN.

In source spatial gauge h=a²(1−2ψ)δ, lapse N=1+α, shift β=0 conditionally, scalar triplet φ³=z+p(t)sin(kz)/k, k>0. Audited ψ=(-k²p+t pdot)/(3k²(1+k²)), oscillator pdd+3pdot/t+(3k²+4)p/t²=0. Translated-constraint candidate α=[(3k²+4)p+t pdot]/[3k²(1+k²)] and b=0, as in v15.114. Independent direct linear Hamiltonian in source-sign convention α=−(1+k²)ψ−tψdot−p/3 reproduces candidate algebraically. Scalar-wave residual on oscillator is zero. However original source scalar_final2.py EL_B,EL_Phi residuals NOT executed. Candidate remains conditional; source B=0 not certified.

For one real cosine k mode, using full v15.107 Hamiltonian quadratic source and β=0, spatial average equals
< H2 >=−5k²ψ²/a²+3ψdot²+12H(α−ψ)ψdot+9H²α²−pdot²/(3k²)−(p²+4ψp+12ψ²)/(3a²),
a²=t²/3, H=1/t. Substitute exact ψ and ψdot=[−(k²+2)pdot−(3k²+4)p/t]/[3k²(1+k²)]. Symbolic simplification gives
< H2 >=−[t²pdot²(k^6+k^4+2k²−3)+tp pdot(4k^4+6k²−8)+p²(3k^8+7k^6+15k^4+16k²)]/[3k^4t²(1+k²)²].
For pdot=0, k→0 leading −16p²/(3k²t²); for p=0, k→0 leading +pdot²/k^4. These are conditional mode-family IR sensitivities, not proof that unrestricted physical constrained data are admissible or that full second-order constraint fails. Exact H1[U2] response remains available and its compatibility/evolution unproved.

Pass/fail handoff: independently execute v14.996 scalar_final2.py and print solB/PhiS after ψ,ψdot reconstruction, check original EL_B, EL_Phi, E1, E2. Compare conditional B=0 and α. If mismatch, retract entire candidate quadratic evaluation. External audit required.

Reproducer calculation:
import sympy as s
k,t=s.symbols('k t',positive=True); p,dp=s.symbols('p dp')
P=(-k*k*p+t*dp)/(3*k*k*(1+k*k))
D=s.factor(s.diff(P,t)+s.diff(P,p)*dp+s.diff(P,dp)*(-3*dp/t-(3*k*k+4)*p/t**2))
A=s.factor(-(1+k*k)*P-t*D-p/3)
E=s.factor(-15*k*k*P**2/t**2+3*D**2+12*(A-P)*D/t+9*A**2/t**2-dp**2/(3*k*k)-(p*p+4*P*p+12*P*P)/t**2)
print(A,E)

Other lanes untouched; Suzuki physical-quarter weld parked.
