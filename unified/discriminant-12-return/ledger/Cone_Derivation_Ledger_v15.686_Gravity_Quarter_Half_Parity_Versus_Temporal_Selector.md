# Cone Derivation Ledger v15.686 — Gravity lane: quarter/half Casimir parity versus temporal 2:1 selector

**Date:** 2026-11-11 US Eastern. **Parents:** v15.624–632 EM/odd-quarter geometric Casimir sectors, parity projectors, actual cross-shell witness, odd-rung completion, rotor/SU2 obstruction and Taub–NUT quarter-pair/patching; v15.646–647 charge-changing-supermonopole comparator versus charge-preserving Taub–NUT KY/Dirac symmetries; v15.676 standard parametric-pump gate; v15.680 finite-cavity seeded omega_c versus unseeded 2 omega_c resonances; v15.685 closure of the present-laboratory K4 cosmological-mass route. **Status:** [D] exact q=2 sector parity rule and actual-witness parity; [D] Hamiltonian/dictionary obstruction to deriving a temporal frequency ratio from static shell spacing alone; [D] opposite energy-versus-wavelength frequency implications of the same 1/4:1/2 labels; [D] geometric-Casimir and Taub–NUT fixed-l transition-gap tests; [N] no currently derived Cone 2:1 temporal selector; [O] independently sourced map from shell coordinate to physical wavelength/energy/time and a physical chi-odd interaction. **Immediately prewrite live HEAD:** 49945153ece0f18380b2c6a172289dd689f83c5e. Collision searches found no v15.686 ledger entry, “temporal selector,” or “frequency dictionary” ledger result. Frozen Suzuki/far-tail objects untouched.

## Gate 231 — the quarter geometry does contain an exact parity selector, but the known physical candidates do not implement its odd rung

The recovered all-mesh q=2 geometric shell spectrum is

**j=L/4,   C_geom(L)=L(L+4)/16,   L=0,1,2,...**

with even L the embedded EM half-grid and odd L the additional quarter-only gravity-candidate shells. v15.626 proves the exact spectral grading

**chi=exp(16 pi i C_geom)=(-1)^L.**

Thus

**P_EM=(1+chi)/2,   P_G=(1-chi)/2**

are exact algebraic projectors on the formal shell direct sum. A minimal quarter-rung operator W with L→L+1 must satisfy

**{chi,W}=0,**

whereas a two-rung operator W^2 preserves the grading,

**[chi,W^2]=0.**

This is a genuine parameter-free **mode-parity selection rule** on the formal q=2 carrier.

However, the actual earlier cross-shell witness T of v15.602 moves

**L→L+2**

at q=2 and therefore satisfies **[chi,T]=0** (v15.627). Standard Larmor/rank-1/rank-2 rotor interactions do not realize quarter-spin transitions (v15.630). Standard Taub–NUT Killing–Yano/Dirac symmetries preserve the fiber charge k (v15.647). Hasebe's published supermonopole fermionic charge ladder realizes the matching half-charge/quarter-pair step only on an enlarged supersymmetric carrier, not as a derived Taub–NUT gravity interaction (v15.646).

Therefore the **selection rule exists algebraically**, but no currently sourced gravity/EM Hamiltonian supplies the required chi-odd W or fixes its matrix element.

## Gate 232 — shell spacing cannot determine a clock without a Hamiltonian

Let the established static shell increments be

**Delta u_G=1/4,   Delta u_EM=1/2.**

A temporal transition frequency is defined by a Hamiltonian gap,

**Omega=(E_f-E_i)/hbar,**

not by a dimensionless shell spacing by itself.

Take the most general local affine energy assignments compatible with the same static lattices,

**E_G(u)=a_G u+b_G,   E_EM(u)=a_EM u+b_EM.**

Then one minimal-rung frequency ratio is

**Omega_G/omega_EM
 = (a_G Delta u_G)/(a_EM Delta u_EM)
 = a_G/(2a_EM).**

The static 1/4 and 1/2 lattices place **no restriction at all** on the positive ratio a_G/a_EM. For any desired temporal ratio r>0, choosing **a_G=2r a_EM** realizes it while leaving every shell/Casimir/parity identity unchanged.

This is an exact underdetermination theorem: a bare representation lattice cannot select the primary Mathieu condition **Omega_G=2 omega_EM** until a physical Hamiltonian or propagation dictionary has been derived.

## Gate 233 — the same 1/4:1/2 geometry gives opposite answers under two natural dictionaries

The ambiguity is sharper than mere free normalization.

### Common affine ENERGY dictionary

If one *postulates* the same conversion constant Lambda in both sectors,

**E=Lambda u,**

then

**Omega_G/omega_EM=(1/4)/(1/2)=1/2.**

So the minimal quarter gravity rung oscillates at **half**, not twice, the EM half-rung frequency. Two quarter rungs match one EM half-rung at equal energy/frequency. The standard primary parametric pump condition

**Omega_pump=2 omega_EM**

would require a gravity transition of total shell increment

**Delta u_G=1,**

i.e. **four minimal quarter rungs**, under this energy dictionary. Nothing in the current Cone dynamics selects W^4 as the pump.

### Common WAVELENGTH dictionary

If instead one postulates that the labels are physical wavelengths in a common medium with common propagation speed c,

**lambda_G/lambda_EM=(1/4)/(1/2)=1/2,**

then because **omega=2 pi c/lambda**,

**Omega_G/omega_EM=2.**

This reproduces exactly the desired primary parametric ratio.

The crucial point is that the **same static lattice geometry supports 1:2 under an energy interpretation and 2:1 under a wavelength interpretation**. Therefore seeing the number 1/4 beneath 1/2 cannot by itself tell us which temporal relation is physical. A wavelength/propagation identification would be a new physical result, not an algebraic consequence of the Casimir mesh.

This makes precise the warning already recorded in v15.676: spatial scale ratio and temporal pump ratio are not interchangeable without a propagation dictionary.

## Gate 234 — using the geometric Casimir itself as the Hamiltonian does not rescue a universal 2:1

One might try to eliminate the arbitrary dictionary by declaring the already-derived geometric Casimir to be proportional to energy,

**H=Lambda C_geom.**

That still does not give the desired selector.

For q=2,

**C_geom(L)=L(L+4)/16.**

The one-quarter-rung gap is

**Delta C_1=C(L+1)-C(L)=(2L+5)/16,**

whereas the two-rung/half-grid gap is

**Delta C_2=C(L+2)-C(L)=(L+3)/4.**

Their ratio is

**Delta C_1/Delta C_2=(2L+5)/[4(L+3)],**

which is shell dependent and is never a universal 2. Declaring C_geom to be an energy operator would therefore introduce a non-equidistant spectrum rather than the desired fixed temporal lock. Moreover v15.630 already proves that C_geom on odd L is not the Casimir of an ordinary SU2 spin representation, so this Hamiltonian assignment has no independently derived physical status.

The actually derived fixed-l Lorentzian Taub–NUT time spectrum provides a second control. v15.631/v15.646 give

**E_k=hbar c k/(4l).**

A single k→k+1 quarter-pair transition has

**Omega_1=c/(4l),**

while a k→k+2 transition has

**Omega_2=c/(2l),**

hence **Omega_1/Omega_2=1/2**. The real Taub–NUT time quantization therefore supplies an equidistant quarter-pair energy ladder, but it does not turn the minimal quarter into a twice-frequency EM pump. Identifying its k→k+2 gap with an EM half-grid mode would itself be an additional cross-sector map.

## Gate 235 — exact disposition of the “gravity quarter grid pumps EM half waves” idea

The finite-cavity work established a real physical distinction:

- seeded inverse-Gertsenshtein-type conversion resonates at **Omega=omega_c**;
- unseeded primary parametric excitation is centered at **Omega=2 omega_c**.

The q=2 shell work separately establishes a real algebraic distinction:

- minimal odd quarter rung W is **chi-odd** and exchanges the even/odd shell sectors;
- W^2 is **chi-even** and returns to the same parity sector;
- the actual previously constructed cross-shell witness is chi-even.

What is **not** established is the bridge that identifies one of these shell operators with a time-dependent gravitational metric/constitutive modulation of frequency 2 omega_c.

Accordingly:

**[D]** The Cone has a parameter-free q=2 parity/mode-sector selector.

**[D]** Representation spacing alone cannot fix a temporal resonance.

**[N]** No existing rotor, Taub–NUT KY/Dirac operator, actual v15.602 cross-shell witness, or certified K4 tensor scale derives the required local 2:1 pump relation from the quarter/half labels.

**[C]** If the quarter and half labels are independently shown to be physical wavelengths propagating at the same speed, then the desired 2:1 frequency ratio follows immediately by inversion. That is the strongest surviving route.

**[C]** If instead they are energy/rung labels with a shared affine energy scale, the minimal quarter rung gives the opposite 1:2 relation; four quarter rungs would be required for a 2:1 pump.

Thus the attractive “pump at the EM peaks” picture remains a viable **conditional engineering mechanism**, but the current Cone geometry does not yet select its clock.

**Reproducibility:** research-notes/quarter_half_temporal_selector_v15_686.py, additive commit 49945153ece0f18380b2c6a172289dd689f83c5e. The exact SymPy test verifies the energy-dictionary ratio, arbitrary sector-normalization ratio, inverse wavelength ratio, q=2 Casimir gap formula, parity of one/two rungs, and the fixed-l Taub–NUT k=1 versus k=2 frequency ratio. No figures and no protected Suzuki modifications.

**HANDOFF:** external audit/gravity/sandbox should verify the dictionary theorem and, especially, the distinction between an algebraic shell coordinate and a physical wavelength. Check that the actual v15.602 q=2 witness remains chi-even and that no earlier ledger already derives a common propagation speed/wavelength interpretation for the quarter and half meshes. Reject any statement “1/4 automatically means twice the frequency” unless that missing physical map is supplied.

**NEXT:** inspect the strongest existing candidate for that missing map: the previously derived **EM→G power map / scale hyperbola** and its half-scale relation. Determine whether it genuinely identifies the q=2 shell coordinate with a physical wavelength or propagation length, or only maps dimensionless parabolic/hyperbolic geometry and divisor counts. If it supplies a covariant length/time interpretation with a common characteristic speed, v15.686 Gate 233 would turn the static half-scale into a real 2:1 temporal selector. If it does not, close the quarter-grid parametric-frequency claim as an analogy pending new dynamics.
