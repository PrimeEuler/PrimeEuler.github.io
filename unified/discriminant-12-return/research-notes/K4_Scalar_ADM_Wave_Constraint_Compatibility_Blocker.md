# v15.057 — Independent scalar-wave substitution conflicts with certified v14.996 oscillator

Date 2026-10-28. Parent v15.038, v15.049, v15.053; source v14.996 scalar_final2.py inspected. Current HEAD checked. This is an AUDIT BLOCKER, not a promoted metric reconstruction.

Assumptions inherited from v15.038:
a=t/√3, H=1/t, p=Δσ (Fourier Δ→−k²).
S:=dotσ−b, with (1−Δ)S=−dot p−Hp+3Hψ−Δψ/(a²H).
alpha=dotψ/H+S/(3H).
From v15.053 scalar wave linearization, ∂t(a³ S)−a(p+alpha+ψ)=0 (for k≠0).
Substituting Fourier S=[−dot p−Hp+(3H+k²/(a²H))ψ]/(1+k²) and alpha into wave yields exactly (verified symbolic differentiation)
wave=−√3*t/[9*(k²+1)] [t² pdd+3t pd−(3k²+2)p].
So proposed gauge-fixed equations force
pdd+3/t pd−(3k²+2)/t² p=0.
However corrected v14.996 scalar_final2.py / reconciliation payload certified
pdd+3/t pd+(3k²+4)/t² p=0
for source strain coefficient pi; p=Δσ agrees with pi up to Fourier phase/sign normalizations (not dynamical sign of potential). Difference in oscillator potential is [6k²+6]/t², inconsistent for all real k.

Conclusion: at least one of the inherited gauge-fixed ADM constraint sign/index normalizations, wave linearization, or mapping from corrected action variable is wrong/incompatible. This is an exact algebraic contradiction, not evidence of a ghost in actual corrected theory. Withhold v15.038, v15.049, v15.053 as JOINTLY CONSISTENT reconstruction inputs, suspend claims that normal-velocity cancellation or ψ decay inferred by combining them establishes physical full-theory estimate, until independent corrected ADM action check. Earlier conditional statements not automatic falsification but applicability not certified.

Independent verification: use machine-built v14.996 scalar_adm2.py, inspect metric +--- vs source code gtt=-1/N² while matter L has sign convention (potential sign conventions!), and derive all canonical constraints and scalar wave with one single consistent ADM convention and 2-jet identity. A direct reproduction of v14.996 psi_sol and unreduced Euler residuals would locate discrepancy. This note establishes only the contradiction and priority re-audit.

Suzuki quantum quarter physical weld parked; protected lanes untouched.
