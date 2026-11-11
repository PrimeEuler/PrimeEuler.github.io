# Cone Derivation Ledger v15.647 — Gravity lane: Taub–NUT Dirac/Killing–Yano symmetries preserve fiber charge; a quarter-pair shift needs additional structure

**Date:** 2026-11-10. **Parents:** v14.731–732 gravitational dyon pair; v15.631–632 normalized Misner Fourier/Chern winding; v15.637 actual TN worldline charge projector; v15.646 Hasebe supermonopole fermionic half-charge ladder and bundle/spin/energy obstructions. **Status:** [D] exact fiber-isometry operator algebra and bundle patching; [I] literature comparison; [O] global TN-derived charge-changing spinor operator and gravity coupling. **Fresh prewrite live HEAD:** 5e2b109f03b6aa143bbcdfdc66ee852f5a1e1976 (new exact reproducer), duplicate v15.647 search empty. Frozen Suzuki/far-tail work and proposed Suzuki physical-quarter weld untouched.

**Primary references.** Ion I. Cotăescu and Mihai Visinescu, *Runge–Lenz operator for Dirac field in Taub–NUT background*, Phys. Lett. B **502** (2001) 229–234, DOI 10.1016/S0370-2693(01)00184-8, arXiv:hep-th/0101163; *Dynamical algebra and Dirac quantum modes in the Taub–NUT background*, Class. Quantum Grav. **18** (2001) 3383, DOI 10.1088/0264-9381/18/17/304. Kazuki Hasebe, *Super Landau model and Howe duality: From supermonopole harmonics to quantum matrix geometry*, Phys. Rev. D **114** (2026) 085006, DOI 10.1103/lvq2-k6x8, Sec. VI C, eqs. (6.14)–(6.19).

## Gate 163 — source-faithful KY/Dirac symmetries preserve Taub–NUT fiber momentum

The established Cotăescu–Visinescu construction is for the four-dimensional **Euclidean self-dual** Taub–NUT Dirac system with a fourth Kaluza–Klein circle generator P₄=−i∂_ψ. Its Dirac operator, Killing–Yano tensors and derived Runge–Lenz operators are constructed from the fiber-translation-invariant geometric data. On any patch where these tensorial data and the spin frame are invariant in ψ, the corresponding covariant differential operators Q obey **[P₄,Q]=0**. Explicitly, [∂_ψ,f(x)]=0 and [∂_ψ,∂ᵢ−aᵢ(x)∂_ψ]=0; compositions preserve the commutator. Consequently Q maps the P₄=k sector into itself. The source papers establish the supercharges' Dirac/Hamiltonian symmetry; the stated extra fiber-commutator is a direct derivation using their fiber-independent construction, **not** an equation claimed to have been quoted verbatim from them.

Thus the ordinary Euclidean Taub–NUT Killing–Yano supersymmetry is different from Hasebe's right-acting UOSp(1|2) fermionic *monopole-charge-changing* ladder. Hasebe's charge changes Δg=1/2 while preserving its superspin ℓ, on an explicitly larger super-Hilbert space. Their different meanings of “supercharge” cannot be silently identified.

## Gate 164 — an explicit local fiber phase shifts k, but is not a global scalar intertwiner

For a **local** 2π-periodic fiber angle ψ, define W_loc=e^{iψ}. Then **[P₄,W_loc]=W_loc** exactly and W_loc sends Fourier mode k→k+1. However, the Taub–NUT/monopole fiber is nontrivially patched. The angular charge-k line bundle has north/south transition e^{ikφ}; a map B_k:L_k→L_{k+1} must patch with an extra e^{iφ} factor, i.e. is a section of Hom(L_k,L_{k+1})≅L₁. Since c₁(L₁)=1, no everywhere-nonzero *scalar zeroth-order* global bundle map exists. This does not exclude maps with zeros, sections tensored with spinor bundles, nontrivial differential intertwiners, or a different physical geometry. Merely writing e^{iψ} in a local chart does not construct any of those globally.

## Gate 165 — charge shifting is not a conserved TN time-fiber symmetry

The original Lorentzian Misner-periodic (rather than Euclidean KK) argument of v14.731 yields, for fixed l, E_k=ℏ c k/(4l), with the usual caveat about periodic Lorentzian time and closed timelike curves. Any k→k+1 shift must change energy by **ΔE=ℏ c/(4l)** and therefore obey [H,B]=ΔE B in the formal energy-mode tower, not [H,B]=0. This cannot be the same kind of conserved symmetry as an invariant KY/Runge–Lenz operator. **The relation is a necessary spectrally defined algebraic test, not evidence that such a global B exists.** Euclidean KK momentum P₄ is not automatically identical to Lorentzian energy H; the two analytic continuations should not be conflated.

## Gate 166 — exact obstacle inventory

A meaningful transfer of Hasebe's fermionic Δg=1/2 ladder into Taub–NUT requires jointly: (a) a globally defined map L_k→L_{k+1} with nontrivial degree-one patch transformation; (b) a representation carrying the required spinorial/graded transformation, since adjacent monopole sectors have opposite central SU(2) signs; (c) a dynamics compatible with k-changing rather than conserving fiber translation; and (d) a sourced normalization of this interaction. The existing Taub–NUT KY operators satisfy none of these k-changing requirements by themselves; they preserve the charge. This is a **scoped negative for the standard invariant KY/Dirac constructions**, not a general nonexistence theorem for all TN spinor supercharge extensions.

The **gravitational pair** step Δp=1/4 from v14.731 and Hasebe's Δg=1/2 match under the *conditional* dictionary g=s_TN=2p. But matching the charge lattice does **not** identify the geometric quarter-shell Casimir j_geom=k/4 with physical monopole angular spin j_phys≥|k|/2; at k=1 these are C_geom=5/16 versus C_phys=3/4. The original observation survives; the desired angular/gravitational observable remains open.

## Verification and audit handoff

**Reproducer:** `research-notes/taub_nut_ky_charge_gate_v15_647.py`, commit 5e2b109f03b6aa143bbcdfdc66ee852f5a1e1976, executed locally and passed. Checks the exact covariant local fiber derivative commutator, [P₄,e^{iψ}], unit patch winding L_k→L_{k+1}, and fixed-l energy spacing. The global topological statement follows from c₁ and not from finite matrices.

**HANDOFF:** target external-audit, gravity, sandbox. Independently read cited 2001 Dirac/KY papers, verify fiber invariance and track frame-gauge subtleties; check that the supersphere supercharge's role in Hasebe is **not** mistaken for TN KY supersymmetry; verify charge-bundle twisting and Euclidean vs Lorentzian distinction. Record any counterexample of a **published genuinely charge-changing** TN operator, with its global patching and [P₄,B]. No changes to frozen Suzuki certificates.

**Next gate:** investigate globally defined spinor-valued intertwiners `Hom(L_k,L_{k+1})⊗Spinor`, using the actual Dirac monopole and spin-weighted harmonics; check bundle topology and index/zero-mode selection, and ask whether their spectrum fixes a physical charge-changing operator rather than merely permitting one.
