# Gravity v15.1543 — Actual tilted plane and second-harmonic rotor: no universal mesh crossing selector

Date 2026-11-26. Parent v15.1542. Live HEAD before source write 05e7f632987cfa70c8c08d2c8f0fef2a2041e5da. Audit Round 668 confirmed v15.1540/1541; no newer audit return at initial check. Additive only.

## Gate 1439 exact geometry
Unit slope cone Z²=X²+Y², plane Z cosθ−X sinθ=h>0. Orthonormal plane coordinates (X,Z)=(-h sinθ+u cosθ,h cosθ+u sinθ). Then Y²=h²cos2θ+2hu sin2θ−u²cos2θ. Translate u=u0+q with u0=h(sinθ−cosθ)/(sinθ+cosθ). Where denominator nonzero, constant term vanishes and linear term is 2h q. Thus Y²=2h q−cos2θ q². λ=−cos2θ, exact bounded second harmonic. At θ=0 circle, π/4 parabola, π/2 hyperbola. The branch vertex chart is singular where sinθ+cosθ=0, so full rotor cycles use λ as global coefficient, not a single globally regular vertex chart. Plane angle is not yet identified dynamically with existing physical action circle phase. h is plane normal offset and common vertex curvature radius in these intrinsic coordinates.

## Gate 1440 candidate rotor action
Use normalized time s and independent displacement x. Candidate L=(x'²+Jθ'²)/2−V, V=−hx+(cos2θ)x²/2+g x⁴/4, J,g>0. Equations x''=h−cos2θ x−g x³, Jθ''=x² sin2θ. E conserved by time translation. λ is bounded without prior harmonic λ potential; g>0 suffices for coercivity in x and bounded velocities at finite E (angle compact). g=0 remains unbounded below in hyperbolic sector. At θ=0,θ'=0 the rotor remains identically there by uniqueness for every h; a seed angular velocity or tilt is required. This is an introduced mechanical witness, not derived Cone field action. Quartic term alters fixed-conic trajectories; angle dynamics do not describe a rigid physical plane without further kinematic derivation.

## Gate 1441 actual numerical nonselector
Executed /mnt/data/cone_plane_rotor.py with SymPy geometry assertions and SciPy solve_ivp; exact same text committed at 2f755dce31f61aafe2aeeab79c722eebba5665d5 in research-notes/k4_plane_rotor_v15_1543.py. J=g=1, x=x'=θ=0 initially, θ'=w0. s=0..20, rtol=1e-11 atol=1e-13 max_step=.03; zero events for λ. Counts (columns h=1/4,1/2,2/3,1):
w0=0: 0,0,0,0
w0=.1: 2,5,7,7
w0=.5: 5,7,9,10
w0=1: 7,10,12,9
Maximum sampled absolute energy drift across all 16 runs 1.84e-10. At w0=.1 both half and quarter reach λ near +1. Thus separation from v15.1542 is not robust to replacing the prescribed cutting-coordinate potential with an actual bounded plane angle. No universal mesh selector. Exact geometry survives; dynamics remain model-dependent. Independent audit pending. Next test whether a canonical action-angle or Spin(2) representation fixes rotor inertia and initial angular momentum and whether symmetry permits the quadratic interaction; avoid imposing a desired scale. GH subsidiary/N40 remain open.