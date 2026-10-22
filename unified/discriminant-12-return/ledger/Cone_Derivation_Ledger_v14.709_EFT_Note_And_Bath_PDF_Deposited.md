# Cone Derivation Ledger v14.709 — Jeremy-directed deposits: Kepler_EFT_Note.tex and Bath_Note.pdf into the D12 repo; results record for the EFT note (moment map, Lie–Poisson bracket, KKS sector)

**Timestamp:** 2026-10-22 (EDT)
**Lane:** Cross-lane record (deposits by the sandbox on Jeremy's explicit line: "read it and deposite it, also there is a Bath_Note.pdf," 2026-10-22).
**Parents:** v14.707 (Bath_Note.tex + EFT v3.4 deposited; Bath Note results record). **v14.708** (gravity lane: exact bath/phase coordinate gate) landed while these deposits were being made; it takes v14.705–707 as parents and its arithmetic was spot-verified by the sandbox at this entry's preparation (ρ² at the bath point = 5 − 2√6; Gram witness (4√6−8)/3 = 0.599319657044237; the ρ = q confusion would give 4/9). v14.708's sandbox handoff — derive the hot-limit drift coefficients from the EFT v3.4 collision operator, no hand-fit fixed point, test whether any independently derived interaction alters the Ξ response — is **acknowledged and taken** by the sandbox (disposition at the end).

## 1. The deposits

- **`research-notes/Kepler_EFT_Note.tex`** — *Fast Phase, Slow Moment Map: An Effective-Field-Theory Reading of the Kepler–Oscillator Correspondence on the AM–GM Cone* (Jeremy Ebert, 2026). Deposited as-is, unedited, from the workspace copy (`explorations/kepler-eft/`): SHA-256 `782177be1c5ea6c5095ce8ec4495d363ab7e440a9dc618666cd43db1da9ab4c6`, commit `f9c0ba8`, fetch-back verified.
- **`research-notes/Bath_Note.pdf`** — the compiled companion of the Bath Note deposited in v14.707. Byte-identical copy of `unified/Bath_Note.pdf`: SHA-256 `2992973ed023667e416950a385b350a3cfb96f1d688c28e3b7b1096d8cd80c43` at both locations, fetch-back verified. The `unified/` originals remain in place (deposits, not moves).
- Observed but **not** deposited (not named in Jeremy's instruction): `unified/Bath_Note_Velocity_Addendum.tex` and `.pdf` — a velocity addendum to the Bath Note, present in the repo's `unified/` since the same era. Deposit on Jeremy's word.

## 2. Results record — the EFT note

Read in full by the sandbox at deposit. Claim types follow the note's own Scope section, which separates its claims with unusual care; the sandbox's record preserves that separation.

**New and verified in the note [D].** The explicit moment map μ: (u,u′) ↦ (K₀,K₁,K₂) built directly from the Levi-Civita position spinor and its fictitious-time derivative — K₀ = ½(|u|² + |u′|²/ω²), K₁ = −½Re(A₊A₋), K₂ = Im(ūu′)/ω — equals **(T, X, Y) identically**, whence K₀² = K₁² + K₂² exactly: the image lies on the null cone. (Verification as reported in the note: symbolic substitution returning exactly 0 for each of K₀−T, K₁−X, K₂−Y and the cone combination.) The **Lie–Poisson bracket** {X,Y} = T, {Y,T} = −X, {T,X} = −Y on so(2,1)*, with the Casimir Q = X²+Y²−T² annihilated by all three brackets (the note's sign-consistency check). And the identification, via the cone paper's transitivity corollary restated in coadjoint language: **the null cone minus its vertex is a single KKS coadjoint orbit**, and every physical Kepler shape lies on this one degenerate leaf — the Kepler shape sector *is* the KKS sector of so(2,1)*, not an arbitrary leaf.

**Organizing observation [I — the note's own label].** Reading the dynamic slicing operator's per-revolution averaging remark as the EFT step of *integrating out the fast phase* θ = E/2, leaving an effective slow generator on the KKS sector. The note is explicit: the averaged coefficients are not computed and the averaged flow is not verified against the true one — an organizing observation and a motivation for a genuine averaging calculation, not a substitute for one. The reconstruction (fast phase + slow shape jointly sufficient, ζ = u²) is a re-derivation of the Levi-Civita note's closed form.

**Explicitly not established (the note's own flags, carried).** A genuine symplectic moment-map property for μ in Souriau's sense — that a specific symplectic form on (u,u′) ∈ ℂ² pushes forward to the bracket — is asserted only by analogy with the Bacry–Ruegg–Souriau / Moser / Kustaanheimo–Stiefel literature, which uses canonical momenta rather than u′; whether u′ is proportional to the canonical momentum with the constant the bracket (4.1) needs is **open**. No slow-sector effective Lagrangian/Hamiltonian (Wess–Zumino-type term from the KKS potential) is constructed. The note also discloses its LaTeX was never compiled in its drafting environment.

## 3. Corpus state after this entry

The bath/EFT corpus in the D12 tree is now complete as it exists: `Bath_Note.tex` + `Bath_Note.pdf` (T-relaxation), `Kepler_EFT_Note.tex` (the fast/slow EFT frame), the EFT v3.4 draft (Maxwellian shape dynamics), and the v14.705 expansion payload (cone dictionary, ray fixed point, G lever). The two remaining `unified/` items (Velocity Addendum pair) await Jeremy's word.

## Scope flags (honest)

`deposits_on_jeremy_line = true`; `answers_lane_a_handoff = false`; `far_tail_touched = false`; `documents_edited = false (byte-identical deposits)`; `G_derived = false`; `v14_708_sandbox_handoff = TAKEN (drift-coefficient derivation from the v3.4 collision operator)`.

## Disposition

Deposits closed. Open sandbox work after this entry: the v14.708 handoff (drift coefficients from the collision operator; Ξ-alteration test), and the far gate (v14.585 actions 3–4, assembly running).
