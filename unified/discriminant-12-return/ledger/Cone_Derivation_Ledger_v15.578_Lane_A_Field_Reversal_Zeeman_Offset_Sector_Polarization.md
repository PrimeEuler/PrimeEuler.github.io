# Cone Derivation Ledger v15.578 — Lane A: field-reversal symmetry, Zeeman offset-sector polarization, and energy-current no-go

Date: 2026-11-09. Parents: v13.595, v13.598, v15.140, v15.180, v15.572–577 (v15.577 External Audit Round 518 independently verified v15.576). Status **[D] exact finite-dimensional identities**, **[C] candidate Zeeman coupling and equilibrium model**, **[O] physical carrier, energy source, chirality/acceleration channel**. Latest prewrite HEAD ee1380fe3108ac7e88ec4ff0376aa56850f85f04; no existing v15.578 collision found. Additive; Suzuki production and far-tail unchanged.

## 1. Field reversal is exactly shell reflection [D]

On shell j=N/4, basis i=0,...,N and m_i=-j+i/2, define magnetic M=diag(m_i), original step-one J_+ with squared AM-GM weights (j-m)(j+m+1), half-step B_+ with squared weights (j-m)(j+m+1/2), adjoints J_-,B_-, Jx=(J_++J_-)/2, Bx=(B_++B_-)/2, offset grading Gamma=(-1)^i, mirror R|i>=|N-i>. Set for real omega,g,h:

H(omega,g,h)=omega M-g Jx-h Bx.

Then RMR=-M, R Jx R=Jx, R Bx R=Bx, hence
**R H(omega,g,h)R=H(-omega,g,h)**.

Also [Gamma,Jx]=[Gamma,M]=0, {Gamma,Bx}=0, R Gamma R=(-1)^N Gamma. So for odd quarters (N odd) the mirror exchanges two offset classes; reversing the field reverses their relative energetic preference. The symmetric model has no field-independent choice of 'left' or 'right'. These are exact finite matrices; do not identify Gamma with Lorentz gamma5.

## 2. Full j=3/4 spectrum and sector selection [D/C]

For N=3, the Gamma=+ chain spans i=(0,2), Gamma=- spans i=(1,3). With h=0 the two 2x2 Hamiltonians are

H_+ = [[-3 omega/4, -g sqrt(3/2)/2],[-g sqrt(3/2)/2, omega/4]],
H_- = [[-omega/4, -g sqrt(3/2)/2],[-g sqrt(3/2)/2,3 omega/4]].

Their eigenvalues are E_{Gamma,s}= -Gamma*omega/4+s*sqrt(omega²+(3/2)g²)/2, s in {+1,-1}. The chain-center splitting is |omega|/2, whereas the original within-chain AM-GM strengths remain 3/2 on both channels.

For the **specified** Gibbs state rho_beta=exp(-beta H)/Z (beta>0) with h=0:

Z_Gamma=2 exp(beta Gamma omega/4) cosh(beta sqrt(omega²+(3/2)g²)/2),
and **<Gamma>_beta=tanh(beta omega/4)**.

This exact thermal polarization is independent of g and odd in omega. The result does NOT prove that a real physical field couples to the odd-quarter magnetic coordinate M; that coupling was posited as the candidate test Hamiltonian. For h nonzero Gamma ceases to be a conserved quantum number, though R H(omega)R=H(-omega) still holds.

## 3. Directed transition energy and no steady current [D]

For pure J drive, the gap between upward and downward connected m-states is omega. At j=3/4, beginning in a lower m state of either chain, coherent Rabi transfer to the upper state has exact probability
P(t)=[(3/2)g²/(omega²+(3/2)g²)] sin²[t sqrt(omega²+(3/2)g²)/2].
For the reversed initial state the transfer probability is the same; its bare Zeeman-energy change has opposite sign. Half-step B channels have bare energy gap omega/2. Reversing omega swaps the sign of these energy transfers; unequal physical emission/absorption intensities still require populations, a bath, polarized drive or other physical coupling.

For any finite Hermitian H with amplitudes c_i, define oriented edge current i->k (k>i) as I_{ik}=2 Im(conj(c_k) H_{ki} c_i). Then
d<omega M>/dt=Σ_{i<k} omega(m_k-m_i) I_{ik}.
In a time-independent H, the interaction sector supplies the opposite energy transfer and d<H>/dt=0. In any stationary rho commuting with H, d<omega M>/dt=0; in the Gibbs state for this real-symmetric H, all edge currents vanish separately. A field-biased **population selector** is not automatically a sustained energy flux.

The original J out-of-shell escape weight c=j+1/4, its boundary defect D and Casimir deficit E remain intact under this test; without an explicit external target and coupling, there is no probability leakage. The opposite-opening confocal acceleration parabolas of v15.235/270/274 and drive/reaction *interpretation* of v15.275 are not equated to actual measured Zeeman transitions by this finite-H calculation.

## 4. Checks, boundaries, audit handoff

Independent exact SymPy matrix reconstruction and assertions for N=1,2,3,4,5,7,9 established field reversal, Gamma symmetry and coupling selection, and the j=3/4 eigenvalues; j=5/4 original squared strengths (5/2,3,3,5/2) and half-step squared strengths (5/4,2,9/4,2,5/4) also reproduced. A reproducible script and report were generated in Lane A response archive cone_field_orientation_zeeman_gates_46_47.zip.

No new physical chirality, gravity coupling G, acceleration-to-deceleration force law, emission spectrum, mass selector or Suzuki operator identity follows. The next discriminating gate is to test whether a source-defined factor-exchange odd term or a physically defined bath breaks the degeneracy/establishes detailed balance without importing the wanted asymmetry by hand.

**HANDOFF** target external-audit; type field orientation / sector thermal-selection / energy-current audit; status open; action independently verify the reflection conjugacy, j=3/4 block spectrum and Gibbs tanh formula (including sign), coherent transition probabilities and current identity, and scrutinize whether a claimed direction/energy selector has been overinterpreted. Production fence unchanged.
