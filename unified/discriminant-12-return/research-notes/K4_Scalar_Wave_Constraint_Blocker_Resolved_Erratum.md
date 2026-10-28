# v15.058 — Erratum to v15.057: exact scalar-wave compatibility recovers corrected oscillator

Date 2026-10-28. Checked latest live HEAD. Parent v15.057 blocker, v15.038 constraint, v15.053 wave, corrected v14.996 scalar oscillator. Additive erratum; do not edit historical ledger; separate protected lanes untouched.

Set a=t/√3, H=1/t, p=Δσ, Fourier Δ→−k², k≠0, σ=−p/k². v15.038 constraints:
 α= t ψdot+(t/3)S where S=dotσ−b=−pdot/k²−b;
 Hamiltonian 4k²/a² ψ+12Hψdot+4H k² b−12H² α−4H²p+12H²ψ=0.
Algebraically solve for b:
 b=[−t pdot+k²p−3k²(1+k²)ψ]/[k² t(1+k²)].
Then S=−pdot/k²−b=[−t pdot−p+3(1+k²)ψ]/[t(1+k²)].
v15.053 scalar wave equation ∂t(a³ S)−a(p+α+ψ)=0 is equivalent to W:=d/dt(t³ S)−3t(p+α+ψ)=0. Substituting expressions for b,S,α and differentiating exactly gives
 W=−t/(1+k²)[t² pddot+3t pdot+(3k²+4)p].
Thus W=0 is PRECISELY v14.996 corrected physical strain oscillator, not the inconsistent equation asserted in v15.057. Verify by direct symbolic algebra (independent SymPy evaluate, no action rerun); all ψ and ψdot cancel identically. Former claim v15.057 pddot+3/t pdot−(3k²+2)/t² p=0 was an algebraic substitution/simplification error. Do not infer the momentum sign is wrong. V15.057 blocker RESOLVED for consistency of the v15.038/v15.053 *linear scalar constraints+wave*. This does not prove all off-shell ADM action equalities or extract ψ reconstruction, which remains open, as elimination naturally cancels ψ in the matter wave residual after using constraints.

Diagnostic: for k>0, multiply W by −(1+k²)/t and check it equals oscillator bracket. On k=0 the longitudinal σ potential and gradient division invalid; treat separately. Original v14.996 independently verified linear stability preserved.

Next obtain ψ coefficient-level reconstruction from corrected source Euler equation E1, rather than assume wave+constraints determines ψ. Independent external audit requested for erratum and low-k conditions.
