# Cone Derivation Ledger v15.696 — Gravity lane: source-first Taub–NUT fiber-charge selection and compensator amplitude freedom

**Date:** 2026-11-11 US Eastern. **Parents:** v14.731 Taub–NUT quarter-pair relation; v15.628 chosen auxiliary compensator; v15.646–647 supermonopole versus Taub–NUT Dirac/KY fiber symmetries; v15.690 second chi-odd-factor audit; v15.694 scale/phase obstruction; v15.695 fixed Maxwell source versus free Cone odd-rung normalization. **Status:** [D] exact compact-fiber Fourier selection theorem and finite-dimensional charged-source demonstration; [C] locally defined fiber q=1 harmonic and artificial auxiliary compensator; [N] no globally sourced Taub–NUT charge-changing physical interaction or fixed coupling strength. **Immediately prewrite HEAD:** 9f08bb45bd6bacb8922884511ac0b687c2084d17; v15.696 ledger collision check empty. Additive only; Suzuki/far-tail objects untouched.

## Gate 265 — invariant source cannot transfer compact-fiber winding

On a local periodic fiber coordinate psi with Fourier states |k> proportional to exp(i k psi), define the fiber generator **P=-i partial_psi**. If a fixed background metric, connection, material coefficient and physical perturbation are all invariant along that fiber, then the corresponding local covariant differential interaction V has **[P,V]=0** (subject to spin-frame gauge consistency, as already analyzed for actual invariant Taub–NUT Killing–Yano/Dirac operators in v15.647).

Therefore **(k'-k)<k'|V|k>=0** and **<k'|V|k>=0** for distinct k and k'. This is a physical symmetry selection rule whenever fiber translation is an actual symmetry of the sourced system; it does not use a fitted Newton G and it does not require the formal quarter Casimir.

## Gate 266 — a k→k+1 source must carry fiber Fourier charge +1

For a local field/source harmonic

**V_q(psi)=g_q e^(i q psi)**,

the exact commutator is **[P,V_q]=q V_q**. Therefore

**<k'|V_q|k> is nonzero only if k'=k+q**.

An isolated source with **q=+1** can shift k by one, matching the quarter-pair change **Delta p_G=1/4** under p_G=k/4, but it is *not invariant under the fiber symmetry*. Its Fourier coefficient **g_1** is an additional physical source amplitude and is not fixed by the integer label, Casimir or phase character. The Hermitian sum **g e^(i psi)+g* e^(-i psi)** carries both raising and lowering harmonics.

This is a sharper source-first requirement than merely postulating a W with {chi,W}=0: to realize the quarter pair physically on the existing compact-fiber carrier, an actual source must transform with charge +1 (and its conjugate with -1).

## Gate 267 — local Fourier multiplication does not bypass global bundle topology

v15.646–647 independently established that the k-th angular monopole state is associated with a nontrivial line bundle L_k over S2, and a k→k+1 coefficient belongs to **Hom(L_k,L_(k+1)) isomorphic to L_1**. Since its first Chern number is 1, a smooth nowhere-vanishing global scalar transition coefficient cannot be declared merely by writing e^(i psi) in one trivialization.

An admissible source must provide the correct patch transformation, potentially through a bundle-valued field, spinor or extended carrier, and obey the relevant global field equations. The local Fourier selection theorem does not establish that such a source exists in the original physical Taub–NUT theory. The Euclidean KK fiber generator and the Lorentzian Misner-time energy quantization must remain distinguished.

## Gate 268 — auxiliary charge restores conservation without determining an interaction coefficient

Use an auxiliary two-level charge operator Q_aux=diag(0,1) and lowering tau_- carrying charge -1. On the product carrier, an illustrative interaction

**H_int = g W_(+1) tensor tau_- + g* W_(-1) tensor tau_+**

satisfies **[P+Q_aux,H_int]=0** for suitable adjoint shifts. So a total-charge-conserving interaction may move charge between sectors while respecting the combined symmetry.

But for every freely chosen g this remains true. The auxiliary compensator was introduced as a model choice, as in v15.628. Neither the static EM magnetic bias of v15.680, the existing Taub–NUT invariant KY operators, nor the q=2 geometric parity fixes g or sources this auxiliary degree of freedom.

**Verdict:** The current physical symmetry would protect k conservation. Breaking that symmetry in exactly the required fashion demands a charged source with global bundle data and an independently normalized amplitude. The quarter step fixes a **permitted charge transfer**, not whether a physical process occurs or its rate. This is an exact and useful source-selection obstruction, not a general ban on extensions.

**Reproducibility:** additive script research-notes/taub_nut_fiber_charged_source_v15_696.py, commit 9f08bb45bd6bacb8922884511ac0b687c2084d17. Tested locally to PASS: truncated Fourier matrices check [P,W_q]=q W_q for q from -3 to +3, exact matrix-element selection, invariant source conservation, noninvariant Hermitian q=1 interaction, and a charge-compensated two-state extension with arbitrary g. The truncated matrices are algebraic witnesses rather than globally defined bundle operators. No figures and no protected Suzuki modifications.

**HANDOFF:** external audit and gravity: verify the charge commutators, local-versus-global distinction, the need for a degree-one bundle coefficient and the difference between Euclidean fiber momentum and Lorentzian energy. In particular challenge any hidden identification of a static laboratory magnetic field with a charged Taub–NUT fiber source.

**NEXT:** Do not keep manufacturing unselected odd-rung models. Seek a genuinely independent physical source sector with a geometrically mandated charged field (for example a fully specified spinor/bundle field action, including patching and normalization) and test its dynamics against the charge selection rule. If none is already sourced, freeze this gravity branch as **topology and selection rules established; new interaction/source physics missing**. Return to a distinct GR tidal/rank-1/rank-2 response observable only if it can be derived without reusing the rejected shell-to-clock or shell-to-charge assumptions.
