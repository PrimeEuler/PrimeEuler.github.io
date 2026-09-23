# Cone Derivation Ledger v13.738 — External Audit Round 87

Date: 2026-09-23

Auditor: independent external LLM session (Claude Sonnet 5), auditing via shared git ledger only. No private channel with the source thread exists; coordination is solely through commit history.

Scope: (1) resolve a genuine 5-way version-number collision spanning v13.732–v13.735 across two independent commit streams; (2) independently verify the mathematical content of all five affected entries; (3) directly check, against the archived Suzuki PDF, the specific formula the user asked this auditor to confirm.

## 1. Collision found and resolved

At the start of this round, six entries existed under conflicting labels v13.732–v13.735:

| Original label | Title | Commit | UTC timestamp |
|---|---|---|---|
| v13.732 | External Audit Round 86 (this auditor) | `1c080f3` | 2026-09-23T19:45:37Z |
| v13.732 | Exact Compensated Edge Wiener–Hopf Equation | `6430c33` | 2026-09-23T19:45:49Z |
| v13.733 | Weil Explicit-Formula Normalization Match | `3a61481` | 2026-09-23T19:54:54Z |
| v13.733 | Screw-Symbol Extraction and Xi/Theta Transfer Obstruction | `59b4762` | 2026-09-23T20:22:30Z |
| v13.734 | Norm-Quotient Information Loss | `ccf4c20` | 2026-09-23T20:27:33Z |
| v13.735 | Analytic Screw Current, Paired Channel, Xi/E Gate | `8d9b3a0` | 2026-09-23T21:40:35Z |

Per the standing UTC-commit-timestamp protocol, ordering by absolute commit time and renumbering later entries to remove collisions gives:

- v13.732 — External Audit Round 86 (unchanged; earliest commit)
- v13.733 — Exact Compensated Edge Wiener–Hopf Equation (was v13.732)
- v13.734 — Weil Explicit-Formula Normalization Match (was v13.733)
- v13.735 — Screw-Symbol Extraction and Xi/Theta Transfer Obstruction (was v13.733)
- v13.736 — Norm-Quotient Information Loss (was v13.734)
- v13.737 — Analytic Screw Current, Paired Channel, Xi/E Gate (was v13.735)

Each renumbered file received a "Renumbering note" documenting its original label, commit hash, and timestamp, with no mathematical content altered. Internal cross-references that named a colliding file by its old number were located and corrected:

- Screw-Symbol Extraction §2/§5 referred to "the v13.732 formal symbol" / "v13.732 wrote formally" (meaning the Wiener–Hopf entry) — corrected to v13.733.
- Norm-Quotient Information Loss's header ("Parents: v13.731, v13.733") and body (§5, the diagram in §8) referred to the Weil-normalization entry as "v13.733" — corrected to v13.734.
- Analytic Screw Current/Paired Channel's synchronization line referred to its predecessor as "v13.734" — annotated to note that entry is now v13.736.

A repo-wide search confirmed no other file (index pages, cross-referencing entries outside this collision batch) cites any of the old, now-vacated numbers.

A final `git fetch origin master` immediately before this write confirmed the local HEAD (`8d9b3a0`) matches `origin/master` exactly — no further commits landed during this renumbering.

## 2. Independent mathematical verification

All five non-audit entries in the collision batch were independently re-derived by hand; no errors were found in any of them.

**v13.733, Exact Compensated Edge Wiener–Hopf Equation.** Re-derived the distributional extension `(h_+)'' = -q_+ + Q_+(0)δ_0` from `h_+= H·h`, `h(0)=0`, `h''=-q` by hand (product-rule differentiation of a function extended by zero, picking up exactly one boundary delta from the jump in `h'` at 0, since `h` itself is continuous there). Confirmed the Fourier transform `ĥ_+(k) = (Q_+(k)-Q_+(0))/k^2` follows from `-k^2ĥ_+(k) = -Q_+(k)+Q_+(0)`. Verified the pole-free form and the rank-one moment argument `M=Q_+(0)` algebraically. No errors.

**v13.734, Weil Explicit-Formula Normalization Match.** Re-derived `ĥ(1/2+it)=ĝ(t)` from the centering substitution `h(e^r)=e^{-r/2}g(r)` by direct substitution into the Mellin integral. Verified the finite-place `n^{-1/2}` half-density algebraically (it is exactly the value of `e^{-r/2}` at `r=log n`, symmetrized). Verified the pole-term identities `ĥ(0)=ĝ(i/2)`, `ĥ(1)=ĝ(-i/2)` by substituting `s=0` and `s=1` respectively into `s=1/2+it`. Verified the archimedean digamma multiplier via `L_∞'/L_∞(s) = -½log π + ½ψ(s/2)` at `s=1/2+it`. No errors.

**v13.735, Screw-Symbol Extraction.** Re-verified `𝓕[-g''](k)=k²ĝ(k)` from the standard distributional-differentiation Fourier identity under the stated convention. Cross-checked every cited Suzuki formula word-for-word against the archived PDF `research-notes/2606.09096v2.pdf`: equation (1.3) defining `g(t)` (page 4), the Section 2.2 constant `A=½(log(2π)+C₀-1)` (page 8), the Section 2.4 Fourier-side formulas for `r̂₁''(z)` and the quadratic-form multiplier (pages 10–12), and — most directly relevant to the user's specific question this round — the Section 2.5 distributional formula
\[
-g''(t)= -\tfrac12\,{\rm Pf}\tfrac1{|t|} -(2A+1)\delta_0 -\sum_{n\ge2}\tfrac{\Lambda(n)}{\sqrt n} [\delta(t-\log n)+\delta(t+\log n)] -r''(t)
\]
(pages 12–13). **This is confirmed verbatim-accurate against the source.** It decomposes exactly as claimed into a finite-part logarithmic singularity, a local delta, the symmetric prime-power delta train, and the archimedean remainder — and it is, as the user observed, structurally the same prime/archimedean logarithmic current independently isolated in the cone lane via `ξ'/ξ(s)-ξ'/ξ(2) = ∫(e^{-sr}-e^{-2r})dν_ξ(r)`. No errors in the citation or in the surrounding derivation (the correction that the raw symbol is distribution-valued, not an ordinary scalar Wiener–Hopf symbol, was independently re-checked and is correct).

**v13.736, Norm-Quotient Information Loss.** Independently re-derived the exact sequence `1→C_ℚ¹→C_ℚ→ℝ_{>0}×→1` (surjectivity of the adelic norm via the real place; `C_ℚ¹` well-defined as its kernel by the product formula on `ℚ×`) and the resulting isomorphism `C_ℚ/C_ℚ¹≅ℝ_{>0}×` by the first isomorphism theorem. Verified the local claim `ℚ_p×/ℤ_p× ≅ ℤ` via the standard valuation splitting `ℚ_p× ≅ p^ℤ×ℤ_p×`. Verified the character-level claim (a quasicharacter `χ(u)|u|^s` descends to the norm quotient exactly when `χ` is trivial on `C_ℚ¹`) as definitional/standard. The three-level status distinction (group-level quotient: proven; trivial-character projection: proven; v13.731 Hilbert-space realization: correctly NOT claimed as a proven quotient representation) is logically sound and appropriately hedged. No errors.

**v13.737, Analytic Screw Current, Paired Deficiency Channel, and Xi/E Gate.** Independently re-derived every algebraic step by hand:
- `L(s)=-L(1-s)` from `ξ(s)=ξ(1-s)` by differentiating both sides;
- the odd/even parity split `ℓ(-w)=-ℓ(w)`, `Ξ(-w)=Ξ(w)`, and `ℓ(w)=Ξ'(w)/Ξ(w)`, all confirmed by direct substitution `s=1/2+w`;
- the log-derivative identity `T_pair'/T_pair(z) = -iL(1/2-iz) - E'/E(z)`, re-derived by differentiating `log[Ξ(-iz)/E(z)]` and confirmed to match the boxed claim exactly;
- the algebraic identity `R(z)=E(z)T_pair(z)/Ξ(-iz)=C_ξ` and `d/dz log R(z)=0`, confirmed as trivial consequences of the assumed target;
- the substitution `Ξ(-iz)=Φ̂(z)` using the v13.722 bilateral transform, giving `E(z)T_pair(z)=C_ξΦ̂(z)`, confirmed by direct substitution.

Most critically, the load-bearing citation — Suzuki's Section 7 identity `(z-i)f̂_{+i}(z)-(z+i)f̂_{-i}(z) = [2ξ'(3/2)/(π²i)]·ξ(1/2-iz)/E(z)`, on which the entire paired-channel argument (Gates 5–9) depends — was checked directly against the PDF. It appears verbatim on page 27 (Section 7.8), including the definition `E(z)=ξ(1/2-iz)+ξ'(1/2-iz)` used elsewhere in the same file. No errors. The entry's own hedging (Gates 4, 6, 10: explicitly not claiming an edge-limit theorem) is accurate — nothing here overclaims.

## 3. Answer to the user's specific question this round

The user directly quoted Suzuki's `-g''(t)` decomposition and asked for verification. That formula is confirmed **word-for-word accurate** against the archived source PDF (Section 2.5, pages 12–13), as detailed in §2 above under v13.735. The user's characterization — that this is "essentially the same prime–archimedean logarithmic current...independently found in the cone lane" — is also independently supported: the cone lane's own `ξ'/ξ(s)-ξ'/ξ(2)=∫(e^{-sr}-e^{-2r})dν_ξ(r)` (used explicitly in v13.735 §6 and again in v13.737 Gate 1 as `𝓒(s)=L(s)-L(2)`) and Suzuki's `-g''` decomposition are, as the source thread itself argues in v13.735 §6, the Laplace/Cauchy and Fourier realizations respectively of the same underlying explicit-formula data (prime atoms at `log n` with `Λ(n)/√n` weights, plus an archimedean/gamma remainder). This structural match was independently re-confirmed, not merely re-quoted from the ledger.

## 4. Result

\[
\boxed{\textbf{PASS: 5-way version collision fully resolved, cross-references corrected, no mathematical content altered.}}
\]
\[
\boxed{\textbf{PASS: all five audited entries (v13.733--737) independently verified, no errors found.}}
\]
\[
\boxed{\textbf{PASS: user-quoted Suzuki } -g''(t) \textbf{ formula confirmed verbatim-accurate against source PDF.}}
\]

No errors were found in the source thread's work this round. No errors were found in this auditor's own prior work this round (Round 86's self-correction, disclosed last round, stands; nothing new to retract).

## 5. Next gate

Per v13.737 Gate 10, the sharpest open target in the Suzuki edge lane is now the finite-to-infinite-volume convergence statement
\[
\mathcal R_A(z) = \frac{E(z)\mathcal T_{{\rm pair},A}(z)}{\Xi(-iz)} \xrightarrow{A\to\infty} C_\xi,
\]
which this auditor will watch for in subsequent rounds, along with the v13.736 "next discriminating gate" (constructing the trivial-`C_ℚ¹`-isotypic sector of a canonical idele-class representation).
