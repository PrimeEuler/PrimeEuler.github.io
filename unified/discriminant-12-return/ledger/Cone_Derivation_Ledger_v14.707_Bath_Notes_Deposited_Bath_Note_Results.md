# Cone Derivation Ledger v14.707 — Jeremy-directed deposit: both bath notes now resident in the D12 repo; results record for *The Cone in a Bath* (T-relaxation: exact Lindblad laws, the Itô/Jensen term, plasma cancellation)

**Timestamp:** 2026-10-22 (EDT)
**Lane:** Cross-lane record (deposits made by the sandbox on Jeremy's explicit line: "I want both the bath note and the EFT in our D12 repo up from the unified dir," 2026-10-22).
**Parents:** v14.705 (the expanded bath-note results — the EFT expansion), v14.706 (provenance erratum: the bath-note corpus has two members). Collision check at deposit: live HEAD v14.706, v14.707 next-free.

## 1. The deposits

- **`research-notes/Bath_Note.tex`** — *The Cone in a Bath: Boson, Gravitational, and Plasma Relaxation of the Semi-Major Axis* (Jeremy Ebert, 2026). Byte-identical copy of the repo-resident `unified/Bath_Note.tex` (2026-08-26, commit `faec0d2`): SHA-256 `cd61d8c006b4aa3456abdd98241d5788f728f9f166ba72179b61f04b5cd5ce0c` at both locations, deposit commit `6969fd0`, fetch-back verified. The `unified/` original is **left in place** — this is a deposit into the D12 tree, not a move; removing the original is Jeremy's separate call.
- **`research-notes/Kepler_Cone_Revised_EFT_Draft_v3_4_Elevated_Hot_Benchmark.tex`** — the EFT draft v3.4, direct parent of the v14.705 expansion, previously Mac-local with its only copy in the sandbox workspace (`explorations/kepler-eft/`). SHA-256 `1355fdf576b2093e7130b4ada32ebee3a3919872b482d0f928b57389af4aff84`, deposit commit `a907017`, fetch-back verified. Deposited as-is, unedited.

## 2. Results record — *The Cone in a Bath*

Claim types: **[D]** the note's theorems/propositions as stated (proofs in the note); **[N-reported]** the note's own numerical verifications, as documented in the note (including its AI-assistance disclosure) — the note's producers are not in this workspace and were **not** re-run by the sandbox; the sandbox's verification at deposit is documentary (full read) plus the byte-identity above.

**Boson bath.** Thm 2.1 [D]: under independent two-mode Lindblad coupling at mean occupation n̄, the cone coordinates relax *exactly linearly*: Ṫ = −κ(T − n̄ − ½), Ẋ = −κ(X − ½), with T_eq = n̄ + ½. Prop 2.2 [D]: ⟨Y²⟩_ss = n̄(n̄+1), and the cone identity survives exactly at moment level, ⟨X⟩² + ⟨Y²⟩_ss = ⟨T⟩². [N-reported]: truncated Fock-space checks — ⟨n(t)⟩ to 1.9×10⁻³ over t∈[0,8]; ⟨Y²⟩ = 7.58999987 vs 7.59 at n̄ = 2.3; identity residual −1.8×10⁻¹⁵. Open in the note, carried as open: no transient equation for ⟨Y²(t)⟩ for arbitrary (non-Gaussian) initial states.

**Gravitational bath.** Thm 3.1 [D]: for a Langevin velocity process with drift **A** and diffusion D, Itô's lemma applied twice (h, then T = −μ/2h) gives ⟨Ṫ⟩ = (2T²/μ)(**v**·**A** + TrD) + (8T³/μ²)**v**ᵀD**v** — both correction terms always ≥ 0 for physical D. The second term is the convexity/Jensen term: T is a convex (reciprocal) function of the exchanged energy. [N-reported, the note's Table 1]: 20,000-trajectory ensemble — MC 25105.51 ± 30.25; formula without the Itô term 24494.04 (**20.2σ off**, always hot); corrected formula 25108.10 (**0.09σ**). The note records the initial error and its diagnosis deliberately, as method. Scope as stated in the note: toy/state-independent D for the check; Chandrasekhar's velocity-dependent **A**, D **not** substituted; no global-equilibrium claim for self-gravitating systems.

**Plasma bath.** Prop 4.1 [D]: TrD = 8πκ_int² n_f lnΛ/(m_t² u), derived from individual Rutherford encounters at leading log. Prop 4.2 [D]: the friction drift (eq. 5) from the same encounters, with the exact ratio (eq. 6) → −1/u at equal masses. Corollary [D]: for equal test/field masses in the monoenergetic shell model, friction and diffusion cancel **exactly** in ⟨Ṫ⟩, isolating the pure heating term ⟨Ṫ⟩ = (8T³/μ²)**v**ᵀD**v** ≥ 0. [N-reported]: 3×10⁶ encounter windows — TrD_MC = 2.241 ± 0.002 vs 2.458 analytic, friction −1.120 ± 0.001 vs −1.229 (both 9% gaps, the expected leading-log accuracy at lnΛ ≈ 3.91); the note records its own two catches en route (a b_min cutoff error, factor 2.3; a mis-simplified power of u, factor 2). Open in the note, carried as open: the Maxwellian average of (4)–(6) is **not** done — the cancellation is a shell-model feature, not a general plasma result.

**The one-sidedness [D, the note's §5].** The Itô correction appears only classically, structurally: on the quantum side T is *linear* in the quantity the bath exchanges (boson number N = n₁+n₂); classically T is a *reciprocal* function of the exchanged energy h. Itô terms live exactly where the coordinate is a nonlinear function of the additively-diffusing variable.

## 3. Relation to the rest of the corpus

The two bath notes divide the relaxation problem by coordinate: *The Cone in a Bath* treats **T** (the semi-major-axis coordinate) under boson, gravitational, and plasma baths; the **EFT v3.4** treats the **shape** coordinate (eccentricity, via q) under a Maxwellian bath — the note whose hot-bath fixed point the sandbox expanded into the cone ray pair and the G lever (v14.705). Both are now resident in the D12 tree with the expansion, closing the provenance gap corrected in v14.706.

## Scope flags (honest)

`deposits_on_jeremy_line = true`; `answers_lane_a_handoff = false`; `far_tail_touched = false`; `papers_modified = false`; `documents_edited = false (byte-identical deposits)`; `bath_note_verifications = AS_REPORTED_IN_THE_NOTE (producers not in workspace, not re-run)`; `G_derived = false`; `unified_original_removed = false`.
