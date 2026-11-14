# Cone Derivation Ledger v15.941 — Global descent of the 8π Spin(4) quarter-phase carrier

**Date:** 2026-11-13 US Eastern. **Lane:** Gravity. **Parents:** v15.632–633 Chern class/fourth-root and four-component clutching; v15.639 exchange-versus-Casimir grading; v15.642 headless polarity quotient; v15.701 Hopf spinor/charge-one carrier; v15.940 auxiliary 8π Fourier phase; External Audit Round 575 v15.939 verified v15.930–938. **Immediately prewrite live HEAD:** a89484f6345de44e0d6d4c4f6741b63ad1d32c21. Target filename confirmed absent. Additive only; frozen Suzuki work and all past ledgers unchanged.

**Question:** Does the 8π Fourier quarter-phase from v15.940 descend globally to the degree-one monopole/Hopf bundle underlying the physical bicone/Taub–NUT winding? Or does a four-component carrier evade the topological obstruction and produce a sourced physical connection?

**Status:** [D, prior result sharpened] obstruction for ordinary scalar fourth root and explicit global rank-four clutching; [D] Spin4 has no nontrivial continuous one-dimensional characters; [N] clutching is not group representation or physical holonomy; [O] source-derived connection/coupling and observational discriminator.

## Gate 706 — scalar quarter-phase cannot descend from the Hopf total space

On S² with equatorial north/south overlap, a unit-Chern monopole line bundle has transition `g_NS(φ)=exp(iφ)`. A fourth-root **ordinary line bundle** R would obey `4 c1(R)=c1(L)=1`, impossible in `H²(S²,Z)=Z`. Equivalently, the local function `r_NS(φ)=exp(iφ/4)` becomes `i r_NS(φ)` upon φ→φ+2π and fails to be single-valued. More generally L_k has an ordinary fourth root iff **4 divides k**. This is exactly the v15.633 theorem, not a new gravity field derivation.

Pullback of L_1 to the Hopf total space S³ can be trivial because `H²(S³,Z)=0`, but triviality upstairs does **not** create an equivariant weight-1/4 one-dimensional character of the original principal U1 circle nor descend an ordinary fourth-root line bundle to S². The pulled-back structure forgets the nontrivial descent datum; adding a fourfold phase cover modifies that datum. This explicitly distinguishes a valid auxiliary 8π coordinate from a global physical charge.

## Gate 707 — four-component bundle is global, not a character

The pre-existing v15.633 U4 clutching map `M(z)=[[0,0,0,z],[1,0,0,0],[0,1,0,0],[0,0,1,0]]` with `z=e^(ikφ)` satisfies `M^4=zI4`, `det M=−z`, `charpoly λ^4−z`; it is single-valued and unitary at |z|=1. Its determinant has first Chern winding k, so it describes a rank-four vector bundle rather than four copies of a fourth-root line bundle. The eigenbranches permute in gcd(k,4) cycles of length 4/gcd(k,4), as already certified.

With χ=diag(1,−1,1,−1), **{M,χ}=0**, so a fixed numeric grade cannot be used identically in both local frames; globally defined endomorphism data must be transformed by conjugation when switching patches. This is compatible with mathematical vector-bundle patching but gives no preferred EM/G physical interpretation.

Importantly, the map `φ→M(e^(iφ))` is *not* itself a group homomorphism U1→U4: at φ=0 it is a nonidentity permutation `M(1)≠I4`, whereas a homomorphism must send the identity to I4. Hence the clutching map must not be claimed to define a physical internal U1 action or a gauge Wilson loop. A separately derived connection and field equation would be necessary.

## Gate 708 — Spin(4) alone does not produce the quarter-phase charge

Spin(4)=SU2_L×SU2_R is simply connected and semisimple. For any continuous character ρ:Spin4→U1, its Lie algebra differential maps the perfect Lie algebra `su2⊕su2=[su2⊕su2,su2⊕su2]` into abelian `u1`, and therefore vanishes. Connectedness then makes ρ identically trivial. In particular there is no nontrivial continuous **scalar** quarter-phase character naturally derived from the two Spin4 factors themselves. This statement does not ban higher-dimensional Spin4 representations or separately added U1 fiber/bundle charges; indeed the v15.633 companion is a four-component clutching construction, not a 1D character. The 8π auxiliary Fourier circle is a consistent distinct factor but is not a new connected double cover of SU2.

## Gate 709 — verification, novelty, next physical gate

**Reproducer:** `research-notes/k4_spin4_quarter_global_bundle_descent_v15_941.py`, additive commit **a89484f6345de44e0d6d4c4f6741b63ad1d32c21**. Local SymPy PASS: fourth-root divisibility for k=1..32, explicit cyclic M identities, nontrivial M(1), grade anticommutator, analytic branch-length arithmetic, and Lie-algebra 1D-character obstruction. **Independent Audit pending.**

**Result:** The 8π formal carrier is well-defined and reproduces the quarter Casimir, but a degree-one monopole bundle admits no ordinary scalar fourth root. The rank-four global solution already in v15.633 remains viable *as mathematical bundle data*, not a source-selected gravitational field. Neither scalar phase alone nor Spin4 alone yields an intrinsically chosen physical gravity quarter-charge, relative coupling strength, tidal matrix element, or new G-independent observable.

**NEXT:** Only advance the branch if a physical action selects a connection on this rank-four bundle (or a specified associated spinor carrier) and determines source normalization/coupling. Test gauge-invariant curvature/Wilson observables against ordinary monopole U(4) gauge freedom; show explicitly where the new dimensionless prediction survives changes of connection and all arbitrary source coefficients. Otherwise preserve this no-go and redirect to rank-one/rank-two physical gravimetry.

**HANDOFF Audit/Muse:** Check the subtle distinction between topological pullback triviality on S³ and equivariant descent to S², the strict ordinary-line-bundle fourth-root condition 4|k, the non-homomorphism of the clutching matrix, and the absence of nontrivial continuous 1D Spin4 characters.
