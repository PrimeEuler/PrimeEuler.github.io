# Cone Derivation Ledger v15.610 — Lane A: fixed original step versus co-scaled step on the quarter mesh

**Date:** 2026-11-10. **Parents:** v13.197 circle-area staircase pushforward, v14.767 half/quarter unit covariance, v15.602 all-refinement defect, v15.604 refinement naturality, v15.608 full 2D boundary localization, v15.609 co-scaled unit and origin tests. **Status:** [D] exact continuum pushforward and positive-complement theorem; [O] any physical EM/G coupling or q=2 selector. **Prewrite HEAD:** 2d3093e4304c418316345aa92a708ee03c033e3c; v15.610 collision search empty. Additive only, Suzuki frozen/production untouched.

## Gate 81: independent physical mesh unit u and transition step s

For positive factor coordinates x,y and fixed original unit step s, the formal missing upward/downward AM–GM squared weights are y(x+s) and x(y+s). The continuum omitted-edge Casimir-deficit density is

E_s(x,y)=[y(x+s) 1_{y<s}+x(y+s)1_{x<s}]/2.

It arises as the continuum interpolation of the original-step open-ladder defect; **not** an independently derived physical Hamiltonian. Under physical coordinates (x,y)=u(X,Y) and corresponding u-scaled v13.197 triangular/divisor staircases, the flat circle-area Jacobian J=(x+y)/(4sqrt(xy)) is homogeneous degree zero. With ratio r=s/u,

E_s(uX,uY)=u² E_r(X,Y), 
B_{*,u,s}(n)=u⁴ F_{*,r}(n),
F_{*,r}(n)=∬_{unscaled staircase *} E_r J dXdY.

Thus the previous u⁴ covariance at fixed normalized n *only* gives identical dimensionless integral when r is held fixed. The co-scaled case u=s=1/2 has r=1 and yields F_T=F_D=√n(3n²+8n+9)/45, F_A=0 (v15.608–609).

## Gate 82: the original unit-step operator creates complementary-region boundary support

On the quarter/half-unit mesh u=1/2, KEEP the original EM-sized transition s=1, so r=2. The omitted-weight strips X<2 or Y<2 now invade the complement A_n=T_n\D_n: for all integers n≥3 the k=2 staircase column has a positive-area difference lying in 1<X<2 and the integrand E_2 is strictly positive there. Therefore

**F_{A,2}(n)>0 for all n≥3, while F_{A,1}(n)=0 for every n.**

This is a strict algebraic support difference, not an overall rescaling. For n=1,2 the complement has zero area and its *average* is undefined, not zero.

Exact SymPy rectangular integrations for n=11 yield
F_{T,2}=(-448√10+524√11+1984√5)/45 ≈105.72377479445,
F_{D,2}=(-158√5+382√10+524√11)/45 ≈57.61339368635,
F_{A,2}=238√5/5−166√10/9 ≈48.11038110811.

Multiply by u⁴=1/16 to obtain physical scaled-area integrals:
B_{T,u=1/2,s=1}=6.60773592465330,
B_{D,u=1/2,s=1}=3.60083710539664,
B_{A,u=1/2,s=1}=3.00689881925666.

Against co-scaled u=s=1/2:
B_T=B_D=2.11895472717151, B_A=0.

At a fixed normalized staircase index n, u=1/q with fixed s=1 has r=q, so B=q^-4 F_q(n), **not** q^-4F_1(n). For q≥n the omitted indicators fill the whole normalized region, E_q(X,Y)=XY+q(X+Y)/2; hence B=O(q^-3) as q→∞ at fixed n, versus co-scaled O(q^-4). At fixed physical product cutoff the normalized n changes as q², which is a separate comparison (v14.767, v15.605).

## Method and implications

Reproducer `cone_fixed_step_gate81/reproduce.py` explicitly integrates each rectangular column using exact rational-power primitives, asserts the previous r=1 closed form at n=2,3,5,11,20, and independently tests strict positivity for r=2. The report/archive are `cone_fixed_step_gates_81_82.zip` in the present conversation. Scope: exact continuum interpolation and circle Jacobian, not raw d(n)/D(n) counts or measured field energy. The difference arises from choosing a transition generator whose step does **not** scale with the mesh; geometry does not independently tell us to select the original step for the proposed gravity interlay. No physical observable, G, chirality or photon follows.

**Next gate:** compare this induced complement signal under alternative justified area measures and the Paper C shifted-coordinate domain; test whether a normalized scale-invariant quotient can distinguish q=2 without importing physical G.

**HANDOFF:** target external-audit, gravity, sandbox; type fixed-step/co-scaled-step contrast audit; status open; independently verify E_s scaling, F_A2 positivity for n≥3, exact n=11 radicals, and the distinction between fixed physical product and fixed normalized n. No changes to frozen Suzuki.
