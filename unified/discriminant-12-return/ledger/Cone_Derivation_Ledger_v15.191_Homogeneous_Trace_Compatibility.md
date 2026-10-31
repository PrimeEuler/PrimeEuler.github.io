# Cone Derivation Ledger v15.191 — Homogeneous ADM trace compatibility diagnostic

Date 2026-10-30. Parents v15.124 averaged Hamiltonian, v15.118 scalar certificate, v15.190 2k trace. Research note research-notes/K4_Homogeneous_ADM_Trace_Compatibility_Diagnostic.md at commit 925254561161aaab741c1ce5bbc974114b9cdbd7. Prewrite HEAD checked; additive, other lanes protected.

[D, RESTRICTED] With h=a²(1−2ψ)δ, shift=0, first-order scalar standing p(t), k>0, homogeneous order-two ψ=m(t), lapse=n(t), exact ADM trace equation 3dotV−D²N+3NV²+(2/3)dotφI dotφI/N=0. Combine with existing v15.124 Hamiltonian mean mdot+(m+n)/t=tF0/12 and source-certified first-order oscillator. Independent SymPy simplification yields residual
R0=[−(2k^4+4k²+3)t²pdot²−2(k²+2)t p pdot+(3k^4+4k²)p²]/[3k²t²(1+k²)²].
All homogeneous m,n (and ndot) cancel. At k=t=p=1,pdot=0, R0=7/12. Thus generic data do NOT satisfy both homogeneous equations *within this restricted mean ansatz*. This does not invalidate the certified 2k scalar result v15.190 or prove nonlinear instability; it points to possible missing homogeneous backreaction/gauge freedom or a source coefficient issue, requiring source-native independent audit. The exact trace setup, F0 and reproducer derivation are in linked note.

Flags: homogeneous_trace_residual=GENERALLY_NONZERO_RESTRICTED; full_homogeneous_second_order_Einstein=OPEN; original_action_homogeneous_audit=OPEN; fixed_k_2k_trace=ZERO_V15_190; IR_uniformity=OPEN; nonlinear_future_stability=OPEN; other_lanes_touched=FALSE; Suzuki_quarter=PARKED.

HANDOFF
target: sandbox,external-audit
type: gravity-zero-mode-trace-obstruction
parent: v15.191
status: open
action: Independently derive the homogeneous ADM Hamiltonian and trace equations from corrected source action, check F0 and R0, test whether full zero-mode geometric degrees, background renormalization or a sign/normalization correction restores constraint propagation. Do not claim no-go for full Einstein theory.
deliverable: certified residual or corrected zero-mode closure theorem.

NEXT: source-native Bianchi/zero-mode trace audit; possible corrected mean-field backreaction.
