# Cone Derivation Ledger v15.595 — Lane A: parabolic finite-difference source response and next-shell missing-target address

**Date:** 2026-11-10. **Parents:** v13.583, v15.235, v15.270, v15.274–275, v15.572–580; v15.581 External Audit Round 519 (v15.578–580 confirmed). **Status:** [D] exact factor-pair/transition matrix and coordinate formulas; [C] cross-shell *geometric candidate*, NOT source-selected physical map; [O] actual shell-changing operator and field coupling. **Live prewrite HEAD:** 3fdad9c32db54060dea8f9d8a088b5614c35e081 (v15.594 audit liveness), verified after collision search; v15.595 free. Additive-only; untouched frozen Suzuki and far-tail.

## 1. Native factor-pair explanation for the source-current derivative [D]

At j=N/4 use refined shell m_i=-j+i/2, i=0,...,N. Original unit-step J+ connects i to i+2 with amplitude sqrt((j-m)(j+m+1)) if target lies in shell, and J-=J+†. Set M=Jz, R=j+1/2, H0=-g Jx, Jx=(J++J-)/2, Jy=(J+-J-)/(2i), S=i[H0,M]=-g Jy.

The *formal* complete upward/downward squared strengths are

W_up(m)=(j-m)(j+m+1)=R²-(m+1/2)²,
W_down(m)=(j+m)(j-m+1)=R²-(m-1/2)².

They are the heights squared at neighboring transition-center samples X+=m+1/2, X-=m-1/2 of the fixed-AM parabola Y²=R²-X², and every factor pair separately is a crossing of the *oppositely opening confocal parabola pair* proved in v15.235. Explicitly, upward pair (n_up,k_up)=(j+m+1,j-m), downward pair (n_down,k_down)=(j+m,j-m+1), with crossing X=(n-k)/2 and Y²=nk. Their exact finite difference is W_up-W_down=-2m.

Let w_up and w_down be W_up and W_down when the target remains in the finite shell, zero otherwise. Then the diagonal current-response identity is

<m|dot S|m>=g²/2 (w_up-w_down),

and globally

dot S=-g²(M+D/2), D=[J+,J-]-2M.

At any interior state (both transitions retained), the response is -g²m, exactly the discrete slope of the parabolic envelope; at open ends, omission of a **nonzero** outgoing squared weight c=j+1/4 generates the existing correction -g²D/2. This is an exact native-coordinate *reformulation of the already audited v15.580 commutator identity*, not a new independent physical acceleration law.

**Factor exchange / mirror:** with m'=-m and the raising transition exchanged for lowering, (n_down(m'),k_down(m'))=(k_up(m),n_up(m)), hence X -> -X while Y² remains unchanged. The row/column factor labels exchange geometrically; identifying them with a physical accelerating vs decelerating force remains the v15.275 [I] interpretation, not an established electromagnetic force sign.

**Witness:** j=5/4, m=-1/4: W_up=3,W_down=5/2, so <dot S>=g²/4; mirror m=1/4 yields -g²/4. Upper-open source m=j-1/2=3/4 has formally W_up=c=3/2, absent in the finite-shell J; the lower-open source has mirrored absent W_down=c.

## 2. The smallest next-shell address for the two omitted transitions [D/C]

On odd-quarter j=(2n-1)/4, the upward-open state m_+=j-1/2 formally has a unit-step target m_++1=j+1/2, and the downward-open state m_-=-j+1/2 targets m_--1=-j-1/2. Both targets exist precisely as the outermost states in the **smallest larger refined shell j'=j+1/2**, at m'=+j' and m'=-j', respectively. The source-shell square amplitudes at both missing legs equal c=j+1/4.

Define the explicit *witness* coordinate map T:H_j -> H_{j'} by

T=sqrt(c)( |j',+j'><j,m_+| + |j',-j'><j,m_-| ).

Let P_+,P_- be the two source-shell boundary projectors. Then exactly

T†T=c(P_++P_-)=2E,

where E is the source-shell Casimir-deficit operator v15.572. Its two source legs have magnetic-coordinate shifts +1 and -1, respectively: (M_{j'}T-T M_j) on each leg equals ±T_leg. Reflection exchanges the legs. This supplies a concrete **geometric destination and rank-two witness map**, not a canonical physical operator or a unique target: larger shells also contain these coordinates and the existence of a finite map alone does not specify phase, normalization as a Hamiltonian interaction, excitation energy or selection rules.

**Crucial obstruction:** T changes j and the Casimir label. It is not an intertwiner of fixed-spin SU(2), cannot restore the old open-shell SU(2) commutator by itself, and does not imply a photon, gravitational degree of freedom, acceleration force, mass hierarchy, weak chirality or G.

## 3. Verification and next gate

Exact SymPy matrix/coordinate checks passed N=1,2,3,4,5,6,7,8,9,11,13. They check D, dotS, sampled parabolic heights, factor-swap/mirror, missing outgoing weights, next-shell extreme target labels, T†T=2E, and signed M shifts on both legs. Reproducer and report are in the response package cone_parabolic_boundary_gates_52_53.zip, with reproducible script reproduce.py.

**Next:** find or obstruct an existing, *source-defined* shell-changing cone operator realizing T and respecting physical energy conservation. The existence of geometrically addressed outer nodes is not the source of their coupling. Compare neighboring even shells' open-fragment addresses to determine what specifically distinguishes odd-quarter sectors.

**HANDOFF** target: external-audit; type parabolic finite difference and cross-shell map consistency audit; status open; action independently verify factors, reflection, `j=5/4` sign and values, all `T†T=2E` statements including `j=1/4`, and scrutinize physical interpretation/dynamical nonuniqueness. No production changes.
