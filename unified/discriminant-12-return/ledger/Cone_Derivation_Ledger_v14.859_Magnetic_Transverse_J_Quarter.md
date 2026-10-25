# Cone Derivation Ledger v14.859 — Magnetic-drive transverse j weighting and quarter Casimir

Date 2026-10-25. Parents v13.364, v13.595, v14.858. Research-note source research-notes/Magnetic_Driver_Transverse_J_Casimir_Contact_Correction.md commit 4540b2c0fceafa4c1bb8ea31113896256e15b9ab. Prewrite HEAD 4540b2c0fceafa4c1bb8ea31113896256e15b9ab. Additive-only gravity lane; protected Suzuki and far tail untouched.

[D] Magnetic field quantization axis Z maps to Cone X. In a spin j multiplet, Casimir \(j(j+1)=(j+\tfrac12)^2-\tfrac14\). The transverse moment in |j,m> is \(\langle J_x²+J_y²\rangle=j(j+1)-m²\) in ħ=1 units. A single upward driven transition obeys
\[
|\langle j,m+1|J_+|j,m\rangle|²=(j-m)(j+m+1)
=(j+\tfrac12)^2-(m+\tfrac12)^2.
\]
The quarter is exactly the half-step Casimir completion and centered transition-lattice structure from v13.595; this MUST NOT be conflated with the separately scaled physical u=1/2 factor grid. The driven multiplet is connected, not a direct sum of independent adjacent transitions.

[D/I] If one labels ordered contacts (a,b) via the *conventional* choice oscillator occupations n1=a-1,n2=b-1, then j=(a+b-2)/2 and m=(a-b)/2. The transverse arithmetic weight is
\[
j(j+1)-m²=ab-\frac{a+b}{2}.
\]
For N=12 the six ordered contact weights are (11/2,8,17/2,17/2,8,11/2), totaling exactly **44**, whereas the summed full Casimir weight from v14.858 is 113. Define candidate \(W_\perp(N)=\sum_{ab\le N}(ab-(a+b)/2)\). This is an exact weighted count under the chosen contact-state mapping, not a measured response, stiffness or energy. The source research-note includes an explicitly superseded draft numerical list; the corrected six-contact list and total 44 here are definitive.

[O] Determine how a seat-balance displacement couples to the full magnetic H(t), which state/density matrix is prepared, and compute the quantum susceptibility/second derivative of dressed energy. Until then do not identify W_perp with contact energy or Newton G. No Suzuki/Weil carrier identification.

Flags: transverse_casimir_identity=EXACT; half_step_driver_edge=EXACT; shell12_Wperp=44; contact_physical_excitation=OPEN; G_derived=false; Suzuki_payloads_touched=false; far_tail_touched=false.

HANDOFF
target: external-audit
type: magnetic-driver-contact-quarter-shift
parent: v14.859
status: open
action: Verify operator identities and magnetic-drive basis orientation, occupation convention, pairwise shell12 weights totaling 44, and distinction of transverse state variance from driven transition strength. Do not modify Suzuki/far-tail.
deliverable: scoped audit verdict.
