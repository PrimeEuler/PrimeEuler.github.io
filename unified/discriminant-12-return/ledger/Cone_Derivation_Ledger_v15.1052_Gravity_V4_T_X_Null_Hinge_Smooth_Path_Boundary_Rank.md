# Cone Derivation Ledger v15.1052 — V4 mirrored T/X unit parabolas: finite-regularity null-hinge paths and open-quarter boundary-rank obstruction

**Date:** 2026-11-16 Eastern. **Track:** Gravity/Cone. **Owner:** after v15.1050, actually test whether the opposed V4 unit-parabola branches can pass through null uv=0 with finite-energy regularity, whether an existing physical field action sources that crossing, and whether it is the original open quarter-ladder boundary map. **Status:** [D] exact continuous signed-pair crossing and differentiability/finite squared height-rate test; [D] rigorous rank mismatch between a one-to-one four-point sign reflection and original-unit-step rank-two quarter boundary T; [C] toy two-sector odd Hamiltonian permits transfer with chosen g; [N] no selected K4/Maxwell physical sector-changing source, frequency, or q2 boundary amplitudes.

**Synchronization and collision:** Parents v13.169 V4 sqrt(1,5,7,11) shells, v13.179 Pell null ray, v13.517 signed Cone is prior to sign carrier; v15.602 exact q2 open T†T=2E; v15.628 T preserves L parity; v15.991 corrected closed-Casimir focus; v15.1042 Sandbox X-cone, independently audited v15.1043; v15.1049/1050 Pell/V4 and mirrored unit-parabolas. **Audit Round 587 has now landed as v15.1051** commit 46f31cf7a7a73c1b01d2d27c6a2b859760fb98c9, independently verifying v15.1049/1050. During the overlapping check, a provisional Gravity script with v15.1051 in its filename was added at commit 04df69f8bba24c5b9ea58850fb9a312447707475; this conflicts *in version label* with the independently committed Audit v15.1051, although it does not overwrite any file. This ledger makes **v15.1052** the sole canonical Gravity gate and adds a separate canonical v15.1052 script rather than rewriting either historical object. **Live HEAD immediately prewrite:** 64e38c30d7ded27ae14aca0e1f752672eafe4e95, canonical script; target absent. All writes additive only; no Suzuki/Audit/Sandbox/Muse/certified modifications.

## Gate 848 — an actual continuous bridge exists in the signed-pair plane

For each arithmetic representative r∈{1,5,7,11}, keep u=r and connect the initial positive pair (r,1) to the final negative pair (r,−1) by

**v_p(t)=−(2t−1)^p**, 0≤t≤1, with p positive odd.

Define **T=(u+v)/2**, **X=(u−v)/2**, and **R(t)=sqrt(|uv|)=sqrt(r)|2t−1|^(p/2)**. At t=0 the point is the original T-cone shell (T,X,Y)=((r+1)/2,(r−1)/2,sqrt r). At t=1 the point is the X-cone point ((r−1)/2,(r+1)/2,sqrt r). At t=1/2 the hinge is **(T,X,R)=(r/2,r/2,0)**, lying on T=X. The path is continuous and crosses sign uv from positive to negative. It stays on the signed-pair cone relation **T²−X²=uv** exactly; it is NOT an orbit of the Pell boost, since Pell strictly preserves sign uv.

The crossing parameter t here is an arbitrary dimensionless path coordinate; no proper time, energy, physical action or frequency is selected by the algebra.

## Gate 849 — height-coordinate squared-rate regularity distinguishes crossings

On either side of t=1/2, let x=|2t−1|. Then the squared derivative of R is exactly

**(dR/dt)² = p² r x^(p−2)**.

The full interval integral is

**∫_0^1 (dR/dt)² dt = p²r/(p−1)** for p>1, and infinite at p=1. For checked powers:
- p=1: integrand r/|2t−1|, logarithmic divergence.
- p=3: integral 9r/2, R(t)=sqrt r |2t−1|^(3/2) is C1 at the hinge, but its second derivative diverges.
- p=5: integral 25r/4, R(t)=sqrt r |2t−1|^(5/2) is C2 at the hinge; its first and second derivatives both vanish at the hinge.

In the ambient *linear pair coordinates* (T,X), however, the Euclidean squared-rate integral is finite already for the linear path, namely

**∫_0^1 (Tdot²+Xdot²)dt=2p²/(2p−1)**,

so it equals 2, 18/5, 50/9 at p=1,3,5. This difference demonstrates that the 'infinite kinetic energy' of the linear path is NOT coordinate-invariant physics: it assumes a **chosen quadratic kinetic metric including the cone square-root height R**. R is a derived geometric height and becomes non-smooth at the null hinge. No K4 physical metric/ADM action has selected such a kinetic term; the divergence is a conditional geometric regularity test only.

Even the p=5 path is not an Einstein/Maxwell matter solution merely because it is smooth. Its v(t) profile carries arbitrary acceleration and demands a source if v is to be a dynamical coordinate.

## Gate 850 — a one-to-one V4 sign reflection is not the rank-two open q2 boundary operator

On the four labeled V4 representatives, the signed involution (r,+1)→(r,−1) is a bijection between four state labels. Its linear action in these finite label bases is a unitary/permutation isometry **F†F=I_4**, and therefore has rank four.

By contrast the *original-unit-step q2 cross-shell boundary operator* of v15.602/v15.991, on shell L≥3, connects H_L (dimension L+1) to H_(L+2) (dimension L+3), with only two nonzero boundary links of squared weight **w_L=(L+1)/4**; its rank is **two**, and **T_q†T_q=2E_L** with E_L supported on precisely the two boundary source states. For L=3, T_q†T_q has eigenvalues (1,1,0,0), whereas the four-state sign reflection has eigenvalues (1,1,1,1) in F†F. More generally no scalar rescaling of a rank-four full V4 sign reflection reproduces a rank-two open q2 boundary map. The spaces and operators are different, and they cannot be identified merely because each relates two geometric pictures.

This is a precise, strong *operator obstruction*, not a proof that an enlarged physical theory cannot contain both. A projector selecting the correct two boundary states, an inter-shell physical carrier map, and the dynamically sourced amplitude normalization would all be additionally required.

## Gate 851 — what a sourced crossing would actually require

Let Q distinguish two physical positive/negative sign sectors in an explicitly enlarged quantum carrier. If a physical Hamiltonian commutes with Q, sign-sector populations cannot change. A toy interaction **H_mix=g σ_x** anticommutes with Q=σ_z and evolves population between sectors with a frequency proportional to freely chosen **g/ℏ**. This demonstrates mathematical possibility but does not derive g, a relation to K4, or the original q2 T amplitudes. The real Pell return and any evolution generated solely from its positive reciprocal scaling preserve sign uv. The existing linear Maxwell and homogeneous K4 sources tested v15.695/702 and v15.995–998 do not furnish a unique sign-changing generator on this signed-pair state space. The map (u,v)→(u,−v) is a discrete geometric identification, not a generated finite-time physical evolution absent an action.

A genuine new source-first gate must (i) specify physical canonical signed-pair variables or a Hilbert-space carrier; (ii) derive a smooth, constraint-compatible on-shell crossing from K4/Maxwell or another justified action; (iii) show gauge/charge/parity conservation and any null-interface boundary terms; (iv) project the source onto the two boundary links of T_q and recover their **sqrt[(L+1)/4]** amplitudes for multiple L without postselection; and (v) isolate a dimensionless, source-normalized observable distinguishable from ordinary Maxwell/GR.

## Gate 852 — reproducibility and handoff

**Exact canonical reproducer:** `research-notes/k4_hinge_crossing_boundary_rank_v15_1052.py`, additive commit **64e38c30d7ded27ae14aca0e1f752672eafe4e95**. The path-integral formulas were independently executed locally using SymPy for p=1,3,5; rank-two q2 T†T=2E checked for L=3..13 separately. Canonical script encodes both. The provisional script `research-notes/k4_null_hinge_smooth_crossing_v15_1051.py` commit 04df69f8bba24c5b9ea58850fb9a312447707475 is preserved as history and NOT an additional v15.1051 ledger gate, since that number belongs to Audit Round 587. Independent Audit of this new gate pending.

**Verdict:** Positive explicit geometric crossing and strong smoothness classification; negative full-V4-reflection-to-open-q2-operator identification and absent sourced physical crossing. The X-cone/ T-cone two-branch extension is a useful exact geometric completion; it has not yet become a physical acceleration law or gravitational interaction.

**HANDOFF Audit/Muse/Sandbox:** independently verify the p1 divergence and p3/p5 smoothness, highlight kinetic-metric dependence, confirm the rank-two q2 T versus full-rank V4 sign flip, and audit that Audit Round 587's own v15.1051 remains authoritative despite the separate provisional Gravity script name. Do not infer a real gravitational frequency or a G-free observable from parameterizing a signed-factor path.
