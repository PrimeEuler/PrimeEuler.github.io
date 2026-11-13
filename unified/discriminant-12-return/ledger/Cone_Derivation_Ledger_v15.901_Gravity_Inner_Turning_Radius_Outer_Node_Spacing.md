# Cone Derivation Ledger v15.901 — Inner sqrt(n) turning radius and outer n+1 phase-node spacing

**Date:** 2026-11-13 US Eastern. **Gravity.** Parents: v13.177, v14.367, v15.867/869 node/rate parabola, v15.895–900 two-circle geometry and rotor turning points. Live master HEAD immediately before write: 0084f26dd01f4251f22768d93ab4ce97312928ce. Target checked absent. Additive only; no modification to Audit/Sandbox/Suzuki/certified material.

**User clarification:** sqrt(n) circle is a radial turning/tuning point and also organizes the n+1 outer circle's *frequency node spacing*. Need avoid conflation of stationary phase stations, wave zeros, physical temporal frequency and physical action.

**[D] Exact geometry of a CONDITIONAL n+1-station model.** Fix normalized integer n>=1 and factor scale u>0. R_i=u sqrt(n), R_o=u(n+1)/2. The Cone identity is 2R_o/u=1+(R_i/u)^2=n+1. IF the outer circumference is equipped with N=n+1 equally spaced phase stations, angular separation is

**Delta theta_o=2pi/(n+1)**,

and outer *arc-length* separation is

**Delta ell_o=(2pi R_o)/N=pi u**, independent of n.

Thus the inner radius labels n, thereby fixing N and outer angular spacing *under the additional N=n+1 count rule*. The radius law does not by itself require this wave count; that is a separate spectral/boundary-condition identification.

**[C] Node meaning and count caveat.** N evenly spaced phase *marks* are compatible with any positive integer N. A complex phase winding exp(iN theta) returns to the same value at N uniformly spaced stations, but sin(N theta) has 2N zeros per 2pi; a real standing-wave sin(m theta) with integer mode m has 2m zeros (nondegenerate), so exactly N standing-wave zero nodes would require N even and m=N/2. Therefore 'n+1 nodes' is ambiguous unless a specific waveform and boundary condition is specified. Neither the v15.867 half-turn transition lattice nor the v15.869 rate-crown parabola automatically yields this N=n+1 law on the circle.

**[D] Contracting a fixed N-station pattern under conserved angular momentum.** If each radius becomes a physical length r=ell_* R and the same N material/phase marks are carried inward from r_o to r_i in a thin ring with I=M r², conserved L gives omega_i/omega_o=(r_o/r_i)²=gamma_n² where gamma_n=(n+1)/(2sqrt n). The passage frequency of rigidly carried marks across a laboratory ray is f_pass=N omega/(2pi), hence

**f_pass,i/f_pass,o=gamma_n²**.

At the inner radius their arc separation is **Delta ell_i=2pi u sqrt(n)/(n+1)=pi u/gamma_n**, while the outer arc step was pi u. Thus constant outer arc spacing is NOT conserved through ring contraction with fixed N; holding spatial node spacing fixed instead would require changing N and is a different physical hypothesis. The relative acceleration and frequency ratios remain conditional on thin-ring mechanics and a prescribed radius path; angular momentum conservation does not create the contraction force or determine absolute omega.

**[N] Physical frequency selector.** The index n and circle radii fix station geometry if N=n+1 is postulated, not a source frequency in Hz or a spectral gap Delta f. Frequency has units 1/s; geometry is invariant under rescaling L or ell_* with unchanged normalized phase spacing. The original Cone's velocity-axis radii (m/s) are also distinct from mechanical rotation lever arms (meters). A physical time law, field stiffness and wave boundary condition must be derived before interpreting the marks as EM or gravity frequency nodes.

**Reproducer:** research-notes/k4_two_circle_node_spacing_v15_901.py, commit 0084f26dd01f4251f22768d93ab4ce97312928ce. Fresh SymPy identities and integer examples verified locally; independent Audit pending.

**Next gate:** compare the actual Cone counting/boundary action spectrum to N=n+1 phase stations and alternatives N=2(n+1) or N=n; apply full angular-momentum and energy matching to a derived field wave equation, rather than assuming n+1 labels are temporal nodes. Audit/Muse: specifically assess the distinction between phase marks vs zeros, n+1 as diameter vs mode count, and outer fixed arc pitch versus inner contracted pitch.
