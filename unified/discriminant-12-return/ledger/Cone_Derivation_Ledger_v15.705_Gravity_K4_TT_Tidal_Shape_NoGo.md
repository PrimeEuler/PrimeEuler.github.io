# Cone Derivation Ledger v15.705 — Gravity: pure TT tidal shape unchanged by local K4 tensor dispersion

**Date:** 2026-11-11 US Eastern. **Parents:** v14.928/930 K4 elastic-solid tensor quadratic action and exact coasting evolution; v15.679/682/685 K4 local dispersion, cavity response and present-laboratory scale limitation; v15.703 standard GR tidal/rotor rank-two control. **Status:** [D] exact linearized curvature for prescribed local TT metric; [C] insertion of K4 dispersion into local WKB TT field; [N] no changed dimensionless eigenvalue ratio from tensor-mass dispersion alone; [O] full cosmological proper-frame K4 detector response including scalar/vector and wall/matter. **Immediately prewrite live HEAD:** 1f89877a5c21104dfcc91df44672eb11810d436e. Explicit v15.705 target ledger path absent. v15.704 was simultaneously occupied by Suzuki, so this gate moved additively to v15.705; no Suzuki/far-tail modification.

## Gate 282 — actual K4 tensor quadratic action preserves TT tensor field structure

v14.928 derived the K4 tensor action

**S_T²=(M_Pl²/8) integral a³[dot(gamma_ij)²-(partial gamma_ij)²/a²-m_T² gamma_ij²]**,

with **gamma_ii=0, partial_i gamma_ij=0**, and

**m_T²=(8 eta/3)H²**.

The tensor effective mass modifies frequency/propagation and time evolution in the expanding background. In this tensor-only quadratic action it does not introduce additional tensor polarizations or a new angular representation. The full scalar/vector channels, matter and proper detector-frame metric cannot be replaced by this pure-TT subproblem.

## Gate 283 — independent electric-curvature calculation at arbitrary K

Use a locally Minkowski, synchronous pure-TT perturbation propagating along z,

**h_ij(t,z)=exp[i(Omega t-Kz)] [[A,B,0],[B,-A,0],[0,0,0]]**,

with h_0mu=0. From the first-order Riemann tensor formula, the electric curvature measured on the local fiducial worldline is

**E_ij=R_(0i0j)=-(1/2)partial_t² h_ij
       =(Omega²/2)exp[i(Omega t-Kz)] [[A,B,0],[B,-A,0],[0,0,0]].**

There is **no K dependence in the algebraic tensor shape**. In particular, imposing ordinary lightlike propagation K²=Omega² or *conditionally* the K4 local timelike relation **K²=Omega²-m_T²** leaves exactly the same tracefree transverse polarization matrix.

For nonzero amplitude (and for a fixed real phase/quadrature of the curvature) the normalized eigenvalue pattern is **(+1,0,-1)** in either case, and **tr(E³)=0**. The common Omega²/2 amplitude factor drops out of the ratio.

This is a **local WKB / prescribed TT** statement. Exact cosmological FLRW curvature includes isotropic background and expansion-scale terms; a complete K4 detector would need its proper-frame tensor and scalar/vector matter responses. The present gate does not claim a global K4-versus-GR tidal no-go.

## Gate 284 — GR tidal-shape null survives the pure K4 tensor mass

A mass or non-null tensor dispersion alone can be detected conditionally through propagation phase/time of flight or frequency-dependent cavity overlap (v15.682), but **not** from the instantaneous, amplitude-normalized pure-TT curvature eigenvalue ratio in this local model.

Thus the dimensionless eigenvalue triple from v15.703 is a valid conventional **GR comparator**, not a new Cone/K4-specific effect. The different tensor dispersion changes the wave trajectory/phase and can affect transfer functions; it does not furnish new tensor angular selection rules or a quarter-grid rotor resonance. The present-day K4 mass scale remains cosmological H (v15.685), limiting its laboratory detectability.

**Reproducibility:** research-notes/k4_tt_tidal_shape_no_go_v15_705.py committed at 1f89877a5c21104dfcc91df44672eb11810d436e; locally executed PASS with exact symbolic linearized R_(0i0j), TT traces, characteristic polynomial and arbitrary K/m_T substitution. No image generation; no prior certified file edits.

**HANDOFF:** external audit/gravity/sandbox: verify the TT Riemann sign convention and characteristic polynomial; check that the claim is explicitly scoped to local WKB pure-TT and does not ignore independent K4 scalar/vector excitations or cosmological background curvature. Preserve Suzuki’s occupied v15.704 and all protected objects.

**NEXT:** test whether any *fully derived* K4 scalar/vector physical polarization can yield an amplitude-normalized tidal eigenvalue invariant different from pure TT without fitting eta. Check v14.935 full SVT field equations and actual matter constraints before assuming independent propagating polarization amplitudes. If a distinct shape arises only by selecting arbitrary scalar/vector amplitudes, record its conditional status and close the remaining tidal-shape shortcut.
