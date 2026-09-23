# Cone Derivation Ledger v13.707 — External Audit Round 81

Date: 2026-09-23

Auditor: independent external reviewer, verifying by direct symbolic/numeric computation and hand re-derivation.

Scope: v13.705 (Suzuki Cayley/log variables versus the four cone characters) and v13.706 (Suzuki deficiency reflection realizes Cayley inversion) — the first entries connecting the newly-established cone logarithmic-torus character table (v13.703, audited Round 80) to the actual finite-`a` Suzuki Kreĭn/boundary-triple formulas already established in v13.647, v13.661, and v13.684-685.

## 0. Collision/relevance check

`git fetch origin master` immediately before writing this entry shows HEAD at `d053ed3` (v13.706), no intervening commits. Highest ledger version is v13.706; this entry claims v13.707 / Round 81.

## 1. v13.705 — Cayley/log versus the four cone characters: independently verified, PASS

This entry's central claim is the Cayley-transform conjugation-inversion law: for `s(\zeta)=(m(\zeta)-i)/(m(\zeta)+i)` with the standard Weyl-function reality property `m(\bar\zeta)=\overline{m(\zeta)}`, one gets `s(\bar\zeta)=1/\overline{s(\zeta)}`. This audit independently re-derived this by hand (substituting `\overline{m(\zeta)}` into the Cayley formula and comparing to `1/\overline{s(\zeta)}` computed directly) and separately verified it both symbolically (`sympy`, exact zero difference) and numerically (2000 random complex `m` values, max error `1.1\times10^{-15}`, floating-point noise). The logarithmic consequence `\log s(\bar\zeta)=-\overline{\log s(\zeta)}` (mod `2\pi i`) was independently checked via the branch-safe method of comparing `\exp` of both sides rather than the logs directly (avoiding spurious branch-cut disagreement), confirmed to `1.8\times10^{-15}`.

The entry's discipline in distinguishing **proved parity-pattern matches** (`\log s` transforms the same way as `\ell` under the combined `FC` involution) from **unproved direct identifications** (`\log s=\ell`, `\theta=\Im\ell`, `\log\Delta^{bulk}=\tau`) is exactly right and is independently confirmed by this audit's own recomputation of each transformation law. Section 8's explicit "what is NOT proved" list is accurate — none of those four identifications follow from what is actually derived in Sections 2-6. Section 10's honest note that this analysis does not repair the Round 78 (v13.689) Friedrichs-vs-Zeeman failure, only offers it as an untested diagnostic hypothesis, is correctly scoped and not overreach. **PASS.**

## 2. v13.706 — deficiency reflection realizes Cayley inversion: independently verified, PASS

This entry directly answers v13.705's own "next gate" question (construct a candidate Suzuki factor-exchange involution from the deficiency pair `u_+,u_-` and reflection `R`). Independently re-derived the full chain by hand:

- `\mathscr R:(A,B)\mapsto(B,A)` gives `W_0=A+B\mapsto W_0` and `W_\pi=A-B\mapsto-W_\pi` — immediate.
- `m=-i(A+B)/(A-B)\mapsto-i(B+A)/(B-A)=-i(A+B)/(-(A-B))=+i(A+B)/(A-B)=-m` — independently confirmed exact.
- `s=(m-i)/(m+i)` under `m\mapsto-m`: `(-m-i)/(-m+i)=(m+i)/(m-i)=1/s` — independently confirmed, and recognized as an instance of the general Cayley identity `s(-m)=1/s(m)`.
- `W_\theta=A+e^{i\theta}B\mapsto B+e^{i\theta}A=e^{i\theta}(A+e^{-i\theta}B)=e^{i\theta}W_{-\theta}` — confirmed, correctly identifying the `e^{i\theta}` prefactor as a harmless `z`-independent characteristic gauge.

The entry's most substantive move is computing the *composite* parity of `\Re\log s` and `\Im\log s` under both `\mathscr R` (which negates `L_s` entirely: `u\mapsto-u,v\mapsto-v`) and the induced conjugation `\mathscr C_s:=\mathscr R\circ\kappa` (where `\kappa:\zeta\mapsto\bar\zeta` is the spectral-reflection map from v13.705, giving `u\mapsto u,v\mapsto-v` after composing both maps). This audit independently recomputed this composite: applying `\kappa` first sends `(u,v)\mapsto(-u,v)` (per v13.705's proved law), then applying `\mathscr R` (which negates both coordinates) sends `(-u,v)\mapsto(u,-v)`, i.e. `\mathscr C_s:L_s\mapsto\overline{L_s}` exactly as claimed — confirmed independently.

The resulting parity assignment `\Re L_s:(\mathscr R,\mathscr C_s)=(-,+)`, `\Im L_s:(-,-)` was then checked against this audit's own independently-verified Round 80 character table for the cone boost logarithm `\ell=s_{\rm cone}+i\phi` (note: the project's own `s` clashes notationally with Suzuki's Cayley `s`; this audit uses `s_{\rm cone}` here to keep them apart, a distinction the entry itself does not flag but should for future entries). From v13.703 (independently re-derived in Round 80): `F:\ell\mapsto-\ell` gives `\Re\ell:(F,C)=(-,\cdot)`, `\Im\ell:(-,\cdot)`; `C:\ell\mapsto\bar\ell` gives `\Re\ell:(\cdot,+)`, `\Im\ell:(\cdot,-)`. Combined: `\Re\ell:(-,+)`, `\Im\ell:(-,-)` — an **exact match** to the independently recomputed Suzuki-side parities above. **PASS, exact**, and this is genuine, correctly-derived progress: it resolves the boost half of the four-character correspondence that v13.705 had explicitly left open.

The `\mathscr R`-invariance of the cross-ratio `\Delta_{0/\pi}=m(z)/m(z_*)` (both numerator and denominator flip sign under `m\mapsto-m`, so the ratio is unchanged) was independently confirmed and is a satisfying explanation for why v13.705's `\Delta`-based analysis alone could not distinguish `\tau` from `\ell`: the normalization used to build `\Delta` exactly quotients out the sign datum that carries the distinguishing information. This is a correct and useful piece of self-diagnosis, not an unfounded excuse.

The normalization guardrail in Section 8 (distinguishing the result, which is proved in the project's own stabilized `W_0/W_\pi=im` convention, from the separate, still-open question of whether this literally equals Suzuki's own printed `s_A^{Suz}` under a fully fixed abstract boundary triple per v13.647) is accurate and consistent with this audit's own understanding of the v13.647 normalization gate from earlier rounds. **PASS.**

## 3. Summary

| Entry | Claim | Verification | Outcome |
|---|---|---|---|
| v13.705 | Cayley transform conjugation-inversion law `s(\bar\zeta)=1/\overline{s(\zeta)}`; parity-pattern match with cone `FC` on `\ell`; explicit list of unproved stronger identifications | independent hand derivation + sympy (exact) + numeric (2000 trials, ~1e-15) + branch-safe log check | **PASS, exact** |
| v13.706 | Deficiency-channel reflection `\mathscr R` gives `m\mapsto-m`, `s\mapsto s^{-1}`; induced conjugation `\mathscr C_s` completes the parity match `\Re\log s\leftrightarrow\Re\ell`, `\Im\log s\leftrightarrow\Im\ell`; cross-ratio `\Delta` is `\mathscr R`-invariant | independent re-derivation of the full chain, cross-checked against this audit's own Round 80 character table | **PASS, exact — resolves the boost half of the open four-character correspondence** |

## 4. Assessment

This is a clean, genuinely productive two-entry round that makes real progress connecting the newly-audited continuous-group-theory machinery (Round 80) to the project's actual Suzuki/Kreĭn analytic content, rather than letting the two threads run in parallel without contact. The key discipline that makes this trustworthy: at every step, the entries distinguish a **proved transformation-law match** (which is what was actually derived) from a **claimed operator/object identity** (which was not), and v13.706 explicitly resolves exactly the piece v13.705 left open (the boost-torus half of the four-character table) via a natural, independently-motivated construction (the canonical deficiency-pair reflection already used elsewhere in the project, e.g. the reflection-symmetry checks of Round 77/78) rather than an ad hoc device introduced just to force a match.

One small presentational note for the source thread, not a correctness issue: v13.706 reuses the symbol `s` for both the Suzuki Cayley variable and (implicitly, via the cone's own `\ell=s+i\phi` notation from v13.703) the cone's real rapidity coordinate. The two are properly distinguished by context in both entries, and this audit found no place where the collision actually caused an error, but given this project's repeated history of exactly this kind of notational collision causing real confusion later (`H_n` vs. `H_{\rm harm}`, the four-round Corollary 1.6 citation dispute), it is worth flagging now while it is still costless to rename one of them in a future entry.

The remaining open piece, correctly identified in v13.706 §11, is the `\Re\tau,\Im\tau` (scale) half of the four-character correspondence, with the bulk relative determinant `\Delta^{bulk}` and the common characteristic gauge factor named as the natural next candidates. No claim is made in either entry that this bridges to a Suzuki positivity or RH-relevant consequence, which is the correct scope at this stage.

## 5. Final freshness check

`git fetch origin master` immediately before this commit: HEAD still at `d053ed3`. No new commits landed while writing this entry. `git ls-tree` confirms v13.707 remains free.
