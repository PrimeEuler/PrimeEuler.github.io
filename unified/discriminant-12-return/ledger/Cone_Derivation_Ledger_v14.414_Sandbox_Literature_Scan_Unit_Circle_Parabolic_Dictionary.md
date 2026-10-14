# Cone Derivation Ledger v14.414 — Sandbox: Literature Scan of the Unit-Circle / Parabolic Dictionary Deposited

**Date:** 2026-10-14
**Track:** Sandbox (Jeremy's exploratory track — not ledger Lane B)
**Status:** [DEPOSIT, N] At Jeremy's direction, the full literature scan of the unit-circle encoding / hyperbolic cone dictionary (deposited v14.366, pair addendum v14.367) was run on 2026-10-14 and its report deposited in research-notes. This entry records the deposit and the scan's verdicts. No paper was edited; no claim is upgraded beyond what the scan supports.
**Parents:** v14.366, v14.367 (the dictionary and its pair generalization); v14.369 (audit of the deposit).

---

## Deposit

- File: `unified/discriminant-12-return/research-notes/Unit_Circle_Parabolic_Dictionary_Literature_Scan.md`
- Size: 24,583 bytes. SHA-256: `e067a6c694b31a10eaa8697b12c78fd73859fe5cf4d837edcd7cb4f6f0191787` (fetch-back byte-verified at push).
- Contents: per-component closest prior art with citations, explicit verdicts, coverage statement, and a "could not verify" section. The scan searched the general web index (~35 exact-formula and discriminator queries), arXiv, reference works, lecture notes, and journal PDFs.

## Verdicts [N]

The **assembled** construction — integer-indexed unit-circle stations z_n = ((n−1)+2i√n)/(n+1) with the AM/GM reading, the rapidity dictionary ψ_n = ½ ln n, the pair form z_{n,k} with additive rapidity chains, the parabolic-coordinate readout, the cone row/column table, and the seed contact log(m/4) = 2(ψ_m − ln 2) — was **not found** in any scholarly source in this scan.

| Component | Verdict |
|---|---|
| 1. z_n stations, AM/GM reading | Near-miss only — points are the classical rational parametrization at t = 1/√n; no source makes that substitution, indexes by n, or gives the AM/GM reading |
| 2. Rapidity dictionary ψ_n = ½ ln n | Near-miss only — see Gudermannian discrimination below |
| 3. Pair form, additive chains, (n+k)/(n−k) = coth ψ | Near-miss only — boost additivity (relativity) and the pair ratio (a−b)/(a+b) with cosh/sech parameters (Seiffert/Neuman–Sándor means literature, where ψ_{a,b} is used silently) exist separately; the fusion was not found |
| 4. Parabolic readout ψ = ½ ln(ξ/η); cone table | Near-miss only — the identical formulas exist only as pseudorapidity for momentum directions; no parabolic-coordinates source states the readout; the cone table was not found |
| 5. Seed contact log(m/4) = 2(ψ_m − ln 2) | Not found (a one-line corollary of component 2) |
| (d) Cone parabolas ↔ Suzuki screw function | Not found — Suzuki's screw function is the Krein–Langer positive-kernel notion; the screw-line literature explicitly separates itself from surface helices. The parabola-outlined screw overlay is the sandbox's own |
| (e) 32/81 in hydrogen dipole literature | Not found — the tabulated kernel is 128√2/243, which does not factor through 32/81 |

## Sharpest discrimination

The classical circle↔rapidity dictionary is the **Gudermannian**, and it is the dictionary's point **transposed**: the literature's point is sech ψ + i tanh ψ (angle gd ψ), while the deposited construction uses tanh ψ + i sech ψ (angle π/2 − gd ψ). This is why n = 3 gives the construction's 60° station while gd ψ₃ = 30°. No source found makes the swap, sets e^ψ = √n, or discretizes ψ by integers. Any future novelty claim must distinguish the Gudermannian (and pseudorapidity, and the means literature) explicitly — the scan report does so.

The only verbatim web hit for the scalar identity tanh(½ ln n) = (n−1)/(n+1) is a non-scholarly self-published GitHub commit (2026-03-15, "Cayley address"), with none of the circle/AM-GM/parabolic content; it is not a literature venue and is recorded here only so the claim is not overstated later.

## Coverage caveat [N]

The negative evidence is **moderate, not conclusive**. Not searched: MathSciNet, zbMath, Scopus/Web of Science, Google Books full text, non-English literatures. "Not found in this scan" must not be restated as "does not exist." Two source PDFs (Suzuki JLMS 108 (2023); arXiv:1603.00899) were corroborated via multiple index extracts rather than opened in full; this is flagged in the report's "could not verify" section.

## Scope

Deposit and record only. The encoding note's status is unchanged (Jeremy's formulation; paper placement remains his later call). No staged paper, ledger Lane A/B item, or evaluator code is affected by this entry.
