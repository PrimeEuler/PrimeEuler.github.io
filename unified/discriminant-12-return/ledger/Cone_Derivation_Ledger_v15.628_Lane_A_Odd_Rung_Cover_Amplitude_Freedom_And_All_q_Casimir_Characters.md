# Cone Derivation Ledger v15.628 — Lane A: odd-rung two-sector completion, amplitude freedom, and the correct all-q Casimir characters

**Date:** 2026-11-10. **Parents:** v15.135 §5 odd-quarter/EM Casimir classes, v15.602 every-q shell and cross-shell witness, v15.624–625 sector clarification, v15.626 Casimir parity involution, v15.627 existing cross-shell parity preservation. **Status:** [D] exact spectral/representation obstructions and all-q character identities; [C] deliberately chosen two-sector completion; [O] physically selected interaction, amplitude, energy gap, coupling or gravity observable. **Fresh prewrite HEAD:** 94494d23e6a97e99534979c84dce9b0120eec855; v15.628 name and nearby-topic collision searches empty. Additive-only; frozen Suzuki and far-tail work untouched.

## Gate 119 — no odd-quarter shell jump within native two-mode Fock number spectrum

For the original Paper C two-boson Schwinger carrier, N=n1+n2 has spectrum nonnegative integers, j_phys=N/2, and its native operators respect that occupation quantization. If the proposed q=2 geometric quarter-shell step Δj=1/4 were to act in the *same* carrier as a standard Schwinger spin jump, it would require ΔN=1/2 and an operator W with [N,W]=(1/2)W. Since no half-integer eigenvalues occur in spec N, W=0 on the finite-number core. Thus no nonzero such operator acts in the ordinary Fock space with this exact interpretation. This is a scoped spectral argument; an enlarged carrier, changed number definition or non-Schwinger identification is not excluded.

## Gate 120 — constructive two-copy odd-rung with freely factorizable amplitudes

Construct an auxiliary carrier with basis |n,σ> (n>=0, σ=0,1), Q|n,σ>=(n+σ/2)|n,σ>, χ|n,σ>=(-1)^σ|n,σ>. For arbitrary nonzero amplitudes a_n,b_n, define W|n,0>=a_n|n,1>, W|n,1>=b_n|n+1,0>. Then [Q,W]=W/2 and {χ,W}=0 exactly. Asking that its square agree with the *illustrative inter-shell EM number-raising operator* A†|n,0>=sqrt(n+1)|n+1,0> yields **a_n b_n=sqrt(n+1)**. This leaves one arbitrary factor per n, e.g. a_n=t_n>0,b_n=sqrt(n+1)/t_n. This A† is NOT the within-shell Schwinger J+ or the chosen v15.602 T: no native EM→gravity interaction has been derived.

A finite cyclic alternative makes the freedom especially transparent. On an even 2m-site toy ring let S|L>=|L+1 mod 2m>, χ=(-1)^L. For any t>0 let W|L>=t|L+1> when L even and W|L>=t^(-1)|L+1> when L odd. **W²=S², {χ,W}=0**, and the interaction H=W+W† is Hermitian for every t. Unitarity of W itself would force |t|=1, but ladder/transition operators are not generally unitary, and Hermiticity of H does not fix t or its total coupling. This is an existence witness, not a physical choice of gravity.

## Gate 121 — elementary compensator permits charge conservation without fixing the interaction

Let an auxiliary two-state system have Q_aux=diag(0,1/2), lowering τ_-, and define **H_int=g W⊗τ_-+g* W†⊗τ_+**. Then [Q+Q_aux,H_int]=0 and H_int is Hermitian for any g. The subsystem Casimir grading χ is exchanged by H_int; its combined charge/holonomy is conserved. The two-state compensator and its assignment are externally postulated; it has no derived relation to a photon, graviton, Newton G or a specific field. Fractional Q can be re-normalized to a faithful doubled U(1) cover; no physical quantization claim follows.

## Gate 122 — correction: q-fold Casimir character is the real all-mesh EM-subgrid projector

Already known C_{q,L}=L(L+2q)/(4q²)=j(j+1), j=L/(2q), L>=0. Therefore sqrt(1+4C_{q,L})−1=L/q (positive branch). Define

**Z_q=exp[2πi(sqrt(1+4C_shell)−1)]**, with eigenvalue exp(2πi L/q).

This is an exact Z_q spectral character. Its group-average **P_EM(q)=(1/q) Σ_{k=0}^{q−1} Z_q^k** projects precisely onto L≡0 mod q, the original q=1/EM half-shell submesh. At q=2 only, Z_2=(-1)^L=exp(16πi C_shell), exactly the v15.626 quarter-mesh χ. The identity from v15.626 χ_q=exp(4πi q² C_shell)=(-1)^L remains true for all q, but **for q>2 it is NOT generally the EM-submesh selector**: e.g. at q=3, L=2 is even but not an EM shell, and L=3 is an EM shell but odd. This is a refinement of the interpretation, not an invalidation of the earlier parity theorem.

## Gate 123 — actual v15.602 cross-shell witness is Z_q-charged for q>2

The v15.602 witness T_{q,L} moves from L to L'=L+2(q−1). Therefore **χ_q T=Tχ_q** for all q, exactly as v15.627 proved, but the true refined character transforms as

**Z_q T=exp[−4πi/q] T Z_q.**

The factor equals 1 exactly for q=1,2; for q>2 the witness typically changes the mod-q residue sector. Thus v15.627's "parity preserved for every q" is sound but "EM/gravity" as a two-sector interpretation is specific to q=2, not a generic q>2 EM-submesh conservation theorem. At q=2 the existing T remains parity-preserving and is NOT the missing EM↔G odd-rung operator.

## Exact checks and physical status

Conversation archive `cone_odd_rung_gates_119_123.zip` contains `cone_odd_rung_119_121/reproduce.py` and `REPORT.md`. Script passed: exact residue tables (32 shells), 8-state cyclic squared-root/anticommutator identities, 12-state symbolic two-copy operator with arbitrary weights, exact Hermitian combined-charge exchange, q=1..11 witness parity, q=2..10 all-q Casimir character/projector numeric and exact root identities. No measurements or fitted physical constants. The operator classes are explicitly not promoted to a prediction of G.

**Next gate:** compare representation-theoretically allowed odd-sector matter couplings with actual Larmor/rotor and gravitational candidate symmetries; identify which *independently physically specified* mechanism fixes W and its normalization instead of postulating it. Keep the Suzuki-quarter physical weld parked.

**HANDOFF:** external-audit, gravity, sandbox; independently verify the Fock spectral proof, indefinite square-root amplitudes and charge compensator, all-q character/projection correction and Z_q charge of the genuine v15.602 witness. Preserve prior certified materials and frozen Suzuki files.
