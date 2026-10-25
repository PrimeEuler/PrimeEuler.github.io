# Cone Derivation Ledger v14.860 — Magnetic transverse divisor asymptotic and seat susceptibility

Date 2026-10-25. Parents v13.595, v14.856–859. Research note research-notes/Magnetic_Transverse_Divisor_Asymptotic_Seat_Susceptibility.md commit d4bf0a4b25b1af43d45a1edb9469fb5d1ec56925. Live prewrite HEAD d4bf0a4b25b1af43d45a1edb9469fb5d1ec56925. Additive only; no protected Suzuki or far-tail changes.

[D] For Schwinger-labelled ordered contacts, transverse spin variance has weight \(w(a,b)=j(j+1)-m²=ab-(a+b)/2\). The cumulative sum is \(W_\perp(N)=\sum_{k≤N}[k d(k)-\sigma_1(k)]\). Standard summatory formulas imply
\[
W_\perp(N)=\frac12 N²\log N+(\gamma_E-\tfrac14-\tfrac12\zeta(2))N²+O(N^{3/2});
\quad W_\perp(4n)-16W_\perp(n)=8n²\log4+O(n^{3/2}).
\]
Exact enumerations W(12)=137,W(48)=3503,W(25)=749,W(100)=18580,W(400)=403500; corresponding n=12,25,100 sixteenfold anomalies 1311,6596,106220. The correct leading rescaling is 16, not 4.

[D/I] Test a specifically DECLARED static transverse magnetic seat coupling \(H_j(\delta)=-\Omega J_z-g\delta J_x\), Ω>0. Its exact eigenbranches are \(E_{j,m_\parallel}=-m_\parallel\sqrt{\Omega²+g²\delta²}\). For adiabatic ground state m_parallel=j, \(E''(0)=-jg²/\Omega\): this magnetically driven branch SOFTENS the seat and is not a restoring mechanism by itself. With independent positive bare seat stiffness k0 and independently occupied contacts (not established by arithmetic) the effective curvature would be \(k_0-(g²/\Omega)\sum j\). The state transverse moment \(j(j+1)-m²\) is not itself a susceptibility: Kubo/perturbation response requires transition matrix elements, spectral denominators and occupations, and resonant Floquet drive v13.595 is not equivalent to this static Hamiltonian. No physical state preparation or energy-contact rule is derived.

[O] Determine a physical seat-to-drive coupling and its symmetry/occupation constraints. Derive frequency-dependent susceptibility or stable interaction from real magnetic-drive protocol; avoid implying the 1/4 Casimir identity selects Newton G or a u=1/2 physical normalization.

Flags: Wperp_asymptotic=EXACT; fourfold_corrected_baseline=16; static_ground_seat_curvature=NEGATIVE; magnetic_restoring_derived=NO; contact_independence=UNPROVED; G_derived=false; Suzuki_payloads_touched=false; far_tail_touched=false.

HANDOFF
target: external-audit
type: magnetic-weighted-divisor-and-seat-response
parent: v14.860
status: open
action: Independently verify Wperp arithmetic identity, coefficient of N², finite examples, factor 16 under N->4N, and exact static SU(2) diagonalization and negative ground-state seat curvature. Guard distinction from resonant Floquet magnetic drive and physical contact independence; do not touch Suzuki/far-tail.
deliverable: scoped verdict.
