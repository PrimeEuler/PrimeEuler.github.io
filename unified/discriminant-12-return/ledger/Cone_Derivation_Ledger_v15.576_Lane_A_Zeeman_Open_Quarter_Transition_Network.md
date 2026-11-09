# Cone Derivation Ledger v15.576 — Lane A: Zeeman-style transition network on odd-quarter open shells

Date 2026-11-09. Parents v13.583, v13.595, v13.598, v15.140, v15.180, v15.275, v15.572–575. Status [D] exact finite-Hamiltonian identities; [C] magnetic/field interpretation on non-SU(2) open carrier; [O] physically selected interaction and out-of-shell target. Prewrite HEAD 95967c94c834235c30e8f2b07990b3c9fbc1d049 (External Audit Round 517); no v15.576 collision. Additive only; production Suzuki and far-tail untouched.

## Background/collision guard
The physical resonant Zeeman coupling profile \(\sqrt{(j-m)(j+m+1)}\) on complete SU(2) multiplets is *already proved and audited* in v13.595, v13.598. The two opposite-sign confocal parabola crossing identities are proved in v15.235/274, and identifying one family as the drive and the other as reaction is [I] in v15.275, audited v15.276. Recent audit v15.575 independently verifies v15.572–574 (boundary defect, AM-GM offset parity, half-step SU(2) construction). This entry applies the established weighted paths to **candidate Hermitian Hamiltonians** for the odd-quarter, originally non-SU(2) carrier.

## Definitions and conservation theorem [D]
On shell \(j=N/4\), basis \(m_i=-j+i/2\), \(i=0,...,N\), define diagonal \(M=J_z^q\). Original \(J_+|m\rangle=\sqrt{(j-m)(j+m+1)}|m+1\rangle\) only if target is in the finite shell, adjoint \(J_-\). Alternative half-step \(B_+|m\rangle=\sqrt{(j-m)(j+m+1/2)}|m+1/2\rangle\), adjoint \(B_-\). \(\Gamma|i\rangle=(-1)^i|i\rangle\). Consider \(H=\omega M-g(J_++J_-)/2-h(B_++B_-)/2\) for real \(\omega,g,h\), \(\hbar=1\).

This finite H is Hermitian, so every state norm is conserved. With h=0, \([H,\Gamma]=0\) and no inter-sector population transport exists. With h nonzero the new half-step channel connects the two offset classes, but the original J's missing destination states remain missing; \(D=[J_+,J_-]-2M\) remains nonzero. An **algebraic escape weight** is not probability leakage or an emitted photon unless an external target and Hamiltonian coupling are supplied.

## Transition-strength predictions of the two mathematical drives [D]

Edge matrix-coupling squares are \(g^2(j-m)(j+m+1)/4\) for J steps, and \(h^2(j-m)(j+m+1/2)/4\) for B steps. These are *relative squared couplings*, not measured line intensities without populations, polarization, coupling and spectral factors.

For j=3/4 (states -3/4,-1/4,+1/4,+3/4): original J edges \(0\to2\) and \(1\to3\) each have squared ladder weight 3/2; their excluded outgoing weights both have square 1. The B consecutive-edge squared weights are **3/4,1,3/4**. At omega=0, spec(-g Jx) = \(\{\pm g\sqrt{3/2}/2\}\) each twice; the J network is two disconnected two-state blocks. Meanwhile spec(-h Bx) = \(\{-3h/4,-h/4,h/4,3h/4\}\), the ordinary spin K=3/2 representation under **alternative** half-step operators.

For j=5/4, original J squared edges are (5/2,3,3,5/2), two disconnected mirror three-state chains; B squared edges are (5/4,2,9/4,2,5/4), one connected six-state chain. Both patterns are reflection symmetric with no built-in directional preference.

For initial |i=0> at j=3/4 under pure B drive, the opposite-Gamma probability at short time is \(3h^2t^2/16+O(t^4)\) (hbar=1), while under pure J drive it vanishes identically for all time. The B coupling is sufficient for cross-sector *connectivity*, not for defining physical acceleration vs deceleration or repairing the original J Lie-algebra defect.

## Explicit leakage extension and its unselected coupling [C]
For odd quarters the existing boundary projector identities are \(D=c(P_+-P_-)\), \(E=c(P_++P_-)/2\) with \(c=j+1/4\). If one *adds new external Hilbert states* and a map T obeying \(T^\dagger T=c(P_++P_-)\), a Hermitian block Hamiltonian with off-diagonal \(\lambda T\) yields short-time external occupancy \(P_{\rm ext}(t)=|\lambda|^2c t^2\langle P_++P_-\rangle+O(t^3)\) for initially internal normalized state. This is mathematically consistent but the external states, frequency, \(\lambda\), and any irreversible continuum limit are NOT selected by the cone. Without this added channel \(P_{\rm ext}=0\) identically. Equal escape norms do not imply directional emission or a preferred chirality.

## Guardrails and next gate
The original step-one AM–GM transition weights yield an exact Zeeman-*style* comparison but odd-quarter fragments cannot be ordinary physical spin-j SU(2) multiplets (nonzero D). The action/reaction interpretation of the parabolas is not upgraded to dynamics merely by the mirrored J couplings. No kinetic-to-potential energy accounting, G, mass hierarchy, electroweak chirality, magnetic spectrum, or Suzuki intertwiner is derived. A serious next gate requires sourcing either a physical field-odd term or the external boundary targets from the existing cone geometry and checking all energy/selection rules.

Reproducer: independent exact SymPy script zeeman_open_shell.py, run for N=1,2,3,4,5,7,9, with characteristic-polynomial assertions and symmetry checks, plus report in user handoff package cone_zeeman_open_quarter_gates_44_45.zip.

HANDOFF target external-audit; status open; type finite Hamiltonian/transition intensity audit; checks: verify exact weight profiles, both j=3/4 spectra, conserved Gamma for J and broken Gamma for B, j=5/4 weights, and distinction between formally nonzero boundary weights and actual leakage. No frozen or production changes.