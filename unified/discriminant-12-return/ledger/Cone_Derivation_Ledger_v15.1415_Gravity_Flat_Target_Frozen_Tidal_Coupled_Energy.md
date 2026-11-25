# Cone Derivation Ledger v15.1415 — Preliminary coupled flat-target Maxwell/sigma frozen-tidal surrogate conserves energy

**Date:** 2026-11-24 Eastern / GitHub UTC Nov 25. **Gravity/Cone.** **Status:** [N PASS] three fields evolved from one explicit real local 1+1D Lagrangian including electromagnetic feedback, with no externally prescribed source; [N PASS] conserved total Hamiltonian to ~7×10^−10 relative in N32 and N48 runs, zero-coupling and half-coupling controls; [NEGATIVE] flat target is NOT actual hyperbolic H² geometry, fixed arbitrary tidal tensor component is not complete Weyl, Einstein/K4 gravity and metric backreaction absent; [OPEN] full action and causal principal symbol, actual quarter-grid carrier and parameter selection. **Pre-ledger live HEAD checked** research note 31a0066d8b263bc0f05f4687483a4fd430c559bc. Strict additive.

## Gate 1354 — variational source-side feedback rather than externally prescribed current

Let A=A_z(t,x) be the transverse dimensionally reduced Maxwell amplitude, with internal scalar coordinates u(t,x),v(t,x). Use the explicitly *chosen* reduced action `S=∫dt dx L` with

`L=½(A_t²−A_x²+u_t²−u_x²+v_t²−v_x²)+g A_t(u_t v_x−u_x v_t)`.

The term can be motivated as retaining just one fixed Weyl–F–target-area tensor component, but this is **not an exact consistent truncation of the complete Weyl tensor**. The g coefficient is freely chosen; it has no derivation from the geometric quarter radius, finite SU2 intersector operator, or physical gravitational constant. It is a useful local classical coupled field theory with standard translational invariance and thus a conserved Noether energy. Its canonical momenta are

`p_A=A_t+g(u_t v_x−u_x v_t)`,
`p_u=u_t+g A_t v_x`,
`p_v=v_t−g A_t u_x`.

The symmetric kinetic matrix in velocity coordinates (A_t,u_t,v_t) is
`M=[[1,g v_x,−g u_x],[g v_x,1,0],[−g u_x,0,1]]`, with `det M=1−g²(u_x²+v_x²)`, so it is positive definite whenever `g²(u_x²+v_x²)<1`. Exact Euler–Lagrange momentum equations:

`∂t p_A=∂x A_x`,
`∂t p_u=∂x(u_x+g A_t v_t)`,
`∂t p_v=∂x(v_x−g A_t u_t)`.

The full canonical Hamiltonian density is
`H=½(p_A A_t+p_u u_t+p_v v_t)+½(A_x²+u_x²+v_x²)`,
where the velocities are found by inverting M; no externally supplied source energy is assumed.

## Gate 1355 — actual coupled numerical energy consistency

On periodic x∈[0,2π), use spectral derivatives, time evolution via high-accuracy DOP853, and initial A=A_t=0, u=.16 sin x, v=.13 sin(2x+.3), u_t=.16 cos x,v_t=−.13 cos(2x+.3). Canonical p_A is initially *not* zero because it contains g B_tx even when A_t=0. This correctly encodes no **initial electromagnetic velocity** rather than incorrectly setting every canonical electromagnetic momentum to zero.

**Actually executed Python** `/mnt/data/cone_gate/k4_coupled_frozen_tidal_energy_v15_1415.py`; additive GitHub equivalent `research-notes/k4_flat_target_coupled_energy_v15_1415.py`, SHA **31a0066d8b263bc0f05f4687483a4fd430c559bc**, exact committed-byte Audit replay pending. Local test outputs:

| N | g | final t | E_initial | max total relative energy drift | final A RMS |
|---:|---:|---:|---:|---:|---:|
| 32 | .12 | 3 | .033925 | 6.2284×10^-10 | 8.2842552263×10^-5 |
| 32 | .06 | 3 | .033925 | 6.8150×10^-10 | 4.1585684853×10^-5 |
| 32 | 0 | 3 | .033925 | 6.9797×10^-10 | 0 |
| 48 | .12 | 3 | .033925 | 6.1874×10^-10 | 8.2842552264×10^-5 |

For small g the EM field RMS is nearly proportional to g; zero coupling gives exactly zero. The total Hamiltonian is conserved, so its EM growth is not an energy source placed outside the model. Its decomposition into separate EM, scalar and mixing pieces is not uniquely gauge invariant in an arbitrary gauge theory; the total energy is the actual Noether invariant of this chosen reduced theory.

**Crucial negative:** There is no actual dynamical Lorentzian metric or gravitational wave in this calculation, no full Weyl contraction and no curved H² sigma target. This is a preliminary necessary-condition model, not the physical resolution of all GR+K4+Maxwell+quarter coupling gates. The curved-target upgrade and causality check follow at v15.1416 and 1417. The 45.31 Dirac rapidity remains an empirical input, and v15.1387/1398 show quarter-radius scaling does not determine g.

**AUDIT:** independently derive all canonical momenta, Euler–Lagrange equations and conserved Hamiltonian, replay committed code without patching, confirm N32/48 and half-g/zero-g controls, and do not label this full Einstein energy conservation.
