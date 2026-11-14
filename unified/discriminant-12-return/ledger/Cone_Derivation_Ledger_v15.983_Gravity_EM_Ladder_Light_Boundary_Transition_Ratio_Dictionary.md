# Cone Derivation Ledger v15.983 — EM Schwinger transition weights and the n+1 null/light-speed boundary

**Date:** 2026-11-14 US Eastern. **Lane:** Gravity/EM Cone. **User:** "what is the relation between the em spectrum on the transition ratios and the N+1 speed of light boundary?" **Status:** [D] exact transition amplitude–null-circle–factor/Cayley identities; [C] identification of algebraic X/T with physical v/c, and of the boundary with a physical c light cone; [N] no unique physical EM photon frequency spectrum, inertia, force or gravity speed selector derived from the fixed-D ladder.

**Prior research/redundancy:** Paper C Schwinger two-oscillator shell, v15.906 diameter–secant and fixed-circle ladder; canonical v15.968 (reissued from v15.955 after Audit Round 578) exact f_D(k) J± edge and half-state-midpoint Jx²+Jy²; v15.885 SR velocity axis and time selector obstruction; v15.888 hypothetical c/4,c/2 proper-time nodes; v15.981 D4 special 9/5 CG/rapidity match and failure at D≥6; v15.982 native X/T versus chosen half-edge/D beta normalization. Latest Audit seen v15.980 Round 580, commit 93ce5785e8b20317a062eeefdd26e3552a3093dc, audited v15.978–979; v15.981–982 still pending. **Immediately prewrite live HEAD:** 642c14525d4ecc1a9319d84bd705c1218047129e (new exact reproducer), target confirmed absent; additive-only and preserve Suzuki/Audit/Sandbox certified objects.

## Gate 786 — n+1 is the EM Hilbert dimension and outer null diameter, not an automatically physical frequency

Define total two-boson occupation **N=n1+n2**, ordinary Schwinger spin **j=N/2**, Hilbert dimension **D=N+1=2j+1**, and geometric outer circle radius **T=D/2=j+1/2**. The magnetic *state center* positions m=−j,...,+j all lie inside this outer circle: **|m|/T≤(D−1)/D<1**. The boundary |X|=T is a **half-step beyond the two extreme magnetic states**; it corresponds to the zero-amplitude *formal transition endpoints* k=0,D, not to an allowed extra state. This n+1 boundary is a finite-dimensional representation/midpoint fact before attaching SI units.

There are D−1 nonzero J± edges. Let k=1,...,D−1. Their amplitude squares and null-circle edge positions are

**f_D(k)=|<k−1|J+|k>|²=k(D−k)**,
**X_k=D/2−k**, **Y_k²=f_D(k)**,
**T²−X_k²−Y_k²=0**.

The quantum J+ is the ordinary spin-j Schwinger ladder. This is an exact already-known EM *transition amplitude* structure, not photon energy or an emitted spectral frequency by itself. A Hamiltonian is needed to obtain photon transition energies ΔE=ℏω.

## Gate 787 — conditional speed-of-light boundary produces an exact inverse-Lorentz-factor transition envelope

**If and only if** the homogeneous Cone X/T variable is physically interpreted as the velocity ratio **β_k=v_k/c=X_k/T=(D−2k)/D**, the boundary |X|=T maps to |v|=c and the circle identity becomes

**f_D(k)=T²(1−β_k²)=(D²/4)(1−v_k²/c²)**,

**sqrt(f_D(k))=(D/2)/γ_k**, where **γ_k=(1−β_k²)^(−1/2)**.

Consequently for any two internal edges k,l,
**f_D(k)/f_D(l)=(1−β_k²)/(1−β_l²)=(γ_l/γ_k)²**.
Neighboring intensity ratios are **f_D(k)/f_D(k+1)=k(D−k)/[(k+1)(D−k−1)]** for k=1..D−2. The maximum is at zero β (for even D an integer edge); amplitudes vanish at formal boundary k=0,D, corresponding to |β|=1. These are fixed-Cone exact identities. The γ symbol is a mathematical reparameterization until a genuine physical spacetime velocity/energy field map is proven. The coefficient of a physical optical/EM transition matrix element is not generically just dimensionless J+: additional dipole operator and field strengths are needed.

For D=5, the 4 nonzero edges have (k,β,f)=(1,3/5,4),(2,1/5,6),(3,−1/5,6),(4,−3/5,4). Their successive squared-amplitude ratio 4/6=2/3 is a standard Schwinger ladder fact. It may look relativistic under the chosen mapping, but it is **not relativistic time dilation derived from Maxwell/GR**.

## Gate 788 — factor pairs directly give the Cayley/rapidity chart, but inverse secant is a different number

At edge k, let factor pair **(a,b)=(D−k,k)**. Then D=a+b, X=(a−b)/2, Y²=ab. The normalized ratio under the conditional velocity interpretation is

**β=(a−b)/(a+b)**,
**(1+β)/(1−β)=a/b**, and so **η=atanh β=(1/2)ln(a/b)**.

These are exact hyperbolic/AM–GM/factor identities; in projective geometry they hold without physically identifying a boost. The old diameter-to-secant ratio **D/(D−2k)=(a+b)/(a−b)=1/β**, *not* the Cayley ratio a/b. The former has a pole at β=0 even though the transition weight ab is maximal there; the latter has its own endpoint divergences.

A suggestive conditional special-relativistic mass-shell dictionary is **E=ε T**, **pc=ε X**, **mc²=ε Y** for fixed positive energy calibration ε, which algebraically yields E²=(pc)²+(mc²)² and β=pc/E. However with **fixed D and fixed ε**, E is fixed while Y=√[k(D−k)] varies across the edges, so the inferred **rest mass m varies**. The finite-D edge ladder would relate states with different relativistic mass contributions, not one massive particle changing speed at fixed rest mass. Conversely keeping m constant requires ε to vary with k, and then E=ε T is not a constant physical shell energy. Neither option is chosen by Cone geometry; do not conflate a null-cone *identity* with a physical Minkowski worldline.

## Gate 789 — D=4 centers versus edges resolve the c/4 and c/2 comparison

At D=4 the four **magnetic state centers** m=3/2,1/2,−1/2,−3/2 map by β_center=m/T to **(3/4,1/4,−1/4,−3/4)**. The three **nonzero transition edges** k=1,2,3 map by β_edge=X_k/T to **(1/2,0,−1/2)** with squared strengths **(3,4,3)**. Thus c/4 and c/2 are naturally present at the same D shell but label **different objects**: c/4 is a state center, c/2 is a transition midpoint/edge. Taking their ratio in a single SR rapidity difference requires a physical rule for comparing that state with that edge; no unitary/SO(1,1)↔SU(2) map currently supplies one. The special 9/5 of v15.981 therefore remains an exact selected-coordinate coincidence, not forced gravitational dynamics.

The older v15.968 midpoint identity is again **f_D(k+1/2)=[f_D(k)+f_D(k+1)]/2+1/4**, yielding state-centered **<Jx²+Jy²>=f_D(k+1/2)−1/4**. The midpoint quarter correction is EM state geometry, not an independently established physical q2 gravity Casimir.

## Gate 790 — practical experimental discriminator, and negative selector

**Exact result:** the Schwinger transition ladder is related to its n+1 outer null boundary through **f_D/T²=1−(X/T)²**. Expressing X/T as physical β produces a perfect inverse-γ envelope and factor Cayley rapidity; these identities are exact and structurally strong.

**Limitations:** n+1 is the **outer transition diameter/state count**, not automatically a light-travel frequency. A null boundary tagged ±c can justify units *if a physical spacetime map is supplied*, but does not prove X is particle speed across Fock ladder states or that Y is fixed rest mass. No dynamical relationship between Maxwell field strengths, physical EM dipole matrix elements and gravitational response is derived. The function 1−β² is a rewriting of f_D, not a novel field dispersion law. A real test requires a sourced time Hamiltonian and source/detector comparison with a unique allowed carrier map, beyond ordinary SU2/relativistic kinematics.

**Reproducer:** `research-notes/k4_transition_light_boundary_v15_983.py`, commit **642c14525d4ecc1a9319d84bd705c1218047129e**; local exact SymPy execution PASS covering symbolic f_D, normalized β, γ envelope, factor Cayley identity, reciprocal secant, adjacent-edge ratios and half-row relation, D=4 center/edge lists, and D=3..29 exact controls. Independent Audit pending.

**NEXT — Audit/Muse:** check physical velocity coordinate conventions in spacetime dimensions, factor a/b vs inverse secant 1/β, D=4 mixed center/edge 1/4 and 1/2, fixed rest mass/energy obstruction, and that no photon transition *frequency* follows from J± coefficients. Seek any real Maxwell/K4 on-shell action implying the required β→state mapping, not merely a boundary SI tag. The separate quarter-sector gravitational Casimir remains explicitly unsourced.
