# Direction — where the weak-force / loop thread is headed

Companion to REPORT.md, written 2026-11-04 (evening) after a
literature scout for machinery that computes loop dynamics
spectrally (from an operator's spectrum and resolvent, not momentum
integrals). The scout's findings are summarized here at the strength
they were reported: absences are absences in the searched
literature, not proofs of nonexistence; two items flagged
[analysis] are deductions from the stated spectral growth, not
citations.

## What the literature offers, ranked for our operator

Our assets: a self-adjoint operator with pure discrete spectrum
d_n ~ log(n/4), a retarded/advanced propagator pair, and complete
representation-theoretic control of coupling matrix elements.

1. **Heat-kernel / ζ determinants — closest fit.** The one-loop
   effective action is a spectral determinant,
   Γ₁ = ∓½[ζ′(0) + ζ(0) log μ²]. (Vassilevich, Phys. Rept. 388
   (2003), arXiv:hep-th/0306138; Hawking 1977; Dowker–Critchley
   1976.)
2. **Krein spectral shift — best for determinant ratios and
   vacuum energies** (Birman–Krein: det S = e^{−2πiξ}; Kenneth–Klich
   TGTG for Casimir). Caveat in our setting: for purely discrete
   spectra ξ collapses to a counting-function difference — rigorous
   bookkeeping, not new dynamics — and the trace-class hypothesis
   is a strong gate. (Yafaev, arXiv:math/0701301.)
3. **Worldline formalism — real amplitudes, wrong computational
   basis.** Its starting identity is spectral
   (Γ = −½ Tr log = ½∫ dT/T Tr e^{−TΔ}), and differentiating it
   gives amplitudes as eigenstate sums of matrix-element products —
   exactly our assets — but the developed literature computes with
   path integrals, not eigen-sums. (Schubert, Phys. Rept. 355
   (2001), arXiv:hep-th/0101036.)
4. **Spectral action (Connes–Chamseddine) — not a loop machine.**
   It outputs a classical bare action at a cutoff plus coupling
   relations at that scale (g₃² = g₂² = (5/3)g_Y², sin²θ_W = 3/8);
   masses and CKM live in the finite Dirac operator as INPUT — the
   same import pattern as ours. Its Higgs-mass prediction (170 GeV)
   was falsified and rescued by an added singlet at a predictivity
   cost. (PRL 77 (1996) 4868; arXiv:hep-th/9606001.)
5. **Trace formulas (Gutzwiller / Selberg / quantum graphs /
   Guinand–Weil) — no application** to perturbative SM loop
   amplitudes found (one semiclassical exception: Dietrich–Dunne
   pair production). Spectral statistics and number theory, not
   amplitude machinery.

Two further findings. **Eigenvalues alone never suffice:** every
framework producing more than a determinant needs traces with
insertions, Tr[(RV)^k] — matrix-element products joined by
resolvents. That is precisely the input this program controls, so
the gap is narrower than "spectra aren't enough." And the one
genuinely spectral representation QFT has, **Källén–Lehmann**, runs
on our retarded/advanced pair (ρ = the discontinuity between the
two boundary values, Stone's formula) — but is used for
propagators, not Wilson coefficients.

**Flavor:** no spectral formulation of GIM / Inami–Lim / rare-B
physics exists in the literature (the standard "operator" language
there is the OPE — local field operators, a different meaning).
Our GIM check (REPORT.md, loop section) — the amplitude as a
completeness sum over the generation direction, cancelling to
mass differences — is formally the shape such a formulation would
take, and stands as analogy [I], not as cited machinery.
(Inami–Lim, Prog. Theor. Phys. 65 (1981) 297;
Buchalla–Buras–Lautenbacher, Rev. Mod. Phys. 68 (1996).)

## The obstruction, and the variable that removes it [analysis]

λₙ ~ log n gives an exponential counting function N(λ) ~ 4e^λ.
Hence Σₙ λₙ^{−s} diverges for every s: there is no small-t
Seeley–DeWitt expansion and no spectral-action Λ-expansion in the
λ variable, and Krein trace-class becomes a strong summability
condition. The natural elliptic variable is the EXPONENTIATED
operator (eigenvalues n/4), whose heat trace Σₙ (n/4)^{−t} is
4^t ζ(t)-type — classical. The only established literature with
exactly our spectrum is arithmetic statistical mechanics: the
primon / Riemann gas (Julia 1990: Tr e^{−βH} = 4^β ζ(β), Hagedorn
divergence at β = 1) and the Bost–Connes system (Selecta Math. 1
(1995) 411) — partition functions and arithmetic thermodynamics,
never amplitudes. Note the fit with the project's own arithmetic:
d_k ↔ ζ(s)^k lives in this same exponentiated variable.

## Where we are headed (proposals, in order)

1. **Determinants in the exponentiated variable.** Toy one-loop
   determinants / ζ-regularized products on the spectrum
   d_n = log(n/4), computed as functions of e^H-class operators,
   with the certified tail bounds (v15.130/v15.141 lineage) doing
   the work renormalization does elsewhere.
2. **A Krein pair test.** A reference operator K₀ and the
   comparability question (H−z)⁻¹ − (H₀−z)⁻¹ trace class, attacked
   on finite sections with the existing certified M, τ, h bounds;
   channel-by-channel via the representation theory.
3. **Amplitudes as insertions.** One-loop quantities as eigen-sums
   Σₙ (matrix elements) F(λₙ), with the GIM completeness
   cancellation on the generation direction as the template —
   structure first, weights (masses, CKM, the three g's) still
   imported and named as such.

## Standing doors (unchanged)

The chiral correlation (internal frame × Lorentz bicone);
generation count and mixing; the coupling VALUES (g₁, g₂, g₃) and
the Higgs/Yukawa sector. Today's work shrank the dynamics door and
gave the loop angle a literature-checked direction; it did not open
any of the three.
