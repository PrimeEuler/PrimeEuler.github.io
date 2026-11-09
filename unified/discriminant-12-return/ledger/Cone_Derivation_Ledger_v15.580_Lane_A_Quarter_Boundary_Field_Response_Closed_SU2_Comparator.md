# Cone Derivation Ledger v15.580 — Lane A: boundary contribution to magnetic-source response, matched closed-SU(2) comparator

Date 2026-11-09. Parents v13.595, v15.140, v15.572–579. Status [D] exact finite-matrix identities and comparator no-go; [C] explicitly postulated oscillator field coupling; [O] physical field dictionary, unique emission source and boundary-specific signature. Prewrite HEAD 73ef2b283e5323ed4cc749a26bdfe136aa0db625, version/path collision search clean. Additive only; no Suzuki production or far-tail changes.

## 1. General current acceleration identity [D]

On any refined j=N/4 shell, retain *original* AM–GM raising operator J_+ (unit step in m, index jump 2) and its adjoint J_-, and magnetic coordinate M=Jz. Define Jx=(J_++J_-)/2, Jy=(J_+-J_-)/(2i), commutator defect D=[J_+,J_-]-2M. The original generator obeys [M,J_±]=±J_± exactly, even on open chains. Put H0=-g Jx, real g, and mathematically define transition-current source S=i[H0,M]=-g Jy (hbar=1). Then

**dot S = i[H0,S] = -g²(M+D/2).**

Thus the open-shell boundary defect enters the source *acceleration* as the explicit term -g²D/2. For a closed unitary SU(2) multiplet D=0. The equality was verified symbolically on j=1/4,3/4,5/4,7/4,9/4,11/4. This is a model identity, not Maxwell's equations or a derivation that S is a physical current.

If an oscillator is *postulated* with Htot=H0+Omega b†b+lambda S Q, Q=(b+b†)/sqrt2, for a matter initial state with <S>0=0 and an oscillator vacuum, then

<Q(t)>=-Omega lambda <dot S>0 t³/6+O(t⁴),

with dot S evaluated under H0 at t=0. This follows from Qddot=-Omega² Q-Omega lambda S; the source-coupling term commutes with S and therefore does not modify the initial source derivative. All full-H dynamics are unitary.

## 2. First open j=3/4: an exact no-go for unique field response [D]

Each of the two open 2-state chains has magnetic levels one unit apart and identical original Jx edge amplitude sqrt(3/2)/2. Write the restricted M=mu I+sigma_z/2 in ascending energy order with mu=-1/4 for indices (0,2) and +1/4 for (1,3), while Jx=sqrt(3/2) sigma_x/2. Hence under the change g_closed=g sqrt(3/2), each chain's H0 and transition-current S are *exactly equivalent* to a conventional closed spin-1/2 driver. The offset mu contributes only a scalar to any omega*M Zeeman term and cancels in the current commutator. The equivalence persists when coupled to the same oscillator through lambda S Q. Thus no field response of a **single** j=3/4 open chain can diagnose its open boundary against a coupling-normalized spin-1/2 comparator under the tested Hamiltonian. This is a discriminating negative result, not a failure of algebraic boundary identity.

## 3. Next j=5/4: an unequal-edge, mirror-odd response [D/C]

Each open three-state chain has squared original J_+ edge weights (5/2,3) or (3,5/2), mirror-reversed. A closed spin-1 SU(2) chain has (2,2). Thus no scalar choice of g_closed can match both edge amplitudes while preserving the M-eigenstate ordering.

At the **middle state** of one open chain m=-1/4, D=0, and the exact source derivative is <dot S>=+g²/4; at its reflected partner m=+1/4, <dot S>=-g²/4. The middle m=0 state of an ordinary closed spin-1 ladder has <dot S>=0 for all scalar g_closed. For the *postulated* current-oscillator Hamiltonian, the corresponding leading field means are -Omega lambda g² t³/24, +Omega lambda g² t³/24 and 0, respectively.

This differential feature depends on unequal AM–GM edge strengths and the open-fragment magnetic-coordinate offset; it can also be engineered in generic anisotropic three-level hopping systems. It is not evidence that real odd-quarter spins exist, that an emitted field is measurable, or that the open-boundary D term alone produces a unique new phenomenon. The operator D has boundary support; the middle state's nonzero acceleration appears because the finite open path weights are asymmetric.

## 4. Symmetry, energy bookkeeping, guardrails [D/O]

On odd-quarter shells, mirror R obeys RMR=-M, RJxR=Jx and RDR=-D. So the proposed S is mirror-odd, mirror states generate opposite source profiles, and mirror-even superpositions have zero mean field under the combined oscillator parity (not necessarily zero bosonic occupation). The original finite Hamiltonian remains Hermitian; missing-edge AM–GM weights are algebraic defects, not actual probability leakage. In particular the absence of an external drive omega does not mean creation from zero energy: g and lambda are supplied interactions and the initial state can carry energy. Physical magnetic spectra depend on spin representation, field polarization, populations and gauge coupling, none of which is derived on an odd-quarter carrier.

**Next gate:** compare source-defined coupling to the original cone acceleration/deceleration parabolas and the exterior 'missing targets', ideally by constructing a canonical external target/map (or an obstruction) rather than simply naming lambda or a field mode.

**HANDOFF:** external-audit; type boundary-vs-closed magnetic response certificate; status open; verify exact commutator-current acceleration, j=3/4 spin-1/2 dynamical equivalence (including oscillator), j=5/4 unequal-edge ratio and middle-state field coefficient, and absence of unsupported physical promotion. Local reproducibility artifact: cone_boundary_field_comparison_gates_50_51.zip. No production changes.
