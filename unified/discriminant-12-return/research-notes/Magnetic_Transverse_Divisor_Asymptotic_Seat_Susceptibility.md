# Magnetic transverse divisor sum and central-seat susceptibility: exact test

Date 2026-10-25. Parents v13.595, v14.856–859. Gravity side lane, no Suzuki/far-tail modifications.

## I. Exact weighted arithmetic [D]
Under chosen contact labels j=(a+b-2)/2, m=(a-b)/2, the transverse Jx²+Jy² moment at ħ=1 is \(w(a,b)=j(j+1)-m²=ab-(a+b)/2\). Thus
\[
W_\perp(N)=\sum_{ab\le N}w(a,b)
=\sum_{k\le N}k\,d(k)-\sum_{k\le N}\sigma_1(k),
\]
where \(\sigma_1(k)=\sum_{a|k}a\). This is an identity, not an energy assignment. The standard summatory estimates and partial summation imply
\[
W_\perp(N)=\frac{N²}{2}\log N+
\left(\gamma_E-\frac14-\frac{\zeta(2)}2\right)N²+
O(N^{3/2})
\]
(the stated coarse error is safe). Consequently
\[
\boxed{W_\perp(4n)-16W_\perp(n)=8n²\log4+O(n^{3/2})}.
\]
The 16 is the appropriate leading power scale, not the fourfold divisor contact-count scale. Direct integer enumeration: W(12)=137,W(48)=3503, W(25)=749,W(100)=18580,W(400)=403500. For n=12 the normalized-dilation excess is 3503-16*137=1311; for n=25 it is 18580-16*749=6596; for n=100 it is 403500-16*18580=106220. The shell ab=12 transverse sum equals 44.

## II. Explicit magnetic response, not just a state weight [D/I]
To test if a transverse magnetic drive creates a positive restoring potential, take a fixed spin-j multiplet with Hamiltonian
\[
H_j(\delta)=-\Omega J_z-g\delta J_x,\quad \Omega>0.
\]
This is a separately CHOSEN static/adiabatic seat-to-drive coupling, not the resonant time-dependent Hamiltonian of v13.595; g has appropriate dimensions and J is dimensionless. SU(2) covariance diagonalizes it exactly:
\[
E_{j,m_\parallel}(\delta)=-m_\parallel\sqrt{\Omega²+g²\delta²}.
\]
On the adiabatic ground branch m_parallel=j,
\[
E_{\rm ground}''(0)=-jg²/\Omega <0 \quad(j>0).
\]
Thus simple linear coupling of a balanced seat displacement to a transverse magnetic field produces NEGATIVE quadratic energy curvature: it *softens/destabilizes*, rather than autonomously creating a restoring seat. With an independently positive bare stiffness k0, the effective curvature is \(k_{\rm eff}=k_0-(g²/\Omega)\sum j\) for physically independent adiabatic ground-state contacts. The independent-contact additivity, common Ω and g, and ground-state occupation are assumptions. A state |j,m> that is not an adiabatic eigenstate or a resonantly driven Floquet state requires a density matrix and genuine time-dependent susceptibility; one cannot infer stiffness from W_perp alone.

If the field has seat dependence Ω(δ), terms proportional to Ω'' and different states may alter signs; those are different actions that must be independently specified. The transverse Jx² expectation \([j(j+1)-m²]/2\) is the squared matrix-element sum, not the static susceptibility, which involves energy denominators and signed occupation differences. This is the key separation between arithmetic weighted counts and magnetic response.

## III. Physical boundary [O]
The exact 1/4 in the magnetic Casimir and half-step transitions does not by itself select gravity u=1/2; v14.767 demonstrates the half/quarter factor grids are related by dilation. Need physically derived seat coupling and prepared-state dynamics before extracting restoring stiffness or G. No Suzuki/Weil identification.
